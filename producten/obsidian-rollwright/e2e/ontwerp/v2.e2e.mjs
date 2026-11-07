import { browser } from "@wdio/globals";
import * as fs from "fs";

// Ontwerptest v2 van Daan: plaatjes van het voorstel in ontwerp-v2.md. Elke stap vangt zijn eigen fout.
const SHOTS = "screenshots";
let n = 0;
const shot = async (naam, el) => {
	n += 1;
	const file = `${SHOTS}/v2-${String(n).padStart(2, "0")}-${naam}.png`;
	if (el) await el.saveScreenshot(file); else await browser.saveScreenshot(file);
	console.log("SCHERM:", file);
};
const stap = async (naam, fn) => {
	try { await fn(); } catch (e) { console.log("STAP MISLUKT:", naam, String(e).slice(0, 300)); }
};
const NOTE = "The Rusty Flagon.md";
const open = async (pad, mode) => {
	await browser.executeObsidian(async ({ app }, pad, mode) => {
		const leaf = app.workspace.getLeaf(false);
		await leaf.openFile(app.vault.getAbstractFileByPath(pad), { state: { mode, source: false } });
		app.workspace.setActiveLeaf(leaf, { focus: true });
	}, pad, mode);
	await browser.pause(1500);
};
const thema = async (naam, licht) => {
	await browser.executeObsidian(({ app }, naam, licht) => { app.customCss.setTheme(naam); app.changeTheme(licht ? "moonstone" : "obsidian"); }, naam, licht);
	await browser.pause(1500);
};
const skin = async (s) => {
	await browser.execute((k) => {
		document.body.classList.remove("rollwright-skin-classic", "rollwright-skin-parchment", "rollwright-skin-arcane");
		document.body.classList.add(k);
	}, `rollwright-skin-${s}`);
	await browser.pause(300);
};
const klik = async (woord) => {
	await browser.execute((w) => {
		const r = [...document.querySelectorAll(".mod-root .rollwright-roll")].filter((x) => x.offsetParent !== null).find((x) => x.textContent.includes(w));
		// Nagebootst tot Olaf het bouwt (klus 2c): bewegingen op het token zelf beginnen bij elke klik opnieuw.
		if (r) { r.classList.remove("rollwright-rolled", "rollwright-crit", "rollwright-fumble"); void r.offsetWidth; }
		r?.click();
	}, woord);
};
// Echte crit en fumble (code van Olaf): Math.random even vastzetten en klikken. Het resultaat blijft
// onthouden, dus bij elke volgende keer openen staan de saving throw op 20 en de schade op 5 (2d6 + 3).
let geforceerd = false;
const zetKans = async (h) => browser.execute((h) => { if (!window.__rwRandom) window.__rwRandom = Math.random; Math.random = () => (h ? 0.99999 : 0); }, h);
const losKans = async () => browser.execute(() => { if (window.__rwRandom) { Math.random = window.__rwRandom; window.__rwRandom = undefined; } });
const markeer = async () => {
	if (geforceerd) return;
	geforceerd = true;
	await zetKans(true); await klik("Wisdom"); await browser.pause(600); await losKans();
	await zetKans(false); await klik("Damage"); await browser.pause(600); await losKans();
	const s = await browser.execute(() => [...document.querySelectorAll(".mod-root .rollwright-roll")].filter((x) => x.offsetParent !== null).map((x) => `${x.textContent.trim()} [${[...x.classList].filter((c) => c !== "rollwright-roll").join(" ")}]`));
	console.log("WORPEN NA FORCEREN:", JSON.stringify(s));
};
const zoom = async (f) => {
	await browser.execute((f) => { try { window.require("electron").webFrame.setZoomFactor(f); } catch (e) { document.body.style.zoom = String(f); } }, f);
	await browser.pause(600);
};
const zijpaneelDicht = async () => {
	await browser.executeObsidian(({ app }) => { app.workspace.leftSplit?.collapse(); app.workspace.rightSplit?.collapse(); });
};

const sluitInstellingen = async () => {
	await browser.executeObsidian(({ app }) => { try { app.setting.close(); } catch (e) {} window.__ontwerpModal?.close(); window.__ontwerpModal = undefined; });
	await browser.pause(500);
};

const openInstellingen = async () => {
	const r = await browser.executeObsidian(async ({ app }) => {
		app.setting.open();
		app.setting.openTabById("rollwright");
		await new Promise((res) => setTimeout(res, 1200));
		const el = app.setting.modalEl;
		return `zichtbaar=${!!el?.isConnected && el.getClientRects().length > 0} tab=${app.setting.activeTab?.id} tegels=${el?.querySelectorAll(".rollwright-skin-preview-tile").length}`;
	});
	await browser.pause(500);
	return r;
};

const zweef = async (selector) => {
	await browser.execute((sel) => {
		const el = document.querySelector(sel);
		if (!el) return;
		el.scrollIntoView({ block: "center" });
		for (const t of ["mouseover", "mouseenter", "mousemove"]) el.dispatchEvent(new MouseEvent(t, { bubbles: true, clientX: el.getBoundingClientRect().x + 5, clientY: el.getBoundingClientRect().y + 5 }));
	}, selector);
	await browser.pause(1200);
};

const smal = async (breed) => {
	return browser.execute((breed) => {
		const tries = [];
		try { const w = require("@electron/remote").getCurrentWindow(); w.setSize(breed, 820); tries.push("@electron/remote"); } catch (e) { tries.push("remote fout"); }
		try { const w = require("electron").remote.getCurrentWindow(); w.setSize(breed, 820); tries.push("electron.remote"); } catch (e) { tries.push("electron.remote fout"); }
		return tries.join(", ") + " breedte=" + window.innerWidth;
	}, breed);
};

describe("Rollwright v2 voorstel", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.setWindowSize(1280, 820).catch(() => {});
		await zijpaneelDicht();
	});

	it("licht en donker, lezen en Live Preview, met crit en fumble", async function () {
		for (const licht of [true, false]) {
			const kant = licht ? "licht" : "donker";
			await stap(`notitie ${kant}`, async () => {
				await thema("", licht);
				await open(NOTE, "preview");
				await browser.pause(2500);
				await markeer();
				await browser.pause(1300);
				await browser.execute(() => document.activeElement?.blur());
				await shot(`notitie-${kant}`);
				await zoom(2);
				await browser.execute(() => [...document.querySelectorAll(".mod-root .rollwright-roll")].filter((x) => x.offsetParent !== null)[0]?.scrollIntoView({ block: "start" }));
				await browser.pause(300);
				await shot(`notitie-${kant}-zoom`);
				await zoom(1);
			});
		}
		await stap("live preview", async () => {
			await thema("", true);
			await open(NOTE, "source");
			await browser.pause(2500);
			await markeer();
			await browser.pause(1300);
			await shot("live-preview-licht");
		});
	});

	it("de worp rolt, vertraagd 8 keer", async function () {
		for (const [woord, naam] of [["Initiative", "gewoon"], ["Wisdom", "crit"], ["Damage", "fumble"]]) {
			await stap(`rollen ${naam}`, async () => {
				await thema("", true);
				await open(NOTE, "preview");
				await zoom(2.5);
				await markeer();
				await browser.execute((w) => {
					const r = [...document.querySelectorAll(".mod-root .rollwright-roll")].filter((x) => x.offsetParent !== null).find((x) => x.textContent.includes(w));
					r?.scrollIntoView({ block: "center" });
				}, woord);
				await browser.pause(300);
				await browser.execute(() => document.body.style.setProperty("--rw-slow", "8"));
				if (naam !== "gewoon") await zetKans(naam === "crit");
				await klik(woord);
				let vorige = 60;
				for (const ms of [250, 900, 1800, 3500, 8000]) {
					await browser.pause(ms - vorige);
					vorige = ms;
					await shot(`rol-${naam}-${ms}ms`);
					if (ms === 250) await losKans();
				}
				await losKans();
				await browser.execute(() => document.body.style.setProperty("--rw-slow", "1"));
				await zoom(1);
			});
		}
	});

	it("het logboek", async function () {
		for (const licht of [true, false]) {
			const kant = licht ? "licht" : "donker";
			await stap(`logboek ${kant}`, async () => {
				await thema("", licht);
				await open(NOTE, "preview");
				if (licht) {
					for (const w of ["Rumour", "Initiative", "Hit", "guests", "Wisdom", "Damage", "stranger says"]) { if (w === "Wisdom" || w === "Damage") await zetKans(w === "Wisdom"); await klik(w); await browser.pause(500); await losKans(); }
				}
				await browser.executeObsidian(({ app }) => app.commands.executeCommandById("rollwright:open-history"));
				await browser.pause(1500);
				await browser.execute(() => document.activeElement?.blur());
				await shot(`logboek-${kant}`);
				const paneel = await browser.$(".rollwright-history");
				if (await paneel.isExisting()) await shot(`logboek-${kant}-paneel`, paneel);
			});
		}
		await zijpaneelDicht();
	});

	it("thema's en skins", async function () {
		for (const [t, licht] of [["Minimal", false], ["AnuPpuccin", true], ["Things", true], ["Border", false]]) {
			await stap(`thema ${t}`, async () => {
				await thema(t, licht);
				await open(NOTE, "preview");
				await browser.pause(1500);
				await markeer();
				await browser.pause(1300);
				await shot(`thema-${t}-${licht ? "licht" : "donker"}`);
			});
		}
		await thema("", true);
		for (const s of ["parchment", "arcane"]) {
			for (const licht of [true, false]) {
				await stap(`skin ${s}`, async () => {
					await thema("", licht);
					await open(NOTE, "preview");
					await skin(s);
					await browser.pause(1500);
					await markeer();
					await browser.pause(1300);
					await shot(`skin-${s}-${licht ? "licht" : "donker"}`);
				});
			}
		}
		await skin("classic");
		await thema("", true);
	});

	it("skins in de instellingen", async function () {
		for (const licht of [true, false]) {
			await stap(`instellingen ${licht}`, async () => {
				await thema("", licht);
				console.log("INSTELLINGEN OPEN:", await openInstellingen());
				await browser.executeObsidian(({ app }) => app.setting.modalEl?.querySelector(".rollwright-skin-preview")?.scrollIntoView({ block: "center" }));
				await browser.pause(500);
				const hoofd = await browser.getWindowHandle();
				const ander = (await browser.getWindowHandles()).find((h) => h !== hoofd);
				console.log("VENSTERS:", ander ? "eigen venster" : "alleen hoofdvenster");
				try {
					if (ander) await browser.switchToWindow(ander);
					await shot(`instellingen-skins-${licht ? "licht" : "donker"}`);
				} finally {
					await browser.switchToWindow(hoofd);
				}
				await sluitInstellingen();
			});
		}
		await thema("", true);
	});
});
