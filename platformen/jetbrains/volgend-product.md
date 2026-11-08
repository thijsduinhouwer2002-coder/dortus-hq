# JetBrains: voorstel tweede product (Jet, 8 nov 2026)

**Stand (8 nov 14:10 UTC): nog NIET ter beslissing bij Hans.** Controleur: akkoord nee (cijfers kloppen, maar het bewijs voor vraag nu is te dun en een directe gratis concurrent, DOT Studio, ontbrak). Volgens de regel is dun bewijs nee. Wat nodig is voor een ja staat onderaan; eerste moment 15 nov (weekmeting).

**Voorstel:** een freemium plugin voor **Graphviz DOT** (`*.dot`, `*.gv`) in alle JetBrains-IDE's: de taal goed in de editor, plus een voorbeeld dat in de IDE zelf tekent, zonder Graphviz te installeren en zonder de IDE te laten hangen. Werknaam "Graphviz voor JetBrains" (naam kiezen met Daan en Chris). Hans beslist; zonder zijn ja wordt er niet gebouwd. Alle cijfers: `data/volgend-product-meting-2026-11-08.md` (gemeten 8 nov met curl en `gh api`, tenzij anders vermeld).

**Belofte in één zin:** Graphviz-diagrammen schrijven in je JetBrains-IDE met een snel live voorbeeld dat meteen werkt, zonder Graphviz te installeren en zonder dat de editor bevriest; Pro maakt het voorbeeld klikbaar en exporteert.

**Voor wie:** ontwikkelaars die afhankelijkheden, toestandsmachines, architectuur of datastromen als `.dot` bijhouden, in IntelliJ, PyCharm, CLion, GoLand, WebStorm en de rest.

## Het marktbewijs (zelf gezien)
- **Verlaten product met veel gebruikers.** DOT Language (id 10312): 154.587 downloads, laatste versie 1 aug 2024; die laatste versie alleen al 39.857 downloads in 27 maanden, ±1.475 per maand (GEZIEN, `/api/plugins/10312/updates`). Van de 25 sterrenstemmen zijn er 10 één ster en 7 twee sterren (GEZIEN, `/rating`).
- **Klachten in reviews, letterlijk:** "Freezes the UI" (dec 2024), "after a few days it starts freezing WebStorm completely" (juni 2025), "runs on EVERY keystroke ... in order not to crash, you must type in another editor" (sept 2025), "It doesn't work" (jan 2025), "Never worked for me. I'm switching to PlantUML" (okt 2024) (GEZIEN, `/api/plugins/10312/comments`).
- **De jongere vervangers werken niet meer.** Dot Base (21.773 downloads, ±1.170 per maand sinds april 2025) en Dot Plus (2.290) hebben until-build 261.\*: niet te installeren in 2026.2 en 2026.3 (GEZIEN). Een Dot Base-gebruiker klaagt dat Graphviz niet gevonden werd.
- **Veel en echte bestanden.** `*.dot` 2.375.680 bestanden op GitHub, waarvan 2.248.704 het woord `digraph` bevatten, dus vrijwel allemaal Graphviz en geen Word-sjabloon (GEZIEN 8 nov, `gh api search/code`, schattingen van GitHub). Op 6 nov was 47% groter dan 2 kB (GEZIEN, `data/grootte-soorten-2026-11-06.tsv`). Een deel wordt door tools gemaakt (Doxygen, compilers) en hoeft niet met de hand geschreven te zijn (GOK hoeveel).
- **Mensen betalen voor een diagramtaal in de IDE.** Mermaid Studio (betaald, $4,90 per maand) ±1.680 downloads per maand, Mermaid Studio Core (freemium) ±3.800 per maand (GEZIEN; veel versies blazen dat op, GOK een derde zijn echte gebruikers).
- **De IDE zet ons product zelf voor de gebruiker.** Voor `*.dot` raadt de Marketplace nu DOT Language, DevTools, Dot Base, Dot Compat, Document Viewer en Dot Plus aan (GEZIEN, `getImplementations`); Dot Base en Dot Plus werken daarvan niet in 2026.2 en 2026.3 (GEZIEN); DOT Language werkt volgens zijn gegevens wel, maar is niet in 2026.3 getest, en DevTools en Document Viewer zijn niet nagekeken. Een plugin die de soort aanmeldt komt in die lijst (zo groeide BatchCraft, deel 6 van de marktmeting, GOK voor het verband).

**Zwak in het bewijs (eerlijk):** geen stemmen in YouTrack (IDEABKL-7173 "Graphviz syntax support" 0, open sinds 2015; hoogste melding 1 stem, GEZIEN). De groei nu is laag gemeten: DOT Language en Dot Base samen +39 in 2 dagen, en dat waren vrijdag tot zondag (GEZIEN, één meting). Het bewijs is "veel mensen installeren iets en zijn ontevreden", niet "mensen vragen erom". Dat is precies de soort "verlaten product met veel gebruikers" en "klachten in reviews" uit de regel, maar de omvang van nu is nog niet over een week gemeten.

## De 3 sterkste concurrenten en waarom wij beter zijn
| Concurrent | Wat het is | Waarom wij beter |
|---|---|---|
| DOT Language (gratis, 154.587) | kleuren en voorbeeld, sinds aug 2024 stil | belofte, nog niet gemeten: bevriest niet (tekenen buiten de editor-draad, pas na een pauze in het typen), echte foutmeldingen, ga naar definitie en hernoemen van knopen, bijgehouden voor elke nieuwe IDE |
| Dot Base (gratis, 21.773) | voorbeeld met een geïnstalleerde Graphviz | werkt in 2026.2 en 2026.3; tekent zonder Graphviz te installeren (Graphviz als WebAssembly in de ingebouwde browser van de IDE, GOK dat dit snel genoeg is, eerst bewijzen) |
| DOT Studio (gratis, open source, 109 downloads, 3 okt 2026, until 262.\*) | volgens zijn eigen beschrijving al meegeleverde Graphviz (viz-js, WASM), live voorbeeld in JCEF, lay-out kiezen, export SVG en PNG, zoomen, structuur en fouten (GEZIEN door de controleur) | nog niet in 2026.3 en niet in de aanraadlijst (meldt de soort niet aan); maar met één update is hij dat wel. Ons verschil is daardoor klein: klikbaar voorbeeld, PDF, IDE-themakleuren, ga naar definitie en hernoemen (GOK dat dat genoeg is). Dit is het zwakste punt van het voorstel |
| Graphlume (freemium, $10 per jaar, 30) | grafische editor voor DOT | meldt `*.dot` wel aan, dus de IDE raadt ons aan; taal en voorbeeld in één |

## Hoe het geld oplevert
Freemium zoals Bison & Flex (zelfde betaalroute, licentiecode, proef van 30 dagen, Annual). Gratis, rustig (beter dan DOT Language en Dot Base, GOK; DOT Studio geeft voorbeeld en export ook al gratis): taal (kleuren, fouten, folding, structuur, ga naar definitie en hernoemen in het bestand, aanvullen van attributen) en een live voorbeeld. Pro, duidelijk speciaal: klikbaar voorbeeld (klik op een knoop en de editor springt naar de regel, en terug), export naar SVG, PNG en PDF, andere lay-outs (dot, neato, fdp, circo), zoeken en inzoomen in grote grafen, voorbeeld in de kleuren van het IDE-thema. Prijs voorstel $19 / $49 per jaar zoals Bison & Flex (Chris kijkt mee). Opbrengst (GOK op GOK): neemt dit de aanraadstroom van ±1.000 tot 1.500 downloads per maand over en betaalt 2 tot 5%, dan zijn dat na een jaar enkele honderden betalers, ruwweg €150 tot €500 per maand. Dat is meer dan Bison & Flex (±200 per maand op de oude concurrent) en telt mee voor de tussenstap van €300 tot €400 in maart.

## Hergebruik en risico's
- Hergebruik: Grammar-Kit en JFlex, bouwsjabloon, CLion/IDEA-tests en Plugin Verifier op Actions, e2e met schermen voor Daan, licentie en proef (`pro/`), uploadsleutel zodra Thijs die zet.
- Nieuw werk: het voorbeeld in de ingebouwde browser (JCEF). Eerst een proefje: tekent een graaf van 300 knopen in een paar honderd ms zonder de editor te blokkeren? Lukt dat niet, dan wordt het voorbeeld de zwakke plek en is het antwoord nee.
- Licentie: @hpcc-js/wasm 2.36.0 is Apache-2.0 en Graphviz EPL-2.0 (GEZIEN door de controleur). In een gesloten betaalde plugin mag dat als we Graphviz niet aanpassen, de licenties meeleveren en de bron van de Graphviz-delen beschikbaar maken (GOK, DOT Studio doet het zo).
- Twee plugins die allebei `*.dot` aanmelden: bij gebruikers met DOT Language erbij kiest de IDE er één; nagaan in de IDE-test.
- Nog te meten vóór het bouwbesluit valt (kan parallel aan het ontwerp): groei van DOT Language en Dot Base over een week (15 nov), en in een IDE-test of DOT Language in 2026.3 echt bevriest.

## Betaalbereidheid-scan (8 nov 16:10 UTC)
Alle 897 betaalde en freemium plugins gemeten (`data/betaalbereidheid-scan-2026-11-08.md`, nagekeken, akkoord ja). Geen niche met sterk bewijs én een open gat. Ansible heeft het sterkste betaalbewijs (OrchidE $59 per jaar, 355.579 downloads, 23 van 54 stemmen 1 of 2 sterren, PY-23226 49 stemmen, GEZIEN), maar er zijn al twee betaalde plugins en het is veel werk: bewaren als grotere kandidaat, niet als snelle tweede. Excel bewerken en HDL: dun. Wolfram, QML, Latte: nee. Wat de scan wel laat zien (GOK): betaald loont waar de IDE een slechte gratis plugin aanraadt. Dat steunt het DOT-spoor; weekmeting 15 nov blijft het beslismoment.

## Afgevallen
- **Tcl:** echte vraag (CPP-6388, 38 stemmen), maar de gratis Tcl Language Support met taalserver bestaat, en kan elk moment bijwerken voor 2026.3 (nu until 262.\*, laatste versie 10 sept). Over 2 tot 4 weken opnieuw kijken.
- **Nunjucks:** klein (twee betaalde plugins samen ±500 per maand) en al verdeeld.
- **Jinja2:** groeit (±1.050 per maand betaald), maar bezet door een bijgehouden plugin die in 2026.3 werkt.

## Wat nodig is voor een ja (controleur 8 nov 14:05, overgenomen)
1. Weekmeting op 15 nov: groeien DOT Language en Dot Base samen met ruwweg 1.000 per maand of meer? Op 8 nov was het +39 in 2 dagen (±600 per maand, één weekendmeting). Lager: nee.
2. Een Pro-pakket dat duidelijk verder gaat dan wat DOT Studio gratis geeft, anders is er geen reden om te betalen.
3. Bewijs dat iemand voor DOT betaalt ontbreekt: de enige betaalde DOT-plugin (Graphlume) heeft 30 downloads, maar wordt niet aangeraden. Mermaid is een vergelijkbare markt, geen bewijs voor DOT.
4. IDE-test in 2026.3: bevriest DOT Language echt, en wat doet DOT Studio.
Niet gehaald: verder zoeken (Tcl over 2 tot 4 weken opnieuw; viewers zoals Key Explorer en de Lens-reeks groeien, deel D van de meting).

## Tweede spoor uit de scan van 8 nov (nog niet nagekeken door een controleur)
Scan van alle 219 verlaten gratis plugins op groei in 2 dagen (`data/verlaten-scan-2026-11-08.md`, `data/verlaten-groei-2026-11-08.tsv`). Les (GEZIEN): plugins die niet meer in nieuwe IDE's werken krijgen bijna niets meer (mediaan 3 in 2 dagen); de vraag gaat naar wat nog te installeren is. Enige uitschieter: **Batch** (`.bat`, `.cmd`): de oude gratis Batch Scripts Support +785 en CMD Support +603 in 2 dagen (GEZIEN), met klachten "Does not work" en "looks abandoned"; BatchCraft (betaald, $1 per maand, geen gratis deel) +531 in dezelfde dagen. Dus nog altijd kiezen meer mensen een kapotte gratis plugin dan de betaalde (GOK op één meting). Een freemium Batch-plugin met een sterk gratis deel zou die stroom kunnen pakken, maar gaat recht tegen KITSS TECH in. Volgende run: dit nameten en afwegen tegen DOT, met een controleur.

**Afweging Batch (8 nov 15:00 UTC, nagekeken door een controleur): nee voor nu.** Vraag is er, betaalbereidheid niet bewezen; BatchCraft (betaald, sterk) dekt bijna alles wat een Pro kan bieden. De IDE laat de gebruiker kiezen uit de aanraadlijst (geen automatische installatie van alle plugins, broncode intellij-community). Downloadtellers verversen één keer per dag. Details: `data/batch-afweging-2026-11-08.md`.
