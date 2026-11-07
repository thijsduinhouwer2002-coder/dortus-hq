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
// Zet de klasse die Olaf straks na een klik zet, en markeer de saving throw als 20 en de schade als 1-1 (nagebootst).
const markeer = async () => {
	await browser.execute(() => {
		const rolls = [...document.querySelectorAll(".mod-root .rollwright-roll")].filter((x) => x.offsetParent !== null);
		for (const r of rolls) r.classList.add("rollwright-rolled");
		const save = rolls.find((r) => r.textContent.includes("Wisdom"));
		if (save) { save.classList.add("rollwright-crit"); save.querySelector(".rollwright-value").textContent = "20"; }
		const dmg = rolls.find((r) => r.textContent.includes("Damage"));
		if (dmg) { dmg.classList.add("rollwright-fumble"); dmg.querySelector(".rollwright-value").textContent = "5"; }
	});
};
const klik = async (woord) => {
	await browser.execute((w) => {
		const r = [...document.querySelectorAll(".mod-root .rollwright-roll")].filter((x) => x.offsetParent !== null).find((x) => x.textContent.includes(w));
		r?.click();
	}, woord);
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
	const r = await browser.executeObsidian(async ({ app, obsidian }) => {
		const log = [];
		try { app.commands.executeCommandById("app:open-settings"); log.push("commando"); } catch (e) { log.push("commando fout " + e); }
		await new Promise((res) => setTimeout(res, 800));
		try { if (!document.querySelector(".modal.mod-settings")) { app.setting.open(); log.push("open()"); } } catch (e) { log.push("open fout " + e); }
		await new Promise((res) => setTimeout(res, 500));
		try { app.setting.openTabById("rollwright"); log.push("tab"); } catch (e) { log.push("tab fout " + e); }
		await new Promise((res) => setTimeout(res, 800));
		log.push("modal=" + !!document.querySelector(".modal.mod-settings"));
		if (!document.querySelector(".modal.mod-settings")) {
			// Noodweg: dezelfde instellingen in een eigen venster, zo groot als het echte instellingenvenster.
			try {
				const tab = app.setting.pluginTabs.find((t) => t.id === "rollwright");
				tab.display();
				const m = new obsidian.Modal(app);
				m.modalEl.addClass("mod-settings");
				m.modalEl.style.width = "860px";
				m.modalEl.style.maxHeight = "720px";
				m.setTitle?.("Rollwright");
				tab.containerEl.addClass("vertical-tab-content");
				tab.containerEl.style.overflowY = "auto";
				tab.containerEl.style.maxHeight = "620px";
				m.contentEl.appendChild(tab.containerEl);
				m.open();
				window.__ontwerpModal = m;
				log.push("noodweg modal");
			} catch (e) { log.push("noodweg fout " + e); }
		}
		return log.join(", ");
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
				await klik(woord);
				// Na de klik tekent de widget opnieuw; zet crit of fumble weer zoals Olaf dat straks doet.
				await browser.pause(60);
				await markeer();
				let vorige = 60;
				for (const ms of [250, 900, 1800, 3500, 8000]) {
					await browser.pause(ms - vorige);
					vorige = ms;
					await shot(`rol-${naam}-${ms}ms`);
				}
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
					for (const w of ["Rumour", "Initiative", "Hit", "guests", "Wisdom", "Damage", "stranger says"]) { await klik(w); await browser.pause(500); }
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
				await browser.execute(() => document.querySelector(".rollwright-skin-preview")?.scrollIntoView({ block: "center" }));
				await browser.pause(500);
				await shot(`instellingen-skins-${licht ? "licht" : "donker"}`);
				await sluitInstellingen();
			});
		}
		await thema("", true);
	});
});
