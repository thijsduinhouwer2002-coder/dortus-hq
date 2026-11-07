# Bison & Flex (JetBrains): lancering

Door Chris, 7 nov 2026. Concepten. Posten onder de naam van Thijs doet Thijs zelf; ik zet ze pas op `organisatie/lijst-thijs.md` als de plugin goedgekeurd en met één klik te installeren is (beoordeling door JetBrains duurt tot 2 werkdagen, DERDEN [release-plugin](https://plugins.jetbrains.com/docs/marketplace/release-plugin.html)).

## Waar de mensen zitten (gemeten 7 nov, GEZIEN tenzij anders)
| Plek | Waarom | Wat |
|---|---|---|
| In de IDE zelf | Bij een `.l`-bestand raadt CLion nu geen enkele plugin aan; na de lancering alleen ons (zie `winkeltekst.md`) | niets doen, gebeurt vanzelf |
| YouTrack [IDEABKL-7544](https://youtrack.jetbrains.com/issue/IDEABKL-7544) "Handling Yacc and Flex (Bison) markup" | 8 stemmen, 7 reacties, open sinds 2013: mensen die precies dit missen en een melding krijgen bij een nieuwe reactie | één korte reactie (concept A) |
| Stack Overflow [49288299](https://stackoverflow.com/questions/49288299/syntax-highlighting-for-lex-files-in-clion) "Syntax highlighting for Lex files in CLion" | 1.238 keer bekeken | een antwoord met vermelding dat het onze plugin is (concept B) |
| r/Compilers op Reddit | bouwers van parsers en compilers (GOK: grootste plek voor deze groep) | concept C |
| Hacker News, "Show HN" | soms veel bereik voor gereedschap voor ontwikkelaars, vaak niets (GOK) | concept D, alleen als A tot C iets opleveren |

Niet: r/cpp en r/C_Programming los posten (strenge regels tegen zelfpromotie, GOK, eerst de regels lezen), en geen berichten op de mailinglijsten van GNU.

## Concept A: reactie op YouTrack IDEABKL-7544
> For anyone still looking: I made a plugin for this, "Bison/Yacc & Flex/Lex" on the JetBrains Marketplace. It handles `.y`, `.yy`, `.l` and `.ll`: highlighting (including C in actions), syntax errors, folding and the Structure view for free. Go to definition, find usages and rename across grammar and scanner are in a Pro tier with a 30-day trial. Feedback welcome at thijs@dortus.com.

## Concept B: antwoord op Stack Overflow 49288299
Stack Overflow eist dat je zegt dat het je eigen werk is (DERDEN, [How not to be a spammer](https://stackoverflow.com/help/promotion)).
> CLion still doesn't recognize Lex/Flex files out of the box (checked in CLion 2026.3). There is now a plugin for it: **Bison/Yacc & Flex/Lex** (Settings > Plugins > Marketplace, search "yacc"). Disclosure: I wrote it.
>
> It gives `.l`/`.ll` and `.y`/`.yy` files syntax highlighting, syntax errors, folding and a Structure view for free. Navigation and rename between the scanner and the grammar are paid, with a 30-day trial.
>
> If you only want highlighting without a plugin, you can register `*.l` as a custom file type under Settings > Editor > File Types, but that only colors keywords you list yourself.

Let op: de laatste alinea (eigen bestandssoort) is een echte gratis oplossing; die hoort erbij, zodat het antwoord ook zonder onze plugin helpt. Vóór posten nakijken of het in 2026.3 zo heet.

## Concept C: r/Compilers
Titel: `I made a JetBrains plugin for Bison and Flex files (free highlighting, cross-file navigation)`
> I write my lexers and grammars in CLion, and it treats `.y` and `.l` files as plain text. So I built a plugin: highlighting for both files (including the C code in actions and `$$`/`$1`), syntax errors, folding and a Structure view. That part is free.
>
> The part I use most: jump from a token in the `.l` scanner to its `%token` in the `.y` grammar, find all usages, and rename a token in both files at once. That's a Pro tier with a 30-day trial ($19/year personal).
>
> It doesn't do conflict explanation (shift/reduce) yet. What would you want next?
>
> [link naar de Marketplace]

Eerlijk: "I write my lexers in CLion" alleen laten staan als Thijs dat zelf zo zegt; anders "CLion treats `.y` and `.l` files as plain text." Zie de regels van r/Compilers vóór het posten.

## Concept D: Show HN
Titel: `Show HN: Bison and Flex support for JetBrains IDEs`
Tekst als concept C, korter, met één zin over waarom: "Bison and Flex are 30+ years old and still in many compilers, but no JetBrains IDE knows the files."

## Volgorde
1. Lancering (JetBrains keurt goed).
2. Dag 0: A en B (klein, gericht, wie het zoekt vindt het).
3. Dag 2 tot 3: C, met eerste reacties of fouten al gerepareerd.
4. D alleen bij een goede ontvangst van C.
