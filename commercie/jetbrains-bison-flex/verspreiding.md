# Bison & Flex (JetBrains): verspreidingsplan

Door Chris, 8 nov 2026 (run 12), op opdracht van Thijs (8 nov 18:33). Gemeten met een onderzoeker, steekproef zelf nagemeten met curl. Elk cijfer heeft een label: GEZIEN (zelf gemeten), DERDEN (bron met link) of GOK. De teksten voor YouTrack en r/Compilers staan al in `lancering.md` (concept A en C); hier staat het hele plan.

**Waarom wij (de zin van Jet, bovenaan `producten/jetbrains-bison-flex/ontwerp.md`):** de enige JetBrains-plugin die Bison/Yacc én Flex/Lex kent en de grammatica aan de scanner koppelt. Gratis: kleuren, fouten, folding, structuur, navigeren en hernoemen binnen één bestand. Pro ($19 per jaar persoonlijk, 30 dagen proef): springen en hernoemen tussen scanner en grammatica, meldingen voor ongedefinieerde en ongebruikte namen.

**Voor wie:** mensen die Bison of Flex schrijven in CLion of IntelliJ IDEA: compilerstudenten, docenten, onderhouders van parsers. Hoe groot: Bison Language Support (alleen `.y`) 13.024 downloads (GEZIEN 8 nov, `/api/plugins/16595`), groeit ±4 per dag (GOK, twee metingen). De markt is klein, ±200 downloads per maand (GOK, bouwbesluit Jet).

## Stand vandaag (8 nov, GEZIEN met `/api/plugins/35901`)
`approve: false`, 0 downloads, `pricingModel: FREE`, proef 30 dagen. Nog in moderatie. **Niets plaatsen voordat alle drie kloppen:** versie goedgekeurd, Hidden uit, prijs zichtbaar op de pagina. **Let op (run 22, 9 nov):** het veld `approve` van de plugin zelf is géén teken van goedkeuring; het staat ook bij live plugins op `false`. Kijk naar het seintje in `lancering.md`, deel run 22.

## Twee vaste regels voor alle plekken
1. **AI eerlijk melden.** De code is door AI-agents geschreven. Steeds meer programmeerplekken weren AI-projecten of door AI geschreven tekst (Stack Overflow, r/ProgrammingLanguages, r/opensource, Lobsters, dev.to voor promotie, zie onder). Elke tekst zegt het daarom, en een plek die het verbiedt slaan we over.
2. **Thijs kan geen diepe technische vragen beantwoorden.** Plekken waar de reacties vooral technisch zijn, kiezen we alleen als de ploeg antwoorden als concept kan klaarzetten in `berichten-geplaatst.md` en de plek dat (door AI geschreven antwoorden) toestaat.

## De plekken, in volgorde

| # | Plek | Grootte | Wanneer | Wie | Mag het al? |
|---|---|---|---|---|---|
| 1 | Zoeken en aanraden in de Marketplace en de IDE | grootste bron (GOK); bij `*.l` raadt de IDE nu niets aan (GEZIEN 7 nov) | vanzelf, na goedkeuring | ploeg (Jet, Chris) | ja, zonder Thijs |
| 2 | dortus.com/bison-flex/ | pagina staat, HTTP 200 (GEZIEN 8 nov) | nu | Chris | ja, zonder Thijs |
| 3 | YouTrack IDEABKL-7544, IDEABKL-4162, CPP-1122 | 8, 2 en 1 stemmen (GEZIEN 7 en 8 nov) | dag 0 | hoofdchat of Thijs (JetBrains-account) | ja, advies 21 overgenomen door Hans |
| 4 | JetBrains Platform forum, Showcase & Feedback | 2.031 leden, 156 actief in 30 dagen (GEZIEN, `about.json`) | dag 1 | hoofdchat of Thijs (JetBrains-account) | ja, advies 25 overgenomen door Hans (8 nov) |
| 5 | r/Compilers | 25.000 tot 33.000 leden (DERDEN, zie `lancering.md`) | dag 2 tot 3 | hoofdchat of Thijs | ja, mits de regels in de browser gelezen zijn (advies 21) |
| 6 | Lijst awesome_jetbrains_plugins, één issue | 99 sterren (DERDEN via de onderzoeker, GitHub-zoek-API; de gewone repo-API gaf mij niets terug) | ±dag 3 | hoofdchat of Thijs (GitHub-account) | ja, advies 24 en 25 overgenomen door Hans (8 nov) |
| 7 | comp.compilers (gemodereerde nieuwsgroep en mailinglijst) | "over 100,000" lezers (DERDEN, oud getal, https://compilers.iecc.com/) | na dag 7, als 3 tot 6 goed gingen | alleen Thijs, mail vanaf zijn adres | alleen als Thijs het zelf wil (Hans, 8 nov) |
| 8 | r/Jetbrains | 39k leden (DERDEN, https://gummysearch.com/r/Jetbrains/) | na de meting van dag 14 | hoofdchat of Thijs | ja, na dag 14 (Hans, 8 nov) |
| 9 | JetBrains Staff Picks | groot (GOK) | ronde van april 2027 | Thijs (YouTrack-ticket) | later, eerst gebruikers; dan **besluit Hans nodig** |

Volgens regel 2 van Thijs: naar de volgende plek alleen als de vorige gelukt is en er geen klacht of verwijdering kwam. Wordt een bericht verwijderd of komt er een waarschuwing: overal stoppen (regel 7).

### 1. Marketplace en IDE (zonder Thijs)
- Naam en beschrijving bevatten Bison, Yacc, Flex en Lex: de zoekfunctie leest ook de beschrijving (GEZIEN 7 nov, zie `winkeltekst.md`). Tags staan: Inspection, Navigation, Programming Language (GEZIEN 8 nov).
- Aanraden bij een onbekend bestand: wij melden `.y`, `.yy`, `.l`, `.ll` aan. JetBrains keurt dat apart goed (DERDEN, approval guidelines). Na goedkeuring meet ik met `/feature/getImplementations?featureType=com.intellij.fileTypeFactory&implementationName=*.l` of wij erin staan. Staan we er na een week niet in: advies aan Jet.

### 2. dortus.com/bison-flex/ (zonder Thijs)
- Titel en beschrijving noemen alle vier de woorden en de bestandssoorten (GEZIEN). Na goedkeuring: de knop naar de Marketplace controleren en de prijs alleen tonen als die op de Marketplace staat.

### 3. YouTrack (dag 0)
- Teksten: `lancering.md`, concept A; bij IDEABKL-4162 met de aanhef "Not quite this request, but ...". Eén reactie per melding, nooit terugkomen om te herhalen.
- Voorbeeld dat het mag: de maker van Bison Language Support deed hetzelfde in IDEABKL-7544 (27 dec 2022), en JetBrains schreef bij CPP-1122 "We leave this for third-party plugins" (GEZIEN, YouTrack-API, run 9).

### 4. JetBrains Platform forum, Showcase & Feedback (nieuw)
- https://platform.jetbrains.com/c/showcase-feedback/13. De categorie zegt over zichzelf: "A place for sharing your plugins and gathering feedback from the community." Richtlijn: "Don't post spam or otherwise vandalize the forum." (DERDEN via de onderzoeker, https://platform.jetbrains.com/guidelines). Berichten daar halen 29 tot 164 keer bekeken in oktober en november, oudere tot 653 (GEZIEN door de controleur). Betaalde plugins worden er gepost (Swift Pro, Oskuvi met proef, GTD Brain $19,99 per maand; GEZIEN door de controleur), en plugins met AI-functies ook. Of plugins die door AI geschreven zijn er welkom zijn: niet gezien, geen regel ertegen.
- Klein en vooral pluginmakers, dus weinig gebruikers, maar het hoort hier en het kan feedback opleveren. Inloggen gaat met het JetBrains-account van Thijs, dat hij al heeft (Marketplace).
- Tekst (zelfde beweringen als concept A):

```
Title: Bison & Flex: Bison/Yacc and Flex/Lex support for CLion and IntelliJ IDEA

I made a plugin for Bison/Yacc (.y, .yy) and Flex/Lex (.l, .ll) files. The JetBrains IDEs open them as plain text, and until now there was nothing for Flex/Lex (.l) files.

Free: highlighting (including the C code in actions and $$/$1), syntax errors, folding, the Structure view, and go to definition, find usages and rename within one file (renaming a token the scanner also uses is Pro).
Pro (30-day free trial): jump from a token in the scanner to its %token in the grammar, rename a token in both files at once, and warnings for undefined and unused symbols.

To be upfront: the code was written by AI agents that my small studio, Dortus, runs. It's tested in CLion and IntelliJ IDEA. Feedback on what's missing is very welcome.

https://plugins.jetbrains.com/plugin/35901-bison--flex

Made by Thijs at Dortus
```

### 5. r/Compilers (dag 2 tot 3)
- Tekst: `lancering.md`, concept C. Regels met curl niet te lezen (Reddit 403, GEZIEN), niet omzeild. Wie plaatst leest eerst de zijbalk, de regels en de wiki in de browser. Staat er iets tegen AI-projecten, door AI geschreven tekst of zelfpromotie: niet plaatsen, op de lijst van Thijs.

### 6. awesome_jetbrains_plugins (nieuw)
- https://github.com/clutcher/awesome_jetbrains_plugins. Er is een sectie "Additional file types support" en een sectie "C/C++" (met CMake Plus); de beheerder kiest. Ook betaalde plugins staan erin ("Paid plugin for integration with Azure DevOps. ...", GEZIEN in de README 8 nov). Geen CONTRIBUTING, geen regel over AI (onderzoeker).
- Belangrijk: de onderzoeker zag dat geen enkele pull request van buitenaf ooit is samengevoegd, maar een plugin uit issue #1 (MetricsTree) staat nu wel in de lijst. Dus **een kort issue, geen pull request**: de beheerder voegt zelf toe.
- Laatste push 14 maart 2026 (DERDEN via de onderzoeker): traag, klein bereik, maar het blijft staan.
- Tekst issue:

```
Title: Suggestion: Bison & Flex (Additional file types support)

Suggestion for "Additional file types support" (or "C/C++", whichever you prefer): Bison & Flex, https://plugins.jetbrains.com/plugin/35901-bison--flex
Support for Bison/Yacc (.y, .yy) and Flex/Lex (.l, .ll) files: highlighting, syntax errors, Structure view and navigation within a file for free; a paid Pro tier adds navigation and rename across grammar and scanner.

Disclosure: I made it (Thijs, Dortus). The code is written by AI agents my studio runs; there are no AI features in the plugin itself.

Made by Thijs at Dortus
```

- Waarom besluit Hans: zo'n issue staat onder het GitHub-account van Thijs op een plek buiten zijn lijst. Dezelfde vraag ligt al in advies 24 (lijsten); advies 25 vraagt het voor Bison & Flex, één antwoord geldt voor beide producten.

### 7. comp.compilers (nieuw, alleen Thijs)
- https://compilers.iecc.com/, gemodereerd door John Levine, in 2026 nog actief, met aankondigingen van gereedschap rond Yacc en Lex (onderzoeker zag "Announcing Ox release 1.12.2" in de RSS). Regel (GEZIEN, https://compilers.iecc.com/faq.txt): "Postings announcing commercial products are welcome so long as there is substantially more technical content than hype." Alleen platte tekst ("Plain old ASCII").
- Dit is de plek met de meeste mensen die echt parsers schrijven. Maar: een mail vanaf het adres van Thijs, en de reacties zijn technisch en gaan naar zijn mail. De koppeling Gmail mogen wij niet gebruiken, en Thijs kan technische vragen niet zelf beantwoorden. De FAQ (2016) zegt niets over AI; de lezers zijn kritisch (er liep een draad over een door AI gemaakte C-compiler, onderzoeker).
- Daarom: pas na dag 7, alleen als Thijs het zelf wil versturen, en dan een nuchtere technische tekst die ik dan schrijf (wat de plugin met `%token`, `%type`, start-condities en `$$` doet, wat hij niet doet). Geen tekst nu: eerst het besluit.

### 8. r/Jetbrains
- Groot maar algemeen; regels niet te lezen (403). Pas na de meting van dag 14 en alleen als 3 tot 5 iets opleverden.

### 9. Staff Picks
- "To apply to become featured in the Staff Picks category, please submit a YouTrack ticket" en "Popularity and community impact: The primary factor" (DERDEN via de onderzoeker, https://plugins.jetbrains.com/docs/marketplace/staff-picks.html). Ook betaalde plugins mogen. Zonder gebruikers kansloos: in maart 2027 kijken of we genoeg hebben voor de ronde van april.

### Afgevallen
- **Stack Overflow:** geen door AI geschreven tekst, ook niet deels (GEZIEN run 9). Alleen als Thijs zelf in eigen woorden schrijft; feiten in `lancering.md` concept B.
- **Show HN:** de maker moet er persoonlijk aan gewerkt hebben en erover kunnen praten (GEZIEN run 9).
- **r/ProgrammingLanguages, r/opensource:** verbieden AI-projecten (DERDEN, zie `lancering.md`).
- **Lobsters:** "New users (first 70 days) are not allowed to submit self-promo", alleen op uitnodiging, en spam is daar ook "content that is created without meaningful human authorship" (DERDEN via de onderzoeker, https://lobste.rs/about).
- **dev.to:** door AI geschreven artikelen mogen niet "Promote any business, program, or course (including your own)" (DERDEN via de onderzoeker); de tag #bison heeft 0 artikelen.
- **aalhour/awesome-compilers** (9.953 sterren): geen merges sinds 2024, geen IDE-plugins. **fffaraz/awesome-cpp:** "PRs by accounts created after 2024 or for repos created after 2024 will also result in an instant block and report" en alleen bibliotheken (DERDEN via de onderzoeker).
- **awesome-IntelliJ-IDEA, championswimmer/awesome-jetbrains:** dood (laatste push 2023 en 2017).
- **GNU-mailinglijsten, studentenrepo's, reviews onder Bison Language Support:** spam of reclame onder het werk van een ander.
- **Onderwijs:** geen open, uitnodigende plek gevonden.

## Wat zonder Thijs kan (doet de ploeg zelf)
- Zoekwoorden, tags en plaatjes in de Marketplace (Jet en Daan, tekst van mij).
- dortus.com/bison-flex/ gelijk houden aan de winkeltekst en de prijs (Chris).
- Volgen: downloads met `/api/plugins/35901`, de aanraadlijst voor `*.l` en `*.y`, reacties op de YouTrack-meldingen met de YouTrack-API, het platformforum met curl (`.json`). Reddit kan ik niet volgen; dat doet wie plaatst.
- Antwoorden als concept in `berichten-geplaatst.md`.
- Meten: dag 0, dag 7, dag 14 en dag 30 in `cijfers.md`, en elke week Bison Language Support ernaast.

## Wat ik meet om te zien of een plek werkte
Downloads de dag voor en twee dagen na elk bericht (de teller ververst één keer per dag, dus alleen sprongen tellen), plus reacties en keer bekeken op de plek. Na 2 tot 3 weken beslist Hans (koers punt 3): er vol op, of alleen onderhoud.

## Keuring
Controleur (8 nov run 12): akkoord mits. Moet-punten verwerkt: (1) "rename within one file" kreeg de kanttekening uit plugin.xml ("renaming a token the scanner also uses is Pro"), want `pro/ProHernoemen.kt` blokkeert dat zonder licentie; ook in concept A van `lancering.md`; (2) het issue eindigt nu met "Made by Thijs at Dortus". Kan-punten verwerkt: "nothing for Flex/Lex (.l) files" (JFlex Support bestaat voor `*.flex`, maar dat is JFlex voor Java); de zin over AI-plugins op het platformforum eerlijker; bereik keer bekeken met de oudere berichten; sectie C/C++ genoemd; Staff Picks ook besluit Hans; eigen advies 25. Niet na te meten door de controleur: 99 sterren, laatste push en geen samengevoegde pull requests van buitenaf (GitHub-API dicht); label blijft DERDEN via de onderzoeker.
