# Chrome-extensie 1: architectuur

Stand 17 nov 2026 (Kai, run 3). Ontwerp: `ontwerp.md`. Product nog niet gekozen (keuze ±10:45 NL); alleen het deel dat voor elke kandidaat geldt is gebouwd.

| Onderdeel | Bestand | Wat | Tests |
|---|---|---|---|
| Sleutel | `ext/lib/sleutel.js` | Gumroad-licentie controleren zonder server. Zuivere functies: `controleer` (vraagt Gumroad, meerdere product-id's), `verwerk` (nieuw bewaard record), `isPro`, `melding`, `moetControleren`, `normaliseer`. 30 dagen uitstel bij storing; alleen een echt nee van Gumroad haalt Pro weg. | `test/sleutel.test.js` (node --test) |
| Dubbelen | `ext/lib/dubbelen.js` | Dubbele afspraken over agenda's heen vinden. `vindDubbelen(agendas)` geeft groepen met per afspraak `blijft`, `kan`, `aangevinkt`, `reden`; `teVerwijderen(groepen)` geeft wat weg mag. Zelfde iCalUID (plus originalStartTime) is dezelfde vergadering. Alleen-lezen grijs; gast, organisator met gasten en gedeelde agenda niet aangevinkt. | `test/dubbelen.test.js` (24 tests, waarvan 20.000 afspraken onder 2 s) |

Afspraak voor de aanroeper (scherm en service worker, nog te bouwen): roep bij het opstarten `moetControleren` aan en controleer dan; bewaar het record uit `verwerk` in `chrome.storage.local`.

Tests draaien: `npm test` in deze map (geen pakketten nodig, Node 22).
