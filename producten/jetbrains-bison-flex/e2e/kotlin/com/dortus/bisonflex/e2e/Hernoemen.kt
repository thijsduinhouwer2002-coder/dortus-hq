package com.dortus.bisonflex.e2e

import com.intellij.driver.client.Driver
import com.intellij.driver.client.Remote
import com.intellij.driver.client.service
import com.intellij.driver.client.utility
import com.intellij.driver.model.LockSemantics
import com.intellij.driver.model.OnDispatcher
import com.intellij.driver.sdk.FileEditorManager
import com.intellij.driver.sdk.Project
import com.intellij.driver.sdk.invokeAction
import com.intellij.driver.sdk.openFile
import com.intellij.driver.sdk.singleProject
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Assertions.assertTrue

/*
 * Het winkelproject heeft calc.y en calc.yy, calc.l en calc.ll in één map: NUM in calc.y raakt dus calc.l en calc.ll.
 * Hernoemen (Shift+F6) in de echte IDE, stand GEEN (Daan, beoordeling 8). Loopt na IdeTest.proMelding, dus de
 * ga-naar-balloon is dan al getoond. Schermen: hernoem-melding, hernoem-hint, hernoem-scanner, hernoem-structuur,
 * hernoem-venster en hernoem-conflict. Elke stap zet in het log welke melding er kwam, hoeveel hints, en of er
 * een vreemde editor-hint stond (een IDE-fout zoals "Cannot perform refactoring" is ook een editor-hint).
 */

@Remote("com.intellij.codeInsight.hint.HintManager")
interface HintBeheerOpAfstand {
    fun getInstance(): HintBeheerOpAfstand
    fun hasShownHintsThatWillHideByOtherHint(onlyFocused: Boolean): Boolean
}

@Remote("com.intellij.openapi.wm.WindowManager")
interface VensterBeheerOpAfstand {
    fun getInstance(): VensterBeheerOpAfstand
    fun getStatusBar(project: Project): StatusBalkOpAfstand?
}

@Remote("com.intellij.openapi.wm.StatusBar")
interface StatusBalkOpAfstand {
    fun getInfo(): String?
}

private const val HERNOEMEN = "hernoemen"

/** Of er nu een editor-hint in beeld is (onze hint of een fout van de IDE), of een korte fout. */
private fun Driver.hintInBeeld(): String = try {
    withContext(OnDispatcher.EDT) { utility<HintBeheerOpAfstand>().getInstance().hasShownHintsThatWillHideByOtherHint(false) }.toString()
} catch (e: Throwable) {
    "onbekend (${e.javaClass.simpleName})"
}

private fun Driver.statusBalk(): String? = try {
    withContext(OnDispatcher.EDT) { utility<VensterBeheerOpAfstand>().getInstance().getStatusBar(singleProject())?.getInfo() }
} catch (e: Throwable) {
    "fout ${e.javaClass.simpleName}: ${e.message?.take(150)}"
}

private fun Driver.tekstEditor(): String = service<FileEditorManager>(singleProject()).getSelectedTextEditor()?.let { e ->
    withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) { e.getDocument().getText() }
} ?: ""

/**
 * Shift+F6 via de Driver (zonder te wachten, want het hernoemvenster is modaal); is [klaar] na 8 s niet waar,
 * dan nog eens met Shift+F6 via xdotool. Geeft of [klaar] waar werd.
 */
private fun IdeTest.shiftF6(d: Driver, naam: String, klaar: () -> Boolean): Boolean {
    try { d.invokeAction("RenameElement", now = false) } catch (e: Throwable) {
        println("DORTUS-E2E [$naam] RenameElement via Driver mislukt: ${e.javaClass.simpleName}: ${e.message?.take(200)}")
    }
    if (wacht(8) { klaar() }) return true
    println("DORTUS-E2E [$naam] na RenameElement (Driver) nog niet klaar, nu Shift+F6 (xdotool)")
    toets("shift+F6")
    return wacht(10) { klaar() }
}

/** Eén geblokkeerde Shift+F6 in de editor; logt wat er te zien is en geeft of er een nieuwe hint of balloon kwam. */
private fun IdeTest.geblokkeerd(d: Driver, naam: String, wat: String, melding: ProMeldingOpAfstand, scherm: String) = with(d) {
    val hintsVoor = melding.aantalHints()
    val balloonVoor = melding.isGetoondVoor(HERNOEMEN)
    val tekstVoor = tekstEditor()
    val gelukt = shiftF6(d, naam) { melding.aantalHints() > hintsVoor || (!balloonVoor && melding.isGetoondVoor(HERNOEMEN)) }
    Thread.sleep(1_500)
    val nieuweHint = melding.aantalHints() > hintsVoor
    val balloon = !balloonVoor && melding.isGetoondVoor(HERNOEMEN)
    val hint = hintInBeeld()
    // Een hint in beeld zonder dat wij er een toonden, is een hint van de IDE zelf: een foutmelding.
    val fout = hint == "true" && !nieuweHint
    println("DORTUS-E2E [$naam] $wat: balloon nu $balloon (tekst '${if (balloon) melding.laatsteMelding() else "-"}'), " +
        "hints ${melding.aantalHints()} (was $hintsVoor), laatste hint '${melding.laatsteHint()}', editor-hint in beeld $hint, foutmelding IDE $fout")
    scherm("$naam-$scherm.png")
    assertTrue(gelukt, "melding of hint bij $wat ($naam)")
    assertTrue(!fout, "geen foutmelding van de IDE bij $wat ($naam)")
    assertEquals(tekstVoor, tekstEditor(), "niets hernoemd bij $wat ($naam)")
    balloon
}

/** De schermen en controles voor hernoemen; zie het commentaar bovenaan. */
internal fun IdeTest.hernoemen(d: Driver, naam: String) = with(d) {
    val melding = service<ProMeldingOpAfstand>()
    println("DORTUS-E2E [$naam] hernoemen begint: ga-naar-balloon al getoond ${melding.isGetoondVoor("ga-naar")}, hernoem-balloon ${melding.isGetoondVoor(HERNOEMEN)}, hints ${melding.aantalHints()}")

    // 1. Shift+F6 op NUM in calc.y, na de ga-naar-balloon: toch de balloon over hernoemen (eigen vlag).
    openFile("calc.y")
    pauze()
    structuurBij(naam, "calc.y")
    cursorOp("%token NUM", 8)
    val balloon = geblokkeerd(d, naam, "eerste Shift+F6 op NUM in calc.y", melding, "hernoem-melding")
    assertTrue(balloon, "balloon over hernoemen na de ga-naar-balloon ($naam)")
    assertEquals("Renaming NUM also changes calc.l and calc.ll. Rename across grammar and scanner is a Pro feature. Try it free for 30 days.", melding.laatsteMelding())

    // 2. Nog eens: de hint zegt waarom er niets gebeurde.
    geblokkeerd(d, naam, "tweede Shift+F6 op NUM in calc.y", melding, "hernoem-hint")
    assertEquals("NUM is also used in calc.l and calc.ll. Rename across grammar and scanner is a Pro feature.", melding.laatsteHint())

    // 3. Shift+F6 op NUM in return NUM; van calc.l: dezelfde hint, geen "Cannot perform refactoring".
    openFile("calc.l")
    pauze()
    structuurBij(naam, "calc.l")
    cursorOp("return NUM", 8)
    geblokkeerd(d, naam, "Shift+F6 op NUM in calc.l", melding, "hernoem-scanner")
    assertEquals("NUM is also used in calc.y and calc.yy. Rename across grammar and scanner is a Pro feature.", melding.laatsteHint())

    // 4. Vanuit de structuurweergave (geen editor): de hint in de statusbalk.
    openFile("calc.y")
    pauze()
    structuurBij(naam, "calc.y")
    val zonderVoor = melding.aantalHintsZonderEditor()
    try { invokeAction("ActivateStructureToolWindow") } catch (e: Throwable) {
        println("DORTUS-E2E [$naam] ActivateStructureToolWindow mislukt: ${e.javaClass.simpleName}: ${e.message?.take(200)}")
    }
    Thread.sleep(1_500)
    typ("NUM")
    Thread.sleep(1_000)
    toets("shift+F6")
    val structuur = wacht(10) { melding.aantalHintsZonderEditor() > zonderVoor }
    Thread.sleep(1_000)
    println("DORTUS-E2E [$naam] Shift+F6 op NUM in de structuurweergave: hint zonder editor $structuur (aantal ${melding.aantalHintsZonderEditor()}), " +
        "laatste hint '${melding.laatsteHint()}', statusbalk '${statusBalk()}'")
    scherm("$naam-hernoem-structuur.png")
    toets("Escape")
    assertTrue(structuur, "hint in de statusbalk bij hernoemen vanuit de structuurweergave ($naam)")

    // 5. Een regel die alleen in calc.y staat: het hernoemvenster, en het conflictvenster bij een bestaande naam.
    hernoemvenster(d, naam, melding)
}

/** Shift+F6 op `exp:`: het venster opent zonder melding; "line" invullen geeft het conflictvenster. Daarna sluiten. */
private fun IdeTest.hernoemvenster(d: Driver, naam: String, melding: ProMeldingOpAfstand) = with(d) {
    openFile("calc.y")
    pauze()
    cursorOp("\nexp:", 2)
    val tekstVoor = tekstEditor()
    val hintsVoor = melding.aantalHints()
    val ide = actiefVenster()
    var venster: String? = null
    var conflict: String? = null
    try {
        shiftF6(d, naam) { actiefVenster().let { it != null && it != ide }.also { if (it) venster = actiefVenster() } }
        println("DORTUS-E2E [$naam] Shift+F6 op exp in calc.y: hernoemvenster ${venster ?: "niet gezien"}, hints ${melding.aantalHints()} (was $hintsVoor), laatste melding '${melding.laatsteMelding()}'")
        if (venster == null) return@with
        Thread.sleep(2_000)
        scherm("$naam-hernoem-venster.png")
        toets("ctrl+a")
        typ("line")
        Thread.sleep(500)
        toets("Return")
        wacht(20) { actiefVenster().let { it != null && it != ide && it != venster }.also { if (it) conflict = actiefVenster() } }
        Thread.sleep(2_000)
        println("DORTUS-E2E [$naam] naam 'line' ingevuld: conflictvenster ${conflict ?: "niet gezien"}")
        if (conflict != null) scherm("$naam-hernoem-conflict.png")
    } finally {
        // Alles dicht tot de IDE weer actief is (Escape is Cancel in beide vensters).
        for (i in 1..4) {
            if (actiefVenster() == ide) break
            toets("Escape")
            Thread.sleep(1_500)
        }
        println("DORTUS-E2E [$naam] na sluiten: IDE weer actief ${actiefVenster() == ide}, calc.y ongewijzigd ${tekstEditor() == tekstVoor}")
    }
    assertTrue(venster != null, "hernoemvenster bij exp ($naam)")
    assertEquals(hintsVoor, melding.aantalHints(), "geen Pro-hint bij een regel die alleen in calc.y staat ($naam)")
    assertTrue(conflict != null, "conflictvenster bij de bestaande naam line ($naam)")
    assertEquals(tekstVoor, tekstEditor(), "calc.y ongewijzigd na annuleren ($naam)")
}
