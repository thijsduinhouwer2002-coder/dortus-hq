package com.dortus.bisonflex

import com.intellij.icons.AllIcons
import com.intellij.ide.structureView.StructureViewTreeElement
import com.intellij.ide.structureView.TreeBasedStructureViewBuilder
import com.intellij.lang.folding.LanguageFolding
import com.intellij.lang.folding.FoldingDescriptor
import com.intellij.lang.LanguageStructureViewBuilder
import com.intellij.openapi.editor.Document
import com.intellij.psi.PsiElement
import com.intellij.psi.PsiFile
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File
import javax.swing.Icon

/** Eis 4 (folding en structuurweergave): vaste uitvoer voor de rekenmachine, en geen fouten op de 10 echte bestanden. */
class StructuurTest : BasePlatformTestCase() {

    private val testdata get() = File(System.getProperty("dortus.testdata"))
    private val verwachtMap get() = File(testdata, "verwacht")

    private fun open(naam: String, tekst: String): PsiFile = myFixture.configureByText(naam, tekst)
    private fun document(): Document = myFixture.editor.document

    private fun folding(f: PsiFile, d: Document): List<FoldingDescriptor> {
        val bouwer = LanguageFolding.INSTANCE.forLanguage(f.language)
        assertNotNull("geen folding voor ${f.language.id}", bouwer)
        return LanguageFolding.buildFoldingDescriptors(bouwer, f, d, false).sortedWith(
            compareBy<FoldingDescriptor>({ it.range.startOffset }, { -it.range.endOffset }))
    }

    private fun regel(d: Document, pos: Int) = d.getLineNumber(pos) + 1

    /** Korte vorm: `begin..eind (regel a-b) placeholder`. */
    private fun foldingTekst(d: Document, gebieden: List<FoldingDescriptor>) = gebieden.joinToString("") {
        val r = it.range
        "${r.startOffset}..${r.endOffset} (regel ${regel(d, r.startOffset)}-${regel(d, r.endOffset)}) ${it.placeholderText}\n"
    }

    /** Geldig: niet leeg, binnen het bestand, meer dan één regel, en twee gebieden liggen los of in elkaar. */
    private fun controleer(naam: String, d: Document, gebieden: List<FoldingDescriptor>) {
        for (g in gebieden) {
            val r = g.range
            assertTrue("$naam: leeg $r", r.startOffset < r.endOffset)
            assertTrue("$naam: buiten het bestand $r", r.startOffset >= 0 && r.endOffset <= d.textLength)
            assertTrue("$naam: één regel $r", d.getLineNumber(r.startOffset) < d.getLineNumber(r.endOffset))
            assertFalse("$naam: lege placeholder $r", g.placeholderText.isNullOrEmpty())
        }
        for (i in gebieden.indices) for (j in i + 1 until gebieden.size) {
            val a = gebieden[i].range
            val b = gebieden[j].range
            assertFalse("$naam: dubbel $a", a == b)
            val los = a.endOffset <= b.startOffset || b.endOffset <= a.startOffset
            val inElkaar = a.contains(b) || b.contains(a)
            assertTrue("$naam: $a en $b overlappen half", los || inElkaar)
        }
    }

    // ---- structuurweergave ----

    private fun bovenste(f: PsiFile): StructureViewTreeElement {
        val bouwer = LanguageStructureViewBuilder.getInstance().getStructureViewBuilder(f)
        assertTrue("geen structuurweergave voor ${f.language.id}", bouwer is TreeBasedStructureViewBuilder)
        val model = (bouwer as TreeBasedStructureViewBuilder).createStructureViewModel(null)
        try { return model.root } finally { model.dispose() }
    }

    private val iconen: Map<Icon, String> by lazy {
        AllIcons.Nodes::class.java.fields.mapNotNull { v -> (v.get(null) as? Icon)?.let { it to "Nodes.${v.name}" } }.toMap()
    }

    /** Eigen korte vorm: `naam [plek] (icoon, regel n)`, ingesprongen per niveau. */
    private fun boom(e: StructureViewTreeElement, d: Document, diepte: Int, sb: StringBuilder) {
        val p = e.presentation
        val icoon = p.getIcon(false)
        val naam = iconen[icoon] ?: "EIGEN ICOON $icoon"
        val element = e.value as PsiElement
        assertTrue("niet te navigeren: ${p.presentableText}", e.canNavigate())
        sb.append("  ".repeat(diepte)).append(p.presentableText)
        p.locationString?.let { sb.append(" \"").append(it).append('"') }
        sb.append(" (").append(naam).append(", regel ").append(regel(d, element.textOffset)).append(")\n")
        for (k in e.children) boom(k as StructureViewTreeElement, d, diepte + 1, sb)
    }

    private fun structuurTekst(f: PsiFile, d: Document): String {
        val sb = StringBuilder()
        for (k in bovenste(f).children) boom(k as StructureViewTreeElement, d, 0, sb)
        return sb.toString()
    }

    private fun vergelijk(bestand: String, gekregen: String) {
        val verwacht = File(verwachtMap, bestand)
        if (!verwacht.exists()) { verwacht.writeText(gekregen); fail("$bestand gemaakt, nakijken") }
        assertEquals(bestand, verwacht.readText(), gekregen)
    }

    /** Vaste folding-gebieden voor de rekenmachine (`testdata/verwacht/calc.y.folding` en `calc.l.folding`). */
    fun testFoldingRekenmachine() {
        for (naam in listOf("calc.y", "calc.l")) {
            val f = open(naam, File(testdata, "../e2e/project/$naam").readText())
            val d = document()
            val gebieden = folding(f, d)
            controleer(naam, d, gebieden)
            vergelijk("$naam.folding", foldingTekst(d, gebieden))
        }
    }

    /** Vaste boom van de structuurweergave voor de rekenmachine (`testdata/verwacht/calc.y.structuur` en `calc.l.structuur`). */
    fun testStructuurRekenmachine() {
        for (naam in listOf("calc.y", "calc.l")) {
            val f = open(naam, File(testdata, "../e2e/project/$naam").readText())
            vergelijk("$naam.structuur", structuurTekst(f, document()))
        }
    }

    /** Op de 10 echte bestanden: geen fout, geldige gebieden, en een structuur met regels. */
    fun testEchteBestanden() {
        val bestanden = testdata.listFiles { f -> f.extension in setOf("y", "yy", "l", "ll") }!!.sortedBy { it.name }
        assertEquals(10, bestanden.size)
        for (b in bestanden) {
            val f = open(b.name, b.readText())
            val d = document()
            val gebieden = folding(f, d)
            controleer(b.name, d, gebieden)
            assertTrue("${b.name}: geen folding", gebieden.isNotEmpty())
            val structuur = structuurTekst(f, d)
            assertTrue("${b.name}: geen regels in de structuur\n$structuur", structuur.lines().any { it.startsWith("Rules ") })
            assertFalse("${b.name}: eigen icoon", structuur.contains("EIGEN ICOON"))
            println("DORTUS ${b.name}: ${gebieden.size} folding-gebieden, ${structuur.lines().size - 1} knopen in de structuur")
        }
    }

    /** Kleine gevallen: geen gebied van één regel, `%union` één keer, `<SC>{` met regels eronder. */
    fun testKleineGevallen() {
        val y = "%union {\n  int i;\n}\n%token <i> A B\n%start s\n%%\ns: A { x(); } ;\nt: B\n  { y();\n  }\n  ;\n"
        val f = open("a.y", y)
        assertEquals(
            "0..19 (regel 1-3) %union {…}\n63..84 (regel 8-11) t: …\n70..80 (regel 9-10) {…}\n",
            foldingTekst(document(), folding(f, document())))
        assertEquals(
            "Declarations (Nodes.Folder, regel 1)\n  A \"%token\" (Nodes.Constant, regel 4)\n  B \"%token\" (Nodes.Constant, regel 4)\n" +
                "  s \"%start\" (Nodes.EntryPoints, regel 5)\nRules (Nodes.Folder, regel 7)\n  s (Nodes.Method, regel 7)\n  t (Nodes.Method, regel 8)\n",
            structuurTekst(f, document()))
        val l = "%x STR\n%%\n<STR>{\n\"x\"  { a(); }\n}\n\"y\"  ;\n"
        val g = open("a.l", l)
        assertEquals("10..32 (regel 3-5) <STR>{…}\n", foldingTekst(document(), folding(g, document())))
        assertEquals(
            "Definitions (Nodes.Folder, regel 1)\n  STR \"%x\" (Nodes.Tag, regel 1)\nRules (Nodes.Folder, regel 3)\n" +
                "  <STR> (Nodes.Tag, regel 3)\n    \"x\" (Nodes.Method, regel 4)\n  \"y\" (Nodes.Method, regel 6)\n",
            structuurTekst(g, document()))
    }
}
