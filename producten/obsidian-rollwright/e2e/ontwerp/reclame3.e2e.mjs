import { browser } from "@wdio/globals";
import * as fs from "fs";

// Ontwerptest van Daan (run 38): ruwe beelden voor GIF en poster v3, in een rijke sessienotitie
// met kaart, en het logboek rechts dat live vult. Daarna dezelfde NAT 20 in de optionele skins.
const SHOTS = "screenshots";
const NOTE = "Session 12.md";
const stap = async (naam, fn) => { try { await fn(); } catch (e) { console.log("STAP MISLUKT:", naam, String(e).slice(0, 300)); } };
const save = async (naam) => { await browser.saveScreenshot(`${SHOTS}/${naam}.png`); };
const zetVast = async (v) => browser.execute((v) => { if (!window.__rwRandom) window.__rwRandom = Math.random; Math.random = () => v; }, v);
const losKans = async () => browser.execute(() => { if (window.__rwRandom) { Math.random = window.__rwRandom; window.__rwRandom = undefined; } });
const zoom = async (f) => { await browser.execute((f) => { try { window.require("electron").webFrame.setZoomFactor(f); } catch (e) { document.body.style.zoom = String(f); } }, f); await browser.pause(700); };
const muisWeg = async () => {
	try { await browser.$(".view-header-title-container, .view-header").moveTo(); } catch (e) {}
	await browser.execute(() => { document.querySelectorAll(".tooltip").forEach((t) => t.remove()); document.activeElement?.blur(); });
};
const tokens = () => browser.execute(() => [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null)
	.map((x, i) => { const b = x.getBoundingClientRect(); const z = window.devicePixelRatio; return { i, t: x.textContent.trim().slice(0, 40), x: Math.round(b.x * z), y: Math.round(b.y * z), w: Math.round(b.width * z), h: Math.round(b.height * z) }; }));
const klik = (i) => browser.execute((i) => { const a = [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null); a[i]?.click(); return a.length; }, i);
const skin = (s) => browser.execute((s) => { for (const c of Array.from(document.body.classList)) if (c.startsWith("rollwright-skin-")) document.body.classList.remove(c); document.body.classList.add(`rollwright-skin-${s}`); }, s);
const meta = {};
let f = 0;
const frame = async (wat) => { f += 1; const n = `f-${String(f).padStart(3, "0")}-${wat}`; await save(n); return n; };
const worp = async (label, i, kans, duur = 1150) => {
	meta[label] = await tokens();
	await frame(`${label}-voor`);
	await zetVast(kans);
	const t0 = Date.now();
	await klik(i);
	while (Date.now() - t0 < duur) await frame(`${label}-${Date.now() - t0}ms`);
	await losKans();
	await browser.pause(250);
	await frame(`${label}-rust`);
};

describe("Rollwright reclame 3", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.setWindowSize(1400, 860).catch(() => {});
		await browser.executeObsidian(({ app }) => { app.vault.setConfig("spellcheck", false); app.customCss.setTheme(""); app.changeTheme("obsidian"); }).catch(() => {});
		await browser.executeObsidian(async ({ app }, pad) => {
			await app.plugins.plugins.rollwright.clearHistory();
			app.workspace.leftSplit?.collapse();
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(app.vault.getAbstractFileByPath(pad), { state: { mode: "preview" } });
			app.workspace.setActiveLeaf(leaf, { focus: true });
		}, NOTE);
		await browser.pause(1500);
		await browser.executeObsidian(({ app }) => app.commands.executeCommandById("rollwright:open-history"));
		await browser.pause(1200);
		// Het logboek opent rechts; de notitie weer actief maken zodat de klikken in de notitie landen.
		await browser.executeObsidian(({ app }) => { const l = app.workspace.getLeavesOfType("markdown")[0]; if (l) app.workspace.setActiveLeaf(l, { focus: true }); });
		await zoom(1.2);
		await muisWeg();
	});

	it("worpen met logboek, standaard donker", async function () {
		await stap("start", async () => { meta.start = await tokens(); await frame("start"); });
		// Volgorde in de notitie: 0 Initiative, 1 Attack, 2 Damage, 3 Perception, 4 tabel.
		await stap("ini", () => worp("ini", 0, 0.62));
		await stap("att", () => worp("att", 1, 0.8, 900));
		await stap("dmg", () => worp("dmg", 2, 0.85, 900));
		await stap("per", () => worp("per", 3, 0.99999, 1400));
		await stap("tab", () => worp("tab", 4, 0.01, 900));
		await stap("held", async () => { await muisWeg(); await save("held-donker"); });
	});

	for (const s of ["parchment", "arcane"]) {
		it(`NAT 20 in skin ${s}`, async function () {
			await stap(s, async () => { await skin(s); await browser.pause(500); await worp(`skin-${s}`, 3, 0.99999, 1400); await save(`held-${s}`); });
		});
	}

	after(async function () {
		await skin("classic");
		fs.writeFileSync(`${SHOTS}/meta.json`, JSON.stringify(meta, null, 1));
	});
});
