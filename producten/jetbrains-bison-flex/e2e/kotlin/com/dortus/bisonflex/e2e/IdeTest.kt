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
import com.intellij.ide.starter.driver.engine.runIdeWithDriver
import com.intellij.ide.starter.ide.IdeProductProvider
import com.intellij.ide.starter.models.TestCase
import com.intellij.ide.starter.project.LocalProjectInfo
import com.intellij.ide.starter.runner.Starter
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertFalse
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test
import java.nio.file.Files
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
    fun isGetoondVoor(actie: String): Boolean
    fun aantalHints(): Int
    fun aantalHintsZonderEditor(): Int
    fun balloonZonderEditorInBeeld(): Boolean
    fun laatstePlekZonderEditor(): String?
    fun laatsteHint(): String?
    fun laatsteMelding(): String?
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

    init { zetCiServer() }

    @Test
    fun lichtThema() = draai("licht", "ExperimentalLight", "Light")

    @Test
    fun donkerThema() = draai("donker", "ExperimentalDark", "Dark")

    private fun draai(naam: String, themaId: String, kleurenschema: String) {
        val project = winkelproject("bisonflex-$naam")
        Starter.newContext("bisonflex-$naam", TestCase(IdeProductProvider.IC, LocalProjectInfo(project)).useRelease(IDE_VERSIE))
            .apply {
                // Thema vooraf vastzetten (GOK: zo werkt het in een verse config, de schermen laten het zien).
                richIn(themaId, kleurenschema) {
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
                // Hernoemen na de ga-naar-balloon (Daan, beoordeling 8), in Hernoemen.kt.
                hernoemen(this, naam)
                // Eis 7: stand halverwege op GELDIG, meldingen en Alt+Enter in beeld (Meldingen.kt).
                meldingen(this, naam)
                kleurenpagina(naam)
                // Schermen voor winkelplaatje 4 en 5, alleen licht, als laatste stap (Winkelschermen.kt).
                if (naam == "licht") winkelschermen(this, naam)
            }
    }

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
     * 3. Ctrl+zweven (Daan, beoordeling 6 punt 1): over `line` in calc.y als controle (daar hoort de IDE te
     *    onderstrepen), over `NUM` in calc.l vóór de eerste Ctrl+B (geen balloon, geen hint) en na de balloon
     *    (het aantal hints loopt niet op).
     */
    private fun Driver.proMelding(naam: String) {
        val melding = service<ProMeldingOpAfstand>()
        // "Start free trial" roept de registratie van de IDE aan (Proef.kt); hier alleen kijken welke actie er is.
        val acties = service<com.intellij.driver.sdk.ActionManager>()
        println("DORTUS-E2E [$naam] registratie-acties: RegisterPlugins ${acties.getAction("RegisterPlugins") != null}, Register ${acties.getAction("Register") != null}")
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
        val controle = ctrlZweven("$naam calc.y", melding, "input line", 6, na)
        println("DORTUS-E2E [$naam] controle Ctrl+zweven op line in calc.y: $controle onderstreping(en)")

        openFile("calc.l")
        pauze()
        // Alleen van tab wisselen liet de structuurweergave bij calc.y staan (schermen pro-melding en pro-hint).
        structuurBij(naam, "calc.l")
        cursorOp("return NUM", 8)
        val regelL = cursorRegel()
        ctrlZweven("$naam voor Ctrl+B", melding, "return NUM", 8, regelL)
        println("DORTUS-E2E [$naam] na Ctrl+zweven voor de eerste Ctrl+B: melding getoond ${melding.isGetoond()}, hints ${melding.aantalHints()}")
        assertFalse(melding.isGetoond(), "geen balloon door Ctrl+zweven voor de eerste Ctrl+B ($naam)")
        assertEquals(0, melding.aantalHints(), "geen hint door Ctrl+zweven voor de eerste Ctrl+B ($naam)")
        val getoond = gaNaarDefinitie(naam) { melding.isGetoond() }
        Thread.sleep(2_000)
        println("DORTUS-E2E [$naam] eerste Ctrl+B op NUM in calc.l: melding getoond $getoond, hints ${melding.aantalHints()}, cursor regel ${cursorRegel() + 1} (was ${regelL + 1})")
        scherm("$naam-pro-melding.png")
        assertEquals("calc.l", structuurBestand(), "structuurweergave hoort bij calc.l op pro-melding ($naam)")
        assertTrue(getoond, "Pro-melding getoond ($naam)")
        assertEquals(0, melding.aantalHints(), "geen hint bij de eerste klik ($naam)")
        assertEquals(regelL, cursorRegel(), "geen sprong vanuit calc.l ($naam)")

        ctrlZweven("$naam na balloon", melding, "return NUM", 8, regelL)
        println("DORTUS-E2E [$naam] na Ctrl+zweven na de balloon: hints ${melding.aantalHints()} (moet 0 blijven)")
        assertEquals(0, melding.aantalHints(), "geen hint door Ctrl+zweven na de balloon ($naam)")

        val hint = gaNaarDefinitie(naam) { melding.aantalHints() >= 1 }
        Thread.sleep(1_000)
        println("DORTUS-E2E [$naam] tweede Ctrl+B op NUM in calc.l: hint getoond $hint (hints ${melding.aantalHints()}), cursor regel ${cursorRegel() + 1}")
        scherm("$naam-pro-hint.png")
        assertTrue(hint, "korte Pro-hint getoond bij de tweede klik ($naam)")
        assertEquals(regelL, cursorRegel(), "geen sprong vanuit calc.l, tweede klik ($naam)")
        assertEquals("calc.l", structuurBestand(), "structuurweergave hoort bij calc.l op pro-hint ($naam)")
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
    internal fun Driver.cursorRegel(): Int {
        val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor() ?: return -1
        return withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) { editor.getCaretModel().getLogicalPosition().getLine() }
    }

    /** Regel (vanaf 0) waarop [tekst] begint in de open editor. */
    internal fun Driver.regelVan(tekst: String): Int {
        val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor() ?: return -1
        return withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
            val d = editor.getDocument()
            d.getText().substring(0, d.getText().indexOf(tekst)).count { it == '\n' }
        }
    }

    /** Cursor op [tekst] plus [extra] tekens in de open editor. */
    internal fun Driver.cursorOp(tekst: String, extra: Int) {
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
}
