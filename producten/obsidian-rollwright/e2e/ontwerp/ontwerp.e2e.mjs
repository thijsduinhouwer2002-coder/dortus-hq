import { browser } from "@wdio/globals";
import * as fs from "fs";

// Ontwerptest van Daan. Maakt alleen schermafbeeldingen en schrijft op wat hij ziet.
// Faalt een stap, dan gaat de rest door: elke stap vangt zijn eigen fout.
const SHOTS = "screenshots";
let n = 0;
const shot = async (naam) => {
	n += 1;
	const file = `${SHOTS}/${String(n).padStart(2, "0")}-${naam}.png`;
	await browser.saveScreenshot(file);
	console.log("SCHERM:", file);
};
const stap = async (naam, fn) => {
	try {
		await fn();
	} catch (e) {
		console.log("STAP MISLUKT:", naam, String(e).slice(0, 300));
	}
};

const open = async (pad, mode) => {
	await browser.executeObsidian(async ({ app }, pad, mode) => {
		const file = app.vault.getAbstractFileByPath(pad);
		const leaf = app.workspace.getLeaf(false);
		await leaf.openFile(file, { state: { mode, source: false } });
		app.workspace.setActiveLeaf(leaf, { focus: true });
	}, pad, mode);
	await browser.pause(1500);
};

const thema = async (naam, licht) => {
	await browser.executeObsidian(({ app }, naam, licht) => {
		app.customCss.setTheme(naam);
		app.changeTheme(licht ? "moonstone" : "obsidian");
	}, naam, licht);
	await browser.pause(1500);
};

const skin = async (klasse) => {
	await browser.execute((klasse) => {
		document.body.classList.remove("rollwright-skin-classic", "rollwright-skin-parchment", "rollwright-skin-arcane");
		document.body.classList.add(klasse);
	}, klasse);
	await browser.pause(300);
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

describe("Ontwerp van Rollwright", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.setWindowSize(1280, 820).catch(() => {});
	});

	it("licht en donker, leesweergave en Live Preview", async function () {
		for (const licht of [true, false]) {
			const kant = licht ? "licht" : "donker";
			await stap(`standaard ${kant}`, async () => {
				await thema("", licht);
				await open("Taverne.md", "preview");
				await shot(`standaard-${kant}-lezen`);
				await open("Taverne.md", "source");
				await shot(`standaard-${kant}-live-preview`);
			});
		}
	});

	it("tooltip bij zweven en na een klik", async function () {
		await stap("tooltip", async () => {
			await thema("", true);
			await open("Taverne.md", "preview");
			await zweef(".workspace-leaf.mod-active .rollwright-roll");
			await shot("tooltip-zweven");
			const roll = await browser.$(".workspace-leaf.mod-active .rollwright-roll");
			await browser.execute((el) => el.click(), roll);
			await browser.pause(150);
			await shot("klik-direct");
			await browser.pause(600);
			await shot("klik-daarna");
		});
	});

	it("de foutmelding van een kapotte formule", async function () {
		await stap("fout", async () => {
			const fout = await browser.$(".workspace-leaf.mod-active .rollwright-error");
			if (await fout.isExisting()) {
				await zweef(".workspace-leaf.mod-active .rollwright-error");
				console.log("FOUTTEKST:", await fout.getAttribute("aria-label"), "|", await fout.getProperty("textContent"));
			} else console.log("FOUT: geen .rollwright-error gevonden");
			await shot("foutmelding-zweven");
		});
	});

	it("worpen op secties en dice-mod", async function () {
		await stap("secties", async () => {
			await open("Secties.md", "preview");
			await shot("secties-lezen");
			await open("Secties.md", "source");
			await shot("secties-live-preview");
		});
		await stap("dice-mod", async () => {
			await open("Secties.md", "preview");
			await browser.execute(() => {
				const all = Array.from(document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll"));
				all[all.length - 1]?.click();
			});
			await browser.pause(800);
			await shot("dice-mod-venster");
			await browser.keys(["Escape"]);
		});
	});

	it("populaire thema's", async function () {
		for (const naam of ["Minimal", "AnuPpuccin", "Things", "Border"]) {
			for (const licht of [true, false]) {
				await stap(`${naam} ${licht}`, async () => {
					await thema(naam, licht);
					await open("Taverne.md", "preview");
					await shot(`thema-${naam.replace(/\s/g, "")}-${licht ? "licht" : "donker"}`);
				});
			}
		}
		await thema("", true);
	});

	it("betaalde skins, licht en donker", async function () {
		for (const s of ["parchment", "arcane"]) {
			for (const licht of [true, false]) {
				await stap(`skin ${s}`, async () => {
					await thema("", licht);
					await open("Taverne.md", "preview");
					await skin(`rollwright-skin-${s}`);
					await shot(`skin-${s}-${licht ? "licht" : "donker"}`);
				});
			}
		}
		await skin("rollwright-skin-classic");
		await thema("", true);
	});

	it("leeg begin: lege notitie, geschiedenis, formule-venster", async function () {
		await stap("leeg", async () => {
			await open("Leeg.md", "source");
			await shot("leeg-notitie");
		});
		await stap("geschiedenis leeg", async () => {
			await browser.executeObsidian(({ app }) => app.commands.executeCommandById("rollwright:open-history"));
			await browser.pause(1200);
			await shot("geschiedenis-leeg");
		});
		await stap("formule-venster", async () => {
			await browser.executeObsidian(({ app }) => app.commands.executeCommandById("rollwright:roll-formula"));
			await browser.pause(800);
			await shot("formule-venster-leeg");
			await browser.keys(["2", "d", "6", "Enter"]);
			await browser.pause(800);
			await shot("formule-venster-na-enter");
			await browser.keys(["Escape"]);
		});
		await stap("geschiedenis gevuld", async () => {
			await open("Taverne.md", "preview");
			// Alleen de worpen in de leesweergave (tip Olaf): anders klikt de test ook de verborgen bronweergave.
			const rolls = await browser.$$(".workspace-leaf.mod-active .markdown-reading-view .rollwright-roll");
			for (const r of rolls.slice(0, 4)) await browser.execute((el) => el.click(), r);
			await browser.pause(800);
			await shot("geschiedenis-gevuld");
		});
	});

	it("toetsenbord alleen", async function () {
		await stap("tab", async () => {
			await open("Taverne.md", "preview");
			await browser.execute(() => document.activeElement?.blur());
			for (let i = 0; i < 6; i++) await browser.keys(["Tab"]);
			await browser.pause(400);
			const info = await browser.execute(() => {
				const a = document.activeElement;
				return a ? `${a.tagName}.${a.className} tabindex=${a.getAttribute("tabindex")} role=${a.getAttribute("role")} label=${a.getAttribute("aria-label")}` : "niets";
			});
			console.log("FOCUS NA 6 TABS:", info);
			const rolls = await browser.execute(() => Array.from(document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")).map((r) => `${r.tagName} tabindex=${r.getAttribute("tabindex")} role=${r.getAttribute("role")}`));
			console.log("WORPEN TOEGANKELIJK:", JSON.stringify(rolls));
			await shot("toetsenbord-focus");
		});
	});

	it("smal venster", async function () {
		await stap("smal", async () => {
			console.log("SMAL:", await smal(480));
			await browser.pause(1000);
			await open("Taverne.md", "preview");
			await shot("smal-lezen");
			await sluitInstellingen();
			await smal(1024);
		});
	});
});
