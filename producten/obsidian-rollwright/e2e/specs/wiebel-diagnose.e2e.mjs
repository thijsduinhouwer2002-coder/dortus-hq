import { browser } from "@wdio/globals";

// TIJDELIJK, alleen op een eigen tak, niet samenvoegen. Zoekt uit waarom een klik in
// geschiedenis.e2e.mjs soms niets doet. Doet dezelfde stappen als die spec, twintig rondes,
// en schrijft per klik op wat er in de leesweergave gebeurt. Eist niets.
const LEAF = ".workspace-leaf.mod-active";
const VIEW = `${LEAF} .markdown-reading-view`;

async function opzetten() {
	await browser.executeObsidian(async ({ app }) => {
		const plugin = app.plugins.plugins.rollwright;
		await plugin.clearHistory();
		await plugin.openHistory();
		const file = app.vault.getAbstractFileByPath("Geschiedenis.md");
		const leaf = app.workspace.getLeaf(false);
		await leaf.openFile(file, { state: { mode: "preview" } });
		app.workspace.setActiveLeaf(leaf, { focus: true });
		// Tel aanroepen van freshResult, en wat de leesweergave weghaalt en toevoegt.
		if (!plugin.__diagFresh) {
			const orig = plugin.freshResult.bind(plugin);
			plugin.__diagFresh = 0;
			plugin.freshResult = (...a) => { plugin.__diagFresh++; return orig(...a); };
		}
	});
	await browser.waitUntil(async () => browser.execute((sel) => {
		const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll .rollwright-value`));
		return r.length >= 4 && r.every((v) => v.textContent !== "");
	}, VIEW), { timeout: 20000 });
	await browser.execute((sel) => {
		const root = document.querySelector(sel);
		window.__diag = { weg: 0, erbij: 0, log: [] };
		const telt = (n) => n.nodeType === 1 && (n.matches(".rollwright-roll") || n.querySelector(".rollwright-roll"));
		window.__diagObs?.disconnect();
		window.__diagObs = new MutationObserver((ms) => {
			for (const m of ms) {
				m.removedNodes.forEach((n) => { if (telt(n)) { window.__diag.weg++; window.__diag.log.push(`weg ${performance.now().toFixed(0)} ${n.nodeName}.${n.className}`); } });
				m.addedNodes.forEach((n) => { if (telt(n)) { window.__diag.erbij++; window.__diag.log.push(`erbij ${performance.now().toFixed(0)} ${n.nodeName}.${n.className}`); } });
			}
		});
		window.__diagObs.observe(root, { childList: true, subtree: true });
	}, VIEW);
}

async function klik(ronde, i) {
	const voor = await browser.execute((sel, i) => {
		const alle = document.querySelectorAll(`${sel} .rollwright-roll`);
		const el = alle[i];
		window.__diagEl = el;
		el?.querySelector(".rollwright-value")?.setAttribute("data-e2e-oud", "1");
		window.__diag.log = [];
		return { aantal: alle.length, bestaat: !!el, tekst: el?.textContent ?? null, t: performance.now() };
	}, VIEW, i);
	const fresh0 = await browser.executeObsidian(({ app }) => [app.plugins.plugins.rollwright.__diagFresh, app.plugins.plugins.rollwright.settings.history.length]);
	const opKlik = await browser.execute((sel, i) => {
		const alle = document.querySelectorAll(`${sel} .rollwright-roll`);
		const el = alle[i];
		const zelfde = el === window.__diagEl;
		const verbonden = window.__diagEl?.isConnected ?? null;
		const rect = el?.getBoundingClientRect();
		el?.click();
		return { aantal: alle.length, bestaat: !!el, zelfde, verbonden, zichtbaar: rect ? rect.height > 0 : null, t: performance.now() };
	}, VIEW, i);
	await browser.pause(700);
	const na = await browser.execute((sel, i) => {
		const alle = document.querySelectorAll(`${sel} .rollwright-roll`);
		const el = alle[i];
		return { aantal: alle.length, zelfde: el === window.__diagEl, oudVerbonden: window.__diagEl?.isConnected ?? null, merk: el?.querySelector(".rollwright-value")?.getAttribute("data-e2e-oud") ?? null, tekst: el?.textContent ?? null, weg: window.__diag.weg, erbij: window.__diag.erbij, log: window.__diag.log.slice(0, 12) };
	}, VIEW, i);
	const fresh1 = await browser.executeObsidian(({ app }) => [app.plugins.plugins.rollwright.__diagFresh, app.plugins.plugins.rollwright.settings.history.length]);
	const raar = fresh1[0] === fresh0[0] || fresh1[1] === fresh0[1] || na.merk === "1" || !opKlik.zelfde;
	console.log(`WIEBEL ${raar ? "RAAR" : "ok"} ronde ${ronde} worp ${i}: voor=${JSON.stringify(voor)} opKlik=${JSON.stringify(opKlik)} na=${JSON.stringify(na)} fresh ${fresh0[0]}->${fresh1[0]} geschiedenis ${fresh0[1]}->${fresh1[1]}`);
}

describe("Rollwright: diagnose wiebelende klik (tijdelijk)", function () {
	it("twintig rondes van vier klikken in de leesweergave", async function () {
		for (let ronde = 0; ronde < 20; ronde++) {
			await opzetten();
			for (let i = 0; i < 4; i++) await klik(ronde, i);
		}
	});
});
