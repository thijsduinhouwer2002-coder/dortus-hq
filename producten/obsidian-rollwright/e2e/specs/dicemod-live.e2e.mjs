import { browser, expect } from "@wdio/globals";
import * as fs from "fs";
import { CODE, LEAF, SHOTS, VORM_ZONDER, blijftGelijk, klik, knop, laatsteWorp, leesBestand, markeer, openNote, readRolls, readVenster, vervang, waitForBestand, waitForRolls, waitForVenster, waitVensterDicht } from "./dicemod-hulp.mjs";

// dice-mod in de echte Obsidian, in Live Preview: Replace, Ctrl-Z, Cancel en Escape, zonder formule, tabel.
// De hulpfuncties en de uitleg over de notities staan in dicemod-hulp.mjs.
describe("Rollwright: dice-mod met Replace in Live Preview", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	afterEach(async function () {
		// Een venster dat open bleef na een mislukte test mag de volgende niet raken.
		if ((await readVenster()) !== null) {
			await browser.keys(["Escape"]);
			await browser.pause(300);
		}
	});

	it("Live Preview: Replace schrijft precies de tekst uit het venster, de rest blijft gelijk", async function () {
		await openNote("Vervangen.md", "source");
		const { voor, na, tekst } = await vervang(".markdown-source-view", "Vervangen.md", "m1-venster-live-preview.png");
		// Alleen de code (met backticks) is vervangen; de regels ervoor en erna zijn gelijk.
		const i = voor.indexOf(CODE);
		expect(na.slice(0, i)).toBe(voor.slice(0, i));
		expect(na.slice(i + tekst.length)).toBe(voor.slice(i + CODE.length));
		const editor = await browser.executeObsidian(({ app }) => app.workspace.activeEditor?.editor?.getValue() ?? null);
		expect(editor).toBe(na);
		await browser.saveScreenshot(`${SHOTS}/m2-na-replace-live-preview.png`);
	});

	it("Live Preview: Ctrl-Z zet de code terug", async function () {
		await openNote("Ongedaan.md", "source");
		const { voor } = await vervang(".markdown-source-view", "Ongedaan.md", "m3-venster-ongedaan.png");
		// Een echte toets: de editor krijgt de focus en Obsidian moet Ctrl-Z zelf als ongedaan maken lezen.
		const gefocust = await browser.executeObsidian(({ app }, sel) => {
			app.workspace.activeEditor?.editor?.focus();
			return document.activeElement?.closest(`${sel} .cm-content`) !== null && document.activeElement !== null;
		}, LEAF);
		console.log("EDITOR GEFOCUST:", gefocust, "EDITOR NU:", JSON.stringify(await browser.executeObsidian(({ app }) => app.workspace.activeEditor?.editor?.getValue() ?? null)));
		expect(gefocust).toBe(true);
		await browser.keys(["Control", "z"]);
		const terug = await waitForBestand("Ongedaan.md", voor, "na Ctrl-Z");
		console.log("Ongedaan.md NA CTRL-Z:", JSON.stringify(terug));
		expect(terug).toContain(CODE);
		// De code toont weer een worp.
		await waitForRolls(".markdown-source-view", 1);
		await browser.saveScreenshot(`${SHOTS}/m4-na-ctrl-z.png`);
	});

	it("Cancel en Escape laten het bestand gelijk", async function () {
		await openNote("Annuleren.md", "source");
		const voor = await leesBestand("Annuleren.md");
		console.log("Annuleren.md VOOR:", JSON.stringify(voor));
		const rolls = await waitForRolls(".markdown-source-view", 1);
		const historieVoor = await laatsteWorp();
		await markeer(".markdown-source-view", 0);

		await klik(".markdown-source-view", 0);
		await waitForVenster();
		await knop("Cancel");
		await waitVensterDicht();

		await klik(".markdown-source-view", 0);
		await waitForVenster();
		await browser.saveScreenshot(`${SHOTS}/m5-venster-voor-escape.png`);
		await browser.keys(["Escape"]);
		await waitVensterDicht();

		// Bewaar wat de editor heeft, en lees dan een seconde lang steeds het bestand: het blijft gelijk.
		await browser.executeObsidian(async ({ app }) => {
			await app.workspace.activeLeaf?.view?.save?.();
		});
		await blijftGelijk("Annuleren.md", voor);
		const na = await leesBestand("Annuleren.md");
		console.log("Annuleren.md NA:", JSON.stringify(na));
		expect(na).toBe(voor);
		// Geen nieuwe worp: hetzelfde element met merkteken, dezelfde uitkomst, niets nieuws in de geschiedenis.
		const rollsNa = await readRolls(".markdown-source-view");
		console.log("WORP VOOR EN NA:", JSON.stringify(rolls[0]), JSON.stringify(rollsNa[0]));
		expect(rollsNa.length).toBe(1);
		expect(rollsNa[0].old).toBe(true);
		expect(rollsNa[0].value).toBe(rolls[0].value);
		const historieNa = await laatsteWorp();
		console.log("LAATSTE WORP IN GESCHIEDENIS VOOR EN NA:", historieVoor, historieNa);
		expect(historieNa).toBe(historieVoor);
		const editor = await browser.executeObsidian(({ app }) => app.workspace.activeEditor?.editor?.getValue() ?? null);
		expect(editor).toBe(voor);
		await waitForRolls(".markdown-source-view", 1);
	});

	it("Live Preview zonder formule: Replace schrijft alleen uitkomst en totaal", async function () {
		// De instelling heet diceModFormula (src/main.ts, regel 35; src/ui/settings.ts, regel 126-127).
		// Alleen in het geheugen uit, niet op schijf; de plugin leest hem bij de klik (src/ui/dice-mod.ts).
		const eerst = await browser.executeObsidian(({ app }) => {
			const plugin = app.plugins.plugins.rollwright;
			const oud = plugin.settings.diceModFormula;
			plugin.settings.diceModFormula = false;
			return oud;
		});
		console.log("diceModFormula WAS:", eerst);
		try {
			await openNote("Zonder formule.md", "source");
			const { na, tekst } = await vervang(".markdown-source-view", "Zonder formule.md", "m10-venster-zonder-formule.png", VORM_ZONDER);
			expect(na).toContain(`Worp: ${tekst} en dan verder.`);
			expect(na.includes("3d100")).toBe(false);
		} finally {
			await browser.executeObsidian(({ app }, oud) => {
				app.plugins.plugins.rollwright.settings.diceModFormula = oud;
			}, eerst);
		}
	});

	it("dice-mod op een tabel schrijft alleen de uitkomst, en Tabellen.md blijft gelijk", async function () {
		const tabelVoor = await browser.executeObsidian(async ({ app }) => {
			const stat = await app.vault.adapter.stat("Tabellen.md");
			return { tekst: await app.vault.adapter.read("Tabellen.md"), mtime: stat?.mtime ?? null, size: stat?.size ?? null };
		});
		console.log("Tabellen.md VOOR: grootte", tabelVoor.size, "mtime", tabelVoor.mtime);
		await openNote("Tabel vervangen.md", "source");
		const path = "Tabel vervangen.md";
		const code = "`dice-mod: [[Tabellen^kleuren]]`";
		const voor = await leesBestand(path);
		console.log(`${path} VOOR:`, JSON.stringify(voor));
		const rolls = await waitForRolls(".markdown-source-view", 1);
		console.log("TABELWORP:", JSON.stringify(rolls));
		await klik(".markdown-source-view", 0);
		const venster = await waitForVenster();
		await browser.saveScreenshot(`${SHOTS}/m8-venster-tabel.png`);
		// Alleen de uitkomst, één kleur uit de tabel, zonder formule of pijl.
		expect(["Rood", "Blauw", "Groen"]).toContain(venster.tekst);
		expect(venster.tekst).toBe(rolls[0].value);
		await knop("Replace");
		await waitVensterDicht();
		const na = await waitForBestand(path, voor.replace(code, venster.tekst), "na Replace op tabel");
		console.log(`${path} NA:`, JSON.stringify(na));
		const regel = na.split("\n").find((r) => r.startsWith("Kleur: "));
		expect(regel).toBe(`Kleur: ${venster.tekst} en dan verder.`);
		expect(na.split("\n").length).toBe(voor.split("\n").length);
		const tabelNa = await browser.executeObsidian(async ({ app }) => {
			const stat = await app.vault.adapter.stat("Tabellen.md");
			return { tekst: await app.vault.adapter.read("Tabellen.md"), mtime: stat?.mtime ?? null, size: stat?.size ?? null };
		});
		console.log("Tabellen.md NA: grootte", tabelNa.size, "mtime", tabelNa.mtime);
		expect(tabelNa.tekst).toBe(tabelVoor.tekst);
		expect(tabelNa.size).toBe(tabelVoor.size);
		expect(tabelNa.mtime).toBe(tabelVoor.mtime);
	});
});
