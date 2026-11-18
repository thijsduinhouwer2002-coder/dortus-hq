# Keuring Bison & Flex kan-punten automatische keurder, 19-11-2026, automatische keurder
Wat ik keurde: commits 10a21ea..8fa9e1f (8fa9e1f6), bestanden `loket/.github/ISSUE_TEMPLATE/bug.yml` en `src/test/kotlin/com/dortus/bisonflex/MeldenTest.kt`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|-----------|-------------------|------------------------------|--------------------------------------|
| 1 | De wijziging raakt geen code van de plugin en geen winkeltekst. De belofte in `ontwerp.md` blijft dus zoals Daan hem op 18 nov goedkeurde. | Feit | hoog | De diff bevat alleen een issue-formulier en een test. |
| 2 | Het bugformulier vraagt nu om naam of gebruikersmap uit paden te halen voordat je een foutmelding plakt, en zegt dat alles openbaar is. Dat past bij de regel over persoonsgegevens. | Feit | hoog | De tekst staat in `bug.yml`. |
| 3 | De test voor "geen gebruikersnaam in het systeem" is nu robuuster voor een ontbrekende of korte gebruikersnaam. Of hij daarmee groen blijft in de CI, kan ik niet zien. | Vermoeden | midden | Een groene run van `MeldenTest` op GitHub Actions bevestigt het. |
| 4 | De commitregel noemt "Obsidian-versie getest". Dat hoort niet bij dit product en staat nergens in de diff. | Vermoeden | laag | Controleren of dit een slordige commitregel is of een ander werkstuk. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|-----------|-------------------|-----------|-------|
| 1 | De test slaat de controle nu over bij een gebruikersnaam korter dan 4 tekens. Dat is een verzwakking, maar een verdedigbare: korte namen geven valse treffers in de tekst van het besturingssysteem. Er staat geen uitleg bij in de code. | Feit | midden | Tests niet aanpassen om te slagen. Kan: voeg een regel commentaar toe met de reden. |
| 2 | Het voorbeeldpad `C:\Users\yourname` is een voorbeeld en geen echte persoon. Er staan geen sleutels of persoonsgegevens in de diff. | Feit | hoog | Geen persoonsgegevens |
| 3 | `architectuur.md` en `CHANGELOG.md` hoeven niet mee te veranderen. Er is geen gedrag of zichtbaar plugin-onderdeel gewijzigd. | Vermoeden | midden | `architectuur.md` bijgewerkt. Bevestigen kan door te kijken of `Melden` zelf is aangepast, en dat is in deze diff niet zo. |
| 4 | De diff is klein. De grootte van `MeldenTest.kt` zie ik niet, maar het is waarschijnlijk ruim onder 400 regels. | Vermoeden | midden | Bestanden onder ±400 regels. Een regeltelling van het bestand bevestigt het. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet in `MeldenTest.kt` een korte reden bij de grens van 4 tekens, bijvoorbeeld dat korte namen toevallig in de OS-tekst kunnen staan.
- Controleer dat de CI-run van `MeldenTest` groen is. Ik kon geen uitslag zien.
- Maak de commitregel kloppend: "Obsidian-versie getest" past niet bij Bison & Flex.

---
Automatische keurder, model `claude-sonnet-5-5`, 18468 tokens in, 2020 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
