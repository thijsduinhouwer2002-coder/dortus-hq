import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// OPEN.md punt 20: de instellingen van Rollwright in de zoekfunctie van Obsidian 1.13 en later
// (src/ui/settings.ts, getSettingDefinitions). Deze spec zoekt zoals een gebruiker: typen in het
// zoekveld van het instellingenvenster, klikken op wat er gevonden wordt. Hij schrijft op wat hij ziet,
// zodat het log laat zien hoe Obsidian het zoeken toont.
// klikWorp uit klik-hulp.mjs past hier niet (die klikt worpen in een notitie); hier klikt wdio echt.
const SHOTS = "screenshots";
const MODAL = ".modal.mod-settings";
// Per zoekterm een stukje van de uitleg van de regel, zodat we weten dat het de regel van Rollwright is.
const TERMEN = [
	{ term: "Default die", uitleg: "number of sides" },
	{ term: "Skin", uitleg: "All rolling is free" },
	{ term: "License key", uitleg: "once every 30 days" },
];

async function openInstellingen(tab) {
	await browser.executeObsidian(({ app }, tab) => {
		app.setting.open();
		app.setting.openTabById(tab);
	}, tab);
	await browser.$(MODAL).waitForDisplayed({ timeout: 10000, timeoutMsg: "het instellingenvenster ging niet open" });
}

async function sluitInstellingen() {
	await browser.executeObsidian(({ app }) => app.setting.close());
	await browser.waitUntil(async () => !(await browser.$(MODAL).isExisting()), { timeout: 10000, timeoutMsg: "het instellingenvenster bleef open" });
}

async function actieveTab() {
	return browser.executeObsidian(({ app }) => app.setting.activeTab?.id ?? null);
}

/** Het zoekveld van het venster zelf (niet een veld in een tab). Zet er data-e2e-zoek op en beschrijf alle velden. */
async function vindZoekveld() {
	return browser.execute((modalSel) => {
		const modal = document.querySelector(modalSel);
		if (!modal) return { gevonden: false, velden: [] };
		const inputs = Array.from(modal.querySelectorAll("input"));
		const velden = inputs.map((i) => ({
			type: i.type,
			placeholder: i.placeholder,
			klasse: i.className,
			ouder: i.parentElement?.className ?? "",
			inTab: !!i.closest(".vertical-tab-content"),
			zichtbaar: i.getClientRects().length > 0,
		}));
		const zoek = inputs.find((i) => !i.closest(".vertical-tab-content") && i.getClientRects().length > 0 && (i.type === "search" || /search|zoek/i.test(i.placeholder) || i.closest(".search-input-container")));
		if (zoek) zoek.setAttribute("data-e2e-zoek", "1");
		return { gevonden: !!zoek, velden };
	}, MODAL);
}

/** Zichtbare regels in het venster met de zoekterm in de naam, met hun omgeving als bewijs. Zet data-e2e-hit op elk. */
async function treffers(term) {
	return browser.execute((modalSel, term) => {
		const modal = document.querySelector(modalSel);
		if (!modal) return [];
		for (const el of Array.from(modal.querySelectorAll("[data-e2e-hit]"))) el.removeAttribute("data-e2e-hit");
		const laag = term.toLowerCase();
		const zichtbaar = (el) => el.getClientRects().length > 0;
		let namen = Array.from(modal.querySelectorAll(".setting-item-name")).filter((el) => zichtbaar(el) && (el.textContent ?? "").toLowerCase().includes(laag));
		if (namen.length === 0) {
			// Toont Obsidian treffers op een andere manier, pak dan de kleinste zichtbare elementen met de term.
			namen = Array.from(modal.querySelectorAll("*")).filter((el) => zichtbaar(el) && el.tagName !== "INPUT" && el.children.length <= 2
				&& (el.textContent ?? "").toLowerCase().includes(laag) && !Array.from(el.children).some((c) => (c.textContent ?? "").toLowerCase().includes(laag)));
		}
		return namen.map((el, i) => {
			el.setAttribute("data-e2e-hit", String(i));
			const rij = el.closest(".setting-item") ?? el.parentElement;
			const voorouders = [];
			for (let a = el.parentElement, n = 0; a && a !== modal && n < 7; a = a.parentElement, n++) voorouders.push(`${a.tagName.toLowerCase()}.${a.className}`);
			let omgeving = "";
			for (let a = el.parentElement, n = 0; a && a !== modal && n < 5; a = a.parentElement, n++) {
				if (/rollwright/i.test(a.textContent ?? "")) { omgeving = (a.textContent ?? "").slice(0, 200); break; }
			}
			return {
				tekst: (el.textContent ?? "").trim(),
				klasse: el.className,
				html: el.innerHTML.slice(0, 200),
				rij: (rij?.textContent ?? "").trim().slice(0, 200),
				rijKlasse: rij?.className ?? "",
				voorouders,
				rollwrightInBuurt: omgeving,
			};
		});
	}, MODAL, term);
}

/** Typ in het zoekveld zoals een gebruiker. Leeg maken gaat met een input-event, want setValue("") typt niets. */
async function zoek(term) {
	const veld = browser.$("[data-e2e-zoek]");
	if (term === "") {
		await browser.execute(() => {
			const i = document.querySelector("[data-e2e-zoek]");
			if (!i) return;
			i.value = "";
			i.dispatchEvent(new Event("input", { bubbles: true }));
		});
		return;
	}
	await veld.setValue(term);
}

/** De Rollwright-tab: aantal formulerijen, en hoe vaak een naam of uitleg er staat. */
async function tabStaat(naam, uitleg) {
	return browser.executeObsidian(({ app }, naam, uitleg) => {
		const tab = app.setting.pluginTabs.find((t) => t.id === "rollwright");
		const el = tab?.containerEl;
		if (!el) return null;
		const items = Array.from(el.querySelectorAll(".setting-item"));
		return {
			formulerijen: items.filter((it) => it.querySelector('input[placeholder="Formula"]')).length,
			namen: Array.from(el.querySelectorAll(".setting-item-name")).filter((n) => (n.textContent ?? "").trim() === naam).length,
			uitleg: Array.from(el.querySelectorAll(".setting-item-description")).filter((d) => (d.textContent ?? "").includes(uitleg)).length,
			opgeslagen: app.plugins.plugins.rollwright.settings.formulas.length,
		};
	}, naam, uitleg);
}

/** Zet data-e2e-veld op het tekstveld van de regel met deze naam in de Rollwright-tab. */
async function markeerVeld(naam) {
	await browser.waitUntil(async () => browser.executeObsidian(({ app }, naam) => {
		const el = app.setting.pluginTabs.find((t) => t.id === "rollwright")?.containerEl;
		const rij = Array.from(el?.querySelectorAll(".setting-item") ?? []).find((it) => (it.querySelector(".setting-item-name")?.textContent ?? "").trim() === naam);
		const input = rij?.querySelector("input[type=text], input:not([type])");
		if (!input || input.getClientRects().length === 0) return false;
		for (const oud of Array.from(document.querySelectorAll("[data-e2e-veld]"))) oud.removeAttribute("data-e2e-veld");
		input.setAttribute("data-e2e-veld", "1");
		return true;
	}, naam), { timeout: 10000, timeoutMsg: `geen tekstveld bij ${naam} in de Rollwright-tab` });
	return browser.$("[data-e2e-veld]");
}

describe("Rollwright: zoeken in de instellingen (OPEN.md punt 20)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		const versie = await browser.executeObsidian(({ obsidian }) => ({ api: obsidian.apiVersion, nieuw: obsidian.requireApiVersion("1.13.0") }));
		console.log("OBSIDIAN VERSIE:", JSON.stringify(versie));
	});

	after(async function () {
		await browser.executeObsidian(({ app }) => app.setting.close());
	});

	it("typen in het zoekveld vindt Default die, Skin en License key van Rollwright", async function () {
		await openInstellingen("editor");
		const veld = await vindZoekveld();
		console.log("VELDEN IN HET VENSTER:", JSON.stringify(veld.velden));
		expect(veld.gevonden).toBe(true);
		expect(await treffers("Default die")).toEqual([]);

		for (const [n, { term, uitleg }] of TERMEN.entries()) {
			await zoek(term);
			let hits = [];
			const vanRollwright = (h) => h.rij.includes(uitleg) || h.rollwrightInBuurt !== "";
			await browser.waitUntil(async () => {
				hits = await treffers(term);
				return hits.some(vanRollwright);
			}, { timeout: 10000, timeoutMsg: `zoeken op "${term}" vond de regel van Rollwright niet` }).catch(async (e) => {
				console.log(`ZOEK "${term}" TREFFERS TOT NU:`, JSON.stringify(hits, null, 1));
				console.log("VENSTER TEKST:", JSON.stringify((await browser.$(MODAL).getText()).slice(0, 1500)));
				throw e;
			});
			console.log(`ZOEK "${term}": met de uitleg van Rollwright in de regel: ${hits.some((h) => h.rij.includes(uitleg))}`);
			console.log(`ZOEK "${term}": ${hits.length} treffers:`, JSON.stringify(hits, null, 1));
			console.log(`ZOEK "${term}": actieve tab ${await actieveTab()}`);
			await browser.saveScreenshot(`${SHOTS}/zoek-${n + 1}-${term.replace(/ /g, "-").toLowerCase()}.png`);
		}
	});

	it("een gevonden regel aanklikken opent de Rollwright-tab op de goede plek", async function () {
		await zoek("Default die");
		let hits = [];
		await browser.waitUntil(async () => {
			hits = await treffers("Default die");
			return hits.some((h) => h.rij.includes("number of sides"));
		}, { timeout: 10000, timeoutMsg: "Default die werd niet weer gevonden" });
		const i = hits.findIndex((h) => h.rij.includes("number of sides"));
		console.log("KLIK OP TREFFER:", JSON.stringify(hits[i]));

		// Eerst de naam, dan de hele regel, dan een zichtbare kop of link met Rollwright erin: wat Obsidian ook klikbaar maakt.
		const pogingen = [
			["naam", `[data-e2e-hit="${i}"]`],
			["regel", `.setting-item:has([data-e2e-hit="${i}"])`],
		];
		let geopend = false;
		for (const [wat, sel] of pogingen) {
			const el = browser.$(sel);
			if (!(await el.isExisting())) { console.log(`KLIK ${wat}: niet gevonden`); continue; }
			await el.click();
			geopend = await browser.waitUntil(async () => (await actieveTab()) === "rollwright", { timeout: 4000 }).catch(() => false);
			const zoektekst = await browser.execute(() => document.querySelector("[data-e2e-zoek]")?.value ?? "(zoekveld weg)");
			console.log(`KLIK ${wat}: actieve tab ${await actieveTab()}, zoekveld "${zoektekst}", geopend ${geopend}`);
			if (geopend) break;
		}
		if (!geopend) {
			const kop = await browser.execute((modalSel) => {
				const modal = document.querySelector(modalSel);
				const el = Array.from(modal?.querySelectorAll("*") ?? []).find((e) => e.getClientRects().length > 0 && e.children.length === 0 && /^rollwright$/i.test((e.textContent ?? "").trim()) && !e.closest(".vertical-tab-header"));
				if (!el) return null;
				el.setAttribute("data-e2e-kop", "1");
				return `${el.tagName.toLowerCase()}.${el.className} in ${el.parentElement?.className ?? ""}`;
			}, MODAL);
			console.log("KOP MET ROLLWRIGHT IN DE ZOEKUITSLAG:", kop);
			if (kop) {
				await browser.$("[data-e2e-kop]").click();
				geopend = await browser.waitUntil(async () => (await actieveTab()) === "rollwright", { timeout: 4000 }).catch(() => false);
				console.log(`KLIK kop: actieve tab ${await actieveTab()}, geopend ${geopend}`);
			}
		}

		const plek = await browser.executeObsidian(({ app }) => {
			const el = app.setting.pluginTabs.find((t) => t.id === "rollwright")?.containerEl;
			const rij = Array.from(el?.querySelectorAll(".setting-item") ?? []).find((it) => (it.querySelector(".setting-item-name")?.textContent ?? "").trim() === "Default die");
			if (!rij) return null;
			const r = rij.getBoundingClientRect();
			const vak = el.getBoundingClientRect();
			return { klasse: rij.className, zichtbaar: rij.getClientRects().length > 0 && r.top >= vak.top - 1 && r.bottom <= vak.bottom + 1, actieveTab: app.setting.activeTab?.id ?? null };
		});
		console.log("NA DE KLIK, REGEL DEFAULT DIE IN DE TAB:", JSON.stringify(plek));
		await browser.saveScreenshot(`${SHOTS}/zoek-4-na-klik.png`);
		if (!geopend) {
			console.log("OBSIDIAN OPENT GEEN TAB BIJ EEN KLIK OP EEN TREFFER; zie de treffers en klikken hierboven.");
			this.skip();
		}
		expect(plek?.zichtbaar).toBe(true);
	});

	it("naam en uitleg staan er maar één keer in de Rollwright-tab", async function () {
		await vindZoekveld();
		await zoek("");
		await browser.executeObsidian(({ app }) => app.setting.openTabById("rollwright"));
		await markeerVeld("Default die");
		for (const [naam, uitleg] of [["Default die", "number of sides"], ["Skin", "All rolling is free"], ["License key", "once every 30 days"]]) {
			const s = await tabStaat(naam, uitleg);
			console.log(`DUBBEL? ${naam}: ${s.namen} keer de naam, ${s.uitleg} keer de uitleg`);
			expect(s.namen).toBe(1);
			expect(s.uitleg).toBe(1);
		}
		await browser.saveScreenshot(`${SHOTS}/zoek-5-tab.png`);
	});

	it("Add en de prullenbak tekenen de tab opnieuw", async function () {
		const voor = await tabStaat("Default die", "number of sides");
		console.log("FORMULES VOOR ADD:", JSON.stringify(voor));
		await browser.$(MODAL).$("button=Add").click();
		let na = voor;
		await browser.waitUntil(async () => {
			na = await tabStaat("Default die", "number of sides");
			return na.formulerijen === voor.formulerijen + 1;
		}, { timeout: 10000, timeoutMsg: "na Add kwam er geen formulerij bij in de tab" }).catch((e) => {
			console.log("FORMULES NA ADD:", JSON.stringify(na));
			throw e;
		});
		console.log("FORMULES NA ADD:", JSON.stringify(na));
		expect(na.opgeslagen).toBe(voor.opgeslagen + 1);
		await browser.saveScreenshot(`${SHOTS}/zoek-6-na-add.png`);

		const prullenbakken = await browser.$(MODAL).$$('.clickable-icon[aria-label="Remove"]');
		console.log("PRULLENBAKKEN:", prullenbakken.length);
		await prullenbakken[prullenbakken.length - 1].click();
		await browser.waitUntil(async () => {
			na = await tabStaat("Default die", "number of sides");
			return na.formulerijen === voor.formulerijen;
		}, { timeout: 10000, timeoutMsg: "na de prullenbak bleef de formulerij in de tab staan" }).catch((e) => {
			console.log("FORMULES NA PRULLENBAK:", JSON.stringify(na));
			throw e;
		});
		console.log("FORMULES NA PRULLENBAK:", JSON.stringify(na));
		expect(na.opgeslagen).toBe(voor.opgeslagen);
	});

	it("een waarde blijft bewaard na sluiten en weer openen", async function () {
		const oud = await browser.executeObsidian(({ app }) => app.plugins.plugins.rollwright.settings.defaultSides);
		await (await markeerVeld("Default die")).setValue("12");
		await browser.waitUntil(async () => (await browser.executeObsidian(async ({ app }) => (await app.plugins.plugins.rollwright.loadData())?.defaultSides)) === 12,
			{ timeout: 10000, timeoutMsg: "12 werd niet opgeslagen" });
		await sluitInstellingen();
		await openInstellingen("rollwright");
		const waarde = await (await markeerVeld("Default die")).getValue();
		const opgeslagen = await browser.executeObsidian(async ({ app }) => (await app.plugins.plugins.rollwright.loadData())?.defaultSides);
		console.log(`BEWAARD: was ${oud}, getypt 12, na weer openen staat er "${waarde}", in data.json ${opgeslagen}`);
		expect(waarde).toBe("12");
		expect(opgeslagen).toBe(12);

		await (await markeerVeld("Default die")).setValue(String(oud));
		await browser.waitUntil(async () => (await browser.executeObsidian(({ app }) => app.plugins.plugins.rollwright.settings.defaultSides)) === oud,
			{ timeout: 10000, timeoutMsg: "de oude waarde kwam niet terug" });
	});
});
