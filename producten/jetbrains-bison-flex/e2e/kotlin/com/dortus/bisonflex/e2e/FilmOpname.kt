package com.dortus.bisonflex.e2e

import com.intellij.driver.client.Driver
import com.intellij.driver.client.Remote
import com.intellij.driver.client.service
import com.intellij.driver.client.utility
import com.intellij.driver.model.LockSemantics
import com.intellij.driver.model.OnDispatcher
import com.intellij.driver.sdk.FileEditorManager
import com.intellij.driver.sdk.closeToolWindow
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
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test
import java.awt.Point
import java.nio.file.Files
import java.nio.file.Path
import kotlin.io.path.createDirectories
import kotlin.io.path.writeText
import kotlin.time.Duration.Companion.minutes

/*
 * Beelden voor het filmpje van Daan (ontwerp/bison-flex/film.md, "Wat ik van Jet vraag"). Eigen test en eigen
 * workflow (jetbrains-bison-flex-film.yml), los van de gewone IDE-test: Xvfb 3840x2160 met factor 2, dus de IDE
 * is 1920x1080 punten en elk beeld wordt verkleind naar 1920x1080 pixels (punten = pixels in het beeld).
 * IDEA Community, donker thema (New UI), lettergrootte editor 18, eigen projectmap met alleen calc.l en calc.y
 * (anders geeft Ctrl+Click een keuzelijst). Scène 3 is gratis (stand GEEN), vanaf scène 4 stand GELDIG (Pro).
 * Per beeld: scene<n>/<nnnn>.png, een regel in posities.tsv met de schermplek van elke NUM of NUMBER die in beeld
 * staat (x, y, breedte, hoogte in pixels van het beeld van 1920x1080), en een regel in het log. Scène 4 ook in 4k/
 * (3840x2160), voor de haak van Daan dichtbij. Fouten pas aan het eind, zodat een mislukte scène de rest niet stopt.
 */

@Remote("com.intellij.openapi.editor.ex.EditorEx")
interface EditorExOpAfstand {
    fun setFontSize(fontSize: Int)
    fun getColorsScheme(): KleurSchemaOpAfstand
}

@Remote("com.intellij.openapi.editor.colors.EditorColorsScheme")
interface KleurSchemaOpAfstand {
    fun getEditorFontSize(): Int
}

@Remote("com.intellij.openapi.fileEditor.FileEditorManager")
interface GekozenBestandOpAfstand {
    fun getInstance(project: com.intellij.driver.sdk.Project): GekozenBestandOpAfstand
    fun getSelectedFiles(): Array<BestandOpAfstand>
}

private const val LETTERGROOTTE = 18
private const val NA_INPUT = "  | input line\n  ;\n"
private const val NA_INPUT_ONGEBRUIKT = "  | input line\n  ;\n\nterm:\n    exp\n  ;\n"

class FilmOpname {
    private val film: Path by lazy { schermen.resolve("film").also { it.createDirectories() } }
    private val posities = mutableListOf("scene\tbeeld\tbestand\twoord\tx\ty\tbreedte\thoogte")

    init { zetCiServer() }

    @Test
    fun film() {
        val project = winkelproject("bisonflex-film")
        for (b in listOf("calc.yy", "calc.ll")) Files.deleteIfExists(project.resolve(b))
        println("DORTUS-FILM projectmap ${Files.list(project).use { s -> s.map { it.fileName.toString() }.sorted().toList() }}")
        Starter.newContext("bisonflex-film", TestCase(IdeProductProvider.IC, LocalProjectInfo(project)).useRelease(IdeTest.IDE_VERSIE))
            .apply {
                richIn("ExperimentalDark", "Dark") { addSystemProperty("bisonflex.internal.e2e.forceNoLicense", true) }
                paths.configDir.resolve("options").createDirectories().resolve("editor-font.xml").writeText(
                    """<application><component name="DefaultFont"><option name="FONT_SIZE" value="$LETTERGROOTTE"/><option name="FONT_SIZE_2D" value="$LETTERGROOTTE.0"/></component></application>"""
                )
            }
            .runIdeWithDriver()
            .useDriverAndCloseIde {
                waitForIndicators(5.minutes)
                val ide = IdeTest()
                val diagnose = service<MeldingenDiagnoseOpAfstand>()
                val fouten = mutableListOf<Throwable>()
                for ((scene, werk) in listOf<Pair<Int, () -> Unit>>(
                    3 to { scene3(this, ide) },
                    4 to { diagnose.zetStand("GELDIG"); println("DORTUS-FILM stand GELDIG"); Thread.sleep(3_000); scene4(this, ide) },
                    5 to { scene5(this, ide) },
                    6 to { scene6(this, ide, diagnose) },
                )) {
                    try { werk() } catch (e: Throwable) {
                        println("DORTUS-FILM scène $scene mislukt: ${e.javaClass.simpleName}: ${e.message?.take(300)}")
                        fouten += e
                    }
                }
                Files.writeString(film.resolve("posities.tsv"), posities.joinToString("\n", postfix = "\n"))
                println("DORTUS-FILM klaar: ${posities.size - 1} posities, fouten ${fouten.size}")
                fouten.firstOrNull()?.let { throw it }
            }
    }

    /** Scène 3 (gratis): calc.y met kleuren, Structure klapt open, een tikfout (`:` weg na `line`) geeft een rode golflijn. */
    private fun scene3(d: Driver, ide: IdeTest) = with(d) {
        for (p in listOf("Project", "Structure")) try { closeToolWindow(p) } catch (e: Throwable) { println("DORTUS-FILM $p sluiten: ${e.javaClass.simpleName}") }
        openFile("calc.y")
        lettergrootte()
        muisWeg()
        pauze()
        with(ide) { cursorOp("\nline:", 6) }
        beeld(3)
        openToolWindow("Structure")
        Thread.sleep(300); beeld(3)
        Thread.sleep(700); beeld(3)
        pauze(); beeld(3)
        editorFocus()
        with(ide) { cursorOp("\nline:", 6) }
        toets("BackSpace")
        Thread.sleep(300); beeld(3)
        for (i in 1..3) { Thread.sleep(1_000); beeld(3) }
        // Muis op "line": de lege foutknoop van b.error() staat meestal achter de vorige naam (controleur 9 nov).
        val plek = schermPlek("\nline\n", 3)
        println("DORTUS-FILM scène 3 muis naar ${plek.x},${plek.y} (pixels)")
        for (dx in listOf(0, 2, 4)) { xdo("mousemove", "${plek.x + dx}", "${plek.y}"); Thread.sleep(400) }
        Thread.sleep(3_000); beeld(3)
        Thread.sleep(1_000); beeld(3)
        // Ook de foutomschrijving bij de cursor (Ctrl+F1), voor het geval de zweeftekst niet kwam.
        muisWeg()
        with(ide) { cursorOp("\nline\n", 5) }
        try { invokeAction("ShowErrorDescription", now = false) } catch (e: Throwable) { println("DORTUS-FILM ShowErrorDescription: ${e.javaClass.simpleName}") }
        Thread.sleep(2_000); beeld(3)
        toets("Escape")
        with(ide) { cursorOp("\nline\n", 5) }
        typ(":")
        Thread.sleep(2_000)
        println("DORTUS-FILM scène 3 teruggezet: ${"\nline:" in tekstOpen()}")
        try { closeToolWindow("Structure") } catch (e: Throwable) { println("DORTUS-FILM Structure sluiten: ${e.javaClass.simpleName}") }
    }

    /** Scène 4 (Pro): Ctrl boven NUM in calc.l onderstreept, klik springt naar `%token NUM` in calc.y. */
    private fun scene4(d: Driver, ide: IdeTest) = with(d) {
        openFile("calc.l")
        lettergrootte()
        editorFocus()
        with(ide) { cursorOp("return NUM", 0) }
        muisWeg()
        pauze()
        beeld(4)
        val plek = schermPlek("return NUM", 8)
        xdo("mousemove", "${plek.x}", "${plek.y}")
        Thread.sleep(800); beeld(4)
        var streep = 0
        xdo("keydown", "ctrl")
        try {
            for (dx in listOf(2, 4, 6)) { Thread.sleep(400); xdo("mousemove", "${plek.x + dx}", "${plek.y}") }
            Thread.sleep(2_000)
            streep = onderstreept()
            println("DORTUS-FILM scène 4 onderstrepingen bij Ctrl-zweven (ctrlZweven): $streep")
            beeld(4)
            Thread.sleep(500); beeld(4)
            xdo("click", "1")
        } finally {
            xdo("keyup", "ctrl")
        }
        Thread.sleep(500); beeld(4)
        muisWeg()
        Thread.sleep(2_000)
        val bestand = openBestand()
        val regel = with(ide) { cursorRegel() }
        val doel = with(ide) { regelVan("%token NUM") }
        println("DORTUS-FILM scène 4 na de klik: bestand $bestand, cursor regel ${regel + 1}, %token NUM op regel ${doel + 1}")
        lettergrootte()
        beeld(4)
        assertTrue(streep >= 1, "onderstreping bij Ctrl-zweven op NUM in calc.l (scène 4)")
        assertTrue(bestand == "calc.y" && regel == doel, "Ctrl+Click op NUM springt naar %token NUM in calc.y (scène 4), gezien $bestand regel ${regel + 1}")
    }

    /** Scène 5 (Pro): Shift+F6 op `%token NUM`, NUMBER letter voor letter, daarna calc.l links en calc.y rechts. */
    private fun scene5(d: Driver, ide: IdeTest) = with(d) {
        openFile("calc.y")
        editorFocus()
        with(ide) { cursorOp("%token NUM", 8) }
        pauze()
        val ideVenster = actiefVenster()
        try { invokeAction("RenameElement", now = false) } catch (e: Throwable) { println("DORTUS-FILM RenameElement: ${e.javaClass.simpleName}") }
        val venster = wacht(10) { actiefVenster().let { it != null && it != ideVenster } }
        println("DORTUS-FILM scène 5 hernoemvenster $venster")
        // Zonder venster zouden Ctrl+A en het typen heel calc.y vervangen (controleur 9 nov).
        if (!venster) error("geen hernoemvenster na Shift+F6 op %token NUM (scène 5)")
        Thread.sleep(1_500)
        beeld(5)
        toets("ctrl+a")
        for (letter in "NUMBER") { typ(letter.toString()); Thread.sleep(400); beeld(5) }
        toets("Return")
        val terug = wacht(20) { actiefVenster() == ideVenster }
        println("DORTUS-FILM scène 5 terug in de IDE na Enter: $terug")
        if (!terug) for (i in 1..3) { if (actiefVenster() == ideVenster) break; toets("Escape"); Thread.sleep(1_500) }
        Thread.sleep(2_000)
        // calc.l links en calc.y rechts (film.md): eerst alles dicht, anders springt openFile("calc.y") naar het
        // tabblad links (run 42553896267 gaf calc.y links).
        try { invokeAction("CloseAllEditors") } catch (e: Throwable) { println("DORTUS-FILM CloseAllEditors: ${e.javaClass.simpleName}") }
        Thread.sleep(1_000)
        openFile("calc.l")
        Thread.sleep(1_000)
        val inL = "return NUMBER;" in tekstOpen()
        invokeAction("SplitVertically")
        Thread.sleep(1_500)
        openFile("calc.y")
        Thread.sleep(1_500)
        lettergrootte()
        with(ide) { cursorOp("%token NUMBER", 13) }
        pauze()
        beeld(5)
        Thread.sleep(1_000); beeld(5)
        println("DORTUS-FILM scène 5 return NUMBER; in calc.l: $inL")
        assertTrue(inL, "return NUMBER; in calc.l na hernoemen (scène 5)")
    }

    /** Scène 6 (Pro): een ongebruikte regel, de zweeftekst, het Alt+Enter-menu, en na Enter is de regel weg. */
    private fun scene6(d: Driver, ide: IdeTest, diagnose: MeldingenDiagnoseOpAfstand) = with(d) {
        try { invokeAction("UnsplitAll") } catch (e: Throwable) { println("DORTUS-FILM UnsplitAll: ${e.javaClass.simpleName}") }
        Thread.sleep(1_000)
        openFile("calc.y")
        lettergrootte()
        editorFocus()
        assertTrue(diagnose.vervang(NA_INPUT, NA_INPUT_ONGEBRUIKT), "ongebruikte regel term in calc.y gezet (scène 6)")
        val gezien = wacht(40) { "Unused rule 'term'" in diagnose.meldingen() }
        println("DORTUS-FILM scène 6 melding: ${diagnose.meldingen()}")
        with(ide) { cursorOp("\nterm:", 1) }
        muisWeg()
        pauze(); beeld(6)
        val plek = schermPlek("\nterm:", 2)
        for (dx in listOf(0, 2, 4)) { xdo("mousemove", "${plek.x + dx}", "${plek.y}"); Thread.sleep(400) }
        Thread.sleep(3_000); beeld(6)
        muisWeg()
        toets("Escape")
        with(ide) { cursorOp("\nterm:", 2) }
        Thread.sleep(1_000)
        toets("alt+Return")
        Thread.sleep(3_000); beeld(6)
        toets("Return")
        val weg = wacht(15) { "\nterm:" !in tekstOpen() }
        Thread.sleep(2_000); beeld(6)
        println("DORTUS-FILM scène 6 regel term weg na Enter: $weg")
        assertTrue(gezien, "melding Unused rule 'term' (scène 6)")
        assertTrue(weg, "regel term weg na de snelle oplossing (scène 6)")
    }

    // ---- beelden en posities ----

    private val teller = mutableMapOf<Int, Int>()

    /** Heel scherm (3840x2160, ook vensters en menu's), verkleind naar 1920x1080; scène 4 ook in 4k/. */
    private fun Driver.beeld(scene: Int) {
        val nr = (teller[scene] ?: 0) + 1
        teller[scene] = nr
        val naam = "%04d.png".format(nr)
        val groot = film.resolve("4k/scene$scene").createDirectories().resolve(naam)
        val klein = film.resolve("scene$scene").createDirectories().resolve(naam)
        val code = ProcessBuilder("import", "-window", "root", groot.toString()).inheritIO().start().waitFor()
        val code2 = ProcessBuilder("convert", groot.toString(), "-filter", "Lanczos", "-resize", "1920x1080", klein.toString()).inheritIO().start().waitFor()
        if (scene != 4) Files.deleteIfExists(groot)
        val grootte = if (Files.exists(klein)) Files.size(klein) else 0
        val plekken = plekkenInBeeld()
        plekken.forEach { posities += "$scene\t$nr\t$it" }
        println("DORTUS-FILM beeld scene$scene/$naam: import $code, verklein $code2, $grootte bytes, NUM in beeld: ${plekken.map { it.replace('\t', ' ') }}")
    }

    /** Elke NUM of NUMBER (heel woord) in een getoonde editor die in beeld staat: "bestand woord x y b h" in punten. */
    private fun Driver.plekkenInBeeld(): List<String> = try {
        val beheer = utility<AlleEditorsOpAfstand>().getInstance(singleProject())
        withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
            beheer.getAllEditors().flatMap { fe ->
                val bestand = fe.getFile()?.getName() ?: return@flatMap emptyList()
                val e = try { cast(fe, TekstEditorOpAfstand::class).getEditor() } catch (t: Throwable) { return@flatMap emptyList() }
                val c = e.getContentComponent()
                if (!c.isShowing()) return@flatMap emptyList()
                val o = c.getLocationOnScreen()
                val zicht = e.getScrollingModel().getVisibleArea()
                val h = e.getLineHeight()
                Regex("\\bNUM(BER)?\\b").findAll(e.getDocument().getText()).mapNotNull { m ->
                    val a = e.offsetToXY(m.range.first)
                    val b = e.offsetToXY(m.range.last + 1)
                    if (a.y < zicht.y || a.y + h > zicht.y + zicht.height || a.x < zicht.x || b.x > zicht.x + zicht.width) null
                    else "$bestand\t${m.value}\t${o.x + a.x}\t${o.y + a.y}\t${b.x - a.x}\t$h"
                }.toList()
            }
        }
    } catch (t: Throwable) {
        listOf("fout\t${t.javaClass.simpleName}\t0\t0\t0\t0")
    }

    /** Schermplek in pixels (xdotool, factor 2) van [tekst] plus [extra] tekens in de open editor, midden van de regel. */
    private fun Driver.schermPlek(tekst: String, extra: Int): Point {
        val editor = cast(service<FileEditorManager>(singleProject()).getSelectedTextEditor()!!, EditorMetOnderdeel::class)
        return withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) {
            val xy = editor.offsetToXY(editor.getDocument().getText().indexOf(tekst) + extra)
            val o = editor.getContentComponent().getLocationOnScreen()
            Point((o.x + xy.x + 3) * 2, (o.y + xy.y + editor.getLineHeight() / 2) * 2)
        }
    }

    /** Aantal navigatie-onderstrepingen (laag HYPERLINK, 5900) in de open editor. */
    private fun Driver.onderstreept(): Int = try {
        val editor = cast(service<FileEditorManager>(singleProject()).getSelectedTextEditor()!!, EditorMetOnderdeel::class)
        withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) { editor.getMarkupModel().getAllHighlighters().count { it.getLayer() == 5900 } }
    } catch (t: Throwable) {
        println("DORTUS-FILM onderstrepingen niet te lezen: ${t.javaClass.simpleName}")
        -1
    }

    /** Lettergrootte 18 in elke getoonde editor; logt wat er stond (het instellingenbestand kan genegeerd worden). */
    private fun Driver.lettergrootte() = try {
        val beheer = utility<AlleEditorsOpAfstand>().getInstance(singleProject())
        withContext(OnDispatcher.EDT) {
            beheer.getAllEditors().forEach { fe ->
                val e = try { cast(cast(fe, TekstEditorOpAfstand::class).getEditor(), EditorExOpAfstand::class) } catch (t: Throwable) { return@forEach }
                val voor = e.getColorsScheme().getEditorFontSize()
                if (voor != LETTERGROOTTE) e.setFontSize(LETTERGROOTTE)
                println("DORTUS-FILM lettergrootte ${fe.getFile()?.getName()}: was $voor, nu ${e.getColorsScheme().getEditorFontSize()}")
            }
        }
    } catch (t: Throwable) {
        println("DORTUS-FILM lettergrootte niet gezet: ${t.javaClass.simpleName}: ${t.message?.take(200)}")
    }

    /** Naam van het bestand in de editor met de focus. */
    private fun Driver.openBestand(): String? = try {
        val beheer = utility<GekozenBestandOpAfstand>().getInstance(singleProject())
        withContext(OnDispatcher.EDT) { beheer.getSelectedFiles().firstOrNull()?.getName() }
    } catch (t: Throwable) {
        "onbekend (${t.javaClass.simpleName})"
    }

    private fun Driver.tekstOpen(): String = service<FileEditorManager>(singleProject()).getSelectedTextEditor()?.let { e ->
        withContext(OnDispatcher.EDT, LockSemantics.READ_ACTION) { e.getDocument().getText() }
    } ?: ""

    private fun Driver.editorFocus() {
        val editor = service<FileEditorManager>(singleProject()).getSelectedTextEditor() ?: return
        withContext(OnDispatcher.EDT) { cast(editor, EditorMetOnderdeel::class).getContentComponent().requestFocusInWindow() }
        Thread.sleep(500)
    }

    private fun muisWeg() = xdo("mousemove", "3830", "2150")

    private fun xdo(vararg args: String) {
        val code = ProcessBuilder(listOf("xdotool") + args).inheritIO().start().waitFor()
        if (code != 0) println("DORTUS-FILM xdotool ${args.joinToString(" ")}: code $code")
    }
}
