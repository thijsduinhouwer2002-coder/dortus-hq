import { browser } from "@wdio/globals";

// Ontwerptest van Daan, 9 nov: de foutmelding van 0.3.3 (rode stippellijn) in licht, donker en twee thema's, en bij hover.
const SHOTS = "screenshots";
const shot = async (naam) => { const f = `${SHOTS}/fout-${naam}.png`; await browser.saveScreenshot(f); console.log("SCHERM:", f); };
const thema = async (naam, licht) => {
	await browser.executeObsidian(({ app }, naam, licht) => { app.customCss.setTheme(naam); app.changeTheme(licht ? "moonstone" : "obsidian"); }, naam, licht);
	await browser.pause(1200);
};
describe("Foutmelding 0.3.3", () => {
	it("maakt plaatjes", async () => {
		await browser.executeObsidian(async ({ app }) => {
			const tekst = "# Fouten\n\nEen goede worp: `dice: 1d20 + 5`\n\nEen kapotte formule: `dice: 1d20 +` en verder gaat de zin gewoon door.\n\nNog een: `dice: banaan` naast een [[link]] ter vergelijking.\n";
			const f = app.vault.getAbstractFileByPath("Fouten.md") || await app.vault.create("Fouten.md", tekst);
			await app.vault.modify(f, tekst);
			const leaf = app.workspace.getLeaf(false);
			await leaf.openFile(f, { state: { mode: "preview" } });
			app.workspace.leftSplit?.collapse();
		});
		await browser.pause(2000);
		const meting = await browser.execute(() => [...document.querySelectorAll(".rollwright-error")].map((e) => { const s = getComputedStyle(e); return `${e.textContent.trim()} | rand=${s.borderBottom} | deco=${s.textDecorationLine} | breed=${Math.round(e.getBoundingClientRect().width)}`; }));
		console.log("FOUTEN:", JSON.stringify(meting));
		for (const [naam, licht] of [["", true], ["", false], ["Minimal", true], ["AnuPpuccin", false]]) {
			await thema(naam, licht);
			await shot(`${naam || "standaard"}-${licht ? "licht" : "donker"}`);
		}
		await thema("", true);
		const el = await browser.$(".rollwright-error");
		if (await el.isExisting()) { await el.moveTo(); await browser.pause(800); await shot("hover-licht"); }
		await browser.execute(() => { document.body.style.zoom = "2"; });
		await browser.pause(600);
		await shot("zoom-licht");
	});
});
