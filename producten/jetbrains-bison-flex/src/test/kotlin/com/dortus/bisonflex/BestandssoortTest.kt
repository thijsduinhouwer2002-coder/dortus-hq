package com.dortus.bisonflex

import com.intellij.openapi.util.IconLoader
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/** Eis 1 en een eerste stap van eis 2 uit ontwerp.md. */
class BestandssoortTest : BasePlatformTestCase() {

    fun testExtensiesKrijgenOnzeSoort() {
        val verwacht = mapOf("calc.y" to BisonFileType, "calc.yy" to BisonFileType,
            "calc.l" to FlexFileType, "calc.ll" to FlexFileType)
        for ((naam, soort) in verwacht) {
            val file = myFixture.configureByText(naam, "%%\n")
            assertSame("soort van $naam", soort, file.fileType)
            assertEquals("taal van $naam", soort.language, file.language)
        }
    }

    // In lichte tests staat IconLoader uit (dan breedte 1); hier zetten we hem even aan.
    fun testIconenLadenEchtOp16() {
        IconLoader.activate()
        try {
            assertEquals(16, BisonFileType.icon.iconWidth)
            assertEquals(16, FlexFileType.icon.iconWidth)
        } finally {
            IconLoader.deactivate()
        }
    }

    fun testIconenBestaanInLichtEnDonker() {
        for (naam in listOf("bison", "bison_dark", "flex", "flex_dark")) {
            val tekst = javaClass.getResource("/icons/$naam.svg")?.readText()
            assertNotNull("icoon $naam.svg", tekst)
            assertTrue("$naam.svg is 16 bij 16", tekst!!.contains("width=\"16\"") && tekst.contains("height=\"16\""))
        }
    }

    fun testEchteBestandenGevenEenBoomZonderVerlies() {
        val map = File(System.getProperty("dortus.testdata"))
        val bestanden = map.listFiles { f -> f.extension in setOf("y", "yy", "l", "ll") }!!.sortedBy { it.name }
        assertEquals("aantal bestanden in de vaste testset", 10, bestanden.size)
        for (f in bestanden) {
            val tekst = f.readText()
            val psi = myFixture.configureByText(f.name, tekst)
            assertEquals("tekst van ${f.name} blijft gelijk", tekst, psi.text)
            assertTrue("${f.name} is onze soort", psi.fileType === BisonFileType || psi.fileType === FlexFileType)
        }
    }
}
