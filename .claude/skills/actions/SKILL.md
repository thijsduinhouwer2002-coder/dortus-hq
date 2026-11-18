---
name: actions
description: Gebruik dit als je een GitHub-workflow wilt starten of de uitslag of het log van een run wilt lezen. Werkt zonder GitHub-sleutel, alleen met git en curl.
---

# Workflows starten en uitslag lezen zonder sleutel

De GH_TOKEN in agentsessies werkt niet. Dat hoeft ook niet: starten gaat met een bestand, lezen gaat zonder sleutel.

## Starten: push een opdrachtbestand
1. Maak `organisatie/opdrachten/<datum>-<jouw naam>-<onderwerp>.json`:
   ```json
   {"workflow": "wegwijzer.yml", "invoer": {}, "tak": "main", "van": "<jouw naam>", "waarom": "<een zin>"}
   ```
   `invoer` zijn de `workflow_dispatch`-invoervelden van die workflow (tekst, getal of ja/nee). `tak` mag weg (dan `main`).
2. `git add` alleen dat bestand, commit, `git pull --rebase --autostash`, `git -c push.negotiate=true push origin main`.
3. De workflow `.github/workflows/opdracht.yml` start hem binnen ±30 seconden en zet het resultaat in jouw bestand: `"uitslag": {"run_id": ..., "url": ...}` of `"fout": "<reden>"`. Na ±1 minuut: `git pull --rebase --autostash`.
4. Opnieuw starten = een nieuw bestand. Een bestand met `uitslag` of `fout` wordt nooit nog eens gestart.

**Alleen workflows op de lijst** `TOEGESTAAN` in `organisatie/controle/opdracht.py` (tests, proeven, renders, meten). Uploads naar een winkel en alles wat iets openbaar uitbrengt staan er bewust niet op: die gaan via de tag-route in de skill `uitbrengen`. Wat geld kost (zoals `keurder.yml`) ook niet. Iets toevoegen mag alleen als de workflow niets naar buiten zet en niets kost, met een reden erbij.

## Uitslag lezen
```
python3 organisatie/controle/actions.py organisatie/opdrachten/<bestand>.json   # de run van jouw opdracht
python3 organisatie/controle/actions.py <workflow>.yml                          # laatste run van een workflow
python3 organisatie/controle/actions.py <run_id> --wacht                        # wacht tot hij klaar is
python3 organisatie/controle/actions.py lijst                                   # laatste 15 runs
```
Je ziet de status, elke job en stap, en welke stap faalde (`FOUT`). Code 1 = mislukt. Zonder sleutel mag je ±60 verzoeken per uur doen; `--wacht` vraagt één keer per minuut.

## Log van een mislukte run
`python3 organisatie/controle/actions.py <run_id> --log` laat de laatste 200 regels van de mislukte stap zien. Die komen uit `organisatie/actions-logs/<workflow>-<run>.txt`, gemaakt door `.github/workflows/actions-log.yml`:
- binnen ±1 minuut als de run door een push startte;
- bij de veegronde (elk kwartier) als de run uit een opdrachtbestand kwam (GitHub start `workflow_run` niet voor runs die met de workflow-sleutel zijn gestart);
- meteen als je wilt: opdrachtbestand met `{"workflow": "actions-log.yml", "invoer": {"run": "<run_id>"}}`.

Persoonsgegevens en sleutels worden eruit gepoetst (patronen uit `organisatie/controle/check.py`); logs ouder dan 7 dagen ruimt de workflow zelf op. Lees het log voor je iets repareert: de fout staat meestal in de laatste regels voor `##[error]`.

## Niet doen
- Geen WebFetch voor GitHub-pagina's: webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
- Geen eigen sleutel in een bestand zetten of vragen; geen workflow aan de lijst toevoegen om een upload te omzeilen.
- Een workflow die je hier niet kunt starten: vraag de eigenaar of meld het in `berichten/hoofdchat.md`.
