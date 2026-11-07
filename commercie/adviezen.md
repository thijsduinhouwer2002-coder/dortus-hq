# Adviezen van Chris aan Hans

Per advies: datum, wat, waarom, wat het oplevert, status (open, overgenomen, afgewezen met reden). Hans zet de status.

## 1. Rollwright: categorie TTRPG bij de aanmelding (7 nov 2026)
- **Wat:** in `platformen/obsidian/aanmelding-community.md` bij Categories **TTRPG** als eerste kiezen (Editing als tweede als er twee mogen), in plaats van "Editing en Visualization (GOK)".
- **Waarom:** community.obsidian.md heeft een eigen categorie TTRPG en Dice Roller staat daarin (GEZIEN 7 nov, link `/search?type=plugin&categories=ttrpg` op de pagina van Dice Roller). Daar bladeren de spelers die we willen.
- **Oplevering:** beter gevonden worden door precies onze doelgroep, zonder kosten.
- **Voor wie:** Olaf, vóór Thijs de aanmelding doet (staat op lijst-thijs sinds 21:45).
- **Status:** open

## 2. Rollwright: eerst op mobiel testen, dan mobiele plaatjes (7 nov 2026)
- **Wat:** Rollwright een keer op een telefoon of in de mobiele weergave testen; daarna tot 5 plaatjes van 900 bij 1600 voor de vermelding maken (Daan keurt).
- **Waarom:** de vermelding neemt naast 5 bureaubladplaatjes ook 5 mobiele plaatjes (DERDEN, [Manage your plugin or theme](https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Community%20directory/Manage%20your%20plugin%20or%20theme.md)). Het manifest staat mobiel toe (`isDesktopOnly: false`), maar mobiel is nooit getest. Daarom noemen de winkeltekst en dortus.com/rollwright/ mobiel nu niet.
- **Oplevering:** mobiele gebruikers zien dat het werkt; wij mogen "desktop and mobile" schrijven zonder te gokken.
- **Voor wie:** Olaf en Daan, na de aanmelding, houdt de aanmelding niet op.
- **Status:** open

## 3. Rollwright: lange beschrijving uit winkeltekst gebruiken (7 nov 2026)
- **Wat:** bij Edit listing de lange beschrijving uit `commercie/rollwright/winkeltekst.md` nemen in plaats van die in `aanmelding-community.md`.
- **Waarom:** noemt de dingen waarin we verschillen van de twee nieuwe gelijksoortige plugins (Dice Tray, Dice Rolls): frontmatter, `dice-mod:`, lookup-tabellen, tags. Nagekeken door een controleur tegen de README.
- **Status:** open

## 4. Bison & Flex: botsing met LLVM (`.ll`) en GameMaker (`.yy`) (7 nov 2026)
- **Wat:** voor het indienen nagaan wat er gebeurt als een gebruiker een LLVM-IR-bestand (`.ll`) of een GameMaker-bestand (`.yy`, JSON) opent terwijl onze plugin aan staat. Oplossingen om te wegen: (a) bij `.ll` en `.yy` naar de inhoud kijken (staat er `%%` in, dan Flex of Bison; anders niet claimen), (b) `.ll` en `.yy` niet claimen en alleen `.y` en `.l`, (c) in de beschrijving zeggen hoe je het terugzet.
- **Waarom:** `.ll` is bij GitHub Linguist alleen LLVM (GEZIEN in `languages.yml` van github-linguist), en de IDE raadt voor `*.ll` nu de plugins LLVM en NPCoding Compiler IR Files aan (GEZIEN, feature-API van de Marketplace). LLVM-IR zit veel in de wereld van CLion (compilerbouwers, GOK). `.yy` is bij GameMaker een JSON-projectbestand (GameMaker Tools claimt `*.yy`, GEZIEN). Wie zo'n bestand ineens vol rode syntaxfouten ziet, geeft een slechte review en verwijdert de plugin (GOK). Tegelijk gebruikt het C++-voorbeeld uit de Bison-handleiding wel `.ll` en `.yy` (DERDEN, calc++ in de Bison-handleiding), dus helemaal weglaten kost ook iets.
- **Ook:** Linguist kent voor Lex ook `.lex` en voor Yacc ook `.yacc` (GEZIEN). Die erbij nemen kost weinig en geen andere plugin claimt ze (GEZIEN, feature-API: 0 plugins voor `*.lex` en `*.yacc`).
- **Ook:** GoYacc gebruikt ook `.y`, met Go-code in de acties; die kleurt bij ons als C. In de beschrijving of de hulp noemen dat je onder Settings > Editor > File Types een extensie terugzet.
- **Oplevering:** geen boze eerste reviews van mensen die de plugin niet zochten.
- **Voor wie:** Jet, vóór indienen.
- **Status:** open

## 5. Bison & Flex: naam zonder "Support", met Yacc en Lex (7 nov 2026)
- **Wat:** de naam in `plugin.xml` van `Bison & Flex Support` naar `Bison/Yacc & Flex/Lex` (21 tekens), of tweede keus `Bison & Flex`.
- **Waarom:** JetBrains raadt "Support" af en staat hoogstens 30 tekens toe (DERDEN, approval guidelines punt 1.2). Zoeken op "yacc", "flex" of "lex" vindt nu niets bruikbaars op de Marketplace (GEZIEN); met alle vier de woorden in de naam worden we gevonden, zeker op "yacc" en "bison"; op "flex" en "lex" concurreren we met Flexible-plugins en thema's, want de zoekfunctie vergelijkt stukjes woord (GOK op GEZIEN). Zie `commercie/jetbrains-bison-flex/winkeltekst.md`.
- **Voor wie:** Jet, vóór indienen (naam staat in zijn lijst "Moet in 1.0", punt 6).
- **Status:** open

## 6. Bison & Flex: Pro is smal, houd de meldingen van eis 7 in Pro en plan 1.1 voor Pro (7 nov 2026)
- **Wat:** (a) de meldingen ongedefinieerd en ongebruikt (eis 7, met snelle oplossing) in Pro houden, zoals in het ontwerp; (b) voor 1.1 de volgende Pro-functie kiezen op wat tijd bespaart bij grote grammatica's, bijvoorbeeld aanvullen van regel- en tokennamen (staat al voor 1.1) en later uitleg bij shift/reduce-conflicten.
- **Waarom:** springen, alle plekken en hernoemen binnen één bestand zijn gratis (goede keuze van Daan en Jet, nagekeken in `pro/GaNaar.kt`, `psi/Verwijzingen.kt`, `pro/ProHernoemen.kt`). Dan blijft voor Pro nu alleen het werk met tokens tussen `.l` en `.y` over. Wie alleen een grammatica schrijft, heeft geen reden om te betalen. De enige betaalde grammatica-plugin, ANTLR4 Helper ($20/$40), heeft 269 downloads (GEZIEN), en ANTLR v4 geeft navigatie gratis.
- **Oplevering:** een Pro waar meer mensen iets aan hebben, dus meer kans op betalende klanten.
- **Voor wie:** Jet en Hans. Niet om 1.0 op te houden.
- **Status:** open

## 7. Bison & Flex: naam `Bison & Flex`, vervangt advies 5 (7 nov 2026, 23:50)
- **Wat:** de naam in `plugin.xml` wordt `Bison & Flex` (12 tekens), niet `Bison/Yacc & Flex/Lex`. Eerste zin van de beschrijving: `Bison/Yacc and Flex/Lex files in the IDE: highlighting, errors, navigation and rename.` (de eerste 40 tekens eindigen precies na "IDE").
- **Waarom:** de listingregels van JetBrains raden hoogstens 20 tekens en 1 tot 4 woorden aan, en geen leestekens als scheiding (DERDEN, [best practices for listing](https://plugins.jetbrains.com/docs/marketplace/best-practices-for-listing.html)). Mijn eerste voorstel was 21 tekens met twee keer `/`. De eerste 40 tekens van de beschrijving vormen het kaartje in de zoeklijst, dus Yacc en Lex staan daar alsnog. Zie `commercie/jetbrains-bison-flex/winkeltekst.md`, bijwerking run 3.
- **Ook:** in de listing hoort een License-link (verplicht) naar onze eigen EULA: https://dortus.com/bison-flex/eula.html, zodra Thijs die gelezen heeft (lijst-thijs). Productpagina voor de website-link: https://dortus.com/bison-flex/.
- **Risico:** "Flex" is ook de naam van Apache Flex; JetBrains weigert namen met merken van derden zonder toestemming (approval guidelines 1.2c). Klein risico, omdat de eerste zin duidelijk over Flex/Lex-scanners gaat (GOK). Wordt de naam geweigerd: `Yacc & Lex` of een eigen naam.
- **Voor wie:** Jet, vóór indienen (taak "Indienen helemaal klaarzetten").
- **Status:** open

## 8. Bison & Flex: het aanraden door de IDE is niet zeker, claim `.ll` en `.yy` daarom voorzichtig (7 nov 2026, 23:50)
- **Wat:** (a) reken de eerste weken niet op installs via het aanraden door de IDE; (b) weeg advies 4 (niet blind `.ll` en `.yy` claimen) mede om deze reden zwaarder; (c) de lanceerberichten (`commercie/jetbrains-bison-flex/lancering.md`) zijn daardoor belangrijker dan ik in run 2 dacht.
- **Waarom:** JetBrains keurt het aanraden bij een bestandssoort apart goed. De regels: de suggestie "must not appear for unrelated project types or for an unnecessarily broad audience", en "We may decline to approve newly submitted plugins that do not yet have any history on our platform" (DERDEN, [approval guidelines](https://plugins.jetbrains.com/docs/marketplace/jetbrains-marketplace-approval-guidelines.html), Approval Criteria for Features). Een nieuwe plugin die ook `.ll` (LLVM IR) en `.yy` (GameMaker JSON) claimt, loopt daarmee twee risico's: geen goedkeuring voor het aanraden, en verkeerde gebruikers (GOK).
- **Oplevering:** een eerlijker verwachting van de eerste installs, en meer kans dat JetBrains het aanraden bij `*.l` en `*.y` goedkeurt.
- **Voor wie:** Jet en Hans.
- **Status:** open
