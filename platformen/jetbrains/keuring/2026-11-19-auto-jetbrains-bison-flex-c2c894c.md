# Keuring Bison & Flex e2e: vaste scheiding instellingenvenster, 19-11-2026, automatische keurder
Wat ik keurde: commits f057cf7..c2c894c (c2c894cc), bestanden `architectuur.md` en `e2e/.../Gedeeld.kt`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen de testhulp `winkelproject()` en de documentatie. De plugincode, `plugin.xml` en de belofte van het ontwerp (kennen van Bison en Flex, Pro over beide bestanden) blijven ongewijzigd. | Feit | Hoog | De diff bevat geen bestand onder `src/main`. |
| 2 | De wijziging moet de scheiding op de kleurenpagina laten stilstaan, zodat de beeldvergelijking geen vals alarm geeft. Of dat lukt blijkt niet uit de tekst. Er staat geen run na deze commit bij. | Vermoeden | Midden | Drie e2e-runs na deze commit met 0 grote verschillen op `*-kleurenpagina`, of de sleutel `settings.editor.splitter.proportion` die in het log of op het scherm de 0,33 laat zien. |
| 3 | De uitleg klopt op het eerste gezicht: bij een venster van 2000 px is 0,33 gelijk aan 660 px, en dat ligt voorbij de gemeten 474 tot 630 px. | Vermoeden | Midden | Meting van de scheidingspositie in de runs na de wijziging. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Alleen de opzet van het testproject is veranderd, en de beeldvergelijking geeft volgens het ontwerp nooit een rode test. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is in dezelfde commit bijgewerkt: de 0,33, het oude masker met `%` is weg en de gemeten reeks 474 tot 630 px staat erbij. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | De cijfers in de tekst hebben een bron: runnummers met GEZIEN. De 0,33 en de bewering "voorbij die breedtes" hebben geen eigen label, en een run die dat bewijst ontbreekt. | Feit | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | `writeText` en `createDirectories` komen uit `kotlin.io.path`. Of `writeText` al is geïmporteerd, zie ik niet in de diff. | Vermoeden | Laag | Bouwt de e2e-code; de run bevestigt dat |
| 5 | `workspace.xml` wordt zonder controle geschreven. Staat er al een `.idea/workspace.xml` in het winkelproject, dan wordt die overschreven. | Vermoeden | Laag | Een blik in de map `dortus.e2e.winkelproject` |
| 6 | De tekst zegt "126 px", maar 474 tot 630 px is 156 px. De "wordt hier niet meer gebruikt" voor het `%`-masker staat niet in deze diff, dus ik kan niet zien of `beeldvergelijk.py` dat masker nog heeft. | Vermoeden | Laag | `beeldvergelijk.py` nalezen op het `%`-masker |
| 7 | Bestandsgrootte (±400 regels) van `Gedeeld.kt` kan ik uit de diff niet halen. Persoonsgegevens, sleutels, AI-beeld of -geluid en spelerstekst: niets gezien. | Vermoeden | Laag | `wc -l` op `Gedeeld.kt` |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet het effect van de 0,33 pas als vast na drie groene runs, en label de claim dan GEZIEN. Tot die runs er zijn is het een hypothese.
- Controleer of een bestaand `workspace.xml` in het winkelproject niet wordt overschreven, of voeg dan samen.
- Controleer de import van `writeText`.
- Maak de cijfers in de architectuurtekst consistent (156 px of 126 px) en controleer of het `%`-masker echt uit `beeldvergelijk.py` is.

---
Automatische keurder, model `claude-sonnet-5-5`, 22252 tokens in, 2779 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
