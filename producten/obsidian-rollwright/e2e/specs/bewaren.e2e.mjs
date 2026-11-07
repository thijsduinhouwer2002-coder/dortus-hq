import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// dice+: bewaart de uitkomst over een herstart van Obsidian, dice-: en dice: niet.
// Bewaren.md heeft drie worpen van 1d1000000, zodat een toevallig gelijke nieuwe worp vrijwel onmogelijk is.
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";

async function openNote(path, mode) {
	await browser.executeObsidian(async ({ app }, path, mode) => {
		const file = app.vault.getAbstractFileByPath(path);
		if (!file) throw new Error(`notitie ${path} niet gevonden`);
		const leaf = app.workspace.getLeaf(false);
		const state = mode === "preview" ? { mode: "preview" } : { mode: "source", source: false };
		await leaf.openFile(file, { state });
		app.workspace.setActiveLeaf(leaf, { focus: true });
	}, path, mode);
}

async function readValues(view) {
	return browser.execute((sel) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`))
		.map((r) => ({
			value: (r.querySelector(".rollwright-value")?.textContent ?? "").trim(),
			old: r.querySelector(".rollwright-value")?.getAttribute("data-e2e-oud") === "1",
			error: r.getAttribute("data-rollwright-error") ?? "",
		})), `${LEAF} ${view}`);
}

async function waitForValues(view) {
	let last = [];
	await browser.waitUntil(async () => {
		last = await readValues(view);
		return last.length === 3 && last.every((r) => r.value !== "" && !r.old);
	}, { timeout: 20000, timeoutMsg: `geen 3 uitkomsten in ${view}` }).catch((e) => {
		console.log("WORPEN TOT NU:", JSON.stringify(last));
		throw e;
	});
	for (const r of last) expect(r.error).toBe("");
	return last.map((r) => r.value);
}

/** Bewaarde uitkomsten in de plugindata, zoals ze op schijf staan. */
async function keptOnDisk() {
	return browser.executeObsidian(async ({ app }) => {
		const data = await app.plugins.plugins.rollwright?.loadData();
		return (data?.keptResults ?? []).length;
	});
}

/** Herstart Obsidian met dezelfde kluis en open Bewaren.md opnieuw. */
async function herstart(mode) {
	// Geef het opslaan van de plugindata even de tijd.
	await browser.pause(1500);
	await browser.reloadObsidian();
	await openNote("Bewaren.md", mode);
}

describe("Rollwright: dice+ bewaart over een herstart in de echte Obsidian", function () {
	let eerst;

	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("drie worpen, en dice+ staat in de plugindata", async function () {
		await openNote("Bewaren.md", "preview");
		eerst = await waitForValues(".markdown-reading-view");
		console.log("EERSTE WORPEN (dice+, dice-, dice):", JSON.stringify(eerst));
		await browser.pause(1500);
		const kept = await keptOnDisk();
		console.log("BEWAARD OP SCHIJF:", kept);
		expect(kept).toBeGreaterThanOrEqual(1);
		await browser.saveScreenshot(`${SHOTS}/b1-bewaren-voor-herstart.png`);
	});

	it("na een herstart is alleen de dice+ uitkomst dezelfde", async function () {
		await herstart("preview");
		const na = await waitForValues(".markdown-reading-view");
		console.log("NA HERSTART:", JSON.stringify(na), "EERST:", JSON.stringify(eerst));
		await browser.saveScreenshot(`${SHOTS}/b2-bewaren-na-herstart.png`);
		expect(na[0]).toBe(eerst[0]);
		expect(na[1]).not.toBe(eerst[1]);
		expect(na[2]).not.toBe(eerst[2]);
	});

	it("Live Preview toont dezelfde bewaarde uitkomst", async function () {
		await openNote("Bewaren.md", "source");
		const lp = await waitForValues(".markdown-source-view");
		console.log("LIVE PREVIEW NA HERSTART:", JSON.stringify(lp));
		expect(lp[0]).toBe(eerst[0]);
	});

	it("een klik op dice+ rolt opnieuw en ook die uitkomst blijft na een herstart", async function () {
		await openNote("Bewaren.md", "preview");
		await waitForValues(".markdown-reading-view");
		await browser.execute((sel) => {
			const v = document.querySelector(`${sel} .rollwright-roll .rollwright-value`);
			v?.setAttribute("data-e2e-oud", "1");
			document.querySelector(`${sel} .rollwright-roll`)?.click();
		}, `${LEAF} .markdown-reading-view`);
		const geklikt = await waitForValues(".markdown-reading-view");
		console.log("NA KLIK:", JSON.stringify(geklikt));
		expect(geklikt[0]).not.toBe(eerst[0]);
		await herstart("preview");
		const na = await waitForValues(".markdown-reading-view");
		console.log("NA KLIK EN HERSTART:", JSON.stringify(na));
		await browser.saveScreenshot(`${SHOTS}/b3-klik-en-herstart.png`);
		expect(na[0]).toBe(geklikt[0]);
		expect(na[1]).not.toBe(geklikt[1]);
	});
});
