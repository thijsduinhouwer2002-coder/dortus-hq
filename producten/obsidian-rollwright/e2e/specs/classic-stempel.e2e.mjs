import { browser, expect } from "@wdio/globals";

// Daan, kan-punt 1 (ontwerp.md, 8 nov): in Classic verscheen de stempel al terwijl het cijfer nog doortelde,
// dus even stond "NAT 20" boven een 1 (GIF-opname, 446 tot 646 ms). Nu: geen zichtbare stempel zolang er
// geteld wordt (data-rollwright-tick op het getal), wel een stempel als het getal geland is.
// De meting gebeurt in de pagina zelf, elk beeld (requestAnimationFrame), vanaf de klik tot 800 ms na de laatste tel.
// De crit wordt afgedwongen met Math.random, zoals in crit.e2e.mjs en classic-rustig.e2e.mjs.
const LEAF = ".workspace-leaf.mod-active";

async function zetClassic() {
	await browser.execute(() => {
		for (const c of Array.from(document.body.classList)) if (c.startsWith("rollwright-skin-")) document.body.classList.remove(c);
		document.body.classList.add("rollwright-skin-classic");
	});
	await browser.pause(300);
}

/** Klikt worp i met een vaste Math.random en meet elk beeld: telt hij nog, en hoe zichtbaar is de stempel. */
async function klikEnMeet(i, waarde) {
	return browser.executeAsync((sel, i, waarde, klaar) => {
		const echt = Math.random;
		Math.random = () => waarde;
		// Alleen worpen die je ziet. Run 42539754760: worp 0 van het blad zat in de verborgen bronweergave
		// (.markdown-source-view, display none, want de notitie staat in lezen); daar loopt geen animatie.
		const zichtbaar = () => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).filter((e) => e.checkVisibility());
		const el = zichtbaar()[i];
		if (!el) {
			Math.random = echt;
			klaar({ fout: "geen worp" });
			return;
		}
		const beelden = [];
		const start = performance.now();
		el.click();
		const kijk = () => {
			const t = performance.now() - start;
			const roll = zichtbaar()[i];
			const stempel = roll?.querySelector(":scope > .rollwright-stamp");
			const waardeEl = roll?.querySelector(".rollwright-value");
			const st = stempel ? getComputedStyle(stempel) : null;
			beelden.push({
				t: Math.round(t),
				telt: waardeEl?.hasAttribute("data-rollwright-tick") ?? false,
				getal: waardeEl?.getAttribute("data-rollwright-tick") ?? waardeEl?.textContent ?? "",
				stempel: stempel?.textContent ?? "",
				zicht: st && st.display !== "none" && st.visibility !== "hidden" ? Number(st.opacity) : 0,
				// Run 42535424206: de opacity bleef in CI ook na 1,2 s op 0 (beelden maar 15 per seconde, de animatie
				// liep daar niet zichtbaar door). Daarom ook de animatie zelf: vertraging en of hij nog wacht.
				anim: (stempel?.getAnimations?.() ?? []).map((a) => ({ naam: a.animationName ?? "", wacht: a.effect?.getComputedTiming().progress === null && (a.currentTime ?? 0) < (a.effect?.getComputedTiming().delay ?? 0), vertraging: a.effect?.getComputedTiming().delay ?? 0, tijd: Math.round(Number(a.currentTime ?? -1)) })),
			});
			// De uitkomst komt pas na het bewaren van de geschiedenis in beeld (widget.ts, showIfNewest), dus niet
			// vanaf de klik tellen maar door tot 800 ms na het laatste getelde beeld (stempel 480 + 160 ms), hooguit 4 s.
			const laatsteTel = beelden.filter((b) => b.telt).at(-1)?.t;
			if (t < 4000 && (laatsteTel === undefined || t < laatsteTel + 800)) requestAnimationFrame(kijk);
			else {
				Math.random = echt;
				// Laat de animaties van de stempel uitlopen, zodat te zien is waar ze eindigen (zichtbaar of niet).
				const eindStempel = roll?.querySelector(":scope > .rollwright-stamp");
				// Run 42536132426: geen animaties en zicht 0 in elk beeld. Waarom precies: de stijl zelf en de ouders.
				const es = eindStempel ? getComputedStyle(eindStempel) : null;
				const ouders = [];
				for (let p = eindStempel?.parentElement; p && ouders.length < 12; p = p.parentElement) {
					const ps = getComputedStyle(p);
					if (ps.display === "none" || ps.visibility !== "visible" || ps.opacity !== "1") ouders.push(`${p.tagName}.${String(p.className).slice(0, 60)} d=${ps.display} v=${ps.visibility} o=${ps.opacity}`);
				}
				const uitleg = es ? { display: es.display, visibility: es.visibility, opacity: es.opacity, animatie: es.animationName, vertraging: es.animationDelay, duur: es.animationDuration, verbonden: eindStempel.isConnected, zichtbaar: document.visibilityState, ouders, html: roll?.outerHTML.slice(0, 400) } : null;
				for (const a of eindStempel?.getAnimations?.() ?? []) a.finish();
				const eindZicht = eindStempel ? Number(getComputedStyle(eindStempel).opacity) : 0;
				klaar({ beelden, klassen: roll?.className ?? "", eindZicht, uitleg });
			}
		};
		requestAnimationFrame(kijk);
	}, LEAF, i, waarde);
}

describe("Rollwright: stempel in Classic pas na het doortellen (Daan kan-punt 1)", function () {
	before(async function () {
		await browser.executeObsidian(async ({ app }) => {
			const file = app.vault.getAbstractFileByPath("Crit.md");
			if (!file) throw new Error("Crit.md niet gevonden");
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(file, { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		});
		await browser.waitUntil(async () => browser.execute((sel) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll .rollwright-value`)).some((e) => e.checkVisibility()), LEAF), {
			timeout: 20000, timeoutMsg: "de worpen in Crit.md kwamen niet",
		});
		await zetClassic();
	});

	for (const [naam, waarde, stempel, klasse] of [
		["NAT 20", 0.9999, "NAT 20", "rollwright-crit"],
		["NAT 1", 0, "NAT 1", "rollwright-fumble"],
	]) {
		it(`${naam}: geen zichtbare stempel zolang het getal telt, daarna wel`, async function () {
			// Twee keer: de eerste klik op een verse worp en een tweede klik op een worp die al gerold is.
			for (const keer of [1, 2]) {
				const m = await klikEnMeet(0, waarde);
				expect(m.fout).toBeUndefined();
				const tellend = m.beelden.filter((b) => b.telt);
				const fout = tellend.filter((b) => b.zicht > 0.05);
				console.log(`CLASSIC STEMPEL ${naam} klik ${keer}: ${m.beelden.length} beelden, ${tellend.length} tellend, laatste tel op ${tellend.at(-1)?.t ?? "-"} ms, te vroeg zichtbaar: ${JSON.stringify(fout.slice(0, 5))}`);
				console.log(`CLASSIC STEMPEL ${naam} klik ${keer} verloop: ${JSON.stringify(m.beelden.filter((_, j) => j % 4 === 0))}`);
				// De test zegt alleen iets als er echt geteld is.
				expect(tellend.length).toBeGreaterThan(3);
				expect(fout).toEqual([]);
				const eind = m.beelden.at(-1);
				expect(eind.telt).toBe(false);
				expect(eind.stempel).toBe(stempel);
				console.log(`CLASSIC STEMPEL ${naam} klik ${keer} eind: zicht ${eind.zicht}, na finish ${m.eindZicht}, animaties ${JSON.stringify(eind.anim)}`);
				console.log(`CLASSIC STEMPEL ${naam} klik ${keer} uitleg: klassen ${m.klassen} ${JSON.stringify(m.uitleg)}`);
				// Elk tellend beeld: de stempel-animatie wacht nog (of er is geen zichtbare stempel).
				expect(tellend.filter((b) => b.zicht > 0.05 && !b.anim.some((a) => a.wacht))).toEqual([]);
				// De stempel-animatie wacht minstens tot de landing (460 ms) en eindigt zichtbaar.
				expect(Math.max(0, ...eind.anim.map((a) => a.vertraging))).toBeGreaterThanOrEqual(460);
				expect(m.eindZicht).toBeGreaterThan(0.95);
				expect(m.klassen).toContain(klasse);
				await browser.pause(400);
			}
		});
	}
});
