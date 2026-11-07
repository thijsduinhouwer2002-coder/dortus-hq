import { browser, expect } from "@wdio/globals";
import * as fs from "fs";
import { LEAF, SHOTS, checkVorm, klik, knop, laatsteWorp, leesBestand, markeer, openNote, readRolls, readVenster, vervang, waitForRolls, waitForVenster, waitVensterDicht } from "./dicemod-hulp.mjs";

// dice-mod in de echte Obsidian, in de leesweergave: Replace, en Enter op de gefocuste worp.
// De hulpfuncties en de uitleg over de notities staan in dicemod-hulp.mjs.
describe("Rollwright: dice-mod met Replace in de leesweergave en met Enter", function () {
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

	it("Leesweergave: Replace verandert het bestand direct", async function () {
		await openNote("Vervangen lezen.md", "preview");
		const { na } = await vervang(".markdown-reading-view", "Vervangen lezen.md", "m6-venster-lezen.png");
		expect(na).toContain("Worp: 3d100 + 12 -> [");
		await browser.saveScreenshot(`${SHOTS}/m7-na-replace-lezen.png`);
	});

	it("Enter op de gefocuste worp rolt niet opnieuw maar opent het venster", async function () {
		// src/ui/widget.ts: een keydown met Enter roept dezelfde handeling aan als een klik.
		// In de leesweergave, zodat de editor de toets niet als nieuwe regel kan lezen.
		await openNote("Enter.md", "preview");
		const view = ".markdown-reading-view";
		const voor = await leesBestand("Enter.md");
		console.log("Enter.md VOOR:", JSON.stringify(voor));
		const rolls = await waitForRolls(view, 1);
		const historieVoor = await laatsteWorp();
		await markeer(view, 0);
		const focus = await browser.execute((sel) => {
			const el = document.querySelector(`${sel} .rollwright-roll`);
			el?.focus();
			return document.activeElement === el;
		}, `${LEAF} ${view}`);
		console.log("WORP GEFOCUST:", focus);
		expect(focus).toBe(true);
		await browser.keys(["Enter"]);
		await browser.pause(300);
		const venster = await waitForVenster();
		await browser.saveScreenshot(`${SHOTS}/m9-venster-enter.png`);
		const na = await readRolls(view);
		console.log("WORP VOOR EN NA ENTER:", JSON.stringify(rolls[0]), JSON.stringify(na[0]));
		expect(na[0].old).toBe(true);
		expect(na[0].value).toBe(rolls[0].value);
		expect(String(checkVorm(venster.tekst))).toBe(rolls[0].value);
		const historieNa = await laatsteWorp();
		console.log("LAATSTE WORP IN GESCHIEDENIS VOOR EN NA:", historieVoor, historieNa);
		expect(historieNa).toBe(historieVoor);
		await knop("Cancel");
		await waitVensterDicht();
		const bestand = await leesBestand("Enter.md");
		console.log("Enter.md NA:", JSON.stringify(bestand));
		expect(bestand).toBe(voor);
	});
});
