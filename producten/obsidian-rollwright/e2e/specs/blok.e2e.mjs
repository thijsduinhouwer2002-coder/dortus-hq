import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Daan punt 1: een uitkomst van meer dan één regel of een blok staat als eigen blok onder de regel,
// met gewone tekstgrootte en zonder lijstbolletjes. Eén regel blijft in de zin.
// Blokwerpen.md rolt op Bron.md (zelfde notitie als in secties.e2e.mjs).
const SHOTS = "screenshots";
const LEAF = ".workspace-leaf.mod-active";
const AANTAL = 5;
// Volgorde van de worpen in Blokwerpen.md.
const KOP = 0;
const TWEE_REGELS = 1;
const LIJST = 2;
const GEWOON = 3;
const EEN_ALINEA = 4;

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

/** Wat elke worp laat zien: klasse, weergave, en de berekende stijl van kop, lijst en een gewone alinea. */
async function meet(view) {
	return browser.execute((sel) => {
		const root = document.querySelector(sel);
		if (!root) return { rolls: [], tekst: "" };
		// De gewone alinea van de notitie, buiten elke worp.
		const gewoon = Array.from(root.querySelectorAll("p, .cm-line"))
			.find((el) => !el.closest(".rollwright-roll") && (el.textContent ?? "").includes("Een gewone alinea"));
		const rolls = Array.from(root.querySelectorAll(".rollwright-roll"))
			.filter((r) => !r.parentElement?.closest(".rollwright-roll"))
			.map((r) => {
				const value = r.querySelector(".rollwright-value");
				const kop = value?.querySelector("h1, h2, h3, h4, h5, h6");
				const lis = Array.from(value?.querySelectorAll("li") ?? []);
				const rect = r.getBoundingClientRect();
				return {
					tekst: (r.textContent ?? "").trim(),
					oud: value?.getAttribute("data-e2e-oud") === "1",
					blok: r.classList.contains("rollwright-roll-block"),
					fout: r.getAttribute("data-rollwright-error") ?? "",
					display: getComputedStyle(r).display,
					rol: r.getAttribute("role"),
					tabindex: r.getAttribute("tabindex"),
					breedte: Math.round(rect.width),
					hoogte: Math.round(rect.height),
					kop: kop ? { grootte: getComputedStyle(kop).fontSize, gewicht: getComputedStyle(kop).fontWeight, margeBoven: getComputedStyle(kop).marginTop } : null,
					lijst: lis.map((li) => ({
						stijl: getComputedStyle(li).listStyleType,
						display: getComputedStyle(li).display,
						marker: getComputedStyle(li, "::marker").content,
						bolletje: Array.from(li.querySelectorAll(".list-bullet")).some((b) => getComputedStyle(b).display !== "none"),
						top: Math.round(li.getBoundingClientRect().top),
					})),
				};
			});
		return {
			rolls,
			tekst: gewoon ? getComputedStyle(gewoon).fontSize : "",
			regelBreedte: gewoon ? Math.round(gewoon.getBoundingClientRect().width) : 0,
		};
	}, `${LEAF} ${view}`);
}

async function wachtOpWorpen(view) {
	let last = { rolls: [] };
	await browser.waitUntil(async () => {
		last = await meet(view);
		return last.rolls.length >= AANTAL && last.rolls.every((r) => r.tekst !== "" || r.fout !== "");
	}, { timeout: 20000, timeoutMsg: `geen ${AANTAL} uitkomsten in ${view}` }).catch((e) => {
		console.log("WORPEN TOT NU:", JSON.stringify(last));
		throw e;
	});
	// Het renderen van markdown is async: wacht tot de klasse op de kop staat.
	await browser.waitUntil(async () => {
		last = await meet(view);
		return last.rolls[KOP]?.blok === true;
	}, { timeout: 5000, timeoutMsg: "de kopworp kreeg geen blokklasse" }).catch((e) => {
		console.log("WORPEN:", JSON.stringify(last));
		throw e;
	});
	return last;
}

const px = (s) => parseFloat(s);

function check(gemeten, wat) {
	const { rolls, tekst } = gemeten;
	console.log(`${wat}: gewone tekst ${tekst}, regelbreedte ${gemeten.regelBreedte}`);
	rolls.forEach((r, i) => console.log(`${wat} WORP ${i}:`, JSON.stringify(r)));
	expect(rolls.length).toBe(AANTAL);
	for (const r of rolls) {
		expect(r.fout).toBe("");
		expect(r.rol).toBe("button");
		expect(r.tabindex).toBe("0");
	}

	const kop = rolls[KOP];
	expect(kop.blok).toBe(true);
	expect(kop.display).toBe("flex");
	expect(kop.kop).not.toBe(null);
	console.log(`${wat}: kop in uitkomst ${kop.kop.grootte} tegen gewone tekst ${tekst}, marge boven ${kop.kop.margeBoven}, gewicht ${kop.kop.gewicht}`);
	expect(px(kop.kop.grootte)).toBeLessThanOrEqual(px(tekst) + 0.5);
	expect(px(kop.kop.margeBoven)).toBe(0);
	expect(Number(kop.kop.gewicht)).toBeGreaterThanOrEqual(600);

	const twee = rolls[TWEE_REGELS];
	expect(twee.blok).toBe(true);
	expect(twee.display).toBe("flex");

	const lijst = rolls[LIJST];
	expect(lijst.blok).toBe(true);
	expect(lijst.lijst.length).toBe(2);
	for (const li of lijst.lijst) {
		// Geen bolletje: geen list-item (dan is er geen ::marker), of stijl none.
		expect(li.display !== "list-item" || li.stijl === "none").toBe(true);
		expect(li.bolletje).toBe(false);
	}
	// Elk punt op een eigen regel.
	expect(lijst.lijst[1].top).toBeGreaterThan(lijst.lijst[0].top);

	const gewoon = rolls[GEWOON];
	expect(gewoon.blok).toBe(false);
	expect(gewoon.display).toBe("inline-flex");

	const alinea = rolls[EEN_ALINEA];
	expect(alinea.blok).toBe(false);
	expect(alinea.display).toBe("inline-flex");
}

/** Zet het thema licht of donker zoals Obsidian dat doet, via de klassen op body. */
async function thema(donker) {
	await browser.execute((donker) => {
		document.body.classList.toggle("theme-dark", donker);
		document.body.classList.toggle("theme-light", !donker);
	}, donker);
	await browser.pause(300);
}

async function plaatjes(naam) {
	await thema(false);
	await browser.saveScreenshot(`${SHOTS}/${naam}.png`);
	await thema(true);
	await browser.saveScreenshot(`${SHOTS}/${naam}-donker.png`);
	await thema(false);
}

/** Klik op de kopworp: de klasse wordt opnieuw bepaald en blijft blok (een kop blijft een kop). */
async function klikKop(view) {
	// Merkteken op de oude uitkomst, zoals in geschiedenis.e2e.mjs: dan is te zien wanneer de nieuwe staat.
	await browser.execute((sel, i) => {
		document.querySelectorAll(`${sel} .rollwright-roll`)[i]?.querySelector(".rollwright-value")?.setAttribute("data-e2e-oud", "1");
	}, `${LEAF} ${view}`, KOP);
	await browser.execute((sel, i) => document.querySelectorAll(`${sel} .rollwright-roll`)[i]?.click(), `${LEAF} ${view}`, KOP);
	let na = { rolls: [] };
	await browser.waitUntil(async () => {
		na = await meet(view);
		const kop = na.rolls[KOP];
		return kop !== undefined && !kop.oud && kop.tekst !== "" && kop.blok;
	}, { timeout: 5000, timeoutMsg: "na een klik op de kop kwam er geen nieuwe uitkomst als blok" }).catch((e) => {
		console.log("NA KLIK OP KOP TOT NU:", JSON.stringify(na.rolls[KOP]));
		throw e;
	});
	console.log("NA KLIK OP KOP:", JSON.stringify(na.rolls[KOP]));
	expect(na.rolls[KOP].blok).toBe(true);
	expect(na.rolls[GEWOON].blok).toBe(false);
}

describe("Rollwright: uitkomst als blok (Daan punt 1)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("in de leesweergave: kop, twee regels en lijst als blok, gewone worp in de zin", async function () {
		await openNote("Blokwerpen.md", "preview");
		const gemeten = await wachtOpWorpen(".markdown-reading-view");
		await plaatjes("blok-lezen");
		check(gemeten, "LEZEN");
		await klikKop(".markdown-reading-view");
	});

	it("in Live Preview hetzelfde", async function () {
		await openNote("Blokwerpen.md", "source");
		const gemeten = await wachtOpWorpen(".markdown-source-view");
		await plaatjes("blok-live-preview");
		check(gemeten, "LIVE PREVIEW");
		await klikKop(".markdown-source-view");
	});
});
