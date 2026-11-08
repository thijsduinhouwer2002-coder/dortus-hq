# Voorstel: Roblox UGC, avatar-items in de Marketplace

Vera, 8 nov 2026, run 17:33 (Amsterdam), tweede platform van de run. Controleur akkoord met het oordeel, 4 correcties verwerkt.

## Kort
**Advies: nee voor nu. Cijfer 3.**
Het grootste geld van alle avatar-winkels (Roblox betaalde makers samen meer dan $1 miljard in 2025, DERDEN), maar voor een nieuwe maker een van de drukste plekken die ik mat: alleen al ±700 tot 1.000 nieuwe accessoires per dag. Een maker krijgt minstens 30% van een item van ±90 Robux (mediaan betaald), dus ±$0,10 per verkoop; voor $300 per maand zijn ±2.900 verkopen per maand nodig (minder bij een hogere prijs in de Marketplace, tot 70%). Uploaden vraagt verificatie met het identiteitsbewijs van de maker (dat kan alleen Thijs, en het geeft ons account een persoon als gezicht) plus vooraf Robux per item. En wat wij kunnen (software) is hier niet wat verkoopt: het zijn 3D-kleding en accessoires.

## Hoe gemeten
- Open catalogus-API `catalog.roblox.com/v2/search/items/details` (geen inlog, 2 s tussen verzoeken). robots.txt van roblox.com verbiedt /catalog/contents en /catalog/html, niet deze API; catalog.roblox.com heeft geen robots.txt (geeft een API-fout).
- Per item: aanmaakdatum (itemCreatedUtc), prijs, favorieten (favoriteCount), maker. **Geen verkoopaantallen**; die ziet alleen de maker zelf.
- De lijst "nieuwste" stopt na 1.000 items, dus een oud cohort is niet rechtstreeks te halen. Daarom: uit de 1.000 nieuwste accessoires 60 willekeurige makers getrokken en van elk alle items tot april 2026 opgehaald.
- Scripts en data: `data/roblox-ugc-nieuwste-script.py`, `data/roblox-ugc-makers-script.py`, `data/roblox-ugc-nieuwste-2026-11-08.json`, `data/roblox-ugc-60makers-2026-11-08.json`, `data/roblox-ugc-bestsellers-2026-11-08.json`.

## Cijfers
**Drukte**
- GEZIEN: van de 1.000 nieuwste accessoires zijn er 693 van 8 nov (in ±15,6 uur, tot 15:38 UTC) en 167 van 7 nov. De lijst is niet netjes op aanmaakdatum gesorteerd (±140 items van 29 jul t/m 6 nov ertussen), dus ±700 tot 1.000 per dag is een schatting van de orde van grootte, alleen in deze ene categorie. 272 makers in die 1.000; 79% van de makers en 91% van de items zijn groepen (studio's).

**Bereik (favorieten, geen verkoop)**
- GEZIEN: van de 60 makers hadden minstens 39 items uit mei t/m aug 2026: minstens 2.089 items, waarvan 1.627 betaald. Ondergrens: het script haalt per maker hooguit 480 items, en bij 3 drukke makers (rosepath, CyberTrouble, True Villain!) mist daardoor (een deel van) het cohort.
- GEZIEN: favorieten van die betaalde items: mediaan 5, 75% onder 21, 90% onder 120; 179 (11%) met 100+, 30 met 1.000+, max 38.340.
- Let op: dit zijn makers die nu nog actief zijn (overlevers), dus het echte beeld voor een nieuwe maker is slechter. Favorieten zijn geen verkopen; de verhouding is onbekend.
- GEZIEN: de bestsellerlijst van accessoires (top ±1.000) is van oud werk: 379 van Roblox zelf, 252 uit 2023, maar 38 uit 2026 en 4 uit mei of later (van 2 makers, waarvan één Roblox zelf). Nieuw werk breekt daar nauwelijks door.

**Geld**
- GEZIEN (create.roblox.com/docs/marketplace/marketplace-fees-and-commissions): maker krijgt 30%, bij verkoop in een spel krijgt de spel-eigenaar 40%. In de Marketplace stijgt het aandeel als de prijs hoger is dan de bodemprijs (2x de bodem 50%, 6x of meer 70%). 30 dagen wachttijd per aankoop.
- GEZIEN (zelfde pagina): uploaden vraagt verificatie met een eigen identiteitsbewijs van de overheid, 80 Robux per upload, en een voorschot bij publiceren dat je alleen terugkrijgt uit verkopen (bijvoorbeeld hoed 1.500, kleding 600 Robux).
- GEZIEN: mediaanprijs van de nieuwe betaalde accessoires 90 Robux (75 met gratis items erbij). Bij 30% en $0,0038 per Robux is dat ±$0,10 per verkoop. In een spel blijft het altijd 30%.
- DERDEN (rowatcher.com, inside-roblox-s-ugc-economy-who-s-winning-in-2026; site lijkt deels automatisch geschreven en noemt 70% als standaard, wat niet klopt met de officiële pagina): DevEx $0,0038 per Robux sinds sep 2025, uitbetalingen aan alle makers samen boven $1 miljard in 2025, mediane DevEx-deelnemer ±$1.575 per jaar. Inwisselen pas vanaf 30.000 verdiende Robux.

## Voor en tegen
Voor:
- Enorm publiek en echt geld aan de top; open voor iedereen sinds 2024.
- Datum, prijs en favorieten per item zijn open te meten; herhaalmeting kan.

Tegen:
- Extreem druk; bestsellers zijn oud werk en van Roblox zelf.
- Per verkoop centen; geld zit bij grote studio's en Limiteds.
- Identiteitsbewijs van Thijs nodig en Robux vooraf per item.
- Het is 3D-kunst en mode, niet software. Roblox-plugins (wel software) zijn al gemeten: cijfer 4 (zie onderzocht.md).

## Wat we zouden bouwen (als het ooit ja wordt)
Een reeks accessoires uit Blender (het werk van Bram) in een niche met weinig aanbod. Maar met ±1.000 nieuwe per dag verwacht ik dat dat verdrinkt.

## Wat het oordeel kan veranderen
- Een openbare bron met verkopen per nieuw item (bijvoorbeeld een externe tracker met eerlijke steekproef).
- Herhaalmeting: over 4 weken dezelfde 60 makers opnieuw (data/roblox-ugc-makers-script.py) en kijken hoe hard de favorieten van de lichting sep en okt groeien.
