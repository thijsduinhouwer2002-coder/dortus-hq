# Voorstel: Autodesk Design and Make Marketplace (vroeger Autodesk App Store)

**Advies: nog niet klaar.** Cijfer 4 (de controleur vond 3 ook verdedigbaar). Onderzocht 7 nov 2026 run 15:32, eigen meting van alle 5.055 apps uit de openbare sitemap (marketplace.autodesk.com, robots.txt staat dat toe) plus een onderzoeker voor het geld. Controleur: eerst niet akkoord (betaald-telling en prijzen fout), 7 correcties verwerkt.

Kort: de voorwaarden zijn de beste die we tot nu toe zagen (0% afdracht, kopers zijn bedrijven, 41% van de apps vraagt in de winkel geld), maar bereik en verkoop zijn van buitenaf niet te zien, en ik vond geen enkele kleine maker die aantoonbaar via deze winkel verdient.

## Wat is het
De winkel voor uitbreidingen op AutoCAD, Revit, Fusion, Civil 3D, Inventor en meer. In april 2026 vervangen door de Design and Make Marketplace; apps.autodesk.com stuurt door (DERDEN, https://blog.autodesk.io/design-make-marketplace/).

## Cijfers

### Drukte (GEZIEN, eigen meting)
- 5.055 apps in de sitemap (3 pagina's gaven een fout). Eerste uitgave per jaar: 2023 458, 2024 513, 2025 651, 2026 tot nu 979.
- Nieuwe apps per maand: 2025 ±40 tot 90, 2026 eerste helft 55 tot 90, daarna 130 (aug), 139 (sep), 158 (okt); nov tot nu 50 (een week). Snelle groei sinds de nieuwe winkel en, denk ik, AI-hulp bij bouwen (GOK).
- Van aug tot nu: 477 nieuwe apps van 251 makers, 185 makers met precies 1 app. Veel kleine makers dus. Maar ook bedrijven met reeksen (Todor Latev 52 sinds nov 2025, Piping Content 25, ProtoTech 24).
- Producten bij nieuwe apps sinds nov 2025 (n=1.070): Revit 435, Fusion 205, Civil 3D 159, Plant 3D 151, AutoCAD 133.
- Nieuw: 10 apps van de soort "MCP" sinds aug (GEZIEN).
- Let op: de sitemap toont alleen apps die nu online staan. Weggehaalde apps tellen niet mee, dus oude jaren lijken kleiner (GOK).

### Geld
- **Afdracht 0%** (Publisher Agreement, bijgewerkt 3 mei 2026: "has set a commission rate of 0.0%", mag Autodesk wijzigen; GEZIEN door de controleur, https://apps.autodesk.com/Content/pdf/Publisher.pdf). De commissie geldt op de "net fee", dus na de kosten van de betaaldienst die Autodesk aanwijst; die kosten betaalt de maker. Volgens de makerspagina's is dat PayPal (DERDEN, https://aps.autodesk.com/marketplace/publisher-center). Btw en terugbetalingen doet de maker zelf (artikel 3 en 20.10).
- **Prijsvormen (GEZIEN, alle apps):** 2.054 van 5.055 apps (41%) zijn echt te koop in de winkel (eenmalig, maand- of jaarabonnement, of een bedrag boven 0). Plannen: gratis 1.836, eenmalig 1.308, onbeperkte proef 1.159, jaarabonnement 736, proef 30 dagen 581, maandabonnement 552, Autodesk-abonnement 76. Een app met alleen "onbeperkte proef" toont alleen "Start free trial" zonder prijs: de licentie loopt buiten de winkel (GEZIEN door de controleur). Nieuwe apps sinds nov 2025: 449 van 1.070 (42%) echt betaald, 211 alleen proef. Mediaanprijs bij nieuwe apps (USD, boven 0): eenmalig $25 (n=311), per maand $8 (n=111), per jaar $60 (n=135).
- **Verkoop: niet te zien.** Geen downloads, geen gebruikers, geen verkopen op de pagina's. Reviews worden pas in de browser geladen via een interne API; die heb ik niet gebruikt (de veiligheidscontrole hier weigerde dat, terecht).
- **Kleine makers met cijfers: niet gevonden** (onderzoeker). Een R&D-lead op r/Revit (jan 2025): "Most for sale plugins are developed by third party app developers (companies), not individuals" (DERDEN, via een Reddit-spiegel). Twee Indie Hackers-titels die mogelijk over AutoCAD-plugins gaan ("$150k/yr product", "10k all time revenue") konden niet gelezen worden (botcheck), dus tellen niet.
- Revit-tools verkopen wel bij bedrijven: DiRootsOne Premium €100 per gebruiker per jaar (DERDEN, https://diroots.com/revit-plugins/dirootsone/), maar dat is een bedrijf.

### Bereik
- Niet te meten. Er is geen sortering op populariteit in de winkel (gebruiker op r/Fusion360, mei 2026, DERDEN). Totaalcijfer alleen oud: 3 miljoen downloads in dec 2017 (DERDEN, https://blog.autodesk.io/autodesk-app-store-surpasses-3-million-downloads/).

### Vindbaarheid (DERDEN en GOK)
- Sinds 27 aug 2026 zoekt Autodesk Assistant in de winkel in gewone taal en vergelijkt apps op prijs en reviews (DERDEN, https://aps.autodesk.com/node/4051). Dat kan een nieuwe, eerlijke ingang zijn voor nieuwe apps (GOK).
- Kopers zijn vaak BIM-managers bij bureaus die meerdere licenties kopen (GOK).

### Past het bij ons
- Revit- en AutoCAD-plugins zijn C# (.NET) op Windows; testen in de echte app kan niet op GitHub Actions zonder Autodesk-licentie (GOK, niet nagegaan). Dat is een groot verschil met Obsidian en JetBrains.
- Fusion-add-ins kunnen in Python of C++. Een web-app of MCP-server kan zonder desktop.
- Een gewone desktop-plugin heeft geen kosten voor Autodesk Platform Services (DERDEN, getting-started).

## Voor- en nadelen
Voor: 0% afdracht; kopers zijn bedrijven met budget; betalen, proef en abonnement zitten in de winkel (41% van de apps gebruikt dat); nieuwe AI-zoekfunctie.
Tegen: verkoop en bereik niet te zien; 185 makers met 1 app sinds aug is vooral drukte; geen bewijs dat kleine makers verdienen; drukte verdubbelt in een paar maanden; bouwen en testen vraagt Windows en een dure licentie (Revit ±$3.000 per jaar, GOK).

## Eerste idee (GOK)
Een Revit-hulpmiddel voor BIM-managers (bijvoorbeeld controle van naamgeving en parameters met een rapport), of een MCP-server die Revit-gegevens leesbaar maakt voor AI, met 30 dagen proef en een jaarabonnement.

## Wat er nog moet gebeuren voor een ja
1. Reviews per app tellen (de enige zichtbare maat voor gebruik): kan met de browser van Thijs, of als Thijs toestemming geeft om de openbare API achter de winkel te lezen. Dan een steekproef van nieuwe apps sinds 2025.
2. Twee kleine makers vinden die een bedrag delen (Indie Hackers met browser, LinkedIn).
3. Nagaan of testen zonder betaalde Revit kan (een proeflicentie of de Revit-API in een test).

## Herhaalmeting
`data/autodesk-haal-script.py` (alle apps uit de sitemap, ±2 minuten) en `data/autodesk-analyse-script.py`. Over 4 weken opnieuw geeft de echte instroom en hoeveel apps verdwijnen.
