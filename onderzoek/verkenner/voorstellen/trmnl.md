# TRMNL (e-ink-schermpje met community "recipes" en een Creator Fund)

Vera, 9 nov 2026 run 00:31 (Amsterdam), platformrun, zelf toegevoegd. Labels: GEZIEN, DERDEN, GOK.

**Advies: nee voor nu. Cijfer 3.**

## Wat het is
TRMNL verkoopt een e-ink-scherm (plus een licentie om je eigen apparaat te gebruiken, BYOD). Gebruikers zetten "plugins" op het scherm. Iedereen kan een **recipe** publiceren: een sjabloon (Liquid) met eigen velden en data uit een open URL. Recipes zijn gratis voor de gebruiker; een eigen prijs vragen kan niet. Sinds nov 2025 betaalt TRMNL makers elke maand uit een **Creator Fund**.

## Wat ik mat (GEZIEN)
Bron: de open Recipes API (`trmnl.com/recipes.json`, gedocumenteerd op docs.trmnl.com/go/public-api/recipes-api; robots.txt verbiedt alleen /api/). Alle 1.237 gepubliceerde recipes opgehaald met publicatiedatum en installs + forks ("connections"). De controleur haalde zelf 4 pagina's op: alle 337 kwamen exact overeen.

**Bereik (connections per lichting):**

| Gepubliceerd | Aantal | Mediaan | 50+ | 100+ |
|---|---|---|---|---|
| feb t/m mei 2026 (6 tot 9 mnd oud) | 230 | 15 | 49 (21%) | 13 (6%) |
| jun t/m aug 2026 (3 tot 5 mnd oud) | 155 | 14 | 25 (16%) | 7 (5%) |
| sep 2026 (jong) | 72 | 10,5 | 10% | 1% |
| okt 2026 (jong) | 102 | 9 | 9% | 1% |

Sep en okt zijn nog jong en tellen niet als trend. Vroege recipes (begin 2025) haalden mediaan 40 tot 200; de beste nieuwe van 2026 halen ±550 tot 660.

**Drukte:** ±45 tot 100 nieuwe recipes per maand, okt 2026 de drukste maand (102). Alle recipes samen: 77.503 connections. 437 makers.

**Verdeling:** 311 recipes halen de fondsdrempel van 50 connections, van 137 makers. De grootste maker (62 recipes) heeft 15,8% van die connections, de tweede 12,8%. Een maker die pas in nov 2025 begon (29 recipes) heeft al 4,3%: een nieuwkomer kan dus wel snel een plek veroveren.

## Geld (DERDEN, maandposts op trmnl.com/blog/creator-fund-MM-YYYY, alle 12 nagekeken door de controleur)
Het fonds is 80% van het abonnement TRMNL+ en 10 tot 15% van de verkoop van Developer Edition, Clarity Kit en BYOD. Daarvan gaat 70% naar plugin-makers, 30% naar bijdragers aan open source.

Deel voor plugin-makers per maand: nov 2025 $2.150, dec $4.124, jan 2026 $3.668, feb $2.442, mrt $21.196 (eenmalig: opgespaarde verkoop Clarity Kit X), apr $3.858, mei $3.798, jun $4.159, jul $4.136, aug $3.979, sep $3.890, okt $3.797. Daarvoor één proefuitkering van $10.777 (22 jul tot 13 nov 2025).

**De pot is sinds april vlak, ±$3.900 per maand voor alle makers samen, licht dalend.** Verdeling op leeftijd in playlists, aandeel in playlists en vertoningen, minimaal 50 connections. Comics krijgen sinds 1 april niets meer.

Ruwe schatting (GOK, aandeel connections staat niet gelijk aan aandeel geld): de grootste maker ±$600 per maand, de nieuwkomer met 4,3% ±$170, 1% van de connections ±$40. Geen maker deelt zijn bedrag openbaar (gezocht, niet gevonden).

Aantal apparaten: niet openbaar. Bekend: 1.325 Kickstarter-voorbestellingen (2024), eerste batch 2.250, "over 700" plugins eind 2025 (DERDEN: trmnl.com/blog/2025-in-review).

## Voor en tegen
Voor:
- Geld gaat aantoonbaar naar kleine makers, elke maand, met openbare cijfers.
- Recipes zijn klein werk (sjabloon plus data-URL); wij kunnen er tientallen in een paar weken maken.
- Een nieuwkomer haalde in een jaar 4,3% van het bereik; de top is niet onaantastbaar.
- Open API: alles is goed te volgen.

Tegen:
- **Het plafond is laag.** De hele pot is ±$47.000 per jaar voor alle makers. Zelfs als nummer één (16%) is het ±$600 per maand, en dat met 62 recipes.
- De pot groeit niet sinds april.
- Een eigen prijs vragen kan niet. Alleen een eigen betaalde dienst buiten TRMNL (Third Party-plugin met OAuth), maar dan geen hulp van TRMNL bij betalen en nog minder bereik.
- Gewone nieuwe recipes halen mediaan 14 tot 15 connections; maar 16 tot 21% haalt de drempel van 50.
- Klein platform, aantal apparaten onbekend.

## Wat we zouden bouwen (als het ooit verandert)
Een reeks van 20 tot 40 nuttige recipes in gaten die nog open zijn (lokale data per land, zoals Nederlandse en Duitse diensten: Buienradar bestaat al, ov, afval, energieprijzen), allemaal onder één naam. Doel: 5 tot 10% van de connections in een half jaar. Dat levert bij de huidige pot ±$200 tot $400 per maand op (GOK).

## Waarom nee voor nu
Bereik voor een nieuwe recipe is klein en het geld is een vaste pot die niet groeit. Grote speler worden kan hier wel, maar groot is hier maximaal een paar honderd dollar per maand. Voor Dortus' doel (€300 tot €400 per maand in maart) is dat te weinig voor de moeite van een nieuwe manager.

## Wat het zou veranderen (cijfer naar 5 of 6)
- TRMNL laat makers een eigen prijs vragen voor recipes, of
- de pot groeit 3 maanden op rij duidelijk (boven $6.000 per maand voor plugin-makers), bijvoorbeeld door een nieuw apparaat of meer TRMNL+.
Herhaalmeting: de maandpost begin december en januari lezen, en de recipes opnieuw halen met `data/trmnl-recipes-json-script.py` (rustig, 1 verzoek per 2 s).

Controleur: alle getallen kloppen (API, lichtingen, verdeling, 12 maandbedragen). Toevoegingen verwerkt: proefuitkering, jonge maanden niet als trend, comics uitgesloten, aandeel connections is niet aandeel geld.

Data: `data/trmnl-recipes-2026-11-09.json`, scripts `data/trmnl-recipes-json-script.py` en `data/trmnl-analyse-script.py`.
