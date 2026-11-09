import { browser, expect } from "@wdio/globals";
import * as fs from "fs";

// Bouwplan notitiesfeer, stap 1 (mechaniek, nog zonder skin-CSS): eisen 1 tot 7.
// Met een betaalde skin krijgt het notitievlak van een notitie met worpen de klasse rollwright-world,
// nooit zonder betaalde skin, nooit in de zijbalk, en weg als de plugin uit gaat.
const SHOTS = "screenshots";
const MET = "Wereld met worp.md";
const ZONDER = "Wereld zonder worp.md";
const TEKST_MET = "# Wereld\n\nAanval `dice: 1d20+5`\n";
const TEKST_ZONDER = "# Gewoon\n\nGeen worp hier, alleen `code`.\n";

/** Per open notitie: pad, wel of geen klasse, en of hij in de zijbalk staat. */
async function stand() {
	return browser.executeObsidian(({ app }) => {
		const uit = [];
		app.workspace.iterateAllLeaves((leaf) => {
			const view = leaf.view;
			if (view.getViewType() !== "markdown" || !view.file) return;
			const root = leaf.getRoot();
			const plek = root === app.workspace.leftSplit ? "links" : root === app.workspace.rightSplit ? "rechts" : root === app.workspace.rootSplit ? "midden" : "venster";
			const inhoud = view.containerEl.querySelector(".view-content");
			uit.push({
				pad: view.file.path,
				plek,
				wereld: view.containerEl.classList.contains("rollwright-world"),
				root: root?.constructor?.name ?? null,
				container: leaf.getContainer() === app.workspace.rootSplit ? "rootSplit" : leaf.getContainer()?.constructor?.name ?? null,
				bg: inhoud ? inhoud.ownerDocument.defaultView.getComputedStyle(inhoud).backgroundColor : null,
			});
		});
		return uit;
	});
}

async function zetPlugin(veranderingen) {
	await browser.executeObsidian(({ app }, veranderingen) => {
		const plugin = app.plugins.plugins.rollwright;
		Object.assign(plugin.settings, veranderingen);
		plugin.applySkin();
	}, veranderingen);
}

/** Wacht tot de klasse op elke genoemde notitie (in het midden) zo staat als gevraagd. */
async function wachtOp(verwacht, uitleg, timeout = 4000) {
	let laatste = [];
	await browser.waitUntil(async () => {
		laatste = await stand();
		return Object.entries(verwacht).every(([pad, wereld]) => laatste.some((s) => s.pad === pad && s.plek === "midden" && s.wereld === wereld));
	}, { timeout, timeoutMsg: `${uitleg}: ${JSON.stringify(laatste)}` });
	console.log(`NOTITIESFEER ${uitleg}:`, JSON.stringify(laatste));
	return laatste;
}

describe("Rollwright: de skin kleurt de hele notitie, mechaniek (bouwplan notitiesfeer)", function () {
	before(async function () {
		fs.mkdirSync(SHOTS, { recursive: true });
		await browser.executeObsidian(async ({ app }, MET, ZONDER, TEKST_MET, TEKST_ZONDER) => {
			for (const [pad, tekst] of [[MET, TEKST_MET], [ZONDER, TEKST_ZONDER]]) {
				const bestaand = app.vault.getAbstractFileByPath(pad);
				if (bestaand) await app.vault.modify(bestaand, tekst);
				else await app.vault.create(pad, tekst);
			}
			const links = app.workspace.getLeaf("tab");
			await links.openFile(app.vault.getAbstractFileByPath(MET), { state: { mode: "preview" } });
			const rechts = app.workspace.getLeaf("split", "vertical");
			await rechts.openFile(app.vault.getAbstractFileByPath(ZONDER), { state: { mode: "source", source: false } });
		}, MET, ZONDER, TEKST_MET, TEKST_ZONDER);
		await browser.pause(1000);
	});

	after(async function () {
		await zetPlugin({ skin: "classic", licenseKey: "", licenseCheckedAt: 0, noteWorld: "rolls" });
	});

	it("eis 1: Classic en zonder sleutel nergens de klasse", async function () {
		await zetPlugin({ skin: "classic", licenseKey: "", licenseCheckedAt: 0 });
		await browser.pause(800);
		const zonderSleutel = await stand();
		console.log("NOTITIESFEER eis 1 zonder sleutel:", JSON.stringify(zonderSleutel));
		expect(zonderSleutel.some((s) => s.wereld)).toBe(false);
		// Parchment gekozen maar zonder geldige sleutel: valt terug op Classic.
		await zetPlugin({ skin: "parchment" });
		await browser.pause(800);
		expect((await stand()).some((s) => s.wereld)).toBe(false);
		await zetPlugin({ skin: "classic", licenseKey: "E2E-SLEUTEL", licenseCheckedAt: Date.now() });
		await browser.pause(800);
		const classic = await stand();
		console.log("NOTITIESFEER eis 1 Classic met sleutel:", JSON.stringify(classic));
		expect(classic.some((s) => s.wereld)).toBe(false);
	});

	it("eis 2: betaalde skin, Notes with rolls: alleen de notitie met een worp", async function () {
		await zetPlugin({ skin: "parchment", licenseKey: "E2E-SLEUTEL", licenseCheckedAt: Date.now(), noteWorld: "rolls" });
		await wachtOp({ [MET]: true, [ZONDER]: false }, "eis 2");
		await browser.saveScreenshot(`${SHOTS}/notitiesfeer-eis2.png`);
	});

	it("eis 3: worp weghalen en terugzetten, klasse volgt binnen 4 seconden", async function () {
		await browser.executeObsidian(async ({ app }, ZONDER) => {
			await app.vault.modify(app.vault.getAbstractFileByPath(ZONDER), "# Nu wel\n\n`dice: 2d6`\n");
		}, ZONDER);
		await wachtOp({ [ZONDER]: true }, "eis 3 worp erbij");
		await browser.executeObsidian(async ({ app }, ZONDER, TEKST_ZONDER) => {
			await app.vault.modify(app.vault.getAbstractFileByPath(ZONDER), TEKST_ZONDER);
		}, ZONDER, TEKST_ZONDER);
		await wachtOp({ [ZONDER]: false }, "eis 3 worp weg");
	});

	it("eis 3: een andere notitie in hetzelfde tabblad neemt de klasse niet mee", async function () {
		// Onderzoek (9 nov, rode run 42618407938): welke events komen er bij openFile in een niet-actief blad, en wat toont het blad dan?
		const events = await browser.executeObsidian(async ({ app }, MET, ZONDER) => {
			let blad = null;
			app.workspace.iterateAllLeaves((leaf) => {
				if (leaf.view.file?.path === MET) blad = leaf;
			});
			const t0 = performance.now();
			const log = [];
			const noteer = (naam) => () => log.push({ naam, ms: Math.round(performance.now() - t0), bestand: blad.view.file?.path ?? null, actief: app.workspace.getMostRecentLeaf?.() === blad, klasse: blad.view.containerEl.classList.contains("rollwright-world") });
			const refs = ["layout-change", "active-leaf-change", "file-open"].map((naam) => app.workspace.on(naam, noteer(naam)));
			await blad.openFile(app.vault.getAbstractFileByPath(ZONDER));
			noteer("openFile klaar")();
			await new Promise((r) => setTimeout(r, 1500));
			noteer("na 1,5 s")();
			for (const ref of refs) app.workspace.offref(ref);
			return log;
		}, MET, ZONDER);
		console.log("NOTITIESFEER eis 3 events:", JSON.stringify(events));
		await browser.waitUntil(async () => (await stand()).every((s) => s.pad !== MET), { timeout: 4000 });
		const na = await wachtOp({ [ZONDER]: false }, "eis 3 ander bestand");
		expect(na.some((s) => s.wereld)).toBe(false);
		await browser.executeObsidian(async ({ app }, MET, ZONDER) => {
			let blad = null;
			app.workspace.iterateAllLeaves((leaf) => {
				if (leaf.view.file?.path === ZONDER && !blad) blad = leaf;
			});
			await blad.openFile(app.vault.getAbstractFileByPath(MET), { state: { mode: "preview" } });
		}, MET, ZONDER);
		await wachtOp({ [MET]: true }, "eis 3 terug");
	});

	it("eis 4: Off nergens, All notes ook de notitie zonder worp", async function () {
		await zetPlugin({ noteWorld: "off" });
		await wachtOp({ [MET]: false, [ZONDER]: false }, "eis 4 Off");
		await zetPlugin({ noteWorld: "all" });
		await wachtOp({ [MET]: true, [ZONDER]: true }, "eis 4 All notes");
		await zetPlugin({ noteWorld: "rolls" });
		await wachtOp({ [MET]: true, [ZONDER]: false }, "eis 4 terug");
	});

	it("eis 5: cssclasses rollwright-plain wint, rollwright-world zet hem aan bij Off", async function () {
		await browser.executeObsidian(async ({ app }, MET, TEKST_MET) => {
			await app.vault.modify(app.vault.getAbstractFileByPath(MET), `---\ncssclasses:\n  - rollwright-plain\n---\n${TEKST_MET}`);
		}, MET, TEKST_MET);
		await wachtOp({ [MET]: false }, "eis 5 plain");
		await browser.executeObsidian(async ({ app }, MET, ZONDER, TEKST_MET, TEKST_ZONDER) => {
			await app.vault.modify(app.vault.getAbstractFileByPath(MET), TEKST_MET);
			await app.vault.modify(app.vault.getAbstractFileByPath(ZONDER), `---\ncssclasses: rollwright-world\n---\n${TEKST_ZONDER}`);
		}, MET, ZONDER, TEKST_MET, TEKST_ZONDER);
		await zetPlugin({ noteWorld: "off" });
		await wachtOp({ [MET]: false, [ZONDER]: true }, "eis 5 world bij Off");
		await browser.executeObsidian(async ({ app }, ZONDER, TEKST_ZONDER) => {
			await app.vault.modify(app.vault.getAbstractFileByPath(ZONDER), TEKST_ZONDER);
		}, ZONDER, TEKST_ZONDER);
		await zetPlugin({ noteWorld: "rolls" });
		await wachtOp({ [MET]: true, [ZONDER]: false }, "eis 5 terug");
	});

	it("eis 6c: een uitgesteld blad krijgt de klasse zodra het opent", async function () {
		// Een achtergrondtab met de worp, dan de lay-out opnieuw laden: Obsidian stelt niet zichtbare tabs uit.
		const voor = await browser.executeObsidian(async ({ app }, MET) => {
			const achter = app.workspace.getLeaf("tab");
			await achter.openFile(app.vault.getAbstractFileByPath(MET), { active: false });
			const actief = app.workspace.getLeaf("tab");
			await actief.openFile(app.vault.getAbstractFileByPath("Rollen.md"), { active: true });
			await app.workspace.changeLayout(app.workspace.getLayout());
			const uitgesteld = [];
			app.workspace.iterateAllLeaves((leaf) => {
				if (leaf.isDeferred) uitgesteld.push({ type: leaf.view.getViewType(), wereld: leaf.view.containerEl.classList.contains("rollwright-world"), state: leaf.getViewState().state?.file });
			});
			return uitgesteld;
		}, MET);
		console.log("NOTITIESFEER eis 6c uitgesteld:", JSON.stringify(voor));
		const blad = voor.find((b) => b.state === MET);
		expect(blad).toBeDefined();
		expect(blad.wereld).toBe(false);
		await browser.executeObsidian(async ({ app }, MET) => {
			let doel = null;
			app.workspace.iterateAllLeaves((leaf) => {
				if (leaf.isDeferred && leaf.getViewState().state?.file === MET) doel = leaf;
			});
			app.workspace.setActiveLeaf(doel, { focus: true });
			await doel.loadIfDeferred();
		}, MET);
		await wachtOp({ [MET]: true }, "eis 6c na openen");
	});

	it("eis 6: een notitie met worpen in de zijbalk krijgt de klasse niet", async function () {
		await browser.executeObsidian(async ({ app }, MET) => {
			const zij = app.workspace.getRightLeaf(true);
			await zij.openFile(app.vault.getAbstractFileByPath(MET), { active: false });
		}, MET);
		await browser.pause(1500);
		const s = await stand();
		console.log("NOTITIESFEER eis 6:", JSON.stringify(s));
		const zij = s.filter((x) => x.plek === "rechts" || x.plek === "links");
		expect(zij.length).toBeGreaterThan(0);
		expect(zij.some((x) => x.wereld)).toBe(false);
		expect(s.some((x) => x.plek === "midden" && x.pad === MET && x.wereld)).toBe(true);
		const buitenNotitie = await browser.execute(() => Array.from(document.querySelectorAll(".rollwright-world")).filter((el) => el.closest(".mod-sidedock")).length);
		expect(buitenNotitie).toBe(0);
	});

	it("eis 6b: een losgemaakt venster met een worp krijgt de klasse", async function () {
		const gelukt = await browser.executeObsidian(async ({ app }, MET) => {
			const blad = app.workspace.openPopoutLeaf();
			await blad.openFile(app.vault.getAbstractFileByPath(MET), { state: { mode: "preview" } });
			return true;
		}, MET);
		expect(gelukt).toBe(true);
		let laatste = [];
		await browser.waitUntil(async () => {
			laatste = await stand();
			return laatste.some((s) => s.plek === "venster" && s.pad === MET && s.wereld);
		}, { timeout: 5000, timeoutMsg: `venster zonder klasse: ${JSON.stringify(laatste)}` });
		console.log("NOTITIESFEER eis 6b:", JSON.stringify(laatste));
	});

	it("eis 7: plugin uit, nergens nog de klasse; weer aan, terug", async function () {
		await browser.executeObsidian(async ({ app }) => {
			await app.plugins.disablePlugin("rollwright");
		});
		await browser.pause(800);
		const uit = await stand();
		console.log("NOTITIESFEER eis 7 uit:", JSON.stringify(uit));
		expect(uit.some((s) => s.wereld)).toBe(false);
		const overal = await browser.executeObsidian(({ app }) => {
			let n = 0;
			app.workspace.iterateAllLeaves((leaf) => {
				n += leaf.view.containerEl.ownerDocument.querySelectorAll(".rollwright-world").length;
			});
			return n;
		});
		expect(overal).toBe(0);
		await browser.executeObsidian(async ({ app }) => {
			await app.plugins.enablePlugin("rollwright");
		});
		await browser.pause(800);
		// Een nieuwe plugin leest de bewaarde instellingen (Classic, geen sleutel): zet de skin weer aan.
		await zetPlugin({ skin: "parchment", licenseKey: "E2E-SLEUTEL", licenseCheckedAt: Date.now(), noteWorld: "rolls" });
		await wachtOp({ [MET]: true }, "eis 7 weer aan");
	});
});
