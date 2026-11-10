// Toetsen (c, keuze), (i) zegOp en (l) budget uit ontwerp-betalen.md, punt 7: de client voor Polar.
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { nepFetch, type NepAntwoord } from "./hulp.ts";
import { NU } from "./ontkoppel-hulp.ts";
import { Budget, isBudgetOp } from "../src/budget.ts";
import { PolarClient, PolarFout } from "../src/polar/client.ts";
import { kiesAbonnement, microVan, standUitState, type PolarAbonnement } from "../src/polar/abonnement.ts";

const iso = (s: number) => new Date(s * 1000).toISOString().replace(/Z$/, "000Z");
const sub = (id: string, eind: number, opties: { winkel?: unknown; opgezegd?: boolean; begin?: number } = {}): PolarAbonnement => ({
  id, metadata: opties.winkel === undefined ? {} : { winkel: opties.winkel as string }, status: "active",
  current_period_end: iso(eind), cancel_at_period_end: opties.opgezegd ?? false, started_at: iso(opties.begin ?? NU - 1000), created_at: iso(opties.begin ?? NU - 1000),
});
const state = (subs: PolarAbonnement[], extra: Record<string, unknown> = {}) => ({ id: "cus-1", type: "individual", external_id: "w1", email: "x@y.nl", deleted_at: null, active_subscriptions: subs, ...extra });
const INST = { api: "https://sandbox-api.polar.sh/", token: "oat_geheim", productId: "prod-1", webhookSecret: "whsec_x", terugUrl: "https://dortus.com/klopt/terug" };

function client(antwoorden: NepAntwoord[], opties: { budget?: Budget; db?: NepD1 } = {}) {
  const nep = nepFetch(antwoorden);
  const slapen: number[] = [];
  const budget = opties.budget ?? new Budget(50);
  const c = new PolarClient({ instellingen: INST, budget, fetchFn: nep.fn, slaap: async (ms) => { slapen.push(ms); }, nu: () => NU, db: opties.db as any });
  return { c, verzoeken: nep.verzoeken, slapen, budget };
}

// --- (c) keuze van het abonnement ----------------------------------------------------------------------------------

test("(c) keuze: met metadata.winkel die van deze winkel, ook als een andere verder loopt", () => {
  const lijst = [sub("a", NU + 9000, { winkel: "w2" }), sub("b", NU + 100, { winkel: "w1" }), sub("c", NU + 9999)];
  assert.equal(kiesAbonnement(lijst, "w1")?.id, "b");
  assert.equal(kiesAbonnement(lijst, "w2")?.id, "a");
  assert.equal(kiesAbonnement([sub("n", NU + 5, { winkel: 123 })], "123")?.id, "n", "metadata als getal");
});

test("(c) keuze: zonder metadata.winkel het enige, bij meerdere het met de verste current_period_end", () => {
  assert.equal(kiesAbonnement([sub("enig", NU + 10)], "w1")?.id, "enig");
  assert.equal(kiesAbonnement([sub("kort", NU + 10), sub("lang", NU + 99), sub("mid", NU + 50)], "w1")?.id, "lang");
  assert.equal(kiesAbonnement([], "w1"), undefined);
  assert.equal(kiesAbonnement(undefined, "w1"), undefined);
});

test("(c) keuze: wel abonnementen met metadata.winkel maar niet van deze winkel: geen, ook niet het abonnement zonder", () => {
  assert.equal(kiesAbonnement([sub("ander", NU + 10, { winkel: "w2" }), sub("zonder", NU + 10)], "w1"), undefined);
  assert.deepEqual(standUitState(state([sub("ander", NU + 10, { winkel: "w2" })]), "w1", 7), { actief: false, tot: null, id: null, opgezegd: false, stand: 7 });
});

test("(c) standUitState: velden, verwijderde klant, en tijden met microseconden", () => {
  assert.deepEqual(standUitState(state([sub("s", NU + 10, { opgezegd: true })]), "w1", 5), { actief: true, tot: NU + 10, id: "s", opgezegd: true, stand: 5 });
  assert.equal(standUitState(state([sub("s", NU + 10)], { deleted_at: iso(NU) }), "w1", 5).actief, false);
  assert.equal(standUitState(null, "w1", 5).actief, false);
  assert.equal(microVan("2026-01-01T00:00:00.000001Z")! - microVan("2026-01-01T00:00:00Z")!, 1);
  assert.equal(microVan("2026-01-01T01:00:00.5+01:00"), microVan("2026-01-01T00:00:00.500000Z"));
  assert.equal(microVan("2026-01-01"), null);
  assert.equal(microVan(1767225600), null);
});

// --- standVan, koppen en (l) budget --------------------------------------------------------------------------------

test("(l) standVan: één verzoek uit de pot, met Bearer, Polar-Version en de winkelsleutel als external id", async () => {
  const { c, verzoeken, budget } = client([{ json: state([sub("s", NU + 10, { winkel: "w1" })]) }]);
  const uit = await c.standVan("w/1");
  assert.deepEqual(uit, { abonnement: { actief: false, tot: null, id: null, opgezegd: false, stand: NU * 1_000_000 }, klant: "cus-1" }, "metadata w1 hoort niet bij w/1");
  assert.equal(budget.over, 49);
  assert.equal(verzoeken.length, 1);
  assert.equal(verzoeken[0].url.href, "https://sandbox-api.polar.sh/v1/customers/external/w%2F1/state");
  assert.equal(verzoeken[0].method, "GET");
  assert.equal(verzoeken[0].headers.authorization, "Bearer oat_geheim");
  assert.equal(verzoeken[0].headers["polar-version"], "2026-10");
  const { c: c2 } = client([{ json: state([sub("s", NU + 10, { winkel: "w1" })]) }]);
  assert.equal((await c2.standVan("w1")).abonnement.actief, true);
});

test("(l) budget op: geen verzoek, BudgetOp", async () => {
  const { c, verzoeken } = client([{ json: state([]) }], { budget: new Budget(0) });
  await assert.rejects(c.standVan("w1"), (e) => isBudgetOp(e));
  assert.equal(verzoeken.length, 0);
});

test("standVan: 404 is niet actief zonder klant; 500 en netwerk geven PolarFout", async () => {
  const { c } = client([{ status: 404, json: { error: "ResourceNotFound", detail: "Customer not found." } }]);
  assert.deepEqual(await c.standVan("w1"), { abonnement: { actief: false, tot: null, id: null, opgezegd: false, stand: NU * 1_000_000 }, klant: null });
  const { c: c2 } = client([{ status: 500 }]);
  await assert.rejects(c2.standVan("w1"), (e) => e instanceof PolarFout && e.httpStatus === 500);
  const { c: c3 } = client([{ fout: new TypeError("fetch failed") }]);
  await assert.rejects(c3.standVan("w1"), (e) => e instanceof PolarFout && e.httpStatus === 0);
});

test("(l) 429: één keer herhalen als Retry-After hoogstens 2 s is (telt ook in de pot), anders opgeven", async () => {
  const een = client([{ status: 429, headers: { "retry-after": "2" } }, { json: state([]) }]);
  assert.equal((await een.c.standVan("w1")).abonnement.actief, false);
  assert.deepEqual(een.slapen, [2000]);
  assert.equal(een.budget.over, 48, "herhaling telt mee");
  const lang = client([{ status: 429, headers: { "retry-after": "3" } }, { json: state([]) }]);
  await assert.rejects(lang.c.standVan("w1"), (e) => e instanceof PolarFout && e.httpStatus === 429);
  assert.equal(lang.verzoeken.length, 1);
  const zonder = client([{ status: 429 }, { json: state([]) }]);
  await assert.rejects(zonder.c.standVan("w1"), (e) => e instanceof PolarFout && e.httpStatus === 429);
  const twee = client([{ status: 429, headers: { "retry-after": "1" } }, { status: 429, headers: { "retry-after": "1" } }, { json: state([]) }]);
  await assert.rejects(twee.c.standVan("w1"), (e) => e instanceof PolarFout && e.httpStatus === 429);
  assert.equal(twee.verzoeken.length, 2, "maar één herhaling");
});

// --- maakCheckout en portaalLink -----------------------------------------------------------------------------------

test("maakCheckout: zet polar_gestart (alleen de eerste keer), stuurt product, sleutel, metadata en IP; geeft de url", async () => {
  const db = new NepD1("w1");
  const { c, verzoeken, budget } = client([{ status: 201, json: { id: "co-1", url: "https://sandbox.polar.sh/checkout/co-1" } }], { db });
  assert.equal(await c.maakCheckout("w1", "203.0.113.7"), "https://sandbox.polar.sh/checkout/co-1");
  assert.equal(budget.over, 48, "D1 en fetch uit dezelfde pot");
  assert.equal((db.sqlite.prepare("SELECT polar_gestart p FROM winkels WHERE id = 'w1'").get() as any).p, NU);
  assert.equal(verzoeken[0].method, "POST");
  assert.equal(verzoeken[0].url.pathname, "/v1/checkouts/");
  assert.deepEqual(JSON.parse(verzoeken[0].body!), {
    products: ["prod-1"], external_customer_id: "w1", metadata: { winkel: "w1" }, success_url: INST.terugUrl, customer_ip_address: "203.0.113.7",
  });
  db.sqlite.prepare("UPDATE winkels SET polar_gestart = 5 WHERE id = 'w1'").run();
  await c.maakCheckout("w1");
  assert.equal((db.sqlite.prepare("SELECT polar_gestart p FROM winkels WHERE id = 'w1'").get() as any).p, 5, "eerste checkout blijft");
  assert.equal(JSON.parse(verzoeken[1].body!).customer_ip_address, undefined);
});

test("maakCheckout: onbekende of ontkoppelde winkel geeft een fout zonder checkout; fout van Polar geeft PolarFout", async () => {
  const db = new NepD1("w1", "w2");
  db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = 1 WHERE id = 'w2'").run();
  const { c, verzoeken } = client([{ status: 201, json: { url: "u" } }], { db });
  await assert.rejects(c.maakCheckout("w2"), /ontkoppeld/);
  await assert.rejects(c.maakCheckout("w9"), /onbekend/);
  assert.equal(verzoeken.length, 0);
  const { c: c2 } = client([{ status: 422, json: { detail: [] } }], { db });
  await assert.rejects(c2.maakCheckout("w1"), (e) => e instanceof PolarFout && e.httpStatus === 422);
});

test("portaalLink: customer session met external_customer_id en return_url", async () => {
  const { c, verzoeken } = client([{ status: 201, json: { customer_portal_url: "https://polar.sh/portaal?t=1" } }]);
  assert.equal(await c.portaalLink("w1"), "https://polar.sh/portaal?t=1");
  assert.equal(verzoeken[0].url.pathname, "/v1/customer-sessions/");
  assert.deepEqual(JSON.parse(verzoeken[0].body!), { external_customer_id: "w1", return_url: INST.terugUrl });
  const { c: c2 } = client([{ status: 409, json: { error: "AmbiguousExternalCustomerID", detail: "x" } }]);
  await assert.rejects(c2.portaalLink("w1"), (e) => e instanceof PolarFout && e.code === "AmbiguousExternalCustomerID");
});

// --- (i) zegOp -----------------------------------------------------------------------------------------------------

test("(i) zegOp 200: alleen actieve, niet opgezegde abonnementen van deze winkel krijgen cancel_at_period_end", async () => {
  const subs = [sub("eigen", NU + 10, { winkel: "w1" }), sub("zonder", NU + 10), sub("al-op", NU + 10, { opgezegd: true }), sub("ander", NU + 10, { winkel: "w2" })];
  const { c, verzoeken } = client([{ json: state(subs) }, { json: {} }, { json: {} }]);
  assert.deepEqual(await c.zegOp("w1"), { uitkomst: "gelukt" });
  const patches = verzoeken.filter((v) => v.method === "PATCH");
  assert.deepEqual(patches.map((v) => v.url.pathname), ["/v1/subscriptions/eigen", "/v1/subscriptions/zonder"]);
  assert.deepEqual(JSON.parse(patches[0].body!), { cancel_at_period_end: true });
});

test("(i) zegOp: 403 AlreadyCanceledSubscription en 404 zijn gelukt; nooit klant (404 op state) ook", async () => {
  for (const a of [{ status: 403, json: { error: "AlreadyCanceledSubscription", detail: "x" } }, { status: 404, json: { error: "ResourceNotFound", detail: "x" } }]) {
    const { c } = client([{ json: state([sub("s", NU + 10)]) }, a]);
    assert.deepEqual(await c.zegOp("w1"), { uitkomst: "gelukt" }, String(a.status));
  }
  const { c, verzoeken } = client([{ status: 404, json: { error: "ResourceNotFound", detail: "Customer not found." } }]);
  assert.deepEqual(await c.zegOp("w1"), { uitkomst: "gelukt" });
  assert.equal(verzoeken.length, 1);
});

test("(i) zegOp: 409, 5xx, 429, ander 403, netwerk of fout bij het lezen van de state: later", async () => {
  const gevallen: NepAntwoord[][] = [
    [{ json: state([sub("s", NU + 10)]) }, { status: 409, json: { error: "SubscriptionLocked", detail: "x" } }],
    [{ json: state([sub("s", NU + 10)]) }, { status: 502 }],
    [{ json: state([sub("s", NU + 10)]) }, { status: 429, headers: { "retry-after": "60" } }],
    [{ json: state([sub("s", NU + 10)]) }, { status: 403, json: { error: "InactiveSubscription", detail: "x" } }],
    [{ json: state([sub("s", NU + 10)]) }, { fout: new TypeError("fetch failed") }],
    [{ status: 503 }],
  ];
  for (const g of gevallen) {
    const { c } = client(g);
    const u = await c.zegOp("w1");
    assert.equal(u.uitkomst, "later", JSON.stringify(g[g.length - 1]));
  }
});

test("(i) zegOp: abonnement dat na `voor` begon niet opzeggen; budget op wordt uitgesteld", async () => {
  const { c, verzoeken } = client([{ json: state([sub("oud", NU + 10, { begin: NU - 10 }), sub("nieuw", NU + 10, { begin: NU + 10 })]) }, { json: {} }]);
  assert.deepEqual(await c.zegOp("w1", NU), { uitkomst: "gelukt" });
  assert.deepEqual(verzoeken.filter((v) => v.method === "PATCH").map((v) => v.url.pathname), ["/v1/subscriptions/oud"]);
  const { c: c2, verzoeken: v2 } = client([{ json: state([sub("s", NU + 10)]) }, { json: {} }], { budget: new Budget(1) });
  assert.deepEqual(await c2.zegOp("w1"), { uitkomst: "uitgesteld" });
  assert.equal(v2.length, 1, "PATCH niet verstuurd");
});
