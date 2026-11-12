# Snelle proefronde voor Ebb (12 nov 2026)

Gemaakt door een hulp-Claude op verzoek van de hoofdchat. Alleen de twee workflowbestanden zijn aangepast, geen broncode van de app.

- Tak: `claude/garmin-snel-proef`, commit `2e85cd64` (bovenop `ed2f4e5f`, de tip van proef65 van 13:00 UTC).
- Bestanden: `.github/workflows/garmin-adem-iq.yml` en `.github/workflows/garmin-adem-e2e.yml`.

## Wat er veranderd is (alleen op takken met "proef" in de naam)

1. **Job `plan`** in beide workflows beslist: snelle proef of volle ronde.
2. **Toetsen (e2e):** drie horloges (fr255, fenix847mm, venu3s), elk in een eigen job tegelijk (`bouw-fr255` enzovoort). Elke job doet alles wat meetelt voor zijn horloge: Run No Evil, bouwen met `-l 2`, veiligheidsbladen en startcheck, opslaan en weggooien met FIT-controle, eis 11 en 12. De pauzeproef draait in de job van fenix847mm. Het vereiste aantal horloges is per job 1 in plaats van 9 in één job.
3. **Plaatjes:** dezelfde drie horloges. De scènes (nu 51 tot 138) zijn verdeeld over 2 jobs per horloge, en in elke job draaien 3 containers tegelijk met elk een eigen simulator en een eigen kopie van de app (eigen `EERSTE` in `Bouw.mc`). Zes stroken van 14 of 15 scènes dus. De wachttijd per scène (12 s MIP, 20 s AMOLED) is niet veranderd. De crashcontrole (watchdog, app crash, out of memory, `VEILIG ... NEE`) leest de logs van elke strook en maakt de job rood.
4. **alle-horloges:** nog steeds alle 28 horloges, maar in 3 jobs naast elkaar. Elk deel eist dat het manifest minstens 28 horloges heeft en dat al zijn eigen horloges een regel kregen.
5. Afbreken bij een nieuwe push is niet veranderd. De image uit een cache halen is niet gedaan: ophalen kost maar 20 tot 30 seconden, een cache van een image van deze grootte is niet sneller.

Op main en op de bouwtak `claude/garmin-2026-11-10b` is alles gelijk: 13 horloges voor de plaatjes, 9 in één job voor de toetsen, alle scènes, één simulator per job, dezelfde jobnamen en artefactnamen.

## Hoe lang het duurt

| | was (proef65, run 43218140269 en 43218140436) | nu (run 43225366044 en 43225365957) |
|---|---|---|
| toetsen | 22,5 minuut (alleen de stap met de schermen 20 minuten) | uitslag na 6,5 minuut |
| plaatjes | 35 minuten per AMOLED-horloge, 23 op MIP, en langer door de rij (13 jobs) | uitslag na 8 minuten |
| alle-horloges | 16 minuten | 5,5 minuut |

Beide runs groen, gemeten vanaf de push. Alle 88 scènes zijn op elk van de drie horloges gemaakt, geen gemiste start, geen crash. De ronde gebruikt 12 jobs tegelijk; GitHub geeft er 20, dus twee proefrondes tegelijk gaan in de rij.

## Volle ronde afdwingen op een proeftak

- Zet `[vol]` in het commitbericht van de laatste commit van de push (de eerste regel telt ook mee), of
- start de workflow met de hand en zet het vinkje `vol` aan.

Dan draait alles zoals op de bouwtak: alle horloges, alle scènes vanaf 0, ook de controle wereld gelijk op 0:30 en 2:30. Bewezen met run 43224487139 (per ongeluk, het woord stond in mijn commitbericht).

## Overnemen (Gijs)

Let op: jij hebt om 13:20 UTC in commit `789d4102` zelf al een korte ronde in dezelfde twee bestanden gebouwd (drie horloges, `proef-scenes.txt`, alle-horloges overgeslagen, afbreken bij een nieuwe push). Samenvoegen met mijn tak geeft daardoor een botsing. Neem mijn bestanden dus NIET in hun geheel over, anders ben je je eigen werk kwijt. Wat mijn tak toevoegt aan die van jou, en wat het oplevert:

1. **Toetsen naast elkaar in plaats van achter elkaar.** Neem uit mijn e2e: de job `plan`, en bij `bouw` de regels `needs`, `name`, `strategy` en de vier `env`-regels (`ALLE`, `S1`, `VEEG`, `HORLOGES_N`), plus `-e ALLE=... -e S1=... -e VEEG=... -e HORLOGES_N=...` bij `docker run`. Jouw `case "$GITHUB_REF_NAME"` met `ALLE`, `MENU`, `VEEG` vervalt dan (bij mij heet `MENU` `S1`), en `MIN` wordt `$HORLOGES_N`. De derde start en de pauzeproef staan bij mij binnen `if echo " $ALLE " | grep -q " fenix847mm "; then ... fi`. Het artefact heet `garmin-adem-schermen-<horloge>`, en job `schermen` haalt ze op met `pattern: garmin-adem-schermen*` en `merge-multiple: true`.
2. **Scènes in stroken.** Neem uit mijn iq de job `plan`, de `env`-regels `DEEL`, `DELEN`, `STROKEN`, `SNEL`, `ART` bij `plaatjes`, de regel met `NR=""` bovenaan het script, het blok `if [ -n "$DEEL" ]` na de regel met `EERSTE=`, `CRASH-$D$NR.txt`, de regel `cp -r plaatjes/. /app/plaatjes/` onderaan het script en het blok met de drie `docker run` op de achtergrond. Met jouw `KEUZE` erbij: verdeel dan `REEKS` over de stroken in plaats van `EERSTE` tot `LAATSTE`. Jouw scènekeuze en mijn stroken versterken elkaar: weinig scènes en ook nog tegelijk.
3. **alle-horloges in drie delen** hoeft niet als je hem op proeftakken overslaat. Wil je hem toch op de proeftak: mijn versie kost 5,5 minuut.

Zie alles in één keer met `git diff ed2f4e5f 2e85cd64 -- .github/workflows`. Heb je liever dat het voor je wordt samengevoegd op jouw nieuwste tip, vraag het de hoofdchat.

Wat je moet weten:
- venu3s draait nu ook de toetsen (was alleen plaatjes) en is groen op alle eisen.
- In de snelle proef overschrijven de drie jobs elkaars `metingen.txt` op tak `schermen`; de cijfers staan per horloge in het log van elke job.
- De pixelvergelijking zoekt het artefact `ebb-plaatjes-<horloge>-<deel>` van de vorige groene run; de eerste snelle run heeft dus nog niets om mee te vergelijken.
- Drie simulators op één runner ging goed (geen gemiste scène). Zie je ooit `GEEN SCENE` of een half getekend beeld, zet dan `STROKEN` op 2 en `DELEN` op 3.
