# Rhino en Grasshopper (plugins voor het 3D-programma Rhino van McNeel)

Vera, 8 nov 2026, run 08:31 (UTC), tweede platform van de run. Zelf toegevoegd.

## Advies: nog niet klaar, cijfer 4

Rhino is een betaald vakprogramma ($995) voor architecten, ontwerpers en scheepsbouw. Het is rustig (±40 tot 130 nieuwe pakketten per maand), McNeel omarmt AI en bouwen met Claude wordt op het forum goed ontvangen, en we kunnen er met code iets bouwen. Maar er is geen betalen in de winkel: McNeel en Food4Rhino verkopen niets voor de maker, die regelt zelf licenties via Gumroad of een eigen site. Ik vond geen enkel verkoopaantal van een betaalde plugin, alleen Patreon-bedragen van een paar makers. Het bereik van nieuwe pakketten is matig: mediaan ±58 downloads na 3 tot 6 maanden, en die teller telt ook updates mee.

Wat nog gemeten moet worden om ja of nee te zeggen: verkoopbewijs van kleine betaalde plugins (Gumroad-pagina's van Grasshopper- en Rhino-tools die een verkoopteller of aantal ratings tonen), en een herhaalmeting van de golf van oktober 2026.

## Nagekeken
Controleur akkoord met nog niet klaar, cijfer 4 (4 tot hoogstens 5 verdedigbaar): tabel, jaren, maanden en top 4 herberekend en gelijk, 8 van 8 pakketten live gelijk. Correcties verwerkt: telling betaalwoorden als ±14 tot 25, uitspraak McNeel preciezer, schrijver van het AI-voorbeeld werkt bij McNeel, groepen overlappen.

## Hoe gemeten
- Open package-API van McNeel: yak.rhino3d.com/packages (alle 1.395 pakketten met totaal aantal downloads) en per pakket /versions/<naam> (alle versies met datum). Daaruit de datum van de eerste versie (GEZIEN, 8 nov 2026, data/rhino-yak-lijst-2026-11-08.json en rhino-yak-versies-2026-11-08.jsonl, scripts rhino-yak-haal-script.py en rhino-yak-analyse-script.py).
- food4rhino.com geeft 403 op curl; niet omzeild. Veel oudere plugins staan alleen op Food4Rhino, dus de yak-lijst is niet de hele markt.
- Let op: download_count is het totaal over alle versies. Een pakket dat vaak een update krijgt telt elke update opnieuw. Pakketten met 1 versie zijn dus de eerlijkste maat.

## Cijfers

### Drukte (GEZIEN, eerste versie in yak)
Per jaar: 2023 143, 2024 149, 2025 189, 2026 593 (t/m 8 nov). Per maand: jul 2025 t/m feb 2026 ±12 tot 20, mrt t/m sep 2026 ±40 tot 80, okt 2026 131. Een golf sinds maart 2026, waarschijnlijk door bouwen met AI (McNeel moedigt "vibe coding" aan, DERDEN hieronder).

### Bereik (GEZIEN, totaal downloads tot 8 nov)

| Eerste versie | n | mediaan | 100+ | 500+ | 1.000+ | 5.000+ |
|---|---|---|---|---|---|---|
| jul t/m dec 2025 | 101 | 196 | 61% | 29% | 12% | 4,0% |
| mrt t/m jun 2026 | 203 | 78 | 44% | 17% | 8,9% | 3,9% |
| mei t/m aug 2026 | 216 | 57,5 | 35% | 11% | 6,9% | 2,8% |

De groepen mrt t/m jun en mei t/m aug overlappen (mei en juni zitten in allebei).

- Van mei t/m aug hebben 72 pakketten maar 1 versie: mediaan 22,5 downloads. Mediaan aantal versies is 3.
- Top mei t/m aug: Raven (251.232, 45 versies), Rhino-MCP-Platform (51.021; makers Callum Sykes en Dan Cascaval, die bij McNeel werken, plus "Claude"), Eddy3D (11.220), R4V3N (10.576).
- 53 nieuwe pakketten (jul 2025 t/m aug 2026) noemen AI, LLM, Claude, GPT of MCP; mediaan 186 downloads, 30% haalt 1.000+. AI-tools doen het dus beter dan gemiddeld.
- Maar ±14 tot 25 van de 461 nieuwe pakketten (jul 2025 t/m aug 2026) noemen in de beschrijving een licentie, proefversie, abonnement of prijs (het getal hangt af van de zoekwoorden; bij 25 zitten ook gratis licenties zoals MIT). De meeste zijn gratis.

### Geld (DERDEN)
- McNeel verwijst makers naar eigen betaaldiensten (FastSpring, Digital River) met een winkellink op hun Food4Rhino-pagina; de maker regelt de verkoop zelf (Carlos Pérez van McNeel, https://discourse.mcneel.com/t/107311, jan 2021). Een winkel van McNeel voor plugins van anderen vond ik niet. Food4Rhino verdient aan betaalde plekken (https://www.rhino3d.com/e-news/0224f4r_dev/, feb 2024).
- Licenties via het Rhino-account kan als "Cloud Zoo Issuer", maar de maker bouwt dan een eigen server en regelt zelf de betaling (https://discourse.mcneel.com/t/191619, sep 2024; https://discourse.mcneel.com/t/212321, nov 2025).
- Gangbaar in 2026: gratis proef op Food4Rhino, volledige versie op Gumroad (bv. MOONG Tools $99, https://discourse.mcneel.com/t/223437, okt 2026). Verkoopaantallen niet gevonden.
- Patreon (graphtreon, schatting, nov 2026): Grasshopper Gold 388 leden, $679 tot $3.000 per maand (https://graphtreon.com/creator/grasshoppergold); Simple GG Sculptor 37 leden, $65 tot $295; display modes van niko $22.
- Een lancering van een betaalde plugin op het forum wordt 74 tot 358 keer bekeken (onderzoeker, forumtellers).

### Markt en regels (DERDEN)
- McNeel deelt geen actuele gebruikerscijfers (https://discourse.mcneel.com/t/174853, feb 2024). Food4Rhino: 1.000+ apps en 10 miljoen downloads in feb 2024.
- Rhino 9 Beta sinds 23 jun 2026 (https://discourse.mcneel.com/t/220246), overstap naar .NET 10 (https://www.rhino3d.com/en/e-news/0726dev/, jul 2026). Grasshopper 2 zit in de beta.
- McNeel brengt zelf RhinoAI uit (koppeling met Claude, Codex, Gemini; https://discourse.mcneel.com/t/223146, sep 2026) en een officiële RhinoMCP. Gratis AI van McNeel wordt concurrentie voor betaalde AI-plugins.
- Geen weerstand gevonden tegen plugins die met AI gemaakt zijn: Brian James (werkt bij McNeel, zegt zelf niet te programmeren) bracht twee met Claude gebouwde plugins uit en kreeg positieve reacties (https://discourse.mcneel.com/t/222297, sep 2026). Omdat hij bij McNeel werkt is dat zwak bewijs voor onafhankelijke makers.
- Vindbaarheid: Package Manager in Rhino (zoeken werkt slecht), Food4Rhino, forum, YouTube.

## Voordelen
- Betalende vakgebruikers, programma van $995: wie een tijd bespaart wil best $20 tot $100 betalen (GOK).
- Rustig en AI-vriendelijk, open API om te meten.
- Past bij ons: C#- of Python-plugins zijn met code te bouwen. Rhino draait op Windows en Mac; een echte test in GitHub Actions moet nog uitgezocht worden (Rhino heeft een licentie nodig).

## Nadelen
- Geen betalen in de winkel, geen verkoopbewijs van kleine makers.
- Matig bereik voor nieuwe pakketten (mediaan ±58, en dat is met updates meegeteld).
- McNeel zelf bouwt gratis AI-functies.
- Rhino kopen voor tests kost geld (Thijs).

## Eerste idee als het ja wordt
Een kleine betaalde tool voor landschapsarchitecten (beplantingsplan en plantlijst, gevraagd op het forum: https://discourse.mcneel.com/t/187887, jul 2024), gratis proef in de Package Manager, licentie via Gumroad.
