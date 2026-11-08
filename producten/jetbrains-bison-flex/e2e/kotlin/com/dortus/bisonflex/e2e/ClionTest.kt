package com.dortus.bisonflex.e2e

import com.intellij.driver.client.Driver
import com.intellij.driver.client.Remote
import com.intellij.driver.client.service
import com.intellij.driver.model.OnDispatcher
import com.intellij.driver.sdk.FileEditorManager
import com.intellij.driver.sdk.getEnabledPluginsIds
import com.intellij.driver.sdk.getHighlights
import com.intellij.driver.sdk.getPlugin
import com.intellij.driver.sdk.openFile
import com.intellij.driver.sdk.openToolWindow
import com.intellij.driver.sdk.singleProject
import com.intellij.driver.sdk.waitForCodeAnalysis
import com.intellij.driver.sdk.waitForIndicators
import com.intellij.ide.starter.driver.engine.runIdeWithDriver
import com.intellij.ide.starter.ide.IdeProductProvider
import com.intellij.ide.starter.models.TestCase
import com.intellij.ide.starter.plugins.PluginConfigurator
import com.intellij.ide.starter.project.LocalProjectInfo
import com.intellij.ide.starter.runner.Starter
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.fail
import java.nio.file.Files
import java.nio.file.Path
import kotlin.io.path.createDirectories
import kotlin.io.path.writeText
import kotlin.time.Duration.Companion.minutes

@Remote("javax.swing.JTree")
interface BoomOpAfstand {
    fun getRowCount(): Int
    fun getPathForRow(row: Int): BoomPadOpAfstand?
}

@Remote("javax.swing.tree.TreePath")
interface BoomPadOpAfstand {
    fun getLastPathComponent(): Any?
}

/**
 * Eis 1 in de echte CLion (de doelgroep van de plugin), los van IdeTest: een eigen Gradle-taak `clionTest`.
 * Gebruikt de EAP-build van CLion, want die heeft een ingebouwde tijdelijke licentie (30 dagen na de builddatum,
 * Starter weigert een verlopen EAP zelf). Is de build verlopen, kies dan de nieuwste EAP en pas [CLION_BUILD] aan.
 * Verschijnt er toch een licentie- of voorwaardenvenster, dan klikt de test niets weg: schermafbeelding, titel in
 * het log, en de test faalt met die reden.
 */
class ClionTest {
    companion object {
        /** CLion 2026.3 EAP van 23 okt 2026, geldig tot ongeveer 22 nov 2026. */
        const val CLION_BUILD = "263.7307.35"
        private const val PLUGIN_ID = "com.dortus.bisonflex"
        private val VERDACHT = Regex("licen|activat|agreement|terms|eula|register|subscription|trial|log ?in|sign ?in|evaluat|privacy|data sharing|expired", RegexOption.IGNORE_CASE)
    }

    /** Hergebruik van de hulpfuncties (schermafbeelding, pauze, wachten) en de CIServer-instelling van IdeTest. */
    private val ide = IdeTest()
    private val schermen: Path = Path.of(System.getProperty("dortus.e2e.screenshots")).also { it.createDirectories() }

    @Test
    fun lichtThema() = draai("licht", "ExperimentalLight", "Light")

    @Test
    fun donkerThema() = draai("donker", "ExperimentalDark", "Dark")

    private fun draai(naam: String, themaId: String, kleurenschema: String) {
        val project = Files.createTempDirectory("clion-$naam").resolve("calculator").createDirectories()
        Path.of(System.getProperty("dortus.e2e.winkelproject")).toFile().copyRecursively(project.toFile())
        val wachter = Vensterwachter(naam).also { it.start() }
        try {
            Starter.newContext("clion-$naam", TestCase(IdeProductProvider.CL, LocalProjectInfo(project)).useEAP(CLION_BUILD))
                .apply {
                    PluginConfigurator(this).installPluginFromPath(Path.of(System.getProperty("path.to.build.plugin")))
                    val opties = paths.configDir.resolve("options").createDirectories()
                    opties.resolve("laf.xml").writeText(
                        """<application><component name="LafManager" autodetect="false"><laf themeId="$themaId"/></component></application>"""
                    )
                    opties.resolve("colors.scheme.xml").writeText(
                        """<application><component name="EditorColorsManagerImpl"><global_color_scheme name="$kleurenschema"/></component></application>"""
                    )
                    applyVMOptionsPatch {
                        addSystemProperty("idea.trust.all.projects", true)
                        addSystemProperty("ide.show.tips.on.startup.default.value", false)
                        addSystemProperty("sun.java2d.uiScale.enabled", true)
                        addSystemProperty("sun.java2d.uiScale", "2")
                    }
                }
                .runIdeWithDriver()
                .useDriverAndCloseIde {
                    try {
                        controleer(naam, wachter)
                    } catch (e: Throwable) {
                        wachter.reden?.let { fail("CLion [$naam] toont een licentie- of voorwaardenvenster: $it", e) }
                        throw e
                    }
                }
        } catch (e: Throwable) {
            wachter.reden?.let { if (e !is AssertionError) fail("CLion [$naam] toont een licentie- of voorwaardenvenster: $it", e) }
            throw e
        } finally {
            wachter.klaar()
        }
    }

    private fun Driver.controleer(naam: String, wachter: Vensterwachter) {
        waitForIndicators(5.minutes)
        wachter.reden?.let { fail("CLion [$naam] toont een licentie- of voorwaardenvenster: $it") }

        val ids = getEnabledPluginsIds()
        val plugin = getPlugin(PLUGIN_ID)
        println("DORTUS-E2E [clion-$naam] plugin $PLUGIN_ID geladen: ${PLUGIN_ID in ids}, naam '${plugin?.getName()}', aan ${plugin?.isEnabled()}, plugins totaal ${ids.size}")
        assertTrue(PLUGIN_ID in ids, "plugin staat in de geladen plugins van CLion ($naam)")

        val ftm = service<FileTypeManagerOpAfstand>()
        for ((bestand, soort) in listOf("calc.y" to "Bison", "calc.l" to "Flex")) {
            val gevonden = ftm.getFileTypeByFileName(bestand).getName()
            println("DORTUS-E2E [clion-$naam] $bestand -> soort $gevonden")
            assertEquals(soort, gevonden, "soort van $bestand in CLion ($naam)")
        }

        openFile("calc.l")
        with(ide) { pauze() }
        openFile("calc.y")
        with(ide) { pauze() }
        val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor() ?: fail("geen editor voor calc.y ($naam)")
        val bestand = editor.getVirtualFile()
        println("DORTUS-E2E [clion-$naam] open editor: ${bestand.getName()}")
        waitForCodeAnalysis(singleProject(), bestand, 2.minutes)
        val fouten = getHighlights(editor.getDocument()).filter { it.getSeverity().getName() == "ERROR" }
        println("DORTUS-E2E [clion-$naam] rode fouten in calc.y: ${fouten.size} ${fouten.take(5).map { "'${it.getText()}': ${it.getDescription()}" }}")
        assertEquals(0, fouten.size, "geen rode syntaxfouten in calc.y ($naam)")

        openToolWindow("Structure")
        structuurBij("clion-$naam", "calc.y")
        val regels = structuurRegels()
        println("DORTUS-E2E [clion-$naam] structuurweergave calc.y: ${regels.size} regels ${regels.take(8)}")
        assertTrue(regels.size > 1, "structuurweergave toont regels van calc.y ($naam)")
        with(ide) { pauze() }
        wachter.reden?.let { fail("CLion [$naam] toont een licentie- of voorwaardenvenster: $it") }
        ide.scherm("clion-$naam-calc-y.png")
    }

    /** Tekst van de zichtbare rijen in de structuurweergave (een paar keer proberen, de boom bouwt traag op). */
    private fun Driver.structuurRegels(): List<String> {
        var regels = emptyList<String>()
        ide.wacht(15) {
            val boom = structuurBoom() ?: return@wacht false
            regels = withContext(OnDispatcher.EDT) {
                val b = cast(boom, BoomOpAfstand::class)
                (0 until b.getRowCount()).map { b.getPathForRow(it)?.getLastPathComponent()?.toString() ?: "?" }
            }
            regels.size > 1
        }
        return regels
    }

    /**
     * Kijkt elke 3 seconden welke vensters er zichtbaar zijn (xdotool) en zet nieuwe titels in het log. Heeft een
     * venster een titel die op een licentie, inlog of voorwaarden lijkt: schermafbeelding van dat venster en de reden
     * bewaren. Er wordt niets aangeklikt.
     */
    private inner class Vensterwachter(private val naam: String) : Thread("vensterwachter-$naam") {
        @Volatile var reden: String? = null
        @Volatile private var door = true
        private val gezien = mutableSetOf<String>()

        init { isDaemon = true }

        override fun run() {
            while (door) {
                for ((id, titel) in vensters()) {
                    if (gezien.add("$id $titel")) println("DORTUS-E2E [clion-$naam] venster $id: '$titel'")
                    if (reden == null && VERDACHT.containsMatchIn(titel)) {
                        val doel = schermen.resolve("clion-$naam-licentievenster.png")
                        val code = ProcessBuilder("import", "-window", id, doel.toString()).inheritIO().start().waitFor()
                        reden = "venster '$titel' (schermafbeelding ${doel.fileName}, code $code)"
                        println("DORTUS-E2E [clion-$naam] LICENTIE/VOORWAARDEN: $reden")
                    }
                }
                try { sleep(3_000) } catch (e: InterruptedException) { return }
            }
        }

        fun klaar() { door = false; interrupt() }

        private fun vensters(): List<Pair<String, String>> = try {
            val p = ProcessBuilder("bash", "-c", "for w in \$(xdotool search --onlyvisible --name . 2>/dev/null); do printf '%s\\t%s\\n' \"\$w\" \"\$(xdotool getwindowname \$w)\"; done")
                .redirectErrorStream(true).start()
            val uit = p.inputStream.bufferedReader().readLines()
            p.waitFor()
            uit.mapNotNull { r -> r.split('\t', limit = 2).takeIf { it.size == 2 && it[1].isNotBlank() }?.let { it[0] to it[1] } }
        } catch (e: Exception) {
            emptyList()
        }
    }
}
