package com.dortus.bisonflex

import com.dortus.bisonflex.lexer.BisonScanner
import com.dortus.bisonflex.lexer.FlexScanner
import com.dortus.bisonflex.lexer.bisonLexer
import com.dortus.bisonflex.lexer.flexLexer
import com.intellij.lexer.Lexer
import com.intellij.openapi.editor.colors.TextAttributesKey
import com.intellij.psi.TokenType
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/** Lexer en kleuren: eis 2 (geen fouten op echte bestanden), eis 4 (kleur per token), eis 9 (snelheid). */
class LexerTest : BasePlatformTestCase() {

    private data class Tok(val start: Int, val einde: Int, val type: String, val toestand: Int)

    private fun lex(lexer: Lexer, tekst: CharSequence, van: Int = 0, toestand: Int = 0): List<Tok> {
        val uit = ArrayList<Tok>()
        lexer.start(tekst, van, tekst.length, toestand)
        while (lexer.tokenType != null) {
            uit += Tok(lexer.tokenStart, lexer.tokenEnd, lexer.tokenType.toString(), lexer.state)
            lexer.advance()
        }
        return uit
    }

    private fun isBison(naam: String) = naam.endsWith(".y") || naam.endsWith(".yy")
    private fun lexerVoor(naam: String) = if (isBison(naam)) bisonLexer() else flexLexer()

    private fun echteBestanden(): List<File> {
        val map = File(System.getProperty("dortus.testdata"))
        return map.listFiles { f -> f.extension in setOf("y", "yy", "l", "ll") }!!.sortedBy { it.name }
    }

    private fun plek(tekst: String, pos: Int): String {
        val regel = tekst.substring(0, pos).count { it == '\n' } + 1
        val begin = tekst.lastIndexOf('\n', pos - 1) + 1
        val eind = tekst.indexOf('\n', pos).let { if (it < 0) tekst.length else it }
        return "regel $regel: ${tekst.substring(begin, eind).trim().take(100)}"
    }

    /** De toestand ná het laatste token: zo zien we of alle blokken netjes dicht zijn. */
    private fun eindToestand(lexer: Lexer, tekst: String): Int {
        lexer.start(tekst, 0, tekst.length, 0)
        var laatst = 0
        while (lexer.tokenType != null) { lexer.advance(); laatst = lexer.state }
        return laatst
    }

    fun testEchteBestandenZonderFoutEnAllesDicht() {
        val bestanden = echteBestanden()
        assertEquals(10, bestanden.size)
        val problemen = ArrayList<String>()
        for (f in bestanden) {
            val tekst = f.readText()
            val toks = lex(lexerVoor(f.name), tekst)
            // Aaneengesloten en de hele tekst.
            var pos = 0
            for (t in toks) {
                if (t.start != pos) problemen += "${f.name}: gat bij $pos"
                pos = t.einde
            }
            if (pos != tekst.length) problemen += "${f.name}: stopt bij $pos van ${tekst.length}"
            toks.filter { it.type == TokenType.BAD_CHARACTER.toString() }.forEach {
                problemen += "${f.name}: onbekend teken '${tekst.substring(it.start, it.einde)}' op ${plek(tekst, it.start)}"
            }
            val eind = eindToestand(lexerVoor(f.name), tekst)
            if (isBison(f.name)) {
                if (BisonScanner.deel(eind) == BisonScanner.DECLARATIES || BisonScanner.stand(eind) == BisonScanner.BLOK ||
                    BisonScanner.stand(eind) == BisonScanner.PROLOOG) problemen += "${f.name}: eindigt in toestand $eind"
            } else {
                val stand = FlexScanner.stand(eind)
                if (FlexScanner.deel(eind) == FlexScanner.DEFINITIES || FlexScanner.scope(eind) != 0 ||
                    stand == FlexScanner.PROLOOG || stand == FlexScanner.TOP || FlexScanner.diepte(eind) != 0)
                    problemen += "${f.name}: eindigt in toestand $eind (deel ${FlexScanner.deel(eind)}, stand $stand, " +
                        "scope ${FlexScanner.scope(eind)}, diepte ${FlexScanner.diepte(eind)})"
            }
        }
        assertTrue(problemen.joinToString("\n"), problemen.isEmpty())
    }

    /** De IDE begint na een wijziging opnieuw bij een token met zijn toestand; dat moet hetzelfde geven. */
    fun testOpnieuwBeginnenMiddenInGeeftHetzelfde() {
        for (f in echteBestanden()) {
            val tekst = f.readText()
            val heel = lex(lexerVoor(f.name), tekst)
            val stap = maxOf(1, heel.size / 40)
            for (i in 1 until heel.size step stap) {
                // Tok.toestand is de toestand aan het begin van dat token.
                val deel = lex(lexerVoor(f.name), tekst, heel[i].start, heel[i].toestand)
                assertEquals("${f.name}: opnieuw beginnen bij token $i (${plek(tekst, heel[i].start)})",
                    heel.subList(i, heel.size).map { Triple(it.start, it.einde, it.type) },
                    deel.map { Triple(it.start, it.einde, it.type) })
            }
        }
    }

    private fun kleurenlijst(naam: String, tekst: String): String {
        val hl = if (isBison(naam)) bisonHighlighter() else flexHighlighter()
        val lexer = hl.highlightingLexer
        lexer.start(tekst, 0, tekst.length, 0)
        val sb = StringBuilder()
        while (lexer.tokenType != null) {
            val keys: Array<TextAttributesKey> = hl.getTokenHighlights(lexer.tokenType)
            val stuk = tekst.substring(lexer.tokenStart, lexer.tokenEnd)
            if (stuk.isNotBlank()) sb.append(stuk.replace("\n", "\\n")).append(" -> ")
                .append(keys.joinToString(",") { it.externalName }.ifEmpty { "-" }).append('\n')
            lexer.advance()
        }
        return sb.toString()
    }

    /** Eis 4 (kleuren): vaste verwachte kleur per token voor de rekenmachine. */
    fun testKleurPerTokenRekenmachine() {
        val verwachtMap = File(System.getProperty("dortus.testdata"), "verwacht")
        for (naam in listOf("calc.y", "calc.l")) {
            val tekst = File(System.getProperty("dortus.testdata"), "../e2e/project/$naam").readText()
            val gekregen = kleurenlijst(naam, tekst)
            val verwacht = File(verwachtMap, "$naam.kleuren")
            if (!verwacht.exists()) { verwacht.parentFile.mkdirs(); verwacht.writeText(gekregen); fail("${verwacht.name} gemaakt, nakijken") }
            assertEquals("kleuren van $naam", verwacht.readText(), gekregen)
        }
    }

    /** Elke kleur valt terug op een standaardkleur van de IDE en heeft zelf geen vaste kleur. */
    fun testGeenVasteKleuren() {
        for (sleutels in listOf(BisonKleuren.SLEUTELS, FlexKleuren.SLEUTELS)) {
            val velden = sleutels.javaClass.declaredFields.filter { TextAttributesKey::class.java.isAssignableFrom(it.type) }
            assertTrue(velden.size >= 20)
            for (v in velden) {
                v.isAccessible = true
                val k = v.get(sleutels) as TextAttributesKey
                val terug = k.fallbackAttributeKey
                assertNotNull("${k.externalName} valt terug op een standaardkleur", terug)
                assertTrue("${k.externalName} valt terug op ${terug!!.externalName}", terug.externalName.startsWith("DEFAULT_"))
            }
        }
        // En nergens in de code een eigen kleur.
        val bron = File(System.getProperty("dortus.testdata"), "../src/main/kotlin").walk().filter { it.isFile }
        for (f in bron) {
            val t = f.readText()
            for (verboden in listOf("TextAttributes(", "JBColor", "java.awt.Color", "Color("))
                assertFalse("${f.name} bevat $verboden", t.contains(verboden))
        }
    }

    fun testVoorbeeldenOpDeKleurenpaginaZonderFout() {
        for ((naam, tekst) in listOf("demo.y" to Voorbeelden.BISON, "demo.l" to Voorbeelden.FLEX)) {
            val fout = lex(lexerVoor(naam), tekst).filter { it.type == TokenType.BAD_CHARACTER.toString() }
            assertTrue("$naam: ${fout.map { plek(tekst, it.start) }}", fout.isEmpty())
        }
        assertEquals("Bison/Yacc", BisonKleurenPagina().displayName)
        assertTrue(BisonKleurenPagina().attributeDescriptors.size >= 18)
        assertTrue(FlexKleurenPagina().attributeDescriptors.size >= 20)
    }

    /** Eis 9 (lexer-deel): 5.000 regels in onder 1 seconde. */
    fun testSnelGenoeg() {
        val y = File(System.getProperty("dortus.testdata"), "pg-gram.y").readLines().take(5000).joinToString("\n")
        val l = File(System.getProperty("dortus.testdata"), "pg-scan.l").readText().repeat(4).lines().take(5000).joinToString("\n")
        lex(bisonLexer(), y); lex(flexLexer(), l) // opwarmen
        val t0 = System.nanoTime()
        lex(bisonLexer(), y); lex(flexLexer(), l)
        val ms = (System.nanoTime() - t0) / 1_000_000
        println("DORTUS lexer: 2 x 5000 regels in $ms ms")
        assertTrue("te traag: $ms ms", ms < 1000)
    }
}
