import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Klus 7 van Daan (ontwerp-v2): in de instellingen toont elke skin-tegel een crit (token "20" met de
// sticker NAT 20) en klein een gewone worp; een betaalde skin zonder sleutel krijgt een slotje.
// Obsidian 1.15 opent de instellingen in een eigen venster, dus alles via app.setting.modalEl (zoals
// zoek-instellingen.e2e.mjs). De spec meet in licht en donker of de sticker binnen de tegel valt en
// het kleine token niet raakt, en schrijft op wat hij ziet.
const SHOTS = "screenshots";

async function openRollwright() {
	await browser.executeObsidian(({ app }) => {
		app.setting.open();
		app.setting.openTabById("rollwright");
	});
	await browser.waitUntil(async () => browser.executeObsidian(({ app }) => (app.setting.modalEl?.querySelectorAll(".rollwright-skin-preview-tile").length ?? 0) > 0),
		{ timeout: 10000, timeoutMsg: "de skin-tegels kwamen niet in beeld" });
}

async function zetThema(donker) {
	await browser.executeObsidian(({ app }, donker) => {
		const docs = new Set([document, app.setting.modalEl?.ownerDocument].filter(Boolean));
		for (const d of docs) {
			d.body.classList.toggle("theme-dark", donker);
			d.body.classList.toggle("theme-light", !donker);
		}
		app.setting.modalEl?.querySelector(".rollwright-skin-preview")?.scrollIntoView({ block: "center" });
	}, donker);
	await browser.pause(300);
}

/** Wat er in elke tegel staat en waar, in pixels van het instellingenvenster. */
async function meet() {
	return browser.executeObsidian(({ app }) => {
		const modal = app.setting.modalEl;
		const box = (el) => {
			const r = el.getBoundingClientRect();
			return { l: Math.round(r.left), t: Math.round(r.top), r: Math.round(r.right), b: Math.round(r.bottom) };
		};
		return Array.from(modal.querySelectorAll(".rollwright-skin-preview-tile")).map((tegel) => {
			const [crit, klein] = Array.from(tegel.querySelectorAll(".rollwright-roll"));
			const sticker = crit?.querySelector(".rollwright-stamp");
			const win = tegel.ownerDocument.defaultView;
			return {
				naam: (tegel.querySelector(".rollwright-skin-preview-name")?.textContent ?? "").trim(),
				slotje: tegel.querySelectorAll(".rollwright-skin-preview-lock svg").length,
				critKlassen: crit?.className ?? "",
				critGetal: crit?.querySelector(".rollwright-value")?.textContent ?? "",
				sticker: sticker?.textContent ?? "",
				stickerPositie: sticker ? win.getComputedStyle(sticker).position : "",
				kleinGetal: klein?.querySelector(".rollwright-value")?.textContent ?? "",
				critAchtergrond: crit ? win.getComputedStyle(crit).backgroundImage.slice(0, 60) + " | " + win.getComputedStyle(crit).backgroundColor : "",
				kleinAchtergrond: klein ? win.getComputedStyle(klein).backgroundImage.slice(0, 60) + " | " + win.getComputedStyle(klein).backgroundColor : "",
				tegel: box(tegel),
				crit: crit ? box(crit) : null,
				stickerBox: sticker ? box(sticker) : null,
				klein: klein ? box(klein) : null,
			};
		});
	});
}

async function foto(naam) {
	const hoofd = await browser.getWindowHandle();
	try {
		for (const h of await browser.getWindowHandles()) {
			if (h === hoofd) continue;
			await browser.switchToWindow(h);
			await browser.saveScreenshot(`${SHOTS}/${naam}.png`);
			return;
		}
		await browser.saveScreenshot(`${SHOTS}/${naam}.png`);
	} catch (e) {
		console.log(`FOTO ${naam} LUKTE NIET:`, String(e).slice(0, 200));
	} finally {
		await browser.switchToWindow(hoofd);
	}
}

describe("Rollwright skin-tegels in de instellingen (Daan klus 7)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await openRollwright();
	});

	after(async function () {
		await browser.executeObsidian(({ app }) => { app.setting.close(); });
	});

	for (const donker of [false, true]) {
		const thema = donker ? "donker" : "licht";
		it(`elke tegel toont een crit met sticker en een gewone worp, ${thema}`, async function () {
			await zetThema(donker);
			const tegels = await meet();
			console.log(`SKIN-TEGELS ${thema}:`, JSON.stringify(tegels));
			await foto(`skin-tegels-${thema}`);
			expect(tegels.map((t) => t.naam)).toEqual(["Classic", "Parchment", "Arcane"]);
			// Zonder sleutel: slotje bij de twee betaalde skins, niet bij Classic.
			expect(tegels.map((t) => t.slotje)).toEqual([0, 1, 1]);
			for (const t of tegels) {
				expect(t.critKlassen).toContain("rollwright-crit");
				expect(t.critGetal).toBe("20");
				expect(t.sticker).toBe("NAT 20");
				expect(t.stickerPositie).toBe("absolute");
				expect(t.kleinGetal).toBe("17");
				expect(t.critAchtergrond).not.toBe(t.kleinAchtergrond);
				// De sticker valt binnen de tegel (niet afgeknipt) en raakt het kleine token niet.
				expect(t.stickerBox.l).toBeGreaterThanOrEqual(t.tegel.l);
				expect(t.stickerBox.r).toBeLessThanOrEqual(t.tegel.r);
				expect(t.stickerBox.t).toBeGreaterThanOrEqual(t.tegel.t);
				expect(t.stickerBox.r <= t.klein.l || t.stickerBox.b <= t.klein.t).toBe(true);
				// Het kleine token is echt kleiner.
				expect(t.klein.b - t.klein.t).toBeLessThan(t.crit.b - t.crit.t);
			}
		});
	}
});
