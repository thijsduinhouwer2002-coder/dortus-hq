# Keuring blender-gewrichten Pro 1.2.6 (robot-enkels), 24-11-2026, automatische keurder
Wat ik keurde: commit a1e868b26 (aabad67..0b76311), bestanden `click_joints/betaald/rig.py` en `e2e/toetsen_robot_meer.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Bij een enkel met een bovenliggend bot krijgt het vangnet `verloren_stuk` nu de lengte van het scheenbot (`vang_lengte`) in plaats van die van het korte voetbot. Dat is wat de commit belooft. Bij alle andere gewrichten blijft `vang_bot = pb`, dus daar verandert niets. | Feit (uit de diff) | Hoog | Weerleggen kan alleen een rig waarin `pb.parent` van een enkel geen scheen is. |
| 2 | De bewering "0% verloren, een weggevallen voet nog ±48%" komt uit een lokale meting op 5.3.0 in de commenttekst. Uit tekst alleen kan ik dat niet nagaan. | Vermoeden | Midden | De CI-log van `toetsen_robot_meer.py` met regels `[cj-robot-toets]` en "KLAAR 0 FOUT" in 4.2.23, 5.2.3 en 5.3.0. |
| 3 | Het akkoord van Daan in `ontwerp.md` geldt voor tak-commit 6dc287f (e2e 45384569641 groen). Deze commit heeft een andere hash. Waarschijnlijk is het dezelfde inhoud na samenvoegen of herbasering, maar dat zie ik hier niet. | Vermoeden | Midden | `git diff 6dc287f a1e868b26` zonder verschil in de add-on. |
| 4 | De commit noemt "versie 1.2.6", maar `blender_manifest.toml` en `CHANGELOG.md` staan niet in de gewijzigde bestanden. | Vermoeden | Midden | Controleren of de versie al eerder is opgehoogd en of de changelog een 1.2.6-regel heeft. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is een nieuwe toets bijgekomen en er is geen bestaande toets aangepast om te slagen. De eisen (enkels minstens 45°, knieën 0-120°, delen gesloten en één stuk) zijn streng en niet verruimd. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `rig.py` is al ver boven de ±400 regels (de diff laat regel 776 en verder zien). Deze wijziging voegt maar een paar regels toe. De toets is 83 regels. | Feit | Hoog | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet meegewijzigd, terwijl het vangnet-gedrag verandert. Ik kan niet zien of dat bestand `verloren_stuk` of de enkelregel beschrijft (de tekst is afgekapt). | Vermoeden | Laag | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. De cijfers in de comments (43 mm, 26 mm, 13%, ±48%) zijn eigen metingen en staan zonder label GEZIEN, DERDEN of GOK. | Feit | Hoog | Cijfers met GEZIEN, DERDEN of GOK |
| 5 | De toets leest `commercie/filmpjes/studio` buiten het product. Er is geen workflowbestand meegewijzigd, dus ik kan niet zien of de toets in CI draait. | Vermoeden | Midden | Controleren of de e2e-workflow `toetsen_robot_meer.py` aanroept. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Er is geen beeld en niets speelbaars meegestuurd, dus ik kan hier niets over plezier of uiterlijk zeggen. Voor de gebruiker is het nuttig als beide enkels van de robot nu een gewricht krijgen. | Een schermafbeelding van de robot met enkels (poster of lijstplaatje) laten zien aan Daan. | Klein |
| 2 | In het akkoord staat als kan: de hap uit de hiel van de blokvoet kleiner. Dat zit niet in deze wijziging. | Later oppakken. | Midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer in de CI-log dat `toetsen_robot_meer.py` groen is in 4.2, 5.2 en 5.3, en dat de toets in de workflow zit (A2, B5).
- Controleer dat `blender_manifest.toml` op 1.2.6 staat en dat `CHANGELOG.md` een korte regel heeft (A4).
- Controleer of `architectuur.md` het vangnet van `verloren_stuk` bij enkels noemt, en werk het zo nodig bij (B3).
- `rig.py` is veel te groot en kan bij gelegenheid worden opgesplitst (B2).

---
Automatische keurder, model `claude-sonnet-5-5`, 20721 tokens in, 3408 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
