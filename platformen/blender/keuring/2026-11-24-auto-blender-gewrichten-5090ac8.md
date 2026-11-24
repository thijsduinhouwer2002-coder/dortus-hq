# Keuring blender-gewrichten (Pro 1.2.8, knietoets), 24-11-2026, automatische keurder
Wat ik keurde: commits 23c9bdf..5090ac8, alleen het bestand `producten/blender-gewrichten/e2e/toetsen_knie_midden.py`
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen de test. Het product wordt er niet beter van, want in Blender 4.2 komt er 12 mm boven het kniemidden nog steeds geen scharnier. | Feit | hoog | De diff bevat alleen een testbestand. |
| 2 | De eis in het testbestand was dat ook 12 mm hoger een scharnier komt. Voor Blender 4.2 (een ondersteunde versie volgens het ontwerp) wordt die eis nu losgelaten. | Feit | hoog | De nieuwe `if`-tak telt dit geval in 4.2 als geslaagd zonder scharnier. |
| 3 | De bewering "1.2.7 doet daar hetzelfde" kan ik uit deze tekst niet nagaan. Alleen een runnummer (45459661428) en "lokaal gemeten" staan in een code-opmerking. | Vermoeden | midden | Het log van die run en een run van 1.2.7 op 4.2 met dezelfde cursorplek. |
| 4 | Het commitbericht noemt "Pro 1.2.8", maar de diff verandert geen manifest of versienummer. | Vermoeden | laag | Een versiebump in een eerdere commit, of die ontbreekt. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is aangepast zodat hij in 4.2 slaagt. De beperking staat wel eerlijk in de opmerking, maar niet in `CHANGELOG.md`, `ontwerp.md` of `architectuur.md`. Ook is er geen akkoord van Daan voor 1.2.8. Het laatste akkoord geldt 1.2.6. | Feit | hoog | Tests niet aangepast om te slagen. |
| 2 | De nieuwe tak test `"mesh is unchanged" in str(r)`. Als `r` de gewone operatoruitkomst is, zoals `{'CANCELLED'}`, staat die tekst daar niet in. Dan wordt de tak nooit genomen en blijft de test in 4.2 rood. Ik zie `plaats()` niet. | Vermoeden | midden | Een run op 4.2 waarin de regel "Blender 4.2 snijdt hier niet" in het log staat. |
| 3 | Het testbestand blijft klein en er staan geen persoonsgegevens of sleutels in. | Feit | hoog | Geen regel geschonden. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Een koper met Blender 4.2 zet een knieën-gewricht iets hoger, krijgt "the mesh is unchanged" en weet niet wat hij daarmee moet. Dit is niet te zien of te spelen, dus dit is een vermoeden uit de tekst. | De melding laat een uitweg zien, bijvoorbeeld de cursor iets lager zetten of Blender 4.5 of nieuwer gebruiken. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. De test is versoepeld voor een ondersteunde Blender-versie (4.2). Leg de beperking vast in `ontwerp.md` en de `CHANGELOG.md` van Pro, of los hem op. Zonder dat is niet te zien dat een koper in 4.2 dit gewricht niet kan plaatsen. Daan of Thijs moet dit ook uitdrukkelijk accepteren.

**Kan**
1. Controleer dat `str(r)` echt de meldingstekst bevat, of toets de melding op een andere manier. Anders doet de nieuwe tak niets.
2. Laat de test ook bewijzen dat de mesh in 4.2 echt ongewijzigd is (geen nieuwe objecten, dezelfde puntenhash). Nu telt alleen `not ab`.
3. Controleer dat de versie en de changelog van 1.2.8 kloppen met het commitbericht.
4. Maak de 4.2-melding bruikbaarder voor de gebruiker (deel C).

---
Automatische keurder, model `claude-sonnet-5-5`, 18118 tokens in, 3170 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
