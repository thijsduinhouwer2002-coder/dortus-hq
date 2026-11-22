# DaVinci Resolve (sjablonen, Fusion-plugins, DCTL, LUT's)

Vera, 15 nov 2026 run 08:31 (Amsterdam). Advies: **nee voor nu. Cijfer 3.**

## Wat het is
DaVinci Resolve is de videobewerker van Blackmagic Design, met een gratis versie en een betaalde Studio-versie (eenmalig). Er is **geen officiële winkel** voor makers. Kleine makers verkopen Fusion-sjablonen en macro's, Fuses (kleine plugins in code), DCTL-kleurfilters, PowerGrades, LUT's en een enkele OpenFX-plugin via Gumroad, hun eigen site en YouTube. Waarom ik keek: veel gebruikers, nooit bekeken, en Fuses en DCTL zijn code die wij kunnen schrijven en op Linux kunnen testen (Resolve draait op Linux).

## Eigen meting (GEZIEN, 15 nov 2026)
Bron: de open zoek-API van Gumroad (`gumroad.com/products/search`), dezelfde methode als bij Gumroad Discover en audio-plugins. Script en ruwe data in `data/davinci-gumroad-*`.

- **Aanbod.** Zoektermen "davinci resolve" (2.162 producten), "davinci" (2.283), "davinci resolve lut" (825), "resolve template" (681), "fusion template" (231), "powergrade" (219), "resolve plugin" (209), "dctl" (67), "fusion macro" (27). Per term de 1.500 nieuwste opgehaald. Na filteren op naam (resolve, davinci, dctl, fusion, powergrade, lut): **1.447 producten van 508 makers, waarvan 1.165 betaald**, mediaanprijs $15.
- **Hoeveel verkopen ze.** Ratings als maat (eerdere meting: ±1 rating op 19 betaalde verkopen, zie voorstellen/gumroad-discover.md). Van de 1.165 betaalde producten:
  - minstens 1 rating: 495 (42%);
  - 5 of meer: 136 (12%);
  - 20 of meer: 24 (2,1%), dus naar schatting ±400 verkopen of meer;
  - 50 of meer: 2 (0,2%); 100 of meer: geen.
  - Kanttekening: de 1.500-grens per term kan een paar oude toppers missen. De lijst "featured" (omzet laatste 3 maanden) laat dezelfde orde zien: bovenaan 0 tot 38 ratings, met één gratis-achtig pakket van $8 met 224.
- **Nieuwkomers ("hot and new", jonger dan 90 dagen, met minstens één verkoop):** 234 producten van 102 makers over alle termen. Mediaan 0 ratings, 73 met 1 of meer, 11 met 5 of meer, 3 met 20 of meer (een LUT-pakket van $10, een "neurocognitief" pakket dat niets met Resolve te maken heeft, en een gratis Blender-tool). Het beste echte Resolve-gereedschap: PinchFlow 2.0 ($8, 14 ratings, dus GOK ±250 verkopen, ±$2.000 in 3 maanden) en SpectraLab ($56, 12 ratings).
- **Wat er verkoopt.** Van de 234 nieuwkomers: 64 LUT-pakketten, 44 sjablonen en macro's, 13 plugins of scripts, 10 PowerGrades, 9 DCTL, de rest overig. LUT's zijn een vloed van gelijke pakketten (één verkoper heeft er 121, een ander 91).
- **Code-makers bestaan en verdienen iets.** Tangenten (Fusion-gereedschap, Puppet Pin $37 met 38 ratings, GOK ±700 verkopen, ±$25.000 in totaal), Akascape (±40 Fuses, de betaalde met 0 tot 17 ratings, GOK ±$500 tot $1.000 per maand), JUNE (Fusion-effecten, Depth of Field 30 ratings), reveace (EaseSpline 11). En een AI-plugin: AI Video Studio V.3 ($59, 33 ratings, bovenaan "featured"), die AI-video maakt binnen Resolve met eigen API-sleutels. Dit zijn echte kleine makers met echte verkopen, maar de bedragen zijn klein en ze halen hun klanten vooral via YouTube en eigen communities (Skool, Discord), niet via een winkel.
- **Patreon (graphtreon, 10 Resolve-makers op naam):** bijna allemaal 0 tot $30 per maand, de hoogste Hen_Colorist ±$94 tot $375. Abonnementen zijn hier niet de geldroute.

## Bronnen van derden
- Resolve 21 (juni 2026) kreeg een Photo-pagina; 21.1 (8 sep 2026) kreeg presets in de Inspector, een MCP-server in Studio en 20 nieuwe API's (DERDEN, digitalproduction.com/2026/09/08/resolve-21-1-adds-mcp-and-finally-gets-presets/).
- **Belangrijk voor ons:** sinds 21.1 vragen externe scripts, Workflow Integrations en de UIManager (scripts met een eigen venster) de betaalde Studio-versie. In de gratis versie kan alleen nog via de console gescript worden. Blackmagic zegt dat de Python-API misbruikt werd om Studio-functies vrij te spelen (DERDEN, zelfde bron). Hulpprogramma's met een eigen venster verliezen daarmee de grote groep gratis gebruikers. Fuses, DCTL en macro's werken wel in de gratis versie (GOK, niet zelf getest).
- Ingebouwde Inspector-presets maken een deel van de goedkope sjabloonpakketten overbodig (GOK).
- Aantal gebruikers: geen betrouwbaar openbaar getal gevonden. Blackmagic noemt geen aantallen; sites met "statistieken" schrijven elkaar over. Niet meegewogen.

## Wat ik niet kon meten
- **Bereik per product** (installs): er is geen winkel en geen teller. Alleen verkopen via Gumroad-ratings, en dat is maar een deel; veel makers verkopen via een eigen site.
- Hoe snel een nieuwe maker zonder YouTube-kanaal aan zijn eerste verkopen komt. Uit de Gumroad-meting van 9 nov weten we dat Discover pas opengaat na $100 eigen omzet.

## Scores op "Wat een 8 is"
1. Nieuwe kleine makers verdienen aantoonbaar: **zwak.** Er wordt betaald, maar 2% van de betaalde producten haalt ±400 verkopen, en nieuwkomers halen meestal 0 ratings.
2. Bereik voor nieuwkomers: **zwak.** Geen winkel, geen zoekscherm in Resolve. Bereik komt van YouTube-tutorials en eigen communities, iets wat Dortus niet heeft en Thijs niet onder zijn naam wil doen.
3. Bouwen en testen: **redelijk.** Fuses (Lua) en DCTL zijn code; Resolve draait op Linux, op GitHub Actions zonder GPU wordt dat lastig (GOK).
4. Thijs kan binnen een week verkopen: **ja**, via Gumroad of Polar zoals bij Obsidian.

## Voor en nadelen
- Voor: veel gebruikers die gewend zijn voor gereedschap te betalen ($15 tot $60), code-makers bestaan en verdienen, nieuwe MCP-server en AI-trend (AI Video Studio staat bovenaan).
- Tegen: geen winkel en dus geen bereik voor nieuwkomers, LUT- en sjabloonvloed, sinds 21.1 kunnen scripts met een venster alleen nog in Studio, sterke gratis alternatieven (Reactor, Akascape geeft veel gratis weg).

## Wat we er zouden bouwen (als het ooit verandert)
Een paar mooie Fuses rond 3D en beweging (bijvoorbeeld een Blender-naar-Fusion brug, of een effect dat opvalt), gratis plus één betaalde, verkocht via Polar. Alleen zinnig als we eerst bereik hebben, bijvoorbeeld via een eigen YouTube-kanaal van Dortus (niet onder de naam van Thijs).

## Cijfer en advies
**3, nee voor nu.** Er wordt betaald, en er zijn kleine code-makers die iets verdienen, maar zonder winkel komt elk bereik van YouTube en eigen gemeenschap, en de verkopen per product zijn klein (2% boven ±400 verkopen, nieuwkomers meestal nul). Dezelfde vorm als audio-plugins (3) en Gumroad Discover (3). Opnieuw kijken alleen als Blackmagic een eigen winkel of plugin-lijst in Resolve opent.

Geen aparte controleur: het nee hangt aan tellingen die met script en ruwe data in `data/` staan en aan één bron van derden die letterlijk is aangehaald.
