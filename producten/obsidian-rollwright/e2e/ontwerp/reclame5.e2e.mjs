import { browser } from "@wdio/globals";
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

// Ontwerptest van Daan (reclame 5, film v4): de echte plugin in een rijke sessienotitie. Het uiterlijk van de
// notitie (perkament, letters, banner, wolf en val) is een snippet en inhoud van de gebruiker, niet van Rollwright.
const SHOTS = "screenshots";
const NOTE = "The Drowned Lantern.md";
const HIER = path.dirname(fileURLToPath(import.meta.url));
const stap = async (naam, fn) => { try { await fn(); } catch (e) { console.log("STAP MISLUKT:", naam, String(e).slice(0, 300)); } };
const save = async (naam) => { await browser.saveScreenshot(`${SHOTS}/${naam}.png`); };
const zetVast = async (v) => browser.execute((v) => { if (!window.__rwRandom) window.__rwRandom = Math.random; Math.random = () => v; }, v);
const losKans = async () => browser.execute(() => { if (window.__rwRandom) { Math.random = window.__rwRandom; window.__rwRandom = undefined; } });
const zoom = async (f) => { await browser.execute((f) => { try { window.require("electron").webFrame.setZoomFactor(f); } catch (e) { document.body.style.zoom = String(f); } }, f); await browser.pause(700); };
const muisWeg = async () => {
	try { await browser.$(".view-header-title-container, .view-header").moveTo(); } catch (e) {}
	await browser.execute(() => { document.querySelectorAll(".tooltip").forEach((t) => t.remove()); document.activeElement?.blur(); });
};
const tokens = () => browser.execute(() => [...document.querySelectorAll(".workspace-leaf-content[data-type=\"markdown\"] .rollwright-roll")].filter((x) => x.offsetParent !== null)
	.map((x, i) => { const b = x.getBoundingClientRect(); const z = window.devicePixelRatio; return { i, t: x.textContent.trim().slice(0, 40), cls: x.className, x: Math.round(b.x * z), y: Math.round(b.y * z), w: Math.round(b.width * z), h: Math.round(b.height * z) }; }));
const klik = (i) => browser.execute((i) => { const a = [...document.querySelectorAll(".workspace-leaf-content[data-type=\"markdown\"] .rollwright-roll")].filter((x) => x.offsetParent !== null); a[i]?.click(); return a.length; }, i);
const skin = (s) => browser.execute((s) => { for (const c of Array.from(document.body.classList)) if (c.startsWith("rollwright-skin-")) document.body.classList.remove(c); document.body.classList.add(`rollwright-skin-${s}`); }, s);
const scrollTo = (y) => browser.execute((y) => { const sc = document.querySelector(".workspace-leaf-content[data-type=\"markdown\"] .markdown-preview-view"); if (sc) sc.scrollTop = y; return sc?.scrollTop; }, y);
const plek = (tekst) => browser.execute((t) => { const sc = document.querySelector(".workspace-leaf-content[data-type=\"markdown\"] .markdown-preview-view"); if (!sc) return null; const el = [...sc.querySelectorAll("p, .callout")].find((p) => p.textContent.includes(t)); return el ? Math.round(el.getBoundingClientRect().top - sc.getBoundingClientRect().top + sc.scrollTop) : null; }, tekst);
const meta = { scroll: {} };
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
const glij = async (van, naar, stappen, label) => {
	for (let s = 1; s <= stappen; s++) { const t = s / stappen; const e = t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2; await scrollTo(Math.round(van + (naar - van) * e)); await frame(`${label}-${s}`); }
};

describe("Rollwright reclame 5 (film v4)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.setWindowSize(1400, 860).catch(() => {});
		const css = fs.readFileSync(path.join(HIER, "drowned.css"), "utf8");
		const ok = await browser.executeObsidian(async ({ app }, css) => {
			app.vault.setConfig("spellcheck", false);
			app.customCss.setTheme(""); app.changeTheme("obsidian");
			const map = `${app.vault.configDir}/snippets`;
			if (!(await app.vault.adapter.exists(map))) await app.vault.adapter.mkdir(map);
			await app.vault.adapter.write(`${map}/drowned.css`, css);
			try { await app.customCss.readSnippets?.(); } catch (e) {}
			try { app.customCss.setCssEnabledStatus("drowned", true); } catch (e) {}
			await new Promise((r) => setTimeout(r, 800));
			const aan = [...document.querySelectorAll("style")].some((s) => s.textContent.includes("DL Cinzel"));
			if (!aan) { const st = document.createElement("style"); st.id = "drowned-fallback"; st.textContent = css; document.head.appendChild(st); }
			return aan ? "snippet" : "style-fallback";
		}, css);
		console.log("SNIPPET:", ok);
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
		await browser.executeObsidian(({ app }) => { const l = app.workspace.getLeavesOfType("markdown")[0]; if (l) app.workspace.setActiveLeaf(l, { focus: true }); });
		await browser.pause(1500);
		await muisWeg();
		await save("debug-start");
		await stap("plek", async () => { meta.scroll.beast = await plek("Dire wolf");
		meta.scroll.trap = await plek("Rusted jaw");
		meta.scroll.ini = await plek("Initiative");
		meta.scroll.per = await plek("The lantern flickers"); });
		meta.leaves = await browser.execute(() => [...document.querySelectorAll(".workspace-leaf-content")].map((l) => l.dataset.type + ":" + l.className));
		console.log("PLEK:", JSON.stringify(meta.scroll));
	});

	it("overzicht en worpen met logboek, standaard donker", async function () {
		await stap("top", async () => { await scrollTo(0); await browser.pause(300); meta.top = await tokens(); await frame("top"); await save("held-top"); });
		const A = Math.max(0, (meta.scroll.ini ?? 600) - 260);
		await stap("glij1", () => glij(0, A, 10, "glij1"));
		await stap("ini", () => worp("ini", 0, 0.62));
		await stap("att", () => worp("att", 1, 0.8, 900));
		await stap("dmg", () => worp("dmg", 2, 0.85, 900));
		const B = Math.max(A, (meta.scroll.trap ?? 1200) - 140);
		await stap("glij2", () => glij(A, B, 10, "glij2"));
		await stap("dex", () => worp("dex", 3, 0, 1300));
		await stap("per", () => worp("per", 4, 0.99999, 1400));
		await stap("tab", () => worp("tab", 5, 0.4, 900));
		await stap("held", async () => { await muisWeg(); await save("held-donker"); meta.held = await tokens(); });
		await stap("held-a", async () => { await scrollTo(A); await browser.pause(300); await save("held-a"); meta.heldA = await tokens(); });
	});

	for (const s of ["parchment", "arcane"]) {
		it(`NAT 20 in skin ${s}`, async function () {
			await stap(s, async () => {
				const B = Math.max(0, (meta.scroll.trap ?? 1200) - 140); await scrollTo(B); await browser.pause(200);
				await skin(s); await browser.pause(500); await worp(`skin-${s}`, 4, 0.99999, 1400); await save(`held-${s}`);
			});
		});
	}

	it("groot: de NAT 20 op zoom 2", async function () {
		await stap("groot", async () => {
			await skin("classic");
			await zoom(2);
			const r = await browser.execute(() => { const t = [...document.querySelectorAll(".workspace-leaf-content[data-type=\"markdown\"] .rollwright-roll")].filter((x) => x.offsetParent !== null)[4]; t?.scrollIntoView({ block: "center" }); const b = t?.getBoundingClientRect(); const z = window.devicePixelRatio; return b ? { x: Math.round(b.x * z), y: Math.round(b.y * z), w: Math.round(b.width * z), h: Math.round(b.height * z) } : null; });
			await browser.pause(400); await muisWeg();
			meta.groot = r; await save("groot-nat20");
			await zoom(1);
		});
	});

	after(async function () {
		await skin("classic");
		fs.writeFileSync(`${SHOTS}/meta.json`, JSON.stringify(meta, null, 1));
	});
});
