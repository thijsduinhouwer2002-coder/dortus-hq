import { browser, expect } from "@wdio/globals";
import * as fs from "fs";
import { klikWorp } from "./klik-hulp.mjs";

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
		old: r.querySelector(".rollwright-value")?.getAttribute("data-e2e-oud") === "1",
		error: r.getAttribute("data-rollwright-error") ?? "",
		label: r.getAttribute("aria-label") ?? "",
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
	expect(rolls.length).toBe(7);
	for (const r of rolls) expect(r.error).toBe("");
	VERWACHT.forEach((v, i) => {
		const ok = v.mag.includes(rolls[i].value);
		if (!ok) console.log(`FOUT BIJ ${v.naam}: "${rolls[i].value}" niet in ${JSON.stringify(v.mag)}`);
		expect(ok).toBe(true);
	});
	const drie = rolls[4].value.split(",").map((x) => x.trim());
	expect(drie.length).toBe(3);
	for (const k of drie) expect(KLEUREN).toContain(k);
	// De opzoektabel kiest de rij die bij de worp hoort: 1 of 2 Regen, 3 Mist, 4 een kleur.
	const worp = Number(/1d4 = (\d+)/.exec(rolls[3].label)?.[1]);
	console.log("OPZOEKTABEL: worp", worp, "gaf", rolls[3].value);
	const bijWorp = worp <= 2 ? ["Regen"] : worp === 3 ? ["Mist"] : KLEUREN;
	expect(bijWorp).toContain(rolls[3].value);
	// Kop "dice: 4" valt altijd op rij 4, dus de geneste worp in de cel draait elke keer.
	expect(KLEUREN).toContain(rolls[5].value);
	expect(["Miauw", "Woef"]).toContain(rolls[6].value);
}

describe("Rollwright: tabellen, lijsten en kolommen in de echte Obsidian", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("in de leesweergave komt elke worp uit de goede tabel", async function () {
		await openNote("Tabelworpen.md", "preview");
		const rolls = await waitForRolls(".markdown-reading-view", 7);
		console.log("TABELWORPEN LEZEN:", JSON.stringify(rolls));
		await browser.saveScreenshot(`${SHOTS}/t1-tabellen-lezen.png`);
		check(rolls);
	});

	it("tien keer klikken geeft steeds een waarde uit dezelfde tabel", async function () {
		const seen = new Set();
		const reeks = [];
		for (let i = 0; i < 10; i++) {
			// Merkteken op de oude uitkomst, zodat we wachten op de nieuwe en niet de oude lezen
			// (zelfde aanpak als secties.e2e.mjs).
			await klikWorp(`${LEAF} .markdown-reading-view`, 0, { markeer: true });
			let rolls = [];
			await browser.waitUntil(async () => {
				rolls = await readRolls(".markdown-reading-view");
				return rolls[0] !== undefined && !rolls[0].old && rolls[0].value !== "";
			}, { timeout: 5000, timeoutMsg: "na een klik kwam er geen nieuwe worp" });
			expect(KLEUREN).toContain(rolls[0].value);
			seen.add(rolls[0].value);
			reeks.push(rolls[0].value);
		}
		console.log("KLEUREN PER KLIK:", JSON.stringify(reeks));
		console.log("KLEUREN GEZIEN NA TIEN KLIKKEN:", JSON.stringify([...seen]));
		// Met drie kleuren en elf worpen is maar één kleur zien vrijwel onmogelijk (kans 3 op 3^11).
		expect(seen.size).toBeGreaterThan(1);
	});

	it("in Live Preview hetzelfde", async function () {
		await openNote("Tabelworpen.md", "source");
		const rolls = await waitForRolls(".markdown-source-view", 7);
		console.log("TABELWORPEN LIVE PREVIEW:", JSON.stringify(rolls));
		// Live Preview deelt de uitkomst met de leesweergave (zelfde sleutel); dit bewijst dat de
		// widgets er staan met de goede waarden, niet dat Live Preview zelf opnieuw rolt.
		await browser.saveScreenshot(`${SHOTS}/t2-tabellen-live-preview.png`);
		check(rolls);
	});

	it("de notitie met de tabellen zelf toont de geneste code als worp", async function () {
		await openNote("Tabellen.md", "preview");
		const rolls = await waitForRolls(".markdown-reading-view", 2);
		console.log("TABELLEN.MD ZELF:", JSON.stringify(rolls));
		expect(rolls.length).toBe(2);
		for (const r of rolls) expect(KLEUREN).toContain(r.value);
	});
});
