import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Bouwplan notitiesfeer, stap 2: Daans CSS per skin (parchment.css, arcane.css) zit in styles.css.
// Deze spec meet de berekende achtergrond en letter (eis 1, 2 en 6) en maakt plaatjes voor Daans
// keuring (eis 8): beide skins, licht en donker, lezen en Live Preview, plus de tegels in de instellingen.
const SHOTS = "screenshots";
const MET = "Wereld css met worp.md";
const ZONDER = "Wereld css zonder worp.md";
const TEKST_MET = "# Taverne\n\nDe waard kijkt op. Aanval `dice: 1d20+5`, schade `dice: 2d6`.\n\n> [!note] Hint\n> Een **vet** woord en een [[link]].\n\n- een lijst\n- met #tag\n\nKleur uit de tabel: `dice: [[Tabellen^kleuren]]`.\n";
const TEKST_ZONDER = "# Gewoon\n\nGeen worp hier, alleen `code`.\n";

/** Achtergrond en letter van het notitievlak per open notitie in het midden, plus zijbalk en tabbalk. */
async function meet() {
	return browser.executeObsidian(({ app }) => {
		const stijl = (el) => {
			if (!el) return null;
			const s = el.ownerDocument.defaultView.getComputedStyle(el);
			return { bg: s.backgroundColor, beeld: s.backgroundImage === "none" ? "none" : "beeld", letter: s.fontFamily, kleur: s.color };
		};
		const notities = [];
		app.workspace.iterateAllLeaves((leaf) => {
			const view = leaf.view;
			if (view.getViewType() !== "markdown" || !view.file || leaf.getRoot() !== app.workspace.rootSplit) return;
			const el = view.containerEl;
			notities.push({
				pad: view.file.path,
				wereld: el.classList.contains("rollwright-world"),
				inhoud: stijl(el.querySelector(".view-content")),
				// Lopende tekst, geen kop: in lezen de eerste alinea, in Live Preview de eerste gevulde regel die geen kop is.
				tekst: stijl(
					el.querySelector(".markdown-reading-view p")?.offsetParent
						? el.querySelector(".markdown-reading-view p")
						: Array.from(el.querySelectorAll(".markdown-source-view .cm-line:not(.HyperMD-header)")).find((l) => l.textContent.trim() !== "") ?? null,
				),
			});
		});
		return {
			notities,
			zijbalk: stijl(document.querySelector(".workspace-split.mod-left-split")),
			tabbalk: stijl(document.querySelector(".workspace-tab-header-container")),
			body: stijl(document.body),
		};
	});
}

async function zet(veranderingen, donker) {
	await browser.executeObsidian(({ app }, veranderingen, donker) => {
		document.body.classList.toggle("theme-dark", donker);
		document.body.classList.toggle("theme-light", !donker);
		const plugin = app.plugins.plugins.rollwright;
		Object.assign(plugin.settings, veranderingen);
		plugin.applySkin();
	}, veranderingen, donker);
	await browser.pause(800);
}

async function modus(mode) {
	await browser.executeObsidian(async ({ app }, MET, mode) => {
		app.workspace.iterateAllLeaves((leaf) => {
			if (leaf.view.getViewType() === "markdown" && leaf.view.file?.path === MET && leaf.getRoot() === app.workspace.rootSplit) {
				void leaf.setViewState({ type: "markdown", state: { file: MET, mode: mode === "lezen" ? "preview" : "source", source: false } });
			}
		});
	}, MET, mode);
	await browser.pause(800);
}

const isRW = (letter) => /"?RW /.test(letter ?? "");
// De letter van de lopende tekst per skin (Daan: --font-text), niet die van de koppen.
const TEKSTLETTER = { parchment: "RW Fell", arcane: "RW Spectral" };

describe("Rollwright: Daans notitiewereld per skin (notitiesfeer stap 2)", function () {
	let classic = {};

	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.executeObsidian(async ({ app }, MET, ZONDER, TEKST_MET, TEKST_ZONDER) => {
			for (const [pad, tekst] of [[MET, TEKST_MET], [ZONDER, TEKST_ZONDER]]) {
				const bestaand = app.vault.getAbstractFileByPath(pad);
				if (bestaand) await app.vault.modify(bestaand, tekst);
				else await app.vault.create(pad, tekst);
			}
			const links = app.workspace.getLeaf("tab");
			await links.openFile(app.vault.getAbstractFileByPath(MET), { state: { mode: "preview" } });
			const rechts = app.workspace.getLeaf("split", "vertical");
			await rechts.openFile(app.vault.getAbstractFileByPath(ZONDER), { state: { mode: "preview" } });
			app.workspace.leftSplit.expand?.();
		}, MET, ZONDER, TEKST_MET, TEKST_ZONDER);
		await browser.pause(1000);
		for (const donker of [false, true]) {
			await zet({ skin: "classic", licenseKey: "E2E-SLEUTEL", licenseCheckedAt: Date.now(), noteWorld: "rolls" }, donker);
			classic[donker ? "donker" : "licht"] = await meet();
		}
		console.log("WERELD-CSS classic:", JSON.stringify(classic));
	});

	after(async function () {
		await zet({ skin: "classic", licenseKey: "", licenseCheckedAt: 0, noteWorld: "rolls" }, false);
	});

	it("eis 1: Classic zet geen wereldletter en geen andere achtergrond", async function () {
		for (const stand of Object.values(classic)) {
			expect(stand.notities.length).toBe(2);
			for (const n of stand.notities) {
				expect(n.wereld).toBe(false);
				expect(isRW(n.tekst?.letter)).toBe(false);
			}
			// Beide notities hebben dezelfde achtergrond: die van het thema.
			expect(stand.notities[0].inhoud.bg).toBe(stand.notities[1].inhoud.bg);
		}
	});

	for (const skin of ["parchment", "arcane"]) {
		for (const donker of [false, true]) {
			const thema = donker ? "donker" : "licht";
			it(`eis 2 en 6: ${skin} ${thema}: alleen de notitie met worp wordt een wereld, de rest blijft het thema`, async function () {
				await zet({ skin, licenseKey: "E2E-SLEUTEL", licenseCheckedAt: Date.now(), noteWorld: "rolls" }, donker);
				await modus("lezen");
				const m = await meet();
				console.log(`WERELD-CSS ${skin} ${thema}:`, JSON.stringify(m));
				const met = m.notities.find((n) => n.pad === MET);
				const zonder = m.notities.find((n) => n.pad === ZONDER);
				const basis = classic[thema];
				expect(met.wereld).toBe(true);
				expect(zonder.wereld).toBe(false);
				// Eis 2: andere achtergrond (kleur of textuur) en de letter van de skin.
				expect(met.inhoud.bg !== zonder.inhoud.bg || met.inhoud.beeld !== zonder.inhoud.beeld).toBe(true);
				expect(met.tekst.letter).toContain(TEKSTLETTER[skin]);
				expect(isRW(zonder.tekst.letter)).toBe(false);
				// Eis 6: de notitie zonder worp, de zijbalk en de tabbalk zien eruit als bij Classic.
				expect(zonder.inhoud).toEqual(basis.notities.find((n) => n.pad === ZONDER).inhoud);
				expect(zonder.tekst).toEqual(basis.notities.find((n) => n.pad === ZONDER).tekst);
				expect(m.zijbalk).toEqual(basis.zijbalk);
				expect(m.tabbalk).toEqual(basis.tabbalk);
				await browser.saveScreenshot(`${SHOTS}/wereld-${skin}-${thema}-lezen.png`);
				await modus("lp");
				const lp = await meet();
				const metLp = lp.notities.find((n) => n.pad === MET);
				console.log(`WERELD-CSS ${skin} ${thema} live preview:`, JSON.stringify(metLp));
				expect(metLp.wereld).toBe(true);
				expect(metLp.tekst.letter).toContain(TEKSTLETTER[skin]);
				await browser.saveScreenshot(`${SHOTS}/wereld-${skin}-${thema}-lp.png`);
				await modus("lezen");
			});
		}
	}

	// Plaatjes van de tegels maakt skin-tegels.e2e.mjs (eigen venster van de instellingen); hier de regel zelf.
	it("de tegels in de instellingen hebben de regel onder de betaalde skins, leesbaar op hun eigen achtergrond", async function () {
		await zet({ skin: "parchment", licenseKey: "", licenseCheckedAt: 0, noteWorld: "rolls" }, false);
		await browser.executeObsidian(({ app }) => {
			app.setting.open();
			app.setting.openTabById("rollwright");
		});
		await browser.waitUntil(async () => browser.executeObsidian(({ app }) => (app.setting.modalEl?.querySelectorAll(".rollwright-skin-preview-tile").length ?? 0) === 3),
			{ timeout: 10000, timeoutMsg: "de skin-tegels kwamen niet in beeld" });
		for (const donker of [false, true]) {
			const regels = await browser.executeObsidian(({ app }, donker) => {
				const modal = app.setting.modalEl;
				for (const d of new Set([document, modal.ownerDocument])) {
					d.body.classList.toggle("theme-dark", donker);
					d.body.classList.toggle("theme-light", !donker);
				}
				modal.querySelector(".rollwright-skin-preview")?.scrollIntoView({ block: "center" });
				return Array.from(modal.querySelectorAll(".rollwright-skin-preview-tile")).map((tegel) => {
					const regel = tegel.querySelector(".rollwright-skin-preview-tagline");
					const r = tegel.getBoundingClientRect();
					const rr = regel?.getBoundingClientRect();
					return {
						tekst: regel?.textContent ?? null,
						kleur: regel ? regel.ownerDocument.defaultView.getComputedStyle(regel).color : null,
						binnen: rr ? rr.left >= r.left && rr.right <= r.right && rr.bottom <= r.bottom : null,
					};
				});
			}, donker);
			console.log(`WERELD-CSS tegels ${donker ? "donker" : "licht"}:`, JSON.stringify(regels));
			expect(regels.map((r) => r.tekst)).toEqual([null, "Turns the whole note into old parchment", "Turns the whole note into a torch-lit dungeon"]);
			expect(regels.filter((r) => r.tekst).every((r) => r.binnen)).toBe(true);
			// Vaste kleur per tegel, in licht en donker gelijk (de tegels hebben een vaste achtergrond).
			expect(regels.map((r) => r.kleur)).toEqual([null, "rgb(90, 58, 30)", "rgb(185, 194, 188)"]);
		}
		await browser.executeObsidian(({ app }) => app.setting.close());
	});
	// Daan (9 nov 10:55): tabeluitkomsten in beeld, in Parchment en Arcane, en Arcane met de wereld uit in een licht thema.
	// Gemeten: de letterkleur van de uitkomst tegen zijn eigen vlak (over het vlak van de notitie gelegd), minstens 3 op 1.
	const TABEL_STANDEN = [
		{ naam: "parchment-licht", skin: "parchment", donker: false, wereld: "rolls", isWereld: true },
		{ naam: "parchment-donker", skin: "parchment", donker: true, wereld: "rolls", isWereld: true },
		{ naam: "arcane-licht", skin: "arcane", donker: false, wereld: "rolls", isWereld: true },
		{ naam: "arcane-donker", skin: "arcane", donker: true, wereld: "rolls", isWereld: true },
		{ naam: "arcane-wereld-uit-licht", skin: "arcane", donker: false, wereld: "off", isWereld: false },
		{ naam: "parchment-wereld-uit-donker", skin: "parchment", donker: true, wereld: "off", isWereld: false },
	];
	for (const stand of TABEL_STANDEN) {
		it(`tabeluitkomst ${stand.naam}: een kleur uit de tabel, leesbaar op zijn vlak`, async function () {
			await zet({ skin: stand.skin, licenseKey: "E2E-SLEUTEL", licenseCheckedAt: Date.now(), noteWorld: stand.wereld }, stand.donker);
			await modus("lezen");
			const uit = await browser.executeObsidian(({ app }, MET) => {
				const kleur = (txt) => {
					const m = txt.match(/rgba?\(([^)]+)\)/);
					if (!m) return null;
					const d = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number);
					return { r: d[0], g: d[1], b: d[2], a: d.length > 3 ? d[3] : 1 };
				};
				let leaf = null;
				app.workspace.iterateAllLeaves((l) => { if (l.view.getViewType() === "markdown" && l.view.file?.path === MET && l.getRoot() === app.workspace.rootSplit) leaf = l; });
				const el = leaf?.view.containerEl.querySelector(".markdown-reading-view .rollwright-roll.rollwright-text");
				if (!el) return null;
				el.scrollIntoView({ block: "center" });
				const win = el.ownerDocument.defaultView;
				const s = win.getComputedStyle(el);
				// Het eerste niet-doorzichtige vlak onder de uitkomst.
				let onder = null;
				for (let p = el.parentElement; p && !onder; p = p.parentElement) {
					const c = kleur(win.getComputedStyle(p).backgroundColor);
					if (c && c.a > 0.5) onder = c;
				}
				onder ??= document.body.classList.contains("theme-dark") ? { r: 30, g: 30, b: 30, a: 1 } : { r: 255, g: 255, b: 255, a: 1 };
				const eigen = kleur(s.backgroundColor) ?? { r: 0, g: 0, b: 0, a: 0 };
				const vlak = ["r", "g", "b"].reduce((o, k) => ({ ...o, [k]: eigen[k] * eigen.a + onder[k] * (1 - eigen.a) }), {});
				const lum = (c) => {
					const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
					return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b);
				};
				const letter = kleur(s.color);
				const [a, b] = [lum(letter), lum(vlak)].sort((x, y) => y - x);
				return {
					tekst: el.querySelector(".rollwright-value")?.textContent ?? el.textContent,
					wereld: leaf.view.containerEl.classList.contains("rollwright-world"),
					kleur: s.color, vlak: s.backgroundColor, beeld: s.backgroundImage === "none" ? "none" : "beeld", rand: s.borderColor,
					contrast: Math.round(((a + 0.05) / (b + 0.05)) * 100) / 100,
				};
			}, MET);
			console.log(`WERELD-CSS tabel ${stand.naam}:`, JSON.stringify(uit));
			await browser.saveScreenshot(`${SHOTS}/tabel-${stand.naam}.png`);
			expect(uit).not.toBe(null);
			expect(["Rood", "Blauw", "Groen"].some((k) => uit.tekst.includes(k))).toBe(true);
			expect(uit.wereld).toBe(stand.isWereld);
			// Een vlak met een verloop of textuur kan niet als één kleur gemeten worden; daar beslist het plaatje.
			if (uit.beeld === "none") expect(uit.contrast).toBeGreaterThanOrEqual(3);
		});
	}
});
