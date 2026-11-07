import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// OPEN.md punt 20: de instellingen van Rollwright in de zoekfunctie van Obsidian 1.13 en later
// (src/ui/settings.ts, getSettingDefinitions). Deze spec zoekt zoals een gebruiker: typen in het
// zoekveld van het instellingenvenster, klikken op wat er gevonden wordt. Hij schrijft op wat hij ziet,
// zodat het log laat zien hoe Obsidian het zoeken toont.
//
// Obsidian 1.15 opent de instellingen in een eigen venster (de body heeft is-popout-window, run
// 42401067049), dus wdio vindt het venster niet in het hoofddocument. Daarom loopt alles via
// executeObsidian en app.setting.modalEl: typen is de waarde zetten met een input-event, klikken is
// el.click(), net als klikWorp in klik-hulp.mjs (die hulp zelf zoekt worpen in een notitie, dat past hier niet).
const SHOTS = "screenshots";
// De namen van regels van Rollwright om op te zoeken. Obsidian 1.15 toont in een treffer alleen de naam,
// geen uitleg (run 42401543789); dat een treffer van Rollwright is, blijkt uit de kop van zijn groep.
const TERMEN = ["Default die", "Skin", "License key"];

/** Een treffer van Rollwright: een gevonden regel met precies deze naam, onder de groepskop "Rollwright". */
const vanRollwright = (h, term) => h.groep === "Rollwright" && h.titel === term;

async function openInstellingen(tab) {
	const venster = await browser.executeObsidian(({ app }, tab) => {
		app.setting.open();
		app.setting.openTabById(tab);
		const el = app.setting.modalEl;
		return { klasse: el?.className ?? null, body: el?.ownerDocument?.body?.className ?? null, eigenVenster: el?.ownerDocument !== document };
	}, tab);
	console.log("INSTELLINGENVENSTER:", JSON.stringify(venster));
	await browser.waitUntil(async () => browser.executeObsidian(({ app }) => !!app.setting.modalEl?.isConnected && app.setting.modalEl.getClientRects().length > 0),
		{ timeout: 10000, timeoutMsg: "het instellingenvenster ging niet open" });
}

async function sluitInstellingen() {
	await browser.executeObsidian(({ app }) => { app.setting.close(); });
	await browser.waitUntil(async () => browser.executeObsidian(({ app }) => !app.setting.modalEl?.isConnected || app.setting.modalEl.getClientRects().length === 0),
		{ timeout: 10000, timeoutMsg: "het instellingenvenster bleef open" });
}

async function actieveTab() {
	return browser.executeObsidian(({ app }) => app.setting.activeTab?.id ?? null);
}

/** Een schermafbeelding van het venster van de instellingen, ook als dat een eigen venster is. */
async function foto(naam) {
	const hoofd = await browser.getWindowHandle();
	try {
		const vensters = await browser.getWindowHandles();
		for (const h of vensters) {
			if (h === hoofd) continue;
			await browser.switchToWindow(h);
			await browser.saveScreenshot(`${SHOTS}/${naam}.png`);
			return;
		}
		await browser.saveScreenshot(`${SHOTS}/${naam}.png`);
	} catch (e) {
		console.log(`FOTO ${naam} LUKTE NIET:`, String(e).slice(0, 200));
	} finally {
		await browser.switchToWindow(hoofd);
	}
}

/** Het zoekveld van het venster zelf (niet een veld in een tab). Zet er data-e2e-zoek op en beschrijf alle velden. */
async function vindZoekveld() {
	return browser.executeObsidian(({ app }) => {
		const modal = app.setting.modalEl;
		const inhoud = app.setting.activeTab?.containerEl;
		const inputs = Array.from(modal?.querySelectorAll("input") ?? []);
		const velden = inputs.map((i) => ({
			type: i.type,
			placeholder: i.placeholder,
			klasse: i.className,
			ouder: i.parentElement?.className ?? "",
			inTab: !!inhoud?.contains(i),
			zichtbaar: i.getClientRects().length > 0,
		}));
		const zoek = inputs.find((i) => !inhoud?.contains(i) && i.getClientRects().length > 0 && (i.type === "search" || /search|zoek/i.test(i.placeholder) || i.closest(".search-input-container")));
		if (zoek) zoek.setAttribute("data-e2e-zoek", "1");
		return { gevonden: !!zoek, velden };
	});
}

/** Typ in het zoekveld: de waarde zetten en een input-event, zoals bij typen. */
async function zoek(term) {
	return browser.executeObsidian(({ app }, term) => {
		const i = app.setting.modalEl?.querySelector("[data-e2e-zoek]");
		if (!i) return false;
		i.focus();
		i.value = term;
		i.dispatchEvent(new InputEvent("input", { bubbles: true, data: term, inputType: "insertText" }));
		return true;
	}, term);
}

/** Zichtbare regels in het venster met de zoekterm in de naam, met hun omgeving als bewijs. Zet data-e2e-hit op elk. */
async function treffers(term) {
	return browser.executeObsidian(({ app }, term) => {
		const modal = app.setting.modalEl;
		if (!modal) return [];
		for (const el of Array.from(modal.querySelectorAll("[data-e2e-hit]"))) el.removeAttribute("data-e2e-hit");
		const laag = term.toLowerCase();
		const heeft = (el) => (el.textContent ?? "").toLowerCase().includes(laag);
		const zichtbaar = (el) => el.getClientRects().length > 0;
		let namen = Array.from(modal.querySelectorAll(".setting-item-name")).filter((el) => zichtbaar(el) && heeft(el));
		if (namen.length === 0) {
			// Toont Obsidian treffers op een andere manier, pak dan de kleinste zichtbare elementen met de term.
			namen = Array.from(modal.querySelectorAll("*")).filter((el) => zichtbaar(el) && el.tagName !== "INPUT" && heeft(el) && !Array.from(el.children).some(heeft));
		}
		return namen.map((el, i) => {
			el.setAttribute("data-e2e-hit", String(i));
			const rij = el.closest(".setting-item") ?? el.parentElement;
			// In de zoekuitslag: de naam van de gevonden regel en de kop van zijn groep (het kind van de
			// groep dat niet de lijst met treffers is).
			const item = el.closest(".setting-search-result-item");
			const groep = el.closest(".setting-search-result-group");
			const kop = groep ? Array.from(groep.children).find((c) => !c.classList.contains("setting-search-result-group-items")) : null;
			const voorouders = [];
			for (let a = el.parentElement, n = 0; a && a !== modal && n < 7; a = a.parentElement, n++) voorouders.push(`${a.tagName.toLowerCase()}.${a.className}`);
			let omgeving = "";
			for (let a = el.parentElement, n = 0; a && a !== modal && n < 5; a = a.parentElement, n++) {
				if (/rollwright/i.test(a.textContent ?? "")) { omgeving = (a.textContent ?? "").slice(0, 200); break; }
			}
			return {
				titel: (item?.querySelector(".vertical-tab-nav-item-title")?.textContent ?? "").trim(),
				groep: (kop?.textContent ?? "").trim(),
				groepKlasse: kop ? `${kop.tagName.toLowerCase()}.${kop.className}` : "",
				tekst: (el.textContent ?? "").trim(),
				klasse: el.className,
				html: el.innerHTML.slice(0, 200),
				rij: (rij?.textContent ?? "").trim().slice(0, 200),
				rijKlasse: rij?.className ?? "",
				voorouders,
				rollwrightInBuurt: omgeving,
			};
		});
	}, term);
}

/** Klik op het eerste element in het venster dat bij de selector past. */
async function klik(sel, laatste = false) {
	return browser.executeObsidian(({ app }, sel, laatste) => {
		const alle = Array.from(app.setting.modalEl?.querySelectorAll(sel) ?? []);
		const el = laatste ? alle[alle.length - 1] : alle[0];
		if (!el) return false;
		el.click();
		return true;
	}, sel, laatste);
}

/** De Rollwright-tab: aantal formulerijen, en hoe vaak een naam of uitleg er staat. */
async function tabStaat(naam, uitleg) {
	return browser.executeObsidian(({ app }, naam, uitleg) => {
		const el = app.setting.pluginTabs.find((t) => t.id === "rollwright")?.containerEl;
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

/** Het tekstveld van de regel met deze naam in de Rollwright-tab: lezen, of typen (waarde plus input-event). */
async function veld(naam, typ) {
	let uit = null;
	await browser.waitUntil(async () => {
		uit = await browser.executeObsidian(({ app }, naam, typ) => {
			const el = app.setting.pluginTabs.find((t) => t.id === "rollwright")?.containerEl;
			const rij = Array.from(el?.querySelectorAll(".setting-item") ?? []).find((it) => (it.querySelector(".setting-item-name")?.textContent ?? "").trim() === naam);
			const input = rij?.querySelector("input[type=text], input:not([type])");
			if (!input || input.getClientRects().length === 0) return null;
			if (typ !== null) {
				input.focus();
				input.value = typ;
				input.dispatchEvent(new InputEvent("input", { bubbles: true, data: typ, inputType: "insertText" }));
			}
			return input.value;
		}, naam, typ);
		return uit !== null;
	}, { timeout: 10000, timeoutMsg: `geen tekstveld bij ${naam} in de Rollwright-tab` });
	return uit;
}

async function opgeslagenZijden() {
	return browser.executeObsidian(async ({ app }) => (await app.plugins.plugins.rollwright.loadData())?.defaultSides);
}

describe("Rollwright: zoeken in de instellingen (OPEN.md punt 20)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		const versie = await browser.executeObsidian(({ obsidian }) => ({ api: obsidian.apiVersion, nieuw: obsidian.requireApiVersion("1.13.0") }));
		console.log("OBSIDIAN VERSIE:", JSON.stringify(versie));
	});

	after(async function () {
		await browser.executeObsidian(({ app }) => { app.setting.close(); });
	});

	it("typen in het zoekveld vindt Default die, Skin en License key van Rollwright", async function () {
		await openInstellingen("editor");
		const zoekveld = await vindZoekveld();
		console.log("VELDEN IN HET VENSTER:", JSON.stringify(zoekveld.velden));
		expect(zoekveld.gevonden).toBe(true);
		expect(await treffers("Default die")).toEqual([]);

		for (const [n, term] of TERMEN.entries()) {
			expect(await zoek(term)).toBe(true);
			let hits = [];
			await browser.waitUntil(async () => {
				hits = await treffers(term);
				return hits.some((h) => vanRollwright(h, term));
			}, { timeout: 10000, timeoutMsg: `zoeken op "${term}" vond de regel van Rollwright niet` }).catch(async (e) => {
				console.log(`ZOEK "${term}" TREFFERS TOT NU:`, JSON.stringify(hits, null, 1));
				console.log("VENSTER TEKST:", JSON.stringify(await browser.executeObsidian(({ app }) => (app.setting.modalEl?.innerText ?? "").slice(0, 1500))));
				throw e;
			});
			console.log(`ZOEK "${term}": treffers onder de kop Rollwright: ${hits.filter((h) => vanRollwright(h, term)).length}`);
			console.log(`ZOEK "${term}": ${hits.length} treffers:`, JSON.stringify(hits, null, 1));
			console.log(`ZOEK "${term}": actieve tab ${await actieveTab()}`);
			await foto(`zoek-${n + 1}-${term.replace(/ /g, "-").toLowerCase()}`);
		}
	});

	it("een gevonden regel aanklikken opent de Rollwright-tab op de goede plek", async function () {
		await zoek("Default die");
		let hits = [];
		await browser.waitUntil(async () => {
			hits = await treffers("Default die");
			return hits.some((h) => vanRollwright(h, "Default die"));
		}, { timeout: 10000, timeoutMsg: "Default die werd niet weer gevonden onder de kop Rollwright" });
		// Obsidian 1.15 toont een treffer als .setting-search-result-item in de zijbalk, onder een groep met de
		// naam van de tab (Rollwright), zonder de uitleg (run 42401543789).
		const i = hits.findIndex((h) => vanRollwright(h, "Default die"));
		console.log("KLIK OP TREFFER:", JSON.stringify(hits[i]));

		// Eerst de naam, dan de hele treffer. Allebei de gevonden regel zelf; een klik op de groepskop telt niet.
		const pogingen = [
			["naam", `[data-e2e-hit="${i}"]`],
			["treffer", `.setting-search-result-item:has([data-e2e-hit="${i}"])`],
		];
		let geopend = false;
		for (const [wat, sel] of pogingen) {
			if (!(await klik(sel))) { console.log(`KLIK ${wat}: niet gevonden`); continue; }
			geopend = await browser.waitUntil(async () => (await actieveTab()) === "rollwright", { timeout: 4000 }).catch(() => false);
			const zoektekst = await browser.executeObsidian(({ app }) => app.setting.modalEl?.querySelector("[data-e2e-zoek]")?.value ?? "(zoekveld weg)");
			console.log(`KLIK ${wat}: actieve tab ${await actieveTab()}, zoekveld "${zoektekst}", geopend ${geopend}`);
			if (geopend) break;
		}
		const plek = await browser.executeObsidian(({ app }) => {
			const el = app.setting.pluginTabs.find((t) => t.id === "rollwright")?.containerEl;
			const rij = Array.from(el?.querySelectorAll(".setting-item") ?? []).find((it) => (it.querySelector(".setting-item-name")?.textContent ?? "").trim() === "Default die");
			if (!rij) return null;
			const r = rij.getBoundingClientRect();
			const vak = (el.closest(".vertical-tab-content-container") ?? el).getBoundingClientRect();
			return { klasse: rij.className, zichtbaar: rij.getClientRects().length > 0 && r.top >= vak.top - 1 && r.bottom <= vak.bottom + 1, actieveTab: app.setting.activeTab?.id ?? null };
		});
		console.log("NA DE KLIK, REGEL DEFAULT DIE IN DE TAB:", JSON.stringify(plek));
		await foto("zoek-4-na-klik");
		// Obsidian 1.15 opent bij deze klik altijd de tab (run 42420553342), dus geen tab is een fout, geen reden om over te slaan.
		if (!geopend) throw new Error(`een klik op de treffer Default die opende de Rollwright-tab niet (actieve tab ${plek?.actieveTab ?? "onbekend"}); zie KLIK hierboven`);
		expect(plek?.actieveTab).toBe("rollwright");
		expect(plek?.zichtbaar).toBe(true);
	});

	it("naam en uitleg staan er maar één keer in de Rollwright-tab", async function () {
		await vindZoekveld();
		await zoek("");
		await browser.executeObsidian(({ app }) => { app.setting.openTabById("rollwright"); });
		await veld("Default die", null);
		for (const [naam, uitleg] of [["Default die", "number of sides"], ["Skin", "All rolling is free"], ["License key", "once every 30 days"]]) {
			const s = await tabStaat(naam, uitleg);
			console.log(`DUBBEL? ${naam}: ${s.namen} keer de naam, ${s.uitleg} keer de uitleg`);
			expect(s.namen).toBe(1);
			expect(s.uitleg).toBe(1);
		}
		await foto("zoek-5-tab");
	});

	it("Add en de prullenbak tekenen de tab opnieuw", async function () {
		const voor = await tabStaat("Default die", "number of sides");
		console.log("FORMULES VOOR ADD:", JSON.stringify(voor));
		const knop = await browser.executeObsidian(({ app }) => {
			const el = app.setting.pluginTabs.find((t) => t.id === "rollwright")?.containerEl;
			const b = Array.from(el?.querySelectorAll("button") ?? []).find((x) => (x.textContent ?? "").trim() === "Add");
			b?.click();
			return !!b;
		});
		expect(knop).toBe(true);
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
		await foto("zoek-6-na-add");

		expect(await klik('.clickable-icon[aria-label="Remove"]', true)).toBe(true);
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
		await veld("Default die", "12");
		await browser.waitUntil(async () => (await opgeslagenZijden()) === 12, { timeout: 10000, timeoutMsg: "12 werd niet opgeslagen" });
		await sluitInstellingen();
		await openInstellingen("rollwright");
		const waarde = await veld("Default die", null);
		const opgeslagen = await opgeslagenZijden();
		console.log(`BEWAARD: was ${oud}, getypt 12, na weer openen staat er "${waarde}", in data.json ${opgeslagen}`);
		expect(waarde).toBe("12");
		expect(opgeslagen).toBe(12);

		await veld("Default die", String(oud));
		await browser.waitUntil(async () => (await opgeslagenZijden()) === oud, { timeout: 10000, timeoutMsg: "de oude waarde kwam niet terug" });
	});
});
