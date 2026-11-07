# Architectuur: Bison & Flex (JetBrains-plugin)

Stand 7 nov 2026: skelet (versie 0). Alleen bestandssoorten, nog geen echte lexer of parser.

## Onderdelen
- `src/main/kotlin/com/dortus/bisonflex/Talen.kt`: de twee talen, `BisonLanguage` en `FlexLanguage`.
- `Bestandssoorten.kt`: `BisonFileType` (`.y`, `.yy`) en `FlexFileType` (`.l`, `.ll`) met iconen uit `src/main/resources/icons/` (licht en `_dark`).
- `Parsers.kt`: tijdelijke `HeleTekstLexer` (hele tekst is één token) en `SkeletParserDefinition`, zodat er een geldige PSI-boom is. Wordt vervangen door een JFlex-lexer en Grammar-Kit-parser per taal.
- `src/main/resources/META-INF/plugin.xml`: registratie van soorten en parsers. Alleen `com.intellij.modules.platform`, dus werkt in elke IDE.

## Tests
- `src/test/kotlin/`: unittests (`BasePlatformTestCase`, JUnit 4). Lezen de vaste testset in `testdata/` (10 echte bestanden, bronnen in `testdata/BRONNEN.md`).
- `e2e/kotlin/`: test in de echte IDE (Starter + Driver, JUnit 5), Gradle-taak `integrationTest`. Opent `e2e/project/` in IDEA Community 2025.2.6.4 (vaste versie), één keer licht en één keer donker thema, en maakt schermafbeeldingen in `e2e/screenshots/`.
- `.github/workflows/jetbrains-bison-flex-e2e.yml`: draait beide op GitHub Actions bij elke wijziging (main en `claude/jetbrains-*`), en zet de schermen op de tak `schermen`, map `jetbrains-bison-flex/<tak>/`.

## Bouwen
`./gradlew test` (unittests), `./gradlew integrationTest` (echte IDE, alleen op GitHub Actions), `./gradlew buildPlugin` (zip in `build/distributions/`). Gradle 9.8.2 via de wrapper, Java 21. Zie `platformen/jetbrains/bouwsjabloon.md`.

## Open
- Eis 1 vraagt ook CLion. De IDE-test draait nu alleen IDEA Community 2025.2.6.4 (vast). CLion vraagt in Starter waarschijnlijk een licentie (GOK); volgende stap: proberen met `IdeProductProvider.CL` en een vaste versie.
- Taal-ID's zijn `BisonFlex.Bison` en `BisonFlex.Flex`, uniek naast de gratis Bison-plugin. Niet meer veranderen na de lancering.
