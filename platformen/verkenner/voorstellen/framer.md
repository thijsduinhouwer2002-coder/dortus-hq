# Voorstel: Framer (Marketplace)

**Advies: nee, voor nu. Cijfer: 4 van 10** (was 5, nog niet klaar). Geen manager en geen bouwwerk. Bijgewerkt op 6 nov 2026, run 17:31 UTC, met een eigen steekproef van 603 plugins.

Waarom nee: van de drie vooraf vastgelegde eisen (zie onderaan) is er geen gehaald. Geld na Framer 3.0 is er wel, maar alleen in kleine bedragen bij nieuwe makers, en de templatemarkt is volgens veel makers ingestort. Bereik is niet te meten, want Framer toont nergens meer gebruikersaantallen. Ondertussen groeit het aanbod snel en is de helft betaald.

## Eigen meting (GEZIEN, 6 nov 2026)
Werkwijze: de overzichtspagina en de 11 categoriepagina's van de pluginwinkel gelezen met curl (elk ±65 plugins), 605 unieke plugins gevonden, daarvan 603 winkelpagina's gelezen. In elke pagina staan id, maker, datum van publiceren en of de plugin betaald is. Data en scripts: `data/framer-steekproef-2026-11-06.json`, `data/framer-slugs-2026-11-06.txt`, `data/framer-ontleed-script.py`, `data/framer-haal-script.sh`.

Let op: de categoriepagina's tonen de bovenste ±65 per categorie, dus de steekproef leunt naar plugins die Framer hoog zet. Het is niet de hele winkel.

**Bereik**
- Geen gebruikersaantallen op winkelpagina's, overzicht of categorieën (GEZIEN, 603 pagina's). Vroeger stond er "12K users" op de pagina (DERDEN: voorbeeld in de [Apify-scraper](https://apify.com/parsebird/framer-plugins-scraper)). Dat veld is weg.
- De statistiekpagina's (`/community/analytics/rankings/`) vragen een account. Alleen eigen cijfers te zien.
- Mediaan en percentage 100+: **niet te meten**. Kan alleen als we zelf een plugin uitbrengen, of via makers die hun aantal openbaar maken. Twee zulke aantallen (eigen opgave van de maker op TrustMRR, niet nagekeken): BuildinFrame ±100 gebruikers voor een reeks van 8 plugins, Framer Export ±3.259 gebruikers.

**Drukte**
- Plugin-id's lopen op. Hoogste id per maand (GEZIEN): dec 2025 679, mrt 2026 970, mei 1232, aug 1538, okt 1843. Dat is ±100 tot 180 nieuwe id's per maand in 2026, tegen ±25 tot 50 per maand begin 2025, dus 3 tot 4 keer zo veel. Id's kunnen ook nooit gepubliceerde plugins tellen (GOK).
- In de steekproef: 376 van 603 zijn van 2026. Oktober 2026 alleen: 58.
- Eén maker (Luke Sn) bracht in oktober 2026 9 betaalde plugins uit, PlumSpace 9 betaald sinds dec 2025, KDX Studios 8 betaald in 2 maanden. In 2026 hebben 10 makers samen 68 plugins (18% van 2026). Dat wijst op makers die met hulp van AI in serie bouwen (GOK).

**Geld**
- 306 van 603 plugins zijn betaald (51%), per halfjaar (GEZIEN): 2024-H2 44% (n=62), 2025-H1 62% (n=65), 2025-H2 54% (n=100), 2026-H1 47% (n=208), 2026-H2 52% (n=168). Het schommelt rond de helft, zonder duidelijke trend.
- Afdracht 0%, maar Framer regelt geen betaling: kassa en btw liggen bij de maker. [Publiceren](https://www.framer.com/help/articles/how-to-publish-a-plugin/). Stream Bunny verkoopt bijvoorbeeld via Polar met een licentiesleutel (GEZIEN op de pagina).
- Geverifieerde bedragen bij pluginmakers (DERDEN, TrustMRR, gekoppeld aan de betaaldienst):
  - [BuildinFrame](https://trustmrr.com/startup/buildinframe), kleine maker uit India, sinds jan 2026, 8 plugins in onze steekproef onder de naam "Soubhagya Sahu" (FrameSEO, FrameAlt, FrameCharts, FrameShaders, Color Palette, Text Styles, LemonSqueezy Checkout, Gumroad Checkout, allemaal 2026): **$400 in totaal**, $83 in de laatste 30 dagen (data tot 27 aug 2026).
  - [Framer Export](https://trustmrr.com/startup/framer-export), sinds mrt 2026: $4.071 in totaal, maar $48 in de laatste 30 dagen. Geen plugin in de winkel, een losse dienst.
  - [Framergenie](https://trustmrr.com/startup/framergenie), sinds okt 2023: $3.479 in totaal, componenten.
- Geen enkele kleine pluginmaker gevonden met meer dan een paar honderd dollar per maand. Grote betaalde plugins (Frameship en FramerForms van Insert Frame, Framer Commerce) tonen geen cijfers.

**Geld na Framer 3.0 (juni 2026), templates**
- Makers melden instorting, allemaal eigen opgave (DERDEN):
  - [Hamzah Haroon](https://www.framer.com/community/posts/Gg7vNAoqv7ij2tpipftzHs/): kliks van 978 naar 224 (min 77%) in 4 weken, geen verkoop sinds de update.
  - [Agop Studio](https://www.framer.com/community/posts/ju3VxLu414Sp3T1MEz6bf/): geen verkoop sinds de update, de top 300 krijgt alle views.
  - [Koshfolio](https://www.framer.com/community/posts/Bu2fkYgR3osZGK8LDgYGSu/): 2 verkopen in 3 dagen ervoor, daarna geen.
  - [Aureus.Design](https://www.framer.com/community/posts/2CPcCh7jGx6JkgKvfuQUX1/) (±2 maanden geleden): stopt, twee maanden geen verkoop.
  - [Dentéa (Snowy Atiq)](https://www.framer.com/community/posts/Gzr6vCiwHFgVsRE4yFPvAU/): template van 16 juni 2026, 2 verkopen in 6 weken.
- Tegengeluid: [Struxent](https://www.framer.com/community/posts/7me3zLvW3iEf6cJdJ8UYCt/) ziet meer verkoop ondanks lagere plek. [Miglena](https://www.framer.com/community/posts/Ljy1CmCTqFFY7Ntcj74GNt/): $1.000 aan verkoop via haar doorverwijslinks (Dub.co) in de eerste maand, post van 14 aug 2026. Haar eigen verdienste is daar maar een deel van, en het is commissie op abonnementen, geen verkoop van een product. [TMPL](https://tmpl.digital/blog/can-you-make-money-with-framer) meldt ±$3.000 per maand aan templates, sinds 2024, artikel uit 2026 zonder precieze datum.
- Conclusie: na 3.0 gaat het geld naar een kleine top en naar doorverwijzen met een eigen publiek. Een nieuwe maker zonder publiek verdient er weinig (GOK, op basis van bovenstaande losse berichten).

**Grootte**
- ±500.000 maandgebruikers, waardering $2 miljard. [Persbericht, aug 2025](https://www.dutchnews.nl/businesswire/framer-raises-100-million-series-d-at-a-2-billion-valuation-to-redefine-how-businesses-build-websites)
- Framer zegt $6,5 miljoen aan makers te hebben uitbetaald in 2025, zonder splitsing, waarschijnlijk vooral doorverwijzing. [Framer 2025](https://www.framer.com/2025)

**Vindbaarheid**
- Geen keuring meer, publiceren gaat direct. Ranking op views, remixes en aankopen, formule geheim. [Ranking](https://www.framer.com/help/articles/marketplace-ranking/). Makers klagen dat alleen de top gezien wordt (zie boven).

**Past het bij ons**
- Een plugin bouwen in 1 tot 2 weken kan (GOK, web-techniek). Maar we moeten zelf een kassa en btw regelen (Polar of Lemon Squeezy), en Thijs een Framer-account en betaaldienst.

## Voor
- Groot, zakelijk publiek dat al betaalt voor Framer.
- 0% afdracht.
- Betaalde plugins zijn normaal: de helft vraagt geld.

## Tegen
- Geen kleine pluginmaker aantoonbaar boven ±$100 per maand. Het enige geverifieerde voorbeeld van een kleine maker met 8 plugins haalt $400 in 7 maanden.
- Bereik niet te meten, dus we zouden blind lanceren.
- Aanbod groeit 3 tot 4 keer sneller dan begin 2025, met makers die in serie uitbrengen.
- Na Framer 3.0 krijgt een kleine top bijna alle aandacht.
- Framer bouwt zelf AI-functies (Agents) die templates en kleine plugins overbodig kunnen maken.
- Eigen kassa en btw, meer werk voor Thijs.

## Eerste idee (als het ooit wel ja wordt)
Een betaalde plugin voor een gat dat Framer zelf niet snel dicht, bijvoorbeeld formulieren met bestandsupload of video. Zie het vorige idee in de geschiedenis van dit bestand.

## Wat dit oordeel zou veranderen
- Een openbare telling van gebruikers per plugin (bijvoorbeeld als Framer het veld terugzet).
- Twee of meer nieuwe kleine pluginmakers met geverifieerde omzet boven $300 per maand na juni 2026.

## Vooraf vastgelegde grens (uit de vorige versie) en uitkomst
1. Bereik: steekproef van 30+ plugins uit 2026, mediaan 100+ gebruikers. **Niet te meten**: geen gebruikersaantallen meer openbaar. Telt als niet gehaald.
2. Geld na Framer 3.0: 2 kleine makers met eigen verkoopcijfers van na juni 2026. **Niet gehaald**: wel cijfers gevonden (BuildinFrame $83 per 30 dagen, Dentéa 2 verkopen, Framer Export $48 per 30 dagen), maar ze laten juist zien dat het weinig is.
3. Past het bij ons (template): niet meer nodig, want we doen geen templates.

## Nakijken
Eerste versie (advies ja als test) afgekeurd door de controleur (6 nov). Tweede versie (nog niet klaar, 5). Deze derde versie met eigen steekproef: controleur akkoord (6 nov, run 17:31). Hij rekende de steekproef na, las de bronnen met curl, bevestigde dat er geen gebruikersaantallen op de pagina's staan en vond geen tegenvoorbeeld (Framera op TrustMRR is een iOS-app, niet Framer). Vier correcties verwerkt.
