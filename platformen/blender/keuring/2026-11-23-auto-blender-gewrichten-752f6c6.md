# Keuring blender-gewrichten (Pro 1.2.2, solver-terugval), 23-11-2026, automatische keurder
Wat ik keurde: commit 752f6c6e9 (ca9e012..752f6c6): `betaald/terugval.py` (nieuw), `betaald/__init__.py`, `e2e/toetsen_correcties.py`, `architectuur.md`
Akkoord: ja

Ik zie alleen tekst. Er is geen testuitslag meegestuurd en ik heb niets gedraaid.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Als de Manifold-snede een open deel geeft, wordt één keer opnieuw gesneden met Exact. Daarna volgt de gewone gesloten-controle van de operator. De logica klopt met de beschrijving in `architectuur.md` en de docstring. | Feit | hoog | n.v.t. |
| 2 | De toets simuleert de fout met `FORCEER_OPEN`. Het echte geval (linkerschouder bij Olaf, CI 8 gewrichten en lokaal 9) wordt niet nagespeeld. Of Exact daar echt een gesloten deel geeft, is dus niet bewezen. | Vermoeden | midden | De run met het figuur van Olaf op Manifold: negen gewrichten in CI en lokaal, en `cj_solver_terugval` gezet op de schouder. |
| 3 | Is ook de Exact-snede open, dan weigert de gratis operator zelf, met het figuur heel en zichtbaar. De toets (`FORCEER_OPEN` = 2) dekt dat af. | Feit (uit de toetscode) | midden | Groene run op 5.2.3 en 5.3.0 met de stap "terugval 2x open". |
| 4 | De commitmelding noemt PRO_VERSIE 1.2.2, maar dat staat niet in de meegestuurde diff. Misschien stond het er al. | Vermoeden | laag | `grep PRO_VERSIE` in de Pro-bron en het manifest van de Pro-zip. |
| 5 | In `een_lid.STAND` wordt `solver` op EXACT gezet. Blijft die stand bewaard tot het volgende gewricht, dan snijdt dat ook met Exact (trager, wel gesloten). Ik zie niet of de operator hem per aanroep terugzet. | Vermoeden | laag | Twee gewrichten achter elkaar op één lid, waarvan het eerste de terugval krijgt: `cj_solver` op het tweede deel. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen bestaande toets aangepast om te slagen. De nieuwe toets `solver_terugval` is erbij gekomen en wordt aangeroepen in `alles`. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt met een volledige beschrijving van `terugval.py`, de testhaak en de toets. | Feit | hoog | architectuur.md bijgewerkt |
| 3 | Het gratis deel is niet aangeraakt: geen gratis bestanden in de diff, en de tekst zegt dat `gewricht.py` gelijk blijft aan 014172e. De terugval staat alleen onder `betaald/`. | Feit (uit de diff) | hoog | Gratis zip gelijk aan de bron (`toets_zips.py`) |
| 4 | `terugval.py` heeft 98 regels. `toetsen_correcties.py` komt naar schatting rond 365 tot 380 regels (afgeleid uit de regelnummers van de hunk) en zit dicht bij de grens van 400. | Vermoeden | midden | Bestanden onder ±400 regels |
| 5 | Het commitbericht zegt "akkoord Daan" voor Pro 1.2.2. In het zichtbare deel van `ontwerp.md` staat dat akkoord niet. Het bestand is afgekapt, dus ik kan het niet nagaan. | Vermoeden | laag | Akkoord van Daan bovenaan `ontwerp.md` |
| 6 | Er staan geen persoonsgegevens of sleutels in de wijziging. De naam "Olaf" staat als spoor in een commentaar en docstring. | Feit | hoog | Geen persoonsgegevens |
| 7 | In de docstring staan "8" en "9" gewrichten zonder GEZIEN of DERDEN erbij. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Een Pro-gebruiker krijgt bij een zeldzame open Manifold-snede nu een gewricht in plaats van "no watertight parts". Dat is een duidelijke winst, maar ik kon het niet zien of spelen. | n.v.t. | n.v.t. |
| 2 | De gebruiker merkt niet dat er is teruggevallen op Exact. De vlag `cj_solver_terugval` staat alleen op het deel. | Eventueel een korte informatieve melding "Retried with the exact solver" voor wie de tijd opvalt. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Draai de terugval ook op het echte figuur van Olaf (deel A, punt 2), niet alleen met `FORCEER_OPEN`.
- Controleer dat PRO_VERSIE 1.2.2 en het zipmanifest echt omhoog zijn gegaan (deel A, punt 4).
- Controleer dat `een_lid.STAND["solver"]` niet blijft hangen op EXACT voor het volgende gewricht (deel A, punt 5).
- Bevestig het akkoord van Daan in `ontwerp.md` voor Pro 1.2.2 (deel B, punt 5).
- Houd `toetsen_correcties.py` in de gaten qua lengte en splits het als het over 400 regels gaat.
- Zet GEZIEN of DERDEN bij de cijfers 8 en 9 in de docstring.

---
Automatische keurder, model `claude-sonnet-5-5`, 24988 tokens in, 5380 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
