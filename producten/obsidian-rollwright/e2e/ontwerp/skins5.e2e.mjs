import { browser } from "@wdio/globals";
import * as fs from "fs";

// Daan, run 26: skins v3 (eigen vorm, letter, merkteken, beweging). Daan, run 22: skins v2 (na skins nee van Thijs). Notitie met een NAT 20 en een NAT 1.
// Daan, run 18: lijstplaatje 3. Dezelfde demonotitie in Classic, Parchment en Arcane, licht en donker,
// groot en scherp (zoom 1.5), alleen het notitievlak. De skin is alleen CSS, dus wisselen gooit niet opnieuw.
const SHOTS = "screenshots";
const NOTE = "Demo/Skins.md";
const LEAF = ".workspace-leaf.mod-active";

async function zet(skin, donker) {
	await browser.execute((skin, donker) => {
		for (const c of Array.from(document.body.classList)) if (c.startsWith("rollwright-skin-")) document.body.classList.remove(c);
		document.body.classList.add(`rollwright-skin-${skin}`);
		document.body.classList.toggle("theme-dark", donker);
		document.body.classList.toggle("theme-light", !donker);
	}, skin, donker);
	await browser.pause(700);
}

describe("Daan: drie skins voor het lijstplaatje", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.executeObsidian(async ({ app }, path) => {
			app.workspace.leftSplit?.collapse();
			app.workspace.rightSplit?.collapse();
			const file = app.vault.getAbstractFileByPath(path);
			if (!file) throw new Error(`notitie ${path} niet gevonden`);
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(file, { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		}, NOTE);
		await browser.executeObsidian(({ app }) => { app.vault.setConfig?.("showInlineTitle", false); });
		await browser.execute(() => {
			try { require("electron").webFrame.setZoomFactor(1.25); } catch (e) { console.log("zoom", e); }
			const st = document.createElement("style");
			st.textContent = ".status-bar{display:none!important}.inline-title{display:none!important}.tooltip{display:none!important}";
			document.head.appendChild(st);
		});
		await browser.waitUntil(async () => browser.execute((sel) => {
			const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`));
			return r.length >= 5 && r.every((e) => (e.textContent ?? "").trim() !== "");
		}, LEAF), { timeout: 20000, timeoutMsg: "geen worpen in de demonotitie" });
		// Gooi de tweede worp tot 20 en de derde tot 1, zodat elke skin een crit en een fumble toont.
		for (const [i, doel] of [[0, "17"], [1, "20"], [2, "1"]]) {
			for (let poging = 0; poging < 200; poging++) {
				const w = await browser.execute((sel) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`))
					.filter((r) => !r.parentElement?.closest(".rollwright-roll")).map((r) => (r.querySelector(".rollwright-value")?.textContent ?? "").trim()), LEAF);
				if (w[i] === doel) break;
				await browser.execute((sel, i) => {
					const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).filter((e) => !e.parentElement?.closest(".rollwright-roll"))[i];
					r?.click();
				}, LEAF, i);
				await browser.pause(120);
			}
		}
		await browser.pause(1500);
		await browser.$(".workspace-ribbon").moveTo().catch(() => {});
		// Muis weg, geen tooltip; wachten tot alle bewegingen klaar zijn.
		await browser.execute(() => document.activeElement?.blur?.());
		await browser.pause(1500);
	});

	for (const donker of [true, false]) {
		for (const skin of ["classic", "parchment", "arcane"]) {
			it(`${skin} ${donker ? "donker" : "licht"}`, async function () {
				await zet(skin, donker);
				const naam = `skins5-${skin}-${donker ? "donker" : "licht"}`;
				await browser.saveScreenshot(`${SHOTS}/${naam}-vol.png`);
				await browser.$(`${LEAF} .markdown-preview-sizer`).saveScreenshot(`${SHOTS}/${naam}-notitie.png`).catch((e) => console.log("crop", e));
				const kleur = await browser.execute((sel) => {
					const t = document.querySelector(`${sel} .rollwright-roll`);
					const s = t && getComputedStyle(t);
					return s ? `${s.backgroundColor} | ${s.color} | ${s.borderColor}` : "geen token";
				}, LEAF);
				console.log(`SKINS4 ${naam}: ${kleur}`);
			});
		}
	}

	// Daan, run 24: groot voor het skins-plaatje. Zoom 2.0, alleen de eerste regels (crit, fumble), scherp genoeg om groot te tonen.
	it("groot voor het skins-plaatje", async function () {
		await browser.execute(() => { try { require("electron").webFrame.setZoomFactor(2.0); } catch (e) { console.log("zoom", e); } });
		await browser.pause(1200);
		for (const donker of [true, false]) {
			for (const skin of ["classic", "parchment", "arcane"]) {
				await zet(skin, donker);
				await browser.saveScreenshot(`${SHOTS}/skins5-${skin}-${donker ? "donker" : "licht"}-groot.png`);
			}
		}
	});

	// Daan, run 26: de beweging bij het rollen per skin, vertraagd (--rw-slow 8), als reeks plaatjes van een regel.
	it("beweging per skin", async function () {
		await browser.execute(() => { try { require("electron").webFrame.setZoomFactor(2.0); } catch (e) { console.log("zoom", e); } });
		for (const skin of ["parchment", "arcane", "classic"]) {
			await zet(skin, true);
			await browser.execute(() => document.body.style.setProperty("--rw-slow", "8"));
			await browser.execute((sel) => {
				const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).filter((e) => !e.parentElement?.closest(".rollwright-roll"))[3];
				r?.scrollIntoView({ block: "center" });
			}, LEAF);
			await browser.pause(400);
			const p = await browser.execute((sel) => {
				const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).filter((e) => !e.parentElement?.closest(".rollwright-roll"))[3];
				(r?.closest("p") ?? r?.parentElement)?.setAttribute("data-daan", "regel");
				r?.click();
				return !!r;
			}, LEAF);
			const t0 = Date.now();
			for (const ms of [500, 1300, 2200, 3200, 5000, 9000]) {
				const wacht = ms - (Date.now() - t0);
				if (wacht > 0) await browser.pause(wacht);
				await browser.saveScreenshot(`${SHOTS}/skins5-beweging-${skin}-${ms}.png`);
			}
			console.log(`SKINS5 beweging ${skin}: token gevonden ${p}`);
			await browser.execute(() => document.body.style.removeProperty("--rw-slow"));
		}
	});

	// Daan, run 26: de Roll log als eigen wereld per skin.
	it("roll log per skin", async function () {
		await browser.execute(() => { try { require("electron").webFrame.setZoomFactor(1.25); } catch (e) { console.log("zoom", e); } });
		await browser.executeObsidian(async ({ app }) => {
			const note = app.workspace.getMostRecentLeaf();
			await app.plugins.plugins.rollwright.openHistory();
			app.workspace.rightSplit?.expand();
			if (note) app.workspace.setActiveLeaf(note, { focus: true });
		});
		await browser.pause(1200);
		for (const donker of [true, false]) {
			for (const skin of ["classic", "parchment", "arcane"]) {
				await zet(skin, donker);
				const naam = `skins5-log-${skin}-${donker ? "donker" : "licht"}`;
				await browser.saveScreenshot(`${SHOTS}/${naam}-vol.png`);
				await browser.$('.workspace-leaf-content[data-type="rollwright-history"]').saveScreenshot(`${SHOTS}/${naam}.png`).catch((e) => console.log("log", e));
			}
		}
	});
});
