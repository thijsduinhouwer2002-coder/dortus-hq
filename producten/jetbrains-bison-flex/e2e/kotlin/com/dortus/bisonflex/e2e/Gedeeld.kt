package com.dortus.bisonflex.e2e

import com.intellij.driver.client.Driver
import com.intellij.ide.starter.ci.CIServer
import com.intellij.ide.starter.ci.NoCIServer
import com.intellij.ide.starter.di.di
import com.intellij.ide.starter.ide.IDETestContext
import com.intellij.ide.starter.models.VMOptions
import com.intellij.ide.starter.plugins.PluginConfigurator
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.fail
import org.kodein.di.DI
import org.kodein.di.bindSingleton
import java.nio.file.Files
import java.nio.file.Path
import kotlin.io.path.createDirectories
import kotlin.io.path.writeText

/*
 * Gedeelde hulpstukken voor IdeTest (IDEA) en ClionTest (CLion): opzet van de test-IDE (project, thema,
 * geheugenmeter, VM-opties) en het werk met xdotool en ImageMagick (typen, toetsen, vensters, schermafbeeldingen).
 * Opruimtaak van de week (regel Codekwaliteit 5): eerst stond dit dubbel in IdeTest.kt en ClionTest.kt.
 */

/** Map voor de schermafbeeldingen (systeemeigenschap uit build.gradle.kts). */
internal val schermen: Path by lazy { Path.of(System.getProperty("dortus.e2e.screenshots")).also { it.createDirectories() } }

/** Een fout van Starter laat de JUnit-test falen in plaats van alleen een melding voor een CI-server. */
internal fun zetCiServer() {
    di = DI {
        extend(di)
        bindSingleton<CIServer>(overrides = true) {
            object : CIServer by NoCIServer {
                override fun reportTestFailure(testName: String, message: String, details: String, linkToLogs: String?) {
                    fail { "$testName faalt: $message\n$details" }
                }
            }
        }
    }
}

/**
 * Kopie van het Engelse winkelproject in een map die `calculator` heet, zodat titelbalk en code op de schermen
 * netjes zijn (Daan, beoordeling 3).
 */
internal fun winkelproject(voorvoegsel: String): Path {
    val project = Files.createTempDirectory(voorvoegsel).resolve("calculator").createDirectories()
    Path.of(System.getProperty("dortus.e2e.winkelproject")).toFile().copyRecursively(project.toFile())
    return project
}

/**
 * Plugin installeren en de test-IDE inrichten zoals op de winkelplaatjes: thema en editorschema vooraf vast,
 * geheugenmeter uit, projecten vertrouwd, geen tips, factor 2 (Xvfb is 2880x1800, de IDE ziet 1440x900).
 * [extra] voegt per IDE eigen systeemeigenschappen toe.
 */
internal fun IDETestContext.richIn(themaId: String, kleurenschema: String, extra: VMOptions.() -> Unit = {}) {
    PluginConfigurator(this).installPluginFromPath(Path.of(System.getProperty("path.to.build.plugin")))
    val opties = paths.configDir.resolve("options").createDirectories()
    opties.resolve("laf.xml").writeText(
        """<application><component name="LafManager" autodetect="false"><laf themeId="$themaId"/></component></application>"""
    )
    opties.resolve("colors.scheme.xml").writeText(
        """<application><component name="EditorColorsManagerImpl"><global_color_scheme name="$kleurenschema"/></component></application>"""
    )
    // Geheugenmeter rechtsonder uit, hoort niet op een winkelplaatje. Het onderdeel heet "StatusBar" in
    // ide.general.xml (StatusBarWidgetSettings.kt, @State(name = "StatusBar") in 252 tot en met master), de id van
    // de meter is "Memory". De oude naam "StatusBarWidgetSettings" stond in IdeTest (run 42376488091 zonder meter);
    // beide staan erin, een onbekend onderdeel negeert de IDE.
    val meter = """<option name="widgets"><map><entry key="Memory" value="false"/></map></option>"""
    opties.resolve("ide.general.xml").writeText(
        """<application><component name="StatusBar">$meter</component><component name="StatusBarWidgetSettings">$meter</component></application>"""
    )
    applyVMOptionsPatch {
        addSystemProperty("idea.trust.all.projects", true)
        addSystemProperty("ide.show.tips.on.startup.default.value", false)
        addSystemProperty("sun.java2d.uiScale.enabled", true)
        addSystemProperty("sun.java2d.uiScale", "2")
        extra()
    }
}

internal fun Driver.pauze() = Thread.sleep(3_000)

internal fun wacht(seconden: Int, klaar: () -> Boolean): Boolean {
    repeat(seconden) { if (klaar()) return true; Thread.sleep(1_000) }
    return klaar()
}

/** Tekst typen in het venster met de focus, via xdotool (los van de Driver, dus ook in een modale dialoog). */
internal fun typ(tekst: String) {
    val code = ProcessBuilder("xdotool", "type", "--delay", "60", tekst).inheritIO().start().waitFor()
    println("DORTUS-E2E xdotool type '$tekst': code $code")
}

internal fun toets(naam: String) {
    val code = ProcessBuilder("xdotool", "key", naam).inheritIO().start().waitFor()
    println("DORTUS-E2E xdotool key $naam: code $code")
}

/** Id van het actieve venster (de IDE of een dialoog), of null. */
internal fun actiefVenster(): String? = try {
    val p = ProcessBuilder("xdotool", "getactivewindow").redirectErrorStream(true).start()
    val uit = p.inputStream.bufferedReader().readText().trim()
    if (p.waitFor() == 0 && uit.isNotEmpty() && uit.all { it.isDigit() }) uit else null
} catch (e: Exception) {
    null
}

/** Zichtbare vensters met titel (xdotool): id en titel. */
internal fun vensters(): List<Pair<String, String>> = try {
    val p = ProcessBuilder("bash", "-c", "for w in \$(xdotool search --onlyvisible --name . 2>/dev/null); do printf '%s\\t%s\\n' \"\$w\" \"\$(xdotool getwindowname \$w)\"; done")
        .redirectErrorStream(true).start()
    val uit = p.inputStream.bufferedReader().readLines()
    p.waitFor()
    uit.mapNotNull { r -> r.split('\t', limit = 2).takeIf { it.size == 2 && it[1].isNotBlank() }?.let { it[0] to it[1] } }
} catch (e: Exception) {
    emptyList()
}

/**
 * Schermafbeelding met ImageMagick: alleen het actieve venster (de IDE), zodat rand en balk van het testscherm
 * niet in beeld staan (Daan, beoordeling 3a). Geen actief venster: het hele scherm, en dat staat in het log.
 */
internal fun scherm(bestand: String) {
    val doel = schermen.resolve(bestand)
    val venster = actiefVenster()
    println("DORTUS-E2E $bestand: venster ${venster ?: "geen, heel scherm"}")
    val p = ProcessBuilder("import", "-window", venster ?: "root", doel.toString()).inheritIO().start()
    val code = p.waitFor()
    val grootte = if (Files.exists(doel)) Files.size(doel) else 0
    val maat = ProcessBuilder("identify", "-format", "%wx%h", doel.toString()).start().let { it.inputStream.bufferedReader().readText().also { _ -> it.waitFor() } }
    println("DORTUS-E2E schermafbeelding $bestand: code $code, $grootte bytes, $maat pixels")
    assertEquals(0, code, "import voor $bestand")
    assertTrue(grootte > 10_000, "schermafbeelding $bestand is te klein ($grootte bytes)")
}
