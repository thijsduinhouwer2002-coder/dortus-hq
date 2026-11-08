import { browser, expect } from "@wdio/globals";
import * as fs from "fs";
import { LEAF, SHOTS, blijftGelijk, leesBestand, openNote, readVenster } from "./dicemod-hulp.mjs";

// dice-mod in een ingevoegde notitie (![[...]]) in de leesweergave. De worp staat er wel, maar een
// klik mag niets vervangen: de plugin zou anders in de verkeerde notitie schrijven. Hij toont dan de
// melding EMBED_NOTICE uit src/ui/dice-mod.ts (readingModifier) en opent geen vervangvenster.
const MELDING = "A dice-mod code in an embedded note cannot be replaced here. Open that note to replace it.";
const VIEW = ".markdown-reading-view";
const HOST = "Met invoeging dicemod.md";
const INGEVOEGD = "Ingevoegd dicemod.md";

async function worpInInvoeging() {
	return browser.execute((sel) => {
		const r = document.querySelector(`${sel} .internal-embed .rollwright-roll, ${sel} .markdown-embed .rollwright-roll`);
		if (!r) return null;
		return { tekst: (r.textContent ?? "").trim(), fout: r.getAttribute("data-rollwright-error") ?? "" };
	}, `${LEAF} ${VIEW}`);
}

describe("Rollwright: dice-mod in een ingevoegde notitie", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("Een klik toont de melding, opent geen venster en verandert geen bestand", async function () {
		const hostVoor = await leesBestand(HOST);
		const ingevoegdVoor = await leesBestand(INGEVOEGD);
		await openNote(HOST, "preview");
		let worp = null;
		await browser.waitUntil(async () => {
			worp = await worpInInvoeging();
			return worp !== null && worp.tekst !== "";
		}, { timeout: 20000, timeoutMsg: "geen worp in de ingevoegde notitie" });
		console.log("WORP IN INVOEGING:", JSON.stringify(worp));
		expect(worp.fout).toBe("");
		// Oude meldingen weg, zodat alleen de melding van deze klik telt.
		await browser.execute(() => document.querySelectorAll(".notice").forEach((n) => n.remove()));
		await browser.execute((sel) => {
			const r = document.querySelector(`${sel} .internal-embed .rollwright-roll, ${sel} .markdown-embed .rollwright-roll`);
			r?.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
		}, `${LEAF} ${VIEW}`);
		let meldingen = [];
		await browser.waitUntil(async () => {
			meldingen = await browser.execute(() => Array.from(document.querySelectorAll(".notice")).map((n) => (n.textContent ?? "").trim()));
			return meldingen.length > 0;
		}, { timeout: 5000, timeoutMsg: "geen melding na de klik" }).catch(() => {});
		console.log("MELDINGEN NA KLIK:", JSON.stringify(meldingen));
		await browser.saveScreenshot(`${SHOTS}/m10-ingevoegd-melding.png`);
		expect(meldingen).toContain(MELDING);
		const venster = await readVenster();
		console.log("VENSTER NA KLIK:", JSON.stringify(venster));
		expect(venster).toBe(null);
		await blijftGelijk(INGEVOEGD, ingevoegdVoor);
		await blijftGelijk(HOST, hostVoor);
	});
});
