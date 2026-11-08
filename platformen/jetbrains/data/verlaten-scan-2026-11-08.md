# Verlaten gratis plugins: vraag NU (8 nov 2026, ±14:00 UTC, met curl)

Onderzoeker voor Jet. **Labels:** GEZIEN = zelf gemeten op 8 nov met de genoemde route. DERDEN = bron van een ander. GOK = schatting of oordeel.

**Hoe gemeten:** voor alle 219 plugins uit `verlaten-gratis-compat-2026-11-06.tsv` de downloads van nu opgehaald (`https://plugins.jetbrains.com/api/plugins/{id}`) en afgetrokken van de waarde van 6 nov. Dat is de groei in ongeveer 2 dagen (het precieze tijdstip van 6 nov staat niet in de tsv, dus GOK tussen 1,5 en 2,5 dag). De hele lijst, gesorteerd: `verlaten-groei-2026-11-08.tsv` (GEZIEN). Voor de beste kandidaten daarna `/updates`, `/comments`, `searchPlugins` en de aanraadlijst van de IDE (`/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName=*.<ext>`).

## 1. Het belangrijkste inzicht: een plugin die niet meer werkt, krijgt ook geen downloads meer

| Groep (van de 219) | Aantal | Groei in 2 dagen, samen | Mediaan per plugin |
|---|---|---|---|
| Zonder bovengrens (until leeg), dus nog te installeren | 138 | 10.339 | 25 |
| Met bovengrens | 81 | 1.118 | 3 |
| waarvan until onder 252 (werkt niet in 2025.2 en nieuwer) | 76 | 998 | |

(GEZIEN, `verlaten-groei-2026-11-08.tsv`.) Voorbeelden van geblokkeerde plugins: Requirements +4 (2,97 mln in totaal), IntelliBot +3, actiBPM +3, CodeGlance +8, YAML/Ansible +3, SnakeYAML +2, Catdea +1 (GEZIEN). Het teken uit de opdracht ("werkt niet meer, krijgt toch downloads") komt dus bijna niet voor. Uitzonderingen met until laag en toch wat groei: BashSupport +179 (shell zit al in elke IDE, en de maker verkoopt BashSupport Pro, DERDEN/niet gemeten), RESTFul-Tool +87, IDEA Jetty Runner +82, Minecraft NBT Support +64 (daar heeft een oudere versie zonder bovengrens nog 78.836 downloads, dus die wordt waarschijnlijk geïnstalleerd, GOK). De vraag loopt naar plugins die je nog kunt installeren, vooral via de aanraadlijst en de zoekfunctie van de IDE (GOK, past bij deel 6 van `marktmeting-2026-11-06.md`).

## 2. Top van de groei (thema's weggelaten; 15 van de 57 met 50 of meer zijn thema's)

| Plugin (id) | Groei 2 dagen | Per maand (GOK, x15) | Laatste versie, until | Past bij taal/bestand/viewer? | Vervanger in 2026.3 |
|---|---|---|---|---|---|
| ChinesePinyin-CodeCompletionHelper (14838) | +985 | ±15.000 | 2023-06, geen | nee (aanvullen met pinyin, Chinese markt) | niet gezocht |
| Batch Scripts Support (265) | +785 | ±12.000 | 2021-12, geen | ja, `.bat`/`.cmd` | **BatchCraft (34804), betaald, al bezet** |
| CMD Support (5834) | +603 | ±9.000 | 2015-03, geen | ja, `.bat`/`.cmd` | idem |
| Indent Rainbow (13308) | +364 | ±5.500 | 2023-07, geen | nee, editor-opsmuk | werkt zelf nog; nieuw: Strata (freemium, okt 2026), IndentScope (gratis, okt 2026) |
| TestMe (9471) | +324 | ±4.900 | 2024-09, geen | nee, testgenerator | niet gezocht |
| Rainbow CSV (12896) | +196 | ±2.900 | 2022-05, geen | ja, `.csv` viewer | CSV Editor (10037, 13,8 mln, nieuwste versie 7 nov 2026); betaald CSV Color Pro (9.623, until 252) |
| Adapter for Eclipse Code Formatter (6546) | +176 | ±2.600 | 2024-09, geen | nee | niet gezocht |
| nginx Support (4415) | +68 | ±1.000 | 2019-10, geen | ja, config | niet gezocht (JetBrains-aanbod niet gemeten) |
| Minecraft NBT Support (12839) | +64 | ±950 | 2022-12, 223 | ja, viewer | Minecraft Development (8327, 2,4 mln) staat ook bij `*.nbt` in de aanraadlijst (GEZIEN) |

Alle groeicijfers GEZIEN; per maand is een GOK (2 dagen keer 15, en elke update telt als download, maar deze plugins brengen geen updates meer uit, dus hier zijn downloads vrijwel allemaal nieuwe installaties, GOK).

## 3. De drie beste, eerlijk bekeken

### A. Windows Batch (`.bat`, `.cmd`): de vraag is groot en echt, maar het gat is al gevuld
- **Groei nu (GEZIEN):** Batch Scripts Support +785 en CMD Support +603 in 2 dagen. Samen ±1.390, ongeveer 20.000 per maand (GOK). Bijna alles op de laatste versie (1.168.451 en 2.134.045).
- **Waarom:** beide staan in de aanraadlijst voor `*.bat` en `*.cmd` (GEZIEN), en `gradlew.bat`/`mvnw.cmd` zit in heel veel projecten (zie `marktmeting-2026-11-06.md` deel 6).
- **Klachten (GEZIEN, `/comments`):** CMD Support: "Does not work" (sept 2025), "Doesn't work" (maart 2025), "doesn't work" (juni 2024), weinig commando's en geen kleur voor variabelen (2018). Batch Scripts Support: "This plugin looks abandoned" (april 2025), wil meer kleur voor if/else/setlocal (sept 2024), %ERRORLEVEL% fout (2023), typen van ":" breekt de kleuren (2021), twee plugins die elkaar bij elke start de `.bat` afpakken (2021).
- **Vervangers (GEZIEN):** BatchCraft van KITSS TECH, betaald met 7 dagen proef, sinds 5 okt 2026, 9.585 downloads nu (9.054 op 6 nov, dus +531 in 2 dagen), staat in de aanraadlijst, adresseert letterlijk de klachten hierboven (losse ":" breekt niets, waarschuwt bij een tweede batch-plugin). Verder klein en gratis: BatchUI (8.702, until 243), CmdSupport (3.791, alleen acties), Batch Files Support (124, juli 2026), Batch Script Support (70, sept 2026).
- **Oordeel (GOK):** de oude gratis plugins krijgen nog steeds ruim 2,5 keer zoveel downloads als BatchCraft. Er is dus ruimte voor een gratis basis met betaalde extra's naast een volledig betaald product. Maar we zouden de zesde batch-plugin zijn, BatchCraft is een maand oud en goed gemaakt, en dit was in deel 6 al als "bezet" beoordeeld. Past perfect bij Grammar-Kit/JFlex. **Alleen te overwegen als Jet bewust een freemium-aanval op BatchCraft wil.** Niet mijn advies.

### B. CSV (`.csv`): vraag ja, gat nee
- **Groei nu (GEZIEN):** Rainbow CSV +196 in 2 dagen.
- **Klachten (GEZIEN):** blokkeert "open as table" in nieuwe IDE's (juli 2024), traag bij lange bestanden (2022), knippert bij plakken (2020). Een reviewer wijst zelf naar CSV Editor.
- **Vervangers (GEZIEN):** CSV Editor, 13,8 mln, 40 versies sinds 2023, bijgewerkt 7 nov 2026, staat bovenaan de aanraadlijst voor `*.csv`; daarnaast de database-tools van JetBrains en de betaalde CSV Color Pro (9.623 downloads, laatste versie mei 2025, until 252, dus werkt niet in 2026.1 en nieuwer).
- **Oordeel (GOK):** er is betaald aanbod in de buurt en het is een viewer, maar de gratis marktleider wordt actief onderhouden. Geen kandidaat.

### C. Indent Rainbow: vraag ja, maar geen taal of viewer
- **Groei nu (GEZIEN):** +364 in 2 dagen, werkt volgens reviews nog ("Does exactly what I want and I don't need to pay a monthly fee", okt 2026). Klachten: gekleurde blokken leiden af (dec 2025), wil één kleur met verloop (maart 2026), crash in 2024.2 (aug 2024).
- **Vervangers (GEZIEN):** Strata: Rainbow Indents (freemium, sinds 18 okt 2026, 137 downloads), IndentScope (gratis, okt 2026, 168), en Rainbow Brackets (freemium, 25 mln).
- **Oordeel (GOK):** de originele plugin werkt nog en is gratis, en er zijn al twee nieuwkomers. Past niet bij onze aanpak. Geen kandidaat.

## 4. Oordeel
- **Er komt geen goede tweede kandidaat uit deze lijst.** Van de 219 krijgen alleen plugins die nog te installeren zijn echte downloads. De enige taal- of bestandssoort met grote vraag nu is Batch (±20.000 per maand, GOK), en die heeft sinds oktober een betaalde concurrent die in de aanraadlijst staat. CSV, nginx en NBT hebben een onderhouden gratis vervanger of te weinig vraag. De rest is thema's, opsmuk of codegeneratie.
- **Wat dit wel leert (GOK):** "verlaten" is geen goed zoeklicht. Groei zit bij wat de IDE zelf aanraadt of wat goed vindbaar is. Een volgende scan kan beter beginnen bij de aanraadlijst per bestandssoort (zoals deel 7) en daar de groei in 2 dagen meten van de aangeraden plugins, in plaats van bij verlaten plugins.
- **Niet gedaan:** ChinesePinyin, TestMe en Eclipse Formatter niet verder uitgezocht (passen niet bij taal of viewer). nginx niet nagelopen op een JetBrains-plugin of vervanger. Groei is één meting over ongeveer 2 dagen; een tweede meting over een week maakt de getallen steviger.
