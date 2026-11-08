package com.dortus.bisonflex

import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.pro.LicentieStand
import com.dortus.bisonflex.pro.ProMelding
import com.dortus.bisonflex.psi.NaamElement
import com.intellij.codeInsight.navigation.targetPresentation
import com.intellij.psi.PsiDocumentManager
import com.intellij.psi.PsiFile
import com.intellij.psi.PsiManager
import com.intellij.psi.util.PsiTreeUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/**
 * Het testproject van de IDE-test (`e2e/calculator/`): calc.y, calc.yy, calc.l en calc.ll in één map.
 * 1. Het kiesmenu (Ctrl+B, Alt+F7, Shift+F6 op NUM in calc.l) toont de bestandsnaam, zodat de twee regels
 *    niet meer gelijk zijn (Daan, beoordeling 13).
 * 2. Hernoemen van NUM vanuit calc.y met Pro raakt beide scanners in die map (IDE-run 42458935689 leek
 *    alleen calc.ll te raken).
 */
class TweeScannersTest : BasePlatformTestCase() {

    private val map get() = File(System.getProperty("dortus.testdata")).parentFile.resolve("e2e/calculator")
    private fun tekst(naam: String) = File(map, naam).readText()

    override fun setUp() {
        super.setUp()
        ProMelding.getInstance().opnieuwVoorTest()
    }

    override fun tearDown() {
        try {
            Licentie.zetBronVoorTest(null)
            ProMelding.getInstance().opnieuwVoorTest()
        } finally {
            super.tearDown()
        }
    }

    private fun token(f: PsiFile, naam: String): NaamElement =
        PsiTreeUtil.findChildrenOfType(f, NaamElement::class.java).first { it.name == naam }

    private fun inhoud(pad: String): String {
        PsiDocumentManager.getInstance(project).commitAllDocuments()
        return PsiManager.getInstance(project).findFile(myFixture.findFileInTempDir(pad))!!.text
    }

    private fun hernoemd(t: String) = t.replace(Regex("\\bNUM\\b"), "NUMBER")

    fun testKiesmenuToontBestandsnaam() {
        val y = myFixture.addFileToProject("calc.y", tekst("calc.y"))
        val yy = myFixture.addFileToProject("calc.yy", tekst("calc.yy"))
        val a = token(y, "NUM")
        val b = token(yy, "NUM")
        assertEquals("NUM", a.presentation.presentableText)
        assertEquals("calc.y", a.presentation.locationString)
        assertEquals("calc.yy", b.presentation.locationString)
        // Zo rekent het kiesmenu van het platform de regel uit: naam, en grijs erachter de bestandsnaam.
        val pa = targetPresentation(a)
        val pb = targetPresentation(b)
        assertEquals("NUM", pa.presentableText)
        assertEquals("calc.y", pa.containerText)
        assertEquals("calc.yy", pb.containerText)
        assertFalse(pa.presentableText + pa.containerText == pb.presentableText + pb.containerText)
    }

    fun testHernoemenVanafGrammaticaRaaktBeideScanners() {
        Licentie.zetBronVoorTest { LicentieStand.GELDIG }
        myFixture.addFileToProject("calc.yy", tekst("calc.yy"))
        myFixture.addFileToProject("calc.l", tekst("calc.l"))
        myFixture.addFileToProject("calc.ll", tekst("calc.ll"))
        myFixture.configureByText("calc.y", tekst("calc.y"))
        myFixture.editor.caretModel.moveToOffset(myFixture.editor.document.text.indexOf("%token NUM") + 8)
        myFixture.renameElementAtCaret("NUMBER")
        assertEquals(hernoemd(tekst("calc.y")), inhoud("calc.y"))
        assertEquals(hernoemd(tekst("calc.l")), inhoud("calc.l"))
        assertEquals(hernoemd(tekst("calc.ll")), inhoud("calc.ll"))
        // calc.yy is een eigen grammatica: die blijft zoals hij was.
        assertEquals(tekst("calc.yy"), inhoud("calc.yy"))
    }
}
