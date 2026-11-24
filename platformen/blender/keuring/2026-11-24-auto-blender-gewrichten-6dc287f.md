# Keuring blender-gewrichten Pro 1.2.6 (enkel op studio-robot), 24-11-2026, automatische keurder
Wat ik keurde: commit 6dc287f66 (bereik 2d4dd87..6dc287f), bestanden `betaald/rig.py` en `e2e/toetsen_robot_meer.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Bij een enkel met een bovenliggend bot krijgt het vangnet `verloren_stuk` nu de lengte van het scheenbot (`vang_lengte`). Voorheen was dat het korte voetbot, dus een bol van 15 mm. Bij alle andere gewrichten blijft `vang_bot = pb`, dus daar verandert niets. | Feit (uit de diff) | Hoog | n.v.t. |
| 2 | De bewering dat de robot nu een enkel krijgt (bol 26 mm, 0% verloren, 0-90 graden) staat alleen in commentaar en docstring. In deze tekst zit geen logregel of run die het laat zien. | Vermoeden | Midden | Een groene run van `toetsen_robot_meer.py` op 5.3.0 en 4.5+, met beide enkels geplaatst en minstens 45 graden. |
| 3 | Een grotere bol maakt het vangnet soepeler voor de enkel. Het commentaar zegt dat een weggevallen voet nog ±48% geeft, ruim boven `VERLOREN_MAX` (6%). Dat bevestigt dat het vangnet nog werkt, maar alleen voor de robot. | Vermoeden | Midden | Een bestaande toets waarin een enkelsnede echt een stuk verliest en nog steeds wordt geweigerd, en een run op MakeHuman. |
| 4 | Het commitbericht noemt "versie 1.2.6", maar in de gewijzigde bestanden staat geen manifest of changelog. | Feit (bestandslijst), de reden is onbekend | Midden | `blender_manifest.toml` van de betaalde build op 1.2.6, of een build-script dat het versienummer zet. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is een nieuwe toets bijgekomen en geen bestaande toets is aangepast om te slagen. De eisen (enkels ≥45°, knieën 120°±3, alle delen gesloten, elk deel één stuk) zijn niet versoepeld. Op 4.2 gelden bewust zwakkere eisen, omdat daar alleen Exact beschikbaar is. | Feit | Hoog | Tests niet aangepast om te slagen: ok |
| 2 | De bestanden zijn klein: de toets heeft 83 regels. De lengte van `rig.py` kan ik uit de diff niet halen. | Vermoeden | Laag | Bestanden onder ±400 regels: `wc -l` op `rig.py` |
| 3 | `architectuur.md` is niet meegewijzigd. Het vangnet voor de enkel wordt in het afgekapte stuk daarvan misschien beschreven (de knie-regel van 0,6 keer het bot). | Vermoeden | Laag | architectuur.md bijgewerkt: een zin over de enkelbol erbij |
| 4 | De cijfers in de commentaren ("Gemeten op de robot", 26 mm, 43 mm, 0%, ±48%, "lokaal 5.3.0") hebben geen label GEZIEN, DERDEN of GOK. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | Er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | Hoog | Geen persoonsgegevens: ok |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Ik kan hier niets zien of spelen. De winst voor de gebruiker is dat de robot beide enkels krijgt, met een buighoek in het paneel ("Bends ...°"). Dat zou ik pas kunnen beoordelen op een schermafbeelding. | Een plaatje van de robot met enkels, geplaatst voor Daan en Iris. | Klein |
| 2 | Als een enkel toch overgeslagen wordt, staat de reden in `cj_rig_overgeslagen`. Het is onduidelijk of de gebruiker die reden in het paneel te zien krijgt. | Controleer dat het paneel de reden toont. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet `blender_manifest.toml` en CHANGELOG op 1.2.6 als dat nog niet gebeurd is (A4).
- Voeg bij de cijfers in de commentaren GEZIEN, DERDEN of GOK toe, met de run of het logbestand erbij (A2, B4).
- Draai de toets in de CI en leg de uitslag vast, voor 4.2, 4.5+ en 5.3.0. Draai ook de bestaande knie- en MakeHuman-toetsen, om te laten zien dat het ruimere vangnet nergens een echt verloren stuk doorlaat (A2, A3).
- Werk `architectuur.md` bij met de vangnetbol van de enkel, als het daar al beschreven staat (B3).

---
Automatische keurder, model `claude-sonnet-5-5`, 20679 tokens in, 3027 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
