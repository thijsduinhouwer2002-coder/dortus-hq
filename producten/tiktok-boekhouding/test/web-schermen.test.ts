// HTML van scherm 1 en de staten (ontwerp-schermen.md versie 3): teksten uit de schets, rechten en Exact-link (p),
// escapen (l), geen belofte "vanzelf opnieuw" (e), uitgelogd zonder winkelgegevens (k), mailto zonder formulier.
import { test } from "node:test";
import assert from "node:assert/strict";
import { pagina } from "../src/web/html.ts";
import {
  evenGeduld, foutBijKoppelen, gekoppeld, kiesAdministratie, kiesWinkel, koppelScherm, landNaam, nietVoorJou, openAls, uitgelogd,
  weigeringTikTok, type Scherm,
} from "../src/web/schermen.ts";

const tekstVan = (s: Scherm) => pagina(s).text();
const BOOS = `<script>x</script>"'`;

test("(p) scherm 1: schets-teksten, Moneybird-knop als POST met csrf, rechten, Exact-link", async () => {
  const t = await tekstVan(koppelScherm({ winkelnaam: "Studio Lente", csrf: "CSRF123" }));
  const m = await tekstVan(koppelScherm({ winkelnaam: "A", csrf: "c", melding: "Je gaf Moneybird geen toestemming." }));
  assert.ok(m.includes(`<p class="melding" role="status">Je gaf Moneybird geen toestemming.</p>`));
  for (const zin of ["Stap 1 van 3", "Koppel je boekhouding", "Er gaat nog niets naar Moneybird.", "Studio Lente · gekoppeld", "Koppel Moneybird"]) {
    assert.ok(t.includes(zin), zin);
  }
  assert.match(t, /<form method="post" action="\/app\/moneybird\/start"><input type="hidden" name="csrf" value="CSRF123">/);
  assert.ok(t.includes("boekingen te maken en je grootboekrekeningen te lezen en aan te maken"));
  assert.ok(t.includes(`<a href="/app/niet-voor-jou?voor=exact">Zet je op de wachtlijst voor Exact</a>`));
  assert.ok(!/fout/i.test(t));
});

test("(l) winkelnaam, melding, keuzes en csrf worden ge-escaped", async () => {
  const delen = [
    await tekstVan(koppelScherm({ winkelnaam: BOOS, csrf: BOOS, melding: BOOS })),
    await tekstVan(openAls(BOOS)),
    await tekstVan(gekoppeld(BOOS)),
    await tekstVan(kiesWinkel([{ id: BOOS, naam: BOOS }], BOOS)),
    await tekstVan(kiesAdministratie([{ id: BOOS, naam: BOOS }], BOOS)),
  ];
  for (const t of delen) {
    assert.ok(!t.includes("<script>x"), "geen script");
    assert.ok(t.includes("&lt;script&gt;x&lt;/script&gt;&quot;&#39;"));
  }
});

test("keuzeschermen: POST naar de juiste route, eerste keuze aangevinkt, csrf erin", async () => {
  const w = await tekstVan(kiesWinkel([{ id: "1", naam: "A" }, { id: "2", naam: "B" }], "C1"));
  assert.ok(w.includes(`action="/app/tiktok/kies"`) && w.includes(`value="C1"`));
  assert.equal((w.match(/ checked/g) ?? []).length, 1);
  assert.ok(w.includes(`value="2"> B`));
  assert.ok(w.includes("<legend>Welke winkel koppel je?</legend>"));
  assert.throws(() => kiesWinkel([], "c"));
  assert.throws(() => kiesAdministratie([], "c"));
  const a = await tekstVan(kiesAdministratie([{ id: "9", naam: "Studio Lente B.V." }], "C2"));
  assert.ok(a.includes(`action="/app/moneybird/administratie"`) && a.includes(`name="administratie" value="9"`));
});

test("nog niet voor jou: land in gewone woorden, mailto met gecodeerd onderwerp, geen formulier", async () => {
  const t = await tekstVan(nietVoorJou({ soort: "land", land: "de" }));
  assert.ok(t.includes("Nu alleen voor Nederlandse winkels"));
  assert.ok(t.includes("Je winkel staat in Duitsland."));
  assert.ok(t.includes(`href="mailto:thijs@dortus.com?subject=Wachtlijst%20Klopt%3A%20Duitsland"`));
  assert.ok(t.includes("Mail ons, dan hoor je het als Klopt voor jou werkt."));
  assert.ok(!/<form|<input|e-mail achter/i.test(t));
  assert.equal(landNaam("xx"), "XX");
  const boos = await tekstVan(nietVoorJou({ soort: "land", land: `<b>"x` }));
  assert.ok(!boos.includes("<b>") && boos.includes("&lt;B&gt;&quot;X"));
  const mailto = boos.match(/href="(mailto:[^"]*)"/)![1];
  assert.match(mailto, /^mailto:thijs@dortus\.com\?subject=[A-Za-z0-9%._~-]+$/, "alleen gecodeerde tekens");
  assert.ok((await tekstVan(nietVoorJou({ soort: "exact" }))).includes("Wachtlijst%20Klopt%3A%20Exact"));
  assert.ok((await tekstVan(nietVoorJou({ soort: "geen_administratie" }))).includes("geen Moneybird-administratie"));
  assert.ok((await tekstVan(nietVoorJou({ soort: "geen_nl_administratie" }))).includes("Geen Nederlandse administratie in euro"));
});

test("(e) foutstaat: niet aan jou, geen belofte dat we het vanzelf opnieuw proberen", async () => {
  for (const kant of ["TikTok", "Moneybird"] as const) {
    const s = foutBijKoppelen(kant, "andere_kant");
    assert.equal(s.status, 502);
    const t = await tekstVan(s);
    assert.ok(t.includes(`${kant} gaf geen antwoord`) && t.includes("Dat ligt niet aan jou."));
    assert.ok(!/vanzelf|over 5 minuten/i.test(t));
    const anders = await tekstVan(foutBijKoppelen(kant, "anders"));
    assert.ok(anders.includes(`Koppelen met ${kant} lukte niet`) && !anders.includes("ligt niet aan jou"));
  }
  // TikTok opnieuw via de inlog van TikTok, Moneybird via scherm 1 (daar staat de POST-knop met csrf).
  assert.ok((await tekstVan(foutBijKoppelen("TikTok", "anders"))).includes(`href="/app/tiktok/start">Opnieuw koppelen`));
  const mb = await tekstVan(foutBijKoppelen("Moneybird", "anders"));
  assert.ok(mb.includes(`href="/app">Opnieuw koppelen`) && !mb.includes("/app/tiktok/start"));
  assert.ok((await tekstVan(weigeringTikTok())).includes("Je gaf TikTok Shop geen toestemming"));
});

test("(k)-deel uitgelogd en even geduld: geen winkelgegevens, juiste status, knop", async () => {
  const u = uitgelogd();
  assert.equal(pagina(u).status, 200);
  const t = await tekstVan(u);
  assert.ok(t.includes("Open Klopt vanuit TikTok Shop") && t.includes(`href="/app/tiktok/start"`));
  assert.ok(!/gekoppeld|Moneybird/.test(t));
  const g = evenGeduld();
  assert.equal(g.status, 503);
  assert.equal(pagina(g).headers.get("retry-after"), "60");
  assert.ok((await tekstVan(g)).includes(`href="/app">Vernieuwen`));
});

test("alle schermen: geen inline stijl of script, geen uitroeptekens in de tekst", async () => {
  const alle = [
    koppelScherm({ winkelnaam: "A", csrf: "c" }), nietVoorJou({ soort: "land", land: "IT" }), foutBijKoppelen("TikTok", "andere_kant"), foutBijKoppelen("Moneybird", "anders"), weigeringTikTok(),
    uitgelogd(), openAls("A"), evenGeduld(), kiesWinkel([{ id: "1", naam: "A" }], "c"), kiesAdministratie([{ id: "1", naam: "A" }], "c"), gekoppeld("A"),
  ];
  for (const s of alle) {
    const t = await tekstVan(s);
    assert.ok(!/<style|style=|<script|onclick=/i.test(t), s.titel);
    const zichtbaar = t.replace(/<!doctype html>/i, "").replace(/<div class="teken" aria-hidden="true">!<\/div>/g, "");
    assert.ok(!zichtbaar.includes("!"), `uitroepteken in ${s.titel}`);
  }
});
