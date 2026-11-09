# Bison & Flex (JetBrains): lancering

Door Chris, 7 nov 2026, bijgewerkt 8 nov 2026 (run 4 en run 9, zie onderaan wat er veranderde). Concepten. Plaatsen gebeurt via de hoofdchat of Thijs na een besluit van Hans over de plekken (zie Stand); ik zet ze pas op `organisatie/lijst-thijs.md` als de plugin goedgekeurd en met één klik te installeren is (beoordeling door JetBrains duurt tot 2 werkdagen, DERDEN [release-plugin](https://plugins.jetbrains.com/docs/marketplace/release-plugin.html)).

## Waarom kanalen buiten de IDE nodig zijn
Het aanraden door de IDE bij een onbekend `.l`-bestand keurt JetBrains apart goed, en kan het weigeren voor nieuwe plugins zonder geschiedenis (DERDEN, approval guidelines, zie `winkeltekst.md` run 3). De eerste weken moeten installs dus komen uit (1) zoeken op de Marketplace en (2) een paar gerichte plekken waar mensen precies dit missen.

## Waar de mensen zitten (gemeten 7 en 8 nov)
| Plek | Bewijs | Wat |
|---|---|---|
| Zoeken op de Marketplace | Bison Language Support (alleen `.y`) heeft 13.020 downloads en een score van 3,41 (GEZIEN 7 nov). Recentste reviews: "Not reliable. Frequently crashes and reverts to all white text on black background." (2 sterren, dec 2025) en "Do you know something similar for the lex files?" (maart 2025) (GEZIEN 8 nov, `plugins.jetbrains.com/api/plugins/16595/comments`) | naam, eerste zin en tags goed (zie `winkeltekst.md`); dit is de grootste groep die nu al zoekt |
| In de IDE zelf | bij `.l` raadt CLion nu geen enkele plugin aan (GEZIEN 7 nov) | niets doen; komt misschien later |
| YouTrack [IDEABKL-7544](https://youtrack.jetbrains.com/issue/IDEABKL-7544) "Handling Yacc and Flex (Bison) markup" | 8 stemmen, 7 reacties, open sinds 2013 (GEZIEN 7 nov) | concept A |
| YouTrack [IDEABKL-4162](https://youtrack.jetbrains.com/issue/IDEABKL-4162) "Allow user to define custom file types by inputting Flex and Yacc grammar files" | 2 stemmen, 1 reactie, open sinds 2005 (GEZIEN 8 nov) | concept A, zelfde tekst |
| YouTrack [CPP-1122](https://youtrack.jetbrains.com/issue/CPP-1122) "Support for flex and bison" | 1 stem, 3 reacties, status Won't fix (GEZIEN 8 nov): JetBrains bouwt het zelf niet | concept A, alleen als reageren daar nog kan |
| Stack Overflow [49288299](https://stackoverflow.com/questions/49288299/syntax-highlighting-for-lex-files-in-clion) "Syntax highlighting for Lex files in CLion" | 1.238 keer bekeken, 0 antwoorden (GEZIEN 8 nov, Stack Exchange API) | concept B, alleen als Thijs zelf schrijft (regel AI, zie onder) |
| r/Compilers op Reddit | 25.000 tot 33.000 leden (DERDEN, [gummysearch](https://gummysearch.com/r/Compilers), [sentinel](https://reddit.sentinel-team.org/subreddits/Compilers)); regels niet zelf kunnen lezen, Reddit weigert curl vanaf hier | concept C, alleen na het lezen van de regels |
| Hacker News, "Show HN" | soms veel bereik voor gereedschap voor ontwikkelaars, vaak niets (GOK) | vervalt (run 9): regel Show HN, zie onder |

**Bewust niet:**
- Stack Overflow [44866852](https://stackoverflow.com/questions/44866852) (3.408 keer bekeken) en [64551331](https://stackoverflow.com/questions/64551331) (2.870 keer) gaan over bouwen met CMake, niet over kleuren of navigeren (GEZIEN 8 nov). De plugin daar noemen is reclame zonder antwoord op de vraag, dus spam.
- r/ProgrammingLanguages (±133.000 leden, DERDEN, [gummysearch](https://gummysearch.com/r/ProgrammingLanguages)): de moderatoren verbieden sinds dec 2025 "vibecoded/AI" projecten (DERDEN, alleen als zoekresultaat gezien, niet nagelezen). Onze plugin is met AI gebouwd. Niet posten.
- r/cpp en r/C_Programming los (strenge regels tegen zelfpromotie, GOK), en geen berichten op de mailinglijsten van GNU.
- GitHub-repo's van studenten met CLion en Bison (118 README's noemen clion, flex en bison samen, GEZIEN door de onderzoeker): daar ongevraagd iets zetten is spam.

## Eerlijk over wie het maakte
Thijs schreef de plugin niet zelf; een ploeg AI-agents bouwde hem in opdracht van Dortus. Sinds 8 nov 13:47 is de vaste vorm van Thijs voor lanceerberichten: "I made this" en "Made by Thijs at Dortus". Ik volg dezelfde oplossing als bij Rollwright (controleur run 8): "I made" mag, maar in dezelfde tekst staat dan ook eerlijk dat de code door AI-agents geschreven is. Vraagt iemand hoe het gemaakt is: eerlijk antwoorden. Verbiedt een plek AI-projecten of door AI geschreven tekst, dan posten we daar niet.

## Stand 8 nov 2026, ±14:55 UTC (run 9)
- Geüpload 13:17 UTC, Hidden aan, pluginpagina https://plugins.jetbrains.com/plugin/35901-bison--flex . API: `approve: false`, 0 downloads, `pricingModel: FREE`, `productCode: PBISONFLEX`, proef 30 dagen (GEZIEN 14:50 UTC, `/api/plugins/35901`). De prijs is dus nog niet goedgekeurd: Sales Info staat op Submitted ($19 per jaar persoonlijk, $49 organisaties, alleen jaarlijks).
- De voorwaarde "pas na een geslaagde test in CLion" voor concept B en C is vervuld: de echte CLion 2026.3 EAP laadt de plugin, 0 rode fouten, structuur met 6 knopen (IDE-run 42443828755 en 42450473711 groen, GEZIEN door Jet), en alle unittests draaien ook tegen CLion 2025.2 (117 van 117, run 42478154011, GEZIEN door de controleur). Let op: de CLion-test is een rooktest; de Pro-functies over twee bestanden zijn alleen in IDEA van begin tot eind getest. Dus nooit sterker dan "tested in CLion".
- **Pas berichten plaatsen als alle drie kloppen:** (bijwerking run 22: `approve: true` is vervangen door "versie goedgekeurd", zie het seintje in deel run 22; het veld `approve` staat ook bij live plugins op `false`) `approve: true`, Hidden uit (de pagina is zonder login te zien), en de prijs staat op de pagina (`pricingModel` niet meer `FREE`). Anders beloven we een Pro met proef die de bezoeker niet ziet.
- **Wie plaatst:** mijn toestemming om zelf te posten geldt alleen voor de drie Obsidian-plekken; andere plekken pas na een besluit van Hans in `berichten/chris.md` (regel 2 van Thijs, 8 nov 13:47). Een geplande run kan ook niet bij de browser. Daarom advies 21 aan Hans: welke plekken, en dan plaatst de hoofdchat (of Thijs) ze, zoals bij het Rollwright-forumbericht.

## Regels van de plekken (gelezen 8 nov, run 9)
| Plek | Regel (GEZIEN met curl, tenzij anders) | Gevolg |
|---|---|---|
| YouTrack IDEABKL-7544 | Geen aparte regel gevonden. Voorbeeld: de maker van Bison Language Support zette daar op 27 dec 2022 zelf een link naar zijn plugin (GEZIEN, YouTrack-API, laatste reactie). IDEABKL-4162: laatste reactie 2005. CPP-1122: Won't fix, JetBrains schreef "We leave this for third-party plugins" (2014). | A mag, één keer per melding, met eigen naam. Bij CPP-1122 alleen als reageren op een gesloten melding nog kan. |
| Stack Overflow | Zelfpromotie mag als je eigen band meldt en het antwoord het probleem oplost ([promotion](https://stackoverflow.com/help/promotion)). **Maar:** "Generative artificial intelligence ... tools may not be used to generate content for Stack Overflow", ook niet deels; zulke posts worden waarschijnlijk verwijderd, bij herhaling mogelijk een schorsing ([gen-ai-policy](https://stackoverflow.com/help/gen-ai-policy)). | **B niet door de ploeg.** Mijn concept is door een AI geschreven, dus plakken breekt de regel. Alleen als Thijs zelf, in eigen woorden, een antwoord wil schrijven; de feiten staan onder concept B als spiekbriefje, niet als tekst. |
| r/Compilers | Niet te lezen: Reddit geeft 403 en stuurt `old.reddit.com/.../about/rules/` door naar een inlogpagina (GEZIEN). Niet omzeild via spiegels. Steeds meer programmeer-subreddits weren AI-projecten: r/ProgrammingLanguages (zie boven), r/opensource sinds okt 2026 (DERDEN, [winbuzzer](https://winbuzzer.com/2026/10/27/reddits-open-source-forum-bans-ai-assisted-projects-xcxwbn/), [tomshardware](https://tomshardware.com/tech-industry/artificial-intelligence/reddits-r-opensource-bans-ai-made-and-ai-focused-projects-also-bans-non-english-speakers-sweeping-new-rules-spark-backlash-over-linux-kernel-contributions-and-solo-developers)), r/golang (DERDEN, [engineered.at](https://engineered.at/articles/r-golang-draws-a-line-on-ai-generated-projects)). | C alleen als de hoofdchat de regels en de wiki van r/Compilers in de browser leest en er niets staat tegen AI-projecten of zelfpromotie. Twijfel: niet plaatsen. |
| Hacker News, Show HN | "The project must be something you've worked on personally and which you're around to discuss" en "Don't post quickly-generated one-offs" ([showhn](https://news.ycombinator.com/showhn.html)). | **D vervalt.** Thijs schreef de code niet en kan technische vragen in de draad niet zelf beantwoorden; dat botst met "worked on personally and around to discuss". |

## Concept A: reactie op YouTrack IDEABKL-7544 (en IDEABKL-4162, CPP-1122)
> For anyone still looking: I made a plugin for this, "Bison & Flex" on the JetBrains Marketplace (https://plugins.jetbrains.com/plugin/35901-bison--flex). The code was written by AI agents working for my studio Dortus, and it's tested in CLion and IntelliJ IDEA. It handles `.y`, `.yy`, `.l` and `.ll`: highlighting (including the C code in actions), syntax errors, folding, the Structure view, and go to definition, find usages and rename within one file (renaming a token the scanner also uses is Pro), all free. A Pro tier (30-day free trial) adds jumping and renaming tokens across grammar and scanner, and warnings for undefined and unused symbols. Feedback welcome at thijs@dortus.com. Made by Thijs at Dortus.

Bij CPP-1122 dezelfde tekst. **IDEABKL-4162 vraagt iets anders** (zelf bestandssoorten maken uit grammaticabestanden), dus daar "I made a plugin for this" niet; daar begint de tekst met: "Not quite this request, but if you just want Bison and Flex support in the IDE: I made a plugin, ..." (controleur run 9). Eén reactie per melding, niet terugkomen om te herhalen.

## Concept B: Stack Overflow 49288299 (alleen als Thijs het zelf schrijft)
Niet plakken: zie de regel hierboven. Feiten die kloppen, voor als Thijs zelf een antwoord schrijft:
- CLion 2026.3 en IDEA 2026.3 herkennen `.y`, `.yy`, `.l` en `.ll` niet (GEZIEN, `platformen/jetbrains/status.md` deel 13).
- Gratis zonder plugin: Settings > Editor > File Types, eigen bestandssoort voor `*.l` met zelf ingevulde sleutelwoorden.
- De plugin: Settings > Plugins > Marketplace, "Bison & Flex"; gratis kleuren, fouten, folding, structuur; Pro is navigeren en hernoemen tussen scanner en grammatica.
- Verplicht: zeggen dat het van Dortus is ("Disclosure: made by my studio Dortus").

## Concept C: r/Compilers (alleen na lezen van de regels, zie boven)
Titel: `I made a JetBrains plugin for Bison and Flex files (free highlighting, cross-file token navigation)`
> CLion and the other JetBrains IDEs treat `.y` and `.l` files as plain text. I made a plugin for them. To be upfront: the code was written by AI agents working for my small studio Dortus. It's tested in the real CLion and IntelliJ IDEA. The free part: highlighting for both files (including the C code in actions and `$$`/`$1`), syntax errors, folding, a Structure view, and go to definition, find usages and rename within a file (renaming a token the scanner also uses is Pro).
>
> The Pro part: jump from a token in the `.l` scanner to its `%token` in the `.y` grammar, rename a token in both files at once, and warnings for undefined symbols and for unused rules, tokens and start conditions. 30-day trial, then $19 a year for personal use. The free features keep working after the trial.
>
> It doesn't explain shift/reduce conflicts yet. What would you want next?
>
> https://plugins.jetbrains.com/plugin/35901-bison--flex
>
> Made by Thijs at Dortus.

**Wie antwoordt in de draad:** de vraag aan het eind nodigt uit tot gesprek, en Thijs kan technische vragen niet zelf beantwoorden. Antwoorden schrijft de ploeg als concept in `berichten-geplaatst.md`; de hoofdchat of Thijs plaatst ze. Daarom ook nakijken of r/Compilers door AI geschreven tekst toestaat, niet alleen AI-projecten. Mag dat niet: C niet plaatsen.

De prijs alleen noemen als JetBrains de Sales Info goedkeurde en de pagina $19 toont; anders de zin "then $19 a year for personal use" weglaten.

## Concept D: Show HN
Vervalt (run 9), zie de regels hierboven.

## Volgorde
1. JetBrains keurt goed, Hidden uit, prijs zichtbaar (zie de drie voorwaarden).
2. Besluit van Hans over de plekken (advies 21).
3. Dag 0: A (drie meldingen, bij 4162 met de aangepaste aanhef), via de hoofdchat of Thijs.
4. Dag 2 tot 3: C, alleen als de regels het toestaan en A geen klachten gaf.
5. B alleen als Thijs zelf wil schrijven.

## Bijwerking 8 nov 2026, ±00:50 (run 4, Chris)
- Naam in alle concepten nu `Bison & Flex` (advies 7), niet meer `Bison/Yacc & Flex/Lex`.
- "I wrote it" en "I built" eruit: niet waar, Thijs bouwde het niet zelf. Nu "my studio Dortus made", en in C en D staat dat het met AI gebouwd is.
- Concept A noemt nu dat springen en hernoemen binnen één bestand gratis zijn (klopt met de code, zie `winkeltekst.md`).
- Controleur 8 nov: akkoord mits; moet-punt verwerkt (B en C pas na een geslaagde CLion-test, de IDE-test draait nu alleen in IntelliJ IDEA). Kan-punten verwerkt: "within one file" in A, link bij r/ProgrammingLanguages, "many compilers" in D als GOK. Alle cijfers nagemeten en goed.
- Nieuwe plekken gemeten (onderzoeker, 8 nov, steekproef nagemeten door Chris met curl): IDEABKL-4162, CPP-1122, de reviews van Bison Language Support, en de plekken die we bewust overslaan.

## Bijwerking 8 nov 2026, ±14:45 tot 15:20 UTC (run 9, Chris)
- Stand na het uploaden vastgelegd (Hidden, nog niet goedgekeurd, prijs nog FREE in de API) en drie voorwaarden voor plaatsen.
- Regels van de plekken gelezen: Stack Overflow verbiedt door AI geschreven tekst, dus B niet door de ploeg; Show HN eist dat de maker er persoonlijk aan werkte, dus D vervalt; r/Compilers niet te lezen, C blijft voorwaardelijk; YouTrack heeft een voorbeeld van een andere pluginmaker.
- Concepten A en C naar de vaste vorm van Thijs ("I made", "Made by Thijs at Dortus"), met de AI-zin erbij, de link 35901, de Pro-meldingen en $19 per jaar (maandprijs staat uit). CLion-voorwaarde vervuld.
- Controleur: akkoord mits. Moet: IDEABKL-4162 vraagt iets anders, dus daar een eerlijke aanhef: verwerkt (ook in advies 21). Kan verwerkt: "waarschijnlijk verwijderd", reden Show HN alleen "personally / around to discuss", 117 van 117 unittests met de kanttekening rooktest, "it's tested" in twee zinnen, meldingen precies als plugin.xml, wie antwoordt in de draad van C.

## Bijwerking 8 nov 2026, ±18:50 UTC (run 12, Chris)
- Concept A en C: "rename within one file" kreeg de kanttekening uit plugin.xml ("renaming a token the scanner also uses is Pro"). Gevonden door de controleur van het verspreidingsplan: `pro/ProHernoemen.kt` blokkeert hernoemen van een token dat de scanner ook gebruikt zonder licentie. Het hele plan met de nieuwe plekken staat nu in `verspreiding.md`.

## Draaiboek voor de dag van goedkeuring (run 22, Chris, 9 nov 2026 ±03:45 tot 04:40 UTC)
Waarom nu: JetBrains keurt "binnen 2 werkdagen" na de upload van 8 nov 13:17 UTC (DERDEN, mail aan Thijs, zie lijst-thijs), dus het kan vandaag of morgen zijn. Click Joints heeft zo'n draaiboek (deel run 16 in `commercie/blender-click-joints/lancering.md`), Bison & Flex nog niet. En het seintje dat we tot nu toe gebruikten, klopt niet (zie hieronder).

### Stand (GEZIEN 9 nov 03:50 UTC)
- `/api/plugins/35901`: `approve: false`, `isHidden: true`, `pricingModel: FREE`, 0 downloads, `buyUrl: null`, proef 30 dagen. `/api/plugins/35901/updates?size=3`: `[]` (nog geen goedgekeurde versie).
- YouTrack (API): IDEABKL-7544 8 stemmen, 7 reacties, Submitted, laatste wijziging 27 dec 2022; IDEABKL-4162 2 stemmen, 1 reactie, Open, laatste wijziging 2017; CPP-1122 1 stem, 3 reacties, Won't fix, laatste wijziging jan 2023. Alle drie nog stil, dus concept A blijft passen.
- Platformforum, Showcase & Feedback: 2.031 leden, 156 actief in 30 dagen (`about.json`); de nieuwste berichten 29 tot 165 keer bekeken; de categorie zegt alleen "A place for sharing your plugins and gathering feedback from the community." Er staan betaalde plugins (Swift Pro) en plugins van AI-makers tussen.

### Fout in het oude seintje: `approve` zegt niets
Overal (dit bestand, `verspreiding.md`, de status van Jet) stond "wacht op `approve: true`". Maar het veld `approve` van de plugin staat ook bij plugins die al lang live zijn op `false` (GEZIEN 9 nov 04:00 UTC): Bison Language Support (16595, 13.024 downloads), Mermaid Studio (29870, betaald, 15.593), Mermaid Studio Core (30883, 26.831), SequenceDiagram Core (8286, 1.572.173), Mermaid Companion (33340, freemium, 1.305); alleen Mermaid (20146) heeft `true`. Wie op `approve: true` wacht, mist de goedkeuring. De goedkeuring zie je aan de versies: bij Mermaid Companion geeft `/updates` versies met `approve: true, listed: true, hidden: false`. Advies 32 meldt dit aan Jet en Hans.

### Het seintje (elke run van Chris; ook de hoofdchat als Thijs een mail van JetBrains krijgt)
```
curl -s https://plugins.jetbrains.com/api/plugins/35901 | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['isHidden'],d['pricingModel'],d['downloads'])"
curl -s "https://plugins.jetbrains.com/api/plugins/35901/updates?size=3" | python3 -c "import json,sys;print([(u['version'],u.get('approve'),u.get('listed'),u.get('hidden')) for u in json.load(sys.stdin)])"
curl -s "https://plugins.jetbrains.com/plugins/list?pluginId=com.dortus.bisonflex"
```
De derde regel is wat de IDE zelf ziet: nu een lege `<plugin-repository/>` (GEZIEN 9 nov 04:20 UTC); bij Bison Language Support (`info.fluffos.idea_bison`) staat daar een volledige `<idea-plugin downloads="13024" ...>` (GEZIEN door de controleur). Staat er bij ons een `<idea-plugin`, dan is hij met één klik te installeren in de IDE: dat bevestigt stap 2.
Drie stappen, in deze volgorde:
1. **Versie goedgekeurd:** de tweede regel geeft een versie met `approve: True`. Nog niets plaatsen. Plugin staat nog op Hidden; Thijs zet hem zichtbaar met Publish Plugin (staat al op zijn lijst; niet terug te draaien, dus zijn stap). Of `/updates` een goedgekeurde versie al toont zolang de plugin verborgen is, weet ik niet (GOK); misschien zie ik stap 1 pas samen met stap 2. Het eerste teken is dan de mail van JetBrains aan Thijs.
2. **Zichtbaar:** de eerste regel begint met `False` (`isHidden` uit).
3. **Prijs zichtbaar:** `pricingModel` is `FREEMIUM` (zo staat het bij andere live gratis plugins met betaald deel, GEZIEN bij 30883, 33340 en 8286; of het veld omslaat bij de goedkeuring van de Sales Info of pas bij Publish, is GOK). Blijft het `FREE`, dan is de Sales Info nog niet goedgekeurd en ziet een bezoeker geen Pro en geen proef: dan niets plaatsen, de site laat "(planned)" staan, en ik zet het op lijst-thijs (vraag aan de partner success manager van JetBrains).
Volgens lijst-thijs zet Thijs Hidden pas uit als hij beide mails heeft (plugin goedgekeurd én Sales Info goedgekeurd), dus na stap 1 hoeft hij nog niets als de mail over de verkoop ontbreekt; "Hidden uit maar FREE" komt dan alleen voor als het veld achterloopt. Alle drie waar: dat is **dag 0**. Wordt de plugin afgekeurd of komt er een vraag van JetBrains: niets uit dit draaiboek gaat door; Jet verwerkt de reden.
De pluginpagina zelf geeft altijd 200, ook als hij verborgen is (GEZIEN), dus die zegt niets. Of de prijs echt op de pagina staat, kan ik met curl niet zien (de pagina wordt in de browser opgebouwd; een prijs-API vond ik niet, `/pricing` vraagt een parameter die ik niet kon raden): de hoofdchat kijkt het één keer na in de browser vóór het eerste bericht.

### Dag 0 (zonder Thijs, Chris in de eerstvolgende run)
1. Seintje gezien. Uit de API de versie halen (`/updates`, de bovenste met `approve: True`) en de beschrijving nalezen: gelijk aan `winkeltekst.md`.
2. **Nulmeting** in `cijfers.md`, met tijd: downloads van 35901 en ernaast Bison Language Support (16595). Daarna elke run één keer, en dag 7, 14 en 30 apart.
3. **dortus.com/bison-flex/ bijwerken** (repo dortus, map `bison-flex/`, alleen deze regels):
   - regel 72, oud: `<span class="status enter enter-3">Coming soon to JetBrains Marketplace.</span>`; nieuw: `<span class="status enter enter-3">Live on JetBrains Marketplace. Version <versie>.</span>` (zelfde vorm als dortus.com/rollwright/).
   - regel 69, de knop "What it does" (eerste knop in `<div class="btns ...">`, niet de knop in de kopbalk) wordt de knop naar de winkel: `<a class="btn btn-light" href="https://plugins.jetbrains.com/plugin/35901-bison--flex">Get it on JetBrains Marketplace <span class="arrow" aria-hidden="true">&rarr;</span></a>`; "Free and Pro" blijft `btn-line`. Zo blijven het twee knoppen, zoals bij Rollwright.
   - regel 155: "Once it is listed: open Settings, ..." wordt "Open Settings, ...", met erachter: `Or install it from <a href="https://plugins.jetbrains.com/plugin/35901-bison--flex">its page on JetBrains Marketplace</a>.`
   - regel 127 "Planned price for Pro:" wordt "Price for Pro:", en regel 171 "(planned)" weg (op dag 0 is de prijs per definitie zichtbaar, stap 3).
   - de proef: de hero en regel 124 tot 125 noemen de proef van 30 dagen al in de tegenwoordige tijd; dat klopt pas op dag 0 en blijft dan zo. Wordt dag 0 uitgesteld omdat de Sales Info blijft hangen, dan zet ik daar "planned" bij.
   Niet eerder: tot dan is de plugin verborgen en belooft een knop iets wat de bezoeker niet kan doen.
4. `commercie/jetbrains-bison-flex/berichten-geplaatst.md` aanmaken (kop en vorm zoals bij Rollwright).
5. Op `organisatie/lijst-thijs.md` één regel: "Plaatsen via de hoofdchat: YouTrack IDEABKL-7544, IDEABKL-4162 en CPP-1122, tekst in `commercie/jetbrains-bison-flex/lancering.md` concept A (bij 4162 de aangepaste aanhef). Eén reactie per melding, met het JetBrains-account van Thijs." Plus: "Kijk vóór het plaatsen één keer in de browser of de pluginpagina Pro, de proef en $19 per jaar toont."
6. Aanraden bij onbekende bestanden: `curl -s "https://plugins.jetbrains.com/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName=*.l"` en hetzelfde met `*.y`, `*.yy` en `*.ll` (plugin.xml meldt alle vier); staat `com.dortus.bisonflex` (het veld `pluginId`, niet het nummer 35901) er een week na dag 0 niet in: advies aan Jet. Nu staan bij `*.y` GoYacc Support en Bison Language Support (GEZIEN 9 nov 04:10 UTC).

### Daarna (elke stap pas als de vorige gelukt is en er geen klacht of verwijdering kwam)
| Wanneer | Plek | Tekst | Wie |
|---|---|---|---|
| dag 0 | YouTrack, drie meldingen | concept A | hoofdchat of Thijs |
| dag 1 | Platformforum, Showcase & Feedback | `verspreiding.md`, plek 4 | hoofdchat of Thijs (JetBrains-account) |
| dag 2 tot 3 | r/Compilers | concept C, alleen na lezen van regels en wiki in de browser; ook kijken of door AI geschreven tekst mag | hoofdchat of Thijs |
| ±dag 3 | awesome_jetbrains_plugins, één issue | `verspreiding.md`, plek 6 | hoofdchat of Thijs (GitHub-account) |
| na dag 14 | r/Jetbrains | schrijf ik na de meting van dag 14 | hoofdchat of Thijs |
Reddit: niet op dezelfde dag als een ander Reddit-bericht van Thijs (Rollwright r/ObsidianMD op zijn vroegst 9 nov 13:45 UTC, Click Joints r/blender op zijn vroegst twee dagen daarna). Ligt r/Compilers te dicht bij een van die twee, dan schuift r/Compilers op tot twee dagen na het vorige Reddit-bericht (GOK: moderatoren letten op accounts die vooral eigen werk plaatsen; zelfde reden als in het draaiboek van Click Joints).
Het filmpje van Daan (beelden van Jet klaar 9 nov 03:20 UTC, `producten/jetbrains-bison-flex/ontwerp.md`): is het door Daan gekeurd vóór een bericht geplaatst wordt, dan gaat het mee op het forum en bij r/Compilers; zo niet, dan de poster. Niet op YouTrack (een reactie onder een melding, geen reclame).

### Antwoorden in de draden
Technische vragen schrijf ik als concept in `berichten-geplaatst.md`, de hoofdchat of Thijs plaatst. Klachten over geld, terugbetalen, privacy of juridische vragen: niet beantwoorden, bovenaan lijst-thijs. Betalen en terugbetalen gaan via JetBrains.

### Klein verschil rechtgezet (deze run)
dortus.com/bison-flex/ noemde "$1.90 and $4.90 a month", maar de Sales Info is ingestuurd met alleen Annual (lijst-thijs, 8 nov 13:24: Monthly bewust uit, later via de manager van JetBrains). Die zin is weg (repo dortus, commit 6c9e97d). `prijs.md` en `indienen.md` noemen nog de maandprijs als voorstel; de ingestuurde stand is $19 en $49 per jaar, alleen jaarlijks. De concepten noemden de maandprijs nergens.

### Keuring (run 22)
Controleur: akkoord mits. Moet: de oude voorwaarde `approve: true` in deel run 9 van dit bestand en in de status van advies 21 sprak het seintje tegen; beide hebben nu een verwijzing naar het nieuwe seintje. Kan-punten verwerkt: derde regel in het seintje (`/plugins/list`, wat de IDE ziet), `FREEMIUM` als GOK gelabeld, volgorde van de twee mails van JetBrains genoemd, de dubbele voorwaarde in stap 3 weg, `*.yy` en `*.ll` erbij, de proef op de pagina meegenomen. Nagemeten en goed: alle cijfers van JetBrains, YouTrack en het forum, de regelnummers van de pagina, Sales Info alleen Annual, het besluit van Hans over adviezen 24 en 25. Opmerking van de controleur: de site-commit 6c9e97d ging live vóór de controle; inhoud goed (alleen een onjuiste maandprijs weg), maar voortaan eerst laten nakijken.
