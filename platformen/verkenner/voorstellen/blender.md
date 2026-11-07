# Voorstel: Blender

**Advies: ja.** Cijfer 7 (was 5, nog niet klaar). Bijgewerkt 7 nov 2026 run 10:31 met een eigen meting van het geld op Superhive. Dit was de meettaak van Hans van 6 nov.

## Waarom het oordeel verandert
Hans zette Blender op nog niet klaar omdat het geld niet gemeten was. Nu wel: Superhive (vroeger Blender Market) toont op elke productpagina een verkoopteller ("Sales 10+", "Sales 400+") en de publicatiedatum. Daarmee kon ik voor het eerst op een platform echte verkopen van nieuwe betaalde producten tellen, niet beoordelingen.

## Cijfers

### Geld (GEZIEN, eigen meting 7 nov)
- "Published" is de eerste publicatie: de datum volgt het product-id, en updates (Smart Remesh van v1.2.2 tot v3) veranderen hem niet (GEZIEN, nagekeken door de controleur).
- Steekproef: elke derde productpagina uit de sitemap van Superhive, regels 60.500 tot 70.000 (product-id 253.450 tot 264.732, gepubliceerd ±1,5 tot 7 maanden geleden). 3.166 pagina's opgehaald, waarvan 375 add-ons (via de subcategorie van het product). Niet meegeteld: de subcategorieën presets en theme-packages (ook add-ons volgens Superhive) en 19 producten zonder categorie. Met presets en theme-packages erbij: n=366, dezelfde percentages, 19 boven $300 per maand, ±$56.000 samen, ±215 per maand. De cijfers hieronder zijn dus voorzichtig. Data: `data/superhive-steekproef-2026-11-07.jsonl`, scripts `data/superhive-haal-script.py` en `data/superhive-analyse-script.py`.
- **Betaalde add-ons van 2 tot 6 maanden oud (n=316, 238 makers):**
  - mediaan: minder dan 10 verkopen (de teller verschijnt pas bij 10: in 3.166 pagina's staat nooit een getal van 1 tot 9, 12 tonen precies "10", en 41 producten zonder teller hebben wel beoordelingen, dus kopers; GOK op GEZIEN)
  - 31% heeft 10+ verkopen (99), 9% 50+ (28), 7% 100+ (21), ±1% 500+ (2)
  - mediaanprijs $14
- **Netto per maand (GOK op GEZIEN):** verkopen (ondergrens van de teller) maal lijstprijs maal 65% min $0,49 per verkoop, gedeeld door de leeftijd. Dan halen 16 van de 316 (5%) $300+ per maand, 40 (13%) $100+ per maand. Die 16 komen van 14 makers; één maker (Milad Kambari) heeft er 3. Kortingen in uitverkopen drukken dit; de teller is een ondergrens, dat tilt het weer op.
- **Voorbeelden van nieuwe makers boven $300 per maand (GEZIEN teller, bedrag GOK):** Smart Remesh van Milad Kambari ($17, 2.500+ verkopen, 3 maanden), Blaze AutoPose ($40, 400+, 2 maanden), Forge CAD van Ogunsola Omololu ($49, 300+, 4 maanden), Metalworks van Lazy3D ($30, 400+, 3 maanden), Nitro Retopo ($25, 300+, 2 maanden). Hulpagent zag ook Adaptive Auto Skinning van Jessy Leite ($35, 800+, 4 maanden). Of dit allemaal kleine makers zijn heb ik niet per maker nagegaan; de meesten hebben 1 tot 5 producten.
- **Samen:** de betaalde add-ons uit de steekproef (een derde van het aanbod) halen samen ±$36.000 netto per maand (GOK op GEZIEN). Voor alle nieuwe add-ons van die maanden dus ±$100.000 per maand.
- **Wat makers zeggen (DERDEN):** een maker op BlenderArtists (22 mrt 2026): ±$30 per maand, en meer dan $150 is bij makers die hij kent een uitzondering (https://blenderartists.org/t/superhive-changes/1634680/171). Dat past bij de mediaan: de meeste verkopen bijna niets, een kleine groep veel.
- **Afdracht (DERDEN):** maker houdt 70% (gratis plan), 80% (Pro, $49 per maand) of 90% (Ultimate, $199 per maand), plus $0,49 per verkoop en 4 tot 5,5% betaalkosten (https://superhivemarket.com/pricing).
- **Gumroad (DERDEN, hulpagent):** 2.848 resultaten voor "blender addon", maar bijna geen tellers en geen datums. Niet bruikbaar als meting.

### Bereik (GEZIEN, meting 6 nov)
- Gratis add-ons op extensions.blender.org van mei tot aug 2026: ±1.000 tot 1.500 downloads, elke add-on 100+. Daar mag niets betaald worden en geen reclame voor een betaalde versie in Blender (DERDEN, voorwaarden 10 aug 2026, https://extensions.blender.org/terms-of-service/).

### Drukte (GOK op GEZIEN)
- ±190 nieuwe add-ons per maand op Superhive (375 in een derde van ±6 maanden; met presets en theme-packages ±215). Grote veelmakers bestaan (Tachyon Studio 10 in de steekproef, dus ±30 in 6 maanden).

### Vindbaarheid (DERDEN en GEZIEN)
- Superhive heeft lijsten op nieuwste, best verkocht en "new and rising" (GEZIEN op de site).
- Sinds 26 mei 2026 werkt Superhive als extensiebron in Blender zelf: kopers installeren en updaten met één klik (https://superhivemarket.com/posts/blender-extension-support-launched-on-superhive).
- Uitverkopen trekken veel: winteruitverkoop 2025 leverde $354.858 voor 1.483 makers in 6 dagen (https://superhivemarket.com/posts/winter-sale-2025-recap).

### Markt (DERDEN)
- 7.500 makers, 60.000+ producten, bijna $50 miljoen uitbetaald in totaal (21 apr 2026, https://superhivemarket.com/posts/we-built-this-together-now-we-need-to-fix-it).
- Verkoop sinds de piek in 2022 vlak of dalend bij bijna alle topverkopers (18 feb 2026, https://autotroph.com/the-blender-creator-economy-is-breaking-lets-start-talking-about-it). Een gevestigde maker meldt elk jaar 50% minder sinds 2023.

## Voor
- Eerste platform waar ik verkopen van nieuwe betaalde producten zelf kon tellen, en ze zijn er: ±1 op de 3 verkoopt 10+, ±1 op de 14 verkoopt 100+ in een paar maanden. Op Polymart, Unity en Fab was dat bijna nul.
- Eenmalige prijs, geen abonnement nodig, dus geen backend of licentieserver.
- Twee routes naast elkaar: gratis versie op extensions.blender.org voor bereik, betaalde versie op Superhive voor geld (wel zonder reclame in Blender zelf).
- Winnaars zijn technische hulpmiddelen (retopologie, rigging, CAD, modelleren). Dat is code, wat wij goed kunnen.

## Tegen
- De mediaan is onder 10 verkopen: een gemiddelde add-on levert niets op. We hebben een uitschieter nodig, net als op JetBrains.
- De markt krimpt sinds 2022 en de uitverkopen drukken de prijs.
- Python en 3D: we moeten Blender in GitHub Actions kunnen draaien om te testen (Blender heeft een headless modus, dus dat kan waarschijnlijk, GOK).
- Superhive vraagt een makeraccount en uitbetaling: stap voor Thijs.
- 70% op het gratis plan is minder dan JetBrains (85%).
- De bedragen blijven GOK zolang bundels, gratis codes en kortingen niet zijn uitgesloten.

## Eerste idee
Eén betaalde add-on van $15 tot $30 in een categorie waar nieuwe makers nu winnen (modelleren, retopologie, rigging, CAD-achtig precisiewerk), met een kleine gratis versie op extensions.blender.org. Eerst uitzoeken wat Blender-gebruikers missen: lees de best verkochte nieuwe add-ons en hun reacties, en de wensen op BlenderArtists en devtalk.

## Wat het oordeel nog kan veranderen
- Superhive telt misschien verkopen in bundels of gratis codes mee (MatKit gaf een code voor $0). Dan zijn de cijfers te hoog. Controle: een maker vragen of zelf een product plaatsen.
- Een tweede meting over 4 weken met dezelfde scripts laat zien hoe snel de tellers stijgen.

## Eerdere versie (6 nov)
Advies ja als test, daarna door Hans op nog niet klaar (5) gezet: bereik gemeten (±1.000 tot 1.500 downloads, GEZIEN), geld niet. Controleur 7 nov: akkoord, 10 correcties verwerkt.
