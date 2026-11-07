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
	await browser.executeObsidian(({ app }) => app.setting.close());
	await browser.pause(500);
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
			const roll = await browser.$(".workspace-leaf.mod-active .rollwright-roll");
			await roll.moveTo();
			await browser.pause(1200);
			await shot("tooltip-zweven");
			await roll.click();
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
				await fout.scrollIntoView();
				await fout.moveTo();
				await browser.pause(1200);
				console.log("FOUTTEKST:", await fout.getAttribute("aria-label"), "|", await fout.getProperty("textContent"));
			} else console.log("FOUT: geen .rollwright-error gevonden");
			await shot("foutmelding-zweven");
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

	it("de instellingen met de koopknop", async function () {
		for (const licht of [true, false]) {
			await stap(`instellingen ${licht}`, async () => {
				await thema("", licht);
				await browser.executeObsidian(({ app }) => {
					app.setting.open();
					app.setting.openTabById("rollwright");
				});
				await browser.pause(1200);
				await shot(`instellingen-boven-${licht ? "licht" : "donker"}`);
				await browser.execute(() => {
					const el = document.querySelector(".modal.mod-settings .vertical-tab-content");
					if (el) el.scrollTop = el.scrollHeight;
				});
				await browser.pause(500);
				await shot(`instellingen-onder-${licht ? "licht" : "donker"}`);
				const tekst = await browser.execute(() => document.querySelector(".modal.mod-settings .vertical-tab-content")?.innerText ?? "");
				if (licht) console.log("INSTELLINGEN TEKST:", tekst);
				await sluitInstellingen();
			});
		}
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
			const rolls = await browser.$$(".workspace-leaf.mod-active .rollwright-roll");
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
			await browser.setWindowSize(480, 820);
			await browser.pause(1000);
			await open("Taverne.md", "preview");
			await shot("smal-lezen");
			await browser.executeObsidian(({ app }) => {
				app.setting.open();
				app.setting.openTabById("rollwright");
			});
			await browser.pause(1000);
			await shot("smal-instellingen");
			await sluitInstellingen();
			await browser.setWindowSize(1280, 820);
		});
	});
});
