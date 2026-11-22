# Voorstel: GDevelop Asset Store (game-sjablonen en asset-packs)

Vera, 8 nov 2026, run 14:33. Zelf toegevoegd. Construct 3 (de andere kleine game-engine met een winkel) is niet te meten: elke pagina, ook robots.txt, geeft een Cloudflare-uitdaging (403). Niet omzeild.

## Wat het is
GDevelop is een open-source game-engine zonder code (events), met een AI-agent erin. De winkel zit in de editor zelf: wie een nieuw spel begint, ziet sjablonen en asset-packs en koopt met één klik. GDevelop rekent af (kaart, PayPal, app-winkels en GDevelop-credits) en betaalt de maker uit. Betaalde abonnees krijgen elke maand 100 tot 1.000 credits die ze in de winkel kunnen uitgeven; ook die verkopen worden de maker in echt geld betaald.

## Cijfers
| Wat | Waarde | Label |
|---|---|---|
| Asset-packs in de winkel | 274, waarvan 232 van derden van 28 makers (11 zijn bundels, 5 van derden) | GEZIEN (api.gdevelop.io/shop/asset-pack) |
| Game-sjablonen | 79, waarvan 69 van derden van 18 makers | GEZIEN (api.gdevelop.io/shop/game-template) |
| Nieuwe sjablonen van derden | 2024: 18, 2025: 15, 2026 tot nu: 31 (sep 6, okt 7, nov al 3) | GEZIEN |
| Nieuwe asset-packs van derden | 2026: 50, waarvan 30 van één maker; sep 13, okt 26 | GEZIEN |
| Concentratie | één maker 103 van 232 packs (44%), één maker 24 van 69 sjablonen | GEZIEN |
| Mediaanprijs | sjablonen $7,49, packs $5,99 (commerciële licentie, één spel); onbeperkte licentie ±4 keer zo duur | GEZIEN |
| Afdracht | na belasting en betaalkosten 60% maker, 40% GDevelop | GEZIEN (wiki, sell-asset-pack-store) |
| Toelating | betaalde producten worden met de hand gekozen door het team, op kwaliteit | GEZIEN (wiki) |
| Uitbetaling Nederland | via Tremendous (cadeaukaart of virtuele Visa), niet Stripe, eens per paar maanden | GEZIEN (wiki) |
| Verkopen per product | nergens openbaar: geen teller, geen reviews in de API of op de pagina | GEZIEN (niet te meten) |
| Kleine makers met geld | VegeTato: volledig inkomen met 22 sjablonen in 3 jaar; Crowbar_Coder (student, weinig programmeerervaring): "dozens of sales with little to no promotion", regelmatig, op itch.io bijna niets | DERDEN (blog GDevelop, 27 mei 2026, zelf geschreven door GDevelop) |
| Gebruikers | Android-app 1M+ downloads; GDevelop zegt zelf miljoenen makers (niet nagekeken) | GEZIEN (Google Play) / GOK |
| AI | GDevelop heeft een MCP-koppeling voor Claude Code (desktop-app, ingelogd). Geen regel tegen AI-werk in de winkelvoorwaarden gevonden; selectie wel met de hand | GEZIEN (wiki, controleur) |

Gemeten met `data/gdevelop-haal-script.py`, ruwe lijst in `data/gdevelop-winkel-2026-11-08.json`.

## Maatstaf
- **Bereik:** niet te meten. Er is geen enkele openbare teller. Het enige teken is dat de winkel in de editor zit en dat er heel weinig aanbod is: wie een platformspel wil maken, ziet een handvol sjablonen, geen duizenden.
- **Geld:** betalen in de winkel werkt, met credits van abonnees als vaste vraag. Eén maker leeft ervan, één student haalt tientallen verkopen per kwartaal. Rekensom (GOK): een sjabloon van $7,49 levert na btw en kosten ±$3,50 tot $4 op; 30 verkopen per kwartaal per sjabloon is ±$40 per maand. VegeTato met 22 sjablonen kan zo op ±$1.000 per maand komen, wat bij "volledig inkomen" past in een land met lage kosten. Geen enkel bedrag is openbaar.
- **Drukte:** heel rustig. ±3 tot 7 nieuwe sjablonen van derden per maand voor de hele winkel. Wel groeiend (2026 is nu al het dubbele van 2025).
- **Vindbaarheid:** in de editor, bij "nieuw project", plus de websitepagina's per sjabloon. GDevelop helpt makers met hun productpagina.
- **Past het bij ons:** goed. Een sjabloon is een GDevelop-project (JSON met events). Met de MCP-koppeling kan Claude events schrijven. Een net, goed becommentarieerd sjabloon (bijvoorbeeld een puzzel- of idle-spel) is in 1 tot 2 weken te maken. Plaatjes moeten van ons zijn of vrij te gebruiken (CC0, zoals Kenney).

## Voordelen
- Weinig concurrentie: 18 sjabloonmakers in totaal. Hier kan Dortus echt een van de grootste makers worden, wat op bijna geen ander gemeten platform kan.
- Winkel in de editor, met abonnee-credits als vaste koopkracht.
- AI-vriendelijk: de engine heeft zelf een AI-agent en een koppeling voor Claude Code.
- Elk sjabloon is een los product; meer sjablonen = meer kans, zoals bij VegeTato.

## Nadelen
- Verkopen nergens te zien. Het geldbewijs is één blog van GDevelop zelf.
- Klein: de hele markt is misschien een paar duizend dollar per maand voor alle derden samen (GOK).
- Selectie met de hand; onbekend hoe het team AI-gemaakte sjablonen beoordeelt. Als we het doen, zeggen we het eerlijk.
- Uitbetaling naar Nederland als cadeaukaart of virtuele Visa via Tremendous, niet op de bank. Lastig voor de boekhouding.
- 40% afdracht.
- Een verkopersaccount en aanmelding moet Thijs doen (inloggen en voorwaarden).

## Eerste idee
Een reeks van 3 tot 5 goed gemaakte sjablonen in genres die nog leeg zijn (bijvoorbeeld 3D, idle, kaartspel, puzzel met leveleditor), met heldere opmerkingen in de events, gratis plaatjes (CC0) en een speelbare demo op gd.games.

## Cijfer en advies
**Cijfer 5. Nog niet klaar.** De beste kans tot nu toe om op een platform een grote speler te worden, en er is betaald worden met echte vraag. Maar het geld is niet gemeten: geen enkele teller, één blog als bewijs, en de markt is klein.

Wat er nog gemeten moet worden:
1. Gedaan in deze run, als vergelijking: VegeTato verkoopt dezelfde sjablonen ook op itch.io, goedkoper ($3,99 tegen $7,49 in GDevelop). Zijn 25 betaalde sjablonen en extensies daar hebben 0 tot 8 ratings, samen ±60 (GEZIEN, 8 nov). Dat past bij wat beide makers zeggen: itch levert weinig op, de winkel in GDevelop is waar het geld zit. Het zegt niets over het bedrag in GDevelop zelf.
2. Hoeveel betalende GDevelop-abonnees er zijn (jaarcijfers of interviews met de oprichter, Florian Rival).
3. Het eerlijkste is een proef: één sjabloon indienen en 2 maanden verkopen tellen. Dat vraagt een account van Thijs; alleen als Hans dat wil.

## Bronnen
- https://api.gdevelop.io/shop/asset-pack en /shop/game-template (gelezen 8 nov 2026)
- https://wiki.gdevelop.io/gdevelop5/community/sell-asset-pack-store/
- https://gdevelop.io/blog/meet-the-creators-publishing-on-the-gdevelop-store
- https://gdevelop.io/game-example/premium/metroidvania-template-f0b026c0-fa57-4d72-aca2-5366721e5517
- https://play.google.com/store/apps/details?id=io.gdevelop.ide

## Controle
Controleur (agent) las alle bronnen opnieuw met curl: 8 van 8 punten klopt. Correcties verwerkt: 11 van de 274 packs zijn bundels; 2 sjablonen hebben alleen een onbeperkte prijs; het volledige inkomen gaat over de grootste verkoper; meer sjablonen in 2026 betekent ook meer concurrentie.
