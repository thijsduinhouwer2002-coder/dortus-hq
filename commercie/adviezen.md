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

## 9. Bison & Flex: alle winkelplaatjes in één verhouding (8 nov 2026)
- **Wat:** de poster (`ontwerp/bison-flex/winkel-1-poster.png`, 2400 bij 1520, ±1,58) en de schermen uit de IDE-test (2880 bij 1800, 1,6) in dezelfde verhouding zetten vóór het indienen: of de schermen naar 2400 bij 1520 brengen (eerst een smalle strook van 38 pixels breed afsnijden, 2842 bij 1800 is ook 1,58, dan verkleinen; zo blijft het hele IDE-venster heel, controleur), of de poster opnieuw maken in 16:10 (bijvoorbeeld 2560 bij 1600).
- **Waarom:** JetBrains vraagt dat alle plaatjes van een plugin dezelfde verhouding hebben (DERDEN, [best practices for listing](https://plugins.jetbrains.com/docs/marketplace/best-practices-for-listing.html)). Het verschil is klein (GEZIEN, maten van de bestanden), maar in de rij plaatjes op de winkelpagina springt het beeld dan (GOK).
- **Voor wie:** Daan (keuze) en Jet (schermen in de IDE-test), vóór indienen.
- **Status:** open

## 10. Rollwright: een demo in de browser op dortus.com/rollwright/ (8 nov 2026)
- **Wat:** een kleine pagina `dortus.com/rollwright/demo/` (of een blok op de productpagina) waar je zonder Obsidian een paar worpen aanklikt: tuimelen, een crit in goud, het Roll log. Met de echte rekenkern van Rollwright en het echte `styles.css`, op een voorbeeldnotitie (de herberg van Daan, klus 6). Link ernaartoe in de README, de listing en de lanceerberichten ("Try it in your browser").
- **Waarom:** (a) Solo Oracle, een nieuwe plugin voor solo-spel (83 downloads), heeft precies zo'n demo met de echte plugincode in de browser (GEZIEN in hun README, 8 nov). (b) Het verschil van 0.3.0 is een gevoel bij een klik; een stilstaand plaatje in de listing laat dat maar half zien, en GIF's mogen niet in de listing (DERDEN, [Manage your plugin or theme](https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Community%20directory/Manage%20your%20plugin%20or%20theme.md): alleen JPEG, PNG, WebP). (c) Het kan: `src/engine/` en `src/rollers/` gebruiken geen Obsidian-code (GEZIEN, geen `import ... from "obsidian"` in die mappen); alleen de weergave moet nagebouwd worden.
- **Oplevering:** wie de link op Reddit of het forum ziet, voelt de klik zonder iets te installeren. Meer kans dat iemand daarna installeert (GOK, niet gemeten).
- **Kost:** bouwwerk voor Olaf (code is niet mijn werk), ±een halve dag (GOK). De pagina zelf zet ik in de eigen map op de site als Olaf de bundel levert.
- **Voor wie:** Olaf en Hans. Niet om 0.3.0 of de aanmelding op te houden; na klus 8 of na de aanmelding.
- **Status:** open

## 11. Rollwright: korte beschrijving in manifest.json bijwerken bij 0.3.0 (8 nov 2026)
- **Wat:** bij de release van 0.3.0 `description` in `manifest.json` vervangen door: `Roll dice right in your notes with a full formula notation. Click to roll again, see a natural 20 light up, draw from tables, lists, sections and tags, and keep your rolls in a Roll log.` (186 tekens). En in de listing de lange beschrijving en de plaatjesvolgorde uit `commercie/rollwright/winkeltekst.md`, deel "Bijwerking 8 nov 2026".
- **Waarom:** de oude tekst noemt "history", het paneel heet nu "Roll log". En de korte tekst is wat mensen in de lijst in Obsidian lezen; daar moet het enige staan wat ons onderscheidt (het moment van een natuurlijke 20). Past in de regels van Obsidian: hoogstens 250 tekens, begint met een werkwoord, eindigt met een punt (DERDEN, [Submission requirements for plugins](https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Community%20directory/Submission%20requirements%20for%20plugins.md)).
- **Let op:** eerste plaatje in de listing is de poster met een crit in beeld; een GIF kan daar niet.
- **Voor wie:** Olaf, bij de release van 0.3.0.
- **Status:** open

## 12. Bison & Flex: teksten en invulblad uit `indienen.md` gebruiken, release-date vast vóór de upload (8 nov 2026)
- **Wat:** (a) naam, beschrijving en change notes in `plugin.xml` vervangen door die uit `commercie/jetbrains-bison-flex/indienen.md` deel 1 (nu staat er nog "Early version: file types and syntax highlighting", terwijl 1.0 veel meer doet en eis 7 erin zit); (b) het invulblad Sales Info (deel 3) en de uploadvelden (deel 2) op lijst-thijs zetten of ernaar linken bij de stappen voor de upload; (c) de echte lanceerdatum in `release-date` zetten in de build die Thijs uploadt, en die daarna niet meer veranderen.
- **Waarom:** de tekst is de winkelpagina en moet kloppen met de code (nagekeken door de controleur, punt voor punt). Een `release-date` in de toekomst (nu 20261215) betekent: pas vanaf die datum te koop; een latere wijziging geldt als nieuwe hoofdversie en zet lopende proeven opnieuw (DERDEN, [add-required-parameters](https://plugins.jetbrains.com/docs/marketplace/add-required-parameters.html)).
- **Voor wie:** Jet, bij de taak "Indienen helemaal klaarzetten". Prijs blijft zijn besluit; het invulblad gebruikt het voorstel $19 / $49 per jaar.
- **Status:** open

## 13. Rollwright: de afrekenpagina van Polar verkoopt nog niet, en na het betalen ontbreekt de weg terug (8 nov 2026)
- **Wat:** (a) bij het product "Rollwright Skins" in Polar een korte beschrijving en twee plaatjes zetten (Parchment en Arcane, uit de schermen van Daan), zodat wie op Buy drukt ziet wat hij koopt; (b) bij de checkout link de Success URL zetten op `https://dortus.com/rollwright/thanks/` (online sinds 8 nov, curl gaf 200): daar staat in vier stappen hoe je de sleutel vindt en activeert; (c) bij de eerste echte aankoop nagaan of de sleutel ook in de mail van Polar staat; staat hij er niet in, dan in de plugin "purchase email" vervangen door een even korte zin die naar de aankopenpagina wijst, zonder het woord Polar (besluit Daan, `producten/obsidian-rollwright/ontwerp.md` punt 12: de lange zin met Polar liep over vier regels in een smalle kolom; test `tests/skins-settings.test.ts` r.65 controleert de tekst); (d) handmatig uitbetalen, eens per kwartaal of vanaf ±$200.
- **Waarom:** (a) nu staat er alleen een naam en $6 (GEZIEN: `description: null`, `medias: []` in de afrekenpagina, 8 nov). Wie twijfelt, haakt daar af. (b) Zonder Success URL blijft de koper op de bevestigingspagina van Polar, zonder uitleg hoe hij de skins aanzet. Een koper die niet weet waar zijn sleutel is, vraagt geld terug of schrijft een slechte review. (c) Polar zegt dat de sleutel op de pagina met aankopen staat (DERDEN, [License Keys](https://polar.sh/docs/features/benefits/license-keys)); of hij ook in de mail staat heb ik niet kunnen nagaan; de plugin zegt "purchase email", de README "from your Polar purchases". Pas na nagaan veranderen, want de korte zin is bewust gekozen. (d) Uitbetalen kost $2 per maand waarin je uitbetaalt plus 0,25% + $0,25 per uitbetaling plus 0,25% omwisselen in de EU (DERDEN, [Pricing](https://polar.sh/resources/pricing)); bij ±10 verkopen per maand is maandelijks uitbetalen ±5% van de opbrengst.
- **Kost:** (a), (b) en (d) ±10 minuten voor Thijs in het dashboard van Polar (inloggen kan alleen hij), staat op lijst-thijs. (c) alleen als de sleutel niet in de mail staat: één regel tekst en de test op r.65 voor Olaf, na akkoord van Daan.
- **Voor wie:** Thijs (a, b, d), Olaf en Daan (c, pas na de eerste aankoop; houdt de aanmelding niet op).
- **Status:** open

## 14. Rollwright: productpagina 0.3.0 samenvoegen op de dag van de release, en de teksten bij de release bijwerken (8 nov 2026)
- **Wat:** (a) de nieuwe pagina dortus.com/rollwright/ staat klaar op tak `claude/rollwright-0.3.0` in de repo `dortus` (demo als video van 210 kB, poster, roll log, skins, nieuwe tekst). Die tak gaat naar main op dezelfde dag dat release 0.3.0 op GitHub staat en Thijs ja zei tegen de plaatjes. Chris doet dat zelf in zijn eerstvolgende run daarna; doet een ander het eerder, prima, het is één merge in mijn productmap. (b) Bij de release ook bijwerken: de beschrijving in `manifest.json` (zegt nog "history", zie advies 11) en de CHANGELOG (Unreleased noemt tuimelen, goud en rood, het gegroepeerde Roll log en de voorbeeldnotitie nog niet; gezien door de controleur). (c) Kan, voor Olaf: "Roll again" in het Roll log rolt met de notitie die nu open is, niet met de notitie van de worp (`src/ui/history-view.ts` r.39 tot 44 en 150, gezien door de controleur). Met `1d20 + str` uit een andere notitie geeft dat een ander getal of een fout.
- **Waarom:** (a) de pagina zegt "Version 0.3.0 is out" en toont het nieuwe uiterlijk; vóór de release klopt dat niet, en de eerste lancering moet eerst langs Thijs (regels). (b) De README en de listing worden de winkelpagina; een changelog die het belangrijkste verschil niet noemt, verkoopt het niet. (c) Een speler die zijn log terugleest en op opnieuw drukt, verwacht dezelfde worp.
- **Kost:** (a) 1 minuut. (b) ±10 minuten voor Olaf. (c) GOK ±30 minuten met test.
- **Voor wie:** Chris (a), Olaf (b, c).
- **Kan-punt voor Daan:** de voetregel op alle drie de plaatjes zegt "Made by Thijs at Dortus". In mijn lanceerberichten staat "my studio Dortus made" omdat het met AI gebouwd is en Thijs de code niet zelf schreef (logboek 8 nov, run 4 Bison & Flex). Op een plaatje is "Made by Dortus" of "by Dortus" eerlijker en korter. Geen moet: het is de keuze van Thijs, en hij ziet de plaatjes toch.
- **Status:** open

## 15. Click Joints: prijs $15, de beweegproef is niet uniek, en de Cyber Sale van Superhive (8 nov 2026)
- **Wat:** (a) normale prijs op Superhive $15 in plaats van $12, zie `commercie/blender-click-joints/prijs.md` (met het tegenargument van de controleur en mijn antwoord); (b) de beweegproef die Daan voorstelde (eerste reactie, punt 2) niet als onderscheid verkopen of voorrang geven boven het scharnier met eindstop en het testkaartje: Cut Flex heeft al "Check Pose" en LayerMechanic ($25) een beweegproef met PASS/FAIL (GEZIEN 8 nov, superhivemarket.com/products/cut-flex en /layermechanic-print-in-place-motion). Wat niemand heeft: kleur op de snede, scharnier met eindstop, testkaartje dat per printer onthouden wordt (GEZIEN, pagina's van Cleave, Cut Flex, JointLab, CatPin, Split-3DPrint en meer); (c) in het paneel en de teksten het woord **clearance** gebruiken (zo heet het; mensen zeggen ook "tolerance"), en in de tagline "articulated" en "ball joint": op extensions.blender.org gebruikt geen enkele extensie die woorden (GEZIEN, API); (d) Superhive houdt van Black Friday (27 nov) tot Cyber Monday een sitebrede uitverkoop, meestal 25%, de drukste week van het jaar, en een eigen lanceerkorting werkt dan niet (DERDEN, links in prijs.md). Is Click Joints vóór die week klaar met groene test en Daan akkoord, doe dan mee; zo niet, geen haast.
- **Waarom:** (a) $15 ligt nog 35% onder de goedkoopste tool met beweegbare gewrichten (Cleave $23) en levert per verkoop 27% meer op; (b) bouwtijd gaat naar wat ons echt onderscheidt; (c) vindbaarheid zonder iets te bouwen; (d) één keer per jaar, en het past in de planning als het product toch al zo ver is.
- **Naam:** "Click Joints" is vrij op extensions.blender.org, Superhive en GitHub (GEZIEN). Reserve: Socketeer.
- **Voor wie:** Bram (a, c, d), Bram en Daan (b). De prijs blijft het besluit van Bram.
- **Status:** open

## 16. Rollwright: na "skins nee" de skins niet aanprijzen, lanceren in twee momenten (8 nov 2026)
- **Wat:** (a) listing met twee plaatjes (poster, logboek met verschillende tijden), zonder skins-plaatje, en in de lange beschrijving `All rolling is free. Optional extra skins are a one-time purchase. No account, no telemetry.` (zie `commercie/rollwright/winkeltekst.md`, run 6); (b) in de README de zin bovenaan net zo rustig: `All rolling is free. Optional skins are a one-time purchase (see Paid skins).`, het bedrag alleen in het deel Paid skins; (c) koopknop in de plugin laten staan, prijs $6 houden, en dezelfde benefit in Polar houden zodat een sleutel ook de nieuwe skins opent; (d) lanceerberichten in twee momenten: forum en r/ObsidianMD direct na de aanmelding, r/Solo_Roleplaying en Discord pas met de nieuwe skins (zie `lancering.md`, run 6); (e) bij de nieuwe skins de meetlat uit `prijs.md` (run 6): op één blik anders, ook in een klein plaatje, en een eigen gevoel bij de worp, niet alleen andere kleuren.
- **Waarom:** Thijs vindt de huidige skins hun $6 niet waard (8 nov 08:40). Reclame maken voor iets wat de eigenaar zelf niet zou kopen, is niet eerlijk verkopen en kost later reviews. Maar het betaalde deel moet wel gemeld worden: Obsidian staat betalen alleen toe als het duidelijk in de README staat (DERDEN, [Developer policies](https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Community%20directory/Developer%20policies.md), deel Disclosures). De lanceerpiek is één keer; die bewaren we deels voor het moment dat er iets is om te kopen.
- **Gedaan door Chris:** productpagina dortus.com/rollwright/ zonder skins-plaatje, kop "Optional skins", op main in de repo `dortus` (advies 14 punt a is daarmee af). De tak `claude/rollwright-0.3.0` is vervallen: die heeft skins.jpg nog, dus niet meer samenvoegen.
- **Voor wie:** Olaf (a, b, c bij de aanmelding en de README), Daan (e), Thijs (a: de listing vult hij in, d: hij post). Prijs en koopknop blijven het besluit van Olaf.
- **Status:** open
