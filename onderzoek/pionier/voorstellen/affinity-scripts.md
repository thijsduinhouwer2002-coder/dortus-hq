# Voorstel: Affinity by Canva, scripts en hulpprogramma's (Noor, 8 nov 2026)

**Cijfer: 5. Advies: nog niet klaar.** Ja zodra twee dingen kloppen: de voorwaarden van Canva staan verkoop van scripts of hulpprogramma's toe (een mens met een browser moet ze lezen, zie onderaan), en de herhaalmeting rond 8 dec laat zien dat de stroom scripts en downloads van de Script Manager doorgroeit.

## Wat is het
Affinity (Designer, Photo en Publisher in één app) is sinds 30 okt 2025 gratis, eigendom van Canva. Versie 3.2 (april 2026) bracht een ingebouwde MCP-server en een Scripts-paneel; versie 3.3 (15 sept 2026) een Scripting Studio waarin je JavaScript schrijft of door AI laat schrijven (DERDEN, https://www.cgchannel.com/2026/09/canva-releases-affinity-3-3/ en https://www.creativebloq.com/design/design-software/affinity-3-3-shows-that-canva-is-serious-about-taking-on-adobe). Scripts automatiseren werk; ze kunnen geen nieuwe gereedschappen toevoegen. Delen gaat met een bestand (.afscripts). Er is geen officiële winkel of galerij, alleen een voorbeeldbibliotheek in de app.

## De vijf vragen

**1. Groeit het platform hard en zichtbaar? Ja.**
- 1 miljoen nieuwe gebruikers in minder dan een week na de gratis versie (DERDEN, https://petapixel.com/2025/11/06/affinity-added-1-million-users-in-less-than-a-week/), 3 miljoen downloads in 33 dagen (DERDEN, https://petapixel.com/2025/12/03/affinity-hits-3m-downloads-of-its-new-editing-software-in-just-33-days), en volgens Canva "meer dan zeven miljoen aanmeldingen" bij de lancering van de gratis iPad-app op 2 nov 2026 (DERDEN, https://macrumors.com/2026/11/02/canva-free-affinity-app-ipad/).
- Motor: Canva (groot, winstgevend) duwt Affinity als gratis tegenhanger van Adobe en bouwt er snel aan (3.3 had 60+ nieuwe functies).
- Niet gemeten: actuele groei van r/Affinity (Reddit weigert onze verzoeken), of scripting op de iPad werkt (GOK: nog niet).

**2. Is de winkel jong? Ja, er is nog niet eens een officiële.**
- Community-registry van JiriKrblich, de feitelijke winkel achter de Affinity Script Manager: **185 scripts van 76 makers** (GEZIEN, registry.json, 8 nov). Eerste commit 18 april 2026. Nieuwe scriptbestanden per maand: apr 36, mei 43, jun 10, jul 26, aug 14, sep 23, okt 41 (GEZIEN, git-geschiedenis; een script kan uit meer bestanden bestaan, dus dit is een benadering). Na 3.3 trok het aan.
- Categorieën: Object 77, Text 20, Effect 16, Color 15, Artboards 11, Layer 11, Export 10, Generator 10, Layout 5, Print 4 (GEZIEN).
- Affinity Script Manager (desktopapp): 288 sterren, ±11.000 downloads (GEZIEN, shields.io). Tweede lijst: affinityhub.js.org, 51 scripts van 19 makers (DERDEN, onderzoeker).
- Vergelijk: bij 7 miljoen aanmeldingen is 11.000 downloads van de manager heel weinig. Scripting is nog iets voor een kleine groep vroege gebruikers. Dat is precies het pioniersmoment, maar het betekent ook dat het publiek nu klein is.

**3. Kan er betaald worden? Alleen buiten Canva om, en dat gebeurt al.**
- Geen betaalplan of winkel van Canva gevonden (DERDEN, onderzoeker; GOK: komt er niet snel).
- Visual.af verkoopt openlijk hulpprogramma's die in Affinity werken: Filter Gallery (gratis met 8 effecten, $12 voor alle 97), Face Liquify $5, Affont $24, eenmalige betaling, Windows en macOS (GEZIEN, https://www.visual.af/). Verkoopaantallen niet zichtbaar.
- Dortus heeft de betaalweg al: Polar met licentiesleutel, zoals bij Rollwright (besluit 6 nov). Een los script in platte JavaScript is makkelijk te kopiëren, dus het betaalde product moet een hulpprogramma zijn (zoals Visual.af) of een script met een licentiecontrole in een apart programma.
- Onzeker: de Affinity Additional Terms en Feature-Specific Terms van Canva kregen nieuwe versies op 15 april en 30 sept 2026, precies bij 3.2 en 3.3, en staan achter een botmuur (DERDEN, https://www.canva.com/policies/affinity-additional-terms/). Wat erin staat over verkopen weten we niet.

**4. Is er vraag? Ja, al jaren, maar het meeste is oud.**
- Verzoekdraad "Scripting" op het Affinity-forum: ±253.000 keer bekeken, ±862 reacties, sinds 2018 (DERDEN, onderzoeker, https://forum.affinity.serif.com/index.php?/topic/64885-scripting/). Gebruikers die van InDesign en Illustrator komen missen hun scripts.
- Wat makers nu bouwen laat de wensen zien: kalenders, nummering, zoeken en vervangen met een lijst, batch-export, grafieken, rechts-naar-links tekst (GEZIEN, registry).
- Niet gemeten: verzoeken op Reddit met upvotes, en waar de nieuwe Canva-community zit (het oude forum ligt sinds sept 2025 stil).

**5. Is de eerste plek nog te pakken? Ja, in werk voor drukwerk en opmaak (Publisher-kant).**
- De verspreiding is in handen van één hobbymaker (JiriKrblich: manager, registry, webdirectory), alles gratis. Hij is geen concurrent maar een etalage: een gratis versie van ons in zijn registry zet ons voor alle 11.000 gebruikers.
- Per soort script bestaat hooguit één los gratis script (Swiss Calendar Creator, Numbering - Sequences, Smart Exporter, FindChangeByList French, Chart Builder). Niemand heeft een verzorgd, onderhouden product in drukwerk en opmaak. De enige verkoper (Visual.af) zit in effecten en fonts.
- Categorie voor ons: **productie en drukwerk voor Publisher**: kalenders en planners, nummering en tickets, opmaak van kaarten en etiketten met meerdere per vel (imposition), en export in batches met naamregels. Dat zijn klussen waar professionals voor betalen en die een AI-gegenereerd script van tien regels niet goed doet.

## Risico's en waaraan je ze ziet
- **AI maakt eenvoudige scripts waardeloos.** De Scripting Studio laat AI scripts schrijven. Kleine scripts (een kleur wisselen, lagen hernoemen) maakt iedereen zelf. Alleen grote, verzorgde hulpprogramma's houden waarde. Teken: makers in de registry stoppen, of vragen worden "laat AI het doen".
- **Canva pakt het zelf of verbiedt verkoop.** Een officiële galerij zonder betaalroute, of voorwaarden die verkoop verbieden, maakt de kans kleiner. Teken: een nieuwe versie van de voorwaarden, of een scriptgalerij in 3.4.
- **Scripting blijft een nichefunctie.** Teken: de manager blijft rond 11.000 downloads en de registry groeit minder dan 20 scripts per maand.
- **Bewijs dat het blijft:** Canva investeert zichtbaar (twee scriptversies in een half jaar, MCP ingebouwd, iPad), en Affinity is hun antwoord op Adobe. Dat platform verdwijnt niet snel; de vraag is alleen of scripts een markt worden.

## Eerste productidee (GOK, nog niet bouwen)
"Kalender en planner voor Affinity": een gratis script in de registry dat een maandkalender in je eigen stijl op de pagina zet, en een betaalde versie (eenmalig, ±$15, via Polar) met jaarplanners, feestdagen per land, weeknummers, meerdere talen en vaste sjablonen. Kalenders zijn een jaarlijkse piek (nu, november en december), drukkers en ontwerpers maken ze elk jaar, en er staan nu twee losse hobbyscripts. Tweede keus: nummering en tickets met meerdere per vel.

## Wat nog gemeten moet worden
- Herhaalmeting rond 8 dec: `python3 data/affinity-scripts-meet.py` en vergelijk met `data/affinity-scripts-2026-11-08.json` (185 scripts, 76 makers, manager 288 sterren en ±11k downloads). Tel ook de nieuwe scriptbestanden van november in de git-geschiedenis.
- Voorwaarden van Canva over verkopen: staat op de lijst van Thijs (één blik in een browser).

## Werkwijze
Onderzoeker (agent) voor groei, scripting, geld, vraag en concurrentie. Zelf nagekeken: registry (185 scripts, 76 makers, categorieën, groei per maand uit de git-geschiedenis), sterren en downloads van de manager, en de prijzen van Visual.af. Niet zelf gelezen: de help- en voorwaardenpagina's van affinity.studio en canva.com (botmuur; die omzeilen we niet). Geen controleur: advies is geen ja en de kerncijfers zijn zelf gezien.
