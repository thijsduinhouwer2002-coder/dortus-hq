# Keuring blender-gewrichten, 19-11-2026, automatische keurder
Wat ik keurde: commit 30928065 (bereik 4117cbb..3092806), bestand `producten/blender-gewrichten/e2e/scherm_basis.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen een testhulp voor schermafbeeldingen. De add-on en de beloften in `ontwerp.md` (kniefout 0.1.1 en 1.0.2, Pro 1.0.0) veranderen niet. | Feit (uit de diff) | Hoog | Een diff van `click_joints/` tussen 4117cbb en 3092806 die leeg is. |
| 2 | De commit zegt dat `bpy.ops.screen.screenshot` onder Xvfb een zwart beeld geeft en dat niets dat bestand gebruikte. Het "zwart" kan ik niet uit de tekst halen. Dat niets het gebruikte, ondersteunt de tekst deels: de links in `ontwerp.md` wijzen al naar `...-x.png`. | Vermoeden | Midden | Een zoektocht in workflow en scripts naar de bestandsnamen zonder `-x`, en een kijk op één oud zwart beeld op tak `schermen`. |
| 3 | De toets van de add-on blijft in de diff intact: er is geen controle weggehaald of versoepeld. Alleen het maken van een zwart bestand en de logregel daarover verdwijnen. | Feit | Hoog | Niet van toepassing. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Een uitkomst die niet gebruikt werd, is weggehaald. Een toets op bestaan van het oude `.png` zou nu kunnen falen, maar de diff laat zo'n toets niet zien. | Vermoeden | Midden | Tests niet aangepast om te slagen |
| 2 | Het bestand wordt korter (net 5 regels weg). De bestandsgrootte is niet in de wijziging te zien, maar groeit hier niet. | Feit | Hoog | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Het zichtbare deel noemt dit gedrag niet, en een testhulp verandert de bouw van het product niet. Het afgekapte deel kan ik niet nalezen. | Vermoeden | Midden | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of cijfers zonder GEZIEN, DERDEN of GOK in de diff. Er is ook geen spelerstekst of AI-beeld of -geluid. | Feit | Hoog | Persoonsgegevens, cijfers, Hats, Steam |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zoek in de workflow `.github/workflows/` en in de andere `e2e/`-scripts naar verwijzingen naar de bestandsnamen zonder `-x`, zoals een uploadstap, een bestaanscontrole of een link in het ontwerp. Dat bevestigt de claim "niets gebruikte die versie".
- Leg in `architectuur.md` of in de commit vast dat schermafbeeldingen onder Xvfb alleen via het X-scherm gaan. Dan probeert niemand `screen.screenshot` opnieuw.
- Beeld en speelplezier zijn niet te keuren uit tekst; Daan en Iris blijven daarvoor nodig. Deze wijziging raakt beide niet.

---
Automatische keurder, model `claude-sonnet-5-5`, 17301 tokens in, 2045 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
