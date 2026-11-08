import { browser, expect } from "@wdio/globals";
import * as fs from "fs";
import { klikWorp } from "./klik-hulp.mjs";

// Daan punt 1: een uitkomst van meer dan één regel of een blok staat als eigen blok onder de regel,
// met gewone tekstgrootte en zonder lijstbolletjes. Eén regel blijft in de zin.
// Blokwerpen.md rolt op Bron.md (zelfde notitie als in secties.e2e.mjs).
// "Twee regels" trekt willekeurige regels uit Bron.md, maar lezen en Live Preview delen de worp (zelfde sleutel).
// Een losse lijn (***) telt niet als regel: die was in lezen 64 px hoger dan in Live Preview (run 42365261005).
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
				const icoon = r.querySelector(".rollwright-icon")?.getBoundingClientRect();
				// Het ouderelement: in lezen de <p>, in Live Preview de .cm-line.
				const ouder = r.parentElement?.closest("p, li, .cm-line")?.getBoundingClientRect();
				return {
					tekst: (r.textContent ?? "").trim(),
					// Daan punt 3: een worp in de uitkomst is gewone tekst, geen code.
					codes: value?.querySelectorAll("code").length ?? 0,
					stil: Array.from(value?.querySelectorAll(".rollwright-nested") ?? []).map((n) => n.textContent),
					oud: value?.getAttribute("data-e2e-oud") === "1",
					blok: r.classList.contains("rollwright-roll-block"),
					fout: r.getAttribute("data-rollwright-error") ?? "",
					display: getComputedStyle(r).display,
					rol: r.getAttribute("role"),
					tabindex: r.getAttribute("tabindex"),
					breedte: Math.round(rect.width),
					hoogte: Math.round(rect.height),
					icoonBoven: icoon ? Math.round(icoon.top - rect.top) : null,
					// Ruimte in het ouderelement onder het blok (een label ervoor telt niet mee).
					ruimteOnder: ouder ? Math.round(ouder.bottom - rect.bottom) : null,
					ouderHoogte: ouder ? Math.round(ouder.height) : null,
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
	expect(gemeten.regelBreedte).toBeGreaterThan(0);
	rolls.forEach((r, i) => console.log(`${wat} WORP ${i}:`, JSON.stringify(r)));
	expect(rolls.length).toBe(AANTAL);
	for (const r of rolls) {
		expect(r.fout).toBe("");
		expect(r.rol).toBe("button");
		expect(r.tabindex).toBe("0");
	}

	const kop = rolls[KOP];
	expect(kop.blok).toBe(true);
	// In lezen flex, in Live Preview inline-flex (zie styles.css); in beide over de hele breedte.
	expect(["flex", "inline-flex"]).toContain(kop.display);
	expect(kop.breedte).toBeGreaterThanOrEqual(gemeten.regelBreedte * 0.9);
	expect(kop.kop).not.toBe(null);
	console.log(`${wat}: kop in uitkomst ${kop.kop.grootte} tegen gewone tekst ${tekst}, marge boven ${kop.kop.margeBoven}, gewicht ${kop.kop.gewicht}`);
	expect(px(kop.kop.grootte)).toBeLessThanOrEqual(px(tekst) + 0.5);
	expect(px(kop.kop.margeBoven)).toBe(0);
	expect(Number(kop.kop.gewicht)).toBeGreaterThanOrEqual(600);

	const twee = rolls[TWEE_REGELS];
	expect(twee.blok).toBe(true);
	expect(["flex", "inline-flex"]).toContain(twee.display);
	expect(twee.breedte).toBeGreaterThanOrEqual(gemeten.regelBreedte * 0.9);

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
	// Daan punt 3: "Alinea Delta met een worp `dice: 1d6` erin." toont 1d6 als gewone tekst.
	console.log(`punt 3: ${JSON.stringify({ tekst: alinea.tekst, codes: alinea.codes, stil: alinea.stil })}`);
	expect(alinea.codes).toBe(0);
	expect(alinea.stil).toEqual(["1d6"]);
	expect(alinea.tekst).toContain("worp 1d6 erin");
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
	await klikWorp(`${LEAF} ${view}`, KOP, { markeer: true });
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

const BLOKKEN = [KOP, TWEE_REGELS, LIJST];

/** Het icoon staat naast de eerste regel van elk blok, niet erboven. */
function checkIcoon(gemeten, wat) {
	for (const i of BLOKKEN) {
		const r = gemeten.rolls[i];
		console.log(`${wat} BLOK ${i}: hoogte ${r.hoogte}, icoon ${r.icoonBoven} px onder de bovenkant, ruimte onder ${r.ruimteOnder} px`);
		expect(r.icoonBoven).not.toBe(null);
		expect(r.icoonBoven).toBeLessThan(20);
	}
}

/** Live Preview ziet eruit als lezen: zelfde hoogte (hoogstens 4 px verschil), en in de .cm-line hoogstens 8 px onder het blok. */
function vergelijk(lezen, live) {
	for (const i of BLOKKEN) {
		const a = lezen.rolls[i];
		const b = live.rolls[i];
		console.log(`BLOK ${i} LEZEN TEGEN LIVE PREVIEW: hoogte ${a.hoogte} / ${b.hoogte}, ouder ${a.ouderHoogte} / ${b.ouderHoogte}, ruimte onder in ouder ${a.ruimteOnder} / ${b.ruimteOnder}, tekst ${JSON.stringify(a.tekst)} / ${JSON.stringify(b.tekst)}`);
		expect(Math.abs(a.hoogte - b.hoogte)).toBeLessThanOrEqual(4);
		expect(b.ruimteOnder).not.toBe(null);
		expect(b.ruimteOnder).toBeLessThanOrEqual(8);
	}
}

/** De metingen in lezen na de klik, om Live Preview mee te vergelijken. */
let inLezen = null;

describe("Rollwright: uitkomst als blok (Daan punt 1)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
	});

	it("in de leesweergave: kop, twee regels en lijst als blok, gewone worp in de zin", async function () {
		await openNote("Blokwerpen.md", "preview");
		const gemeten = await wachtOpWorpen(".markdown-reading-view");
		await plaatjes("blok-lezen");
		check(gemeten, "LEZEN");
		checkIcoon(gemeten, "LEZEN");
		await klikKop(".markdown-reading-view");
		inLezen = await meet(".markdown-reading-view");
	});

	it("in Live Preview hetzelfde", async function () {
		await openNote("Blokwerpen.md", "source");
		const gemeten = await wachtOpWorpen(".markdown-source-view");
		await plaatjes("blok-live-preview");
		check(gemeten, "LIVE PREVIEW");
		checkIcoon(gemeten, "LIVE PREVIEW");
		expect(inLezen).not.toBe(null);
		vergelijk(inLezen, gemeten);
		await klikKop(".markdown-source-view");
	});
});
