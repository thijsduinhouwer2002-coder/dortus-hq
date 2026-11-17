import { test } from "node:test";
import assert from "node:assert/strict";
import {
  controleer, beoordeel, verwerk, isPro, melding, moetControleren,
  DAG, MELDINGEN, GUMROAD_URL,
} from "../ext/lib/sleutel.js";

const NU = Date.parse("2026-11-17T08:00:00Z");
const P1 = "abonnement-id";
const P2 = "levenslang-id";

function antwoord(status, json) {
  return { status, ok: status >= 200 && status < 300, json: async () => { if (json === undefined) throw new Error("geen json"); return json; } };
}
const goedJson = (extra = {}) => ({ success: true, uses: 1, purchase: { refunded: false, disputed: false, chargebacked: false, ...extra } });
const onbekendJson = { success: false, message: "That license does not exist for the provided product." }; // GEZIEN 17 nov

function nepFetch(perProduct, log = []) {
  return async (url, opts) => {
    assert.equal(url, GUMROAD_URL);
    assert.equal(opts.method, "POST");
    const p = new URLSearchParams(opts.body);
    assert.equal(p.get("increment_uses_count"), "false");
    log.push(p.get("product_id"));
    const r = perProduct[p.get("product_id")];
    if (r instanceof Error) throw r;
    if (r === "hangt") return new Promise((_, nee) => opts.signal.addEventListener("abort", () => nee(new Error("abort"))));
    return r;
  };
}

test("goede sleutel bij het tweede product is genoeg", async () => {
  const log = [];
  const r = await controleer(" abc ", [P1, P2], { fetch: nepFetch({ [P1]: antwoord(404, onbekendJson), [P2]: antwoord(200, goedJson()) }, log), nu: NU });
  assert.deepEqual(r, { uitslag: "goed", reden: "goed", productId: P2 });
  assert.deepEqual(log, [P1, P2]);
});

test("onbekende sleutel (404) is nee", async () => {
  const r = await controleer("x", [P1], { fetch: nepFetch({ [P1]: antwoord(404, onbekendJson) }), nu: NU });
  assert.equal(r.uitslag, "nee"); assert.equal(r.reden, "onbekend");
});

test("lege sleutel vraagt niets aan Gumroad", async () => {
  const log = [];
  const r = await controleer("  ", [P1], { fetch: nepFetch({}, log), nu: NU });
  assert.equal(r.reden, "leeg"); assert.equal(log.length, 0);
});

test("terugbetaald, betwist en chargeback zijn nee", () => {
  for (const k of ["refunded", "disputed", "chargebacked"]) {
    assert.equal(beoordeel(goedJson({ [k]: true }), NU).reden, "terugbetaald");
  }
});

test("abonnement: alle drie de velden zijn een einddatum, pas daarna is het nee (Gumroad artikel 76)", () => {
  assert.equal(beoordeel(goedJson({ subscription_cancelled_at: "2026-12-10T00:00:00Z" }), NU).uitslag, "goed");
  assert.equal(beoordeel(goedJson({ subscription_cancelled_at: "2026-11-10T00:00:00Z" }), NU).reden, "gestopt");
  assert.equal(beoordeel(goedJson({ subscription_ended_at: "2026-12-10T00:00:00Z" }), NU).uitslag, "goed");
  assert.equal(beoordeel(goedJson({ subscription_ended_at: "2026-11-16T00:00:00Z" }), NU).reden, "gestopt");
  assert.equal(beoordeel(goedJson({ subscription_failed_at: "2026-12-16T00:00:00Z" }), NU).uitslag, "goed");
  assert.equal(beoordeel(goedJson({ subscription_failed_at: "2026-11-16T00:00:00Z" }), NU).reden, "betaling_mislukt");
});

test("404 zonder het foutantwoord van Gumroad (proxy, wifi-inlog) is storing, geen nee", async () => {
  for (const g of [antwoord(404, undefined), antwoord(404, { error: "x" }), antwoord(403, undefined), antwoord(200, { success: true }), antwoord(200, { foo: 1 })]) {
    const r = await controleer("abc", [P1], { fetch: nepFetch({ [P1]: g }), nu: NU });
    assert.equal(r.uitslag, "storing");
  }
});

test("lege of ontbrekende productlijst pakt Pro nooit af", async () => {
  assert.equal((await controleer("abc", [], { fetch: nepFetch({}), nu: NU })).uitslag, "storing");
  assert.equal((await controleer("abc", undefined, { fetch: nepFetch({}), nu: NU })).uitslag, "storing");
});

test("sleutel over meer regels of als getal wordt netjes gelezen", async () => {
  const log = [];
  const f = async (url, opts) => { log.push(new URLSearchParams(opts.body).get("license_key")); return antwoord(200, goedJson()); };
  await controleer(" AAAA-BBBB\n CCCC ", [P1], { fetch: f, nu: NU });
  await controleer(1234, [P1], { fetch: f, nu: NU });
  await controleer("AA\u200BBB\uFEFF", [P1], { fetch: f, nu: NU });
  assert.deepEqual(log, ["AAAA-BBBBCCCC", "1234", "AABB"]);
  const rec = verwerk(verwerk(null, "AAAA-BBBB", { uitslag: "goed", productId: P1 }, NU), " AAAA-BBBB ", { uitslag: "storing" }, NU + DAG);
  assert.ok(isPro(rec, NU + DAG));
});

test("klok die vooruit stond geeft geen gratis Pro: meteen opnieuw controleren en geen extra tijd", () => {
  const toekomst = NU + 365 * DAG;
  let rec = verwerk(null, "abc", { uitslag: "goed", productId: P1 }, toekomst);
  assert.ok(moetControleren(rec, NU));
  rec = verwerk(rec, "abc", { uitslag: "storing" }, NU);
  assert.equal(rec.laatsteGoed, NU);
  assert.ok(!isPro(rec, NU + 31 * DAG));
  rec = verwerk(rec, "abc", { uitslag: "nee", reden: "terugbetaald" }, NU + DAG);
  assert.ok(!isPro(rec, NU + DAG));
});

test("na een nee en dan een storing ziet de gebruiker nog de echte reden", () => {
  let rec = verwerk(null, "abc", { uitslag: "goed", productId: P1 }, NU);
  rec = verwerk(rec, "abc", { uitslag: "nee", reden: "terugbetaald" }, NU + DAG);
  rec = verwerk(rec, "abc", { uitslag: "storing" }, NU + 2 * DAG);
  assert.equal(melding(rec, NU + 2 * DAG), MELDINGEN.terugbetaald);
});

test("500, 503, 429, kapotte json, geen netwerk en time-out zijn storing, geen nee", async () => {
  const gevallen = [antwoord(500, {}), antwoord(503, undefined), antwoord(429, {}), antwoord(200, undefined), new TypeError("Failed to fetch"), "hangt"];
  for (const g of gevallen) {
    const r = await controleer("abc", [P1], { fetch: nepFetch({ [P1]: g }), nu: NU, tijdslimietMs: 20 });
    assert.equal(r.uitslag, "storing", String(g && g.status));
  }
});

test("terugbetaald bij het ene product wint van storing bij het andere", async () => {
  const r = await controleer("abc", [P1, P2], { fetch: nepFetch({ [P1]: antwoord(500, {}), [P2]: antwoord(200, goedJson({ refunded: true })) }), nu: NU });
  assert.equal(r.reden, "terugbetaald");
});

test("onbekend bij het ene en storing bij het andere is storing (we weten het niet)", async () => {
  const r = await controleer("abc", [P1, P2], { fetch: nepFetch({ [P1]: antwoord(404, onbekendJson), [P2]: new TypeError("x") }), nu: NU });
  assert.equal(r.uitslag, "storing");
});

test("Pro blijft 30 dagen Pro bij storingen, daarna uit met uitleg", () => {
  let rec = verwerk(null, "abc", { uitslag: "goed", productId: P1 }, NU);
  assert.ok(isPro(rec, NU));
  rec = verwerk(rec, "abc", { uitslag: "storing" }, NU + 29 * DAG);
  assert.ok(isPro(rec, NU + 29 * DAG));
  assert.equal(melding(rec, NU + 29 * DAG), MELDINGEN.storing);
  assert.ok(isPro(rec, NU + 30 * DAG));
  assert.ok(!isPro(rec, NU + 31 * DAG));
  assert.equal(melding(rec, NU + 31 * DAG), MELDINGEN.storing_te_lang);
  rec = verwerk(rec, "abc", { uitslag: "goed", productId: P1 }, NU + 32 * DAG);
  assert.ok(isPro(rec, NU + 32 * DAG));
});

test("een duidelijk nee haalt Pro meteen weg, met de reden", () => {
  let rec = verwerk(null, "abc", { uitslag: "goed", productId: P1 }, NU);
  rec = verwerk(rec, "abc", { uitslag: "nee", reden: "terugbetaald" }, NU + DAG);
  assert.ok(!isPro(rec, NU + DAG));
  assert.equal(melding(rec, NU + DAG), MELDINGEN.terugbetaald);
  rec = verwerk(rec, "abc", { uitslag: "storing" }, NU + 2 * DAG); // storing daarna maakt het niet weer Pro
  assert.ok(!isPro(rec, NU + 2 * DAG));
});

test("nieuwe sleutel met storing is geen Pro en zegt: probeer opnieuw", () => {
  const rec = verwerk(null, "abc", { uitslag: "storing" }, NU);
  assert.ok(!isPro(rec, NU));
  assert.equal(melding(rec, NU), MELDINGEN.storing_nieuw);
});

test("andere sleutel invoeren begint opnieuw", () => {
  let rec = verwerk(null, "abc", { uitslag: "goed", productId: P1 }, NU);
  rec = verwerk(rec, "def", { uitslag: "storing" }, NU + DAG);
  assert.ok(!isPro(rec, NU + DAG));
});

test("achtergrondcontrole hooguit één keer per dag, na storing elk uur", () => {
  let rec = verwerk(null, "abc", { uitslag: "goed", productId: P1 }, NU);
  assert.ok(!moetControleren(rec, NU + DAG - 1));
  assert.ok(moetControleren(rec, NU + DAG));
  rec = verwerk(rec, "abc", { uitslag: "storing" }, NU + DAG);
  assert.ok(!moetControleren(rec, NU + DAG + 59 * 60 * 1000));
  assert.ok(moetControleren(rec, NU + DAG + 60 * 60 * 1000));
  assert.ok(!moetControleren(null, NU));
});
