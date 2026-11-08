import { browser } from "@wdio/globals";

// Ontwerptest van Daan: waarom zie ik geen beweging in de schermen? Meet prefers-reduced-motion en de animatie na een klik.
describe("Rollwright beweging: meten", function () {
	it("reduced motion en animatie na een klik", async function () {
		await browser.executeObsidian(async ({ app }) => {
			app.commands.executeCommandById("rollwright:create-example-note");
		});
		await browser.pause(2500);
		const uit = await browser.execute(() => {
			const r = [...document.querySelectorAll(".workspace-leaf.mod-active .rollwright-roll")].filter((x) => x.offsetParent !== null)[0];
			const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
			if (!r) return { reduce, token: false };
			r.click();
			const metingen = [];
			const icon = r.querySelector(".rollwright-icon");
			const s = getComputedStyle(r); const si = icon ? getComputedStyle(icon) : null;
			metingen.push({ klassen: r.className, anim: s.animationName, duur: s.animationDuration, iconAnim: si?.animationName, iconDuur: si?.animationDuration, slow: getComputedStyle(document.body).getPropertyValue("--rw-slow") });
			return { reduce, metingen, anims: document.getAnimations().length };
		});
		console.log("BEWEGING:", JSON.stringify(uit));
	});
});
