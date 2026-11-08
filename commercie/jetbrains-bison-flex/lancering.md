# Bison & Flex (JetBrains): lancering

Door Chris, 7 nov 2026, bijgewerkt 8 nov 2026 (run 4, zie onderaan wat er veranderde). Concepten. Posten onder de naam van Thijs doet Thijs zelf; ik zet ze pas op `organisatie/lijst-thijs.md` als de plugin goedgekeurd en met één klik te installeren is (beoordeling door JetBrains duurt tot 2 werkdagen, DERDEN [release-plugin](https://plugins.jetbrains.com/docs/marketplace/release-plugin.html)).

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
| Stack Overflow [49288299](https://stackoverflow.com/questions/49288299/syntax-highlighting-for-lex-files-in-clion) "Syntax highlighting for Lex files in CLion" | 1.238 keer bekeken, 0 antwoorden (GEZIEN 8 nov, Stack Exchange API) | concept B |
| r/Compilers op Reddit | 25.000 tot 33.000 leden (DERDEN, [gummysearch](https://gummysearch.com/r/Compilers), [sentinel](https://reddit.sentinel-team.org/subreddits/Compilers)); regels niet zelf kunnen lezen, Reddit weigert curl vanaf hier | concept C, alleen na het lezen van de regels |
| Hacker News, "Show HN" | soms veel bereik voor gereedschap voor ontwikkelaars, vaak niets (GOK) | concept D, alleen als A tot C iets opleveren |

**Bewust niet:**
- Stack Overflow [44866852](https://stackoverflow.com/questions/44866852) (3.408 keer bekeken) en [64551331](https://stackoverflow.com/questions/64551331) (2.870 keer) gaan over bouwen met CMake, niet over kleuren of navigeren (GEZIEN 8 nov). De plugin daar noemen is reclame zonder antwoord op de vraag, dus spam.
- r/ProgrammingLanguages (±133.000 leden, DERDEN, [gummysearch](https://gummysearch.com/r/ProgrammingLanguages)): de moderatoren verbieden sinds dec 2025 "vibecoded/AI" projecten (DERDEN, alleen als zoekresultaat gezien, niet nagelezen). Onze plugin is met AI gebouwd. Niet posten.
- r/cpp en r/C_Programming los (strenge regels tegen zelfpromotie, GOK), en geen berichten op de mailinglijsten van GNU.
- GitHub-repo's van studenten met CLion en Bison (118 README's noemen clion, flex en bison samen, GEZIEN door de onderzoeker): daar ongevraagd iets zetten is spam.

## Eerlijk over wie het maakte
Thijs schreef de plugin niet zelf; een ploeg AI-agents bouwde hem in opdracht van Dortus. Daarom zeggen de concepten "my studio Dortus made" en nooit "I wrote it" of "I built it". Vraagt iemand hoe het gemaakt is: eerlijk antwoorden. Verbiedt een forum AI-projecten, dan posten we daar niet.

## Concept A: reactie op YouTrack IDEABKL-7544 (en IDEABKL-4162, CPP-1122)
> For anyone still looking: my studio Dortus made a plugin for this, "Bison & Flex" on the JetBrains Marketplace. It handles `.y`, `.yy`, `.l` and `.ll`: highlighting (including C in actions), syntax errors, folding, the Structure view, and go to definition, find usages and rename within one file, all free. Jumping and renaming tokens across grammar and scanner is in a Pro tier with a 30-day trial. Feedback welcome at thijs@dortus.com.

## Concept B: antwoord op Stack Overflow 49288299
Stack Overflow eist dat je zegt dat het je eigen werk is (DERDEN, [How not to be a spammer](https://stackoverflow.com/help/promotion)).
> CLion still doesn't recognize Lex/Flex files out of the box (checked in CLion 2026.3). There is now a plugin for it: **Bison & Flex** (Settings > Plugins > Marketplace, search "Bison & Flex"). Disclosure: it is made by my small studio, Dortus.
>
> It gives `.l`/`.ll` and `.y`/`.yy` files syntax highlighting, syntax errors, folding and a Structure view for free. Navigation and rename between the scanner and the grammar are paid, with a 30-day trial.
>
> If you only want highlighting without a plugin, you can register `*.l` as a custom file type under Settings > Editor > File Types, but that only colors keywords you list yourself.

Let op: de laatste alinea (eigen bestandssoort) is een echte gratis oplossing; die hoort erbij, zodat het antwoord ook zonder onze plugin helpt. **Pas posten na een geslaagde test in CLion** (Moet in 1.0 punt 3): de IDE-test draait nu alleen in IntelliJ IDEA Community (controleur, GEZIEN in `architectuur.md`), en deze vraag gaat over CLion. Vóór posten ook nakijken of het in 2026.3 zo heet, en of zoeken op "Bison & Flex" ons bovenaan vindt (anders "search Flex Lex").

## Concept C: r/Compilers
Eerst de regels van r/Compilers lezen (zelfpromotie, AI-projecten). Verbieden ze AI-projecten: niet posten. Pas posten na een geslaagde test in CLion; anders "tested in IntelliJ IDEA" schrijven in plaats van "tested in the real IDE".

Titel: `JetBrains plugin for Bison and Flex files (free highlighting, cross-file navigation)`
> CLion and the other JetBrains IDEs treat `.y` and `.l` files as plain text. My small studio Dortus made a plugin for them, built with AI agents and tested in the real IDE: highlighting for both files (including the C code in actions and `$$`/`$1`), syntax errors, folding, a Structure view, and go to definition and rename within a file. That part is free.
>
> The Pro part: jump from a token in the `.l` scanner to its `%token` in the `.y` grammar, and rename a token in both files at once. 30-day trial, then [prijs uit het besluit van Jet].
>
> It doesn't explain shift/reduce conflicts yet. What would you want next?
>
> [link naar de Marketplace]

## Concept D: Show HN
Titel: `Show HN: Bison and Flex support for JetBrains IDEs`
Tekst als concept C, korter, met één zin over waarom: "Bison and Flex are 30+ years old and still used in big projects, but no JetBrains IDE knows the files." (GOK; vóór posten een of twee bekende projecten met `.y`-bestanden noemen na controle, bijvoorbeeld PostgreSQL) Ook hier zeggen dat het met AI gebouwd is.

## Volgorde
1. Lancering (JetBrains keurt goed).
2. Dag 0: A (drie meldingen). B pas na een geslaagde test in CLion. Klein, gericht, wie het zoekt vindt het.
3. Dag 2 tot 3: C, met eerste reacties of fouten al gerepareerd, alleen als de regels het toestaan.
4. D alleen bij een goede ontvangst van C.

## Bijwerking 8 nov 2026, ±00:50 (run 4, Chris)
- Naam in alle concepten nu `Bison & Flex` (advies 7), niet meer `Bison/Yacc & Flex/Lex`.
- "I wrote it" en "I built" eruit: niet waar, Thijs bouwde het niet zelf. Nu "my studio Dortus made", en in C en D staat dat het met AI gebouwd is.
- Concept A noemt nu dat springen en hernoemen binnen één bestand gratis zijn (klopt met de code, zie `winkeltekst.md`).
- Controleur 8 nov: akkoord mits; moet-punt verwerkt (B en C pas na een geslaagde CLion-test, de IDE-test draait nu alleen in IntelliJ IDEA). Kan-punten verwerkt: "within one file" in A, link bij r/ProgrammingLanguages, "many compilers" in D als GOK. Alle cijfers nagemeten en goed.
- Nieuwe plekken gemeten (onderzoeker, 8 nov, steekproef nagemeten door Chris met curl): IDEABKL-4162, CPP-1122, de reviews van Bison Language Support, en de plekken die we bewust overslaan.
