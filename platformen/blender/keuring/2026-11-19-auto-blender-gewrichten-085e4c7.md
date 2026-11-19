# Keuring Fit test strip (Click Joints Pro), 19-11-2026, automatische keurder
Wat ik keurde: commit 085e4c72f (tak met 1f63c27..085e4c7), drie bestanden: `betaald/__init__.py`, `betaald/testkaart.py`, `e2e/toetsen_testkaart.py`
Akkoord: nee

## Deel A: doet het wat beloofd is?
Getoetst tegen de belofte in `ontwerp.md`: "printerprofielen met een testkaartje (print vijf spelingen, kies welke klikt)". Het ontwerp `platformen/blender-2/testkaart-ontwerp.md` is niet meegestuurd en kon ik niet lezen.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De code maakt vijf staafjes bij 0.10, 0.15, 0.20, 0.25 en 0.30 mm in een eigen collectie "Fit test", met het getal in reliëf op het bovenste deel. Dat past bij de belofte. Alles staat in `betaald/`, dus de gratis zip blijft zonder dit. | Feit | Hoog | Staat in de diff. |
| 2 | Er is geen uitslag van een run meegestuurd. Of `toetsen_testkaart.py` groen is in 4.2 en 5.2 weet ik niet. Ook niet of het getal op het scharnier nu gesloten blijft. | Vermoeden | Hoog (dat ik het niet weet) | Een groene run van deze toets met de Pro-zip, in het log "KLAAR 0 FOUT". |
| 3 | Bij het terugzetten komt `kogel_mm` als laatste in de lijst. Volgens `architectuur.md` zet een nieuwe waarde van `kogel_mm` via de update de knop Auto uit. Daardoor kan Auto na een klik op de testknop uit staan, terwijl de code belooft dat alles terugkomt zoals het was. | Vermoeden | Midden | In de toets na de klik `kogel_auto` en `kogel_mm` vergelijken met de beginstand, met Auto aan. Of `kogel_mm` vóór `kogel_auto` terugzetten. |
| 4 | De toets importeert `bl_ext.user_default.click_joints.eigenschappen`, maar installeert de betaalde zip. Heeft de Pro-extensie een andere id, dan crasht `figuren_u()` met ModuleNotFoundError. | Vermoeden | Laag tot midden | De run, of de id in het Pro-manifest. |
| 5 | De toets gebruikt `figuren.mm_scene`, `figuren.staaf`, `figuren.meter_scene`, `inst.formaat`, `exportmap`, `exporteer` en `cj_laatste_export`. Die staan niet in deze wijziging. Ze bestaan vermoedelijk al. | Vermoeden | Midden | De run. |
| 6 | "De add-on onthoudt het per printer" uit het ontwerp zit niet in deze wijziging. Er wordt hier niets over beloofd, maar het Pro-testkaartje is dus nog niet af. | Feit | Hoog | Het testkaart-ontwerp. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is niet bijgewerkt. De nieuwe module `testkaart.py`, de knop en de aanpassing in `betaald/__init__.py` staan er niet in. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | `testkaart.py` is 197 regels en de toets 165 regels. | Feit | Hoog | Bestanden onder ±400 regels: voldaan |
| 3 | Het is een nieuwe toets. Bestaande toetsen zijn niet aangepast. | Feit | Hoog | Tests niet aangepast om te slagen: voldaan |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens: voldaan |
| 5 | Het nieuwe bestand staat in `betaald/`. Of de gratis zip het nog steeds niet bevat, bewijst alleen `e2e/toets_zips.py`. | Vermoeden | Midden | Groene run van `toets_zips.py`. |
| 6 | Er is geen workflowbestand gewijzigd. Of `toetsen_testkaart.py` automatisch draait, is uit deze tekst niet te zien. | Vermoeden | Midden | Een regel in een workflow die de toets aanroept. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen beeld en kan niets spelen. Dit is een oordeel op de tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Alleen het bovenste deel krijgt het getal. Na het printen liggen er tien losse stukjes en is niet te zien welk onderste deel bij welk getal hoort. Daan wilde dat de strip het mooiste deel van het product werd. | Het getal ook op het onderste deel, of op beide delen een kleine merkstip. | Klein |
| 2 | Het tekstvak "Print this first: five joints from 0.10 to 0.30 mm" is lang voor de smalle zijbalk. Het wordt vermoedelijk afgekapt. De knoppen "Fit test: ball" en "Fit test: hinge" naast elkaar hebben hetzelfde risico. | Een kortere regel ("Print this first") en de uitleg in de knoptip. Bekijk het op een schermafbeelding in Blender. | Klein |
| 3 | Bij vijf staafjes van 20 mm breed en 60 mm lang wordt de strip ongeveer 140 mm breed. Ze liggen los, niet aan een plaatje of lijn. Dat is vermoedelijk onhandig op een kleine printer. | Een kleinere variant, of de staafjes korter. Of een lage plaat eronder voor één printtaak. | Midden |
| 4 | De uitleg ("Print all five. Use the clearance of the one that turns without wobble.") staat alleen in een melding die snel verdwijnt. | De uitleg vast in het paneel, onder de knop. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. `architectuur.md` bijwerken met `betaald/testkaart.py` en de knop in het Pro-paneel (Deel B, 1).

**Kan**
1. Controleren of `kogel_auto` na een klik op de testknop weer aan staat, en zo nodig de terugzetvolgorde aanpassen. Een toetsregel erbij (Deel A, 3).
2. De groene run van `toetsen_testkaart.py` en `toets_zips.py` tonen. Laten zien dat de toets in een workflow draait (Deel A, 2 en 4; Deel B, 5 en 6).
3. Het getal ook op het onderste deel zetten (Deel C, 1). De tekst in het paneel inkorten (Deel C, 2).

---
Automatische keurder, model `claude-sonnet-5-5`, 25798 tokens in, 7669 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
