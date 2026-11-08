package com.dortus.bisonflex

import com.dortus.bisonflex.meldingen.BisonOngebruikt
import com.dortus.bisonflex.meldingen.BisonOngedefinieerd
import com.dortus.bisonflex.meldingen.FlexOngebruikt
import com.dortus.bisonflex.meldingen.FlexOngedefinieerd
import com.dortus.bisonflex.meldingen.StandWacht
import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.pro.LicentieStand
import com.dortus.bisonflex.pro.ProMelding
import com.intellij.codeInspection.InspectionManager
import com.intellij.openapi.project.DumbService
import com.intellij.testFramework.DumbModeTestUtils
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/** Eis 7, toetsbare eisen (d) en (e): geen tokenmelding en geen Pro-balloon tijdens indexeren, en de standwacht. */
class IndexerenTest : BasePlatformTestCase() {
    private val data get() = File(System.getProperty("dortus.testdata"))
    private val inspecties = listOf(BisonOngedefinieerd(), BisonOngebruikt(), FlexOngedefinieerd(), FlexOngebruikt())

    override fun setUp() {
        super.setUp()
        ProMelding.getInstance().opnieuwVoorTest()
    }

    override fun tearDown() {
        try { Licentie.zetBronVoorTest(null); ProMelding.getInstance().opnieuwVoorTest() } finally { super.tearDown() }
    }

    private fun kaal(naam: String) =
        File(data, "meldingen/$naam").readText().replace(Regex("</?(weak_)?warning( descr=\"[^\"]*\")?>"), "")

    private fun meldingen(pad: String): List<String> {
        val f = myFixture.psiManager.findFile(myFixture.findFileInTempDir(pad))!!
        val m = InspectionManager.getInstance(project)
        return inspecties.flatMap { i -> (i.checkFile(f, m, false) ?: emptyArray()).map { it.descriptionTemplate } }
    }

    /** Tijdens indexeren (dumb mode) geen enkele tokenmelding en geen Pro-balloon; daarna wel de tokenmeldingen. */
    fun testGeenTokenmeldingTijdensIndexeren() {
        Licentie.zetBronVoorTest { LicentieStand.GELDIG }
        myFixture.addFileToProject("fout.l", kaal("fout.l"))
        myFixture.addFileToProject("fout.y", kaal("fout.y"))
        var tijdens: List<String> = emptyList()
        DumbModeTestUtils.runInDumbModeSynchronously(project) {
            assertTrue(DumbService.isDumb(project))
            tijdens = meldingen("fout.y")
        }
        println("Meldingen tijdens indexeren: $tijdens")
        assertEquals(emptyList<String>(), tijdens.filter { it.startsWith("Unused token") })
        assertFalse("geen Pro-balloon tijdens indexeren", ProMelding.getInstance().isGetoond())
        val na = meldingen("fout.y")
        assertTrue("na het indexeren wel tokenmeldingen: $na", na.contains("Unused token 'ONGEBRUIKT'"))
    }

    /** Stand GEEN tijdens indexeren: niets, ook geen balloon of hint. */
    fun testGeenLicentieTijdensIndexeren() {
        Licentie.zetBronVoorTest { LicentieStand.GEEN }
        myFixture.addFileToProject("fout.l", kaal("fout.l"))
        myFixture.addFileToProject("fout.y", kaal("fout.y"))
        DumbModeTestUtils.runInDumbModeSynchronously(project) {
            assertEquals(emptyList<String>(), meldingen("fout.y") + meldingen("fout.l"))
        }
        assertEquals(emptyList<String>(), meldingen("fout.y") + meldingen("fout.l"))
        assertFalse(ProMelding.getInstance().isGetoond())
        assertEquals(0, ProMelding.getInstance().aantalHints())
    }

    /** De standwacht herstart de analyse alleen als Pro aan of uit gaat, niet bij elke kijkbeurt. */
    fun testStandWacht() {
        var stand = LicentieStand.GEEN
        Licentie.zetBronVoorTest { stand }
        var herstarts = 0
        val wacht = StandWacht { herstarts++ }
        wacht.kijk()
        assertEquals("geen wijziging, geen herstart", 0, herstarts)
        stand = LicentieStand.GELDIG
        wacht.kijk()
        assertEquals("proef gestart: herstart", 1, herstarts)
        wacht.kijk()
        assertEquals(1, herstarts)
        stand = LicentieStand.ONBEKEND
        wacht.kijk()
        assertEquals("GELDIG naar ONBEKEND: Pro werkt nog, geen herstart", 1, herstarts)
        stand = LicentieStand.GEEN
        wacht.kijk()
        assertEquals("proef voorbij: herstart", 2, herstarts)
    }
}
