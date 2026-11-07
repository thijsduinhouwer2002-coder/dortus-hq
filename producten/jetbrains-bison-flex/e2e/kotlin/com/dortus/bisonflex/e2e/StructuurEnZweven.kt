package com.dortus.bisonflex.e2e

import com.intellij.driver.client.Driver
import com.intellij.driver.client.Remote
import com.intellij.driver.client.service
import com.intellij.driver.client.utility
import com.intellij.driver.model.LockSemantics
import com.intellij.driver.model.OnDispatcher
import com.intellij.driver.sdk.Document
import com.intellij.driver.sdk.FileEditorManager
import com.intellij.driver.sdk.Project
import com.intellij.driver.sdk.singleProject
import org.junit.jupiter.api.Assertions.assertEquals
import java.awt.Point

/*
 * Hulpstukken voor IdeTest: nagaan bij welk bestand de structuurweergave hoort, en Ctrl+zweven met xdotool.
 *
 * Waarom de structuurweergave kan blijven hangen (StructureViewWrapperImpl van de IDE): hij kijkt alleen opnieuw welk
 * bestand hij moet tonen als de ActivityTracker van de IDE opliep (toets, muisklik, focus- of venstergebeurtenis, actie),
 * en dan neemt hij het bestand van het onderdeel met de focus. Staat de focus in de structuurweergave zelf, dan doet
 * hij niets. Wisselt de Driver alleen van tab, dan komt er niet altijd zo'n gebeurtenis en blijft calc.y staan.
 */

@Remote("com.intellij.ide.structureView.StructureViewFactoryEx")
interface StructuurFabriekOpAfstand {
    fun getInstanceEx(project: Project): StructuurFabriekOpAfstand
    fun getStructureViewWrapper(): StructuurWrapperOpAfstand?
}

@Remote("com.intellij.ide.impl.StructureViewWrapperImpl")
interface StructuurWrapperOpAfstand {
    fun getStructureView(): StructuurComponentOpAfstand?
}

@Remote("com.intellij.ide.structureView.newStructureView.StructureViewComponent")
interface StructuurComponentOpAfstand {
    fun getFileEditor(): BestandEditorOpAfstand?
}

@Remote("com.intellij.openapi.fileEditor.FileEditor")
interface BestandEditorOpAfstand {
    fun getFile(): BestandOpAfstand?
}

@Remote("com.intellij.openapi.vfs.VirtualFile")
interface BestandOpAfstand {
    fun getName(): String
}

@Remote("com.intellij.ide.ActivityTracker")
interface ActiviteitOpAfstand {
    fun getInstance(): ActiviteitOpAfstand
    fun inc()
}

@Remote("java.awt.Component")
interface OnderdeelOpAfstand {
    fun requestFocusInWindow(): Boolean
    fun getLocationOnScreen(): Point
}

@Remote("com.intellij.openapi.editor.Editor")
interface EditorMetOnderdeel {
    fun getDocument(): Document
    fun getContentComponent(): OnderdeelOpAfstand
    fun offsetToXY(offset: Int): Point
    fun getLineHeight(): Int
    fun getMarkupModel(): MarkeringenOpAfstand
}

@Remote("com.intellij.openapi.editor.markup.MarkupModel")
interface MarkeringenOpAfstand {
    fun getAllHighlighters(): Array<MarkeringOpAfstand>
}

@Remote("com.intellij.openapi.editor.markup.RangeHighlighter")
interface MarkeringOpAfstand {
    fun getLayer(): Int
    fun getStartOffset(): Int
    fun getEndOffset(): Int
}

/** `HighlighterLayer.HYPERLINK`: de laag van de navigatie-onderstreping bij Ctrl+zweven (CtrlMouseHandler2). */
private const val LAAG_ONDERSTREPING = 5900

/** Naam van het bestand dat de structuurweergave nu toont, of een korte foutomschrijving. */
fun Driver.structuurBestand(): String? = try {
    val wrapper = utility<StructuurFabriekOpAfstand>().getInstanceEx(singleProject()).getStructureViewWrapper()
    val view = wrapper?.let { cast(it, StructuurWrapperOpAfstand::class).getStructureView() }
    view?.let { v -> withContext(OnDispatcher.EDT) { cast(v, StructuurComponentOpAfstand::class).getFileEditor()?.getFile()?.getName() } }
} catch (e: Throwable) {
    "fout ${e.javaClass.simpleName}: ${e.message?.take(150)}"
}

/**
 * Zorgt dat de structuurweergave bij [bestand] hoort (het bestand in de open editor) en controleert dat.
 * Hangt hij nog aan een ander bestand: focus naar de open editor en de ActivityTracker ophogen, zoals een
 * gebruiker die in de editor klikt. Daarna hoogstens 10 seconden wachten.
 */
fun Driver.structuurBij(naam: String, bestand: String) {
    val voor = structuurBestand()
    println("DORTUS-E2E [$naam] structuur na wissel naar $bestand: $voor")
    if (voor != bestand) {
        val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor()
        withContext(OnDispatcher.EDT) {
            val gelukt = editor?.let { cast(it, EditorMetOnderdeel::class).getContentComponent().requestFocusInWindow() }
            println("DORTUS-E2E [$naam] focus naar editor gevraagd: $gelukt")
            utility<ActiviteitOpAfstand>().getInstance().inc()
        }
        var nu = structuurBestand()
        for (i in 1..10) {
            if (nu == bestand) break
            Thread.sleep(1_000)
            nu = structuurBestand()
        }
        println("DORTUS-E2E [$naam] structuur na focus: $nu")
    }
    assertEquals(bestand, structuurBestand(), "structuurweergave hoort bij $bestand ($naam)")
}

/**
 * Ctrl ingedrukt houden en met de muis over [tekst] plus [extra] tekens in de open editor bewegen (xdotool),
 * daarna de muis weg naar een leeg stuk editor. Eis (stand GEEN): geen nieuwe hint, geen balloon, geen sprong.
 * Terwijl Ctrl nog ingedrukt is, telt de stap de navigatie-onderstrepingen van de IDE (laag HYPERLINK in de
 * markeringen van de editor) en zet ze in het log: zo is te zien dat de IDE het zweven echt zag. Geeft dat aantal.
 */
fun Driver.ctrlZweven(naam: String, melding: ProMeldingOpAfstand, tekst: String, extra: Int, regelVoor: Int): Int {
    val getoondVoor = melding.isGetoond()
    val hintsVoor = melding.aantalHints()
    val editor = cast(service<FileEditorManager>(singleProject()).getSelectedTextEditor()!!, EditorMetOnderdeel::class)
    // Java rekent op factor 2 in punten van de halve maat (1440x900); xdotool in echte pixels (2880x1800).
    val (plek, leeg) = withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
        val offset = editor.getDocument().getText().indexOf(tekst) + extra
        val xy = editor.offsetToXY(offset)
        val o = editor.getContentComponent().getLocationOnScreen()
        Point((o.x + xy.x + 3) * 2, (o.y + xy.y + editor.getLineHeight() / 2) * 2) to Point((o.x + 300) * 2, (o.y + 600) * 2)
    }
    println("DORTUS-E2E [$naam] Ctrl+zweven op '$tekst' +$extra: muis naar ${plek.x},${plek.y} (pixels)")
    xdotool("mousemove", "${plek.x}", "${plek.y}")
    var onderstreping = listOf<String>()
    xdotool("keydown", "ctrl")
    try {
        for (dx in listOf(2, 4, 6)) {
            Thread.sleep(500)
            xdotool("mousemove", "${plek.x + dx}", "${plek.y}")
        }
        Thread.sleep(2_000)
        println("DORTUS-E2E [$naam] muis tijdens Ctrl: ${muisPlek()}")
        onderstreping = onderstrepingen(editor)
        Thread.sleep(1_000)
    } finally {
        xdotool("keyup", "ctrl")
    }
    println("DORTUS-E2E [$naam] navigatie-onderstreping van de IDE tijdens Ctrl+zweven: ${onderstreping.size} $onderstreping")
    xdotool("mousemove", "${leeg.x}", "${leeg.y}")
    Thread.sleep(1_000)
    val regelNa = withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) { cast(editor, com.intellij.driver.sdk.Editor::class).getCaretModel().getLogicalPosition().getLine() }
    println("DORTUS-E2E [$naam] na Ctrl+zweven: melding getoond ${melding.isGetoond()} (was $getoondVoor), hints ${melding.aantalHints()} (was $hintsVoor), cursor regel ${regelNa + 1} (was ${regelVoor + 1})")
    assertEquals(getoondVoor, melding.isGetoond(), "geen balloon door Ctrl+zweven ($naam)")
    assertEquals(hintsVoor, melding.aantalHints(), "geen hint door Ctrl+zweven ($naam)")
    assertEquals(regelVoor, regelNa, "geen sprong door Ctrl+zweven ($naam)")
    return onderstreping.size
}

/** De navigatie-onderstrepingen (laag HYPERLINK) in [editor], als "begin-eind: tekst", of een korte fout. */
private fun Driver.onderstrepingen(editor: EditorMetOnderdeel): List<String> = try {
    withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
        val tekst = editor.getDocument().getText()
        editor.getMarkupModel().getAllHighlighters().filter { it.getLayer() == LAAG_ONDERSTREPING }
            .map { "${it.getStartOffset()}-${it.getEndOffset()}: ${tekst.substring(it.getStartOffset(), it.getEndOffset())}" }
    }
} catch (e: Throwable) {
    listOf("fout ${e.javaClass.simpleName}: ${e.message?.take(150)}")
}

/** Waar de muis nu is volgens xdotool (echte pixels). */
private fun muisPlek(): String = try {
    val p = ProcessBuilder("xdotool", "getmouselocation").redirectErrorStream(true).start()
    p.inputStream.bufferedReader().readText().trim().also { p.waitFor() }
} catch (e: Exception) {
    "onbekend (${e.message})"
}

private fun xdotool(vararg args: String) {
    val code = ProcessBuilder(listOf("xdotool") + args).inheritIO().start().waitFor()
    if (code != 0) println("DORTUS-E2E xdotool ${args.joinToString(" ")}: code $code")
}
