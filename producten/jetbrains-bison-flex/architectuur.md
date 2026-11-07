# Architectuur: Bison & Flex (JetBrains-plugin)

Stand 7 nov 2026: versie 0.1. Bestandssoorten, echte lexer met kleuren, kleurenpagina's en commentaar. Parser nog plat.

## Onderdelen
- `src/main/kotlin/com/dortus/bisonflex/Talen.kt`: de twee talen, `BisonLanguage` en `FlexLanguage`.
- `Bestandssoorten.kt`: `BisonFileType` (`.y`, `.yy`) en `FlexFileType` (`.l`, `.ll`) met iconen uit `src/main/resources/icons/` (licht en `_dark`).
- `lexer/`: handgeschreven lexers, los van de IDE te testen. `Soort.kt` (alle tokensoorten), `Scanner.kt` (gedeelde basis plus de eenvoudige C-kleuring voor acties, proloog en epiloog), `BisonScanner.kt`, `FlexScanner.kt`, en `Tokens.kt` (koppeling naar IElementTypes per taal en de `ScannerLexer` voor de IDE). Alle context zit in de toestand (een getal), zodat de IDE midden in een bestand opnieuw kan beginnen; de test `testOpnieuwBeginnenMiddenInGeeftHetzelfde` bewaakt dat. Gekozen voor handgeschreven in plaats van JFlex: Flex hangt sterk af van de plek op de regel, dat is met de hand overzichtelijker, en er hoeft geen generator in de build.
- `Kleuren.kt`: kleursleutels per taal (`BISON_*`, `FLEX_*`), elk met een standaardkleur van de IDE als terugval (`DefaultLanguageHighlighterColors`), geen vaste kleuren. Highlighter, factory's en de kleurenpagina's (Settings, Editor, Color Scheme, "Bison/Yacc" en "Flex/Lex"). `Voorbeelden.kt` bevat de voorbeeldtekst van die pagina's.
- `Commentaar.kt`: commentaar aan en uit (Bison `//` en `/* */`, Flex alleen `/* */`).
- `Parsers.kt`: `SkeletParserDefinition` met de echte lexer, maar nog een platte boom (alle tokens onder het bestand). Wordt vervangen door een echte parser per taal.
- `src/main/resources/META-INF/plugin.xml`: registratie van soorten en parsers. Alleen `com.intellij.modules.platform`, dus werkt in elke IDE.

## Tests
- `src/test/kotlin/`: unittests (`BasePlatformTestCase`, JUnit 4). Lezen de vaste testset in `testdata/` (10 echte bestanden, bronnen in `testdata/BRONNEN.md`). `LexerTest`: geen onbekende tekens en alle blokken dicht op de 10 bestanden, opnieuw beginnen geeft hetzelfde, vaste kleur per token voor de rekenmachine (`testdata/verwacht/*.kleuren`), geen vaste kleuren, snelheid.
- `e2e/kotlin/`: test in de echte IDE (Starter + Driver, JUnit 5), Gradle-taak `integrationTest`. Opent `e2e/project/` in IDEA Community 2025.2.6.4 (vaste versie), één keer licht en één keer donker thema, en maakt schermafbeeldingen in `e2e/screenshots/`.
- `.github/workflows/jetbrains-bison-flex-e2e.yml`: draait beide op GitHub Actions bij elke wijziging (main en `claude/jetbrains-*`), en zet de schermen op de tak `schermen`, map `jetbrains-bison-flex/<tak>/`.

## Bouwen
`./gradlew test` (unittests), `./gradlew integrationTest` (echte IDE, alleen op GitHub Actions), `./gradlew buildPlugin` (zip in `build/distributions/`). Gradle 9.8.2 via de wrapper, Java 21. Zie `platformen/jetbrains/bouwsjabloon.md`.

## Open
- Eis 1 vraagt ook CLion. De IDE-test draait nu alleen IDEA Community 2025.2.6.4 (vast). CLion vraagt in Starter waarschijnlijk een licentie (GOK); volgende stap: proberen met `IdeProductProvider.CL` en een vaste versie.
- Taal-ID's zijn `BisonFlex.Bison` en `BisonFlex.Flex`, uniek naast de gratis Bison-plugin. Niet meer veranderen na de lancering.
