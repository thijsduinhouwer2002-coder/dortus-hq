import { browser } from "@wdio/globals";
import * as fs from "fs";

// Daan, skins v3: de beweging bij het rollen scherp in beeld. Na de klik alle CSS-animaties pauzeren
// en op vaste tijden zetten (currentTime), per stand een scherm. Crit (NAT 20) op het Wisdom-token, donker, zoom 2.
const SHOTS = "screenshots";
const TIJDEN = [0, 60, 120, 200, 300, 450, 650, 900, 1300];

async function skin(naam) {
	await browser.execute((naam) => {
		for (const c of Array.from(document.body.classList)) if (c.startsWith("rollwright-skin-")) document.body.classList.remove(c);
		document.body.classList.add(`rollwright-skin-${naam}`);
		document.body.classList.add("theme-dark"); document.body.classList.remove("theme-light");
	}, naam);
	await browser.pause(600);
}

describe("Daan: beweging per skin in vaste standen", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.setWindowSize(1280, 820).catch(() => {});
		await browser.executeObsidian(async ({ app }) => {
			app.commands.executeCommandById("rollwright:create-example-note");
			app.workspace.leftSplit?.collapse(); app.workspace.rightSplit?.collapse();
		});
		await browser.pause(2500);
		await browser.execute(() => { try { require("electron").webFrame.setZoomFactor(2); } catch (e) {} });
		await browser.pause(800);
		await browser.$(".workspace-ribbon").moveTo().catch(() => {});
	});

	for (const naam of ["classic", "parchment", "arcane"]) {
		it(naam, async function () {
			await skin(naam);
			const uit = await browser.executeAsync((done) => {
				const zoek = () => [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null).find((x) => x.textContent.includes("Wisdom"));
				const r = zoek();
				if (!r) return done({ fout: "geen Wisdom-token" });
				r.scrollIntoView({ block: "center" });
				if (!window.__rwRandom) window.__rwRandom = Math.random;
				Math.random = () => 0.99999;
				r.click();
				const t0 = performance.now();
				const kijk = () => {
					const anims = document.getAnimations().filter((a) => (a.animationName ?? "").startsWith("rw-"));
					const t = zoek();
					if (anims.length && t && t.classList.contains("rollwright-crit")) {
						anims.forEach((a) => { a.pause(); a.currentTime = 0; });
						Math.random = window.__rwRandom; window.__rwRandom = undefined;
						const b = t.getBoundingClientRect();
						return done({ na: Math.round(performance.now() - t0), namen: anims.map((a) => `${a.animationName}:${a.effect?.getTiming?.().delay}+${a.effect?.getTiming?.().duration}`), rect: { x: b.x, y: b.y, w: b.width, h: b.height, dpr: devicePixelRatio } });
					}
					if (performance.now() - t0 > 3000) { Math.random = window.__rwRandom; return done({ fout: "geen animatie binnen 3 s", klassen: t?.className }); }
					requestAnimationFrame(kijk);
				};
				kijk();
			});
			console.log(`STAND ${naam}:`, JSON.stringify(uit));
			for (const ms of TIJDEN) {
				await browser.execute((ms) => document.getAnimations().filter((a) => (a.animationName ?? "").startsWith("rw-")).forEach((a) => { a.currentTime = ms; }), ms);
				await browser.pause(150);
				await browser.saveScreenshot(`${SHOTS}/stand-${naam}-${String(ms).padStart(4, "0")}.png`);
			}
			await browser.execute(() => document.getAnimations().forEach((a) => { try { a.finish(); } catch (e) {} }));
			await browser.pause(300);
		});
	}
});
