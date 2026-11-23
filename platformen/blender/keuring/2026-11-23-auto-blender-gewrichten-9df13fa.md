# Keuring blender-gewrichten e2e shader-log, 23-11-2026, automatische keurder
Wat ik keurde: commit 9df13fad6 (Bram, "e2e logt shader-time-out eerlijk"), alleen `producten/blender-gewrichten/e2e/schermen.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
(De opdracht in ontwerp.md gaat over de add-on. Deze wijziging raakt alleen de logregel van een testscript, dus ik toets tegen de commitbeschrijving.)
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De melding "SHADERS klaar" komt nu alleen als `strook_gekleurd()` waar is. Anders meldt het log dat de shaders niet klaar waren en dat plaatje 4 toch is geschoten. Dat past bij de titel "logt time-out eerlijk". | Feit (uit de diff) | Hoog | n.v.t. |
| 2 | De add-on, het manifest en de zip veranderen niet. Voor de gebruiker verandert dus niets. | Feit (alleen `e2e/schermen.py` gewijzigd) | Hoog | n.v.t. |
| 3 | `strook_gekleurd()` komt in de diff niet voor als nieuwe functie. Ik neem aan dat die al in het bestand staat, waarschijnlijk in de wachtlus erboven. | Vermoeden | Midden | Een `grep` naar `def strook_gekleurd` in `schermen.py`, of een groene e2e-run met deze commit. |
| 4 | Of de wachtlus eindigt als de strook nooit kleurt, zodat de nieuwe tak met "toch geschoten" bereikt wordt, is uit de diff niet te zien. | Vermoeden | Laag | Een e2e-log waarin de regel "nog niet klaar ... toch geschoten" voorkomt, of de lus-code erboven. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Er is alleen een logregel toegevoegd, en het gedrag (schieten, meten, teruggeven) blijft gelijk. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | De wijziging is 5 regels. De totale bestandsgrootte van `schermen.py` zie ik niet. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 3 | `architectuur.md` hoeft niet bij te werken voor een logregel in een testscript. | Feit | Midden | architectuur.md bijgewerkt |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 5 | Er komen geen cijfers, spelerstekst of AI-beeld bij. De regel is niet van toepassing. | Feit | Hoog | GEZIEN/DERDEN/GOK, Hats, Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet van toepassing: dit is een testlog, er is niets te zien of te spelen.
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Als de shaders niet klaar zijn, wordt plaatje 4 toch geschoten. Dat plaatje kan dan een ongekleurde strook tonen. | Laat de test bij "nog niet klaar" een waarschuwing of een gemarkeerde bestandsnaam geven, zodat Daan of Iris geen halfklaar beeld als winkelplaatje gebruiken. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer dat `strook_gekleurd()` bestaat en dat de wachtlus eindigt (vermoeden uit A3 en A4). De eerstvolgende e2e-run laat dat zien.
- Overweeg de bestandsnaam van plaatje 4 te laten afwijken als de shaders niet klaar waren (zie C1).
- Ga na dat `schermen.py` onder ±400 regels blijft.

---
Automatische keurder, model `claude-sonnet-5-5`, 17388 tokens in, 1965 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
