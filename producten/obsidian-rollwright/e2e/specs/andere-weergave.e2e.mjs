import { browser, expect } from "@wdio/globals";

// Lezen en Live Preview van dezelfde notitie tonen dezelfde plek. Een klik in de ene weergave moet na het
// wisselen ook in de andere te zien zijn (run 42380865200: Live Preview toonde nog de buit van voor de klik).
const LEAF = ".workspace-leaf.mod-active";
const NOTITIE = "Andere weergave.md";
const LEZEN = ".markdown-reading-view";
const LIVE = ".markdown-source-view";
const ZWS = String.fromCharCode(0x200b);

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

async function waarden(view) {
	return browser.execute((sel, zws) => Array.from(document.querySelectorAll(`${sel} .rollwright-roll`))
		.filter((r) => !r.parentElement?.closest(".rollwright-roll"))
		.map((r) => {
			const v = r.querySelector(".rollwright-value");
			return v && !v.hasAttribute("data-e2e-oud") ? (v.textContent ?? "").split(zws).join("").trim() : "";
		}), `${LEAF} ${view}`, ZWS);
}

async function wacht(view) {
	let w = [];
	await browser.waitUntil(async () => {
		w = await waarden(view);
		return w.length === 2 && w.every((x) => x !== "");
	}, { timeout: 15000, timeoutMsg: `geen twee uitkomsten in ${view}` }).catch((e) => {
		console.log("WAARDEN TOT NU:", JSON.stringify(w));
		throw e;
	});
	return w;
}

/** Klikt worp i in een weergave tot hij iets anders toont dan voor de klik; geeft alle waarden terug. */
async function klik(view, i) {
	const voor = (await wacht(view))[i];
	for (let poging = 0; poging < 5; poging++) {
		await browser.execute((sel, i) => {
			const r = Array.from(document.querySelectorAll(`${sel} .rollwright-roll`)).filter((e) => !e.parentElement?.closest(".rollwright-roll"))[i];
			r?.querySelector(".rollwright-value")?.setAttribute("data-e2e-oud", "1");
			r?.click();
		}, `${LEAF} ${view}`, i);
		const na = await wacht(view);
		if (na[i] !== voor) return na;
	}
	throw new Error("de worp bleef gelijk na vijf klikken");
}

describe("Rollwright: een klik is ook in de andere weergave te zien", function () {
	it("eerst gelijk in lezen en Live Preview", async function () {
		await open("preview");
		const lezen = await wacht(LEZEN);
		await open("source");
		const live = await wacht(LIVE);
		console.log("ANDERE WEERGAVE BEGIN:", JSON.stringify({ lezen, live }));
		expect(live).toEqual(lezen);
	});

	it("klik in lezen, dan Live Preview: de nieuwe worp", async function () {
		await open("preview");
		const lezen = await klik(LEZEN, 0);
		await open("source");
		const live = await wacht(LIVE);
		console.log("ANDERE WEERGAVE NA KLIK IN LEZEN:", JSON.stringify({ lezen, live }));
		expect(live).toEqual(lezen);
	});

	it("klik in Live Preview, dan lezen: de nieuwe worp", async function () {
		await open("source");
		const live = await klik(LIVE, 1);
		await open("preview");
		const lezen = await wacht(LEZEN);
		console.log("ANDERE WEERGAVE NA KLIK IN LIVE PREVIEW:", JSON.stringify({ live, lezen }));
		expect(lezen).toEqual(live);
	});
});
