package com.dortus.bisonflex

import com.dortus.bisonflex.meldingen.BisonOngebruikt
import com.dortus.bisonflex.meldingen.BisonOngedefinieerd
import com.dortus.bisonflex.meldingen.FlexOngebruikt
import com.dortus.bisonflex.meldingen.FlexOngedefinieerd
import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.pro.LicentieStand
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/**
 * Eis 7, toetsbare eisen (a) en (b): de snelle oplossingen geven precies het verwachte bestand, en de bestanden met
 * `api.token.prefix` en `api.token.constructor` geven geen tokenmeldingen (wel regelmeldingen).
 */
class OplossingenTest : BasePlatformTestCase() {
    private val data get() = File(System.getProperty("dortus.testdata"))

    override fun setUp() {
        super.setUp()
        Licentie.zetBronVoorTest { LicentieStand.GELDIG }
        myFixture.enableInspections(BisonOngedefinieerd(), BisonOngebruikt(), FlexOngedefinieerd(), FlexOngebruikt())
    }

    override fun tearDown() {
        try { Licentie.zetBronVoorTest(null) } finally { super.tearDown() }
    }

    private fun lees(naam: String) = File(data, "meldingen/$naam").readText()
    private fun kaal(t: String) = t.replace(Regex("</?(weak_)?warning( descr=\"[^\"]*\")?>"), "")

    /** Opent [bestand] (zonder markeringen) met de cursor op [plek] + [extra], past [oplossing] toe en vergelijkt. */
    private fun pasToe(bestand: String, ander: String, plek: String, extra: Int, oplossing: String, verwacht: String) {
        myFixture.addFileToProject(ander, kaal(lees(ander)))
        val tekst = kaal(lees(bestand))
        val i = tekst.indexOf(plek)
        assertTrue("'$plek' staat in $bestand", i >= 0)
        val metCursor = tekst.substring(0, i + extra) + "<caret>" + tekst.substring(i + extra)
        myFixture.configureByText(bestand, metCursor)
        val actie = myFixture.getAvailableIntention(oplossing)
        assertNotNull("snelle oplossing '$oplossing' aangeboden", actie)
        myFixture.launchAction(actie!!)
        assertEquals(lees(verwacht), myFixture.editor.document.text)
    }

    /** Regel in twee stukken: beide stukken weg (met de lege regel erna) en de naam uit `%type`. */
    fun testRegelWeg() = pasToe("fout.y", "fout.l", "\nlos: NUM", 2, "Remove unused rule 'los'", "fout.y.na-regel")

    /** Token in `%token` en `%left`: uit beide weg; `%left '+'` blijft staan, want '+' heeft ook voorrang. */
    fun testTokenWeg() = pasToe("fout.y", "fout.l", "%token WEG", 8, "Remove unused token 'WEG'", "fout.y.na-token")

    fun testConditieWeg() = pasToe("fout.l", "fout.y", "%x WEG", 4, "Remove unused start condition 'WEG'", "fout.l.na-conditie")

    /** Op ongedefinieerd is er in 1.0 geen snelle oplossing. */
    fun testGeenOplossingOpOngedefinieerd() {
        myFixture.addFileToProject("fout.l", kaal(lees("fout.l")))
        val tekst = kaal(lees("fout.y"))
        val i = tekst.indexOf("ONBEKEND ;") + 2
        myFixture.configureByText("fout.y", tekst.substring(0, i) + "<caret>" + tekst.substring(i))
        assertEquals(emptyList<String>(), myFixture.availableIntentions.map { it.text }.filter { it.startsWith("Remove unused") })
    }

    private fun meldingen(): List<String> = myFixture.doHighlighting()
        .filter { it.description?.matches(Regex("(Undefined|Unused) .*")) == true }.map { it.description }

    /** `%define api.token.prefix {TOK_}`: de scanner geeft `TOK_NUM`, dus geen tokenmeldingen, wel de regel. */
    fun testPrefix() {
        myFixture.addFileToProject("fout-prefix.l", lees("fout-prefix.l"))
        myFixture.configureByText("fout-prefix.y", lees("fout-prefix.y"))
        myFixture.checkHighlighting(true, false, true)
    }

    /** `%define api.token.constructor`: de scanner geeft `make_NUM`, dus geen tokenmeldingen, wel de regel. */
    fun testConstructor() {
        myFixture.addFileToProject("fout-constructor.ll", lees("fout-constructor.ll"))
        myFixture.configureByText("fout-constructor.yy", lees("fout-constructor.yy"))
        myFixture.checkHighlighting(true, false, true)
    }

    /** Controle dat de twee tests hierboven iets toetsen: zonder de define komen de tokenmeldingen wel. */
    fun testZonderDefineWelTokens() {
        for ((y, l, define) in listOf(
            Triple("fout-prefix.y", "fout-prefix.l", "%define api.token.prefix {TOK_}\n"),
            Triple("fout-constructor.yy", "fout-constructor.ll", "%define api.token.constructor\n"),
        )) {
            myFixture.addFileToProject(l, lees(l))
            val tekst = kaal(lees(y))
            assertTrue(define in tekst)
            myFixture.configureByText(y, tekst.replace(define, ""))
            val m = meldingen()
            assertTrue("$y zonder define: $m", m.contains("Unused token 'ONGEBRUIKT'"))
            assertTrue("$y zonder define: $m", m.contains("Unused rule 'los'"))
        }
    }
}
