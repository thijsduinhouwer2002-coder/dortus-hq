# JetBrains: plan voor de IDE-test op GitHub Actions (7 nov 2026)

Onderzocht door een agent met curl, nog niet nagekeken en nog niet gedraaid. De eerste echte run op GitHub Actions is de toets. Alles DERDEN (met link) of GOK.

## Keuzes
- **Aanpak: Starter + Driver** met `intellijPlatformTesting.testIdeUi` en `testFramework(TestFrameworkType.Starter, configurationName = "integrationTestImplementation")`, JUnit 5. De SDK-docs noemen alleen deze weg; Driver en UI heten daar nog "experimental" (DERDEN: https://plugins.jetbrains.com/docs/intellij/integration-tests-intro.html). Remote-Robot (`runIdeForUiTests`) is de oude weg.
- **Scherm:** zonder `DISPLAY` start Starter de IDE zelf in `xvfb-run` met fluxbox. Op de runner `xvfb fluxbox x11-utils` installeren, geen eigen `xvfb-run` om Gradle (DERDEN: `LinuxIdeDistribution.kt` en `LinuxWindowManagerHandler.kt` in JetBrains/intellij-community, map `tools/intellij.tools.ide.starter`).
- **Schermafbeeldingen:** Driver heeft `openFile(pad)` en `takeScreenshot(map)` (DERDEN: `platform/remote-driver` in intellij-community, tak 252). Noodweg: `import -window root -display :88` (GOK).
- **Thema:** vóór de start `options/laf.xml` in de config-map schrijven met `LafManager`, `autodetect="false"` en `themeId` `ExperimentalLight` of `ExperimentalDark`; één IDE-start per thema (GOK, nakijken in de eerste run).
- **Welke IDE:** IDEA Community 2025.2 (geen licentie nodig, GOK maar vrij zeker). CLion vraagt in Starter een offline sleutel; zonder sleutel verwacht ik een licentievenster dat de test laat hangen (GOK). Dus CLion niet in CI tot er een sleutel is, en de plugin vrij houden van CLion-afhankelijkheden.

## Workflow
`.github/workflows/jetbrains-bison-flex-e2e.yml`: start bij wijzigingen in `producten/jetbrains-bison-flex/**` op main en via workflow_dispatch; Java 21 (temurin), `gradle/actions/setup-gradle@v4`, apt-pakketten hierboven, `./gradlew integrationTest`, artefact uploaden, en daarna de stap "Schermafbeeldingen openbaar zetten (tak schermen)" letterlijk uit `rollwright-e2e.yml`, met de map `jetbrains-bison-flex/`. Het volledige voorbeeld (build.gradle.kts, testklasse, yaml) staat in het logboek van de agent; de bouwer schrijft het opnieuw op basis van de bronnen hierboven.

## Open
- Waar Starter de test-IDE en logs neerzet (kijken in de eerste run).
- Of `intellijIdeaCommunity("2025.2")` in plugin 2.20.0 nog werkt of `intellijIdea(...)` met type IC moet.
