import { browser, expect } from "@wdio/globals";

// OPEN.md punt 19: narratieve dobbelstenen (Genesys, Star Wars) in de echte Obsidian, in lezen en
// Live Preview. Tot nu toe alleen met de nagebootste Obsidian getest (tests/narrative-widget.test.ts).
// Eist: tekst als "2 Success, 1 Threat" in plaats van een getal, een klik rolt opnieuw (nieuw vakje en
// een worp erbij in het logboek), `3g2p` is rood met de reden, en `2d6` blijft een gewone worp.
const LEAF = ".workspace-leaf.mod-active";
const NOTITIE = "Narratief.md";
const LEZEN = ".markdown-reading-view";
const LIVE = ".markdown-source-view";
const ZWS = String.fromCharCode(0x200b);
// Zelfde vorm als SUMMARY in tests/narrative-widget.test.ts.
const SAMENVATTING = /^(No result|((\d+ (Success|Failure|Advantage|Threat|Triumph|Despair|Light|Dark))(, )?)+)$/;
const AANTAL = 5;

async function open(mode) {
	await browser.executeObsidian(async ({ app }, path, mode) => {
		const file = app.vault.getAbstractFileByPath(path);
		if (!file) throw new Error(`notitie ${path} niet gevonden`);
		const leaf = app.workspace.getLeaf(false);
		const state = mode === "preview" ? { mode: "preview" } : { mode: "source", source: false };
		await leaf.openFile(file, { state });
		app.workspace.setActiveLeaf(leaf, { focus: false });
	}, NOTITIE, mode);
	await browser.pause(400);
}

async function lees(view) {
	return browser.execute((sel, zws) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`))
		.filter((r) => !r.parentElement?.closest(".rollwright-roll"))
		.map((r) => {
			const v = r.querySelector(".rollwright-value");
			return {
				tekst: v && !v.hasAttribute("data-e2e-oud") ? (v.textContent ?? "").split(zws).join("").trim() : "",
				fout: r.classList.contains("rollwright-error"),
				reden: r.getAttribute("data-rollwright-error") ?? "",
			};
		}), `${LEAF} ${view}`, ZWS);
}

/** Wacht tot de drie narratieve worpen een samenvatting tonen en de gewone worp een getal. */
async function wacht(view) {
	let w = [];
	await browser.waitUntil(async () => {
		w = await lees(view);
		return w.length === AANTAL && [0, 1, 2].every((i) => SAMENVATTING.test(w[i].tekst)) && w[3].fout && /^\d+$/.test(w[4].tekst);
	}, { timeout: 20000, interval: 300, timeoutMsg: `de worpen in ${view} kwamen niet goed` }).catch((e) => {
		console.log("GEZIEN TOT NU:", JSON.stringify(w));
		throw e;
	});
	return w;
}

async function logLengte() {
	return browser.executeObsidian(({ app }) => app.plugins.plugins.rollwright.settings.history.length);
}

for (const [naam, mode, view] of [["lezen", "preview", LEZEN], ["Live Preview", "live", LIVE]]) {
	describe(`Rollwright: narratieve dobbelstenen in ${naam}`, function () {
		before(async function () {
			// Het logboek houdt de laatste 200 worpen; leeg beginnen, anders kan het niet groeien.
			await browser.executeObsidian(async ({ app }) => app.plugins.plugins.rollwright.clearHistory());
			await open(mode);
		});

		it("toont tekst in plaats van een getal, 3g2p rood, 2d6 gewoon", async function () {
			const w = await wacht(view);
			console.log(`${naam}: ${JSON.stringify(w)}`);
			expect(w[2].tekst).toMatch(/^(No result|((\d+ (Light|Dark))(, )?)+)$/);
			expect(w[3].reden).toContain("P is ambiguous");
			expect(Number(w[4].tekst)).toBeGreaterThanOrEqual(2);
			expect(Number(w[4].tekst)).toBeLessThanOrEqual(12);
		});

		it("een klik op 3g4d rolt opnieuw en komt in het logboek", async function () {
			await wacht(view);
			const voor = await logLengte();
			await browser.execute((sel) => {
				const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).filter((e) => !e.parentElement?.closest(".rollwright-roll"))[0];
				r?.querySelector(".rollwright-value")?.setAttribute("data-e2e-oud", "1");
				r?.click();
			}, `${LEAF} ${view}`);
			const na = await wacht(view);
			const lengte = await logLengte();
			console.log(`${naam} na klik: "${na[0].tekst}", logboek ${voor} -> ${lengte}`);
			expect(na[0].tekst).toMatch(SAMENVATTING);
			expect(lengte).toBeGreaterThan(voor);
		});
	});
}
