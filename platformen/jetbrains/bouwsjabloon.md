# JetBrains: bouwsjabloon (werkt, 6 nov 2026 16:11 UTC)

Een lege plugin met twee tests is in de run gebouwd en getest: `buildPlugin test`, 2 tests, 0 fouten, zip van 1.692 bytes (GEZIEN).

## Wat nodig is
- Gradle 9 via de wrapper. IntelliJ Platform Gradle Plugin 2.20.0 weigert Gradle 8.14.3 die op de machine staat. Wrapper maken in een lege map (`gradle wrapper --gradle-version 9.8.2`) en `gradlew` en `gradle/` overzetten.
- Java 21 (staat erop).
- Maven Central geeft 429 (te veel verzoeken). Daarom alleen de JetBrains-spiegel gebruiken, en `mavenCentral()` weglaten. Met `mavenCentral()` erbij valt Gradle terug op Maven Central en faalt dan alsnog.
- Eerste build duurt ±2 minuten (IDE downloaden).

## settings.gradle.kts (aangevuld 6 nov 17:00 UTC)
In een nieuwe omgeving faalde de build eerst op 429 van Maven Central bij het ophalen van de Kotlin-plugin. Oplossing, werkt (GEZIEN):
```kotlin
pluginManagement {
    repositories {
        maven("https://cache-redirector.jetbrains.com/plugins.gradle.org/m2")
        maven("https://cache-redirector.jetbrains.com/repo1.maven.org/maven2")
    }
}
rootProject.name = "naam"
```
Voor `gradle wrapper` in een lege map eerst een leeg `settings.gradle` maken, anders faalt het. `intellijIdea("2026.2")` werkt ook als doel (GEZIEN).

## build.gradle.kts
```kotlin
plugins {
    id("org.jetbrains.kotlin.jvm") version "2.4.21"
    id("org.jetbrains.intellij.platform") version "2.20.0"
}
group = "com.dortus"
version = "0.0.1"
kotlin { jvmToolchain(21) }
repositories {
    maven("https://cache-redirector.jetbrains.com/repo1.maven.org/maven2")
    intellijPlatform { defaultRepositories() }
}
dependencies {
    intellijPlatform {
        intellijIdeaCommunity("2025.2")
        testFramework(org.jetbrains.intellij.platform.gradle.TestFrameworkType.Platform)
    }
    testImplementation("junit:junit:4.13.2")
}
intellijPlatform {
    pluginConfiguration { ideaVersion { sinceBuild = "252" } }
    buildSearchableOptions = false
}
```

## Test
Testen met `BasePlatformTestCase` (JUnit 4) werken: een test die een bestand opent via `myFixture.configureByText` slaagt.
