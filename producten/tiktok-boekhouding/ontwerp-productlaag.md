# Ontwerp: de product-laag, één afrekening van begin tot eind (bouwstuk van Jet)

**Status: concept, controleur ronde 1 nee (9 nov 20:30 UTC). Niet bouwen voordat de punten onderaan verwerkt zijn en de controleur akkoord geeft.**

Jet, 9 nov 2026, 20:25 UTC. Verbindt de basis (`producten/tiktok-shop-basis/`: endpoints en rekenkern) met de Moneybird-kant (`ontwerp-moneybird.md`). Geen schermen: die volgen na het ontwerp van Daan. Bronnen: docs get-transactions-by-statement-202501 (GEZIEN 9 nov met curl via de docs-API), de basis en de Moneybird-kant.

## Wat het doet
Eén functie `verwerkAfrekening(deps, afrekening, instellingen)` in `src/verwerk.ts`, plus een functie die alle afrekeningen van een winkel langsloopt. `deps` bevat de TikTok-client met token en `shop_cipher`, de Moneybird-client, een **opslag** (eigen interface, zie onder) en `nu()`. Stappen voor één afrekening:
1. **Overslaan** (status, geen enkele aanroep): `statement_time` ligt vóór de startdatum (eis e, datum in Nederlandse tijd); `payment_status` is niet `PAID` (pas boeken als het geld onderweg is; `PROCESSING` komt later vanzelf terug, `FAILED` krijgt status `uitbetaling_mislukt`); al `geboekt` met dezelfde invoer-vingerafdruk; status `onzeker` van minder dan 10 minuten geleden.
2. **Slot:** `opslag.metSlot(statementId, fn)`. Is het slot bezet (automatische run tegen "opnieuw boeken"), dan status `bezig` en niets doen. Het slot verloopt na 5 minuten, zodat een afgebroken run niets blijvend blokkeert.
3. **Ophalen:** `transactiesVanAfrekening`. Per transactie:
   - `ORDER` met `order_id`: `transactiesVanBestelling` en `boekingsregels` (rekenkern), en daarvan alleen de regels met dit `statementId`. Daarna een controle per bestelling: som van die regels tegen het `settlement_amount` van de transactie in de afrekening. Wijkt het af (bijvoorbeeld door `adjustment_amount` op een bestelling, wat de docs niet uitleggen), dan het verschil als regel `correctie` met een waarschuwing per bestelling. Zo boekt de app per transactie precies wat TikTok uitbetaalt.
   - Alle andere soorten (`CHARGE_BACK`, `PLATFORM_PENALTY`, `SHIPPING_FEE_ADJUSTMENT` en de rest van de lijst in de docs, ook onbekende nieuwe): één regel `correctie` met het `settlement_amount` van de transactie, omschrijving met het soort. `RESERVE` (reservering, volgens de docs alleen VK en VS) hoort niet in een NL-winkel; komt hij toch, dan als `correctie` met een waarschuwing.
   - Bestellingen ophalen gaat **in porties**: per aanroep van de functie hoogstens `maxBestellingen` (standaard 40), de uitkomst per bestelling gaat in de opslag. Is de afrekening nog niet compleet, dan status `bezig_met_ophalen` en de volgende run gaat verder. Waarom: Cloudflare Workers op het gratis plan staan maar een beperkt aantal uitgaande verzoeken per aanroep toe (50 volgens hun docs, GOK tot nagekeken bij het kiezen van de opslag), en een afrekening kan honderden bestellingen hebben.
4. **Proef of boeken:** in de proef (eis a) alleen `maakMemoriaal` en het resultaat teruggeven, nooit `boekAfrekening`, niets naar Moneybird. Bij boeken: staat `magBoeken` uit (boven de gratis grens, eis f), dan status `wacht_op_abonnement` met de proef-uitkomst bewaard; anders `boekAfrekening` met `bekendId` uit de opslag, `uitbetaaldCenten` = `settlement_amount` van de afrekening.
5. **Bewaren:** status (`geboekt`, `geboekt_met_waarschuwing`, `onzeker`, `fout`, `leeg`), document-id, waarschuwingen, tijdstip en de vingerafdruk van de invoer (hash van de regels plus koppeling), zodat "opnieuw boeken" na een gewijzigde instelling wel gaat en een gewone run niet onnodig Moneybird aanroept.

**Fouten:** `koppeling_verlopen` (Moneybird 401 na één keer verversen) of TikTok `token_verlopen` na verversen: status `koppeling_verlopen` voor de winkel, de run stopt, niets gaat verloren (eis g): de volgende run neemt alle afrekeningen vanaf de startdatum die nog niet `geboekt` zijn. `te_veel_verzoeken` na de herhalingen van de clients: run stopt, volgende run gaat verder. `periode_afgesloten`, `dubbel`, `geweigerd`: status `fout` met de melding in gewone woorden, de rest van de afrekeningen gaat door.

**Opslag** is een interface (`metSlot`, `leesStatus`, `schrijfStatus`, `leesBestelling`, `schrijfBestelling`), getest met een versie in het geheugen. Welke Cloudflare-opslag (D1 of KV) komt bij de volgende stap, als ook de limieten nagekeken zijn.

## Wat het bewust niet doet
Geen schermen, geen gratis-grens tellen (de product-laag krijgt `magBoeken` binnen; Chris bepaalt de grens), geen tokens bewaren of verversen (de aanroeper doet dat, zoals in de basis), geen andere munt dan EUR, geen omrekening van reserveringen.

## Af als (toetsbaar, met nagebootste TikTok- en Moneybird-antwoorden)
- (a) Proef: drie afrekeningen geven drie memorialen en nul verzoeken naar Moneybird.
- (b) Afrekening vóór de startdatum of niet `PAID`: geen enkel verzoek, juiste status.
- (c) Een afrekening met twee bestellingen en een `PLATFORM_PENALTY`: regels van de rekenkern (alleen dit `statementId`), plus één `correctie` voor de boete; som gelijk aan `settlement_amount`, geen waarschuwing. Een bestelling waarvan de som afwijkt van haar transactie geeft een `correctie` met waarschuwing.
- (d) Slot bezet: status `bezig`, geen verzoek. Status `onzeker` van 5 minuten geleden: overslaan; van 11 minuten: opnieuw (via `bekendId` of kenmerk).
- (e) Porties: 90 bestellingen met `maxBestellingen` 40 geven na twee runs `bezig_met_ophalen` en na de derde een boeking; geen bestelling wordt twee keer opgehaald.
- (f) `magBoeken` uit: `wacht_op_abonnement`, geen schrijfactie; daarna aan: geboekt.
- (g) Moneybird 401: status `koppeling_verlopen`, de run stopt, de volgende run boekt de overgebleven afrekeningen zonder gat.
- (h) Tweede run zonder wijziging: geen verzoek naar Moneybird (vingerafdruk gelijk); na een gewijzigde koppeling wel.

## Controleur ronde 1 (9 nov 20:30 UTC): nee. Open punten voor de volgende run
Moet:
1. Proef kan niet via `maakMemoriaal` (die eist rekeningen, die pas in stap 4 komen): proef geeft regels per soort zonder koppeling, en slaat startdatum, `magBoeken` en porties over.
2. `payment_status` kent ook `SETTLED` (get-statements-202309): per waarde vastleggen (PAID, SETTLED, PROCESSING, FAILED, onbekend); `uitbetaling_mislukt` is niet definitief.
3. Zelfde bestelling kan twee keer in één afrekening staan (verkoop en terugbetaling op één dag): elke bestelling één keer ophalen, regels één keer, vergelijken met de som van alle ORDER-transacties van die bestelling.
4. Verschil per bestelling niet zomaar op `correctie`: `adjustment_amount` op de ORDER-transactie wordt `correctie`, wat overblijft `verschil` (tussenrekening) met waarschuwing; afwijking van de rekenkern (kop-verschil) uitdrukkelijk vastleggen.
5. Veld en teken van aanpassingen zijn tegenstrijdig in de docs (GOK markeren); leeg `settlement_amount` is onbekend, terugval op `adjustment_amount` of `reserve_amount`; controle som transacties tegen `total_settlement_amount`; RESERVE telt niet in settlement (`payable_amount` = settlement + reserve).
6. Aantal transacties gelijk aan `total_count`, anders niet boeken.
7. Eén tabel met alle statussen, wat een run ermee doet en hoe je eruit komt, inclusief 402/403 (winkel stil), alle foutsoorten, TikTok-fouten anders dan token, een mislukte bestelling midden in een portie, en of `fout` elke run opnieuw gaat (nee bij `periode_afgesloten` en `geweigerd`: knop "opnieuw proberen").
8. Gewone run boekt `geboekt` nooit opnieuw; vingerafdruk alleen bij "opnieuw boeken" en "opnieuw proberen".
9. Cloudflare gratis plan: 50 subrequests per aanroep (nagekeken), KV en D1 apart 1000: teller over de hele aanroep met reserve voor de boeking.
10. Slot in D1 of een Durable Object (KV is niet consistent); bij bezet slot niets schrijven; vastleggen wat er gebeurt na 5 minuten.
11. Toetsen voor al het bovenstaande.
Kan: vingerafdruk met administratie, datum, uitbetaald en codeversie; `payable_amount` als uitbetaald; "vanaf hier"-markering; `adjustment_id` in de omschrijving; "opnieuw boeken" haalt opnieuw op; wat er met bewaarde bestellingen gebeurt na boeken.
