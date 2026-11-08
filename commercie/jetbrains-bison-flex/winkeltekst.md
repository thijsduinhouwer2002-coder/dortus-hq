# Bison & Flex (JetBrains): winkeltekst

Door Chris, 7 nov 2026 (eerste versie). Voor Jet (platformmanager) bij het indienen op de JetBrains Marketplace. De naam, de beschrijving in `plugin.xml` en de plaatjes zijn samen de winkelpagina. Daan keurt wat zichtbaar is, Jet beslist over de naam.

## Wat ik gemeten heb (7 nov 2026, met curl, GEZIEN)
- **De zoekfunctie van de Marketplace leest ook de beschrijving**, niet alleen de naam. Zoeken op "Prologue" vindt Bison Language Support, omdat dat woord in zijn beschrijving staat (`https://plugins.jetbrains.com/api/searchPlugins?search=Prologue`).
- **Zoeken op "yacc" vindt Bison Language Support niet** (alleen GoYacc Support 21.167 en een lambda-plugin), want "yacc" staat niet in zijn tekst. Zoeken op "flex" of "lex" geeft niets over Flex of Lex. Wie op die woorden zoekt, vindt nu niets bruikbaars. Dat is onze kans: alle vier de woorden (Bison, Yacc, Flex, Lex) moeten in naam of beschrijving.
- **De IDE raadt zelf plugins aan** bij een onbekend bestand, op grond van de bestandssoorten in `plugin.xml` (`https://plugins.jetbrains.com/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName=*.l`):
  - `*.l`: **geen enkele plugin**. Na de lancering zijn wij de enige die CLion aanraadt bij een `.l`-bestand.
  - `*.y`: GoYacc Support en Bison Language Support. Wij komen er als derde bij.
  - `*.yy`: GameMaker Tools (bij GameMaker is `.yy` een JSON-bestand, zie advies 4).
  - `*.ll`: LLVM en NPCoding Compiler IR Files (bij LLVM is `.ll` een IR-bestand, zie advies 4).
- Dit aanraden was bij BatchCraft waarschijnlijk de motor van de groei (`platformen/jetbrains/marktmeting-2026-11-06.md` deel 6). Voor ons is het waarschijnlijk de belangrijkste bron van installs (GOK).

## Naam (voorstel, Jet beslist)
Regels van JetBrains (DERDEN, [approval guidelines](https://plugins.jetbrains.com/docs/marketplace/jetbrains-marketplace-approval-guidelines.html), punt 1.2): hoogstens **30 tekens**, woorden als "Support" worden afgeraden, geen naam van een JetBrains-product (dus geen "CLion" in de naam), geen "Plugin" of "IntelliJ".

De huidige werknaam in `plugin.xml` is `Bison & Flex Support`: bevat "Support" (afgeraden) en mist "Yacc" en "Lex".

**Voorstel: `Bison/Yacc & Flex/Lex`** (21 tekens).
- Waarom: de naam weegt bij zoeken het zwaarst (GOK), en zo staan alle vier de zoekwoorden er in, ook "yacc" en "lex" waarop nu niets te vinden is. Het zegt meteen wat het is.
- Tweede keus: `Bison & Flex` (12 tekens), rustiger, maar dan moeten Yacc en Lex in de eerste zin van de beschrijving.
- Geen officiële indruk: Bison en Flex zijn namen van open-bronprogramma's (GNU Bison, Flex). De beschrijving zegt "for Bison and Flex files" en niet dat het van GNU is. Een plugin met "Bison" in de naam bestaat al (Bison Language Support), dus JetBrains staat zo'n naam toe (GEZIEN). Of dit juridisch helemaal vrij is, weet ik niet (GOK). Risico bij de beoordeling: regel 1.2c ("Must not use famous or trademarked names of third parties without their authorization"). Wijst JetBrains de naam daarom af, dan terugvallen op `Bison & Flex`, en anders op een eigen naam met Bison, Yacc, Flex en Lex alleen in de beschrijving.
- Let op: de zoekfunctie vergelijkt stukjes woord. "flex" geeft nu 20 treffers vol "Flexible ..."-plugins, "lex" vindt thema's als Solarized (nagekeken door de controleur, GEZIEN). Bovenaan staan op "flex" of "lex" is dus niet zeker; op "yacc" en "bison" waarschijnlijk wel (GOK).

## Beschrijving voor `plugin.xml` (Engels, eerste zin is de preview in de zoeklijst)
Alleen dingen die nu gebouwd en getest zijn. Regels met **[pas na eis 7]** of **[pas na CLion-test]** alleen houden als dat af is voor het indienen.

```html
<p>Bison/Yacc grammars (<code>.y</code>, <code>.yy</code>) and Flex/Lex scanners
(<code>.l</code>, <code>.ll</code>) as real languages in CLion and other JetBrains IDEs.
Made for C and C++ developers who write parsers and lexers.</p>

<p><b>Free</b></p>
<ul>
  <li>Recognizes Bison, Yacc, Flex and Lex files, with their own icons</li>
  <li>Syntax highlighting for directives, tokens, rules, start conditions and regular expressions,
      using your color scheme (light, dark and any theme)</li>
  <li>C code in actions highlighted: keywords, strings, comments and
      <code>$$</code>, <code>$1</code>, <code>@1</code></li>
  <li>Syntax errors in the grammar and the scanner</li>
  <li>Folding of rules and code blocks, a Structure view with rules and tokens</li>
  <li>Comment and uncomment with the usual shortcut</li>
  <li>Go to definition, find usages and rename within a file</li>
</ul>

<p><b>Pro</b> (30-day free trial, then a paid license)</p>
<ul>
  <li>Jump from a token in the <code>.l</code> scanner to its <code>%token</code>
      in the <code>.y</code> grammar</li>
  <li>Find usages and rename tokens across grammar and scanner at once</li>
  <li>[pas na eis 7] Warnings for undefined and unused rules and tokens, with a quick fix</li>
</ul>

<p>The free features keep working after the trial. No sign-up with us, no telemetry.</p>

<p>Another plugin for <code>.y</code> files installed? Disable it, so the IDE uses this one.</p>

<p>Questions or a bug: <a href="mailto:thijs@dortus.com">thijs@dortus.com</a></p>
```

Waarom zo:
- De eerste zin bevat de zes zoekwoorden (Bison, Yacc, Flex, Lex, CLion, parsers/lexers) en de vier bestandssoorten. Die zin is wat mensen in de zoeklijst zien.
- "CLion" mag in de beschrijving, niet in de naam (regel 1.2h).
- Gratis en Pro staan los, zodat niemand zich na de proef bedrogen voelt. Springen, alle plekken en hernoemen binnen één bestand zijn gratis (`pro/GaNaar.kt`, `psi/Verwijzingen.kt`, `pro/ProHernoemen.kt`, keuze van Jet en Daan); alleen het werk tussen `.l` en `.y` is Pro. Dat kan in de praktijk alleen bij tokens, want regels staan alleen in `.y` en start-condities alleen in `.l`. Daarom zegt de tekst "tokens".
- "No sign-up with us" in plaats van "No account": een proef of licentie loopt via een JetBrains-account (Help > Register). De zin "free features keep working" haalt de grootste angst weg bij freemium (GOK).
- Geen naam van de concurrent (regel van mijn rol); alleen een algemene zin over "another plugin".
- Niet beloofd: echte C/C++-hulp in acties (alleen kleuren), shift/reduce-uitleg, Bison draaien. Dat zit niet in 1.0 (`producten/jetbrains-bison-flex/ontwerp.md`).
- Haakjes paren staat in het ontwerp, maar ik vond geen BraceMatcher in de code (GEZIEN, `src/main`), dus niet beloofd.
- **[pas na CLion-test]:** "in CLion" alleen houden als CLion in de IDE-test zit (Moet in 1.0, punt 3). Lukt dat niet, dan "in IntelliJ IDEA and other JetBrains IDEs" en CLion pas noemen na een echte test.

## Change notes voor 1.0 (`<change-notes>`)
```html
<p>First release: Bison/Yacc and Flex/Lex file types, highlighting, syntax errors,
folding and Structure view, go to definition, find usages and rename within a file.
Pro: navigation, find usages and rename of tokens across grammar and scanner.</p>
```

## Tags op de Marketplace
`Programming Language` (zo staat Bison Language Support, GEZIEN) en `Code Tools` als die er nog bij mag (GOK).

## Zoekwoorden (waarop mensen zoeken)
GOK, op grond van de zoekproeven hierboven en de woorden in de beschrijvingen van verwante plugins:
- bison, yacc, flex, lex, lexer, scanner, grammar, parser generator, `.y`, `.l`
- CLion, C, C++, compiler
Allemaal in naam of beschrijving, behalve "parser generator" en "compiler". Die laat ik weg uit de tekst: de plugin genereert geen parser, en "parser generator" als los woord trekt ANTLR-gebruikers die hier niet zoeken.

## Plaatjes (lijst voor Jet en Daan)
De schermen bestaan al op de tak `schermen` (map `jetbrains-bison-flex/`), licht en donker. Voor de winkel adviseer ik deze volgorde, 1280 bij 800 of groter in 16:10 (GOK; JetBrains noemt die maat alleen voor kleurschema's en thema's, punt 1.6 van de approval guidelines):
1. `calc.y` open met kleuren en structuurweergave (licht). Eerste plaatje = wat je krijgt.
2. `calc.l` open met kleuren (donker). Laat zien dat Flex er ook is, daarin zijn we de enige.
3. Ga naar definitie van `.l` naar `.y` (een token in de scanner, sprong naar `%token` in de grammatica). Dit is de Pro-functie die niemand anders heeft.
4. Een token hernoemen in beide bestanden tegelijk.
5. [pas na eis 7] Melding van een ongebruikte regel met de snelle oplossing.
Geen plaatje van de koopmelding: die hoort bij het product, niet bij de etalage.
Thijs ziet de lijstplaatjes eerst (regels, lancering).

## Wat de concurrent mist en wij hebben (alleen voor intern gebruik, niet in de tekst)
- Bison Language Support (13.020 downloads, laatste versie 2 sep 2023, GEZIEN; rating 3,41 uit de zoek-API van de onderzoeker, niet nagemeten): alleen `.y`, geen Flex, geen `.yy`. Heeft sinds dec 2022 wel een structuurweergave (zijn change notes), dus dat is geen voordeel voor ons. "Ga naar definitie" staat sinds 2023 als "planned" in de beschrijving en kwam er niet.
- Voor Flex/Lex bestaat niets.
- ANTLR v4 (788.253 downloads) geeft navigatie en hernoemen gratis. Wie van ANTLR komt, verwacht dat gratis (GOK). Daarom moet het gratis deel op zichzelf al goed zijn.

## Bijwerking 7 nov 2026, ±23:45 (run 3, Chris): nieuwe regels van JetBrains gelezen
Gelezen met curl (DERDEN, [best practices for listing](https://plugins.jetbrains.com/docs/marketplace/best-practices-for-listing.html), [approval guidelines](https://plugins.jetbrains.com/docs/marketplace/jetbrains-marketplace-approval-guidelines.html), [EULA](https://plugins.jetbrains.com/docs/marketplace/eula.html)). Vier dingen veranderen het voorstel hierboven:

1. **Naam: nu `Bison & Flex` als eerste keus** (12 tekens), niet meer `Bison/Yacc & Flex/Lex`. De listingregels raden 1 tot 4 woorden aan, **hoogstens 20 tekens** (de 30 uit punt 1.2 is de harde grens), en leestekens als scheiding (de `/`) worden afgeraden. `Bison/Yacc & Flex/Lex` is 21 tekens en gebruikt twee keer `/`. Yacc en Lex gaan daarom in de eerste zin van de beschrijving; de zoekfunctie leest de beschrijving ook (GEZIEN, run 2). Advies 5 is hiermee bijgewerkt (zie `adviezen.md`, advies 7).
2. **De eerste 40 tekens van de beschrijving zijn het kaartje in de zoeklijst**, in het Engels, met een korte samenvatting. Nieuwe eerste zin:
   `Bison/Yacc and Flex/Lex files in the IDE: highlighting, errors, navigation and rename.`
   De eerste 40 tekens zijn dan precies "Bison/Yacc and Flex/Lex files in the IDE" (nageteld door de controleur). Alle vier de zoekwoorden staan erin. Geen bijvoeglijke woorden als "simple" of "powerful" (afgeraden).
   Daarna de tweede zin: `For .y, .yy, .l and .ll files. Made for C and C++ developers who write parsers and lexers.`
3. **Plaatjes: aanbevolen minimum 1200 bij 760, allemaal dezelfde verhouding**, met het gewone thema van de IDE, zonder bureaubladachtergrond of persoonlijke gegevens. Onze schermen zijn 2880 bij 1800 (16:10, GEZIEN), dus dat klopt; houd alle winkelplaatjes op 16:10.
4. **Een eigen EULA is verplicht** (punt 3.2), en het veld License op de pluginpagina is verplicht. De standaard-EULA van JetBrains mag niet ongewijzigd. Concept staat op https://dortus.com/bison-flex/eula.html (gebouwd op de standaard-EULA, plus: gratis deel blijft gratis, Nederlands recht, consumentenrecht, JetBrains geen partij). Thijs leest het eerst (lijst-thijs), daarna is die link de License-URL.

**Ook gevonden, belangrijk voor de cijfers:** het aanraden door de IDE (bij een onbekend `.l`-bestand) is een "feature" die JetBrains apart goedkeurt: "We may decline to approve newly submitted plugins that do not yet have any history on our platform" (approval guidelines, Approval Criteria for Features). Mijn verwachting uit run 2 dat het aanraden de belangrijkste bron van installs wordt, kan dus de eerste weken niet opgaan (GOK). Zie advies 8.

**Productpagina:** https://dortus.com/bison-flex/ (Engels, plaatjes calc.y licht en calc.l donker uit run 42419247737, met privacy, support en EULA). Werkt als website-link in `plugin.xml` (`<vendor url>` of een eigen link in de beschrijving). Geen prijs genoemd tot Jet besloten heeft, CLion niet beloofd tot de CLion-test.

## Bijwerking 8 nov 2026, ±00:55 (run 4, Chris): poster van Daan
- **Plaatjes:** Daan maakte een poster als eerste winkelplaatje (`ontwerp/bison-flex/winkel-1-poster.png`, 2400 bij 1520, verhouding 1200 bij 760, gemaakt van echte schermen uit IDE-run 42429131027) en een nieuw pluginicoon. Nieuwe volgorde voor de winkel: 1. poster, 2. `calc.y` met kleuren en structuur, 3. `calc.l` donker, 4. hernoemen in beide bestanden, 5. [pas na eis 7] melding met snelle oplossing. Let op: de lijst in run 1 noemde 1280 bij 800 (16:10); de poster is 1200 bij 760 (±1,58). JetBrains wil alle plaatjes in dezelfde verhouding (best practices, zie run 3). De schermen dus bijsnijden naar 1200 bij 760 (of 2400 bij 1520), of de poster naar 16:10. Daan beslist; staat als advies 9.
- **Klopt de poster met de tekst?** Ja (GEZIEN): "Free: colors, structure and syntax errors · Pro: jump and rename across files" volgt de grens uit de code. Hij noemt springen binnen één bestand niet als gratis; dat is weglaten, geen fout.
- **Kop:** de poster zegt "Your grammar and scanner, finally connected." Die zin mag als slotzin van de eerste alinea in de beschrijving, na de 40 tekens van het kaartje, zodat winkelpagina en poster hetzelfde verhaal vertellen. Niet in de eerste 40 tekens: daar moeten de zoekwoorden staan.
- **Productpagina:** https://dortus.com/bison-flex/ toont de poster nu in het deel Free and Pro (`poster.jpg`, 1600 breed, 123 kB), getest op 1280 en 390 breed zonder zijwaarts scrollen (GEZIEN, Playwright, scrollWidth gelijk aan de breedte).
- **Vraag in de winkel (GEZIEN 8 nov):** de recentste review van Bison Language Support vraagt "Do you know something similar for the lex files?" en een andere klaagt dat hij vaak crasht en de kleuren kwijtraakt. Steunt de keuze om Flex/Lex vooraan te zetten.
