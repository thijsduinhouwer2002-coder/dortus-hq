import org.jetbrains.intellij.platform.gradle.IntelliJPlatformType
import org.jetbrains.intellij.platform.gradle.TestFrameworkType

plugins {
    id("org.jetbrains.kotlin.jvm") version "2.4.21"
    id("org.jetbrains.intellij.platform") version "2.20.0"
}

group = "com.dortus"
version = "2026.1.0"

kotlin { jvmToolchain(21) }

// De IDE-test (echte IDE via Starter + Driver) staat in e2e/, zie organisatie/regels.md.
sourceSets {
    create("integrationTest") {
        compileClasspath += sourceSets.main.get().output
        runtimeClasspath += sourceSets.main.get().output
    }
}
kotlin.sourceSets.named("integrationTest") { kotlin.srcDir("e2e/kotlin") }

repositories {
    // Alleen de JetBrains-spiegel: Maven Central geeft hier vaak 429 (zie bouwsjabloon.md).
    maven("https://cache-redirector.jetbrains.com/repo1.maven.org/maven2")
    intellijPlatform { defaultRepositories() }
}

configurations.getByName("integrationTestImplementation") {
    extendsFrom(configurations.getByName("testImplementation"))
}

// Doel-IDE voor de unittests: standaard IDEA Community (IC). Met -PdoelIde=CL draaien
// dezelfde unittests tegen CLion 2025.2, de doelgroep (eis 1). De IDE-test (integrationTest)
// draait alleen met IC, zie .github/workflows/jetbrains-bison-flex-e2e.yml en -clion.yml.
val doelIde = (findProperty("doelIde") as String?)?.uppercase() ?: "IC"

dependencies {
    intellijPlatform {
        when (doelIde) {
            "IC" -> intellijIdeaCommunity("2025.2")
            "CL" -> clion("2025.2")
            else -> error("Onbekende doelIde '$doelIde', kies IC of CL")
        }
        pluginVerifier()
        testFramework(TestFrameworkType.Platform)
        testFramework(TestFrameworkType.Starter, configurationName = "integrationTestImplementation")
    }
    testImplementation("junit:junit:4.13.2")
    "integrationTestImplementation"("org.junit.jupiter:junit-jupiter:5.11.4")
    "integrationTestRuntimeOnly"("org.junit.platform:junit-platform-launcher:1.11.4")
    "integrationTestImplementation"("org.kodein.di:kodein-di-jvm:7.20.2")
    "integrationTestImplementation"("org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm:1.10.1")
}

intellijPlatform {
    pluginConfiguration {
        ideaVersion { sinceBuild = "252" }
    }
    buildSearchableOptions = false
    // Uploaden van updates (taak publishPlugin), alleen vanuit de workflow
    // jetbrains-bison-flex-upload.yml met het secret JETBRAINS_MARKETPLACE_TOKEN.
    publishing {
        token = providers.environmentVariable("PUBLISH_TOKEN")
    }
    // Plugin Verifier (taak verifyPlugin) tegen de doelgroep CLion en tegen IDEA Community.
    pluginVerification {
        ides {
            create(IntelliJPlatformType.CLion, "2025.2")
            create(IntelliJPlatformType.IntellijIdeaCommunity, "2025.2")
        }
    }
}

// Twee IDE-tests met dezelfde instellingen: IDEA Community (integrationTest) en CLion EAP (clionTest, ClionTest.kt).
fun Test.ideTestInstellingen() {
    val src = sourceSets.getByName("integrationTest")
    testClassesDirs = src.output.classesDirs
    classpath = src.runtimeClasspath
    useJUnitPlatform()
    dependsOn(tasks.buildPlugin)
    systemProperty("path.to.build.plugin", tasks.buildPlugin.get().archiveFile.get().asFile.absolutePath)
    systemProperty("dortus.e2e.project", layout.projectDirectory.dir("e2e/project").asFile.absolutePath)
    systemProperty("dortus.e2e.winkelproject", layout.projectDirectory.dir("e2e/calculator").asFile.absolutePath)
    systemProperty("dortus.e2e.screenshots", layout.projectDirectory.dir("e2e/screenshots").asFile.absolutePath)
    testLogging { events("passed", "failed", "skipped", "standard_out", "standard_error"); showStandardStreams = true }
}

intellijPlatformTesting.testIdeUi.register("integrationTest") {
    task {
        ideTestInstellingen()
        filter { excludeTestsMatching("*.ClionTest") }
    }
}

intellijPlatformTesting.testIdeUi.register("clionTest") {
    task {
        ideTestInstellingen()
        filter { includeTestsMatching("*.ClionTest") }
    }
}

tasks.test {
    systemProperty("dortus.testdata", layout.projectDirectory.dir("testdata").asFile.absolutePath)
    testLogging { events("passed", "failed", "skipped") }
}
