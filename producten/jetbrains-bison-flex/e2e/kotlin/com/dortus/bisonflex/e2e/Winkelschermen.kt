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
 * A. Hernoemen met Pro: Shift+F6 op `%token NUM` in calc.y, NUMBER, Enter; calc.l links en calc.y rechts
 *    (editor verticaal gesplitst, panelen dicht): `winkel-hernoemd.png`. Daarna terug naar NUM. Niet meer vanuit
 *    calc.l: daar komt eerst de keuzelijst (calc.y en calc.yy) en Enter daarin startte geen venster maar
 *    (vermoedelijk) hernoemen in de editor zelf; de controle las daarna een lege tekst (run 42458935689).
 * B. Melding met snelle oplossing hoger in calc.y (regel `term`, Daan beoordeling 13): het Alt+Enter-menu
 *    (`winkel-melding-menu.png`, heel scherm, want het menu is een eigen venster), de zweeftekst op UNDEFINED
 *    (`winkel-melding-zweef.png`) en na Enter op de snelle oplossing dezelfde regels zonder `term`
 *    (`winkel-melding-na.png`).
 * C. Alt+F7 op NUM met Pro: Enter op de eerste regel van het kiesmenu, wachten op het Find-paneel
 *    (`winkel-alleplekken.png`), de reserve als splitsen niet lukt. Het log noemt welke regel Enter koos en
 *    welk tabblad het Find-paneel toont (Kiesmenu.kt). Structuurpaneel dicht op alle winkelschermen.
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

@Remote("com.intellij.openapi.wm.ToolWindowManager")
interface PanelenOpAfstand {
    fun getInstance(project: Project): PanelenOpAfstand
    fun getToolWindow(id: String): PaneelOpAfstand?
}

@Remote("com.intellij.openapi.wm.ToolWindow")
interface PaneelOpAfstand {
    fun isVisible(): Boolean
    fun getContentManager(): InhoudBeheerOpAfstand
}

private const val NA_INPUT = "  | input line\n  ;\n"
/** `term` bestaat niet in calc.y (gecontroleerd): een echte naam in plaats van `unused` (Daan, beoordeling 13). */
private const val NA_INPUT_MET_FOUT = "  | input line\n  ;\n\nterm:\n    UNDEFINED\n  ;\n"

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
        val n = herstel(diagnose, "$naam $b")
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
    sluitPanelen(naam)
    openFile("calc.y")
    pauze()
    editorFocus()
    cursorOp("%token NUM", 8)
    val ide = actiefVenster()
    var venster: String? = null
    try { invokeAction("RenameElement", now = false) } catch (e: Throwable) {
        println("DORTUS-E2E [$naam] winkel: RenameElement via Driver mislukt: ${e.javaClass.simpleName}: ${e.message?.take(200)}")
    }
    val nieuwVenster = { actiefVenster().let { it != null && it != ide }.also { if (it) venster = actiefVenster() } }
    if (!wacht(10, nieuwVenster)) {
        println("DORTUS-E2E [$naam] winkel: geen hernoemvenster na Shift+F6 op %token NUM in calc.y")
        schermHeel("winkel-hernoem-keuze.png")
    }
    println("DORTUS-E2E [$naam] winkel: hernoemvenster ${venster ?: "niet gezien"} '${vensterNaam(venster)}'")
    assertTrue(venster != null, "hernoemvenster bij Shift+F6 op %token NUM in calc.y met Pro ($naam)")
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
    // Alle vier bestanden in het log: een echte productfout (calc.l niet bijgewerkt) moet hier zichtbaar zijn.
    for (b in listOf("calc.ll", "calc.yy", "calc.y")) {
        openFile(b)
        Thread.sleep(1_000)
        val t = tekstOpen()
        println("DORTUS-E2E [$naam] winkel: $b na hernoemen (${t.length} tekens): ${t.lines().filter { "NUM" in it }.map { it.trim() }}")
    }
    openFile("calc.l")
    Thread.sleep(1_000)
    val tekstL = tekstOpen()
    println("DORTUS-E2E [$naam] winkel: calc.l na hernoemen (${tekstL.length} tekens): ${tekstL.lines().filter { "NUM" in it }.map { it.trim() }}")
    assertTrue("return NUMBER;" in tekstL, "return NUMBER; in calc.l na hernoemen met Pro ($naam)")

    // calc.l en calc.y naast elkaar (welke links staat maakt voor Daan niet uit, beoordeling 13).
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
        gesplitst = l != null && y != null && xVan(l) != xVan(y)
        println("DORTUS-E2E [$naam] winkel: calc.l en calc.y naast elkaar met de drie regels in beeld: $gesplitst (calc.l x=${l?.let { xVan(it) }}, calc.y x=${y?.let { xVan(it) }})")
        scherm("winkel-hernoemd.png")
    } catch (e: Throwable) {
        println("DORTUS-E2E [$naam] winkel: splitsen mislukt: ${e.javaClass.simpleName}: ${e.message?.take(300)}")
    } finally {
        try { invokeAction("UnsplitAll") } catch (e: Throwable) { println("DORTUS-E2E [$naam] winkel: UnsplitAll: ${e.javaClass.simpleName}") }
        Thread.sleep(1_000)
        for (b in listOf("calc.l", "calc.ll", "calc.y")) {
            openFile(b)
            Thread.sleep(1_000)
            println("DORTUS-E2E [$naam] winkel: $b terug naar NUM (${herstel(diagnose, "$naam $b")} keer vervangen)")
        }
    }
    assertTrue(gesplitst, "calc.l en calc.y naast elkaar met return NUMBER;, %token NUMBER en NUMBER in beeld ($naam)")
}

private fun IdeTest.winkelMelding(d: Driver, naam: String, diagnose: MeldingenDiagnoseOpAfstand) = with(d) {
    sluitPanelen(naam)
    openFile("calc.y")
    pauze()
    editorFocus()
    assertTrue(diagnose.vervang(NA_INPUT, NA_INPUT_MET_FOUT), "fout hoger in calc.y gezet ($naam)")
    var gezien = ""
    val beide = wacht(40) {
        gezien = diagnose.meldingen()
        "Unused rule 'term'" in gezien && "Undefined symbol 'UNDEFINED'" in gezien
    }
    println("DORTUS-E2E [$naam] winkel: meldingen hoger in calc.y: '$gezien'")
    try {
        assertTrue(beide, "beide meldingen hoger in calc.y ($naam), gezien '$gezien'")
        assertTrue(diagnose.cursorOp("\nterm:", 2), "cursor op term ($naam)")
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

        // Plaatje 5 versie 2, het na-vlak: Alt+Enter, Enter op de eerste oplossing, dezelfde regels zonder term.
        toets("Escape")
        assertTrue(diagnose.cursorOp("\nterm:", 2), "cursor weer op term ($naam)")
        toets("alt+Return")
        Thread.sleep(3_000)
        toets("Return")
        val weg = wacht(15) { "\nterm:" !in tekstOpen() }
        Thread.sleep(2_000)
        println("DORTUS-E2E [$naam] winkel: na Enter op de snelle oplossing regel term weg $weg, meldingen '${diagnose.meldingen()}'")
        regelsInBeeld().forEach { println("DORTUS-E2E [$naam] winkel in beeld (na): $it") }
        schermHeel("winkel-melding-na.png")
        assertTrue(weg, "regel term weg na Enter op de snelle oplossing ($naam)")
    } finally {
        toets("Escape")
        // Na de snelle oplossing is de regel al weg; dan staat er (bijna) weer het origineel.
        val terug = diagnose.vervang(NA_INPUT_MET_FOUT, NA_INPUT) || "\nterm:" !in tekstOpen()
        val schoon = wacht(20) { diagnose.meldingen().isEmpty() }
        println("DORTUS-E2E [$naam] winkel: calc.y teruggezet $terug, meldingen weg $schoon")
    }
}

private fun IdeTest.winkelAllePlekken(d: Driver, naam: String) = with(d) {
    sluitPanelen(naam)
    openFile("calc.l")
    pauze()
    editorFocus()
    cursorOp("return NUM", 8)
    val ide = actiefVenster()
    try {
        invokeAction("FindUsages", now = false)
        Thread.sleep(4_000)
        // Keuzelijst "Find Usages Of" (calc.y en calc.yy, run 42457782755): Enter kiest de eerste, dan het Find-paneel.
        println("DORTUS-E2E [$naam] winkel: kiesmenu voor Enter: ${kiesmenuKeuze()}")
        toets("Return")
        val open = wacht(20) { paneelOpen("Find") }
        Thread.sleep(2_000)
        val v = actiefVenster()
        println("DORTUS-E2E [$naam] winkel: na Alt+F7 en Enter Find-paneel open $open, actief venster $v '${vensterNaam(v)}' (IDE $ide)")
        println("DORTUS-E2E [$naam] winkel: Find-paneel toont ${findTabblad()}")
        schermHeel("winkel-alleplekken.png")
        assertTrue(open, "Find-paneel open na Alt+F7 en Enter op de eerste regel ($naam)")
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
                if ("NUM" in r || "UNDEFINED" in r || "term" in r) {
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

/** Of het paneel [id] (Find, Structure) nu open is; false als het niet te lezen is. */
private fun Driver.paneelOpen(id: String): Boolean = try {
    val panelen = utility<PanelenOpAfstand>().getInstance(singleProject())
    withContext(OnDispatcher.EDT) { panelen.getToolWindow(id)?.isVisible() ?: false }
} catch (t: Throwable) {
    false
}

/** Structuur- en projectpaneel dicht: op de winkelschermen hoort alleen code (Daan, beoordeling 13). */
private fun Driver.sluitPanelen(naam: String) {
    for (paneel in listOf("Structure", "Project")) {
        try { closeToolWindow(paneel) } catch (e: Throwable) { println("DORTUS-E2E [$naam] winkel: $paneel sluiten: ${e.javaClass.simpleName}") }
    }
    println("DORTUS-E2E [$naam] winkel: structuurpaneel open ${paneelOpen("Structure")}")
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

/**
 * Alle NUMBER in de open editor terug naar NUM; geeft het aantal. Stopt vanzelf (NUM bevat geen NUMBER);
 * de grens van 100 is alleen een vangnet en wordt in het log gemeld als hij geraakt wordt.
 */
private fun herstel(diagnose: MeldingenDiagnoseOpAfstand, waar: String): Int {
    var n = 0
    while (n < HERSTEL_GRENS && diagnose.vervang("NUMBER", "NUM")) n++
    if (n == HERSTEL_GRENS) println("DORTUS-E2E [$waar] winkel: herstel stopte op de grens van $HERSTEL_GRENS, er kan nog NUMBER staan")
    return n
}

private const val HERSTEL_GRENS = 100

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
