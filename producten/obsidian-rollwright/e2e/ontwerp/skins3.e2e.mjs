import { browser } from "@wdio/globals";
import * as fs from "fs";

// Daan, run 18: lijstplaatje 3. Dezelfde demonotitie in Classic, Parchment en Arcane, licht en donker,
// groot en scherp (zoom 1.5), alleen het notitievlak. De skin is alleen CSS, dus wisselen gooit niet opnieuw.
const SHOTS = "screenshots";
const NOTE = "Demo/Session 12.md";
const LEAF = ".workspace-leaf.mod-active";

async function zet(skin, donker) {
	await browser.execute((skin, donker) => {
		for (const c of Array.from(document.body.classList)) if (c.startsWith("rollwright-skin-")) document.body.classList.remove(c);
		document.body.classList.add(`rollwright-skin-${skin}`);
		document.body.classList.toggle("theme-dark", donker);
		document.body.classList.toggle("theme-light", !donker);
	}, skin, donker);
	await browser.pause(700);
}

describe("Daan: drie skins voor het lijstplaatje", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.executeObsidian(async ({ app }, path) => {
			app.workspace.leftSplit?.collapse();
			app.workspace.rightSplit?.collapse();
			const file = app.vault.getAbstractFileByPath(path);
			if (!file) throw new Error(`notitie ${path} niet gevonden`);
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(file, { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		}, NOTE);
		await browser.execute(() => { try { require("electron").webFrame.setZoomFactor(1.5); } catch (e) { console.log("zoom", e); } });
		await browser.waitUntil(async () => browser.execute((sel) => {
			const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`));
			return r.length >= 6 && r.every((e) => (e.textContent ?? "").trim() !== "");
		}, LEAF), { timeout: 20000, timeoutMsg: "geen worpen in de demonotitie" });
		// Muis weg, geen tooltip; wachten tot alle bewegingen klaar zijn.
		await browser.execute(() => document.activeElement?.blur?.());
		await browser.pause(1500);
	});

	for (const donker of [true, false]) {
		for (const skin of ["classic", "parchment", "arcane"]) {
			it(`${skin} ${donker ? "donker" : "licht"}`, async function () {
				await zet(skin, donker);
				const naam = `skins3-${skin}-${donker ? "donker" : "licht"}`;
				const el = await browser.$(`${LEAF} .markdown-preview-view`);
				await el.saveScreenshot(`${SHOTS}/${naam}.png`);
				await browser.saveScreenshot(`${SHOTS}/${naam}-vol.png`);
				const kleur = await browser.execute((sel) => {
					const t = document.querySelector(`${sel} .rollwright-roll`);
					const s = t && getComputedStyle(t);
					return s ? `${s.backgroundColor} | ${s.color} | ${s.borderColor}` : "geen token";
				}, LEAF);
				console.log(`SKINS3 ${naam}: ${kleur}`);
			});
		}
	}
});
