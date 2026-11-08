package com.dortus.bisonflex

import com.intellij.lang.ASTNode
import com.intellij.openapi.fileTypes.FileType
import com.intellij.psi.PsiErrorElement
import com.intellij.psi.PsiFile
import com.intellij.psi.PsiFileFactory
import com.intellij.psi.TokenType
import com.intellij.psi.util.PsiTreeUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/** Parser: eis 2 (geen fouten op echte bestanden), eis 3 (fout op de juiste plek), eis 9 (snelheid). */
class ParserTest : BasePlatformTestCase() {

    private val testdata get() = File(System.getProperty("dortus.testdata"))

    private fun isBison(naam: String) = naam.endsWith(".y") || naam.endsWith(".yy")
    private fun soort(naam: String): FileType = if (isBison(naam)) BisonFileType else FlexFileType

    private fun parse(naam: String, tekst: String): PsiFile =
        PsiFileFactory.getInstance(project).createFileFromText(naam, soort(naam), tekst)

    private fun fouten(f: PsiFile): List<PsiErrorElement> =
        PsiTreeUtil.collectElementsOfType(f, PsiErrorElement::class.java).sortedBy { it.textOffset }

    private fun regelVan(tekst: String, pos: Int) = tekst.substring(0, pos.coerceAtMost(tekst.length)).count { it == '\n' } + 1

    private fun plek(tekst: String, pos: Int): String {
        val p = pos.coerceAtMost(tekst.length)
        val begin = tekst.lastIndexOf('\n', p - 1) + 1
        val eind = tekst.indexOf('\n', p).let { if (it < 0) tekst.length else it }
        return "regel ${regelVan(tekst, p)}: ${tekst.substring(begin, eind).trim().take(100)}"
    }

    /** Korte vorm van de fouten: `tekst @ offset (regel n)`. */
    private fun foutlijst(tekst: String, f: PsiFile) =
        fouten(f).map { "${it.errorDescription} @ ${it.textOffset} (regel ${regelVan(tekst, it.textOffset)})" }

    private fun zonderFouten(naam: String, tekst: String): String? {
        val e = fouten(parse(naam, tekst)).firstOrNull() ?: return null
        return "$naam: ${e.errorDescription} op ${plek(tekst, e.textOffset)}"
    }

    /** Eis 2: de 10 echte bestanden, de rekenmachine en de voorbeelden geven geen enkele fout. */
    fun testGeenFoutenOpEchteBestanden() {
        val bestanden = testdata.listFiles { f -> f.extension in setOf("y", "yy", "l", "ll") }!!.sortedBy { it.name }
        assertEquals(10, bestanden.size)
        val gevallen = bestanden.map { it.name to it.readText() } +
            File(testdata, "../e2e/project").listFiles()!!.filter { it.extension in setOf("y", "yy", "l", "ll") }
                .sortedBy { it.name }.map { "e2e/${it.name}" to it.readText() } +
            listOf("voorbeeld.y" to Voorbeelden.BISON, "voorbeeld.l" to Voorbeelden.FLEX)
        assertEquals(16, gevallen.size)
        val problemen = gevallen.mapNotNull { (naam, tekst) -> zonderFouten(naam, tekst) }
        assertTrue(problemen.joinToString("\n"), problemen.isEmpty())
        // En er is echt een boom: elke regelnaam van de lexer is een RULE, en Flex heeft regels.
        for ((naam, tekst) in gevallen) {
            val f = parse(naam, tekst)
            if (isBison(naam)) {
                val namen = typesIn(f, "BISON_DEFINITIE").size
                assertTrue("$naam: geen regels", namen > 0)
                assertEquals("$naam: regels", namen, typesIn(f, "RULE").size)
            } else assertTrue("$naam: geen regels", typesIn(f, "FLEX_RULE").isNotEmpty())
        }
    }

    // ---- vaste boom ----

    private val codeKnopen = setOf("PROLOGUE", "CODE_BLOCK", "ACTION", "EPILOGUE", "USER_CODE", "CODE", "TOP_BLOCK")

    /** Eigen korte vorm: knopen ingesprongen, tokens met tekst; codeblokken als één regel. */
    private fun boom(n: ASTNode, diepte: Int, sb: StringBuilder) {
        val type = n.elementType
        if (type == TokenType.WHITE_SPACE) return
        val inspring = "  ".repeat(diepte)
        val kort = n.text.replace("\n", "\\n").let { if (it.length > 60) it.take(57) + "..." else it }
        when {
            n.firstChildNode == null -> sb.append(inspring).append(type).append(" '").append(kort).append("'\n")
            type.toString() in codeKnopen -> sb.append(inspring).append(type).append(" '").append(kort).append("'\n")
            else -> {
                sb.append(inspring).append(type).append('\n')
                var c = n.firstChildNode
                while (c != null) { boom(c, diepte + 1, sb); c = c.treeNext }
            }
        }
    }

    /** Eis 2 en 4: vaste boom voor de rekenmachine (`testdata/verwacht/calc.y.boom` en `calc.l.boom`). */
    fun testBoomRekenmachine() {
        val verwachtMap = File(testdata, "verwacht")
        for (naam in listOf("calc.y", "calc.l")) {
            val tekst = File(testdata, "../e2e/project/$naam").readText()
            val sb = StringBuilder()
            boom(parse(naam, tekst).node, 0, sb)
            val gekregen = sb.toString()
            val verwacht = File(verwachtMap, "$naam.boom")
            if (!verwacht.exists()) { verwacht.writeText(gekregen); fail("${verwacht.name} gemaakt, nakijken") }
            assertEquals("boom van $naam", verwacht.readText(), gekregen)
        }
    }

    // ---- eis 3: fouten op de juiste plek, en daarna weer goed lezen ----
    // Een fout "x expected" staat zoals gewoon in de IDE direct achter het laatste goede token
    // (voor de witruimte). Aan het eind van het bestand is dat dus `tekst.trimEnd().length`.

    /** Tekst van alle knopen (ook tokens) van [type], in volgorde van het bestand. */
    private fun typesIn(f: PsiFile, type: String): List<String> {
        val uit = ArrayList<String>()
        fun loop(n: ASTNode) {
            if (n.elementType.toString() == type) uit += n.text
            var c = n.firstChildNode
            while (c != null) { loop(c); c = c.treeNext }
        }
        loop(f.node)
        return uit
    }

    /** `;` mag weg voor een nieuwe regel of `%%` (zoals Bison), maar niet voor iets anders. */
    fun testBisonRegelZonderPuntkomma() {
        val goed = "%token NUM\n%%\nexp: NUM\n| exp '+' exp\n%%\n"
        assertEquals(emptyList<String>(), foutlijst(goed, parse("a.y", goed)))
        val ookGoed = "%token NUM\n%%\nexp: NUM\nline: exp\n"
        assertEquals(emptyList<String>(), foutlijst(ookGoed, parse("a.y", ookGoed)))
        val fout = "%token NUM NUM2\n%%\nexp: NUM NUM2 ) foo\n;\nline: exp ;\n"
        val f = parse("a.y", fout)
        assertEquals(listOf("'|' or ';' expected, got ')' @ ${fout.indexOf(')')} (regel 3)"), foutlijst(fout, f))
        // Herstel: de volgende regel is weer gewoon gelezen.
        assertEquals(listOf("exp", "line"), typesIn(f, "RULE_NAME"))
        assertEquals("line: exp ;", typesIn(f, "RULE").last())
    }

    /**
     * Bison `parse-gram.y`: `rhses.1: rhs | rhses.1 "|" rhs | rhses.1 ";"`. Na `;` mag dus nog `|`
     * met een alternatief van dezelfde regel komen, en `;;` mag ook.
     */
    fun testBisonPuntkommaDanStreep() {
        val t = "%token b c d\n%%\na: b ; | c ;\ne: a ;; | d ;;\nf: a ;;\n"
        val f = parse("a.y", t)
        assertEquals(emptyList<String>(), foutlijst(t, f))
        assertEquals(listOf("a", "e", "f"), typesIn(f, "RULE_NAME"))
        assertEquals(3, typesIn(f, "RULE").size)
        // Het alternatief na `; |` hoort onder ALTERNATIVES van dezelfde regel, net als een gewoon `|`.
        assertEquals(listOf("b ; | c", "a ;; | d", "a"), typesIn(f, "ALTERNATIVES"))
        assertEquals(listOf("b", "c", "a", "d", "a"), typesIn(f, "ALTERNATIVE"))
    }

    /** Geneste C++-typetags (controleur 7 nov): geen valse fout, de hele tag is een TYPE. */
    fun testBisonGenesteTypetag() {
        val t = "%define api.value.type variant\n%type <std::vector<int>> lst\n%nterm <std::map<int,std::string>> m\n%%\nlst: %empty ;\nm: %empty ;\n"
        assertEquals(emptyList<String>(), foutlijst(t, parse("a.yy", t)))
        val open = "%type <std::vector<int> lst\n%%\nlst: %empty ;\n"
        assertFalse(foutlijst(open, parse("a.yy", open)).isEmpty())
    }

    fun testBisonOpenProloog() {
        val t = "%{\nint x;\n%%\nexp: NUM ;\n"
        assertEquals(listOf("'%}' expected @ ${t.trimEnd().length} (regel 4)"), foutlijst(t, parse("a.y", t)))
    }

    fun testBisonRegelZonderDubbelePunt() {
        val t = "%token NUM\n%%\nexp NUM | exp '+' exp ;\nline: exp ;\n"
        val f = parse("a.y", t)
        assertEquals(listOf("':' expected @ ${t.indexOf("exp NUM") + 3} (regel 3)"), foutlijst(t, f))
        assertEquals(listOf("exp", "line"), typesIn(f, "RULE_NAME"))
        assertEquals(2, typesIn(f, "ALTERNATIVES").first().split('|').size)
    }

    fun testBisonOpenActie() {
        val t = "%%\nexp: NUM { $$ = 1;\nline: exp ;\n"
        assertEquals(listOf("'}' expected @ ${t.trimEnd().length} (regel 3)"), foutlijst(t, parse("a.y", t)))
    }

    fun testFlexScBlokZonderSluiting() {
        val t = "%x SC\n%%\n<SC>{\n\"a\" ;\n%%\nint x;\n"
        val f = parse("a.l", t)
        // Op de plek waar de `}` had moeten staan: direct voor de `%%`, achter `"a" ;`.
        assertEquals(listOf("'}' expected @ ${t.indexOf(";\n%%") + 1} (regel 4)"), foutlijst(t, f))
        assertEquals("int x;", typesIn(f, "USER_CODE").single())
    }

    fun testFlexOpenActie() {
        val t = "%%\n\"a\"   { return 1;\n\"b\"   { return 2; }\n%%\n"
        // De lexer leest na een open `{` alles als C (zoals Flex zelf), dus de fout staat aan het eind.
        assertEquals(listOf("'}' expected @ ${t.trimEnd().length} (regel 4)"), foutlijst(t, parse("a.l", t)))
    }

    fun testFlexOpenProloogEnGeenScheiding() {
        val t = "%{\nint x;\n"
        assertEquals(listOf("'%}' expected @ ${t.trimEnd().length} (regel 2)"), foutlijst(t, parse("a.l", t)))
        val zonder = "DIGIT [0-9]\n"
        assertEquals(listOf("'%%' expected @ ${zonder.trimEnd().length} (regel 1)"), foutlijst(zonder, parse("a.l", zonder)))
    }

    /** Eis 9 (parser-deel): 5.000 regels lexen en parsen in onder 1 seconde (ruim: 2 seconden hier). */
    fun testSnelGenoeg() {
        val y = File(testdata, "pg-gram.y").readLines().take(5000).joinToString("\n")
        val l = File(testdata, "pg-scan.l").readText().repeat(4).lines().take(5000).joinToString("\n")
        fun eenKeer() { fouten(parse("a.y", y)); fouten(parse("a.l", l)) }
        eenKeer() // opwarmen
        val t0 = System.nanoTime()
        eenKeer()
        val ms = (System.nanoTime() - t0) / 1_000_000
        println("DORTUS parser: 2 x 5000 regels gelext en geparsed in $ms ms")
        assertTrue("te traag: $ms ms", ms < 2000)
    }
}
