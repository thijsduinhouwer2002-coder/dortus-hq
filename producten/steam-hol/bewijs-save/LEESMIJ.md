# Bewijs: de save gaat nooit stilletjes weg (issue #194, Olaf 26 nov)

**Wat de speler merkt:** gaat de pc uit terwijl Hats bewaart (stroom, Windows-update, harde uitschakeling), dan is het hol er bij openen nog. Een kapotte save blijft bewaard als `hol.kapot.json`, het hol komt uit `hol.vorige.json`. Een save van een oudere versie wordt `hol.v<versie>.json` in plaats van overschreven.

**Hoe:** `kern/veilig_bestand.gd` schrijft naar `hol.json.tmp`, leest terug of alles erin staat, zet de oude `hol.json` om naar `hol.vorige.json` en dan de `.tmp` naar `hol.json`. Eerst weghalen, dan hernoemen, nooit hernoemen over een bestaand bestand heen (werkt zo op Windows en Linux gelijk). Een onleesbare `hol.json` schuift nooit door naar de vorige. Les uit Antimatter Dimensions (MIT, `organisatie/lat/broncode/antimatter-dimensions.md`), alleen het idee, geen code.

**Toets** `systemen/toetsen/toets_opslag.gd` (eigen map `user://toets_opslag/`, raakt de save van de speler niet): 23 keer OK, 0 FOUT op Linux (GEZIEN, `toets_opslag-linux.txt`). Onder meer:
- 10 bewaarrondes: precies `hol.json` en `hol.vorige.json`, geen `.tmp`.
- half geschreven en lege `hol.json`: goud en hoeden uit `hol.vorige.json` terug, `hol.kapot.json` bestaat nog en wordt nooit overschreven (een tweede kapotte komt ernaast).
- pc uit tussen de twee keer hernoemen, halve `.tmp`, oudere versie, onleesbare `hol.json` bij bewaren.

**Echt spel** (GEZIEN, Linux xvfb, strook 120, Godot 4.3): run 1 van 70 s bewaarde goud 50 in `hol.json` en 38 in `hol.vorige.json`. Daarna `hol.json` op de helft afgekapt zoals een harde uitschakeling midden in het schrijven. Run 2 logde (`run2-na-kapot.log`):

    HOL opslag onleesbaar, bewaard als hol.kapot.json
    HOL opslag geladen uit hol.vorige.json
    HOL opslag geladen: 0 terugkomers, 38 goud, faam 2

Vroeger gaf dit een vers begin en overschreef de eerste bewaarronde het kapotte bestand.

**Windows:** de toetsrun van `steam-hol.yml` draait de nieuwe toets mee; de duurtest van 60 min (`steam-hol-duur.yml`) is rood als er na ±120 bewaarrondes iets anders staat dan `hol.json` en `hol.vorige.json`. Uitslag in het issue.

**Duurtest Windows** (run 45857850884, commit 874cb99, GEZIEN in `steam-hol-duur/main/uitslag.txt` op de tak schermen): groen, 60 min, proces leefde tot het eind, geen scriptfout, daarna `save-bestanden: hol.json, hol.vorige.json`. CPU in de editor gemiddeld 1,90 CPU-s per 10 s, vorige duurtest (483f1cb) 1,92: gelijk binnen de ruis van de runner.
