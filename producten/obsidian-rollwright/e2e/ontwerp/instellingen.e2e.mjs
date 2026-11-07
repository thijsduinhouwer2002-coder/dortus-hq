import { browser } from "@wdio/globals";
import * as fs from "fs";

// Ontwerptest van Daan: alleen het instellingenvenster van Rollwright in beeld krijgen.
// Probeert vier manieren en schrijft per manier op wat er gebeurt, ook wie een venster weer weghaalt.
const SHOTS = "screenshots";
const shot = async (naam) => {
	const file = `${SHOTS}/i-${naam}.png`;
	await browser.saveScreenshot(file);
	console.log("SCHERM:", file);
};

const toestand = (label) => browser.execute((label) => {
	const m = Array.from(document.querySelectorAll(".modal-container")).map((c) => c.className + " > " + (c.querySelector(".modal")?.className ?? "?"));
	return `${label}: containers=${JSON.stringify(m)} focus=${document.hasFocus()} zicht=${document.visibilityState} actief=${document.activeElement?.className ?? "-"} venster=${window.innerWidth}x${window.innerHeight} weg=${JSON.stringify((window.__weg ?? []).slice(-3))}`;
}, label);

const sluit = async () => {
	try { await browser.switchToWindow(hoofd); } catch (e) {}
	await browser.execute(() => { try { window.app.setting.close(); } catch (e) {} document.querySelectorAll(".modal-container").forEach((c) => c.remove()); });
	await browser.pause(400);
	try {
		for (const h of await browser.getWindowHandles()) {
			if (h === hoofd) continue;
			await browser.switchToWindow(h);
			await browser.closeWindow();
		}
	} catch (e) { console.log("INSTELLINGEN sluiten", String(e).slice(0, 200)); }
	await browser.switchToWindow(hoofd);
	await browser.pause(400);
};

const naarTab = async () => {
	// Klik echt op "Rollwright" in de zijbalk van de instellingen.
	const items = await browser.$$(".vertical-tab-nav-item");
	for (const it of items) {
		if ((await it.getText()).trim() === "Rollwright") { await it.click(); return "tab geklikt"; }
	}
	return `tab niet gevonden (${items.length} items)`;
};

let hoofd;
const vensters = async (label) => {
	const handles = await browser.getWindowHandles();
	const uit = [];
	for (const h of handles) {
		await browser.switchToWindow(h);
		const info = await browser.execute(() => `${document.title} | settings=${!!document.querySelector(".vertical-tab-content")} | ${window.innerWidth}x${window.innerHeight}`);
		uit.push(`${h === hoofd ? "HOOFD" : "ANDER"} ${info}`);
	}
	await browser.switchToWindow(hoofd);
	console.log("INSTELLINGEN vensters", label, JSON.stringify(uit));
	return handles;
};

// Zoek het venster met de instellingen (in nieuwe Obsidian een eigen venster) en blijf daar.
const naarInstellingen = async () => {
	for (const h of await browser.getWindowHandles()) {
		await browser.switchToWindow(h);
		if (await browser.execute(() => !!document.querySelector(".vertical-tab-content, .modal.mod-settings"))) return h;
	}
	await browser.switchToWindow(hoofd);
	return null;
};

const vastleggen = async (naam) => {
	await browser.pause(1200);
	console.log("INSTELLINGEN", await toestand(naam));
	await vensters(naam);
	const h = await naarInstellingen();
	if (!h) return false;
	console.log("INSTELLINGEN", naam, "venster", h === hoofd ? "hoofd" : "eigen", await naarTab());
	await browser.pause(800);
	await shot(`${naam}-boven`);
	const tekst = await browser.execute(() => document.querySelector(".vertical-tab-content")?.innerText ?? "");
	console.log("INSTELLINGEN TEKST", naam, JSON.stringify(tekst));
	const hoog = await browser.execute(() => { const el = document.querySelector(".vertical-tab-content"); return el ? `${el.scrollHeight}/${el.clientHeight}` : "-"; });
	console.log("INSTELLINGEN hoogte", naam, hoog);
	await browser.execute(() => { const el = document.querySelector(".vertical-tab-content"); if (el) el.scrollTop = el.scrollHeight / 2; });
	await browser.pause(400);
	await shot(`${naam}-midden`);
	await browser.execute(() => { const el = document.querySelector(".vertical-tab-content"); if (el) el.scrollTop = el.scrollHeight; });
	await browser.pause(400);
	await shot(`${naam}-onder`);
	// Toetsenbord: Tab door de instellingen, kijk waar de focus staat.
	await browser.execute(() => { const el = document.querySelector(".vertical-tab-content"); if (el) el.scrollTop = 0; });
	for (let i = 0; i < 4; i++) await browser.keys(["Tab"]);
	await browser.pause(300);
	await shot(`${naam}-tab-focus`);
	await browser.switchToWindow(hoofd);
	return true;
};

describe("Instellingen van Rollwright in beeld", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		hoofd = await browser.getWindowHandle();
		// Leg vast wie een venster weghaalt, met de aanroepstapel.
		await browser.execute(() => {
			window.__weg = [];
			new MutationObserver((lijst) => {
				for (const m of lijst) for (const n of m.removedNodes) {
					if (n.classList?.contains("modal-container")) window.__weg.push("weg: " + (n.querySelector(".modal")?.className ?? "?"));
				}
				for (const m of lijst) for (const n of m.addedNodes) {
					if (n.classList?.contains("modal-container")) window.__weg.push("erbij: " + (n.querySelector(".modal")?.className ?? "?"));
				}
			}).observe(document.body, { childList: true });
			const oud = Element.prototype.remove;
			Element.prototype.remove = function () {
				if (this.classList?.contains("modal-container")) window.__weg.push("remove() door " + new Error().stack.split("\n").slice(2, 6).join(" | "));
				return oud.call(this);
			};
		});
		await browser.executeObsidian(({ app }) => app.changeTheme("moonstone"));
		await browser.pause(1500);
		await shot("begin");
		console.log("INSTELLINGEN", await toestand("begin"));
	});

	it("manier 1: echt klikken op het tandwiel", async function () {
		try {
			const knoppen = await browser.$$(".workspace-drawer-vault-actions .clickable-icon, .side-dock-settings .side-dock-ribbon-action, [aria-label='Settings'], [aria-label='Open settings']");
			console.log("INSTELLINGEN tandwielen:", knoppen.length);
			if (knoppen.length) await knoppen[knoppen.length - 1].click();
			const ok = await vastleggen("klik");
			if (!ok) await shot("klik-niets");
		} catch (e) { console.log("INSTELLINGEN klik fout", String(e).slice(0, 300)); }
		await sluit();
	});

	it("manier 2: sneltoets Ctrl+,", async function () {
		try {
			await browser.keys(["Control", ","]);
			const ok = await vastleggen("toets");
			if (!ok) await shot("toets-niets");
		} catch (e) { console.log("INSTELLINGEN toets fout", String(e).slice(0, 300)); }
		await sluit();
	});

	it("manier 3: app.setting.open() via browser.execute", async function () {
		try {
			await browser.execute(() => { window.app.setting.open(); });
			const ok = await vastleggen("execute");
			if (!ok) await shot("execute-niets");
		} catch (e) { console.log("INSTELLINGEN execute fout", String(e).slice(0, 300)); }
		await sluit();
	});

	it("manier 4: openTabById en dan donker", async function () {
		try {
			await browser.execute(() => { window.app.setting.open(); window.app.setting.openTabById("rollwright"); });
			const ok = await vastleggen("tabid-licht");
			if (ok) {
				await browser.executeObsidian(({ app }) => app.changeTheme("obsidian"));
				await browser.pause(1200);
				if (await naarInstellingen()) {
					await naarTab();
					await browser.pause(600);
					await shot("tabid-donker-boven");
					await browser.execute(() => { const el = document.querySelector(".vertical-tab-content"); if (el) el.scrollTop = el.scrollHeight; });
					await browser.pause(400);
					await shot("tabid-donker-onder");
					await browser.switchToWindow(hoofd);
				}
				await browser.executeObsidian(({ app }) => app.changeTheme("moonstone"));
			} else await shot("tabid-niets");
		} catch (e) { console.log("INSTELLINGEN tabid fout", String(e).slice(0, 300)); }
		await sluit();
	});
});
