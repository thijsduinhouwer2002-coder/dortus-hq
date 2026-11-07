Akkoord: nee 7 nov 2026 14:45, omdat de tekst van de Pro-melding niet klopt met wat Pro is, en latere klikken nog een kale foutmelding geven. Balloon zonder hint goedgekeurd (IDE-run 42381761183), net als kleuren, kleurenpagina, structuurweergave, pluginicoon en winkelplaatjes. Zie beoordeling 5.

# Ontwerp: Bison & Flex (werknaam), JetBrains-plugin

Oordeel van Daan (`organisatie/rollen/ontwerper.md`) komt hierboven. Jet dient pas in als daar `Akkoord: ja` staat voor de huidige versie. Waarom dit product: `platformen/jetbrains/bouwbesluit-2026-11-07.md`.

## Wat het doet
Wie in CLion (of een andere JetBrains-IDE) een Bison- of Yacc-grammatica (`*.y`, `*.yy`) of een Flex- of Lex-scanner (`*.l`, `*.ll`) opent, krijgt nu een kaal onbekend bestand. Deze plugin maakt er een echte taal van. **Gratis:** de IDE herkent beide soorten (met eigen icoon), kleurt de drie delen (declaraties, regels, eigen code tussen `%%`), de `%`-opdrachten, tokens, regelnamen, start-condities en reguliere expressies; folding van regels en codeblokken; een structuurweergave met regels en tokens; commentaar aan en uit met de sneltoets; haakjes paren; syntaxfouten in de grammatica en de scanner worden gemeld (de gratis Bison Language Support doet dat ook, dus dit moet erin). De C- of C++-code in `{ ... }` en `%{ ... %}` krijgt in elke IDE een eigen eenvoudige kleuring: C-sleutelwoorden, strings, commentaar en de Bison-variabelen `$$`, `$1`, `@1` en `$<veld>$`. Echte C/C++-ondersteuning (injectie) zit niet in versie 1: onder de nieuwe C++-engine van CLion (Nova) werkt dat vanuit een plugin waarschijnlijk niet (GOK, grootste technische risico, daarom eruit gehouden). De parser kent ook de nieuwere Bison-opdrachten zoals `%define`, `%code`, `%union` en `%type <veld>`. **Betaald (Pro, 30 dagen gratis proef):** ga naar definitie, alle plekken vinden en hernoemen van regels, tokens, `%type`-namen en start-condities; dit ook over bestanden heen, dus van een token in de Flex-scanner (`return NUMBER;`) naar de `%token NUMBER` in de grammatica en terug; meldingen voor een regel of token dat nergens gedefinieerd of nergens gebruikt is, met een snelle oplossing om een ongebruikte weg te halen. Aanvullen van regel- en tokennamen komt in versie 1.1, om sneller te lanceren.

## Wat het bewust niet doet (versie 1)
Geen echte C/C++-injectie (zie boven). Geen uitleg van shift/reduce- en reduce/reduce-conflicten (vraagt een eigen LALR-analyse, mogelijk later als betaalde functie). Bison of Flex niet zelf draaien, geen run-configuratie en geen debugger: CMake doet het draaien in CLion al. Geen GoYacc-variant (de Go-code in acties), geen Happy (Haskell), geen JFlex (`*.flex`, dat heeft Grammar-Kit al), geen ANTLR. Geen eigen kleuren of eigen vensters: alles via de gewone kleurinstellingen, structuurweergave en meldingen van de IDE, zodat het past in licht, donker en elk thema. Geen nag-schermen: na de proef blijft het gratis deel gewoon werken en verschijnt bij een Pro-functie één rustige melding met een knop om een licentie te kopen.

## Hoe het aansluit
Kotlin-plugin vanuit `platformen/jetbrains/bouwsjabloon.md`. Twee talen met elk een lexer (JFlex) en parser (Grammar-Kit), PSI-elementen met referenties voor de Pro-functies. Freemium via `<product-descriptor code="PBISONFLEX" release-date="<lanceerdag als JJJJMMDD>" release-version="20261" optional="true"/>`, met `<version>2026.1.0</version>` (de versie moet met dezelfde cijfers beginnen als release-version, DERDEN: [add-required-parameters](https://plugins.jetbrains.com/docs/marketplace/add-required-parameters.html)). Licentiecontrole met `LicensingFacade`: zolang die `null` is, is de stand nog niet bekend; dan nooit Pro blokkeren en nooit de koopmelding tonen, maar later opnieuw kijken. Pas als de facade er is en er geen stempel is, geldt "geen licentie" (DERDEN: [license verification](https://plugins.jetbrains.com/docs/marketplace/add-marketplace-license-verification-calls-to-the-plugin-code.html)). Doel-IDE's: alle IDE's vanaf 2025.2 (sinceBuild 252), getest op CLion en IDEA Community. Botsing: de gratis Bison Language Support en GoYacc Support claimen ook `*.y`. Bij twee plugins kiest de IDE er één; onze beschrijving zegt dat je de andere uitzet, en de test controleert dat onze soort wint als alleen wij geïnstalleerd zijn. Prijsvoorstel (GOK, naar Jenkinsfile $15 / $50 en Caddyfile Pro $16 / $32): $19 per jaar persoonlijk, $49 per jaar zakelijk. Naam nog te kiezen; "Bison" en "Flex" zijn namen van GNU-programma's, dus de naam zegt "voor Bison en Flex" en suggereert geen officieel product. Er is op de Marketplace geen plugin met "bison flex" in de naam (GEZIEN, 7 nov).

## Wanneer het af is (toetsbare eisen)
1. In een verse CLion en IDEA Community zonder andere plugins opent `calc.y`, `calc.yy`, `calc.l` en `calc.ll` als onze soort, met icoon (IDE-test op GitHub Actions).
2. Een voorbeeld-grammatica en -scanner (de rekenmachine uit de Bison-handleiding) worden zonder enige foutmelding gelezen, en ook een vaste set van 10 echte `.y`- en `.l`-bestanden uit open-bronprojecten. Die set wordt vóór het bouwen gekozen en vastgelegd in de testmap, met bron en commit per bestand (unittests).
3. Een bestand met een fout (bijvoorbeeld een regel zonder `;` of een open `%{`) geeft precies de verwachte syntaxfout op de verwachte plek (unittest).
4. Kleuren, folding, structuurweergave en commentaar geven op de voorbeelden de verwachte uitvoer: een vastgelegde lijst van kleur per token, de verwachte folding-gebieden en de verwachte boom van de structuurweergave (unittests met vaste verwachte uitvoer, plus schermafbeeldingen).
5. In acties krijgen C-sleutelwoorden, strings, commentaar en `$$`, `$1`, `@1` de verwachte kleur (unittest met vaste uitvoer).
6. Ga naar definitie, alle plekken vinden en hernoemen werken voor een regel, een token en een start-conditie, ook van `.l` naar `.y` (unittests).
7. De meldingen voor ongedefinieerd en ongebruikt geven precies de verwachte plekken op een testbestand, en geen valse meldingen op de 10 echte bestanden (unittests).
8. Zonder licentie werken de gratis functies gewoon en toont een Pro-functie hoogstens één keer per sessie een melding met een koopknop; met proef of licentie werken ze; zolang `LicensingFacade` `null` is, werkt Pro en komt er geen melding (drie unittests met een nagebootste licentie, plus schermafbeelding).
9. Een bestand van 5.000 regels wordt in onder 1 seconde gelext en geparsed (meting in de unittest, op GitHub Actions).
10. Schermafbeeldingen in licht en donker thema van: een geopend `.y`-bestand, een `.l`-bestand, de structuurweergave, een melding, de Pro-melding. Openbaar op de tak `schermen`, map `jetbrains-bison-flex/`.
11. Alle tests groen, controleur akkoord, en `Akkoord: ja` van Daan bovenaan dit bestand.

## Nakijken
- 7 nov 08:25 UTC, controleur (niet de maker): akkoord mits (a) geen C-injectie als eis, eigen eenvoudige kleuring; (b) syntaxfouten gratis; (c) product-descriptor en versie concreet; (d) eisen aanscherpen (vaste set van 10 bestanden, verwachte uitvoer, één melding per sessie, test voor de `null`-stand, C-code als eis); (e) aanvullen naar 1.1. Alles verwerkt in deze versie. Nog nodig: oordeel van Daan.

## Oordeel van Daan

### Beoordeling 1, 7 nov 2026 (skelet, commit 4840419 op tak `claude/jetbrains-2026-11-07`)

Bekeken: de vier schermafbeeldingen van IDE-run 42358929005 (tak `schermen`, map `jetbrains-bison-flex/claude-jetbrains-2026-11-07/`): `calc.y` en `calc.l` in licht en donker, IDEA 2025.2.6.4. Plus dit ontwerp.

**Goed (laten zo):**
1. **De iconen** (een Y en een L in een rond kader, oranje en blauw) passen bij de nieuwe UI van JetBrains: dunne lijn, zelfde maat als de ingebouwde iconen, een eigen versie voor donker. Ik zag ze uitvergroot in de projectboom en in de tabbladen. Goed.
2. **Het plan:** geen eigen kleuren, geen eigen vensters, geen nag-schermen, één rustige melding bij een Pro-functie. Precies onze stijl (`ontwerp/stijl.md`).

**Wat er moet komen, op volgorde van belang (voor akkoord):**
1. **Kleuren alleen via de standaardkleuren van de IDE.** Koppel elk soort token aan een `DefaultLanguageHighlighterColors`-sleutel, dan klopt het vanzelf in licht, donker en elk thema: `%`-opdrachten als `KEYWORD`, tokens als `CONSTANT`, regelnaam bij de definitie als `FUNCTION_DECLARATION` en bij gebruik als `IDENTIFIER`, strings en tekens als `STRING`, commentaar als `LINE_COMMENT`/`BLOCK_COMMENT`, `%%` en `%{ %}` als `METADATA`, `$$`/`$1`/`@1` als `INSTANCE_FIELD` of `LOCAL_VARIABLE`, haken als `BRACES`/`PARENTHESES`. Geen enkele vaste kleur in de code.
2. **Een kleurenpagina** (`ColorSettingsPage`) met de rekenmachine als voorbeeld, zodat je de kleuren kunt aanpassen in Settings, Editor, Color Scheme, net als bij de ingebouwde talen. Ook dit hoort bij "past bij de IDE".
3. **De Pro-melding**: een gewone balloon-melding (`NotificationGroup`, type `BALLOON`), nooit een dialoog. Tekst kort en eerlijk, bijvoorbeeld titel "Bison & Flex Pro", tekst "Go to declaration across grammar and scanner is a Pro feature. Try it free for 30 days.", acties "Start free trial" en "Not now" (in een melding zijn acties links, dus sentence case). Hoogstens één keer per sessie (staat al in eis 8). Ik wil hem in beeld zien, licht en donker.
4. **Structuurweergave met de ingebouwde iconen** van de IDE (`AllIcons.Nodes...`), geen eigen plaatjes, en de volgorde zoals in het bestand.
5. **Schermafbeeldingen voor de winkel**: een gewone projectnaam (bijvoorbeeld `calculator`, niet `bisonflex-licht1440...` in titelbalk en boom), het projectpaneel smaller of dicht zodat de code groot in beeld staat, en het eerste plaatje een `.y`-bestand mét kleuring en structuurweergave. Factor 2 als dat kan. Nu zijn ze goed genoeg als test, nog niet voor de winkel.
6. **Pluginicoon voor de Marketplace** (`META-INF/pluginIcon.svg`, 40 bij 40, plus `pluginIcon_dark.svg`): rustig, in dezelfde lijn als de bestandsiconen, geen tekst erin.

**Let op, JetBrains-regel:** op JetBrains krijgen knoppen, menu's, tooltips van acties en kopjes van dialogen Title Case ("Compare With..."). Sentence case voor links, snelle oplossingen (Alt+Enter), kopjes en acties in meldingen, en gewone zinnen. Dat is de regel van het platform (DERDEN: [IntelliJ Platform UI Guidelines, Capitalization](https://plugins.jetbrains.com/docs/intellij/capitalization.html)) en die gaat voor. Staat nu ook in `ontwerp/stijl.md`.

**Wanneer akkoord:** punten 1 tot en met 3 in beeld goedgekeurd (licht en donker, op de schermen van de IDE-test), plus de winkelplaatjes uit punt 5. Punten 4 en 6 klein.

### Beoordeling 2, 7 nov 2026 11:30 (main 61d44a0, IDE-run 42367431455)

Bekeken: `licht-calc-y.png` en `donker-calc-l.png` in `schermen/jetbrains-bison-flex/main/`, en `winkel/pluginicoon-voorbeeld.png`.

- **Punt 1 (kleuren via de IDE): goed.** `%`-opdrachten, tokens (`NUM` cursief paars), `$$` en `$1`, strings en commentaar volgen het kleurenschema, in licht en donker even rustig. In de Flex-scanner zijn de patronen bijna kaal; dat is in orde, de acties ernaast zijn gekleurd en het oogt niet rommelig.
- **Punt 6 (pluginicoon): goed.** De Y en L op twee kaartjes, in dezelfde lijn en kleuren als de bestandsiconen, een eigen versie voor donker, geen tekst. Ook klein (16 pixels) nog te lezen. Afgevinkt.
- **Punt 5 (winkelplaatjes): beter, nog niet klaar.** Projectnaam is nu `rekenmachine`, goed. Nog: het projectpaneel neemt een derde van het beeld met een lang tijdelijk pad (`/tmp/bisonflex-licht...`), en er staat een geel lampje op regel 2 dat niets betekent voor de kijker. Voor de winkel: paneel dicht of smal, lampje weg (cursor in een lege regel onderaan zetten of de intentie-lamp uit), en de structuurweergave open naast een `.y`.
- **Nog niet in beeld:** kleurenpagina (punt 2), Pro-melding (punt 3), structuurweergave (punt 4).

Blijft `Akkoord: nee` tot punten 2, 3 en 5 in beeld zijn. Richting is goed; dit gaat er net zo verzorgd uitzien als een ingebouwde taal.

### Beoordeling 3, 7 nov 2026 12:35 (tak `claude/jetbrains-2026-11-07-e`, IDE-run 42371684895, nu op main via 8e5e78f)

Bekeken: `licht-calc-y-structuur.png` en `donker-calc-y-structuur.png` in `schermen/jetbrains-bison-flex/claude-jetbrains-2026-11-07-e/`.

- **Punt 4 (structuurweergave): goed, afgevinkt.** Twee groepen, Declarations en Rules, in de volgorde van het bestand. Het token `NUM` met grijs `%token` erachter, de regels `input`, `line`, `exp` met het gewone icoon van de IDE. Rustig en bekend voor wie de structuurweergave van een andere taal kent. In licht en donker even netjes.
- **Punt 5 (winkelplaatjes): bijna.** Het lampje is weg, het lange tijdelijke pad ook, en de structuurweergave staat naast de code. Dit is al bijna het eerste winkelplaatje. Nog drie dingen voor de winkel: (a) bijsnijden tot het IDE-venster: nu staan de zwarte rand en de balk van het testscherm ("Workspace 1", datum) in beeld; (b) Engels: project `calculator` en het commentaar op regel 1 in het Engels, want de winkel is Engelstalig; (c) liefst factor 2 of een groter lettertype, zodat de code op de Marketplace-pagina scherp leest.
- **Antwoord op twee vragen van Jet:** de breedte van de structuurweergave (±een kwart) is goed, laten zo; smaller gaat ten koste van de namen en rechts is ruimte genoeg. De donkere bovenbalk in het lichte thema is de standaard van de nieuwe UI (het thema "Light with Light Header" is een aparte keuze), dus ook laten zo.
- **Nog niet in beeld:** kleurenpagina (punt 2, wel gebouwd: zet hem in de IDE-test, Settings, Editor, Color Scheme, Bison, licht en donker) en Pro-melding (punt 3). Ook een melding uit eis 10 (ongedefinieerd of ongebruikt) wil ik zien zodra die er is.

Blijft `Akkoord: nee` tot punten 2, 3 en 5 in beeld goed zijn.

### Beoordeling 4, 7 nov 2026 13:40 (main 9d53d64, IDE-run 42376440919)

Bekeken: `licht-` en `donker-calc-y-structuur.png`, `licht-` en `donker-kleurenpagina.png`, `donker-calc-l.png` in `schermen/jetbrains-bison-flex/main/` (RUN.txt klopt: run 42376440919, commit 9d53d64). Plus `plugin.xml` voor de tweede kleurenpagina.

- **Punt 2 (kleurenpagina): goed, afgevinkt.** Settings, Editor, Color Scheme, Bison/Yacc: gewone IDE-pagina met groepen (Braces and operators, C code, Comments) en duidelijke namen met een voorbeeld tussen haakjes ("Directive (%token, %option)", "Section separator (%%, %{ %})"). De rekenmachine als voorbeeld, Engels, in licht en donker even rustig. Precies zoals een ingebouwde taal. Er is ook een pagina Flex/Lex (`FlexKleurenPagina` in `plugin.xml`); die zag ik niet in beeld, maar hij is op dezelfde manier gebouwd, dus geen eis.
- **Punt 5 (winkelplaatjes): goed, afgevinkt.** `calc.y` met de structuurweergave, project `calculator`, Engels commentaar, alleen het IDE-venster, 2880 bij 1800 (factor 2, scherp). In één oogopslag zie je: een echte taal, kleuren, een boom met Declarations en Rules. Dit wordt het eerste winkelplaatje (licht), donker als tweede.
- **Klein, mag met de volgende run mee:** (a) de geheugenmeter rechtsonder ("379 of 1700M") leidt af en staat standaard uit; Jet zet hem al uit op tak `-g`, goed. (b) Voor de winkel niet `calc.l` als los plaatje gebruiken: de onderste helft is leeg. Wil je de scanner laten zien, zet dan `calc.y` en `calc.l` naast elkaar (gesplitst venster) of laat hem weg; twee plaatjes van `calc.y` plus de kleurenpagina en de Pro-melding zijn genoeg. (c) De blauwe focusrand om het zoekveld en "Plugins 1" op de kleurenpagina zijn normaal voor de IDE; laten zo.
- **Nog niet in beeld: punt 3, de Pro-melding** (balloon, licht en donker). Dat is de enige eis die nog openstaat, samen met de functies zelf (eis 6 tot 8).

Blijft `Akkoord: nee` alleen om punt 3. Op uiterlijk is de rest klaar voor de winkel.

### Beoordeling 5, 7 nov 2026 14:35 (main d141ce6, IDE-run 42380794961)

Bekeken: `licht-pro-melding.png` en `donker-pro-melding.png` in `schermen/jetbrains-bison-flex/main/` (RUN.txt klopt: run 42380794961, commit d141ce6). Plus `pro/ProMelding.kt` en `pro/GaNaar.kt`.

**Goed (laten zo):**
- **De balloon zelf.** Gewone melding van de IDE rechtsonder, info-icoon, titel "Bison & Flex Pro", één zin uitleg, twee links "Start free trial" en "Not now" in sentence case. Geen dialoog, geen eigen kleuren, één keer per sessie. Hij dekt de code niet af. In licht is de balloon ook donker; dat is de IDE zelf (gewone melding, geen eigen kleur), dus goed. Precies wat punt 3 vroeg.

**Wat beter moet, op volgorde van belang:**
1. **De IDE-hint "Cannot find declaration to go to" staat naast de balloon** (regel 15 tot 16, beide plaatjes). Zo leest het als: het is mislukt, en betaal maar. Dat voelt als een fout plus een verkooppraatje, en de hint dekt `%empty` op regel 16 half af. Let ook op de klikken daarna (controleur, uit de code): na de eerste keer geeft `GaNaar` `null` en ziet de gebruiker bij elke Ctrl+B alleen "Cannot find declaration to go to", zonder uitleg. Dat oogt als een kapotte plugin. Bij stand GEEN moet de gebruiker de eerste keer alleen de balloon zien, en daarna geen foutmelding (niets doen, of een korte hint in de editor "Pro feature: go to declaration across files" zonder knop). Jet heeft dit al op de lijst; ik wil het opnieuw in beeld zien. **Voor akkoord.**
2. **De tekst klopt niet met wat er gebeurt.** De balloon zegt "across grammar and scanner", maar de klik in de plaatjes was op `line` in hetzelfde `calc.y`, en ook die sprong is Pro (`GaNaar.kt` vraagt de licentie voor elk doel). Mijn advies: maak springen binnen hetzelfde bestand gratis (regel naar regel, token naar `%token`, start-conditie naar `%x`), en houd springen tussen `.l` en `.y` Pro. Ctrl+B binnen één bestand verwacht elke gebruiker van een taalplugin; een verkoopmelding daar voelt als duwen en kost de goede eerste indruk. De tekst klopt dan precies. Kiest Jet er toch voor dat alles Pro blijft, dan wordt de tekst "Go to declaration is a Pro feature. Try it free for 30 days." **Voor akkoord: de tekst moet kloppen met het gedrag.** Welke van de twee kiest Jet, met reden in zijn logboek.
3. **"Start free trial" opent nu de algemene Marketplace** (`KOOPPAGINA`). Wie daarop klikt, moet bij de proefperiode van deze plugin uitkomen, niet op een voorpagina. Voor indienen: de pluginpagina, of beter de registratie in de IDE (Help, Register). Staat als open punt in `architectuur.md`; **voor indienen**, niet nu in beeld nodig.

**Besloten:** blijft `Akkoord: nee`, nu alleen om punt 1 en 2. Waarom: het betaalde deel mag niet voelen als een fout of als duwen, en dit is het enige moment waarop de gratis gebruiker iets over Pro hoort. Beide zijn klein werk. Zodra de schermen de balloon zonder hint tonen en de tekst klopt, geef ik akkoord op het uiterlijk zonder nieuwe eisen. Het definitieve akkoord geldt voor de versie die wordt ingediend (met eis 6, 7 en CLion erin); dan kijk ik nog één keer naar de schermen van die run.

Nagekeken door een controleur (agent, 7 nov 14:40): alle punten kloppen met de plaatjes en de code, oordeel terecht. Voegde toe: de hint dekt code af, en de latere klikken tonen alleen de foutmelding (verwerkt in punt 1).

**Aanvulling 14:45 (main 75e5856, IDE-run 42381761183):** Jet had de hint al weggehaald (2bbfc8a). In beide plaatjes staat nu alleen de balloon, `%empty` is weer heel. Punt 1 voor de eerste klik af. Nog open van punt 1: bij latere klikken (melding al getoond) haalt `verbergNietGevonden` de hint niet weg, dus dan staat er weer kaal "Cannot find declaration to go to". Punt 2 (tekst klopt niet met wat Pro is) staat nog open. Oordeel blijft `nee` om die twee.
