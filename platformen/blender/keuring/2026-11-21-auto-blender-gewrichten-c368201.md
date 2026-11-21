# Keuring blender-gewrichten direct-zip met Pro-knoppen op slot, 21-11-2026, automatische keurder
Wat ik keurde: commits 6b8b254..c368201 (c368201fa), zes bestanden onder producten/blender-gewrichten/e2e/
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De extensions-zip blijft gelijk. `maak_zip.sh` heeft alleen een extra tak `direct`, en `toets_direct_zip.py` controleert die zip op "Pro" en op het ontbreken van `direct.py`. | Feit (uit de tekst van script en toets) | hoog | Een groene run van `toets_direct_zip.py` met de echte zips. Die staat niet in de wijziging. |
| 2 | De direct-zip is de gratis zip plus `direct.py`, en `__init__.py` is gelijk aan de gratis versie plus het fragment. De toets vergelijkt dat byte voor byte. Er zit geen `betaald/` in. | Feit (opzet), werking op de echte zip is vermoeden | midden | Een run van `toets_direct_zip.py` en `test_direct.py` in Blender 4.2 en 5.2. |
| 3 | Geen enkele run, log of run-id is genoemd. Er is ook geen workflowbestand gewijzigd. Of de drie nieuwe toetsen automatisch draaien is dus niet te zien. | Vermoeden | midden | Een groene run-id die de regels `[cj-direct]` en `[cj-direct-zip]` toont, of een workflow die ze aanroept. |
| 4 | Het slotvenster en de plek van de knoppen "boven Report a problem" zijn alleen gedekt door code en een schermscript. Of het er goed uitziet kan ik niet zien. `d2-venster` mag volgens het script zelfs mislukken. | Vermoeden | laag | De plaatjes `d1-slot-paneel` en `d2-venster-paneel`, bekeken door Daan of Iris. |
| 5 | De namen "Figure from rig", "Hinge with end stop" en "Body-part presets" moeten kloppen met wat Pro 1.0.2 echt kan. In het zichtbare ontwerp staan scharnier met eindstop en alle ledematen in één keer. "Body-part presets" zie ik daar niet. | Vermoeden | midden | Een vergelijking met de functielijst van Pro op Superhive of de productpagina. |
| 6 | De link gaat naar dezelfde pagina als de gratis productpagina, `dortus.com/click-joints/`. Het ontwerp zegt dat die pagina alleen de gratis functies toont. Of een klik op "See Click Joints Pro" daar echt Pro laat zien, is onbekend. | Vermoeden | midden | De live pagina lezen met `curl` en kijken of Pro en een koplink erop staan. |
| 7 | Er is alleen getest met één geïnstalleerde zip. Pro heeft dezelfde paneelnaam `CLICK_JOINTS_PT_paneel`. Wie Pro en de direct-zip allebei installeert, kan een botsing krijgen of zelf slotjes zien. | Vermoeden | laag | Een proef waarbij Pro en de direct-zip samen in Blender staan. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is niet meegewijzigd. Er is toch een derde build (`direct`), een nieuw onderdeel `direct.py` met een paneelhaak en een nieuwe toetsset bijgekomen. | Feit (niet in de lijst met gewijzigde bestanden) | hoog | architectuur.md bijgewerkt |
| 2 | Alle nieuwe bestanden zijn kort, ruim onder de 400 regels. | Feit | hoog | Bestanden onder ±400 regels |
| 3 | Er is geen bestaande toets aangepast. Alle toetsen zijn nieuw. | Feit | hoog | Tests niet aangepast om te slagen |
| 4 | Er staan geen persoonsgegevens of sleutels in de wijziging. De add-on opent alleen een link na een klik van de gebruiker. | Feit | hoog | Geen persoonsgegevens |
| 5 | Er staat geen prijs in de add-on, en dat wordt getoetst. Er is geen speltekst, AI-beeld of AI-geluid. | Feit | hoog | Cijfers en Steam-regels, niet van toepassing |
| 6 | De direct-zip is bedoeld voor dortus.com en GitHub, niet voor extensions.blender.org. Het manifest en de versie zijn gelijk aan de gratis zip. Een verkeerde upload is dus niet te onderscheiden en zou regel 3.3 en 3.10 van extensions.blender.org breken. Alleen de bestandsnaam en een commentaar in het script waarschuwen ervoor. | Vermoeden | midden | Regels van extensions.blender.org |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Drie slotknoppen plus "Upgrade to Pro" zijn vier dingen in het gratis paneel die allemaal naar dezelfde plek leiden. Dat kan als reclame aanvoelen. | Eén blok met slotjes en één link. Of de regel "Upgrade to Pro" weglaten. | klein |
| 2 | Het venstertje zegt alleen "This is in Click Joints Pro". Het zegt niet wat de functie doet, dus de klik levert niets op. | Eén regel per functie, bijvoorbeeld wat het scharnier met eindstop oplost. | klein |
| 3 | Een knop met slot die een venster opent met nog een knop is twee klikken voor één link. | De slotknop opent direct de link, met de uitleg in de tooltip. | klein |
| 4 | "Body-part presets" is vaag voor een koper. | Een duidelijkere naam, bijvoorbeeld "All limbs in one go", in lijn met de Pro-pagina. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Werk `architectuur.md` bij met de directe build, `direct.py` en `init_direct.py`, de paneelhaak en de drie toetsen (Deel B 1).

**Kan**
1. Noem een groene run-id of koppel de drie nieuwe toetsen aan een workflow, zodat te zien is dat ze draaien (Deel A 3).
2. Laat Daan of Iris de schermen d1 en d2 bekijken, en kijk of de Pro-link op `dortus.com/click-joints/` echt Pro laat zien (Deel A 4 en 6).
3. Controleer de functienamen van de slotknoppen tegen Pro 1.0.2 (Deel A 5).
4. Zorg dat de direct-zip niet per ongeluk bij extensions.blender.org terechtkomt, bijvoorbeeld met een eigen versie-achtervoegsel of een vaste uploadcontrole (Deel B 6).
5. Test wat er gebeurt als Pro en de direct-zip samen geïnstalleerd zijn (Deel A 7).
6. Houd de slotknoppen korter en bruikbaarder (Deel C 1 tot 4).

---
Automatische keurder, model `claude-sonnet-5-5`, 24930 tokens in, 5579 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
