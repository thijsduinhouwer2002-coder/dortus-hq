package com.dortus.bisonflex

import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.pro.LicentieStand
import com.dortus.bisonflex.pro.ProMelding
import com.dortus.bisonflex.psi.NaamElement
import com.intellij.notification.Notification
import com.intellij.notification.Notifications
import com.intellij.psi.PsiDocumentManager
import com.intellij.psi.PsiFile
import com.intellij.psi.PsiManager
import com.intellij.psi.util.PsiTreeUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/**
 * Eis 6, rest: alle plekken vinden en hernoemen voor regel, token en start-conditie, en van `.y` terug naar `.l`.
 * Gratis en Pro (Jet): binnen één bestand altijd; wat het andere bestand raakt is Pro. De rekenmachine uit
 * `e2e/project/`. In `calc.y` staat `exp` op regel 25 (definitie), 22, 27 tot en met 31; `NUM` op 9 en 26.
 */
class AllePlekkenTest : BasePlatformTestCase() {

    private val meldingen = ArrayList<Notification>()
    private val map get() = File(System.getProperty("dortus.testdata")).parentFile.resolve("e2e/project")
    private fun tekst(naam: String) = File(map, naam).readText()

    override fun setUp() {
        super.setUp()
        ProMelding.getInstance().opnieuwVoorTest()
        project.messageBus.connect(testRootDisposable).subscribe(Notifications.TOPIC, object : Notifications {
            override fun notify(notification: Notification) {
                if (notification.groupId == ProMelding.GROEP) meldingen += notification
            }
        })
    }

    override fun tearDown() {
        try {
            Licentie.zetBronVoorTest(null)
            ProMelding.getInstance().opnieuwVoorTest()
        } finally {
            super.tearDown()
        }
    }

    private fun stand(s: LicentieStand) = Licentie.zetBronVoorTest { s }

    /** De eerste definitie met [naam] in [f]. */
    private fun definitie(f: PsiFile, naam: String): NaamElement =
        PsiTreeUtil.findChildrenOfType(f, NaamElement::class.java).first { it.name == naam }

    /** Alle plekken (Alt+F7) als `bestand:regel`, gesorteerd. */
    private fun plekken(f: PsiFile, naam: String): List<String> = myFixture.findUsages(definitie(f, naam)).map {
        val e = it.element!!
        val d = PsiDocumentManager.getInstance(project).getDocument(e.containingFile)!!
        "${e.containingFile.name}:${d.getLineNumber(it.navigationRange!!.startOffset) + 1}"
    }.sorted()

    /** Zet de cursor op het [n]-de voorkomen (vanaf 0) van [woord]. */
    private fun cursorOp(woord: String, n: Int = 0) {
        val inhoud = myFixture.editor.document.text
        var plek = -1
        repeat(n + 1) { plek = inhoud.indexOf(woord, plek + 1) }
        assertTrue("'$woord' (#$n) niet gevonden", plek >= 0)
        myFixture.editor.caretModel.moveToOffset(plek + 1)
    }

    private fun inhoud(pad: String): String {
        PsiDocumentManager.getInstance(project).commitAllDocuments()
        val vf = myFixture.findFileInTempDir(pad)
        return PsiManager.getInstance(project).findFile(vf)!!.text
    }

    private fun hernoemd(t: String, oud: String, nieuw: String) = t.replace(Regex("\\b$oud\\b"), nieuw)

    // ---- binnen één bestand: gratis ----

    fun testRegelZonderLicentie() {
        stand(LicentieStand.GEEN)
        val f = myFixture.configureByText("calc.y", tekst("calc.y"))
        assertEquals(listOf(22, 27, 27, 28, 28, 29, 29, 30, 30, 31).map { "calc.y:$it" }, plekken(f, "exp"))
        assertEquals(listOf("calc.y:17"), plekken(f, "line"))
        cursorOp("exp:")
        myFixture.renameElementAtCaret("expr")
        assertEquals(hernoemd(tekst("calc.y"), "exp", "expr"), myFixture.editor.document.text)
        assertEquals(0, meldingen.size)
    }

    fun testTokenZonderLicentieAlleenGrammatica() {
        stand(LicentieStand.GEEN)
        val f = myFixture.configureByText("calc.y", tekst("calc.y"))
        assertEquals(listOf("calc.y:26"), plekken(f, "NUM"))
        cursorOp("NUM", 1) // het gebruik in `exp: NUM`
        myFixture.renameElementAtCaret("GETAL")
        assertEquals(hernoemd(tekst("calc.y"), "NUM", "GETAL"), myFixture.editor.document.text)
        assertEquals(0, meldingen.size)
    }

    fun testTokenMetTypeDubbeleDefinitieEnEpiloog() {
        stand(LicentieStand.GEEN)
        val f = myFixture.configureByText("t.y", GRAMMATICA)
        // %type, het gebruik, de tweede `exp:` en `exp '-' exp`.
        assertEquals(listOf("t.y:2", "t.y:5", "t.y:6", "t.y:6", "t.y:6"), plekken(f, "exp"))
        // %left NUM, twee gebruiken en `return NUM;` in de epiloog.
        assertEquals(listOf("t.y:3", "t.y:5", "t.y:5", "t.y:8"), plekken(f, "NUM"))
        cursorOp("NUM")
        myFixture.renameElementAtCaret("GETAL")
        cursorOp("exp")
        myFixture.renameElementAtCaret("expr")
        assertEquals(hernoemd(hernoemd(GRAMMATICA, "NUM", "GETAL"), "exp", "expr"), myFixture.editor.document.text)
    }

    fun testStartConditieZonderLicentie() {
        stand(LicentieStand.GEEN)
        val f = myFixture.configureByText("sc.l", START_CONDITIES)
        // BEGIN(COMMENT) in een actie, <COMMENT> en <STR,COMMENT>.
        assertEquals(listOf("sc.l:3", "sc.l:4", "sc.l:5"), plekken(f, "COMMENT"))
        assertEquals(listOf("sc.l:5"), plekken(f, "STR"))
        cursorOp("COMMENT", 2) // op <COMMENT>
        myFixture.renameElementAtCaret("OPMERKING")
        assertEquals(hernoemd(START_CONDITIES, "COMMENT", "OPMERKING"), myFixture.editor.document.text)
        assertEquals(0, meldingen.size)
    }

    // ---- tussen .y en .l: Pro ----

    private fun tussenBestanden(s: LicentieStand) {
        stand(s)
        myFixture.addFileToProject("calc.l", tekst("calc.l"))
        val f = myFixture.configureByText("calc.y", tekst("calc.y"))
        // Terug van .y naar .l: `return NUM;` in de Flex-actie.
        assertEquals(listOf("calc.l:11", "calc.y:26"), plekken(f, "NUM"))
        cursorOp("NUM")
        myFixture.renameElementAtCaret("GETAL")
        assertEquals(hernoemd(tekst("calc.y"), "NUM", "GETAL"), inhoud("calc.y"))
        assertEquals(hernoemd(tekst("calc.l"), "NUM", "GETAL"), inhoud("calc.l"))
        assertEquals(0, meldingen.size)
    }

    fun testTussenBestandenMetLicentie() = tussenBestanden(LicentieStand.GELDIG)
    fun testTussenBestandenStandOnbekend() = tussenBestanden(LicentieStand.ONBEKEND)

    fun testHernoemenVanafScannerMetLicentie() {
        stand(LicentieStand.GELDIG)
        myFixture.addFileToProject("calc.y", tekst("calc.y"))
        myFixture.configureByText("calc.l", tekst("calc.l"))
        cursorOp("NUM")
        myFixture.renameElementAtCaret("GETAL")
        assertEquals(hernoemd(tekst("calc.y"), "NUM", "GETAL"), inhoud("calc.y"))
        assertEquals(hernoemd(tekst("calc.l"), "NUM", "GETAL"), inhoud("calc.l"))
    }

    fun testZonderLicentieAllePlekkenAlleenEigenBestand() {
        stand(LicentieStand.GEEN)
        myFixture.addFileToProject("calc.l", tekst("calc.l"))
        val f = myFixture.configureByText("calc.y", tekst("calc.y"))
        assertEquals(listOf("calc.y:26"), plekken(f, "NUM"))
        assertEquals(0, meldingen.size)
    }

    fun testZonderLicentieHernoemenDatScannerRaaktGebeurtNiet() {
        stand(LicentieStand.GEEN)
        myFixture.addFileToProject("calc.l", tekst("calc.l"))
        myFixture.configureByText("calc.y", tekst("calc.y"))
        cursorOp("NUM")
        myFixture.renameElementAtCaret("GETAL")
        assertEquals(tekst("calc.y"), inhoud("calc.y"))
        assertEquals(tekst("calc.l"), inhoud("calc.l"))
        assertEquals(1, meldingen.size)
        assertEquals(ProMelding.TEKST, meldingen[0].content)
        assertEquals(0, ProMelding.getInstance().aantalHints())
        // Tweede keer: geen tweede balloon, wel de korte hint; nog steeds niets veranderd.
        myFixture.renameElementAtCaret("GETAL")
        assertEquals(tekst("calc.y"), inhoud("calc.y"))
        assertEquals(tekst("calc.l"), inhoud("calc.l"))
        assertEquals(1, meldingen.size)
        assertEquals(1, ProMelding.getInstance().aantalHints())
        // Een regel raakt de scanner niet: die hernoemt gewoon.
        cursorOp("exp:")
        myFixture.renameElementAtCaret("expr")
        assertEquals(hernoemd(tekst("calc.y"), "exp", "expr"), inhoud("calc.y"))
        assertEquals(tekst("calc.l"), inhoud("calc.l"))
    }

    fun testGrammaticaInDezelfdeMapGaatVoor() {
        stand(LicentieStand.GELDIG)
        myFixture.addFileToProject("a/calc.l", tekst("calc.l"))
        val a = myFixture.addFileToProject("a/calc.y", tekst("calc.y"))
        val b = myFixture.addFileToProject("b/calc.y", tekst("calc.y"))
        assertEquals(listOf("calc.l:11", "calc.y:26"), plekken(a, "NUM"))
        assertEquals(listOf("calc.y:26"), plekken(b, "NUM"))
    }

    // ---- de 10 echte bestanden ----

    fun testEchteBestandenGeenValsePlekken() {
        stand(LicentieStand.GELDIG)
        val bestanden = File(System.getProperty("dortus.testdata")).listFiles()!!
            .filter { it.extension in setOf("y", "yy", "l", "ll") }.sortedBy { it.name }
        assertEquals(10, bestanden.size)
        for (b in bestanden) {
            val f = myFixture.configureByText(b.name, b.readText())
            val namen = PsiTreeUtil.findChildrenOfType(f, NaamElement::class.java).filter { it.eerste() == it }
            // Een scanner zonder start-condities (pg-bootscanner.l) heeft geen namen; een grammatica altijd.
            if (f.language == BisonLanguage) assertTrue("${b.name}: geen namen", namen.isNotEmpty())
            for (n in namen) {
                for (r in com.intellij.psi.search.searches.ReferencesSearch.search(n).findAll()) {
                    val gevonden = r.rangeInElement.substring(r.element.text)
                    assertEquals("${b.name}: valse plek voor ${n.name}", n.name, gevonden)
                    assertTrue("${b.name}: ${n.name} gaat niet terug", r.isReferenceTo(n))
                }
            }
        }
    }

    companion object {
        const val START_CONDITIES =
            "%x COMMENT STR\n%%\n\"/*\"  BEGIN(COMMENT);\n<COMMENT>\"*/\"  BEGIN(INITIAL);\n<STR,COMMENT>.  ;\n%%\n"

        val GRAMMATICA = """
            %token <int> NUM
            %type <int> exp
            %left NUM
            %%
            exp: NUM | exp '+' NUM ;
            exp: exp '-' exp ;
            %%
            int yylex(void) { return NUM; }
        """.trimIndent() + "\n"
    }
}
