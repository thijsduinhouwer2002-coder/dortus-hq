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
- **Pas berichten plaatsen als alle drie kloppen:** `approve: true`, Hidden uit (de pagina is zonder login te zien), en de prijs staat op de pagina (`pricingModel` niet meer `FREE`). Anders beloven we een Pro met proef die de bezoeker niet ziet.
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
