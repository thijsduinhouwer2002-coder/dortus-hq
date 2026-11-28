# Keuring blender-gewrichten, kaartnotitie kogel na Shift + rechtsklik (#410), 28-11-2026, automatische keurder
Wat ik keurde: commit 727b32b25, alleen `producten/blender-gewrichten/KAART.md` (een notitie van 2 regels, geen code)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging bevat geen code, alleen de kaartnotitie. De fix zelf (tak `claude/blender-410`, alleen Pro) zit niet in deze diff. Ik keur dus alleen of de notitie netjes en consistent is. | Feit | hoog | De diff toont één gewijzigd bestand. |
| 2 | De notitie zegt dat de kogel op de huid naar het midden schuift en de as langs het lid loopt. Maten en uitslag staan erbij: arm 60 x 36 x 36 mm, been 42 x 42 x 91 mm, beide Good fit. | Vermoeden (alleen het label GEZIEN in de tekst) | midden | De e2e-run 46169569125 en `e2e/toetsen_kogel_huid.py` op de tak. |
| 3 | De oude fout (hele figuur in een voor- en achterhelft gesneden en toch "Good fit") wordt benoemd. Dat is een fout in de passingcontrole, niet alleen in de snede. De notitie zegt niet of de controle zelf is aangepast. | Vermoeden | midden | De tak lezen: geeft de passing nu rood of een melding als de delen veel groter zijn dan het lid? |
| 4 | Het geval "cursor binnen het lid" blijft open en verwijst naar #419. Dat is eerlijk gemeld en valt buiten dit werk. | Feit | hoog | Staat letterlijk in de notitie. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Afmetingen en runs hebben bijna overal een GEZIEN of een nummer. "Kopersreis Iris" heeft geen label, maar het is een herkomst en geen cijfer. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 2 | Of architectuur.md is bijgewerkt voor het nieuwe gedrag (punt naar het midden, as langs het lid), is uit deze diff niet te zien. De tak zit er niet bij. | Vermoeden | laag | architectuur.md bijgewerkt |
| 3 | Of er tests zijn aangepast om te slagen, kan ik niet zien. De notitie noemt een nieuwe toets `toetsen_kogel_huid.py`, wat in de goede richting wijst. | Vermoeden | laag | Tests niet aangepast om te slagen |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | hoog | Geen persoonsgegevens |
| 5 | Geen spelerstekst van Hats, geen AI-beeld of -geluid. | Feit | hoog | Regels Hats en Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Als het punt naar het midden schuift, merkt de gebruiker dat misschien niet. De cursor staat dan ergens anders dan hij had geklikt. | Een korte melding in het paneel, bijvoorbeeld "Moved to the middle of the limb". | klein |
| 2 | Bij een cursor binnen het lid (#419) krijgt een koper nog steeds twee halve figuren. Dat is het eerste wat iemand na een rechtsklik probeert. | #419 vóór of samen met 1.2.10 oplossen, of in het paneel waarschuwen. | midden |

## Deel C: is het goed genoeg?
Niet van toepassing. Deze wijziging bevat geen beeld, video, winkeltekst, spel of site die een klant ziet, dus er is geen cijfer te geven. De beoordeling van het gedrag zelf (keuring Daan #425) staat nog open en blijft nodig voor het uitbrengen.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Bij het samenvoegen van `claude/blender-410` apart keuren, met de code in beeld: is de passingcontrole zelf aangepast, is architectuur.md bijgewerkt en blijven de tests ongewijzigd?
- Een melding in het paneel als het punt naar het midden is verschoven.
- #419 (cursor binnen het lid) niet te lang open laten.
- Daan keurt het gedrag in de viewport (#425), want dat kan ik uit tekst niet beoordelen.

---
Automatische keurder, model `claude-sonnet-5-5`, 18866 tokens in, 2985 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
