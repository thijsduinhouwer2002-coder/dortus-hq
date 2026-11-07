import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Worpen op blokken (secties) en regels van een andere notitie, in de echte Obsidian.
// Sectiewerpen.md rolt op Bron.md. Elk blok in Bron.md heeft een eigen woord, zodat te zien is
// welk blok of welke regel er kwam.
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";
const ZWS = String.fromCharCode(0x200b);

// Blokken van Bron.md zoals de plugin ze ziet: frontmatter en de horizontale lijn tellen niet mee.
const BLOKKEN = {
	kop1: ["Alfa"],
	alinea1: ["Bravo"],
	kop2: ["Charlie"],
	alinea2: ["Delta"],
	lijst: ["Foxtrot", "Golf"],
	alinea3: ["Hotel", "India"],
};
const ALINEAS = ["alinea1", "alinea2", "alinea3"];
const ALLE_WOORDEN = Object.values(BLOKKEN).flat();
const NOOIT = ["Geheimyaml", "soort"];

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
	return browser.execute((sel, zws) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`))
		.filter((r) => !r.parentElement?.closest(".rollwright-roll"))
		.map((r) => {
			const value = r.querySelector(".rollwright-value");
			return {
				value: (value?.textContent ?? "").split(zws).join("").trim(),
				error: r.getAttribute("data-rollwright-error") ?? "",
				hr: value?.querySelector("hr") !== null && value !== null,
				nested: value?.querySelectorAll(".rollwright-roll").length ?? 0,
				codes: Array.from(value?.querySelectorAll("code") ?? []).map((c) => (c.textContent ?? "").split(zws).join("")),
				paragraphs: value?.querySelectorAll("p").length ?? 0,
			};
		}), `${LEAF} ${view}`, ZWS);
}

async function waitForRolls(view, n) {
	let last = [];
	await browser.waitUntil(async () => {
		last = await readRolls(view);
		return last.length >= n && last.every((r) => r.value !== "" || r.error !== "" || r.hr);
	}, { timeout: 20000, timeoutMsg: `geen ${n} uitkomsten in ${view}` }).catch((e) => {
		console.log("WORPEN TOT NU:", JSON.stringify(last));
		throw e;
	});
	return last;
}

/** Welke woorden van Bron.md staan in de tekst. */
function woorden(text) {
	return ALLE_WOORDEN.filter((w) => text.includes(w));
}

/** Klopt de tekst met precies één blok uit de lijst? Geeft de naam van dat blok. */
function eenBlok(text, toegestaan) {
	const gezien = woorden(text);
	return toegestaan.find((naam) => {
		const w = BLOKKEN[naam];
		return w.every((x) => gezien.includes(x)) && gezien.every((x) => w.includes(x));
	});
}

function checkRegel(r, aantal, wat) {
	const gezien = woorden(r.value);
	// "---" is ook een niet-lege regel; dan toont de uitkomst een lijn zonder tekst.
	const lijnen = r.hr ? 1 : 0;
	console.log(`${wat}: woorden ${JSON.stringify(gezien)}, lijnen ${lijnen}`);
	expect(gezien.length + lijnen).toBe(aantal);
}

function check(rolls) {
	expect(rolls.length).toBe(7);
	for (const r of rolls) {
		expect(r.error).toBe("");
		for (const n of NOOIT) expect(r.value.includes(n)).toBe(false);
		// Een code in een getrokken blok rolt niet opnieuw.
		expect(r.nested).toBe(0);
	}
	const [blok, alinea, kop2, regel, vast, tweeRegels, tweeAlineas] = rolls;

	const b = eenBlok(blok.value, Object.keys(BLOKKEN));
	console.log("BLOK:", b, JSON.stringify(blok.value));
	expect(b).not.toBe(undefined);
	expect(blok.hr).toBe(false);

	const a = eenBlok(alinea.value, ALINEAS);
	console.log("ALINEA:", a);
	expect(a).not.toBe(undefined);

	expect(eenBlok(kop2.value, ["kop2"])).toBe("kop2");

	checkRegel(regel, 1, "REGEL");
	// Een regel is één regel: van de alinea Hotel/India komt nooit alles tegelijk.
	expect(regel.value.includes("Hotel") && regel.value.includes("India")).toBe(false);

	expect(eenBlok(vast.value, ["alinea2"])).toBe("alinea2");
	console.log("CODES IN VAST BLOK:", JSON.stringify(vast.codes));
	expect(vast.codes).toContain("dice: 1d6");

	checkRegel(tweeRegels, 2, "TWEE REGELS");

	// Twee alinea's: elk woord hoort bij een alinea, en er zijn twee <p> in de uitkomst.
	const tw = woorden(tweeAlineas.value);
	console.log("TWEE ALINEA'S:", JSON.stringify(tw), "p:", tweeAlineas.paragraphs);
	for (const w of tw) expect(ALINEAS.some((n) => BLOKKEN[n].includes(w))).toBe(true);
	expect(tweeAlineas.paragraphs).toBe(2);
}

describe("Rollwright: secties en regels in de echte Obsidian", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("in de leesweergave komt elke worp uit het goede blok of de goede regel", async function () {
		await openNote("Sectiewerpen.md", "preview");
		const rolls = await waitForRolls(".markdown-reading-view", 7);
		console.log("SECTIEWERPEN LEZEN:", JSON.stringify(rolls));
		await browser.saveScreenshot(`${SHOTS}/s1-secties-lezen.png`);
		check(rolls);
	});

	it("vijftien keer klikken op de regelworp geeft steeds één regel, en verschillende", async function () {
		const seen = new Set();
		for (let i = 0; i < 15; i++) {
			const before = (await readRolls(".markdown-reading-view"))[3];
			await browser.execute((sel) => document.querySelectorAll(`${sel} .rollwright-roll`)[3]?.click(), `${LEAF} .markdown-reading-view`);
			let rolls = [];
			await browser.waitUntil(async () => {
				rolls = await readRolls(".markdown-reading-view");
				return rolls[3] !== undefined && (rolls[3].value !== "" || rolls[3].hr);
			}, { timeout: 5000, timeoutMsg: "na een klik bleef de regelworp leeg" });
			checkRegel(rolls[3], 1, `KLIK ${i + 1}`);
			seen.add(rolls[3].hr ? "---" : woorden(rolls[3].value)[0]);
			if (i === 0) console.log("VOOR DE EERSTE KLIK:", JSON.stringify(before.value));
		}
		console.log("REGELS GEZIEN:", JSON.stringify([...seen]));
		// Negen regels en zestien worpen: steeds dezelfde regel is vrijwel onmogelijk.
		expect(seen.size).toBeGreaterThan(1);
	});

	it("in Live Preview hetzelfde", async function () {
		await openNote("Sectiewerpen.md", "source");
		const rolls = await waitForRolls(".markdown-source-view", 7);
		console.log("SECTIEWERPEN LIVE PREVIEW:", JSON.stringify(rolls));
		await browser.saveScreenshot(`${SHOTS}/s2-secties-live-preview.png`);
		check(rolls);
	});

	it("Ctrl-klik op het vaste blok opent Bron.md in een nieuw tabblad en rolt niet", async function () {
		await openNote("Sectiewerpen.md", "preview");
		await waitForRolls(".markdown-reading-view", 7);
		const tabsBefore = await browser.executeObsidian(({ app }) => app.workspace.getLeavesOfType("markdown").length);
		await browser.execute((sel) => {
			const el = document.querySelectorAll(`${sel} .rollwright-roll`)[4];
			el?.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, ctrlKey: true }));
		}, `${LEAF} .markdown-reading-view`);
		let state = null;
		await browser.waitUntil(async () => {
			state = await browser.executeObsidian(({ app }) => ({
				active: app.workspace.getActiveFile()?.path ?? "",
				tabs: app.workspace.getLeavesOfType("markdown").length,
				open: app.workspace.getLeavesOfType("markdown").map((l) => l.view?.file?.path ?? ""),
			}));
			return state.open.includes("Bron.md");
		}, { timeout: 5000, timeoutMsg: "Bron.md ging niet open" }).catch((e) => {
			console.log("NA CTRL-KLIK:", JSON.stringify(state));
			throw e;
		});
		console.log("NA CTRL-KLIK:", JSON.stringify(state), "tabbladen eerst:", tabsBefore);
		expect(state.tabs).toBe(tabsBefore + 1);
		await browser.saveScreenshot(`${SHOTS}/s3-ctrl-klik-bron.png`);
		// Terug naar Sectiewerpen: het vaste blok staat er nog, ongewijzigd.
		await browser.executeObsidian(async ({ app }) => {
			for (const leaf of app.workspace.getLeavesOfType("markdown")) {
				if (leaf.view?.file?.path === "Bron.md") leaf.detach();
			}
		});
		await openNote("Sectiewerpen.md", "preview");
		const rolls = await waitForRolls(".markdown-reading-view", 7);
		expect(eenBlok(rolls[4].value, ["alinea2"])).toBe("alinea2");
	});
});
