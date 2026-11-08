import { browser } from "@wdio/globals";
import * as fs from "fs";

// Daan, skins v3: eindstand van een crit (NAT 20) en een gewone worp in Parchment en Arcane,
// in standaard donker en licht en in vier populaire thema's. Zoom 1.5, venster 1280 x 820.
const SHOTS = "screenshots";
const THEMAS = [["", false], ["", true], ["Minimal", false], ["AnuPpuccin", true], ["Things", true], ["Border", false]];

const zet = async (thema, licht, skin) => {
	await browser.executeObsidian(({ app }, thema, licht) => { app.customCss.setTheme(thema); app.changeTheme(licht ? "moonstone" : "obsidian"); }, thema, licht);
	await browser.execute((k) => {
		for (const c of Array.from(document.body.classList)) if (c.startsWith("rollwright-skin-")) document.body.classList.remove(c);
		document.body.classList.add(k);
	}, `rollwright-skin-${skin}`);
	await browser.pause(1500);
};

const rol = async (woord, kans) => browser.execute((woord, kans) => {
	const r = [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null).find((x) => x.textContent.includes(woord));
	if (!r) return `geen ${woord}`;
	const oud = Math.random; Math.random = () => kans;
	r.click();
	Math.random = oud;
	return "ok";
}, woord, kans);

describe("Daan: skins v3 in thema's", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.setWindowSize(1280, 820).catch(() => {});
		await browser.executeObsidian(async ({ app }) => {
			app.commands.executeCommandById("rollwright:create-example-note");
			app.workspace.leftSplit?.collapse(); app.workspace.rightSplit?.collapse();
		});
		await browser.pause(2500);
		await browser.execute(() => { try { require("electron").webFrame.setZoomFactor(1.5); } catch (e) {} });
		await browser.pause(800);
		await browser.$(".workspace-ribbon").moveTo().catch(() => {});
	});

	for (const skin of ["parchment", "arcane"]) {
		for (const [thema, licht] of THEMAS) {
			const naam = `${skin}-${thema || "standaard"}-${licht ? "licht" : "donker"}`;
			it(naam, async function () {
				await zet(thema, licht, skin);
				await browser.execute(() => {
					const r = [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].find((x) => x.textContent.includes("Wisdom"));
					r?.scrollIntoView({ block: "center" });
				});
				console.log(`ROL ${naam}:`, await rol("Wisdom", 0.99999), await rol("Damage", 0.5));
				// Eerst landen (LAND_MS 460, daarna start het slot), dan alles afmaken. Run 42515571099 schoot te vroeg.
				await browser.pause(2200);
				await browser.execute(() => document.getAnimations().forEach((a) => { try { a.finish(); } catch (e) {} }));
				await browser.pause(300);
				await browser.saveScreenshot(`${SHOTS}/thema-${naam}.png`);
			});
		}
	}
});
