import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Worpen op tabellen, lijsten, kolommen en een opzoektabel met een geneste worp,
// in de echte Obsidian. De notitie Tabelworpen.md rolt op Tabellen.md.
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";
const KLEUREN = ["Rood", "Blauw", "Groen"];
const VERWACHT = [
	{ naam: "kleur", mag: KLEUREN },
	{ naam: "fruit", mag: ["Appel", "Peer"] },
	{ naam: "dier (kolom Naam)", mag: ["Kat", "Hond"] },
	{ naam: "weer (opzoektabel, 4 rolt op de kleuren)", mag: ["Regen", "Mist", ...KLEUREN] },
];

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

async function readRolls(view) {
	return browser.execute((sel) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).map((r) => ({
		value: (r.querySelector(".rollwright-value")?.textContent ?? "").trim(),
		error: r.getAttribute("data-rollwright-error") ?? "",
	})), `${LEAF} ${view}`);
}

async function waitForRolls(view, n) {
	let last = [];
	await browser.waitUntil(async () => {
		last = await readRolls(view);
		return last.length >= n && last.every((r) => r.value !== "" || r.error !== "");
	}, { timeout: 20000, timeoutMsg: `geen ${n} uitkomsten in ${view}` }).catch((e) => {
		console.log("WORPEN TOT NU:", JSON.stringify(last));
		throw e;
	});
	return last;
}

function check(rolls) {
	expect(rolls.length).toBe(5);
	for (const r of rolls) expect(r.error).toBe("");
	VERWACHT.forEach((v, i) => {
		const ok = v.mag.includes(rolls[i].value);
		if (!ok) console.log(`FOUT BIJ ${v.naam}: "${rolls[i].value}" niet in ${JSON.stringify(v.mag)}`);
		expect(ok).toBe(true);
	});
	const drie = rolls[4].value.split(",").map((x) => x.trim());
	expect(drie.length).toBe(3);
	for (const k of drie) expect(KLEUREN).toContain(k);
}

describe("Rollwright: tabellen, lijsten en kolommen in de echte Obsidian", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("in de leesweergave komt elke worp uit de goede tabel", async function () {
		await openNote("Tabelworpen.md", "preview");
		const rolls = await waitForRolls(".markdown-reading-view", 5);
		console.log("TABELWORPEN LEZEN:", JSON.stringify(rolls));
		await browser.saveScreenshot(`${SHOTS}/t1-tabellen-lezen.png`);
		check(rolls);
	});

	it("tien keer klikken geeft steeds een waarde uit dezelfde tabel", async function () {
		const seen = new Set();
		for (let i = 0; i < 10; i++) {
			await browser.execute((sel) => document.querySelector(`${sel} .rollwright-roll`)?.click(), `${LEAF} .markdown-reading-view`);
			await browser.pause(300);
			const rolls = await readRolls(".markdown-reading-view");
			expect(KLEUREN).toContain(rolls[0].value);
			seen.add(rolls[0].value);
		}
		console.log("KLEUREN GEZIEN NA TIEN KLIKKEN:", JSON.stringify([...seen]));
		// Met drie kleuren en elf worpen is maar één kleur zien vrijwel onmogelijk (kans 3 op 3^11).
		expect(seen.size).toBeGreaterThan(1);
	});

	it("in Live Preview hetzelfde", async function () {
		await openNote("Tabelworpen.md", "source");
		const rolls = await waitForRolls(".markdown-source-view", 5);
		console.log("TABELWORPEN LIVE PREVIEW:", JSON.stringify(rolls));
		await browser.saveScreenshot(`${SHOTS}/t2-tabellen-live-preview.png`);
		check(rolls);
	});

	it("de notitie met de tabellen zelf toont de geneste code als worp", async function () {
		await openNote("Tabellen.md", "preview");
		const rolls = await waitForRolls(".markdown-reading-view", 1);
		console.log("TABELLEN.MD ZELF:", JSON.stringify(rolls));
		expect(rolls.length).toBe(1);
		expect(KLEUREN).toContain(rolls[0].value);
	});
});
