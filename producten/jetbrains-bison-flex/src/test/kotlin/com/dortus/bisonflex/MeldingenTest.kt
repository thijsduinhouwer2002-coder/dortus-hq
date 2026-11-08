package com.dortus.bisonflex

import com.dortus.bisonflex.meldingen.BisonOngebruikt
import com.dortus.bisonflex.meldingen.BisonOngedefinieerd
import com.dortus.bisonflex.meldingen.FlexOngebruikt
import com.dortus.bisonflex.meldingen.FlexOngedefinieerd
import com.dortus.bisonflex.meldingen.MeldingInspectie
import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.pro.LicentieStand
import com.intellij.codeInspection.InspectionManager
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/** Eis 7: ongedefinieerd en ongebruikt (ontwerp.md, "Ontwerp eis 7"), met een nagebootste licentie. */
class MeldingenTest : BasePlatformTestCase() {
    private val data get() = File(System.getProperty("dortus.testdata"))
    private val inspecties = listOf(BisonOngedefinieerd(), BisonOngebruikt(), FlexOngedefinieerd(), FlexOngebruikt())

    override fun setUp() {
        super.setUp()
        Licentie.zetBronVoorTest { LicentieStand.GELDIG }
        myFixture.enableInspections(*inspecties.toTypedArray())
    }

    override fun tearDown() {
        try { Licentie.zetBronVoorTest(null) } finally { super.tearDown() }
    }

    private fun lees(naam: String) = File(data, "meldingen/$naam").readText()
    private fun kaal(t: String) = t.replace(Regex("</?(weak_)?warning( descr=\"[^\"]*\")?>"), "")

    fun testFoutY() {
        myFixture.addFileToProject("fout.l", kaal(lees("fout.l")))
        myFixture.configureByText("fout.y", lees("fout.y"))
        myFixture.checkHighlighting(true, false, true)
    }

    fun testFoutL() {
        myFixture.addFileToProject("fout.y", kaal(lees("fout.y")))
        myFixture.configureByText("fout.l", lees("fout.l"))
        myFixture.checkHighlighting(true, false, true)
    }

    private fun meldingen(): List<String> = myFixture.doHighlighting()
        .filter { it.description?.matches(Regex("(Undefined|Unused) .*")) == true }.map { it.description }

    fun testGeenLicentieGeenMelding() {
        myFixture.addFileToProject("fout.l", kaal(lees("fout.l")))
        myFixture.configureByText("fout.y", kaal(lees("fout.y")))
        for (s in listOf(LicentieStand.GEEN, LicentieStand.ONBEKEND)) {
            Licentie.zetBronVoorTest { s }
            com.intellij.codeInsight.daemon.DaemonCodeAnalyzer.getInstance(project).restart()
            if (s == LicentieStand.GEEN) assertEquals(emptyList<String>(), meldingen())
            else assertTrue(meldingen().contains("Unused rule 'los'"))
        }
    }

    /** Een grammatica zonder scanner geeft geen tokenmeldingen, wel regelmeldingen. */
    fun testZonderScannerGeenTokens() {
        myFixture.configureByText("los.y", "%token A B\n%%\ns: A ;\nweg: s ;\n")
        assertEquals(listOf("Unused rule 'weg'"), meldingen())
    }

    /** Verzamelt alle meldingen van de vier inspecties op een bestand als "map/bestand naam soort". */
    private fun alle(pad: String): List<String> {
        val f = myFixture.psiManager.findFile(myFixture.findFileInTempDir(pad))!!
        val m = InspectionManager.getInstance(project)
        return inspecties.flatMap { i: MeldingInspectie ->
            (i.checkFile(f, m, false) ?: emptyArray()).map { "$pad ${it.psiElement.text} ${it.descriptionTemplate.substringBefore(" '")}" }
        }
    }

    private val echt = mapOf(
        "jq" to listOf("jq-parser.y", "jq-lexer.l"),
        "pg-boot" to listOf("pg-bootparse.y", "pg-bootscanner.l"),
        "pg-gram" to listOf("pg-gram.y", "pg-scan.l"),
        "thrift" to listOf("thrift-thrifty.yy", "thrift-thriftl.ll"),
        "openbsd" to listOf("openbsd-httpd-parse.y"),
        "ruby" to listOf("ruby-parse.y"),
    )

    /** De nultest: elke melding op de echte bestanden staat met bewijs in meldingen-echt.txt, en omgekeerd. */
    fun testEchteBestanden() {
        for ((map, namen) in echt) for (n in namen) myFixture.addFileToProject("$map/$n", File(data, n).readText())
        val gevonden = echt.flatMap { (map, namen) -> namen.flatMap { alle("$map/$it") } }.sorted()
        val verwacht = File(data, "verwacht/meldingen-echt.txt").readLines()
            .filter { it.isNotBlank() && !it.startsWith("#") }.map { it.substringBefore(" |").trim() }.sorted()
        assertEquals(verwacht.joinToString("\n"), gevonden.joinToString("\n"))
    }

    /** De vier rekenmachines: nul meldingen. */
    fun testRekenmachines() {
        for (map in listOf("e2e/project", "e2e/calculator")) {
            val d = File(data.parentFile, map)
            for (n in listOf("calc.y", "calc.l", "calc.yy", "calc.ll")) myFixture.addFileToProject("$map/$n", File(d, n).readText())
        }
        val gevonden = listOf("e2e/project", "e2e/calculator").flatMap { m -> listOf("calc.y", "calc.l", "calc.yy", "calc.ll").flatMap { alle("$m/$it") } }
        assertEquals("", gevonden.joinToString("\n"))
    }
}
