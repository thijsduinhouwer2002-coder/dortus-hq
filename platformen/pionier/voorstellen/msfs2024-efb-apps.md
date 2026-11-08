# Microsoft Flight Simulator 2024: EFB-apps

Noor, pionier, 8 nov 2026, run 22:39 UTC. Cijfer **5**, advies **nog niet klaar** (herhaalmeting rond 8 jan 2027).

## Wat het is
In MSFS 2024 zit in elke cockpit een tablet, de EFB (Electronic Flight Bag). Derden kunnen er losse apps voor maken met de EFB API (TypeScript, zelfde soort werk als een kleine webapp). Microsoft kondigde in de SDK-stream van 30 okt 2024 aan: "Develop your own application: EFB API, publish apps on marketplace" (GEZIEN door hulpagent, https://forums.flightsimulator.com/t/662697.json). Docs: https://docs.flightsimulator.com/msfs2024/retail/programming-apis/efb/electronic-flight-bag-api/index.md (GEZIEN). Losse EFB-apps kwamen pas in 2026 echt los.

Waarom gekozen: betalen werkt al (losse EFB-apps worden verkocht op simMarket en in de Marketplace in de sim), de app-laag is jong, het werk past bij Dortus (kleine TypeScript-apps), en op Xbox en PS5 kan een speler alleen via de Marketplace iets toevoegen.

## De vijf vragen

**1. Groeit het platform? Ja, maar het is herstel en het blijft een niche (5 van 10).**
- Gemiddeld gelijktijdige spelers op Steam (GEZIEN, zelf nagekeken, https://steamcharts.com/app/2537590): nov 2024 6.066 (release), dal apr 2025 1.977, okt 2025 2.715, dec 2025 3.778 (PS5-release), okt 2026 5.400, laatste 30 dagen 5.507. Dus x2,0 in een jaar, maar pas net terug op het niveau van de release.
- MSFS 2020 zakt in dezelfde tijd van 5.952 naar 2.611 (GEZIEN door hulpagent, https://steamcharts.com/app/1250410): spelers stappen over, dus een **gedwongen overstap** naar de nieuwe sim (en de nieuwe app-laag).
- PS5-versie sinds 8 dec 2025 (DERDEN, https://www.techradar.com/gaming/microsoft-flight-simulator-2024-is-flying-onto-ps5-in-december-with-psvr-2-support-coming-in-2026); Jorg Neumann noemt "tons of new players" zonder cijfer (DERDEN, https://simulationdaily.com/news/microsoft-flight-simulator-2024-ps5-tons-players-ps-vr2/). 245.000 verkocht op PS5 gaat rond, niet nagekeken (DERDEN, https://www.avsim.com/forums/topic/693756-msfs-2024-sold-245k-copies-on-ps5-so-far/).
- Steam is maar een deel (ook Microsoft Store, Game Pass, Xbox, PS5). Totaal aantal spelers van 2024 is niet bekend; het laatste officiële cijfer is 15 mln spelers voor 2020 (DERDEN, https://videogameschronicle.com/news/microsoft-flight-simulator-hits-15-million-players).
- Reviews gemengd, ±13.600 tegen ±65.700 voor 2020 (DERDEN, SteamSpy).

**2. Is de app-laag jong? Ja (7 van 10).**
- Betaalde losse MSFS 2024 EFB-apps op simMarket (GEZIEN, zoeken op "efb", https://secure.simmarket.com/advanced_search_result.php?keywords=efb, prijzen uit de productdata): Flight Notes EFB App €8,99, Flightline Sim Rate EFB App €8,72 (Flightline Utilities), Ground Services EFB App €7,99 (LatamStudios), JayDee's EFB Checklist App €8,39 (JayDee Gaming, geplaatst 17 aug 2026), EFB++ early access €19,99 (Arvesia LLC). Vijf stuks, allemaal kleine makers.
- Verder (GEZIEN of DERDEN via hulpagent): FS2EFB (maart 2026, PC en Xbox), iFly Schedules EFB (mei 2026, abonnement $6 per maand), EFB Challenging Weather Finder (aug 2026), MSFS Passport 2024 (okt 2026, 55 likes op het forum), InfinityCharts (gratis), EFB Nearest Navaids (alleen in de Marketplace, voor console). efbX van KatiePilot (maker van de EFB in de Fenix A320) komt in Q4 2026 met gratis basis en Premium £3,88 per maand (DERDEN, https://msfsaddons.com/2026/10/13/efbx-answers-its-biggest-question-with-worldwide-lido-charts-and-a-3-88-premium-tier).
- Het aantal apps in de Marketplace in de sim kon ik niet tellen: de onofficiële lijst msfsmarket.place ondersteunt 2024 nog niet (GEZIEN). flightsim.to is een app die zonder browser niets laat zien (GEZIEN).

**3. Kan er betaald worden? Ja (7 van 10).**
- Verkoop werkt nu al op simMarket, eigen sites en in de Marketplace in de sim (GEZIEN, prijzen hierboven). De Marketplace vraagt aanmelding bij het partnerprogramma: gratis, maar met goedkeuring en "beperkte capaciteit" (GEZIEN door hulpagent, https://www.flightsimulator.com/partner-program/). Het deel dat Microsoft houdt is niet openbaar (vaak 30% genoemd, GOK). Een nieuwe winkel StrataSim laat makers 85% houden (DERDEN, https://msfsaddons.com/2026/10/11/the-team-behind-stratawx-is-opening-its-own-flight-sim-store-and-developers-keep-85/).
- Kosten vooraf: een exemplaar van MSFS 2024 om te testen (±€70, GOK) en een pc die het draait. Aanmelden bij het partnerprogramma en voorwaarden accepteren is iets voor Thijs.

**4. Is er vraag te zien? Matig (5 van 10).** Forum (GEZIEN door hulpagent, Discourse-JSON):
- "Send to avionics" voor alle vliegtuigen: 58 berichten, 142 likes (https://forums.flightsimulator.com/t/670142.json).
- Eigen vliegtuig op grondkaarten: 33 berichten, 53 likes (https://forums.flightsimulator.com/t/745979.json).
- SimBrief op de EFB van PS5: 12 likes (https://forums.flightsimulator.com/t/757483.json). PDF-viewer in de EFB: 11 likes (https://forums.flightsimulator.com/t/675169.json).
- Hoofddraad over EFB-apps: 2.679 keer bekeken, wensen: pushback en grondservices, multiplayer-kaart, apps in de Marketplace voor console (https://forums.flightsimulator.com/t/739415.json).
- Tegenwind: sinds SU7 (sept/okt 2026) zit er een standaard Ground Services-app in de EFB (https://forums.flightsimulator.com/t/776826.json): Microsoft vult zelf wensen in. En een klacht dat EFB-apps haperingen geven.

**5. Is de eerste plek te pakken? Ja in kleine hoeken, nee als algemene EFB (6 van 10).**
- Algemene EFB: efbX komt eraan van een bekende maker; daar niet tegenin gaan.
- Open hoeken waar geen duidelijke nummer één is: **documenten en kaarten in de EFB voor console-spelers** (PDF-viewer, eigen checklists en briefings, SimBrief-plan tonen op PS5 en Xbox, waar spelers geen tweede scherm of losse programma's hebben). JayDee's checklist-app is de enige in die richting, en zit niet aantoonbaar in de Marketplace.

## Risico
- Microsoft bouwt zelf wat loopt (Ground Services in SU7). Teken: nieuwe standaard-EFB-apps in de patch notes.
- De markt is klein: ±5.500 gelijktijdige spelers op Steam; een app van €8 moet honderden kopers vinden om iets op te leveren. Verkoopcijfers zijn nergens te zien.
- De Marketplace laat niet iedereen toe ("beperkte capaciteit"). Zonder Marketplace geen console, en dan valt de beste hoek weg.
- Teken dat het stokt: Steam-spelers zakken weer onder ±4.000, of er komen per kwartaal geen nieuwe betaalde EFB-apps bij.

## Eerste productidee
"Console Briefcase": een EFB-app voor Xbox en PS5 (en pc) met je eigen checklists, een PDF- en notitie-lezer en het SimBrief-plan in de tablet, verkocht via de Marketplace, €5 tot €8. Klein, één taak, en precies wat console-spelers missen.

## Cijfer en advies
**5, nog niet klaar.** Betalen werkt en de app-laag is jong met alleen kleine makers, maar het platform groeit vooral terug naar zijn start en blijft een niche, verkopen zijn onzichtbaar, en de beste hoek (console) hangt aan goedkeuring door Microsoft.

Wat het een 6 of 7 maakt: (1) het partnerprogramma laat kleine makers aantoonbaar toe met EFB-apps op console (zoek apps van eenmansmakers in de Marketplace op PS5), (2) Steam-spelers blijven stijgen boven ±6.000, (3) een verkoopcijfer van een EFB-app (bijvoorbeeld reviews op simMarket of een maker die het deelt).

Herhaalmeting rond 8 jan 2027: steamcharts.com/app/2537590 (maandgemiddelden), simMarket zoeken op "efb" (aantal MSFS 2024 EFB-apps en datums), en of efbX uit is en hoe het ontvangen wordt.

Wat ik niet kon meten: aantal apps in de Marketplace in de sim, verkopen, het deel van Microsoft, de eisen van het partnerprogramma, totaal aantal spelers.

Controle: Steam-cijfers zelf nagekeken (zelfde getallen als de hulpagent); simMarket-prijzen zelf uit de productdata gehaald. Forumcijfers en nieuws komen van de hulpagent met link. Geen aparte controleur-agent: het advies is "nog niet klaar", geen ja.
