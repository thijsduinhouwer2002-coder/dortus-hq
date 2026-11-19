# Bouwen en testen

Lees dit als je code schrijft of een product test. Laad ook de skill `bouwen-in-stappen`.

## Codekwaliteit (zodat een product heel blijft als het groeit)
1. **Tests niet aanpassen om ze te laten slagen.** Faalt een test, dan repareer je de code, niet de test. Een bestaande test wijzigen of weghalen mag alleen met een reden in de commit, en de controleur keurt dat apart goed. De controleur bekijkt bij elke beurt welke tests er veranderd zijn.
2. **Eerst kijken wat er al is.** Lees voor je iets toevoegt de bestaande code en `producten/<naam>/architectuur.md`. Bouw voort op wat er is, maak niets dubbel.
3. **Elke fout is jouw fout.** Faalt er iets na jouw wijziging, ook als het er "niets mee te maken lijkt te hebben", zoek de oorzaak. Zeg nooit "dat komt niet door mij" zonder bewijs.
4. **Klein en overzichtelijk.** Een bestand blijft onder de ±400 regels. Wordt het groter, splits het op. Elk product heeft een `architectuur.md` met de onderdelen en hoe ze samenhangen, en de bouwer werkt dat bij als er iets verandert.
5. **Opruimen hoort erbij.** Elke week (na het weekbesluit van zondag) zet de manager één opruimtaak bovenaan: dubbele code weg, grote bestanden splitsen, `architectuur.md` bijwerken. Pas daarna weer nieuwe functies.

## Testen in de echte app (GitHub Actions)
- Elk product wordt getest in de **echte app** van het platform, niet alleen met een nagebootste versie. Dat gebeurt op **GitHub Actions** (computers van GitHub), want in de Claude-omgeving mogen gedownloade programma's niet starten. Die beveiliging omzeil je nooit.
- Per product staat er een workflow in `.github/workflows/<product>-e2e.yml` en de tests in `producten/<product>/e2e/`. Voorbeeld: Rollwright (`rollwright-e2e.yml`, met wdio-obsidian-service). Voor JetBrains: een IDE-test op dezelfde manier (bijvoorbeeld de UI-test van het IntelliJ Platform Gradle Plugin).
- De test start vanzelf bij elke wijziging aan het product op main. Lees de uitslag met curl (de repo is openbaar):
  - laatste runs: `curl -s "https://api.github.com/repos/thijsduinhouwer2002-coder/dortus-hq/actions/runs?per_page=5"`
  - log van een job: `curl -sL https://api.github.com/repos/thijsduinhouwer2002-coder/dortus-hq/actions/jobs/<job-id>/logs`
- Laat de test opschrijven wat hij ziet (`console.log`), dan staat het bewijs in het log. Screenshots komen als artefact mee, maar die zijn alleen met een inlog te downloaden.
- Een product gaat pas naar indienen als de test in de echte app groen is **en** de ontwerper (Daan) akkoord heeft gegeven: bovenaan `producten/<product>/ontwerp.md` staat `Akkoord: ja` voor de huidige versie. Zie `organisatie/rollen/ontwerper.md`.
- De test zet zijn schermafbeeldingen openbaar op de tak `schermen` (map `<product>/<taknaam>/`). Zet die stap in elke nieuwe workflow, kopieer hem uit `.github/workflows/rollwright-e2e.yml`.
- Een product is voor de helft wat het doet en voor de helft hoe het eruitziet en voelt. Het moet **opvallen, speciaal zijn en mooi**; "netjes en geen fouten" is niet genoeg (besluit Thijs 7 nov 22:05). Denk vanaf het begin na over uiterlijk en gevoel, samen met Daan, niet pas aan het eind. Zie `organisatie/rollen/ontwerper.md`.
- De eerste lancering van elk product: Daan keurt de lijstplaatjes en de README; de hoofdchat zet het live en laat het Thijs zien in de samenvatting (aangepast 16 nov 21:12, was: ja van Thijs). Wordt de repo ooit privé, controleer dan of het lezen van de uitslag nog werkt.

## Skills in de repo (16 nov 2026)
In `.claude/skills/` staan vaste werkwijzen die elke agent kan laden: `bouwen-in-stappen` (elke functie of product: begrijpen, code verkennen, vragen, ontwerp met keuze, bouwen, keuren door een ander, samenvatten) en `frontend-design` (alles wat er goed uit moet zien: site, winkelplaatjes, menu's in het spel). Bouwers laden de eerste, Abel, Mila en Chris de tweede.

## Geplande runs (roestronde R7, 19 nov 2026)
Geplande runs zijn in deze repo niet betrouwbaar; gebruik de klok (organisatie/controle/klok.py) naast elke schedule. GitHub liet het dashboard ±elke 8 uur draaien in plaats van elk half uur, en de keurder van Hats en de wegwijzer nooit (GEZIEN 19 nov). Geef zo'n workflow daarom ook `push: branches: [main]` en als eerste job de klok (`klok.py <naam> <interval> [--paden ...]`, voorbeeld in `scorebord.yml`), met het oude paths-filter als `--paden` (een push die die bestanden raakt is altijd aan de beurt); de werkjob krijgt `needs: klok` en `if: needs.klok.outputs.beurt == 'ja'`. De laatste keer per taak staat op de tak `klok`; bekijken met `python3 organisatie/controle/klok.py stand`. De klokjob heeft `contents: write` nodig (alleen voor de tak `klok`). Pushes die een workflow zelf doet starten geen runs, dus de klok tikt alleen bij pushes van agents of Thijs. Raak de tak `klok` nooit met de hand aan: weghalen betekent voor elke taak "nog nooit gedraaid", dus ook een extra (betaalde) Hats-keuring.
