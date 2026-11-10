// Proef 2 in de Moneybird-sandbox "Klopt test" (Jet, 10 nov 2026): verlegde btw op de commissie van TikTok.
// Vraag van Tess (taken.md, 10 nov): is er een inkooptarief voor verlegde btw op diensten uit de EU, en kan
// Klopt dat op de commissieregel van het memoriaal meegeven, zodat rubriek 4b en 5b vanzelf gevuld worden?
// Ontwerp en veiligheidsregels: proef/README.md, kop "Proef 2". Draait alleen via de workflow tiktok-boekhouding-sandbox.yml.
//
// Veilig: alleen administratie ADM (anders stoppen), maakt hoogstens één memoriaal met kenmerk TikTokShop-98...
// en verwijdert dat aan het eind. Maakt geen rekeningen, geen contacten, geen tarieven (de API kan dat ook niet).

import { writeFileSync } from "node:fs";

const API = "https://moneybird.com/api/v2";
const ADM = "503358859490886985"; // "Klopt test", sandbox van Thijs (berichten/jet.md, 9 nov 22:48)
const token = process.env.MONEYBIRD_SANDBOX_TOKEN ?? "";
const uit: string[] = [];
const log = (s: string) => {
  const veilig = token ? s.split(token).join("***") : s; // het token mag nooit in de uitvoer staan
  uit.push(veilig);
  console.log(veilig);
};
const kort = (x: unknown, n = 1500) => {
  const s = typeof x === "string" ? x : JSON.stringify(x);
  return s.length > n ? s.slice(0, n) + " …(ingekort)" : s;
};

async function ruw(methode: string, pad: string, body?: unknown): Promise<{ status: number; tekst: string; json: any; wacht?: string | null }> {
  const res = await fetch(`${API}${pad}${pad.includes("?") ? "" : ".json"}`, {
    method: methode,
    headers: { authorization: `Bearer ${token}`, accept: "application/json", ...(body ? { "content-type": "application/json" } : {}) },
    body: body ? JSON.stringify(body) : undefined,
  });
  const tekst = await res.text();
  let json: any;
  try { json = tekst ? JSON.parse(tekst) : undefined; } catch { json = undefined; }
  return { status: res.status, tekst, json, wacht: res.headers.get("retry-after") };
}
const tarieven = (filter?: string) => ruw("GET", `/${ADM}/tax_rates.json?per_page=100${filter ? `&filter=${encodeURIComponent(filter)}` : ""}`);
const regel = (t: any) => `${t.name} | ${t.percentage}% | ${t.tax_rate_type} | actief ${t.active} | land ${t.country} | show_tax ${t.show_tax}`;

const gemaakt: string[] = [];

async function hoofd() {
  log(`# Moneybird-sandbox proef 2: verlegde btw, ${new Date().toISOString()}`);
  if (!token) { log("Geen MONEYBIRD_SANDBOX_TOKEN: niets gedaan."); return; }
  const adm = await ruw("GET", "/administrations");
  if (adm.status !== 200) { log(`- GET /administrations: ${adm.status} ${kort(adm.tekst, 300)}: gestopt`); return; }
  if (!/"id"\s*:\s*"?503358859490886985/.test(adm.tekst)) { log("- administratie Klopt test staat er niet in: gestopt zonder iets te doen"); return; }

  log("\n## A. Welke btw-tarieven heeft een nieuwe administratie?");
  const lijsten: Record<string, string | undefined> = {
    "zonder filter": undefined,
    "alleen actief": "active:true",
    "alleen inactief": "active:false",
    "inkoop, actief en inactief": "tax_rate_type:purchase_invoice",
    "memoriaal, actief en inactief": "tax_rate_type:general_journal_document",
    "naam bevat 'verlegd'": "partial_name:verlegd",
    "naam bevat 'EU'": "partial_name:EU",
  };
  const alle = new Map<string, any>();
  for (const [naam, f] of Object.entries(lijsten)) {
    const r = await tarieven(f);
    const rij = Array.isArray(r.json) ? r.json : [];
    if (rij.length === 100) log("  (precies 100: er kan een tweede pagina zijn)");
    for (const t of rij) alle.set(String(t.id), t);
    log(`- ${naam}${f ? ` (\`${f}\`)` : ""}: ${r.status}, ${rij.length} tarieven${rij.length ? ": " + rij.map((t: any) => `"${t.name}" ${t.tax_rate_type}${t.active ? "" : " (inactief)"}`).join(", ") : ""}`);
  }
  log(`- alle velden van elk gevonden tarief (${alle.size}):`);
  for (const t of alle.values()) log(`  - ${regel(t)} | velden: ${Object.keys(t).join(",")}`);
  const verlegd = [...alle.values()].filter((t) => /verleg|reverse/i.test(String(t.name)));
  log(`- tarieven met "verlegd" in de naam: ${verlegd.length ? verlegd.map(regel).join("; ") : "geen"}`);
  log("- Het API-antwoord heeft geen veld voor de rubriek van de aangifte (zie velden hierboven); welke rubriek een tarief vult, is via de API niet te zien.");

  log("\n## B. Inkooptarief op een memoriaalregel");
  // Heeft iemand "Binnen EU 21% (btw verlegd)" aangezet (lijst van Thijs, 10 nov), dan dat tarief; anders het gewone inkooptarief 21%.
  const inkoop = verlegd.find((t) => t.active && t.tax_rate_type !== "sales_invoice")
    ?? [...alle.values()].find((t) => t.tax_rate_type === "purchase_invoice" && t.active && Number(t.percentage) === 21);
  const reks = await ruw("GET", `/${ADM}/ledger_accounts`);
  const lijst = Array.isArray(reks.json) ? reks.json : [];
  const magMemo = (soort: string) => lijst.filter((r: any) => r.account_type === soort && (r.allowed_document_types ?? []).includes("general_journal_document") && r.active !== false);
  const kosten = magMemo("expenses")[0];
  // Geen debiteuren of crediteuren als tegenrekening: die kunnen om een contact vragen en dan zegt de 422 niets over het tarief.
  const tegen = magMemo("current_assets").find((r: any) => !/debiteur|crediteur/i.test(String(r.name)));
  if (!inkoop || !kosten || !tegen) {
    log(`- niet te testen: inkooptarief 21% ${inkoop ? "ja" : "nee"}, kostenrekening ${kosten ? "ja" : "nee"}, tegenrekening ${tegen ? "ja" : "nee"} (GET ledger_accounts ${reks.status})`);
  } else {
    const ref = `TikTokShop-98${String(Date.now()).slice(-9)}`;
    const datum = new Date(Date.now() - 86400000).toISOString().slice(0, 10);
    const periode = datum.slice(0, 4) + datum.slice(5, 7);
    const voor = await btwRapport(periode, "vóór de boeking");
    const body = {
      general_journal_document: {
        reference: ref,
        date: datum,
        general_journal_document_entries_attributes: [
          { ledger_account_id: kosten.id, debit: "10.00", credit: "0.00", description: "TikTok Shop commissie (proef verlegde btw)", row_order: 1, tax_rate_id: inkoop.id },
          { ledger_account_id: tegen.id, debit: "0.00", credit: "10.00", description: "TikTok Shop te ontvangen (proef verlegde btw)", row_order: 2 },
        ],
      },
    };
    log(`- inkooptarief "${inkoop.name}" (${inkoop.tax_rate_type}) op de kostenregel "${kosten.name}", tegenrekening "${tegen.name}"`);
    const p = await ruw("POST", `/${ADM}/documents/general_journal_documents`, body);
    const id = /"id"\s*:\s*"?(\d+)/.exec(p.tekst)?.[1];
    if (p.status === 201 && id) gemaakt.push(id);
    log(`- POST: ${p.status}`);
    log(`- antwoord: ${kort(p.tekst, 2500)}`);
    const regels = p.json?.general_journal_document_entries ?? [];
    const metTarief = regels.filter((e: any) => e.tax_rate_id != null).length;
    log(`- regels terug: ${regels.length} (gestuurd 2), regels met tax_rate_id: ${metTarief} (het antwoord-schema van een memoriaalregel kent dat veld niet, dus dit zegt alleen iets over extra btw-regels)`);
    if (p.status !== 201) { log("- uitkomst B: geweigerd, zie antwoord"); return; }
    // Het echte bewijs: telt het btw-rapport van die maand het inkooptarief na de boeking mee?
    const na = await btwRapport(periode, "na de boeking");
    if (voor === undefined || na === undefined) { log("- uitkomst B: niet vast te stellen, het btw-rapport is niet leesbaar (zie status hierboven)"); return; }
    const verschil = na.filter((t) => t.tax_rate_id === inkoop.id).map((t) => Number(t.amount)).reduce((a, b) => a + b, 0)
      - voor.filter((t) => t.tax_rate_id === inkoop.id).map((t) => Number(t.amount)).reduce((a, b) => a + b, 0);
    log(`- grondslag van "${inkoop.name}" (inkoop) in het rapport, na min vóór: ${verschil}`);
    // Een verlegd tarief kan twee rijen geven (bijvoorbeeld NL/4b en NL/5b): per rubriek grondslag en btw tonen.
    for (const t of na.filter((t) => t.tax_rate_id === inkoop.id)) log(`  - na: ${t.report_reference} grondslag ${t.amount} btw ${t.tax}`);
    log(`- uitkomst B: ${verschil === 0 ? "het btw-rapport telt het inkooptarief op een memoriaalregel niet mee (let op: GET kan uit de cache komen, zie de twee rapporten)" : "het btw-rapport telt de memoriaalregel mee onder het inkooptarief"}`);
  }
}

/** Btw-rapport van één maand (scopes documents en sales_invoices; een 403 loggen we gewoon). */
async function btwRapport(periode: string, wanneer: string): Promise<any[] | undefined> {
  // Run 42753250994 gaf hier twee keer 429 "Retry later" (rapporten hebben kennelijk een strengere grens), dus wachten en opnieuw.
  let r = await ruw("GET", `/${ADM}/reports/tax.json?period=${periode}`);
  for (let poging = 1; r.status === 429 && poging <= 4; poging++) {
    const ra = Number(r.wacht);
    const sec = Math.min(60, Math.max(5, Number.isFinite(ra) ? (ra > 1e9 ? ra - Date.now() / 1000 : ra) : 15 * poging));
    log(`  - 429 (Retry-After ${r.wacht ?? "geen"}), poging ${poging}: ${Math.round(sec)} s wachten`);
    await new Promise((k) => setTimeout(k, sec * 1000));
    r = await ruw("GET", `/${ADM}/reports/tax.json?period=${periode}`);
  }
  const rij = Array.isArray(r.json?.tax_rates) ? r.json.tax_rates : undefined;
  log(`- btw-rapport ${periode} ${wanneer}: ${r.status}${rij ? `, ${rij.length} tarieven: ${rij.map((t: any) => `"${t.name}" ${t.type} ${t.report_reference} grondslag ${t.amount} btw ${t.tax}`).join("; ") || "leeg"}` : ` ${kort(r.tekst, 400)}`}`);
  return rij;
}

async function opruimen() {
  log("\n## Opruimen");
  for (const id of gemaakt) {
    const r = await ruw("DELETE", `/${ADM}/documents/general_journal_documents/${id}`);
    log(`- document ${id}: ${r.status}`);
    if (r.status !== 200 && r.status !== 204) { log(`  LET OP: niet verwijderd, ${kort(r.tekst, 300)}`); process.exitCode = 1; }
  }
  if (!gemaakt.length) log("- niets gemaakt");
}

try {
  await hoofd();
} catch (e) {
  log(`FOUT: ${String((e as Error)?.message ?? e)}`);
  process.exitCode = 1;
} finally {
  try { await opruimen(); } catch (e) { log(`FOUT bij opruimen: ${String((e as Error)?.message ?? e)}`); process.exitCode = 1; }
  if (token) writeFileSync(new URL("./uitslag-btw.md", import.meta.url), uit.join("\n") + "\n");
}
