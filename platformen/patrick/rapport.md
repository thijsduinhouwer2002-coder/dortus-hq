# Rapport Patrick, perfectionist (nacht 9 op 10 nov 2026)

Stand: concept na run 1 (9 nov 23:15 NL). Wordt elke run scherper; de run van 07:13 maakt hem af.
Bewijs staat in `bevindingen.md`, bronnen van buiten in `bronnen/internet.md`. Volledige nieuwe teksten komen in `voorstellen/`.

## Eerst de harde waarheid
In drie dagen maakte de ploeg 1.640 commits. Opbrengst: één product live (Rollwright, 19 downloads, 0 verkopen), twee in keuring, 0 euro. Bouwen gaat snel; wat traag gaat is kiezen, afmaken en uitbrengen. De opzet beloont drukte (commits, logboeken, onderzoek) in plaats van uitkomst (lancering, installs, geld). Daarnaast leest elke run 80 tot 130 KB voordat hij iets doet, uit instructies die op drie plekken staan en elkaar tegenspreken.

## Top 5 (concept)

### 1. Leeswerk per run van ±100 KB naar ±15 KB
- **Wat er mis is:** elke run moet CLAUDE.md, doelen (5 KB), regels (13 KB), besluiten (56 KB), een rol (4 tot 8 KB), het eigen berichtenbestand (Olaf 42 KB, Daan 32 KB) en de eigen map lezen. 8 Claudes elk uur = ±192 runs per dag. Anthropic zegt: CLAUDE.md onder 200 regels, langer "reduce adherence", en verwijzen of verplicht laten lezen bespaart niets (bron 1, 2, 5).
- **Voorstel:** CLAUDE.md wordt een index van ±40 regels. `besluiten.md` alleen nog de besluiten die nu gelden (±30 regels), de rest naar `organisatie/archief/besluiten-2026-11.md`. Per platform één `status.md` van hooguit 25 regels die de eigenaar elke run bijwerkt. Berichtenbestanden: verwerkte berichten naar een archief.
- **Oplevert:** minder verbruik per run (GOK: een kwart tot een derde), en betere naleving omdat de belangrijke regels niet verdrinken.
- **Werk:** 1 run van de hoofdchat. **Gewoon goed**, geen keuze van Thijs.

### 2. Eén plek per instructie; geplande opdrachten kort en gelijk
- **Wat er mis is:** de opdrachten van de geplande taken zijn verouderd en spreken de besluiten tegen. Olaf krijgt elk uur nog "eerst alleen de ideefase, Thijs kiest" (achterhaald 19:20). Hans krijgt elke run "nieuwe platformen zijn nu de hoofdzaak" (zoekers uit sinds 18:30). `geplande-taken.md` is van 7 nov en mist vijf taken. De leeslijst staat in CLAUDE.md, in de rol en in de opdracht, en is overal anders. Anthropic: bij tegenspraak kiest Claude willekeurig (bron 7).
- **Voorstel:** elke geplande opdracht is dezelfde korte tekst van ±8 regels: wie je bent, lees CLAUDE.md, volg `organisatie/rollen/<rol>.md`, vaste veiligheidsregels, afsluiten. Alles wat verandert (taken, team, prioriteit) staat alleen in de rol of in `status.md`, nooit in de opdracht. Dan hoeft een besluit nooit meer in 8 opdrachten te worden aangepast.
- **Oplevert:** geen verouderde opdrachten meer, minder fouten, een besluit werkt meteen door.
- **Werk:** 1 run van de hoofdchat (opdrachten bijwerken met update_trigger). **Gewoon goed.**

### 3. Sturen op lancering en geld, niet op drukte
- **Wat er mis is:** 20% van de commits raakt alleen logboeken en lijsten. De zoekers maakten 410 commits voor één nieuwe 7. De meetlat voor een 8 eist dat kleine makers er nu verdienen én dat wij binnen 2 weken bouwen én dat Thijs binnen een week zonder kosten verkoopt: platforms waar wél verdiend wordt hebben juist drempels (Steam $100, TikTok KvK), dus een 8 kan bijna niet bestaan. Op 9 nov veranderde zes keer wie wanneer draait.
- **Voorstel (keuze Thijs):** hooguit 3 producten tegelijk, elk met een lanceerdatum en een eigenaar. Elke run eindigt met één ding dat dichter bij uitbrengen of geld is, of stopt in twee regels. Het dashboard toont per product: dagen tot lancering, installs, euro's, in plaats van commits. Meetlat: weeg product plus platform samen op "verwachte euro's in 60 dagen" in plaats van vier eisen tegelijk.
- **Oplevert:** sneller de eerste euro, minder verbruik aan onderzoek en heen en weer.
- **Werk:** klein in tekst, groot in gewoonte. **Keuze van Thijs** (ploeggrootte en hoeveel tegelijk).

### 4. De lijst voor Thijs op één scherm
- **Wat er mis is:** `lijst-thijs.md` is 82 KB, vooral doorgestreepte alinea's. Thijs wil in één blik zien wat er van hem nodig is.
- **Voorstel:** bovenaan alleen "Wacht op jou" (hooguit 3 punten, elk: wat, waarom in één zin, minuten, link). Afgehandeld gaat dezelfde dag naar een archief. Ter info hoort op het dashboard, niet op de lijst.
- **Werk:** 1 uur. **Gewoon goed.**

### 5. Repo afslanken: data en films uit de hoofdtak
- **Wat er mis is:** `.git` is 2,7 GB. `platformen/verkenner` is 141 MB aan ruwe data (een json van 16 MB), demo-GIF's van 9 MB staan dubbel. In deze run liep `git fetch` na 2 minuten vast. Elke run betaalt dit.
- **Voorstel:** ruwe data (`*/data/`) en tussenversies van films niet meer in git (in `.gitignore`), maar als artefact van een Actions-run of op een aparte tak. Alleen samenvattingen in markdown.
- **Werk:** 1 run voor de regel; de oude geschiedenis opruimen is een keuze (zie later).

## Wat nog komt
Run 2 tot 4: volledige nieuwe teksten in `voorstellen/` (CLAUDE.md, regels.md, besluiten.md opgesplitst, status.md-sjabloon, opdracht-sjabloon, lijst-thijs.md), rollen nalopen, meer bronnen over samenwerking en meldingen.
