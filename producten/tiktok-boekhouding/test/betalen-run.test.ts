// Toetsen (f) en (g) uit ontwerp-betalen.md, punt 7: wachten kost niets, wacht_ouder, maandwissel, inhalen alleen de
// lopende en vorige maand. Draait ook met D1Opslag (betalen-run-d1.test.ts).
import { test } from "node:test";
import assert from "node:assert/strict";
import { TikTokClient } from "../../tiktok-shop-basis/src/client.ts";
import { MoneybirdClient } from "../src/moneybird/client.ts";
import { Budget } from "../src/budget.ts";
import type { GeheugenOpslag } from "../src/opslag.ts";
import { maakOpslag } from "./opslag-keuze.ts";
import { opnieuw, verwerkWinkel, type BoekDeps } from "../src/verwerk.ts";
import { inst, T0, wereld } from "./wereld.ts";

const DAG = 86400;
const NU = T0 + 10 * DAG; // 16 nov 2026: lopende maand november, vorige oktober
const SEP = T0 - 50 * DAG; // 17 sep 2026: ouder dan de vorige maand
const OKT = T0 - 20 * DAG; // 17 okt 2026: vorige maand
const START = T0 - 80 * DAG; // startdatum in augustus, zodat oude afrekeningen meedoen

function deps(w: ReturnType<typeof wereld>, opslag: GeheugenOpslag, nu = NU, totaal = 45): BoekDeps & { opslag: GeheugenOpslag } {
  const budget = new Budget(totaal);
  const f = budget.omhul(w.fn);
  return {
    tiktok: new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: f, nu: () => nu, slaap: async () => {} }),
    moneybird: new MoneybirdClient({ accessToken: "m", fetchFn: f, nu: () => nu, slaap: async () => {} }),
    accessToken: "t", shopCipher: "c", opslag, budget, nu: () => nu, eigenaar: `run-${nu}`,
  };
}
const status = async (o: GeheugenOpslag, id: string) => (await o.leesStatus(id))?.status;
/** TikTok-verzoeken voor één afrekening (transacties) of voor losse bestellingen. */
const tt = (w: ReturnType<typeof wereld>, deel: string) => w.urls.filter((u) => u.includes(" TT ") && u.includes(deel)).length;
const losseBestellingen = (w: ReturnType<typeof wereld>) => w.urls.filter((u) => u.includes("/orders/")).length;
const gratis = inst({ magBoeken: false, startdatum: START });
const betaald = inst({ magBoeken: true, startdatum: START });
async function runs(w: ReturnType<typeof wereld>, o: GeheugenOpslag, i: Partial<typeof gratis>, van = NU, aantal = 6) {
  for (let k = 0; k < aantal; k++) await verwerkWinkel(deps(w, o, van + k * 1000), { ...gratis, ...i });
}

test("(f) maand vol: geen verzoek naar TikTok voor de afrekening; n te groot: transacties wel, losse bestellingen niet", async () => {
  const w = wereld();
  w.voegToe("8001", T0 + DAG, "PAID", Array(30).fill(10));
  w.voegToe("8002", T0 + 2 * DAG, "PAID", [10]).omzet = "10.00"; // omzet boven 0 in Get Statements: zeker bestellingen
  const o = maakOpslag();
  await runs(w, o, {});
  assert.equal(await status(o, "8001"), "geboekt");
  assert.equal(await status(o, "8002"), "wacht_op_abonnement");
  assert.equal(tt(w, "/statements/8002/"), 0, "maand stond al op 30: niets opgehaald (stap 1)");

  // Nieuwe maand-situatie: 20 geboekt, dan een afrekening van 11: transacties wel, bestellingen niet (stap 2).
  const w2 = wereld();
  w2.voegToe("8101", T0 + DAG, "PAID", Array(20).fill(10));
  w2.voegToe("8102", T0 + 2 * DAG, "PAID", Array(11).fill(10));
  const o2 = maakOpslag();
  await runs(w2, o2, {});
  assert.equal(await status(o2, "8102"), "wacht_op_abonnement");
  assert.ok(tt(w2, "/statements/8102/") >= 1, "transacties opgehaald om n te tellen");
  assert.equal(losseBestellingen(w2), 20, "alleen de bestellingen van 8101");
  // Volgende runs: wachten kost hoogstens de bewaarde transacties (een dag geldig), geen bestellingen.
  const voor = w2.urls.length;
  await runs(w2, o2, {}, NU + 3600, 3);
  assert.equal(losseBestellingen(w2), 20);
  assert.equal(tt(w2, "/statements/8102/"), 1, "binnen een dag uit de bewaarde transacties");
  assert.ok(w2.urls.length - voor <= 3 * 1, "per run alleen de lijst met afrekeningen");
});

test("(f) afrekening zonder bestellingen mag altijd, ook in een volle maand (omzet 0 in Get Statements)", async () => {
  const w = wereld();
  w.voegToe("8201", T0 + DAG, "PAID", Array(30).fill(10));
  const leeg = w.voegToe("8202", T0 + 2 * DAG, "PAID", [], [{ id: "x1", type: "ADJUSTMENT", settlement_amount: "-2.50", adjustment_amount: "-2.50" }]);
  leeg.omzet = "0";
  const o = maakOpslag();
  await runs(w, o, {});
  assert.ok(["geboekt", "geboekt_met_waarschuwing"].includes(String(await status(o, "8202"))), String(await status(o, "8202")));
  assert.equal(((o as any).telling as Map<string, { bestellingen: number }>).get("8202")?.bestellingen, 0);
});

test("(f) te oud zonder abonnement: wacht_ouder zonder verzoek, houdt de markering niet vast en komt niet terug; met abonnement boekt hij wel", async () => {
  const w = wereld();
  w.voegToe("8301", SEP, "PAID", [10]);
  w.voegToe("8302", T0 + DAG, "PAID", [10]);
  const o = maakOpslag();
  await runs(w, o, {}, NU, 2);
  assert.equal(await status(o, "8301"), "wacht_ouder");
  assert.equal(tt(w, "/statements/8301/"), 0, "geen verzoek voor de transacties");
  assert.equal(await status(o, "8302"), "geboekt");
  assert.ok(((o as any).markering ?? 0) > T0 + DAG, "markering voorbij beide");
  const voor = w.urls.length;
  await runs(w, o, {}, NU + 5000, 1);
  assert.equal(w.urls.length - voor, 1, "alleen de lijst met afrekeningen (vanaf de markering)");

  const w2 = wereld();
  w2.voegToe("8401", SEP, "PAID", [10]);
  const o2 = maakOpslag();
  await runs(w2, o2, { magBoeken: true }, NU, 2);
  assert.equal(await status(o2, "8401"), "geboekt", "nieuwe winkel die meteen betaalt: oude afrekening boekt");
});

test("(f, g) maandwissel: wacht_op_abonnement van oktober wordt in december wacht_ouder, bewaarde transacties weg", async () => {
  const w = wereld();
  w.voegToe("8501", OKT, "PAID", Array(30).fill(10));
  w.voegToe("8502", OKT + DAG, "PAID", Array(2).fill(10));
  const o = maakOpslag();
  await runs(w, o, {});
  assert.equal(await status(o, "8501"), "geboekt", "vorige maand: gratis ruimte geldt nog");
  assert.equal(await status(o, "8502"), "wacht_op_abonnement");
  const dec = T0 + 30 * DAG; // 6 dec: oktober is nu ouder dan de vorige maand
  await runs(w, o, {}, dec, 1);
  assert.equal(await status(o, "8502"), "wacht_ouder");
  assert.equal(await o.leesTransacties("8502"), undefined, "bewaren tot af: wacht_ouder telt als af");
  // Met abonnement daarna: wacht_ouder blijft (alleen de knop haalt hem terug).
  await runs(w, o, { magBoeken: true }, dec + 5000, 1);
  assert.equal(await status(o, "8502"), "wacht_ouder");
  // Knop: slaat de leeftijdsregel over; met abonnement boekt hij.
  await opnieuw({ opslag: o, nu: () => dec + 9000 }, "8502");
  await runs(w, o, { magBoeken: true }, dec + 9001, 3);
  assert.equal(await status(o, "8502"), "geboekt");
});

test("(g) inhalen zonder abonnement alleen voor de lopende en vorige maand, ook niet via de knop", async () => {
  const w = wereld();
  w.voegToe("8601", SEP, "PAID", [10]);
  w.voegToe("8602", OKT, "PAID", [10]);
  w.voegToe("8603", T0 + DAG, "PAID", [10]);
  const o = maakOpslag();
  await runs(w, o, {}, NU, 3);
  assert.equal(await status(o, "8601"), "wacht_ouder", "september heeft ruimte, maar is ouder dan de vorige maand");
  assert.equal(await status(o, "8602"), "geboekt");
  assert.equal(await status(o, "8603"), "geboekt");
  // De knop zonder abonnement: blijft wacht_ouder, geen verzoek naar TikTok voor die afrekening, niets naar Moneybird.
  const docs = w.docs.size;
  await opnieuw({ opslag: o, nu: () => NU + 9000 }, "8601");
  await runs(w, o, {}, NU + 9001, 3);
  assert.equal(await status(o, "8601"), "wacht_ouder");
  assert.equal(tt(w, "/statements/8601/"), 0);
  assert.equal(w.docs.size, docs);
  assert.equal(((o as any).telling as Map<string, unknown>).has("8601"), false);
});

test("(f) zonder revenue_amount in Get Statements: maand vol, toch de transacties ophalen (misschien zonder bestellingen)", async () => {
  const w = wereld();
  w.voegToe("8701", T0 + DAG, "PAID", Array(30).fill(10));
  w.voegToe("8702", T0 + 2 * DAG, "PAID", [10]).omzet = "12.50";
  w.voegToe("8703", T0 + 3 * DAG, "PAID", [], [{ id: "y1", type: "ADJUSTMENT", settlement_amount: "-1.00", adjustment_amount: "-1.00" }]);
  const o = maakOpslag();
  await runs(w, o, {});
  assert.equal(tt(w, "/statements/8702/"), 0, "omzet boven 0: wachten zonder verzoek");
  assert.equal(await status(o, "8702"), "wacht_op_abonnement");
  assert.ok(tt(w, "/statements/8703/") >= 1);
  assert.ok(["geboekt", "geboekt_met_waarschuwing"].includes(String(await status(o, "8703"))));
});
