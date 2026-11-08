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

dependencies {
    intellijPlatform {
        intellijIdeaCommunity("2025.2")
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
