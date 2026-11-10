// Abonnement van een winkel bij Polar (ontwerp-betalen.md, punt 1 en 3): de keuze uit Customer State en het schrijven
// naar `winkels.abonnement`. Gedeeld door de webhook (src/polar/webhook.ts) en de opvraging (`standVan` in client.ts).
//
// Vormen uit de OpenAPI van Polar (https://polar.sh/docs/openapi/2026-10.openapi.json, gelezen met curl op 10 nov 2026):
//   CustomerState = CustomerStateIndividual | CustomerStateTeam: `id`, `external_id` (tekst of null), `deleted_at`
//     (date-time of null), `active_subscriptions` (lijst van CustomerStateSubscription).
//   CustomerStateSubscription: `id`, `metadata` (MetadataOutputType: tekst, geheel getal, getal of boolean),
//     `status` ("active" | "trialing"), `current_period_end` (date-time, verplicht), `cancel_at_period_end` (boolean),
//     `started_at` en `created_at` (date-time).
//   Alle tijden zijn tekst als "2026-01-01T00:00:00.000000Z", geen unix-seconden.
//
// Vorm van `winkels.abonnement` (JSON):
//   { actief, tot, id, opgezegd, stand, betalingMislukt, vlagStand }
//   actief, tot (unix-seconden), id, opgezegd en stand komen uit Customer State (webhook `customer.state_changed` of onze
//   opvraging); betalingMislukt en vlagStand komen uit de events `subscription.*`.
//   `stand` en `vlagStand` zijn tijden in MICROseconden sinds 1970: het veld `timestamp` uit de body van de webhook heeft
//   zes cijfers achter de komma, en twee events in dezelfde milliseconde mogen elkaar niet wegdrukken. Een opvraging
//   gebruikt `nu * 1_000_000`.
//
// Twee standen, niet één (keuze bij het bouwen, ontwerp zei één `stand`): Polar stuurt bij één verandering vaak zowel
// `subscription.past_due` als `customer.state_changed`, in willekeurige volgorde en met tijden dicht bij elkaar. Met één
// stand zou een past_due die net iets ouder is dan de laatste state_changed genegeerd worden (vlag nooit gezet), en een
// state_changed na een iets nieuwere past_due ook (actief/tot blijven oud). Elke soort vergelijkt daarom alleen met zijn
// eigen stand en schrijft alleen zijn eigen velden (json_set op losse velden, in één UPDATE met de voorwaarde erin), zodat
// een state_changed de vlag nooit wist en een past_due `actief`/`tot` nooit raakt. "Stand ouder dan 3 dagen" (twijfel,
// punt 2.5) kijkt naar `stand`.
import type { D1, D1Statement } from "../d1/opslag.ts";

/** Wat uit Customer State komt (zonder de vlag). */
export interface StandUitPolar {
  actief: boolean;
  /** `current_period_end` in unix-seconden; null als er geen abonnement gekozen is. */
  tot: number | null;
  id: string | null;
  opgezegd: boolean;
  /** Microseconden (zie boven). */
  stand: number;
}

/** De hele kolom `winkels.abonnement`. */
export interface Abonnement extends Partial<StandUitPolar> {
  betalingMislukt?: boolean;
  vlagStand?: number;
}

/** Het deel van CustomerStateSubscription dat we lezen. */
export interface PolarAbonnement {
  id: string;
  metadata?: Record<string, unknown> | null;
  status?: string;
  current_period_end: string;
  cancel_at_period_end?: boolean;
  started_at?: string | null;
  created_at?: string;
}

/** Het deel van CustomerState dat we lezen. */
export interface PolarKlantStand {
  id: string;
  external_id?: string | null;
  deleted_at?: string | null;
  active_subscriptions?: PolarAbonnement[];
}

const ISO = /^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(?:\.(\d{1,9}))?(Z|[+-]\d{2}:\d{2})$/;

/** ISO-tijd van Polar naar microseconden; null als de tekst geen geldige tijd is. */
export function microVan(tijd: unknown): number | null {
  if (typeof tijd !== "string") return null;
  const m = ISO.exec(tijd);
  if (!m) return null;
  const ms = Date.parse(m[1] + m[3]);
  if (!Number.isFinite(ms)) return null;
  const micro = Number((m[2] ?? "").padEnd(6, "0").slice(0, 6));
  return ms * 1000 + micro;
}

/** ISO-tijd naar unix-seconden (afgerond naar beneden); null als ongeldig. */
export function secondenVan(tijd: unknown): number | null {
  const u = microVan(tijd);
  return u === null ? null : Math.floor(u / 1_000_000);
}

const winkelVan = (a: PolarAbonnement): string | undefined => {
  const w = a.metadata?.winkel;
  return w === undefined || w === null ? undefined : String(w);
};

const verste = (lijst: PolarAbonnement[]) =>
  lijst.reduce<PolarAbonnement | undefined>((best, a) => (best && (secondenVan(best.current_period_end) ?? 0) >= (secondenVan(a.current_period_end) ?? 0) ? best : a), undefined);

/**
 * Het abonnement van deze winkel (punt 3): eerst één met `metadata.winkel` gelijk aan de sleutel; staat er geen enkel
 * abonnement met `metadata.winkel`, dan het enige actieve (oude checkout zonder metadata), en bij meerdere zonder het met
 * de verste `current_period_end`. Hebben er wel een paar `metadata.winkel` maar geen voor deze winkel: geen (die zijn van
 * een andere winkel). Bij meerdere met dezelfde sleutel ook de verste.
 */
export function kiesAbonnement(lijst: PolarAbonnement[] | undefined | null, winkel: string): PolarAbonnement | undefined {
  const alle = Array.isArray(lijst) ? lijst.filter((a) => a && typeof a.id === "string") : [];
  const vanOns = alle.filter((a) => winkelVan(a) === winkel);
  if (vanOns.length) return verste(vanOns);
  if (alle.some((a) => winkelVan(a) !== undefined)) return undefined;
  return verste(alle);
}

/** Customer State naar wat we bewaren. `stand` in microseconden. Geen klant (404) of verwijderd: niet actief. */
export function standUitState(state: PolarKlantStand | null, winkel: string, stand: number): StandUitPolar {
  const leeg: StandUitPolar = { actief: false, tot: null, id: null, opgezegd: false, stand };
  if (!state || state.deleted_at) return leeg;
  const a = kiesAbonnement(state.active_subscriptions, winkel);
  const tot = a ? secondenVan(a.current_period_end) : null;
  if (!a || tot === null) return leeg;
  return { actief: true, tot, id: a.id, opgezegd: a.cancel_at_period_end === true, stand };
}

const jsonBool = (b: boolean) => (b ? "true" : "false");
// Getallen als INTEGER: een JS-getal wordt anders als REAL gebonden en komt als 1800000000.0 in de JSON.
const huidigeStand = (veld: string) => `coalesce(json_extract(abonnement, '$.${veld}'), -1)`;

/**
 * Stand uit Customer State schrijven: alleen als hij nieuwer is dan `stand` en de winkel gekoppeld is (voorwaarde in de
 * UPDATE zelf, dus ook bij twee aanroepen tegelijk wint de nieuwste). Raakt `betalingMislukt` en `vlagStand` niet.
 * `klant` (Polar customer id) alleen als hij bekend is.
 */
export function schrijfStand(db: D1, winkel: string, s: StandUitPolar, klant?: string | null): D1Statement {
  return db
    .prepare(
      `UPDATE winkels SET polar_klant = coalesce(?, polar_klant),
       abonnement = json_set(coalesce(abonnement, '{}'), '$.actief', json(?), '$.tot', CAST(? AS INTEGER), '$.id', ?, '$.opgezegd', json(?),
         '$.stand', CAST(? AS INTEGER))
       WHERE id = ? AND ontkoppeld_op IS NULL AND ${huidigeStand("stand")} < CAST(? AS INTEGER)`,
    )
    .bind(klant ?? null, jsonBool(s.actief), s.tot, s.id, jsonBool(s.opgezegd), s.stand, winkel, s.stand);
}

/** Vlag `betalingMislukt` schrijven, met een eigen stand (`vlagStand`). Raakt de velden uit Customer State niet. */
export function schrijfVlag(db: D1, winkel: string, betalingMislukt: boolean, stand: number): D1Statement {
  return db
    .prepare(
      `UPDATE winkels SET abonnement = json_set(coalesce(abonnement, '{}'), '$.betalingMislukt', json(?), '$.vlagStand', CAST(? AS INTEGER))
       WHERE id = ? AND ontkoppeld_op IS NULL AND ${huidigeStand("vlagStand")} < CAST(? AS INTEGER)`,
    )
    .bind(jsonBool(betalingMislukt), stand, winkel, stand);
}
