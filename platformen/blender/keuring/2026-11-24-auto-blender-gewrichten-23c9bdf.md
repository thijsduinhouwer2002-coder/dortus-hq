# Keuring blender-gewrichten Pro 1.2.8 (kan-punten A4 en B3), 24-11-2026, automatische keurder
Wat ik keurde: commits 4e4166a..23c9bdf (23c9bdfb0), bestanden `e2e/hulp_neus.py` en `architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `hulp_neus.py` geeft nu `u` mee aan `zaag_diepte(bvh, frame, maat, u)`. Daarmee volgt de testhulp de eenheidschaal, zoals de rest van de code via `eenheid_per_mm` doet. | Feit (diff) | Hoog | Niet van toepassing. |
| 2 | Of `zaag_diepte` in `scharnier_neus.py` al een vierde parameter `u` heeft, is in deze wijziging niet te zien. De alinea in `architectuur.md` noemt de oude drie parameters. Zonder die parameter geeft de testhulp een TypeError. | Vermoeden | Midden | Een groene e2e-run op deze commit, of `def zaag_diepte(` in `scharnier_neus.py`. |
| 3 | De add-on zelf is in dit bereik niet veranderd, alleen een testhulp en documentatie. Er is dus geen nieuw gedrag voor de gebruiker te keuren. | Feit (bestandenlijst) | Hoog | Niet van toepassing. |
| 4 | Het ontwerp toont een akkoord van Daan voor Pro 1.2.6. In het meegestuurde deel staat geen akkoord voor 1.2.7 of 1.2.8. Deze wijziging raakt de uitgave niet, maar dat akkoord moet er zijn voor het live gaat. | Vermoeden (het ontwerp is afgekapt) | Laag | Een regel "Akkoord: ja ... 1.2.8" in het volledige `ontwerp.md`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De testwijziging maakt de aanroep consistent met de eenheidschaal en verzwakt geen eis. Er is geen drempel verlaagd en geen uitkomst aangepast. | Feit (diff) | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt met de 1.2.8-regel: `_anker_breed`, de robotknie en de toets `toetsen_knie_midden.py`. Zo is kan-punt B3 gedekt. | Feit (diff) | Hoog | architectuur.md bijgewerkt |
| 3 | De alinea over `zaag_diepte` is erg lang, één regel van ruim 4000 tekens. De regel "bestanden onder ±400 regels" gaat over het aantal regels en wordt hier niet geschonden. Voor het lezen is het wel zwaar. | Feit | Hoog | Leesbaarheid (smaak) |
| 4 | In de diff staan geen persoonsgegevens, sleutels of wachtwoorden. | Feit (diff) | Hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niets te zien of te spelen in deze wijziging. Beeld en speelplezier zijn niet te beoordelen. | Niet van toepassing | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer in de e2e-run dat `zaag_diepte` echt `u` accepteert (A, rij 2).
- Splits de lange `zaag_diepte`-alinea in `architectuur.md` in een korte lijst met punten.
- Zorg voor een akkoord van Daan op `ontwerp.md` voor Pro 1.2.7 en 1.2.8 vóór het live gaat.

---
Automatische keurder, model `claude-sonnet-5-5`, 23029 tokens in, 2310 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
