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
	await browser.execute(() => { try { window.app.setting.close(); } catch (e) {} document.querySelectorAll(".modal-container").forEach((c) => c.remove()); });
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

const vastleggen = async (naam) => {
	await browser.pause(900);
	console.log("INSTELLINGEN", await toestand(naam));
	const open = await browser.execute(() => !!document.querySelector(".modal.mod-settings"));
	if (!open) return false;
	console.log("INSTELLINGEN", naam, await naarTab());
	await browser.pause(700);
	await shot(`${naam}-boven`);
	const tekst = await browser.execute(() => document.querySelector(".modal.mod-settings .vertical-tab-content")?.innerText ?? "");
	console.log("INSTELLINGEN TEKST", naam, JSON.stringify(tekst));
	await browser.execute(() => { const el = document.querySelector(".modal.mod-settings .vertical-tab-content"); if (el) el.scrollTop = el.scrollHeight; });
	await browser.pause(400);
	await shot(`${naam}-onder`);
	return true;
};

describe("Instellingen van Rollwright in beeld", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
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
				await shot("tabid-donker-boven");
				await browser.execute(() => { const el = document.querySelector(".modal.mod-settings .vertical-tab-content"); if (el) el.scrollTop = el.scrollHeight; });
				await browser.pause(400);
				await shot("tabid-donker-onder");
				await browser.executeObsidian(({ app }) => app.changeTheme("moonstone"));
			} else await shot("tabid-niets");
		} catch (e) { console.log("INSTELLINGEN tabid fout", String(e).slice(0, 300)); }
		await sluit();
	});
});
