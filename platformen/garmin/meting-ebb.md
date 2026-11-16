# Ebb in de Connect IQ-winkel: meting per dag

Eén regel per dag, steeds op dezelfde manier gemeten. Bron: de API van de winkel (`.../api/asw/apps/5280653d-1681-452d-8c03-7cbdc7284641`, velden `downloadCount`, `reviewCount`, `averageRating`) en de zoekbalk (`.../api/asw/apps/keywords?keywords=<woord>&startPageIndex=0&pageSize=30&sortType=mostRelevant`, eerste 30 resultaten). "geen" betekent: niet in de eerste 30. Verkopen staan niet in de openbare API; die ziet alleen Thijs in zijn account.

| Datum (UTC) | Downloads | Reviews | Cijfer | ebb | breathing | breath hold | breathwork | Opmerking |
|---|---|---|---|---|---|---|---|---|
| 13 nov 22:08 | 0 | 0 | 0 | 1 | geen | 4 | geen | Dag van goedkeuring (±21:09 UTC), run 96 |
| 16 nov 02:03 | 0 | 0 | 0 | 1 | 30 | 4 | geen | Run 104. Op 14 en 15 nov niet gemeten (ik stond uit). "breathing" voor het eerst in de eerste 30 |
| 16 nov 14:58 | 0 | 0 | 0 | 1 | 29 | 4 | 32 | Run 117, nulmeting vóór 1.0.1. Nu de eerste 90 bekeken, daarom een plek voor "breathwork" (stond eerder als "geen", dat was buiten de eerste 30). Versie in de winkel 1.0.0, 40 horloges |

## Nulmeting vóór de update naar 1.0.1 (16 nov 14:58 UTC, run 117)

Zelfde zoekbalk, alle soorten samen (apps, wijzerplaten, velden), eerste 90 resultaten. Joris mat in verhaal 14 alleen de apps; daarom staat "calm" bij hem op 3 en hier op 42. Vergelijk na de update dus met deze getallen, niet met de zijne.

| Woord | Plek van Ebb | Opmerking |
|---|---|---|
| ebb | 1 | |
| breath hold | 4 | |
| breathe | 16 | |
| breath | 19 | |
| breathing | 29 | woord dat in 1.0.1 vooraan in de naam komt |
| breathwork | 32 | |
| calm | 42 | valt in 1.0.1 uit de naam |
| box breathing | 53 | |
| atem | 1 | Duits |
| atem anhalten | 1 | Duits |
| atemübungen | 3 | Duits, valt in 1.0.1 uit de naam |
| atmung | niet in de eerste 90 | Duits, komt in 1.0.1 in de naam |
| adem | 1 | Nederlands |
| adem inhouden | 1 | Nederlands |
| ademhaling | 1 | Nederlands |
| ademhalingsoefeningen | 1 | Nederlands, valt in 1.0.1 uit de naam |

Wat ik hieruit haal: de zoekbalk vindt een woord ook als het begin van een langer woord in de naam ("ademhaling" vindt "Ademhalingsoefeningen", "atem" vindt "Atemübungen"), maar niet een verwant woord ("atmung" vindt "Atemübungen" niet). Hoeveel mensen op welk woord zoeken staat nergens; dat blijft een gok.
