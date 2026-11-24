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

/**
 * Fouten van IntelliJ zelf die niets met de plug-in te maken hebben en soms optreden. Alleen overslaan als er geen
 * enkele regel van Bison & Flex (com.dortus) in de melding staat; elke andere fout laat de test nog steeds falen.
 * - "node is not a child" in OccurenceNavigatorSupport: de knop "Next Conflict" van het conflictvenster wordt
 *   bijgewerkt terwijl de boom net verandert (run 45262737601, donker thema, stap hernoemen naar line; licht slaagde).
 *   Zelfde fout bij de knop "Previous Conflict" heet "argument is not a child" (getPreviousSibling; run 45305066655,
 *   licht thema). Daarom alleen "is not a child" plus OccurenceNavigatorSupport.
 */
private val bekendePlatformfouten = listOf(
    listOf("is not a child", "OccurenceNavigatorSupport"),
)

internal fun bekendePlatformfout(message: String, details: String): Boolean {
    val tekst = "$message\n$details"
    if (tekst.contains("com.dortus")) return false
    return bekendePlatformfouten.any { delen -> delen.all { tekst.contains(it) } }
}

/** Een fout van Starter laat de JUnit-test falen in plaats van alleen een melding voor een CI-server. */
internal fun zetCiServer() {
    di = DI {
        extend(di)
        bindSingleton<CIServer>(overrides = true) {
            object : CIServer by NoCIServer {
                override fun reportTestFailure(testName: String, message: String, details: String, linkToLogs: String?) {
                    if (bekendePlatformfout(message, details)) {
                        println("DORTUS-E2E bekende fout van het platform zelf overgeslagen (geen Bison & Flex in de stack): ${message.lineSequence().firstOrNull()}")
                        return
                    }
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
    // Vaste map in plaats van createTempDirectory (roestronde R4): de willekeurige mapnaam stond in de projectboom
    // en kleurde de projectknop bovenaan elke run anders, waardoor de beeldvergelijking vals alarm gaf.
    val basis = Path.of(System.getProperty("java.io.tmpdir"), voorvoegsel)
    basis.toFile().deleteRecursively()
    val project = basis.resolve("calculator").createDirectories()
    Path.of(System.getProperty("dortus.e2e.winkelproject")).toFile().copyRecursively(project.toFile())
    // Scheiding in het instellingenvenster vast (roestronde R4, herkeuring 2): standaard 0,2, maar de boom links
    // duwde hem van run tot run naar 474 tot 630 px (kleurenpagina). Met 0,33 ligt hij voorbij die breedtes en blijft
    // hij staan. Projectinstelling settings.editor.splitter.proportion (SettingsEditor.java) in .idea/workspace.xml.
    // Alleen voor IDEA (de kleurenpagina zit in IdeTest): met dit bestand koos CLion van run tot run een andere breedte
    // voor het zijpaneel (runs 44496665424 en 44496687498), zonder bleef CLion gelijk.
    if (voorvoegsel.startsWith("bisonflex-")) project.resolve(".idea").createDirectories().resolve("workspace.xml").writeText(
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<project version=\"4\">\n" +
            "  <component name=\"PropertiesComponent\"><![CDATA[{\n  \"keyToString\": {\n" +
            "    \"settings.editor.splitter.proportion\": \"0.33\"\n  }\n}]]></component>\n</project>\n"
    )
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

/**
 * Zet het actieve venster (een dialoog, nooit de IDE zelf) op een vaste maat, zodat de schermafbeelding elke run
 * dezelfde maat heeft (roestronde R4: dialogen sprongen tussen 1600x1174 en 1592x1172, en panelen schoven mee).
 */
internal fun vastVenster(breedte: Int, hoogte: Int) {
    val v = actiefVenster() ?: return
    val code = ProcessBuilder("xdotool", "windowsize", v, breedte.toString(), hoogte.toString()).inheritIO().start().waitFor()
    println("DORTUS-E2E venster $v vast op ${breedte}x$hoogte: code $code")
    Thread.sleep(1_500)
}

/** Id van het actieve venster (de IDE of een dialoog), of null. */
internal fun actiefVenster(): String? = try {
    val p = ProcessBuilder("xdotool", "getactivewindow").redirectErrorStream(true).start()
    val uit = p.inputStream.bufferedReader().readText().trim()
    if (p.waitFor() == 0 && uit.isNotEmpty() && uit.all { it.isDigit() }) uit else null
} catch (e: Exception) {
    null
}

/**
 * Zet in het log welke vensters zichtbaar zijn en welk venster actief is, met maat. Voor de EAP 263: daar was het
 * actieve venster 1720x1134 en veranderde het beeld niet (runs 45095465886, 45096596345), mogelijk een dialoog
 * boven het IDE-venster.
 */
internal fun vensterVerslag(naam: String) {
    val actief = actiefVenster()
    val maat = actief?.let {
        try {
            val p = ProcessBuilder("xdotool", "getwindowname", it, "getwindowgeometry", it).redirectErrorStream(true).start()
            p.inputStream.bufferedReader().readText().replace("\n", " | ").trim().also { _ -> p.waitFor() }
        } catch (e: Exception) { "?" }
    }
    println("DORTUS-E2E [$naam] actief venster: ${actief ?: "geen"} ($maat)")
    for ((id, titel) in vensters()) println("DORTUS-E2E [$naam] zichtbaar venster $id: '$titel'")
}

private val LICENTIE = Regex("\\b(licen|activat|subscription|trial|log ?in|sign ?in|evaluat|expired|agreement|terms|eula)", RegexOption.IGNORE_CASE)

/**
 * Faalt met een duidelijke reden als er een licentie-, inlog- of voorwaardenvenster zichtbaar is (titel, xdotool).
 * Er wordt niets aangeklikt. Waarom: de bugfix-EAP 263.8311.30 (2026.3.1) toont "No subscription" en "Bison & Flex,
 * Activate to enable" (GEZIEN, run 45101820137, donker-calc-y.png); de test liep dan vast op waitForIndicators of
 * gaf een lege structuurweergave, wat op een fout in de plug-in leek. [oorzaak]: de fout die erna kwam, of null.
 */
internal fun geenLicentievenster(naam: String, oorzaak: Throwable? = null) {
    val (id, titel) = vensters().firstOrNull { LICENTIE.containsMatchIn(it.second) } ?: return
    val doel = schermen.resolve("$naam-licentievenster.png")
    val code = try { ProcessBuilder("import", "-window", id, doel.toString()).inheritIO().start().waitFor() } catch (e: Exception) { -1 }
    val reden = "IDE toont een licentie- of voorwaardenvenster '$titel' (schermafbeelding ${doel.fileName}, code $code). " +
        "Een bugfix-EAP (zoals 2026.3.1) heeft geen ingebouwde licentie: kies een EAP van een grote versie of de vaste versie. " +
        "Of de plug-in werkt, zegt de Plugin Verifier."
    println("DORTUS-E2E [$naam] LICENTIE/VOORWAARDEN: $reden")
    if (oorzaak != null) fail(reden, oorzaak) else fail(reden)
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
 * Zoals [scherm], maar pas als het venster stilstaat: twee opnamen na elkaar (300 ms ertussen) zijn gelijk, hooguit
 * [pogingen] keer. Voor beelden met een melding die nog invaagt of een tooltip die nog komt (roestronde R4: zulke
 * plaatjes verschilden van run tot run, zodat de beeldvergelijking vals alarm gaf).
 */
internal fun schermStil(bestand: String, pogingen: Int = 10) {
    wachtTotStil(bestand, actiefVenster() ?: "root", pogingen)
    scherm(bestand)
}

/** Wacht tot twee opnamen van [venster] (of "root") na elkaar gelijk zijn, hooguit [pogingen] keer. */
internal fun wachtTotStil(bestand: String, venster: String, pogingen: Int = 10) {
    var vorige: ByteArray? = null
    for (i in 1..pogingen) {
        val tijdelijk = Files.createTempFile("dortus-stil", ".rgb")
        ProcessBuilder("import", "-window", venster, "rgb:$tijdelijk").start().waitFor()
        val nu = Files.readAllBytes(tijdelijk)
        Files.deleteIfExists(tijdelijk)
        if (vorige != null && nu.isNotEmpty() && nu.contentEquals(vorige)) {
            println("DORTUS-E2E $bestand: beeld stil na $i opnamen")
            break
        }
        if (i == pogingen) println("DORTUS-E2E $bestand: beeld niet stil na $pogingen opnamen, toch opgenomen")
        vorige = nu
        Thread.sleep(300)
    }
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
