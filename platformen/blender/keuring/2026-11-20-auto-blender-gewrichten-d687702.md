# Keuring blender-gewrichten, 20-11-2026, automatische keurder
Wat ik keurde: commit d687702ce (producten/blender-gewrichten/repo-click-joints/README.md)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De README zegt nu "in Blender 4.5 or newer". Het ontwerp zegt 4.2 LTS tot 5.2 LTS, en Pro 1.0.0 draaide groen in 4.2.23 en 5.2.3. Het is uit de tekst niet te zien of de zin over Pro of over de gratis versie gaat. | Vermoeden | Midden | Het `blender_manifest.toml` van Pro (veld `blender_version_min`) en de laatste testrun. Staat daar 4.2, dan klopt de README niet. |
| 2 | Nieuwe belofte: "A joint that does not fit is skipped, and the list says why." Dit hoort bij de alle-ledematen-functie van Pro. De tekst die ik zie toont niet dat dit zo werkt. | Vermoeden | Midden | Een Pro-test of schermafbeelding van de lijst met een overgeslagen gewricht en de reden erbij. |
| 3 | Nieuwe beweringen: de gratis versie en Pro kunnen niet tegelijk aan staan, en Pro staat op Superhive met eigen prijs en updatevoorwaarden. De eerste is niet in de changelog of in `architectuur.md` te vinden. De tweede is een eerlijke verduidelijking. | Vermoeden | Midden | Een test die beide extensies tegelijk aanzet, of de plek in de code waar dat botst. |
| 4 | De prijzen $19 en $59 staan nu alleen bij Gumroad. In het ontwerp staat nog $12 (lanceerprijs $9) voor Pro. Dat lijkt verouderd, maar ik kan het niet nagaan. | Vermoeden | Laag | Het besluit of de winkelpagina van Pro met de huidige prijs. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alleen `README.md` in de repo-map is gewijzigd. Er zijn geen tests, code, zips of bestanden van meer dan 400 regels geraakt. | Feit | Hoog | Tests niet aangepast, bestandsgrootte |
| 2 | Ik zie geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. De verkooplinks zijn openbare winkelpagina's. | Feit | Hoog | Geen persoonsgegevens |
| 3 | De README verwijst al naar Pro. Dit is de repo-README en niet de beschrijving op extensions.blender.org, dus regel 3.3, 3.10 en 6.1 raken dit niet direct. Staat deze README ook in de extensie-zip of op de listing, dan wel. | Vermoeden | Midden | extensions.blender.org 3.3, 3.10, 6.1, ToS 6.2 |
| 4 | De README zegt "not print tested by us yet: print a test joint first". Dat is eerlijk en past bij de handmatige proef die nog openstaat. | Feit | Hoog | Cijfers eerlijk (GEZIEN/DERDEN/GOK) |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Het advies om eerst een testgewricht te printen en de waarschuwing dat de twee add-ons niet samen aan kunnen staan voorkomen verwarring. Ik kan niet zien hoe het eruitziet. | Zet de waarschuwing over niet tegelijk aanzetten vetgedrukt of op een eigen regel, zodat die niet verdwijnt in een lange alinea. | klein |
| 2 | De alinea over Pro is lang geworden: eisen, overslaan, conflict en prijs staan door elkaar. | Splits in twee korte alinea's: "Before you buy" en "Price". | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Controleer of "Blender 4.5 or newer" klopt voor Pro en voor de gratis versie, en pas de zin aan als de ondergrens 4.2 is (A1).
- Leg het niet tegelijk aan kunnen staan vast in de changelog of `architectuur.md`, met de test of code als bron (A3).
- Controleer de prijzen $19 en $59 tegen het huidige besluit. Het ontwerp noemt nog $12 (A4).
- Controleer dat deze README niet in de extensions.blender.org-zip of listing terechtkomt (B3).
- Daan of Thijs kijken de lay-out van de README na (C1 en C2). Dat kan ik niet zien.

---
Automatische keurder, model `claude-sonnet-5-5`, 17665 tokens in, 2940 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
