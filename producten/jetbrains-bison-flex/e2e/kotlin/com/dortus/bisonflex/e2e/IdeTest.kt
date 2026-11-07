package com.dortus.bisonflex.e2e

import com.intellij.driver.client.Driver
import com.intellij.driver.client.Remote
import com.intellij.driver.client.service
import com.intellij.driver.model.LockSemantics
import com.intellij.driver.model.OnDispatcher
import com.intellij.driver.sdk.FileEditorManager
import com.intellij.driver.sdk.closeToolWindow
import com.intellij.driver.sdk.getToolWindow
import com.intellij.driver.sdk.invokeAction
import com.intellij.driver.sdk.openFile
import com.intellij.driver.sdk.openToolWindow
import com.intellij.driver.sdk.singleProject
import com.intellij.driver.sdk.waitForIndicators
import com.intellij.ide.starter.ci.CIServer
import com.intellij.ide.starter.ci.NoCIServer
import com.intellij.ide.starter.di.di
import com.intellij.ide.starter.driver.engine.runIdeWithDriver
import com.intellij.ide.starter.ide.IdeProductProvider
import com.intellij.ide.starter.models.TestCase
import com.intellij.ide.starter.plugins.PluginConfigurator
import com.intellij.ide.starter.project.LocalProjectInfo
import com.intellij.ide.starter.runner.Starter
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertFalse
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.fail
import org.kodein.di.DI
import org.kodein.di.bindSingleton
import java.nio.file.Files
import java.nio.file.Path
import kotlin.io.path.createDirectories
import kotlin.io.path.writeText
import kotlin.time.Duration.Companion.minutes

@Remote("com.intellij.openapi.fileTypes.FileTypeManager")
interface FileTypeManagerOpAfstand {
    fun getFileTypeByFileName(fileName: String): FileTypeOpAfstand
}

@Remote("com.intellij.openapi.fileTypes.FileType")
interface FileTypeOpAfstand {
    fun getName(): String
    fun getIcon(): IcoonOpAfstand?
}

@Remote("javax.swing.Icon")
interface IcoonOpAfstand {
    fun getIconWidth(): Int
}

@Remote("com.dortus.bisonflex.pro.ProMelding", plugin = "com.dortus.bisonflex")
interface ProMeldingOpAfstand {
    fun isGetoond(): Boolean
    fun aantalHints(): Int
}

/**
 * Test in de echte IDE (IDEA Community 2025.2) op GitHub Actions.
 * Eis 1, eis 8 (Pro-melding in beeld) en eis 10 (eerste deel) uit ontwerp.md: bestandssoorten herkend, schermen licht en donker.
 */
class IdeTest {
    companion object {
        /** Vast, zodat de test niet stilletjes naar een nieuwere IDE schuift (build 252.28539.149). */
        const val IDE_VERSIE = "2025.2.6.4"
    }

    init {
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

    private val schermen: Path = Path.of(System.getProperty("dortus.e2e.screenshots")).also { it.createDirectories() }

    @Test
    fun lichtThema() = draai("licht", "ExperimentalLight", "Light")

    @Test
    fun donkerThema() = draai("donker", "ExperimentalDark", "Dark")

    private fun draai(naam: String, themaId: String, kleurenschema: String) {
        // Engels winkelproject met een vaste mapnaam, zodat titelbalk en code op de schermen netjes zijn (Daan, beoordeling 3).
        val project = Files.createTempDirectory("bisonflex-$naam").resolve("calculator").createDirectories()
        Path.of(System.getProperty("dortus.e2e.winkelproject")).toFile().copyRecursively(project.toFile())

        Starter.newContext("bisonflex-$naam", TestCase(IdeProductProvider.IC, LocalProjectInfo(project)).useRelease(IDE_VERSIE))
            .apply {
                PluginConfigurator(this).installPluginFromPath(Path.of(System.getProperty("path.to.build.plugin")))
                // Thema vooraf vastzetten (GOK: zo werkt het in een verse config, de schermen laten het zien).
                val opties = paths.configDir.resolve("options").createDirectories()
                opties.resolve("laf.xml").writeText(
                    """<application><component name="LafManager" autodetect="false"><laf themeId="$themaId"/></component></application>"""
                )
                opties.resolve("colors.scheme.xml").writeText(
                    """<application><component name="EditorColorsManagerImpl"><global_color_scheme name="$kleurenschema"/></component></application>"""
                )
                // Geheugenmeter rechtsonder uit, hoort niet op een winkelplaatje (kan-punt controleur; werkt, run 42376488091).
                opties.resolve("ide.general.xml").writeText(
                    """<application><component name="StatusBarWidgetSettings"><option name="widgets"><map><entry key="Memory" value="false"/></map></option></component></application>"""
                )
                applyVMOptionsPatch {
                    addSystemProperty("idea.trust.all.projects", true)
                    addSystemProperty("ide.show.tips.on.startup.default.value", false)
                    // Factor 2 voor scherpe winkelplaatjes (Xvfb is 2880x1800, de IDE ziet 1440x900).
                    addSystemProperty("sun.java2d.uiScale.enabled", true)
                    addSystemProperty("sun.java2d.uiScale", "2")
                    // Alleen voor deze test: licentiestand GEEN, anders is de facade null en komt er nooit een Pro-melding.
                    addSystemProperty("bisonflex.internal.e2e.forceNoLicense", true)
                }
            }
            .runIdeWithDriver()
            .useDriverAndCloseIde {
                waitForIndicators(5.minutes)
                val ftm = service<FileTypeManagerOpAfstand>()
                for ((bestand, soort) in listOf("calc.y" to "Bison", "calc.yy" to "Bison", "calc.l" to "Flex", "calc.ll" to "Flex")) {
                    val ft = ftm.getFileTypeByFileName(bestand)
                    val gevonden = ft.getName()
                    val breedte = ft.getIcon()?.getIconWidth() ?: 0
                    val icoon = breedte == 16
                    println("DORTUS-E2E [$naam] $bestand -> soort $gevonden, icoon $breedte px")
                    assertEquals(soort, gevonden, "soort van $bestand")
                    assertTrue(icoon, "icoon van $bestand")
                }
                openFile("calc.y")
                pauze()
                scherm("$naam-calc-y.png")
                // Voor Daan: projectpaneel dicht, structuurweergave open, cursor op de laatste (lege) regel.
                closeToolWindow("Project")
                openToolWindow("Structure")
                cursorNaarEinde()
                pauze()
                val projectOpen = getToolWindow("Project").isVisible()
                val structuurOpen = getToolWindow("Structure").isVisible()
                println("DORTUS-E2E [$naam] Project-venster zichtbaar: $projectOpen, Structure-venster zichtbaar: $structuurOpen")
                assertTrue(structuurOpen, "Structure-venster zichtbaar")
                assertFalse(projectOpen, "Project-venster dicht")
                scherm("$naam-calc-y-structuur.png")
                openFile("calc.l")
                cursorNaarEinde()
                pauze()
                structuurBij(naam, "calc.l")
                scherm("$naam-calc-l.png")
                proMelding(naam)
                kleurenpagina(naam)
            }
    }

    private fun Driver.pauze() = Thread.sleep(3_000)

    /** Cursor naar het einde van het bestand, zodat er geen geel lampje in beeld staat. */
    private fun Driver.cursorNaarEinde() {
        val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor()
        if (editor == null) {
            println("DORTUS-E2E geen open editor gevonden voor de cursor")
            return
        }
        // Een cursor verzetten mag alleen op de EDT binnen een read-action (anders ThreadingAssertions-fout).
        try {
            val regel = withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
                val lengte = editor.getDocument().getText().length
                editor.getCaretModel().moveToOffset(lengte)
                editor.getCaretModel().getLogicalPosition().getLine()
            }
            println("DORTUS-E2E cursor op regel ${regel + 1} (einde bestand)")
        } catch (e: Exception) {
            println("DORTUS-E2E cursor verzetten mislukt: ${e.message?.take(200)}")
        }
    }

    /**
     * Ga naar definitie in stand GEEN (via de systeemeigenschap), Daan beoordeling 5:
     * 1. Binnen calc.y is gratis: Ctrl+B op `line` in `input line` springt naar `line:`, zonder melding.
     * 2. Tussen bestanden is Pro: Ctrl+B op `NUM` in `return NUM;` van calc.l geeft geen sprong maar de balloon
     *    (scherm `pro-melding`), en een tweede keer de korte hint in de editor (scherm `pro-hint`).
     */
    private fun Driver.proMelding(naam: String) {
        val melding = service<ProMeldingOpAfstand>()
        openFile("calc.y")
        pauze()
        val doelRegel = regelVan("\nline:") + 1
        cursorOp("input line", 6)
        val voor = cursorRegel()
        gaNaarDefinitie(naam) { cursorRegel() == doelRegel }
        val na = cursorRegel()
        println("DORTUS-E2E [$naam] sprong binnen calc.y: van regel ${voor + 1} naar regel ${na + 1} (verwacht ${doelRegel + 1}, line:), melding getoond ${melding.isGetoond()}")
        assertEquals(doelRegel, na, "Ctrl+B op line in calc.y springt naar line: ($naam)")
        assertFalse(melding.isGetoond(), "geen Pro-melding bij een sprong binnen calc.y ($naam)")

        openFile("calc.l")
        pauze()
        // Alleen van tab wisselen liet de structuurweergave bij calc.y staan (schermen pro-melding en pro-hint).
        structuurBij(naam, "calc.l")
        cursorOp("return NUM", 8)
        val regelL = cursorRegel()
        // Ctrl+zweven is geen klik: geen melding, geen hint, geen sprong (melding nog niet getoond).
        ctrlZweven(naam, melding, "return NUM", 8, regelL)
        val getoond = gaNaarDefinitie(naam) { melding.isGetoond() }
        Thread.sleep(2_000)
        println("DORTUS-E2E [$naam] eerste Ctrl+B op NUM in calc.l: melding getoond $getoond, hints ${melding.aantalHints()}, cursor regel ${cursorRegel() + 1} (was ${regelL + 1})")
        scherm("$naam-pro-melding.png")
        assertEquals("calc.l", structuurBestand(), "structuurweergave hoort bij calc.l op pro-melding ($naam)")
        assertTrue(getoond, "Pro-melding getoond ($naam)")
        assertEquals(0, melding.aantalHints(), "geen hint bij de eerste klik ($naam)")
        assertEquals(regelL, cursorRegel(), "geen sprong vanuit calc.l ($naam)")

        val hint = gaNaarDefinitie(naam) { melding.aantalHints() >= 1 }
        Thread.sleep(1_000)
        println("DORTUS-E2E [$naam] tweede Ctrl+B op NUM in calc.l: hint getoond $hint (hints ${melding.aantalHints()}), cursor regel ${cursorRegel() + 1}")
        scherm("$naam-pro-hint.png")
        assertTrue(hint, "korte Pro-hint getoond bij de tweede klik ($naam)")
        assertEquals(regelL, cursorRegel(), "geen sprong vanuit calc.l, tweede klik ($naam)")
        assertEquals("calc.l", structuurBestand(), "structuurweergave hoort bij calc.l op pro-hint ($naam)")
        // Nog eens Ctrl+zweven, nu de melding al getoond is: de hint mag niet opnieuw komen.
        ctrlZweven(naam, melding, "return NUM", 8, regelL)
    }

    /** GotoDeclaration via de Driver; is [klaar] na 10 s niet waar, dan nog eens met Ctrl+B via xdotool. */
    private fun Driver.gaNaarDefinitie(naam: String, klaar: () -> Boolean): Boolean {
        try { invokeAction("GotoDeclaration") } catch (e: Throwable) {
            println("DORTUS-E2E [$naam] GotoDeclaration via Driver mislukt: ${e.javaClass.simpleName}: ${e.message?.take(200)}")
        }
        if (wacht(10) { klaar() }) return true
        println("DORTUS-E2E [$naam] na GotoDeclaration (Driver) nog niet klaar, nu Ctrl+B (xdotool)")
        toets("ctrl+b")
        return wacht(10) { klaar() }
    }

    /** Regel (vanaf 0) van de cursor in de open editor, of -1. */
    private fun Driver.cursorRegel(): Int {
        val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor() ?: return -1
        return withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) { editor.getCaretModel().getLogicalPosition().getLine() }
    }

    /** Regel (vanaf 0) waarop [tekst] begint in de open editor. */
    private fun Driver.regelVan(tekst: String): Int {
        val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor() ?: return -1
        return withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
            val d = editor.getDocument()
            d.getText().substring(0, d.getText().indexOf(tekst)).count { it == '\n' }
        }
    }

    private fun wacht(seconden: Int, klaar: () -> Boolean): Boolean {
        repeat(seconden) { if (klaar()) return true; Thread.sleep(1_000) }
        return klaar()
    }

    /** Cursor op [tekst] plus [extra] tekens in de open editor. */
    private fun Driver.cursorOp(tekst: String, extra: Int) {
        val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor() ?: return println("DORTUS-E2E geen editor")
        val regel = withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
            val plek = editor.getDocument().getText().indexOf(tekst)
            editor.getCaretModel().moveToOffset(plek + extra)
            editor.getCaretModel().getLogicalPosition().getLine()
        }
        println("DORTUS-E2E cursor op '$tekst' +$extra, regel ${regel + 1}")
    }

    /**
     * Kleurenpagina (Daan punt 2): Settings openen zonder te wachten (een modale dialoog blokkeert anders de Driver),
     * wachten tot de dialoog actief is, zoeken op "Bison/Yacc" en een scherm maken. Mislukt het, dan staat de reden
     * in het log en faalt de test (pas hier, dus de bestandssoorten en de andere schermen zijn dan al getoetst).
     */
    private fun Driver.kleurenpagina(naam: String) {
        val ideVenster = actiefVenster()
        var dialoog: String? = null
        try {
            invokeAction("ShowSettings", now = false)
            // Wachten tot er een ander venster actief is dan de IDE (de Settings-dialoog), hoogstens 20 seconden.
            for (i in 1..20) {
                Thread.sleep(1_000)
                val nu = actiefVenster()
                if (nu != null && nu != ideVenster) { dialoog = nu; break }
            }
            if (dialoog == null) {
                println("DORTUS-E2E [$naam] kleurenpagina mislukt: Settings-dialoog niet actief na 20 s, niets getypt")
                return
            }
            Thread.sleep(2_000)
            typ("Bison/Yacc")
            Thread.sleep(3_000)
            scherm("$naam-kleurenpagina.png")
            toets("Escape")
            println("DORTUS-E2E [$naam] kleurenpagina: scherm gemaakt")
        } catch (e: Throwable) {
            println("DORTUS-E2E [$naam] kleurenpagina mislukt: ${e.javaClass.simpleName}: ${e.message?.take(300)}")
        } finally {
            // Daan wil deze pagina zien: is hij niet gelukt, dan faalt de test (na de andere schermen).
            assertTrue(dialoog != null && Files.exists(schermen.resolve("$naam-kleurenpagina.png")), "kleurenpagina in beeld ($naam)")
        }
    }

    /** Tekst typen in het venster met de focus, via xdotool (los van de Driver, dus ook in een modale dialoog). */
    private fun typ(tekst: String) {
        val code = ProcessBuilder("xdotool", "type", "--delay", "60", tekst).inheritIO().start().waitFor()
        println("DORTUS-E2E xdotool type '$tekst': code $code")
    }

    private fun toets(naam: String) {
        val code = ProcessBuilder("xdotool", "key", naam).inheritIO().start().waitFor()
        println("DORTUS-E2E xdotool key $naam: code $code")
    }

    /** Id van het actieve venster (de IDE of een dialoog), of null. */
    private fun actiefVenster(): String? = try {
        val p = ProcessBuilder("xdotool", "getactivewindow").redirectErrorStream(true).start()
        val uit = p.inputStream.bufferedReader().readText().trim()
        if (p.waitFor() == 0 && uit.isNotEmpty() && uit.all { it.isDigit() }) uit else null
    } catch (e: Exception) {
        null
    }

    /**
     * Schermafbeelding met ImageMagick: alleen het actieve venster (de IDE), zodat rand en balk van het testscherm
     * niet in beeld staan (Daan, beoordeling 3a). Geen actief venster: het hele scherm, en dat staat in het log.
     */
    private fun scherm(bestand: String) {
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
}
