import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Keuring 0.3.4, Daans kan-punt (9 nov 12:50 UTC): de ringen rond het NAT 20-token in Parchment raakten
// het woord ervoor ("Bite"). De ringen lopen 6px buiten het token; Daan gaf het crit-token in Parchment
// `margin-inline: 6px`. Deze spec zet een echte NAT 20 tussen twee woorden, meet de ruimte tot het woord
// ervoor en erna, en maakt plaatjes voor Daans akkoord 0.3.5 (licht en donker thema).
const SHOTS = "screenshots";
const PAD = "Parchment nat20.md";
const TEKST = "# Wolf\n\nBite `dice: 1d20+5` hits the knight.\n";
// Alleen de lezen-weergave: de verborgen Live Preview van hetzelfde blad heeft ook een token, met maat 0 (run 42637689172).
const LEAF = ".workspace-leaf.mod-active .markdown-reading-view";

async function zetWillekeur(waarde) {
	await browser.execute((waarde) => {
		if (!window.__e2eRandom) window.__e2eRandom = Math.random;
		Math.random = waarde === null ? window.__e2eRandom : () => waarde;
	}, waarde);
}

async function zet(veranderingen, donker) {
	await browser.executeObsidian(({ app }, veranderingen, donker) => {
		document.body.classList.toggle("theme-dark", donker);
		document.body.classList.toggle("theme-light", !donker);
		const plugin = app.plugins.plugins.rollwright;
		Object.assign(plugin.settings, veranderingen);
		plugin.applySkin();
	}, veranderingen, donker);
	await browser.pause(800);
}

/** Klikt tot het token een crit is (de klasse komt ±460 ms na de klik, klus 2d). */
async function klikTotCrit() {
	await browser.waitUntil(async () => browser.execute((sel) => {
		const el = document.querySelector(`${sel} .rollwright-roll`);
		if (!el || !el.isConnected || !el.querySelector(".rollwright-value")) return false;
		if (el.classList.contains("rollwright-rolled") && el.classList.contains("rollwright-crit")) return true;
		el.click();
		return false;
	}, LEAF), { timeout: 8000, interval: 1000, timeoutMsg: "het token werd geen NAT 20" });
}

/** Ruimte in px tussen het token en de tekst ervoor en erna, plus de berekende marge. */
async function meet() {
	return browser.execute((sel) => {
		const el = document.querySelector(`${sel} .rollwright-roll`);
		const r = el.getBoundingClientRect();
		// Zoek "Bite" en "hits" in de tekstnodes van de alinea zelf (niet in het token): het token kan in
		// een eigen omhulsel staan, dus previousSibling is niet altijd de tekst (run 42634862383).
		// Het kleinste omhulsel boven het token dat beide woorden bevat (in lezen niet altijd een <p>, run 42636416109).
		let p = el.parentElement;
		while (p && !(p.textContent.includes("Bite") && p.textContent.includes("hits"))) p = p.parentElement;
		if (!p) return { klassen: el.className, voorTekst: "", naTekst: "", html: (el.parentElement?.outerHTML ?? "").slice(0, 600) };
		const walker = document.createTreeWalker(p, NodeFilter.SHOW_TEXT);
		let bite = null, hits = null;
		for (let n = walker.nextNode(); n; n = walker.nextNode()) {
			if (el.contains(n)) continue;
			if (!bite && n.textContent.includes("Bite")) bite = n;
			if (!hits && n.textContent.includes("hits")) hits = n;
		}
		const rect = (node, vanaf, tot) => {
			const range = document.createRange();
			range.setStart(node, vanaf);
			range.setEnd(node, tot);
			return range.getBoundingClientRect();
		};
		const voorTekst = bite?.textContent ?? "";
		const naTekst = hits?.textContent ?? "";
		if (!bite || !hits) return { klassen: el.className, voorTekst, naTekst, html: p.outerHTML.slice(0, 600) };
		// Laatste letter van "Bite" en eerste letter van "hits" (de spatie telt mee als ruimte).
		const eindBite = voorTekst.indexOf("Bite") + 4;
		const rVoor = rect(bite, eindBite - 1, eindBite);
		const beginHits = naTekst.indexOf("hits");
		const rNa = rect(hits, beginHits, beginHits + 1);
		const s = getComputedStyle(el);
		return {
			klassen: el.className,
			titel: document.querySelector(sel).closest(".workspace-leaf")?.querySelector(".view-header-title")?.textContent ?? "",
			wereld: !!el.closest(".rollwright-world"),
			voorTekst, naTekst,
			margeLinks: s.marginLeft, margeRechts: s.marginRight,
			ruimteVoor: r.left - rVoor.right,
			ruimteNa: rNa.left - r.right,
			token: { x: r.left, y: r.top, b: r.width, h: r.height },
		};
	}, LEAF);
}

describe("Rollwright: NAT 20 in Parchment naast een woord (keuring 0.3.4)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.executeObsidian(async ({ app }, PAD, TEKST) => {
			const bestaand = app.vault.getAbstractFileByPath(PAD);
			if (bestaand) await app.vault.modify(bestaand, TEKST);
			else await app.vault.create(PAD, TEKST);
			const leaf = app.workspace.getLeaf("tab");
			await leaf.openFile(app.vault.getAbstractFileByPath(PAD), { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		}, PAD, TEKST);
		await browser.waitUntil(async () => browser.execute((sel) => !!document.querySelector(`${sel} .rollwright-roll .rollwright-value`), LEAF), {
			timeout: 20000, timeoutMsg: "de worp in de notitie kwam niet",
		});
	});

	after(async function () {
		await zetWillekeur(null);
		await zet({ skin: "classic", licenseKey: "", licenseCheckedAt: 0, noteWorld: "rolls" }, false);
	});

	for (const donker of [false, true]) {
		const thema = donker ? "donker" : "licht";
		it(`${thema} thema: de ringen houden 6px ruimte tot het woord ervoor en erna`, async function () {
			await zet({ skin: "parchment", licenseKey: "E2E-SLEUTEL", licenseCheckedAt: Date.now(), noteWorld: "rolls" }, donker);
			await zetWillekeur(0.9999);
			await klikTotCrit();
			await zetWillekeur(null);
			// Wacht tot de zegeldruk en de ringen (rwp-randen) op hun grootst zijn geweest en stilstaan.
			await browser.pause(1500);
			const m = await meet();
			console.log(`PARCHMENT NAT20 ${thema}:`, JSON.stringify(m));
			await browser.saveScreenshot(`${SHOTS}/parchment-nat20-${thema}.png`);

			expect(m.titel).toBe("Parchment nat20");
			expect(m.klassen).toContain("rollwright-crit");
			expect(m.wereld).toBe(true);
			expect(m.voorTekst).toContain("Bite");
			expect(m.naTekst).toContain("hits");
			expect(m.margeLinks).toBe("6px");
			expect(m.margeRechts).toBe("6px");
			// De ringen lopen 6px buiten het token; de letter ervoor en erna staat daar buiten.
			expect(m.token.b).toBeGreaterThan(0);
			expect(m.ruimteVoor).toBeGreaterThanOrEqual(6);
			expect(m.ruimteNa).toBeGreaterThanOrEqual(6);
		});
	}
});
