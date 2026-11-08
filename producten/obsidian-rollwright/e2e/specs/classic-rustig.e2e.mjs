import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Classic rustig (Daan 8 nov, ja van Thijs 14:58, 0.3.2): Classic is het gratis deel en mag zelf geen skin lijken.
// Een NAT 20 in Classic is plat: gouden rand van 1,5 px, geen verloop, geen schaduw, geen vonk (::after),
// en een rechte stempel zonder schaduw. Een NAT 1 hetzelfde in rood. De betaalde skins houden hun effecten.
// De crit wordt afgedwongen met Math.random, zoals in crit.e2e.mjs; de skin is een klasse op body, zoals in skins.e2e.mjs.
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";

async function zetWillekeur(waarde) {
	await browser.execute((waarde) => {
		if (!window.__e2eRandom) window.__e2eRandom = Math.random;
		Math.random = waarde === null ? window.__e2eRandom : () => waarde;
	}, waarde);
}

async function zet(skin, donker) {
	await browser.execute((skin, donker) => {
		for (const c of Array.from(document.body.classList)) if (c.startsWith("rollwright-skin-")) document.body.classList.remove(c);
		document.body.classList.add(`rollwright-skin-${skin}`);
		document.body.classList.toggle("theme-dark", donker);
		document.body.classList.toggle("theme-light", !donker);
	}, skin, donker);
	await browser.pause(400);
}

async function klikTot(i, klasse) {
	await browser.waitUntil(async () => browser.execute((sel, i, klasse) => {
		const el = document.querySelectorAll(`${sel} .rollwright-roll`)[i];
		if (!el || !el.isConnected || !el.querySelector(".rollwright-value")) return false;
		if (el.classList.contains("rollwright-rolled") && el.classList.contains(klasse)) return true;
		el.click();
		return false;
	}, LEAF, i, klasse), { timeout: 8000, interval: 1000, timeoutMsg: `worp ${i} kreeg geen ${klasse}` });
	await browser.pause(1300);
}

async function meet(i) {
	return browser.execute((sel, i) => {
		const el = document.querySelectorAll(`${sel} .rollwright-roll`)[i];
		const stempel = el?.querySelector(".rollwright-stamp");
		const s = el ? getComputedStyle(el) : null;
		const st = stempel ? getComputedStyle(stempel) : null;
		return {
			klassen: el?.className ?? "",
			rand: s?.borderTopWidth ?? "",
			randKleur: s?.borderTopColor ?? "",
			schaduw: s?.boxShadow ?? "",
			verloop: s?.backgroundImage ?? "",
			achtergrond: s?.backgroundColor ?? "",
			vonk: el ? getComputedStyle(el, "::after").content : "",
			stempel: stempel?.textContent ?? "",
			stempelDraai: st?.transform ?? "",
			stempelSchaduw: st?.boxShadow ?? "",
			stempelLetter: st ? parseFloat(st.fontSize) : 0,
		};
	}, LEAF, i);
}

describe("Rollwright: Classic rustig (0.3.2)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.executeObsidian(async ({ app }) => {
			const file = app.vault.getAbstractFileByPath("Crit.md");
			if (!file) throw new Error("Crit.md niet gevonden");
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(file, { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		});
		await browser.waitUntil(async () => browser.execute((sel) => document.querySelectorAll(`${sel} .rollwright-roll .rollwright-value`).length >= 2, LEAF), {
			timeout: 20000, timeoutMsg: "de worpen in Crit.md kwamen niet",
		});
	});

	after(async function () {
		await zetWillekeur(null);
		await zet("classic", false);
	});

	for (const [naam, waarde, klasse, stempel] of [
		["crit", 0.9999, "rollwright-crit", "NAT 20"],
		["fumble", 0, "rollwright-fumble", "NAT 1"],
	]) {
		it(`een ${naam} in Classic is plat, in licht en donker`, async function () {
			await zet("classic", false);
			await zetWillekeur(waarde);
			await klikTot(0, klasse);
			await zetWillekeur(null);
			for (const donker of [false, true]) {
				await zet("classic", donker);
				const m = await meet(0);
				console.log(`CLASSIC ${naam.toUpperCase()} ${donker ? "DONKER" : "LICHT"}:`, JSON.stringify(m));
				await browser.saveScreenshot(`${SHOTS}/classic-rustig-${naam}-${donker ? "donker" : "licht"}.png`);
				expect(m.klassen).toContain(klasse);
				expect(m.stempel).toBe(stempel);
				// 1.5px wordt op schaal 1 door Chromium afgerond naar 1px (controleur), dus toets de dikte ruim en de kleur echt.
				expect(parseFloat(m.rand)).toBeGreaterThanOrEqual(1);
				// Een color-mix() komt terug als color(srgb 0-1), een gewone kleur als rgb(0-255): eerst gelijk trekken.
				const schaal = m.randKleur.startsWith("color(") ? 255 : 1;
				const [r, g, b] = (m.randKleur.match(/[\d.]+/g) ?? []).map(Number).slice(0, 3).map((x) => x * schaal);
				if (naam === "crit") expect(r > b + 40 && g > b + 20).toBe(true); // goud: veel rood en groen, weinig blauw
				else expect(r > g + 40 && r > b + 40).toBe(true); // rood
				expect(m.schaduw).toBe("none");
				expect(m.verloop).toBe("none");
				expect(m.vonk).toBe("none");
				expect(m.stempelDraai).toBe("none");
				expect(m.stempelSchaduw).toBe("none");
				// controleur van Daan: de stempel niet onder ±9 px
				expect(m.stempelLetter).toBeGreaterThanOrEqual(8.5);
			}
		});
	}

	it("de betaalde skins houden hun effecten bij een NAT 20", async function () {
		await zet("classic", false);
		await zetWillekeur(0.9999);
		await klikTot(0, "rollwright-crit");
		await zetWillekeur(null);
		const classic = await meet(0);
		for (const skin of ["parchment", "arcane"]) {
			await zet(skin, false);
			const m = await meet(0);
			console.log(`${skin.toUpperCase()} CRIT:`, JSON.stringify(m));
			await browser.saveScreenshot(`${SHOTS}/classic-rustig-naast-${skin}.png`);
			const effect = m.schaduw !== "none" || m.verloop !== "none";
			expect(effect).toBe(true);
			expect(JSON.stringify([m.schaduw, m.verloop, m.achtergrond])).not.toBe(JSON.stringify([classic.schaduw, classic.verloop, classic.achtergrond]));
		}
	});
});
