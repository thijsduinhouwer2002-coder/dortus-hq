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
import com.intellij.driver.sdk.closeToolWindow
import com.intellij.driver.sdk.invokeAction
import com.intellij.driver.sdk.openFile
import com.intellij.driver.sdk.singleProject
import org.junit.jupiter.api.Assertions.assertTrue
import java.awt.Point
import java.awt.Rectangle
import java.nio.file.Files
import java.nio.file.Path

/*
 * Schermen voor winkelplaatje 4 en 5 (ontwerp.md, beoordeling 12, "Voor Jet, schermen voor plaatje 4 en 5").
 * Alleen in het lichte thema, als laatste stap na de kleurenpagina, zodat alle bestaande schermen en controles
 * gelijk blijven. Stand GELDIG via MeldingenDiagnose (zoals Meldingen.kt).
 * A. Hernoemen met Pro: Shift+F6 op NUM in `return NUM;` van calc.l, NUMBER, Enter; calc.l links en calc.y rechts
 *    (editor verticaal gesplitst, panelen dicht): `winkel-hernoemd.png`. Daarna terug naar NUM.
 * B. Melding met snelle oplossing hoger in calc.y: het Alt+Enter-menu (`winkel-melding-menu.png`, heel scherm,
 *    want het menu is een eigen venster) en de zweeftekst op UNDEFINED (`winkel-melding-zweef.png`).
 * C. Alt+F7 op NUM met Pro: het Find-paneel (`winkel-alleplekken.png`), de reserve als splitsen niet lukt.
 * Elke stap zet in het log wat er te zien is (regels in beeld, meldingen, vensters).
 */

@Remote("com.intellij.openapi.fileEditor.FileEditorManager")
interface AlleEditorsOpAfstand {
    fun getInstance(project: Project): AlleEditorsOpAfstand
    fun getAllEditors(): Array<BestandEditorOpAfstand>
}

@Remote("com.intellij.openapi.fileEditor.TextEditor")
interface TekstEditorOpAfstand {
    fun getEditor(): EditorInBeeld
}

@Remote("com.intellij.openapi.editor.Editor")
interface EditorInBeeld {
    fun getDocument(): Document
    fun getContentComponent(): ZichtbaarOnderdeel
    fun getScrollingModel(): ScrollOpAfstand
    fun offsetToXY(offset: Int): Point
    fun getLineHeight(): Int
}

@Remote("java.awt.Component")
interface ZichtbaarOnderdeel {
    fun isShowing(): Boolean
    fun getLocationOnScreen(): Point
    fun requestFocusInWindow(): Boolean
}

@Remote("com.intellij.openapi.editor.ScrollingModel")
interface ScrollOpAfstand {
    fun getVisibleArea(): Rectangle
}

private const val NA_INPUT = "  | input line\n  ;\n"
private const val NA_INPUT_MET_FOUT = "  | input line\n  ;\n\nunused:\n    UNDEFINED\n  ;\n"

/** De drie winkelstappen; fouten worden pas aan het eind gegooid, zodat een mislukte stap de andere niet tegenhoudt. */
internal fun IdeTest.winkelschermen(d: Driver, naam: String) = with(d) {
    val diagnose = service<MeldingenDiagnoseOpAfstand>()
    zorgDatIdeActiefIs(naam)
    diagnose.zetStand("GELDIG")
    println("DORTUS-E2E [$naam] winkel: stand op GELDIG gezet")
    val fouten = mutableListOf<Throwable>()
    for ((stap, werk) in listOf<Pair<String, () -> Unit>>(
        "A hernoemen" to { winkelHernoemen(d, naam, diagnose) },
        "B melding" to { winkelMelding(d, naam, diagnose) },
        "C alle plekken" to { winkelAllePlekken(d, naam) },
    )) {
        try { werk() } catch (e: Throwable) {
            println("DORTUS-E2E [$naam] winkel stap $stap mislukt: ${e.javaClass.simpleName}: ${e.message?.take(300)}")
            fouten += e
        }
    }
    // De andere bestanden die het hernoemen raakte (calc.ll, calc.yy) ook terug naar NUM.
    for (b in listOf("calc.ll", "calc.yy", "calc.l", "calc.y")) {
        openFile(b)
        Thread.sleep(1_000)
        val n = herstel(diagnose)
        println("DORTUS-E2E [$naam] winkel: $b terug naar NUM ($n keer vervangen), NUMBER nog ${"NUMBER" in tekstOpen()}")
    }
    diagnose.zetStand("GEEN")
    fouten.firstOrNull()?.let { throw it }
}

/** Na de kleurenpagina: staat er nog een dialoog (Settings) vooraan, dan Escape tot de IDE vooraan staat. */
private fun IdeTest.zorgDatIdeActiefIs(naam: String) {
    for (i in 1..4) {
        val v = actiefVenster()
        val titel = vensterNaam(v)
        println("DORTUS-E2E [$naam] winkel: actief venster $v '$titel'")
        if (!titel.contains("Settings") && !titel.contains("Preferences")) return
        toets("Escape")
        Thread.sleep(1_500)
    }
}

private fun IdeTest.winkelHernoemen(d: Driver, naam: String, diagnose: MeldingenDiagnoseOpAfstand) = with(d) {
    openFile("calc.l")
    pauze()
    editorFocus()
    cursorOp("return NUM", 8)
    val ide = actiefVenster()
    var venster: String? = null
    try { invokeAction("RenameElement", now = false) } catch (e: Throwable) {
        println("DORTUS-E2E [$naam] winkel: RenameElement via Driver mislukt: ${e.javaClass.simpleName}: ${e.message?.take(200)}")
    }
    val nieuwVenster = { actiefVenster().let { it != null && it != ide }.also { if (it) venster = actiefVenster() } }
    if (!wacht(8, nieuwVenster)) {
        println("DORTUS-E2E [$naam] winkel: geen hernoemvenster na RenameElement, nu Shift+F6 (xdotool)")
        toets("shift+F6")
        wacht(10, nieuwVenster)
    }
    println("DORTUS-E2E [$naam] winkel: hernoemvenster ${venster ?: "niet gezien"} '${vensterNaam(venster)}'")
    assertTrue(venster != null, "hernoemvenster bij Shift+F6 op NUM in calc.l met Pro ($naam)")
    Thread.sleep(1_500)
    toets("ctrl+a")
    typ("NUMBER")
    Thread.sleep(500)
    toets("Return")
    val terug = wacht(20) { actiefVenster() == ide }
    if (!terug) {
        // Nog een venster (bijvoorbeeld een vraag of conflict): vastleggen en sluiten, dan staat het in log en scherm.
        val v = actiefVenster()
        println("DORTUS-E2E [$naam] winkel: na Enter nog een venster $v '${vensterNaam(v)}'")
        schermHeel("winkel-hernoem-extra.png")
        for (i in 1..3) { if (actiefVenster() == ide) break; toets("Escape"); Thread.sleep(1_500) }
    }
    Thread.sleep(2_000)
    val tekstL = tekstOpen()
    println("DORTUS-E2E [$naam] winkel: calc.l na hernoemen: ${tekstL.lines().filter { "NUM" in it }.map { it.trim() }}")
    assertTrue("return NUMBER;" in tekstL, "return NUMBER; in calc.l na hernoemen met Pro ($naam)")

    // calc.l links, calc.y rechts.
    var gesplitst = false
    try {
        invokeAction("SplitVertically")
        Thread.sleep(1_500)
        openFile("calc.y")
        Thread.sleep(1_500)
        for (paneel in listOf("Structure", "Project")) {
            try { closeToolWindow(paneel) } catch (e: Throwable) { println("DORTUS-E2E [$naam] winkel: $paneel sluiten: ${e.javaClass.simpleName}") }
        }
        cursorOp("%token NUMBER", 13)
        pauze()
        val beeld = regelsInBeeld()
        beeld.forEach { println("DORTUS-E2E [$naam] winkel in beeld: $it") }
        val l = beeld.firstOrNull { it.startsWith("calc.l ") && "return NUMBER;" in it }
        val y = beeld.firstOrNull { it.startsWith("calc.y ") && "'%token NUMBER'" in it && "'NUMBER'" in it }
        gesplitst = l != null && y != null && xVan(l) < xVan(y)
        println("DORTUS-E2E [$naam] winkel: calc.l links en calc.y rechts met de drie regels in beeld: $gesplitst")
        scherm("winkel-hernoemd.png")
    } catch (e: Throwable) {
        println("DORTUS-E2E [$naam] winkel: splitsen mislukt: ${e.javaClass.simpleName}: ${e.message?.take(300)}")
    } finally {
        try { invokeAction("UnsplitAll") } catch (e: Throwable) { println("DORTUS-E2E [$naam] winkel: UnsplitAll: ${e.javaClass.simpleName}") }
        Thread.sleep(1_000)
        for (b in listOf("calc.l", "calc.y")) {
            openFile(b)
            Thread.sleep(1_000)
            println("DORTUS-E2E [$naam] winkel: $b terug naar NUM (${herstel(diagnose)} keer vervangen)")
        }
    }
    assertTrue(gesplitst, "calc.l links en calc.y rechts met return NUMBER;, %token NUMBER en NUMBER in beeld ($naam)")
}

private fun IdeTest.winkelMelding(d: Driver, naam: String, diagnose: MeldingenDiagnoseOpAfstand) = with(d) {
    openFile("calc.y")
    pauze()
    editorFocus()
    assertTrue(diagnose.vervang(NA_INPUT, NA_INPUT_MET_FOUT), "fout hoger in calc.y gezet ($naam)")
    var gezien = ""
    val beide = wacht(40) {
        gezien = diagnose.meldingen()
        "Unused rule 'unused'" in gezien && "Undefined symbol 'UNDEFINED'" in gezien
    }
    println("DORTUS-E2E [$naam] winkel: meldingen hoger in calc.y: '$gezien'")
    try {
        assertTrue(beide, "beide meldingen hoger in calc.y ($naam), gezien '$gezien'")
        assertTrue(diagnose.cursorOp("\nunused:", 2), "cursor op unused ($naam)")
        pauze()
        regelsInBeeld().forEach { println("DORTUS-E2E [$naam] winkel in beeld (melding): $it") }
        toets("alt+Return")
        Thread.sleep(3_000)
        println("DORTUS-E2E [$naam] winkel: na Alt+Enter actief venster '${vensterNaam(actiefVenster())}'")
        schermHeel("winkel-melding-menu.png")
        toets("Escape")
        Thread.sleep(1_000)

        // Muis op UNDEFINED; Java rekent in punten (1440x900), xdotool in pixels (2880x1800).
        val editor = cast(service<FileEditorManager>(singleProject()).getSelectedTextEditor()!!, EditorMetOnderdeel::class)
        val plek = withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
            val offset = editor.getDocument().getText().indexOf("    UNDEFINED") + 8
            val xy = editor.offsetToXY(offset)
            val o = editor.getContentComponent().getLocationOnScreen()
            Point((o.x + xy.x) * 2, (o.y + xy.y + editor.getLineHeight() / 2) * 2)
        }
        println("DORTUS-E2E [$naam] winkel: muis naar UNDEFINED op ${plek.x},${plek.y} (pixels)")
        for (dx in listOf(0, 2, 4, 6)) {
            ProcessBuilder("xdotool", "mousemove", "${plek.x + dx}", "${plek.y}").inheritIO().start().waitFor()
            Thread.sleep(400)
        }
        Thread.sleep(3_500)
        println("DORTUS-E2E [$naam] winkel: zweven op UNDEFINED, actief venster '${vensterNaam(actiefVenster())}', meldingen '${diagnose.meldingen()}'")
        schermHeel("winkel-melding-zweef.png")
        ProcessBuilder("xdotool", "mousemove", "${plek.x + 600}", "${plek.y + 900}").inheritIO().start().waitFor()
        Thread.sleep(1_000)
    } finally {
        toets("Escape")
        val terug = diagnose.vervang(NA_INPUT_MET_FOUT, NA_INPUT)
        val schoon = wacht(20) { diagnose.meldingen().isEmpty() }
        println("DORTUS-E2E [$naam] winkel: calc.y teruggezet $terug, meldingen weg $schoon")
    }
}

private fun IdeTest.winkelAllePlekken(d: Driver, naam: String) = with(d) {
    openFile("calc.l")
    pauze()
    editorFocus()
    cursorOp("return NUM", 8)
    val ide = actiefVenster()
    try {
        invokeAction("FindUsages", now = false)
        Thread.sleep(6_000)
        val v = actiefVenster()
        println("DORTUS-E2E [$naam] winkel: na Alt+F7 actief venster $v '${vensterNaam(v)}' (IDE $ide)")
        schermHeel("winkel-alleplekken.png")
    } finally {
        for (i in 1..3) { if (actiefVenster() == ide) break; toets("Escape"); Thread.sleep(1_000) }
        try { closeToolWindow("Find") } catch (e: Throwable) { println("DORTUS-E2E [$naam] winkel: Find sluiten: ${e.javaClass.simpleName}") }
    }
}

/** Per editor die nu getoond wordt: "bestand x=..: r9 '%token NUMBER'; ..." met alle regels met NUM die in beeld staan. */
private fun Driver.regelsInBeeld(): List<String> = try {
    val beheer = utility<AlleEditorsOpAfstand>().getInstance(singleProject())
    withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
        beheer.getAllEditors().mapNotNull { fe ->
            val bestand = fe.getFile()?.getName() ?: return@mapNotNull null
            val e = try { cast(fe, TekstEditorOpAfstand::class).getEditor() } catch (t: Throwable) { return@mapNotNull "$bestand: geen teksteditor" }
            val c = e.getContentComponent()
            if (!c.isShowing()) return@mapNotNull "$bestand niet getoond"
            val zicht = e.getScrollingModel().getVisibleArea()
            val hoogte = e.getLineHeight()
            var start = 0
            val regels = mutableListOf<String>()
            e.getDocument().getText().split('\n').forEachIndexed { i, r ->
                if ("NUM" in r || "UNDEFINED" in r || "unused" in r) {
                    val y = e.offsetToXY(start).y
                    if (y >= zicht.y && y + hoogte <= zicht.y + zicht.height) regels += "r${i + 1} '${r.trim()}'"
                }
                start += r.length + 1
            }
            "$bestand x=${c.getLocationOnScreen().x}: ${regels.joinToString("; ")}"
        }
    }
} catch (t: Throwable) {
    listOf("regels in beeld niet te lezen: ${t.javaClass.simpleName}: ${t.message?.take(200)}")
}

private fun xVan(regel: String): Int = Regex("x=(-?\\d+)").find(regel)?.groupValues?.get(1)?.toInt() ?: Int.MAX_VALUE

private fun Driver.tekstOpen(): String = service<FileEditorManager>(singleProject()).getSelectedTextEditor()?.let { e ->
    withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) { e.getDocument().getText() }
} ?: ""

/** Focus naar de open editor, zoals een klik erin (Shift+F6 en Alt+Enter gaan naar het onderdeel met de focus). */
private fun Driver.editorFocus() {
    val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor() ?: return
    withContext(OnDispatcher.EDT) { cast(editor, EditorMetOnderdeel::class).getContentComponent().requestFocusInWindow() }
    Thread.sleep(500)
}

/** Alle NUMBER in de open editor terug naar NUM; geeft het aantal. */
private fun herstel(diagnose: MeldingenDiagnoseOpAfstand): Int {
    var n = 0
    while (n < 10 && diagnose.vervang("NUMBER", "NUM")) n++
    return n
}

private fun vensterNaam(id: String?): String = if (id == null) "" else try {
    val p = ProcessBuilder("xdotool", "getwindowname", id).redirectErrorStream(true).start()
    p.inputStream.bufferedReader().readText().trim().also { p.waitFor() }
} catch (e: Exception) {
    "onbekend"
}

/** Het hele scherm (root): een popup of menu is een eigen venster en valt buiten `import -window <IDE>`. */
private fun schermHeel(bestand: String) {
    val doel = Path.of(System.getProperty("dortus.e2e.screenshots")).resolve(bestand)
    val code = ProcessBuilder("import", "-window", "root", doel.toString()).inheritIO().start().waitFor()
    val grootte = if (Files.exists(doel)) Files.size(doel) else 0
    println("DORTUS-E2E schermafbeelding $bestand (heel scherm): code $code, $grootte bytes")
    assertTrue(code == 0 && grootte > 10_000, "schermafbeelding $bestand ($grootte bytes)")
}
