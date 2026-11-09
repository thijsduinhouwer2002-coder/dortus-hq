# Architectuur: TikTok Shop naar Moneybird

Kort overzicht van de onderdelen en hoe ze samenhangen. Ontwerpen: `ontwerp.md`, `ontwerp-moneybird.md`, `ontwerp-productlaag.md`, `ontwerp-d1-worker.md`.

## Onderdelen
- `src/budget.ts`: één teller per aanroep (`Budget`) voor fetch én D1 (één pot van 50, reserve 6 voor afmaken). `omhul` telt fetch, `opslagTeller` telt D1-queries in dezelfde pot. `BudgetOp` betekent: niets verstuurd.
- `src/ophalen.ts`: een afrekening ophalen bij TikTok (transacties, daarna elke ontbrekende bestelling één keer) en samenstellen; ook de proef (eis a). Gooit `WinkelStop`.
- `src/samenstel.ts`: transacties en bestellingen naar regels per soort, met controles.
- `src/verwerk.ts`: de boekrun (`verwerkWinkel`), de statustabel per afrekening, slot, "boeking gestart", de knoppen (`opnieuw`, `vervroegStartdatum`). Exporteert ook alles uit `ophalen.ts`.
- `src/moneybird/`: Moneybird-client, memoriaalboeking maken, `boekAfrekening` (zoeken op kenmerk of `bekendId`, dan POST of PATCH), OAuth en RGS.
- `src/opslag.ts`: interface `Opslag`, `GeheugenOpslag` voor toetsen, fout `Ontkoppeld`.
- `src/d1/opslag.ts` en `src/d1/schema.sql`: de echte opslag in Cloudflare D1. Lezen per afrekening in één batch, schrijven in een wachtrij die meegaat met de volgende statuswissel, slot altijd vers. Triggers weigeren schrijven na ontkoppelen.
- Basis voor TikTok (client, endpoints, fouten) staat in `../tiktok-shop-basis/`.

## Samenhang van één aanroep
1. De Worker (nog niet gebouwd) maakt één `Budget(50)`, de clients met `budget.omhul(fetch)` en een `D1Opslag` met `budget.opslagTeller()`.
2. `verwerkWinkel` leest markering en open lijst, loopt de afrekeningen langs. Per afrekening: status lezen, slot nemen, status opnieuw lezen, `haalSamen`.
3. Compleet: vingerafdruk, dan `startBoeking` (status `onzeker` "boeking gestart" in dezelfde batch als de slotcontrole), dan `boekAfrekening`, dan de echte status. Budget op of winkelstop van Moneybird: oude status terug.
4. Stopt de aanroep tussen POST en status, dan blijft "boeking gestart" staan: 10 minuten wachten, dan zoekt `boekAfrekening` op kenmerk en vindt het document.
5. Na ontkoppelen geeft D1 de fout `ontkoppeld`; `D1Opslag` maakt daar `Ontkoppeld` van en `verwerkWinkel` stopt netjes met winkelfout `ontkoppeld`.
6. Aan het eind `klaar()`: de rest van de wachtrij naar D1.

## Toetsen
`npm test` (Node 22, type stripping, geen afhankelijkheden). D1 wordt nagebootst op `node:sqlite` met dezelfde SQL (`test/d1-nep.ts`). `test/boekrun-d1.test.ts` en `test/verwerk-d1.test.ts` draaien de bestaande verwerk-toetsen nog eens met `D1Opslag`.

## Nog niet gebouwd
Tokens (`src/d1/tokens.ts`), de Worker (`src/worker.ts`), `ontkoppel` en wissen, opruimen per cron, webhook.
