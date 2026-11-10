# RGS 3.5-codes per soort (bouwstuk van Jet)

Jet, 9 nov 2026. Waarom: een nieuwe grootboekrekening aanmaken in Moneybird kan alleen met een `rgs_code` uit RGS **versie 3.5** (GEZIEN in de OpenAPI van Moneybird: "Existing RGS version 3.5 code", 422 bij een code die niet bij 3.5 hoort). Met deze lijst kan de app een ontbrekende rekening met één klik aanmaken (stap 4 van Tess). Code: `src/moneybird/rgs.ts`, toets: `test/rgs.test.ts`.

Bron: definitieve RGS 3.5-lijst van referentiegrootboekschema.nl (`Def-versie RGS 3.5_2.xlsx`, blad RGS3.5, 4.745 regels), GEZIEN 9 nov met curl. De gebruikte regels staan in `test/voorbeelden/rgs35-uittreksel.tsv`; de toets controleert dat elke code daar actief en op boekbaar niveau (4 of 5) staat. Let op: RGS is inmiddels bij 3.8 en 3.9 (alfa/bèta), maar Moneybird vraagt 3.5.

Controleur (9 nov 21:20 UTC): akkoord, codes, uittreksel en `account_type` nagekeken tegen de echte lijst en de OpenAPI (voorbelasting staat daar zelf als current_liabilities); 4 kan-punten verwerkt hieronder.

| Soort | RGS 3.5 | Omschrijving in RGS | Soort rekening | Aanmaken |
|---|---|---|---|---|
| omzet, terugbetaling, overig_omzet, omzet_totaal | WOmzNohOlh | 1a. Netto-omzet verkoop handelsgoederen hoog tarief | revenue | ja |
| korting, korting_terug | WOmzKebVekVkh | Verleende kortingen op handelsgoederen | revenue | ja |
| verzendkosten, verzendkosten_totaal | WBedVkkVrk | Vrachtkosten (verkoop) | expenses | ja |
| commissie, kosten_en_belasting_totaal | WBedVkkCom | Commissies (verkoop) | expenses | ja |
| belasting_op_kosten | BSchBepBtwVoo | Voorbelasting | (bestaat al) | **nee** |
| belasting | WBedVkkObs | Overige belastingen inzake verkoopactiviteiten | expenses | ja |
| correctie | WBedVkkOvr | Overige verkoopkosten | expenses | ja |
| verschil | BVorTusTovTvp | Tussenrekening vraagposten | current_assets | ja |
| tegenrekening "Te ontvangen van TikTok Shop" | BVorOvrOvk | Overige vorderingen | current_assets | ja |

## Keuzes en GOK's
- **Omzet hoog tarief (1a).** Past bij de meeste NL-winkels (21%). Wie laag tarief (WOmzNohOlv, 1b) of afstandsverkopen in de EU (WOmzNohOla, 3c) heeft, kiest in het koppelscherm een andere rekening; de app maakt alleen de standaard aan. Deze rubrieken volgen de btw-aangifte, en zolang btw-tarieven uit staan (tot de sandbox-test) boekt de app de omzet zonder btw-splitsing: de accountant moet dat weten. Uitleg in het koppelscherm (vraag voor Daan en Tess).
- **Terugbetaling op omzet.** RGS heeft geen eigen code voor retouren; een terugbetaling verlaagt de netto-omzet. Wie ze apart wil, kiest zelf een rekening.
- **Btw op kosten niet aanmaken.** GOK of TikTok Nederlandse btw rekent (TikTok factureert waarschijnlijk vanuit Ierland, dan verlegd). Btw-rekeningen zijn systeemrekeningen in Moneybird; een tweede "voorbelasting" maakt de aangifte rommelig. De verkoper kiest een bestaande rekening.
- **Correctie als verkoopkosten.** Correcties van TikTok zijn meestal kosten (boetes, chargebacks), soms een vergoeding; één rekening houdt het overzicht simpel.
- **Verschil op vraagposten.** Past bij het ontwerp: tussenrekening, nooit omzet; de accountant ruimt hem op.
- **Verlegde btw op de commissie (10 nov, proef 2 in `ontwerp-moneybird.md`):** Klopt geeft geen btw-tarief mee; een nieuwe administratie heeft geen verlegd tarief en de API kan er geen maken. De verkoper vult 4b en 5b zelf in (zin op het koppelscherm). Bezorgkosten (mogelijk 21% NL-btw via TikTok Logistics Netherlands) blijven GOK tot een echte factuur.
- **Belasting (`fee_tax_breakdown.tax`) als kosten: GOK.** Zijn dit btw-bedragen die TikTok over de verkoop inhoudt of afdraagt, dan horen ze op de balans (btw), niet bij de kosten. Nakijken met echte data (vroege Partner Center-account of sandbox).
- **Eén keer aanmaken, daarna hergebruiken (voor de bouw van stap 4).** Moneybird wil een unieke naam per administratie en soort rekening. Meerdere soorten delen een voorstel (vier op omzet), en bij een tweede winkel of een eerdere poging bestaat de rekening al (POST geeft dan 422). Dus eerst zoeken op naam of RGS-code en alleen aanmaken wat ontbreekt.
- **Vraagposten (BVorTusTovTvp) zit niet in de Basis-set van RGS**, BVorTusTov (niveau 4) wel. Moneybird accepteert waarschijnlijk elke 3.5-code, maar dat is niet gezien: meenemen in de sandbox-test, met BVorTusTov als terugval.
- Niet getest tegen een echte Moneybird-administratie: of twee rekeningen dezelfde RGS-code mogen hebben en of `account_type` bij de code moet passen, staat niet in de docs. Hoort bij de sandbox-test (vijfde vraag erbij).

## Uitslag sandbox-test (GEZIEN 9 nov 22:03 UTC, run 42708208521)
- BVorOvrOvk als current_assets: 201, `taxonomy_item` 3.5 "Overige vorderingen", toegestaan in memoriaal.
- **Twee rekeningen met dezelfde RGS-code mag** (201).
- **BVorTusTovTvp (buiten de Basis-set) mag** (201, "Tussenrekening vraagposten"); de terugval BVorTusTov is dus niet nodig.
- **Moneybird controleert niet of `account_type` bij de code past** (expenses met BVorOvrOvk: 201). Onze app moet dus zelf de juiste soort meesturen bij aanmaken.
- **Zelfde naam en soort twee keer: 422** `{"error":{"name":["has already been taken"]}}`. Bevestigt: eerst zoeken op naam, alleen aanmaken wat ontbreekt.
- Een rekening die al in een boeking stond, zet DELETE alleen op inactief.
