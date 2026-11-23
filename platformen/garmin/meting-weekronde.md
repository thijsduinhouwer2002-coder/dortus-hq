# Garmin: meting per week (maandag)

Nieuwste meting bovenaan. Gemeten door de Garmin-ronde met `curl` op de open winkel-API, zonder inloggen.

- Tellers: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>` (velden `downloadCount`, `reviewCount`, `averageRating`, `appLocalizations`). `downloadCount` is een klasse: 1 = "1+", 10 = "10+". Verkopen staan niet in de openbare API; die ziet alleen Thijs.
- Zoekplekken: `.../api/asw/apps/keywords?keywords=<woord>&startPageIndex=<0,30,60>&pageSize=30&sortType=mostRelevant`, eerste 90, alle soorten samen (zoals de zoekpagina standaard toont), dezelfde methode als `winkel-vindbaar-2026-11-20.md`. "-" is niet in de eerste 90.
- Vorige week = de meting van 20 nov ±10:40 UTC in `winkel-vindbaar-2026-11-20.md` (vóór de nieuwe teksten van 20 nov 12:30).

## 23 nov 2026, ±09:25 UTC (ma)

**Tellers (GEZIEN, winkel-API):**

| App | Downloads | Reviews | Versie | Vorige week (16 nov, scorebord-data.csv) |
|---|---|---|---|---|
| Ebb ($2,99) | 1+ | 0 | 1.0.1 | 0, dus +1 klasse (al 1+ sinds 18 nov) |
| Ebb Calm (gratis) | 10+ | 0 | 1.0.1 | nog niet in de winkel op 16 nov; 10+ sinds 19 nov |
| Gloop's Hat Tower (gratis) | 10+ | 0 | 1.0.0 | 10+ op 19 nov, geen verandering |

Taalvolgorde van Ebb (GEZIEN): `de, nl, en, fr`. Frans staat er sinds 20 nov bij, Duits staat nog vooraan, dus Spaanse, Italiaanse en Poolse bezoekers zien nog de Duitse tekst.

**Zoekplekken (GEZIEN), Ebb / Calm, tussen haakjes 20 nov:**

| Zoekwoord | Treffers | Ebb | Calm |
|---|---|---|---|
| breath hold | 997 | 2 (2) | 72 (71) |
| 478 | 44 | **4 (7)** | 3 (3) |
| breathing | 994 | 19 (18) | 27 (27) |
| breathing exercises | 998 | **13 (21)** | 4 (4) |
| box breathing | 997 | **29 (41)** | **41 (52)** |
| breathwork | 996 | **7 (33)** | 42 (42) |
| breath | 998 | 14 (14) | 61 (61) |
| atem | 993 | 2 (1) | 7 (7) |
| atemübungen | 993 | 5 (4) | 4 (3) |
| atem anhalten | 996 | 2 (1 op 16 nov) | 8 (niet gemeten) |
| ademhaling | 993 | 1 (1) | **3 (-)** |
| ademhalingsoefeningen | 999 | 2 (1) | **1 (-)** |
| adem inhouden | 995 | 1 (niet gemeten) | 2 (niet gemeten) |
| respiration (fr) | 1000 | **12 (-)** | **17 (-)** |
| souffle (fr) | 522 | **2 (-)** | **10 (-)** |
| relaxation | 998 | 58 (-) | 6 (6) |
| calm | 999 | 66 (67) | 5 (33) |
| respiración / respirazione (es / it, alleen eerste 30) | 994 / 990 | - | - |

**Bezoekers dortus.com (GEZIEN, `organisatie/scorebord.md`, Amami):** 16 tot 22 nov samen 116 bezoekers op de hele site; op de Ebb-pagina 0 elke dag.

**Wat werkte:** de nieuwe titels van 20 nov. "Breathwork" in de Duitse en Nederlandse titel: Ebb van 33 naar 7. De Franse titel: Ebb op souffle 2 en respiration 12 (was niet in de eerste 90), Calm 10 en 17. Calm met de Nederlandse titel op ademhalingsoefeningen 1. Box breathing en breathing exercises stegen voor allebei.
**Wat niet:** downloads staan stil (Ebb 1+, Calm 10+ sinds 18 en 19 nov). Hogere zoekplekken gaven deze week nog geen nieuwe downloadklasse. Een Duitse of Nederlandse woordplek zakte één plek (atem, ademhalingsoefeningen), omdat Calm nu op die woorden meedoet. De taalvolgorde van Ebb staat nog verkeerd.
**Verbetering deze week:** de 20 door Daan gekeurde teksten in 10 talen van Chris plakken, eerst Ebb es en it (`winkel-voorstel-2026-11-23.md`). Volgende week ook meten: respiración, respirazione, ejercicios de respiración, esercizi di respirazione, trattenere il fiato (eerste 90).
**Filmpje:** overgeslagen; het Ebb-concept `marketing/wachtrij/2026-11-24-tiktok-ebb-porthole.md` staat al ingepland (24 nov 18:00 NL).
