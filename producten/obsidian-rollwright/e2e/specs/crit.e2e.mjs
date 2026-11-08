import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Ontwerp-v2 klus 3 en 3b in de echte Obsidian: een echte crit en fumble, afgedwongen door Math.random
// in het venster vast te zetten (de plugin haalt zijn willekeur uit Math.random, src/engine/random.ts).
// Controleert de klasse en de stempel op het vakje en op het nieuwste item in het logboek, en maakt
// schermafbeeldingen in licht en donker voor Daan (tak schermen).
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";
const PANEEL = '.workspace-leaf-content[data-type="rollwright-history"]';

async function zetWillekeur(waarde) {
	await browser.execute((waarde) => {
		if (!window.__e2eRandom) window.__e2eRandom = Math.random;
		Math.random = waarde === null ? window.__e2eRandom : () => waarde;
	}, waarde);
}

async function zetThema(donker) {
	await browser.execute((donker) => {
		document.body.classList.toggle("theme-dark", donker);
		document.body.classList.toggle("theme-light", !donker);
	}, donker);
}

/** Klikt worp i en wacht tot het vakje de verwachte klasse heeft. De klasse komt ±460 ms na de klik
 *  (klus 2d), dus tussen twee pogingen zit ruim meer, anders klikt hij steeds net voor het landen. */
async function klikTot(i, klasse) {
	await browser.waitUntil(async () => browser.execute((sel, i, klasse) => {
		const el = document.querySelectorAll(`${sel} .rollwright-roll`)[i];
		if (!el || !el.isConnected || !el.querySelector(".rollwright-value")) return false;
		if (el.classList.contains("rollwright-rolled") && el.classList.contains(klasse)) return true;
		el.click();
		return false;
	}, LEAF, i, klasse), { timeout: 8000, interval: 1000, timeoutMsg: `worp ${i} kreeg geen ${klasse}` });
}

async function lees(i) {
	return browser.execute((sel, i, paneel) => {
		const el = document.querySelectorAll(`${sel} .rollwright-roll`)[i];
		const item = document.querySelector(`${paneel} .rollwright-history-item`);
		return {
			klassen: el?.className ?? "",
			waarde: (el?.querySelector(".rollwright-value")?.textContent ?? "").split(String.fromCharCode(0x200b)).join(""),
			stempel: el?.querySelector(".rollwright-stamp")?.textContent ?? "",
			logKlassen: item?.className ?? "",
			logUitkomst: item?.querySelector(".rollwright-history-result")?.textContent ?? "",
			logStempel: item?.querySelector(".rollwright-stamp")?.textContent ?? "",
		};
	}, LEAF, i, PANEEL);
}

describe("Rollwright: echte crit en fumble (ontwerp-v2 klus 3 en 3b)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.executeObsidian(async ({ app }) => {
			const plugin = app.plugins.plugins.rollwright;
			await plugin.clearHistory();
			await plugin.openHistory();
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
		await zetThema(false);
	});

	for (const [naam, waarde, klasse, d20Stempel, d6Stempel, d20Waarde] of [
		["crit", 0.9999, "rollwright-crit", "NAT 20", "MAX", "25"],
		["fumble", 0, "rollwright-fumble", "NAT 1", "MIN", "6"],
	]) {
		it(`een ${naam}: klasse en stempel op het vakje en in het logboek`, async function () {
			await zetThema(false);
			await zetWillekeur(waarde);
			await klikTot(1, klasse);
			const schade = await lees(1);
			await klikTot(0, klasse);
			await browser.pause(1300);
			const aanval = await lees(0);
			console.log(`${naam.toUpperCase()} SCHADE:`, JSON.stringify(schade));
			console.log(`${naam.toUpperCase()} AANVAL:`, JSON.stringify(aanval));
			await browser.saveScreenshot(`${SHOTS}/crit-${naam}-licht.png`);
			await zetThema(true);
			await browser.pause(300);
			await browser.saveScreenshot(`${SHOTS}/crit-${naam}-donker.png`);
			await zetThema(false);
			await zetWillekeur(null);

			expect(schade.klassen).toContain(klasse);
			expect(schade.stempel).toBe(d6Stempel);
			expect(aanval.klassen).toContain(klasse);
			expect(aanval.waarde.trim()).toBe(d20Waarde);
			expect(aanval.stempel).toBe(d20Stempel);
			expect(aanval.logKlassen).toContain(klasse);
			expect(aanval.logStempel).toBe(d20Stempel);
			expect(aanval.logUitkomst).toContain(d20Waarde);
		});
	}
});
