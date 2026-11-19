---
name: uitbrengen
description: Gebruik dit als je een product of nieuwe versie live zet in een winkel (Blender, JetBrains, Obsidian, Garmin, Gumroad, Steam). Vaste volgorde, stopt bij de eerste fout.
---

# Uitbrengen

Afgekeken bij OpenStatus (`/ship`: vaste stappen, stop bij de eerste fout) en de winnaars uit `platformen/ideeen/afkijken-2026-11-18/`. Regels erachter: `organisatie/regels/uitbrengen.md`.

**Wie drukt op de knop?** De eerste lancering van een product, alles in een nieuwe winkel en elke prijswijziging: de hoofdchat, na Daan. Een update van een product dat al live staat: de eigenaar zelf via de workflow, na een keuring. Zo blijft het ritme van elke 2 tot 3 weken haalbaar.

Loop de stappen in volgorde. **Faalt er één: stop, schrijf in je logboek wat faalde en waarom, en ga niet verder.** Niets overslaan "omdat het vast goed is".

1. **Versie:** het versienummer in het manifest is nieuw en gelijk aan de kop in `CHANGELOG.md` (maak die met de skill `update-tekst`).
2. **Tests groen op precies deze commit:** unittests en de e2e-test in de echte app (GitHub Actions). Lees de uitslag met `curl` op de Actions-API, niet uit je geheugen.
3. **Keuring:** een ander keurde de wijziging (skill `keuren`), en bovenaan `producten/<naam>/ontwerp.md` staat `Akkoord: ja` van Daan voor deze versie als het uiterlijk of de winkelpagina veranderde.
4. **Lanceerlijst** uit `organisatie/regels/uitbrengen.md` nagelopen voor wat deze versie raakt (beloftes kloppen, beelden en prijs gelijk overal).
5. **Uitbrengen met de workflow** van het product, gestart door een tag te pushen (zie `organisatie/toegang.md`; "Run workflow" kan de ploeg niet) (bijvoorbeeld `click-joints-uitgave.yml`, `jetbrains-bison-flex-upload.yml`, `publiceer.sh release`). Geen workflow? Dan is het eerste werk er een maken (zie punt 1 van het ritme in de regels), niet met de hand uploaden.
6. **Controleren of het echt live is:** haal de winkelpagina of winkel-API op met `curl` en zie de nieuwe versie staan. Pas dan is het uitgebracht (les Bison & Flex 17 nov: goedgekeurd is niet zichtbaar).
7. **Vastleggen:** `organisatie/scorebord.md` (versie en datum), het bord via de hoofdchat, en de post of aankondiging als concept: voor TikTok en YouTube in `marketing/wachtrij/` (Roep keurt en plaatst), voor de Discord van Hats en andere plekken klaar voor de hoofdchat.

Wat alleen Thijs kan (eerste aanmelding bij een winkel, een sleutel aanmaken, betalen) meld je in `berichten/hoofdchat.md`, met precies wat hij moet doen; de hoofdchat zet het op de lijst voor Thijs.
