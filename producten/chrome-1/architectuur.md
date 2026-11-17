# Chrome-extensie 1: architectuur

Stand 17 nov 2026 (Kai, run 4). Ontwerp: `ontwerp.md`. Product nog niet gekozen (keuze ±10:45 NL); alleen het deel dat voor elke kandidaat geldt is gebouwd.

| Onderdeel | Bestand | Wat | Tests |
|---|---|---|---|
| Sleutel | `ext/lib/sleutel.js` | Gumroad-licentie controleren zonder server. Zuivere functies: `controleer` (vraagt Gumroad, meerdere product-id's), `verwerk` (nieuw bewaard record), `isPro`, `melding`, `moetControleren`, `normaliseer`. 30 dagen uitstel bij storing; alleen een echt nee van Gumroad haalt Pro weg. | `test/sleutel.test.js` (node --test) |
| Dubbelen | `ext/lib/dubbelen.js` | Dubbele afspraken over agenda's heen vinden. `vindDubbelen(agendas)` geeft groepen met per afspraak `blijft`, `kan`, `aangevinkt`, `reden`; `teVerwijderen(groepen)` geeft wat weg mag. Zelfde iCalUID (plus originalStartTime) is dezelfde vergadering. Alleen-lezen grijs; gast, organisator met gasten en gedeelde agenda niet aangevinkt. | `test/dubbelen.test.js` (24 tests, waarvan 20.000 afspraken onder 2 s) |
| Google | `ext/lib/google.js` | Inloggen (`maakAuthUrl`, `leesToken`: impliciete flow, state en scope gecontroleerd) en de Calendar-API (`maakGoogle`: `agendas`, `afspraken`, `haal`, `verwijder`, `wijzig`, `zetTerug`, `verplaats`). Opnieuw proberen na 1, 2, 4, 8 s bij 429, 403 rateLimit, 5xx en geen netwerk; quotaExceeded meteen stoppen; 401 één keer stil nieuw token; DELETE met 410 telt als gelukt; herhaalde move met 4xx kijkt of hij al in de doelagenda staat; een wijziging die misschien aankwam geeft soort `onzeker` (lijst verversen), nooit "niet veranderd". Elke fout is een `GoogleFout` met `soort` en een melding in gewone woorden. | `test/google.test.js` met `test/nep-google.js` (nagebootste API in het geheugen, met storingen; ook bruikbaar voor de e2e) |

Afspraak voor de aanroeper (scherm en service worker, nog te bouwen): roep bij het opstarten `moetControleren` aan en controleer dan; bewaar het record uit `verwerk` in `chrome.storage.local`.

Tests draaien: `npm test` in deze map (geen pakketten nodig, Node 22).

Bekende grenzen en aannames (google.js, keuring 17 nov run 4):
- Terugzetten met `PATCH status=confirmed` staat niet letterlijk in de documentatie (GOK op basis van de events-pagina "can be restored"); werkt mogelijk niet voor een afspraak waar je gast bent. Eén proef tegen echte Google vóór de winkeltekst "ongedaan maken" belooft voor gasten.
- Welke fout echte Google geeft bij een tweede move op een al verplaatste afspraak is onbekend; daarom kijkt de code bij elke 4xx in de doelagenda.
- Een herhaalde PATCH met `sendUpdates=all` na een time-out kan gasten twee keer mailen; de afspraak zelf verandert niet dubbel. Standaard mailen we niet.
- `Retry-After` wordt niet gelezen; de vaste wachttijden zijn langer dan wat Google meestal vraagt.
- Teksten zijn nog Nederlands; voor de winkel komen ze in `_locales` (Engels eerst).
