# Meting voor het tweede betaalde JetBrains-plugin (8 nov 2026, 13:40 tot 14:05 UTC)

Onderzoeker voor Jet. Alles met `curl` op de Marketplace-API (`https://plugins.jetbrains.com/api/...`) en de YouTrack-API, alleen gelezen. Scripts en ruwe uitvoer staan in de kladmap van deze sessie (niet in de repo); de API-routes zijn dezelfde als in `meet-betaald-2026-11-06.py`.

**Labels:** GEZIEN = zelf gemeten op 8 nov, met route. DERDEN = bron van een ander. GOK = schatting of oordeel.

**Twee waarschuwingen bij alle cijfers:**
- Elke update telt als download. Een plugin met veel versies lijkt groter dan hij is. Daarom staat bij elke plugin het aantal versies.
- "Per maand" = totaal gedeeld door maanden sinds de oudste zichtbare versie. Sommige makers verwijderen oude versies; dan lijkt de plugin jonger en het maandcijfer te hoog. Waar dat speelt staat het erbij.
- Een tweede maat, "nu": het verschil met de stand van 6 nov (16:00 tot 19:00 UTC, uit `marktmeting-2026-11-06.md` en de tsv-bestanden) tot nu, ±2 dagen. Klein getal, dus ruw (GOK als maandcijfer).

---

## A. Tcl (`*.tcl`)

**Aanraadlijst `*.tcl` nu (GEZIEN, `/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName=*.tcl`):** HDL and Vivado + MCP Support, Tcl Language Support. Ongewijzigd sinds 6 nov.

| | Tcl Language Support (id 31801) | HDL and Vivado + MCP Support (id 30907) |
|---|---|---|
| Model | gratis (AGPL, taalserver) | gratis |
| Downloads nu (GEZIEN, `/api/plugins/{id}`) | 2.746 | 1.952 |
| Stand 6/7 nov (marktmeting) | 2.727 (6 nov), 2.737 (7 nov) | 1.940 (6 nov), 1.946 (7 nov) |
| Groei "nu" | +19 in ±2 dagen, ruwweg 250 tot 300 per maand (GOK) | +12 in ±2 dagen |
| Versies | 15 | 3 |
| Eerste versie | 18 mei 2026 | 25 maart 2026 |
| Per maand sinds start | ±480 | ±260 |
| Downloads per versiemaand (GEZIEN, `/updates`) | mei 212, juni 1.094, aug 208, sept 1.190 | maart 157, april 1.137, aug 657 |
| Laatste versie | 2.2.5, 10 sept 2026 (689 downloads) | 1.0.0, 7 aug 2026 |
| until-build nieuwste versie | **262.\*** (CLion en IDEA tot 2026.2.4) | 251.0+ (open) |
| Werkt in 2026.3 (sinds 5 nov uit) | **nee** volgens Marketplace, nog steeds niet bijgewerkt | ja volgens de gegevens (niet getest) |
| Reviews (`/comments`) | 0 | 0 (1 stem, 5 sterren) |

**YouTrack (GEZIEN, `https://youtrack.jetbrains.com/api/issues?query=summary: tcl&fields=idReadable,summary,votes,resolved,created`):** 8 meldingen met Tcl in de titel. CPP-6388 "Tcl language support" (CLion) **38 stemmen, open sinds 2016**. De rest 0 stemmen (IDEA-297493, IDEA-172201, PY-25021 dicht; FL-29031 open). Hetzelfde als op 6 nov.

**GitHub (uit `grootte-soorten-2026-11-06.tsv`, 6 nov, niet opnieuw gemeten):** 2.150.400 bestanden, 1.415.168 groter dan 2 kB.

**Wat dit zegt (GOK):** de gratis Tcl-plugin staat sinds 10 september stil en is drie dagen na 2026.3 nog niet bijgewerkt. Wie in CLion 2026.3 een `.tcl` opent, krijgt alleen de Vivado-plugin aangeraden. Dat is precies het signaal uit het bouwbesluit om Tcl opnieuw te bekijken. Maar het blijft één punt: de groei van de gratis plugin is bescheiden (±250 tot 480 per maand) en er zijn geen reviews of klachten om op te bouwen.

---

## B. Graphviz DOT (`*.dot`, `*.gv`)

**Aanraadlijst nu (GEZIEN, zelfde route):**
- `*.dot`: DOT Language, DevTools, Dot Base, Dot Compat, Document Viewer (Word-sjablonen, `.dot` is ook een Word-extensie), Dot Plus.
- `*.gv`: DOT Language, Dot Base, Dot Compat, Dot Plus.
- Graphlume (betaald deel, KITSS) en DOT Studio staan **niet** in de lijst: ze melden de bestandssoort niet aan, dus de IDE raadt ze niet aan.

| Plugin (id) | Model | Downloads (GEZIEN) | Versies | Eerste / laatste versie | until-build nieuwste | Werkt in 2026.3? | Per maand sinds start | "Nu" (+ sinds 6 nov) |
|---|---|---|---|---|---|---|---|---|
| DOT Language (10312) | gratis | 154.587 | 12 | dec 2017 / **1 aug 2024** | 222.0+ (open) | volgens gegevens ja, niet getest | ±1.450; laatste versie 39.857 in 27 maanden, ±1.475 | +25 |
| Dot Base (27121) | gratis | 21.773 | 9 | apr 2025 / 21 apr 2026 | **261.\*** | **nee** (ook niet in 2026.2) | ±1.170 | +14 |
| Dot Plus (29772) | gratis, `approve: false` | 2.290 | 3 | jan 2026 / 28 apr 2026 | **261.\*** | **nee** | ±230 | +4 |
| Dot Compat (27597) | gratis | 191 | 1 | juni 2025 | 231.\* | nee | ±10 | 0 |
| DOT Studio (34732) | gratis | 109 | 1 | 3 okt 2026 | 262.\* | nee | ±90 | (nieuw) |
| Graphlume: DOT Graph Editor (35167) | **freemium, $10/jaar** | 30 | 1 | 18 okt 2026 | 243.0+ | ja | ±30 | +1 |

**Reviews DOT Language (GEZIEN, `/api/plugins/10312/comments` en `/rating`):** 25 sterrenstemmen, waarvan **10 keer 1 ster**, 7 keer 2, 1 keer 3, 3 keer 4, 4 keer 5. Klachten uit de laatste 2 jaar (letterlijk): "Freezes the UI" (dec 2024), "Never worked for me. I'm switching to PlantUML" (okt 2024), "after a few days it starts freezing WebStorm completely" (juni 2025), "runs on EVERY keystroke ... in order not to crash, you must type in another editor" (sept 2025), "It doesn't work" (jan 2025). Dot Base: 3 reviews, vraag om beter verversen en schuiven, en een gebruiker die Graphviz niet vond.

**Betaalde DOT-plugins:** alleen Graphlume (freemium, $10 persoonlijk en zakelijk per jaar, 30 downloads in 3 weken, niet aangeraden door de IDE). Geen andere betaalde of freemium plugin voor DOT gevonden (zoeken op `dot` 145 treffers en `graphviz` 16 treffers nagelopen).

**YouTrack (GEZIEN):** 8 meldingen met Graphviz in de titel; hoogste IJPL-71972 met 1 stem, IDEABKL-7173 "Graphviz syntax support" 0 stemmen, open sinds 2015. Geen vraag via stemmen.

**GitHub (uit `grootte-soorten-2026-11-06.tsv`, 6 nov):** `*.dot` 2.367.488 bestanden (1.107.968 groter dan 2 kB), `*.gv` 122.752 (52.864). Veel `.dot` wordt door tools gemaakt (Doxygen, compilers) en een deel is Word (GOK).

**Vergelijkbare markt die wel betaalt (GEZIEN, zie D):** Mermaid, ook een diagramtaal. Mermaid Studio (betaald, $4,90 per maand) 15.593 downloads in 9,3 maanden (±1.680 per maand, 42 versies) en Mermaid Studio Core (freemium) 26.831 in 7 maanden (±3.800 per maand, 33 versies). Veel versies blazen dat op; echte gebruikers misschien een derde (GOK).

**Wat dit zegt (GOK):** DOT heeft het patroon van een verlaten product met veel gebruikers: de grootste plugin (154.587, ±1.450 per maand gemiddeld) is ruim 2 jaar niet bijgewerkt en krijgt vooral 1-ster-reviews over bevriezen, en de jongere vervangers (Dot Base, Dot Plus) werken niet in 2026.2 en 2026.3. In 2026.3 raadt de IDE voor `.dot` dus vooral een slechte oude plugin aan. Zwak punt: geen stemmen in YouTrack en de "nu"-groei van DOT Language en Dot Base is samen maar ±40 in 2 dagen. Graphlume groeide niet, maar meldt de soort niet aan, dus het zegt weinig over de vraag.

---

## C. Nunjucks (`*.njk`)

**Aanraadlijst `*.njk` nu (GEZIEN):** Nunjucks Hero, Nunjucks. Ongewijzigd.

| | Nunjucks Hero (29567) | Nunjucks van obra (31592) | Nunjucks++ (33743) |
|---|---|---|---|
| Model | betaald, 7 dagen proef | betaald, 14 dagen proef | gratis |
| Prijs VS (GEZIEN, `/api/marketplace/plugin/{id}/prices?countryCode=US`) | $50 persoonlijk, $70 zakelijk, eerste jaar | $12 persoonlijk, $24 zakelijk, eenmalig (perpetual) | - |
| Downloads nu | 2.665 | 827 (de 3 zichtbare versies samen 495) | 86 |
| Stand 6 nov | 2.640 | 819 | - |
| "Nu" (± 2 dagen) | +25 | +8 | - |
| Versies | 5 | 3 | 1 |
| Eerste / laatste versie | 30 dec 2025 / 4 okt 2026 | 22 juli 2026 / 1 sept 2026 | 23 aug 2026 |
| Per maand sinds start | ±260 | ±230 | ±34 |
| Downloads per versiemaand | dec 47, jan 684, feb 351, maart 1.361, okt 222 | juli 231, sept 264 | aug 86 |
| until-build | 242.0+ (open) | 243.0+ (open) | 261.0+ |
| Reviews | 1, 5 sterren: "Great to finally see some Nunjucks support in IntelliJ ... well worth it!" | 0 | 0 |

**Gratis bijgehouden concurrentie:** alleen Nunjucks++ (1 versie, 86 downloads, staat niet in de aanraadlijst). Zoeken op `nunjucks` geeft maar deze 3 (GEZIEN).

**YouTrack (GEZIEN):** 2 meldingen met Nunjucks in de titel, beide 0 stemmen en dicht. Verwant: WEB-8743 "Jinja2 Templates" 29 stemmen, open.

**GitHub (6 nov, tsv):** 333.312 bestanden, 134.400 groter dan 2 kB (40%).

**Wat dit zegt (GOK):** er wordt al betaald voor Nunjucks, maar de markt is klein en al verdeeld over twee betaalde plugins van elk ±230 tot 260 downloads per maand, en de "nu"-groei is laag (+25 en +8 in 2 dagen). Een derde betaalde plugin moet die twee verslaan voor een klein publiek.

---

## D. Verse scan: betaalde en freemium plugins met eerste versie in 2026

**Hoe (GEZIEN):** alle betaalde (539) en freemium (358) plugins opgehaald via `/api/searchPlugins?max=20&offset=N&pricingModels=PAID|FREEMIUM&orderBy=downloads` (max mag alleen 20). Daarvan id 29300 of hoger en 1.100 downloads of meer: 76. Per plugin de versies via `/updates` en de prijs. 70 hebben hun oudste zichtbare versie in 2026.

**Top op downloads per maand (GEZIEN, prijs = persoonlijk, VS):**

| # | Plugin | Model, prijs | Downloads | Versies | Maanden | Per maand | Wat het doet |
|---|---|---|---|---|---|---|---|
| 1 | Agents Deck (Claude/Codex) | freemium, $3,90/mnd | 42.222 | 20 | 2,6 | ±16.000 | AI-codeeragents in de IDE |
| 2 | Key Explorer | freemium, $15/jaar | 16.718 | 1 zichtbaar | ±5 (GOK, oude versies verwijderd, reviews vanaf juni) | ±3.300 (GOK) | certificaten en keystores bekijken (`.jks`, `.p12`, `.pem`, `.crt`) |
| 3 | BatchCraft: Batch & CMD | betaald, $1/mnd | 9.585 | 3 | 1,1 | ±8.600; "nu" +531 in 2 dagen (9.054 op 6 nov) | Windows batch (`.bat`, `.cmd`) |
| 4 | EnvY | freemium, $4,90/mnd | 48.232 | 12 | 6,8 | ±7.000 | geheimen maskeren in terminal en logs |
| 5 | Mermaid Studio Core | freemium, $2,50/mnd | 26.831 | 33 | 7,0 | ±3.800 | Mermaid-diagrammen |
| 6 | Kronk CMS | freemium, $5,90/mnd | 31.135 | 17 | 9,1 | ±3.400 | CMS voor statische sites |
| 7 | Ayu Islands | freemium, $1,50/mnd | 20.568 | 48 | 8,4 | ±2.500 | thema |
| 8 | SQLite Lens | freemium, $5,90/mnd | 5.289 | 27 | 2,6 | ±2.000 | SQLite-bestanden bekijken |
| 9 | shadcn Helper | betaald, $2,90/mnd | 18.032 | 17 | 9,3 | ±1.940 | shadcn/ui-componenten |
| 10 | Flexible Swift / Flexible For Arduino | betaald $4,90 / freemium $2,90 | 13.730 / 13.463 | 45 / 39 | 7,3 | ±1.880 / ±1.840 | Swift-IDE / embedded |
| | Mermaid Studio | betaald, $4,90/mnd | 15.593 | 42 | 9,3 | ±1.680 | Mermaid (betaalde versie) |
| | XLSX Lens | freemium, $2,90/mnd | 3.664 | 31 | 2,6 | ±1.410 | Excel bekijken |
| | Jinja2 Enhanced Support | betaald, $3/mnd ($30/jaar) | 10.112 | 17 | 9,7 | ±1.050 | Jinja2-sjablonen |

Niet meegeteld omdat ze waarschijnlijk ouder zijn dan de zichtbare versies (GOK op basis van het id): Angular Architect (5.365, id uit ±mei, zichtbaar sinds 31 okt), Extra Tools Pack Lifetime en Extra Icons Lifetime (kopieën van bestaande plugins met een eenmalige licentie).

**Welke soorten groeien nu aantoonbaar (GOK, op deze cijfers):**
1. **AI en werkstroom** (Agents Deck, EnvY): de grootste, maar niet ons bouwpatroon.
2. **Bestandssoorten die de IDE niet kent**, met weinig versies dus echt: BatchCraft (3 versies, groeit nog ±280 per dag) en Key Explorer (1 zichtbare versie). Beide staan in de aanraadlijst van hun extensie. Key Explorer groeit zelfs met 7 andere plugins in dezelfde aanraadlijst (`*.jks`).
3. **Diagramtalen**: Mermaid Studio en Core samen ±5.500 per maand (wel 75 versies samen).
4. **Viewers voor databestanden** (de Lens-reeks: SQLite, XLSX, Parquet, heap dumps, ±500 tot 2.000 per maand, steeds ±30 versies).
5. **Sjabloon- en webtalen**: Jinja2 ±1.050, shadcn ±1.940, Nunjucks ±250, Astro ±365, Vue ±580.

---

## E. Eén extra: Jinja2 (`*.j2`, `*.jinja`), kort

Gekozen omdat het de dichtstbijzijnde verwant van Nunjucks is en de enige sjabloontaal in de top die met een taalplugin (Grammar-Kit-opbouw) groeit.

| | Jinja2 Enhanced Support (29804) |
|---|---|
| Model, prijs (GEZIEN) | betaald, $30 persoonlijk / $60 zakelijk per jaar |
| Downloads | 10.112, op 6 nov ±1.048 per maand (marktmeting deel 3) |
| Versies | 17, eerste 18 jan 2026, laatste 31 okt 2026 |
| Per versiemaand | jan 365, feb 1.587, maart 1.011, april 3.541, juni 132, juli 843, aug 1.329, okt 1.240 |
| Werkt in 2026.3 | ja, until-build 263.\* |
| Reviews | 0 |
| Aanraadlijst `*.j2` (GEZIEN) | OrchidE (Ansible), **Python (van JetBrains)**, Jinja2 Enhanced, SaltStack Toolkit, Rolewise for Ansible |
| Aanraadlijst `*.jinja` | Python, Jinja2 Enhanced, SaltStack Toolkit |
| YouTrack | WEB-8743 "Jinja2 Templates" 29 stemmen, open; WEB-42365 7 stemmen |

**Wat dit zegt (GOK):** Jinja2 laat zien dat een betaalde sjabloontaalplugin ±1.000 per maand kan halen, zelfs naast de Python-plugin van JetBrains (die alleen in PyCharm Pro en IDEA Ultimate zit). Maar de plek is bezet: Jinja2 Enhanced is bijgehouden en werkt in 2026.3. Geen gat voor ons. Bijvangst: Nunjucks lijkt sterk op Jinja2, maar haalt maar een kwart van de downloads.

---

## Eerlijk oordeel

**Sterkste marktbewijs: Graphviz DOT.**
- Verlaten product met veel gebruikers (GEZIEN): DOT Language 154.587 downloads, ±1.450 per maand gemiddeld, laatste versie augustus 2024, 10 van de 25 sterrenstemmen zijn 1 ster, met klachten over bevriezen en "doesn't work".
- De jongere gratis vervangers werken niet meer in de nieuwste IDE's (GEZIEN: Dot Base en Dot Plus until-build 261.\*, dus niet in 2026.2 en 2026.3). Samen hadden die ±1.400 downloads per maand gemiddeld.
- Veel bestanden: 2,37 miljoen `.dot` op GitHub, bijna de helft groter dan 2 kB (6 nov), al is een deel gegenereerd of Word (GOK).
- Er is geen betaalde concurrent die de IDE aanraadt. Graphlume (betaald deel) groeide niet, maar meldt `*.dot` niet aan, dus komt niet in de aanraadlijst. De les uit BatchCraft zegt dat dat juist het verschil maakt (GOK voor het verband).
- Een vergelijkbare diagramtaal, Mermaid, verkoopt aantoonbaar betaald en freemium (±1.700 en ±3.800 per maand, wel met veel versies).
- De taal is klein en past bij de opbouw van Bison & Flex (Grammar-Kit en JFlex). Extra werk: een voorbeeldweergave (Graphviz of een JS-renderer), en die moet niet bij elke toets opnieuw draaien, want dat is precies de klacht (GOK).
- **Wat tegen DOT spreekt:** nul stemmen in YouTrack, en de "nu"-groei van de bestaande plugins is laag (+25 en +14 in ±2 dagen). Het bewijs is "veel mensen installeren iets en zijn ontevreden", niet "mensen vragen erom". Ook botst `*.dot` met Word-sjablonen (Document Viewer staat in dezelfde lijst).

**Tweede: Tcl.** Echte vraag (38 stemmen in CLion, GEZIEN) en de gratis taalserver werkt nog niet in 2026.3 (until 262.\*, GEZIEN). Als die niet bijgewerkt wordt, ontstaat er een gat. Maar nu groeit hij maar ±250 tot 480 per maand, er zijn geen reviews of klachten, en hij kan elke dag een update krijgen. Advies: volgen, niet bouwen. Over 2 tot 4 weken opnieuw kijken naar de until-build.

**Valt af: Nunjucks.** Er wordt al betaald, maar door weinig mensen: twee betaalde plugins van elk ±230 tot 260 downloads per maand, samen +33 in 2 dagen, geen YouTrack-stemmen. Een derde betaalde plugin deelt een kleine taart. Ook Jinja2 (E) valt af: bezet door een bijgehouden betaalde plugin.

**Uit D:** de groeiers die bij ons passen zijn bestandssoorten die de IDE niet kent en die de IDE dus vanzelf aanraadt (BatchCraft, Key Explorer). Dat ondersteunt DOT meer dan de andere twee, omdat daar de aangeraden plugins slecht of kapot zijn.

**Hoe dun is het bewijs:** matig. Voor DOT is het bewijs een groot oud product met slechte reviews en kapotte opvolgers (GEZIEN), niet een gemeten betaalbereidheid voor DOT zelf. Voor de stap naar een bouwbesluit zou ik nog meten: (1) de "nu"-groei over een week van DOT Language en Dot Base, (2) of DOT Language echt bevriest of faalt in 2026.3 (IDE-test), (3) hoeveel `.dot` op GitHub echt Graphviz is (zoeken op `digraph`).
