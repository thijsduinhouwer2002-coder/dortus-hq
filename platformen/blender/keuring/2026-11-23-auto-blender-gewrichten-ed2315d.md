# Keuring blender-gewrichten, 23-11-2026, automatische keurder
Wat ik keurde: commits 60e15aa..ed2315d (ed2315d63, Bram): `rig.py`, `scharnier_neus.py`, drie e2e-toetsen en `architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `maten_neus` geeft `TIGHT_KORT` alleen als de lip door de korte onderkant te kort werd én de volle lip wel zou klikken. Anders blijft het `TIGHT`. De logica in `klik_bij` is gelijk aan de oude (zelfde rek-, k- en minimumgrens). | Feit (uit de diff gerekend) | Hoog | Een run van `toetsen_neus.py` die de nieuwe stap "Tight-reden" laat slagen. |
| 2 | Het rekenvoorbeeld in de nieuwe toets klopt met de code. t = 0,4. Volle lip = 6,5 geeft k = 0,25 en klikt. Met diepte 1,0 is L = 0,2 en k = 0,002, onder 0,1. Dus `TIGHT_KORT`. | Feit (handrekening) | Hoog | Hetzelfde logbestand. |
| 3 | De toets eist dat `maten_neus(...)` zonder diepte `""` teruggeeft als het wel klikt. Het succesresultaat van de functie staat niet in de diff. | Vermoeden | Midden | De rest van `maten_neus` lezen, of de run: `""` bij succes bevestigt het. |
| 4 | De nekreden ("no clean spot for a neck ball ...") komt alleen als de kern "too thin here for a ball joint", "nothing was cut" of niets (`None`) zegt. Andere meldingen blijven ongewijzigd, ook de "loose piece"-melding. Dat staat in de toets. | Feit | Hoog | Run van `toetsen_rig.py`. |
| 5 | Dat de knop na `TIGHT_KORT` de volgende plek probeert, steunt op zoeken naar "tight" in kleine letters in code die niet in de diff staat. De tekst bevat "Tight", dus het zou moeten werken. | Vermoeden | Midden | Een rig-toets of -run waarin een scharnier met korte onderkant doorgaat naar de volgende plek. |
| 6 | De commit zegt "e2e groen". Ik zie geen log of run-id. | Vermoeden | Laag | Run-id of groen vinkje op ed2315d. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Drie bestaande toetsen verwachten nu `TIGHT_KORT` in plaats van `TIGHT`. Dat volgt uit een bedoelde tekstwijziging voor precies die gevallen (korte onderkant), met uitleg in het commentaar. Er is ook een nieuwe toets bij. Het is geen aanpassing om te slagen. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` is bijgewerkt voor `TIGHT_KORT` en voor `kogel_reden` met de nek. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | Andere toetsen (bijvoorbeeld in `toetsen_scharnier.py` of `toetsen_mens.py`) kunnen nog `neus.TIGHT` verwachten in een geval dat nu `TIGHT_KORT` wordt. Alleen de gewijzigde bestanden zijn meegestuurd. | Vermoeden | Midden | Tests niet aangepast om te slagen |
| 4 | Bestandsgrootte (±400 regels) van `rig.py` en `scharnier_neus.py` is niet te zien. De diff is klein. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 5 | Geen persoonsgegevens of sleutels in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 6 | De nieuwe spelertekst is Engels. Het commentaar noemt "akkoord Daan" en de architectuur zegt dat ook. Ik kan dat akkoord niet zelf nagaan. | Vermoeden | Midden | Spelerstekst alleen met akkoord |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | "Too little limb past this joint to click. Try a spot further from the end." geeft een duidelijke richting. Dat is beter dan "thicker spot", dat bij een kort lid niet hielp. | Niets nodig. | klein |
| 2 | De nekmelding noemt twee mogelijke oorzaken ("short or sits inside the head") en eindigt met "place it by hand". Dat kan de koper laten twijfelen waar hij moet klikken. | Eén zin erbij over waar een nekkogel meestal past, of de cursor alvast bij de nek zetten. Ik kan dit niet spelen, dus dit is een vermoeden. | klein |
| 3 | Voor een scharnier met een weigering zonder gevonden plek blijft de koper de nuance tussen `TIGHT` en `TIGHT_KORT` zien. Of de samenvattingsregel in de lijst deze tekst ook toont, is niet zichtbaar in de diff. | Bij de rig-knop de statusbalk of lijst controleren op beide teksten. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer in de run dat `maten_neus` zonder diepte `""` geeft (A3) en dat geen andere toets meer `neus.TIGHT` verwacht in een kort-onderkant-geval (B3).
- Zet het run-id van de groene e2e in de commit of in `ontwerp.md`, want de claim "e2e groen" is nu niet te controleren (A6).
- Maak de nekmelding iets concreter (C2).
- Werk de docstring van `kogel_reden` bij, als die nog "heup of schouder" zegt. Het begin staat niet in de diff, dus dat is een vermoeden.

---
Automatische keurder, model `claude-sonnet-5-5`, 28299 tokens in, 4852 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
