# Keuring blender-gewrichten e2e plaatje 4, 23-11-2026, automatische keurder
Wat ik keurde: commit e8900477d (045192b..e890047), alleen `producten/blender-gewrichten/e2e/schermen.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen het schermenscript van de e2e-test, niet de add-on. Het goedgekeurde 0.1.1 en 1.0.2 uit `ontwerp.md` verandert dus niet. | Feit | Hoog | `git diff --stat` laat één bestand zien. |
| 2 | Het doel is dat plaatje 4 (Material Preview) pas wordt genomen als de EEVEE-shaders klaar zijn. De logica is daarvoor in de tekst logisch: tot 30 keer 1 s wachten zolang de taak SHADER_COMPILATION loopt, dan 2 s extra, dan schieten. | Feit | Midden | Een groene run waarin `SHADERS klaar na N s` staat en plaatje 4 geen "Compiling EEVEE engine shaders" toont. |
| 3 | Of de wachtlus echt werkt, is een vermoeden. In EEVEE Next (4.2 en hoger) meldt de shaderbouw zich misschien niet als taak bij `bpy.app.is_job_running("SHADER_COMPILATION")`. Dan is `bouwt` altijd onwaar en verandert er niets. | Vermoeden | Laag | Een run met een log waarin `SHADERS klaar` voorkomt, of een plaatje 4 dat in 4.2.23 en 5.2.3 schoon is. |
| 4 | Er is geen run of log bij de commit die laat zien dat de oplossing werkt. | Feit | Midden | Een Actions-run na deze commit met de schermen van beide Blender-versies. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Er is alleen wachttijd toegevoegd voor een schermafbeelding, geen controle versoepeld. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | `architectuur.md` hoeft niet bij te werken, want de add-on is niet veranderd. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | De bestandslengte van `schermen.py` zie ik niet in de diff. Het bestand kan boven ±400 regels zitten. | Vermoeden | Laag | `wc -l` op het bestand. Bestanden onder ±400 regels |
| 4 | Er staan geen persoonsgegevens of sleutels in de wijziging. Het runnummer 45093224282 is geen geheim. | Feit | Hoog | Geen persoonsgegevens |
| 5 | De wijziging toont geen cijfers of beweringen voor een winkelpagina. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Ik zie geen beelden, dus ik kan niet oordelen of plaatje 4 er goed uitziet. Het gaat erom dat er geen "Compiling EEVEE engine shaders" meer op staat. Iris of Daan moeten het plaatje bekijken als het voor de winkel bedoeld is. | Na de volgende run plaatje 4 met de Read-tool bekijken. | Klein |
| 2 | Na een time-out van 30 s zegt het log toch "SHADERS klaar". Dan is het plaatje misschien nog onvolledig, terwijl het log iets anders zegt. | Een apart logbericht voor "time-out, shaders nog niet klaar". | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Log bij een time-out eerlijk melden dat de shaders nog niet klaar waren, in plaats van "klaar".
- Controleer in de eerstvolgende run (4.2.23 en 5.2.3) of `SHADERS klaar` in het log staat en plaatje 4 schoon is. Staat het er nooit, dan meldt de taak zich niet en is een vaste wachttijd of een proefframe de betere oplossing.
- Controleer dat `is_job_running("SHADER_COMPILATION")` in beide versies geen fout geeft. Een ongeldige taaknaam geeft een uitzondering, en `getattr` vangt dat niet af.
- Controleer de lengte van `schermen.py` (richtlijn ±400 regels).

---
Automatische keurder, model `claude-sonnet-5-5`, 17565 tokens in, 3187 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
