# Keuring blender-gewrichten, terugval naar Exact in Pro, 23-11-2026, automatische keurder
Wat ik keurde: commits 02ac53f..542c4be (542c4befa), alleen de tekst van de wijziging
Akkoord: nee

## Deel A: doet het wat beloofd is?
(De opdracht is hier de commitbeschrijving: gratis deel terug op 014172e, terugval naar Exact alleen in Pro. Het ontwerp zelf noemt de terugval niet.)

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De terugval zit nu in `betaald/terugval.py` als omhulling om `gewricht.snij`. De terugval en het opruimen van de eerste snede verdwijnen uit de operator. | Feit | Hoog | Het diff laat de verplaatsing zien. |
| 2 | De omhulling zet voor de tweede snede alleen `een_lid.STAND["solver"]` en leegt `bronnen`. De oude code riep `een_lid.bereid(...)` opnieuw aan met Exact. Of de hulpvormen nu goed voor Exact zijn opgebouwd, is uit de tekst niet te zien. | Vermoeden | Midden | Een groene run met `FORCEER_OPEN=1` op de Pro-zip, met `TERUGVAL`-regels in het log (twee gesloten delen, geen hulpresten). |
| 3 | Na de terugval krijgen de delen `cj_solver_terugval`. Een nieuwe waarde voor `cj_solver` wordt nergens gezet. Het oude `gegevens["cj_solver"] = solver_nu` is uit de operator weg. De delen kunnen dus "MANIFOLD" melden terwijl Exact is gebruikt. | Vermoeden | Midden | Een controle in de toets dat `cj_solver` na de terugval "EXACT" is. |
| 4 | Registratievolgorde klopt: `terugval` komt na `snippers` en dus buitenom. `unregister` draait in omgekeerde volgorde en herstelt `gewricht.snij` alleen als het nog de eigen omhulling is. | Feit | Hoog | Het diff laat dit zien. |
| 5 | Dat het gratis deel nu byte voor byte gelijk is aan 014172e staat alleen in de commitbeschrijving. Het diff van `gewricht.py` ziet er daarmee consistent uit. | Vermoeden | Midden | `e2e/toets_zips.py` groen op deze commit. |
| 6 | Er is geen testuitslag bij deze wijziging. De nieuwe toets slaat zichzelf over op de gratis zip en op Blender zonder Manifold, dus hij draait alleen op de Pro-zip met 4.5 of nieuwer. | Feit | Hoog | Een run op 5.2.3 met de Pro-zip. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toets is verzwakt. Het geval "2 keer open: netjes weigeren, figuur heel" is weg. De controle `cj_solver == "EXACT"` is weg. Er is een nieuw geval 0 bijgekomen. Met de nieuwe opzet kan 2x open niet nagebootst worden, omdat de omhulling maar één keer forceert. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Er is een nieuw bestand `betaald/terugval.py`, maar `architectuur.md` staat niet bij de gewijzigde bestanden. Het nieuwe Pro-onderdeel en de verplaatste terugval zijn dus niet beschreven. | Feit (dat de wijziging ontbreekt) | Midden | architectuur.md bijgewerkt |
| 3 | `CHANGELOG.md` mist terecht de gratis regel over de terugval. Er is geen Pro-regel voor in de plaats. Of Pro een eigen changelog heeft, is uit de tekst niet te zien. | Vermoeden | Laag | Changelog per versie |
| 4 | Het nieuwe bestand is 64 regels. De grens van ±400 regels voor `gewricht.py` is niet te controleren, maar het bestand wordt kleiner. | Feit | Hoog | Bestanden onder ±400 regels |
| 5 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. De naam "Olaf" in een commentaar is een voornaam, geen gegevens. | Feit | Hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
(Er is niets te zien of te spelen, dus dit zijn vermoedens uit de tekst.)

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Gratis gebruikers krijgen de verbetering niet. Blijft de fout "no watertight parts" bij een bijna-platte driehoek bestaan, dan loopt de gratis gebruiker er tegenaan en de Pro-gebruiker niet. Dat voelt als een fout die achter een betaalmuur zit. | Beslissen of de terugval ook gratis hoort. Dan wel via de gewone keuring van het gratis deel. | Klein |
| 2 | Een Pro-gebruiker merkt van de terugval niets, alleen een eigenschap op het deel. | Eventueel een korte melding zoals "Retried with the Exact solver" als de terugval is gebruikt. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. De toets is verzwakt en de metadata klopt mogelijk niet meer (A3, B1). Zet na de terugval `cj_solver` op "EXACT" in `terugval.py`. Toets dat in `solver_terugval`, zoals de oude toets deed. Leg ook vast hoe het weigeren na een mislukte tweede snede getoetst wordt, of zeg uitdrukkelijk dat dat geval vervalt.
2. Laat een groene run zien op de Pro-zip met Manifold (5.2.3) waarin `TERUGVAL 1x open` twee gesloten delen geeft zonder hulpresten (A2, A6). Zonder dat is niet te zien dat de tweede snede zonder `een_lid.bereid` goed werkt.

**Kan**
- Werk `architectuur.md` bij: `betaald/terugval.py`, de volgorde ten opzichte van `snippers`, en dat de terugval niet meer in het gratis `gewricht.py` zit (B2).
- Zet een regel in de Pro-changelog als die er is (B3).
- Draai `toets_zips.py` en meld de uitslag, als bewijs dat het gratis deel gelijk is aan 014172e (A5).
- Overweeg een melding aan de gebruiker bij de terugval, en beslis of de gratis versie de fix later ook krijgt (C1, C2).

---
Automatische keurder, model `claude-sonnet-5-5`, 22473 tokens in, 5891 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
