# Architectuur: TikTok Shop naar Moneybird

Kort overzicht van de onderdelen en hoe ze samenhangen. Ontwerpen: `ontwerp.md`, `ontwerp-moneybird.md`, `ontwerp-productlaag.md`, `ontwerp-d1-worker.md`, `ontwerp-affiliate.md`.

## Onderdelen
- `src/budget.ts`: één teller per aanroep (`Budget`) voor fetch én D1 (één pot van 50, reserve 6 voor afmaken). `omhul` telt fetch, `opslagTeller` telt D1-queries in dezelfde pot. `BudgetOp` betekent: niets verstuurd.
- `src/ophalen.ts`: een afrekening ophalen bij TikTok (transacties, daarna elke ontbrekende bestelling één keer) en samenstellen; ook de proef (eis a). Gooit `WinkelStop`.
- `src/samenstel.ts`: transacties en bestellingen naar regels per soort, met controles.
- `src/verwerk.ts`: de boekrun (`verwerkWinkel`), de statustabel per afrekening, slot, "boeking gestart", de knoppen (`opnieuw`, `vervroegStartdatum`). Exporteert ook alles uit `ophalen.ts`.
- `src/moneybird/`: Moneybird-client, memoriaalboeking maken, `boekAfrekening` (zoeken op kenmerk of `bekendId`, dan POST of PATCH), OAuth en RGS. Soort `affiliate` zonder eigen rekening valt in `maakMemoriaal` terug op de rekening van `commissie` (zonder btw-tarief).
- `src/opslag.ts`: interface `Opslag`, `GeheugenOpslag` voor toetsen, fout `Ontkoppeld`.
- `src/d1/opslag.ts` en `src/d1/schema.sql`: de echte opslag in Cloudflare D1. Lezen per afrekening in één batch, schrijven in een wachtrij die meegaat met de volgende statuswissel, slot altijd vers. Triggers weigeren schrijven na ontkoppelen.
- `src/d1/tokens.ts`: tokens van TikTok (`tt_tokens`) en Moneybird (`mb_tokens`) per soort met `TokenBron`: AES-GCM met winkel-id als AAD en sleutelversie in de tekst, verversen binnen een uur, voorwaardelijk opslaan op `tt_versie`/`mb_versie`, na een 401 één keer verversen (`met`), dan `WinkelStop` `koppeling_verlopen`; alles in het ene budget.
- `src/d1/ontkoppel.ts`: `ontkoppel` (punt 7). Eén batch zet `ontkoppeld_op`, maakt alles in `winkels` leeg behalve de kale rij (id, `ontkoppeld_op`, `taken`, en bij een open taak `mb_tokens`/`polar_klant`) en wist de rijen in `statussen`, `transacties`, `bestellingen` en `sloten`. Daarna Moneybird intrekken (`trekIn`, refresh token via `ontsleutel` uit `tokens.ts`): 200 token weg, 403 `ALARM` en token weg, anders later opnieuw. Hoogstens 3 uit het budget. Ook `ontkoppelOpShopId` voor de webhook. Bovenin staat de vorm van `taken`.
- `src/d1/opruimen.ts`: `ruimOntkoppeldOp` voor de cron: intrekken opnieuw (hoogstens 5, na 7 dagen token weg en `ALARM`), wissen herhalen als vangnet (hoogstens 20 winkels, één batch), kale rij weg als beide taken klaar zijn of op dag 23 (behalve als `opzeggen` nog openstaat: dan blijft de rij met elke dag een `ALARM`), en winkels die 21 dagen onafgebroken `koppeling_verlopen` aan de kant van TikTok hebben ontkoppelen (hoogstens 3).
- `src/d1/winkels.ts`: `winkelsAanDeBeurt` (cron-query, alleen gekoppelde winkels, gedeeltelijke index) en `winkelfoutStatement` (winkelfout als JSON `{soort, bericht, kant}` met `winkelfout_sinds`, voor de slotbatch van de consumer).
- `src/worker.ts`: de Worker. `cron(o, nu)`: `winkelsAanDeBeurt` (hoogstens 100), één `sendBatch`, dan in één batch `volgende_run = nu + 30 min` (lease), dan `ruimOntkoppeldOp`; eigen `Budget(50)`, de wachtrij telt als één verzoek. `consumer(bericht, o, nu)`: winkelslot (`sloten`, `__winkel`, 15 min, via `D1Opslag.neemSlot`), bezet of ontkoppeld is niets doen; dan tokens via `TokenBron` (alleen onder het slot), `verwerkWinkel`, en in één slotbatch via `klaar(extra)`: winkelfout met kant, `volgende_run` (6 uur, of 15 minuten bij `bezig_met_ophalen` of budget op, hoogstens 8 keer achter elkaar via `snel_teller`) en het winkelslot terug. Kant van de winkelfout: eerst de soort (alleen TikTok, alleen Moneybird, of van ons), bij `server` en `te_veel_verzoeken` de kant van het laatste uitgaande verzoek. Gooit nooit; `export default { scheduled, queue }` bevestigt elk bericht. Env-velden: `DB`, `WACHTRIJ`, `TOKEN_SLEUTELS` (JSON versie naar 32 bytes base64), `TOKEN_SLEUTEL_HUIDIG`, `TIKTOK_APP_KEY`, `TIKTOK_APP_SECRET`, `MONEYBIRD_CLIENT_ID`, `MONEYBIRD_CLIENT_SECRET`, `MONEYBIRD_REDIRECT_URI`. Voorbeeld van de instellingen: `wrangler.voorbeeld.toml`.
- Basis voor TikTok (client, endpoints, fouten) staat in `../tiktok-shop-basis/`.

## Samenhang van één aanroep
1. De consumer in `src/worker.ts` maakt één `Budget(50)` (reserve 6 voor afmaken), de clients met `budget.omhul(fetch)` en een `D1Opslag` met `budget.opslagTeller()`.
2. `verwerkWinkel` leest markering en open lijst, loopt de afrekeningen langs. Per afrekening: status lezen, slot nemen, status opnieuw lezen, `haalSamen`.
3. Compleet: vingerafdruk, dan `startBoeking` (status `onzeker` "boeking gestart" in dezelfde batch als de slotcontrole), dan `boekAfrekening`, dan de echte status. Budget op of winkelstop van Moneybird: oude status terug.
4. Stopt de aanroep tussen POST en status, dan blijft "boeking gestart" staan: 10 minuten wachten, dan zoekt `boekAfrekening` op kenmerk en vindt het document.
5. Na ontkoppelen (knop, webhook of 21 dagen `koppeling_verlopen`) weigeren de triggers elke INSERT en UPDATE en geeft D1 de fout `ontkoppeld`; `D1Opslag` maakt daar `Ontkoppeld` van en `verwerkWinkel` stopt netjes met winkelfout `ontkoppeld`.
6. Aan het eind `klaar()`: de rest van de wachtrij naar D1, met `winkelfoutStatement`, `volgende_run` en het winkelslot terug in dezelfde batch.

## Toetsen
`npm test` (Node 22, type stripping, geen afhankelijkheden). D1 wordt nagebootst op `node:sqlite` met dezelfde SQL (`test/d1-nep.ts`). `test/boekrun-d1.test.ts` en `test/verwerk-d1.test.ts` draaien de bestaande verwerk-toetsen nog eens met `D1Opslag`. `test/ontkoppel.test.ts`, `test/ontkoppel-lopend.test.ts` en `test/opruimen.test.ts` toetsen punt 7 (l, m, n en het cron-deel van o). `test/worker.test.ts` toetst (h) en meet (j).

## Nog niet gebouwd
De knop Ontkoppelen. Echte uitrol van de Worker (alleen `wrangler.voorbeeld.toml`). Na een 401 van TikTok midden in `verwerkWinkel` wordt nog niet ververst en opnieuw geprobeerd (winkelfout `token_verlopen`, kant tiktok; de volgende run ververst als het token binnen een uur verloopt). De webhook type 6 en 7 (handtekening nog niet uit de docs gehaald; `ontkoppelOpShopId` staat klaar). Het betaalstuk dat de taak `opzeggen` uitvoert bij Polar.
