# Keuring Bison & Flex 2026.1.2 change-notes, 23-11-2026, automatische keurder
Wat ik keurde: commits 542c4be..957a9ac (2e46f5e67), bestanden `CHANGELOG.md` en `plugin.xml` van `producten/jetbrains-bison-flex`
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De change-notes in `plugin.xml` kondigen nu de meldknop in het Help-menu en het foutvenster aan. Volgens `ontwerp.md` heeft Daan juist die twee (eb02ba1, R5) nog niet gekeurd. Zijn akkoord van 18 nov geldt tot en met 281d0a3. | Feit | Hoog | Een nieuwe regel `Akkoord: ja` van Daan die eb02ba1 of de huidige versie noemt. |
| 2 | In `CHANGELOG.md` is de kop "CONCEPT tot keuring Daan" weggehaald. De status klopt daardoor niet meer met het ontwerp. | Feit | Hoog | Zelfde als hierboven. |
| 3 | De tekst in `plugin.xml` en in `CHANGELOG.md` zegt hetzelfde: meldknop, foutvenster, nieuwe-IDE-klaarheid en Plugin Verifier. De korte post is bijgewerkt en blijft CONCEPT. | Feit | Hoog | n.v.t. |
| 4 | De claim "Nothing is sent until you submit it yourself" en de voorinvulling met plugin-, IDE- en OS-versies staan niet in deze wijziging. De code zit in een andere commit en ik zie die niet. | Vermoeden | Midden | De code van de meldactie en de error handler: opent die alleen de browser, en wordt er niets verstuurd voor de gebruiker op "submit" klikt? |
| 5 | Het ontwerp noemt voor 2026.1.2 een CLion-run, e2e-run en Plugin Verifier, maar alleen voor de oude stand. Voor de nieuwe code zie ik geen run. | Vermoeden | Midden | Groene runs op de commit die wordt geüpload, met de verifier op 2025.3, 2026.2 en CLion 2026.2. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests of codebestanden gewijzigd, dus er is niets aangepast om te slagen. Er is geen bestand van meer dan 400 regels toegevoegd. | Feit | Hoog | Tests en bestandsgrootte |
| 2 | Er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 3 | `architectuur.md` is niet meegewijzigd en de zichtbare stand (8 nov, versie 0.2) noemt de meldactie niet. Of dit bij de eerdere commit al is bijgewerkt, zie ik niet. | Vermoeden | Midden | architectuur.md bijgewerkt |
| 4 | De menunaam "Report a Problem with Bison & Flex..." volgt Title Case voor menu's. | Feit | Hoog | JetBrains-regel in `ontwerp.md` |
| 5 | De korte post blijft CONCEPT en gaat alleen via de hoofdchat. | Feit | Hoog | Spelerstekst alleen als CONCEPT |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een gebruiker kan een fout direct melden zonder zelf versies op te zoeken. Dat voelt zorgvuldig. | n.v.t. | n.v.t. |
| 2 | De change-notes beginnen met twee lange alinea's. In het pluginvenster is dat veel lopende tekst. | Korte opsomming of kortere zinnen, "New" en "Better" gescheiden zoals in `CHANGELOG.md`. | Klein |
| 3 | Of het Help-menu-item en het foutvenster er goed uitzien en werken, kan ik niet beoordelen zonder schermen. Dat blijft aan Daan. | Schermen licht en donker van het menu-item en het foutvenster. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Daan heeft de meldknop en het foutvenster (eb02ba1) nog niet gekeurd, maar ze staan nu in de change-notes en de CONCEPT-markering is weg. Niet uploaden voor Daan `Akkoord: ja` heeft gezet voor de versie die wordt geüpload. Zet de CONCEPT-markering terug tot dan.

**Kan**
1. Controleer in de code dat er niets wordt verstuurd voor de gebruiker zelf op "submit" klikt, omdat de change-notes dat beloven.
2. Laat voor het uploaden zien dat CLion-run, e2e-run en verifier groen zijn op de nieuwe code.
3. Controleer of `architectuur.md` de meldactie en de error handler noemt.
4. Kort de eerste alinea van de change-notes in.

---
Automatische keurder, model `claude-sonnet-5-5`, 19686 tokens in, 3132 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
