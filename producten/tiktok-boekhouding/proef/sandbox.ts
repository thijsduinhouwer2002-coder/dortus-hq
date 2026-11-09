// Proef in de Moneybird-sandbox "Klopt test" (Jet, 9 nov 2026). Geen product, geen test die bij elke wijziging draait.
// Loopt de vijf open vragen af uit ontwerp-moneybird.md (sandbox-test) en rgs-codes.md (vijfde vraag),
// met onze eigen code waar die bestaat, zodat we ook zien of die tegen het echte Moneybird klopt.
// Ontwerp en veiligheidsregels: proef/README.md. Draait alleen via .github/workflows/tiktok-boekhouding-sandbox.yml.
//
// Veilig: alleen administratie ADM (anders stoppen), alles wat we maken heeft "Dortus proef" of kenmerk
// TikTokShop-99..., en wordt aan het eind weer verwijderd. Het token komt nooit in de uitvoer.

import { writeFileSync } from "node:fs";
import {
  MoneybirdClient,
  MoneybirdFout,
  MONEYBIRD_API,
  administraties,
  boekAfrekening,
  btwTarieven,
  grootboekrekeningen,
  maakMemoriaal,
  type AfrekeningInvoer,
  type Koppeling,
} from "../src/moneybird/index.ts";

const ADM = "503358859490886985"; // "Klopt test", sandbox van Thijs (berichten/jet.md, 9 nov 22:48)
const token = process.env.MONEYBIRD_SANDBOX_TOKEN ?? "";
const uit: string[] = [];
const log = (s: string) => {
  // Vangnet: het token mag nooit in de uitvoer staan.
  const veilig = token ? s.split(token).join("***") : s;
  uit.push(veilig);
  console.log(veilig);
};
const kort = (x: unknown, n = 1500) => {
  const s = typeof x === "string" ? x : JSON.stringify(x);
  return s.length > n ? s.slice(0, n) + " …(ingekort)" : s;
};
const foutUitleg = (e: unknown) => (e instanceof MoneybirdFout ? `${e.soort} (${e.httpStatus}): ${e.message} | body ${kort(e.body, 800)}` : String((e as Error)?.message ?? e));

const run = String(Date.now()).slice(-9);
const gemaakt = { documenten: [] as string[], rekeningen: [] as string[] };
const kenmerken: string[] = [];
// Moneybird cachet GET (introduction.md); het antwoord van POST en PATCH zelf is het bewijs, dus dat loggen we.
const client = new MoneybirdClient({
  accessToken: token,
  fetchFn: async (url, init) => {
    const res = await fetch(url, init);
    const m = (init?.method ?? "GET").toUpperCase();
    if (m !== "GET") {
      const tekst = await res.clone().text();
      log(`  - [${m} via onze code] ${res.status}: ${kort(tekst, 1200)}`);
      for (const id of idsUit(tekst).slice(0, 1)) if (m === "POST" && res.status === 201 && String(url).includes("general_journal_documents") && !gemaakt.documenten.includes(id)) gemaakt.documenten.push(id);
    }
    return res;
  },
});
/** Eerste "id" uit de ruwe tekst, ook als Moneybird hem als getal geeft (dan is JSON.parse al afgerond). */
function idsUit(tekst: string): string[] {
  const m = /"id"\s*:\s*"?(\d+)/.exec(tekst);
  return m ? [m[1]] : [];
}
const versie = (j: any) => `version ${j?.version}, updated_at ${j?.updated_at}`;
const PAD = `/${ADM}/documents/general_journal_documents`;

/** Ruwe aanroep zonder onze foutvertaling, voor de vragen waar we het letterlijke antwoord willen zien. */
async function ruw(methode: string, pad: string, body?: unknown): Promise<{ status: number; tekst: string; json: any }> {
  const res = await fetch(`${MONEYBIRD_API}${pad}.json`, {
    method: methode,
    headers: { authorization: `Bearer ${token}`, accept: "application/json", ...(body ? { "content-type": "application/json" } : {}) },
    body: body ? JSON.stringify(body) : undefined,
  });
  const tekst = await res.text();
  let json: any;
  try { json = tekst ? JSON.parse(tekst) : undefined; } catch { json = undefined; }
  return { status: res.status, tekst, json };
}

function invoer(statementId: string, regels: Array<[AfrekeningInvoer["regels"][number]["soort"], number]>): AfrekeningInvoer {
  return { statementId, statementTime: Math.floor(Date.now() / 1000) - 86400, valuta: "EUR", regels: regels.map(([soort, bedragCenten]) => ({ soort, bedragCenten, statementId })) };
}

async function vraag(naam: string, f: () => Promise<void>) {
  log(`\n## ${naam}`);
  try { await f(); } catch (e) { log(`- FOUT: ${foutUitleg(e)}`); }
}

async function hoofd() {
  log(`# Moneybird-sandbox proef, run ${run}, ${new Date().toISOString()}`);
  if (!token) { log("- GEEN TOKEN: secret MONEYBIRD_SANDBOX_TOKEN is leeg of bestaat niet."); process.exitCode = 3; return; }

  // 0. Toegang en de juiste administratie.
  const a = await ruw("GET", "/administrations");
  log(`\n## 0. Toegang\n- GET /administrations: ${a.status}`);
  if (a.status !== 200) { log(`- Letterlijk antwoord: ${kort(a.tekst, 600)}`); process.exitCode = a.status === 401 ? 2 : 4; return; }
  if (!a.tekst.includes(`"${ADM}"`) && !a.tekst.includes(`:${ADM}`)) { log(`- Administratie ${ADM} staat niet in de lijst; gestopt zonder iets te doen.`); process.exitCode = 5; return; }
  log(`- Id staat ${a.tekst.includes(`"${ADM}"`) ? "als tekst" : "als GETAL (afrondgevaar)"} in het antwoord.`);
  const ruweAdm = (a.json as any[]).find((x) => String(x.id) === ADM || x.name === "Klopt test");
  log(`- Naam: ${ruweAdm?.name}, land ${ruweAdm?.country}, munt ${ruweAdm?.currency}, period_locked_until ${JSON.stringify(ruweAdm?.period_locked_until)}`);
  try { const lijst = await administraties(client); log(`- Onze administraties(): ${lijst.length} gevonden, ids ${lijst.map((x) => x.id).join(", ")}`); }
  catch (e) { log(`- Onze administraties() faalt: ${foutUitleg(e)}`); }
  const lock: string | null = ruweAdm?.period_locked_until ?? null;

  // Rekeningen kiezen.
  const reks = await grootboekrekeningen(client, ADM);
  const mag = (soort: string) => reks.filter((r) => r.soort === soort && r.actief && r.toegestaan.includes("general_journal_document"));
  log(`- ${reks.length} grootboekrekeningen; bruikbaar voor memoriaal: revenue ${mag("revenue").length}, expenses ${mag("expenses").length}, current_assets ${mag("current_assets").length}`);
  const omzet = mag("revenue")[0];
  const kosten = mag("expenses")[0];
  let tegen = mag("current_assets")[0];

  // 5. RGS-codes (vóór de boekingen, want een gelukte 5a geeft de echte tegenrekening).
  await vraag("5. Rekening aanmaken met RGS-code", async () => {
    const maak = async (label: string, naam: string, type: string, rgs: string) => {
      const r = await ruw("POST", `/${ADM}/ledger_accounts`, { rgs_code: rgs, ledger_account: { name: naam, account_type: type } });
      const id = r.json?.id;
      const ruwId = idsUit(r.tekst)[0];
      if (r.status === 201 && ruwId) gemaakt.rekeningen.push(ruwId);
      if (r.status === 201 && String(id) !== ruwId) log(`  - LET OP: id als getal, afgerond ${id}, echt ${ruwId}`);
      if (r.status === 403) log("  - 403: het token heeft waarschijnlijk geen scope settings");
      log(`- ${label}: ${r.status}${r.status === 201 ? `, id ${typeof id} ${id}, taxonomy_item ${kort(r.json?.taxonomy_item, 300)}, allowed ${kort(r.json?.allowed_document_types, 200)}` : `, antwoord ${kort(r.tekst, 500)}`}`);
      return r.status === 201 ? r.json : null;
    };
    const t = await maak("5a tegenrekening BVorOvrOvk (current_assets)", `Dortus proef te ontvangen ${run}`, "current_assets", "BVorOvrOvk");
    if (t && Array.isArray(t.allowed_document_types) && t.allowed_document_types.includes("general_journal_document")) {
      tegen = { id: gemaakt.rekeningen[0] ?? String(t.id), naam: t.name, soort: t.account_type, actief: true, toegestaan: t.allowed_document_types };
    }
    await maak("5b tweede rekening met dezelfde RGS-code", `Dortus proef te ontvangen dubbel ${run}`, "current_assets", "BVorOvrOvk");
    await maak("5c code buiten de Basis-set BVorTusTovTvp", `Dortus proef vraagposten ${run}`, "current_assets", "BVorTusTovTvp");
    await maak("5d terugval BVorTusTov", `Dortus proef tussenrekening ${run}`, "current_assets", "BVorTusTov");
    await maak("5e soort past niet bij code (expenses met BVorOvrOvk)", `Dortus proef verkeerde soort ${run}`, "expenses", "BVorOvrOvk");
    if (t) await maak("5f zelfde naam en soort als 5a", `Dortus proef te ontvangen ${run}`, "current_assets", "BVorOvrOvk");
    else log("- 5f niet zinvol: 5a gaf geen 201");
  });

  if (!omzet || !kosten || !tegen) { log(`\nGeen bruikbare rekeningen (omzet ${!!omzet}, kosten ${!!kosten}, tegen ${!!tegen}); vraag 1 tot 4 overgeslagen.`); return; }
  log(`\nRekeningen voor de proef: omzet "${omzet.naam}", kosten "${kosten.naam}", tegenrekening "${tegen.naam}"`);
  const koppeling: Koppeling = {
    per: { omzet: { grootboekId: omzet.id }, korting: { grootboekId: omzet.id }, commissie: { grootboekId: kosten.id } },
    tegenrekeningId: tegen.id,
  };

  const s1 = `99${run}1`;
  const kenmerk1 = `TikTokShop-${s1}`;
  kenmerken.push(kenmerk1, `TikTokShop-99${run}3`, `TikTokShop-99${run}4`);
  let id1 = "";

  await vraag("1. Memoriaal zonder btw aanmaken en terugzoeken op kenmerk", async () => {
    const r = await boekAfrekening(client, { id: ADM, periodLockedUntil: lock }, invoer(s1, [["omzet", 10000], ["commissie", -1500]]), koppeling);
    log(`- boekAfrekening: ${r.uitkomst}, id ${r.id}${r.fout ? `, fout ${foutUitleg(r.fout)}` : ""}`);
    if (r.id) { id1 = r.id; if (!gemaakt.documenten.includes(r.id)) gemaakt.documenten.push(r.id); }
    if (!id1) { log("- geen id, rest van vraag 1 en vraag 2 overgeslagen"); return; }
    const d = await ruw("GET", `${PAD}/${id1}`);
    log(`- GET document: ${d.status}, ${versie(d.json)}, reference ${d.json?.reference}, date ${d.json?.date}, regels ${kort((d.json?.general_journal_document_entries ?? []).map((e: any) => ({ id: e.id, rek: e.ledger_account_id, debit: e.debit, credit: e.credit, row_order: e.row_order, desc: e.description })), 900)}`);
    for (const [label, filter] of [["exact", `reference:${kenmerk1}`], ["deel (zonder laatste 3 tekens)", `reference:${kenmerk1.slice(0, -3)}`], ["kleine letters", `reference:${kenmerk1.toLowerCase()}`]] as const) {
      const z = await ruw("GET", `${PAD}?filter=${encodeURIComponent(filter)}`);
      const lijst = Array.isArray(z.json) ? z.json : [];
      log(`- zoeken ${label}: ${z.status}, ${lijst.length} gevonden, ons document erbij: ${lijst.some((x: any) => x.id === id1)}`);
    }
    const nog = await boekAfrekening(client, { id: ADM, periodLockedUntil: lock }, invoer(s1, [["omzet", 10000], ["commissie", -1500]]), koppeling);
    if (nog.id && !gemaakt.documenten.includes(nog.id)) gemaakt.documenten.push(nog.id);
    log(`- zelfde afrekening nog eens, zonder bekendId: ${nog.uitkomst} (verwacht ongewijzigd), id gelijk: ${nog.id === id1}`);
  });

  await vraag("2. Vervangen met _destroy en regel-id's als tekst", async () => {
    if (!id1) { log("- overgeslagen: geen document uit vraag 1"); return; }
    const oud = await ruw("GET", `${PAD}/${id1}`);
    const oudeIds = (oud.json?.general_journal_document_entries ?? []).map((e: any) => e.id);
    log(`- oude regel-id's: ${kort(oudeIds)} (soort ${typeof oudeIds[0]}), ${versie(oud.json)}`);
    const r = await boekAfrekening(client, { id: ADM, periodLockedUntil: lock }, invoer(s1, [["omzet", 12000], ["korting", -500], ["commissie", -1500]]), koppeling, { bekendId: id1 });
    log(`- boekAfrekening met nieuwe bedragen: ${r.uitkomst} (verwacht vervangen), id ${r.id}${r.fout ? `, fout ${foutUitleg(r.fout)}` : ""}`);
    const na = await ruw("GET", `${PAD}/${id1}`);
    const regels = na.json?.general_journal_document_entries ?? [];
    log(`- daarna (GET, kan uit de cache komen; het PATCH-antwoord hierboven is het bewijs): ${na.status}, ${versie(na.json)}, ${regels.length} regels (verwacht 4), oude id's nog aanwezig: ${regels.filter((e: any) => oudeIds.includes(e.id)).length}, regels ${kort(regels.map((e: any) => ({ rek: e.ledger_account_id, debit: e.debit, credit: e.credit, row_order: e.row_order })), 700)}`);
    const nog = await boekAfrekening(client, { id: ADM, periodLockedUntil: lock }, invoer(s1, [["omzet", 12000], ["korting", -500], ["commissie", -1500]]), koppeling, { bekendId: id1 });
    log(`- nog eens met bekendId: ${nog.uitkomst} (verwacht ongewijzigd; vervangen kan door de GET-cache komen)`);
  });

  await vraag("3. Regel met tax_rate_id", async () => {
    const tarieven = await btwTarieven(client, ADM);
    log(`- btw-tarieven voor memoriaal (actief): ${kort(tarieven.map((t) => `${t.naam} ${t.percentage}%`), 600)}`);
    const t21 = tarieven.find((t) => Number(t.percentage) === 21) ?? tarieven[0];
    if (!t21) { log("- geen tarief gevonden; overgeslagen"); return; }
    const s3 = `99${run}3`;
    const k3: Koppeling = { ...koppeling, per: { ...koppeling.per, omzet: { grootboekId: omzet.id, btwTariefId: t21.id } } };
    const m = maakMemoriaal(invoer(s3, [["omzet", 12100], ["commissie", -1500]]), k3, { btwToegestaan: true });
    log(`- tarief "${t21.naam}" ${t21.percentage}%, gestuurd: ${kort(m.body.general_journal_document.general_journal_document_entries_attributes, 700)}`);
    const p = await ruw("POST", PAD, m.body);
    log(`- POST: ${p.status}`);
    if (p.status !== 201) { log(`- antwoord: ${kort(p.tekst, 800)}`); return; }
    for (const id of idsUit(p.tekst)) if (!gemaakt.documenten.includes(id)) gemaakt.documenten.push(id);
    log(`- terug gekregen regels (alle velden): ${kort(p.json.general_journal_document_entries, 2500)}`);
    const nog = await boekAfrekening(client, { id: ADM, periodLockedUntil: lock }, invoer(s3, [["omzet", 12100], ["commissie", -1500]]), k3, { btwToegestaan: true, bekendId: idsUit(p.tekst)[0] });
    log(`- onze vergelijking daarna: ${nog.uitkomst} (ongewijzigd betekent: btw breekt het vergelijken niet)`);
  });

  await vraag("4. Boeken in een afgesloten periode", async () => {
    if (!lock) { log("- period_locked_until is leeg in de sandbox, en de API kan geen periode afsluiten (geen endpoint in de OpenAPI): niet te testen zonder handwerk in Moneybird."); return; }
    const s4 = `99${run}4`;
    const m = maakMemoriaal(invoer(s4, [["omzet", 1000]]), koppeling);
    const body = { general_journal_document: { ...m.body.general_journal_document, date: lock } };
    const p = await ruw("POST", PAD, body);
    log(`- ruwe POST op ${lock}: ${p.status}, antwoord ${kort(p.tekst, 800)}`);
    if (p.status === 201) for (const id of idsUit(p.tekst)) if (!gemaakt.documenten.includes(id)) gemaakt.documenten.push(id);
  });
}

async function opruimen() {
  log("\n## Opruimen");
  // Vangnet: ook documenten met onze kenmerken die we zonder id kregen.
  for (const k of kenmerken) {
    try {
      const z = await ruw("GET", `${PAD}?filter=${encodeURIComponent(`reference:${k}`)}`);
      for (const m of z.tekst.matchAll(/"id"\s*:\s*"?(\d+)"?\s*,\s*"administration_id"[^}]*?"reference"\s*:\s*"([^"]*)"/g)) if (m[2] === k && !gemaakt.documenten.includes(m[1])) gemaakt.documenten.push(m[1]);
      if (Array.isArray(z.json)) for (const d of z.json) if (d?.reference === k && typeof d.id === "string" && !gemaakt.documenten.includes(d.id)) gemaakt.documenten.push(d.id);
    } catch (e) { log(`- zoeken op ${k} faalde: ${foutUitleg(e)}`); }
  }
  for (const id of gemaakt.documenten) { const r = await ruw("DELETE", `${PAD}/${id}`); log(`- document ${id}: ${r.status}`); }
  try {
    const l = await ruw("GET", `/${ADM}/ledger_accounts`);
    if (Array.isArray(l.json)) for (const r of l.json) if (typeof r?.name === "string" && r.name.startsWith("Dortus proef") && r.name.includes(run) && typeof r.id === "string" && !gemaakt.rekeningen.includes(r.id)) gemaakt.rekeningen.push(r.id);
  } catch (e) { log(`- rekeningen zoeken faalde: ${foutUitleg(e)}`); }
  for (const id of gemaakt.rekeningen.reverse()) {
    const r = await ruw("DELETE", `/${ADM}/ledger_accounts/${id}`);
    const g = await ruw("GET", `/${ADM}/ledger_accounts/${id}`);
    log(`- rekening ${id}: DELETE ${r.status}${r.status >= 300 ? ` ${kort(r.tekst, 200)}` : ""}, daarna GET ${g.status}${g.status === 200 ? ` active ${g.json?.active} (DELETE zet eerst op inactief)` : ""}`);
  }
}

try {
  await hoofd();
} catch (e) {
  log(`\nONVERWACHTE FOUT: ${foutUitleg(e)}`);
  process.exitCode = 1;
} finally {
  if (token) { try { await opruimen(); } catch (e) { log(`- opruimen faalde: ${foutUitleg(e)}`); } }
  if (process.exitCode === undefined && uit.some((r) => r.includes("FOUT:"))) process.exitCode = 6;
  if (token) writeFileSync(new URL("./uitslag.md", import.meta.url), uit.join("\n") + "\n");
}
