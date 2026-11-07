package com.dortus.bisonflex

import com.intellij.psi.PsiErrorElement
import com.intellij.psi.PsiFileFactory
import com.intellij.psi.util.PsiTreeUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/**
 * Het Engelse winkelproject (`e2e/calculator/`) staat op de winkelplaatjes.
 * Het moet zonder enige fout gelezen worden, net als de rekenmachine in `e2e/project/` (eis 2).
 */
class WinkelVoorbeeldTest : BasePlatformTestCase() {

    fun testWinkelprojectZonderFouten() {
        val map = File(System.getProperty("dortus.testdata"), "../e2e/calculator")
        val bestanden = map.listFiles()!!.filter { it.extension in setOf("y", "yy", "l", "ll") }.sortedBy { it.name }
        assertEquals(listOf("calc.l", "calc.ll", "calc.y", "calc.yy"), bestanden.map { it.name })
        for (b in bestanden) {
            val soort = if (b.extension.startsWith("y")) BisonFileType else FlexFileType
            val f = PsiFileFactory.getInstance(project).createFileFromText(b.name, soort, b.readText())
            val fouten = PsiTreeUtil.collectElementsOfType(f, PsiErrorElement::class.java)
            assertTrue("${b.name}: ${fouten.map { it.errorDescription }}", fouten.isEmpty())
        }
    }

    /** Geen Nederlands op de winkelplaatjes: de winkel is Engelstalig. */
    fun testWinkelprojectIsEngels() {
        val map = File(System.getProperty("dortus.testdata"), "../e2e/calculator")
        val tekst = map.listFiles()!!.joinToString("\n") { it.readText() }.lowercase()
        for (woord in listOf("rekenmachine", "spaties", "onbekend", "overslaan", "handleiding")) {
            assertFalse("Nederlands woord '$woord' in het winkelproject", woord in tekst)
        }
    }
}
