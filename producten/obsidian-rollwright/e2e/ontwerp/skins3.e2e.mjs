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
		await browser.executeObsidian(({ app }) => { app.vault.setConfig?.("showInlineTitle", false); });
		await browser.execute(() => {
			try { require("electron").webFrame.setZoomFactor(1.25); } catch (e) { console.log("zoom", e); }
			const st = document.createElement("style");
			st.textContent = ".status-bar{display:none!important}.inline-title{display:none!important}";
			document.head.appendChild(st);
		});
		await browser.waitUntil(async () => browser.execute((sel) => {
			const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`));
			return r.length >= 6 && r.every((e) => (e.textContent ?? "").trim() !== "");
		}, LEAF), { timeout: 20000, timeoutMsg: "geen worpen in de demonotitie" });
		// Loot en de tolwachter trekken met teruglegging: gooi opnieuw tot alles verschillend is (zoals winkel.e2e.mjs).
		for (let poging = 0; poging < 40; poging++) {
			const w = await browser.execute((sel) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`))
				.filter((r) => !r.parentElement?.closest(".rollwright-roll")).map((r) => (r.textContent ?? "").trim()), LEAF);
			const loot = w[4] ?? "";
			const lootGoed = new Set(loot.split(",").map((x) => x.trim())).size === 3;
			const zinnen = (w[5] ?? "").split('"').map((x) => x.trim()).filter((x) => x.length > 3);
			const zinGoed = zinnen.length === 2 && zinnen[0] !== zinnen[1];
			if (lootGoed && zinGoed) break;
			await browser.execute((sel, i) => {
				const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).filter((e) => !e.parentElement?.closest(".rollwright-roll"))[i];
				r?.click();
			}, LEAF, lootGoed ? 5 : 4);
			await browser.pause(700);
		}
		await browser.$(".workspace-ribbon").moveTo().catch(() => {});
		// Muis weg, geen tooltip; wachten tot alle bewegingen klaar zijn.
		await browser.execute(() => document.activeElement?.blur?.());
		await browser.pause(1500);
	});

	for (const donker of [true, false]) {
		for (const skin of ["classic", "parchment", "arcane"]) {
			it(`${skin} ${donker ? "donker" : "licht"}`, async function () {
				await zet(skin, donker);
				const naam = `skins3-${skin}-${donker ? "donker" : "licht"}`;
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
