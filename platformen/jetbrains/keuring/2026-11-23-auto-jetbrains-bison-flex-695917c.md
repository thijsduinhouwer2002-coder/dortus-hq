# Keuring Bison & Flex ontwerp.md, akkoord 2026.1.2, 23-11-2026, automatische keurder
Wat ik keurde: commits 08c32e4..695917c, alleen `producten/jetbrains-bison-flex/ontwerp.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is alleen tekst: een nieuwe regel "Akkoord: ja 23 nov 2026" voor de uitgave van 2026.1.2 op 2e46f5e2. De oude regel van 18 nov is onder "Oud" gezet. De belofte bovenaan is niet veranderd. | Feit | Hoog | Niets nodig. |
| 2 | De nieuwe regel zegt dat de change-notes de meldknop en de error handler noemen, met "Nothing is sent until you submit it yourself". `CHANGELOG.md` 2026.1.2 bevat precies die twee regels en die zin. | Feit | Hoog | `plugin.xml` zelf zag ik niet. Een blik op de change-notes daar zou bevestigen dat ze gelijk zijn aan de changelog. |
| 3 | De regel claimt dat de CLion-run 45197751752 en de e2e-run 45197752060 groen zijn. Ik kan dat niet nagaan. | Vermoeden | Midden | De uitslag van die twee runs in de API of het log. |
| 4 | De regel verwijst naar `platformen/jetbrains/keuring/2026-11-23-bison-flex-2026.1.2-uitgave-daan.md`. Dat bestand zat niet in de wijziging. | Vermoeden | Midden | Controleren dat het bestand bestaat en "Akkoord: ja" bevat. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests of code aangepast, dus er is niets om te slagen gemaakt. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is niet gewijzigd. Dat hoeft ook niet bij een wijziging die alleen een akkoordregel toevoegt. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in. De run-nummers zijn publieke ID's. | Feit | Hoog | Geen persoonsgegevens |
| 4 | De runs zijn gemarkeerd als "GEZIEN in de API". Dat past bij de GEZIEN/DERDEN/GOK-regel, maar ik kan het niet zelf nakijken. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | Er is geen speltekst of AI-beeld of -geluid toegevoegd. | Feit | Hoog | Hats en Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen in deze wijziging. Daarover geef ik geen oordeel. | Niet van toepassing | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Het tijdstip "Daan 23 nov ±16:35 NL" ligt na het tijdstip van deze keuring (16:27 NL). Het is met "±" aangegeven, maar het kan betekenen dat de akkoordregel is geschreven voor het akkoord er was. Controleer in het keuringsbestand van Daan wanneer het akkoord echt staat.
- Controleer dat het keuringsbestand van Daan bestaat en dat de twee run-uitslagen kloppen (A3 en A4).
- De commitmelding noemt ook "terugval Pro (nee, testhaak)". Dat staat niet in dit bestand. Hoort die nee bij Pro van dit product, kijk dan of die niet botst met het "ja" voor de uitgave.
- Het open kan-punt uit de regel zelf blijft staan: één keer de meldlink openen om te zien dat issues aan staan op de loketrepo.

---
Automatische keurder, model `claude-sonnet-5-5`, 19204 tokens in, 2633 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
