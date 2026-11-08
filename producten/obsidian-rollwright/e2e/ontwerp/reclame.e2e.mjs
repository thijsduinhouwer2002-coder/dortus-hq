import { browser } from "@wdio/globals";
import * as fs from "fs";

// Ontwerptest van Daan: ruwe beelden voor de lijstplaatjes (poster) en de GIF in de README.
// De poster en de GIF zelf maakt Daan daarna uit deze plaatjes (bijsnijden, kop erbij).
const SHOTS = "screenshots";
const stap = async (naam, fn) => {
	try { await fn(); } catch (e) { console.log("STAP MISLUKT:", naam, String(e).slice(0, 300)); }
};
const save = async (naam) => { const f = `${SHOTS}/${naam}.png`; await browser.saveScreenshot(f); return f; };
const NOTE = "Rollwright example.md";
const thema = async (naam, licht) => {
	await browser.executeObsidian(({ app }, naam, licht) => { app.customCss.setTheme(naam); app.changeTheme(licht ? "moonstone" : "obsidian"); }, naam, licht);
	await browser.pause(1200);
};
const open = async (pad, mode) => {
	await browser.executeObsidian(async ({ app }, pad, mode) => {
		const leaf = app.workspace.getLeaf(false);
		await leaf.openFile(app.vault.getAbstractFileByPath(pad), { state: { mode, source: false } });
		app.workspace.setActiveLeaf(leaf, { focus: true });
	}, pad, mode);
	await browser.pause(1500);
};
const zoom = async (f) => {
	await browser.execute((f) => { try { window.require("electron").webFrame.setZoomFactor(f); } catch (e) { document.body.style.zoom = String(f); } }, f);
	await browser.pause(700);
};
const muisWeg = async () => {
	try { await browser.$(".view-header-title-container, .view-header").moveTo(); } catch (e) {}
	await browser.execute(() => { document.querySelectorAll(".tooltip").forEach((t) => t.remove()); document.activeElement?.blur(); });
};
const zetKans = async (h) => browser.execute((h) => { if (!window.__rwRandom) window.__rwRandom = Math.random; Math.random = () => (h ? 0.99999 : 0); }, h);
const zetVast = async (v) => browser.execute((v) => { if (!window.__rwRandom) window.__rwRandom = Math.random; Math.random = () => v; }, v);
const losKans = async () => browser.execute(() => { if (window.__rwRandom) { Math.random = window.__rwRandom; window.__rwRandom = undefined; } });
// In de voorbeeldnotitie staat "Initiative" buiten het token, dus ook klikken op volgorde: 0 Initiative,
// 1 Hit, 2 Damage, 3 Wisdom save, 4 gasten, 5 geruchten.
const VOLG = { Initiative: 0, Hit: 1, Damage: 2, Wisdom: 3, bar: 4, stranger: 5 };
const klik = async (woord, opVolgorde = true) => browser.execute((w, i) => {
	const alle = [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null);
	const r = alle.find((x) => x.textContent.includes(w)) ?? (i === undefined ? undefined : alle[i]);
	r?.click();
	return !!r;
}, woord, opVolgorde ? VOLG[woord] : undefined);
const zijDicht = async () => browser.executeObsidian(({ app }) => { app.workspace.leftSplit?.collapse(); app.workspace.rightSplit?.collapse(); });
// Waar de notitie op het scherm staat (in CSS-pixels van het venster), om later bij te snijden.
const kader = async () => browser.execute(() => {
	const el = document.querySelector(".workspace-leaf.mod-active .markdown-reading-view .markdown-preview-sizer")
		?? document.querySelector(".workspace-leaf.mod-active .cm-sizer");
	const b = el?.getBoundingClientRect();
	return b ? { x: b.x, y: b.y, w: b.width, h: b.height, vw: window.innerWidth, vh: window.innerHeight, dpr: window.devicePixelRatio } : null;
});

describe("Rollwright reclame: beelden voor poster en GIF", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.setWindowSize(1280, 820).catch(() => {});
		await browser.executeObsidian(({ app }) => app.vault.setConfig("spellcheck", false)).catch(() => {});
		// De voorbeeldnotitie zoals Olaf hem maakt (klus 6).
		await browser.executeObsidian(async ({ app }) => {
			const p = app.plugins.plugins.rollwright;
			await p.clearHistory();
			app.commands.executeCommandById("rollwright:create-example-note");
		});
		await browser.pause(2000);
		await zijDicht();
	});

	it("poster: voorbeeldnotitie met crit, donker en licht", async function () {
		for (const licht of [false, true]) {
			const kant = licht ? "licht" : "donker";
			await stap(`poster ${kant}`, async () => {
				await thema("", licht);
				await open(NOTE, "preview");
				await zoom(1.35);
				// Vaste, mooie uitkomsten: crit op de saving throw, een hoge hit.
				await zetVast(0.7); await klik("Initiative"); await browser.pause(700);
				await zetVast(0.8); await klik("Hit"); await browser.pause(700);
				await zetVast(0.6); await klik("Damage"); await browser.pause(700);
				await zetKans(true); await klik("Wisdom"); await browser.pause(1300);
				await losKans();
				await muisWeg();
				console.log(`KADER poster-${kant}:`, JSON.stringify(await kader()));
				console.log("SCHERM:", await save(`poster-ruw-${kant}`));
				await zoom(1);
			});
		}
	});

	it("poster: logboek ernaast, donker", async function () {
		await stap("poster logboek", async () => {
			await thema("", false);
			await open(NOTE, "preview");
			await browser.executeObsidian(({ app }) => app.commands.executeCommandById("rollwright:open-history"));
			await browser.pause(1200);
			await muisWeg();
			console.log("SCHERM:", await save("poster-ruw-logboek-donker"));
			await zijDicht();
		});
	});

	it("GIF: drie klikken, de derde een crit, donker", async function () {
		await stap("gif", async () => {
			await thema("", false);
			await open(NOTE, "preview");
			await zoom(1.35);
			// Begin zonder goud: de crit is het slot van de GIF, niet het begin (eerste opname run 42442883775).
			await zetVast(0.35); await klik("Wisdom"); await browser.pause(800);
			await zetVast(0.3); await klik("Damage"); await browser.pause(800);
			await losKans();
			await muisWeg();
			console.log("KADER gif:", JSON.stringify(await kader()));
			let f = 0;
			const frame = async (wat) => { f += 1; const naam = `gif-${String(f).padStart(3, "0")}-${wat}`; await save(naam); console.log("FRAME", naam, Date.now()); };
			await frame("start");
			for (const [woord, kans] of [["Initiative", 0.45], ["Damage", 0.7], ["Wisdom", "crit"]]) {
				// De muis op het token, zoals een echte klik (hover-stijl in beeld).
				await browser.execute((w) => {
					const r = [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null).find((x) => x.textContent.includes(w));
					r?.scrollIntoView({ block: "nearest" });
				}, woord);
				try {
					const el = await browser.$(`.workspace-leaf.mod-active .rollwright-roll*=${woord}`);
					if (await el.isExisting()) await el.moveTo();
				} catch (e) {}
				await frame(`hover-${woord}`);
				if (kans === "crit") await zetKans(true); else await zetVast(kans);
				const t0 = Date.now();
				await klik(woord);
				while (Date.now() - t0 < 1100) await frame(`${woord}-${Date.now() - t0}ms`);
				await losKans();
				await browser.pause(400);
				await frame(`${woord}-rust`);
			}
			await zoom(1);
		});
	});
});
