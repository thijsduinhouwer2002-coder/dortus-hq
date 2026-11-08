package com.dortus.bisonflex.meldingen

import com.dortus.bisonflex.FlexFileType
import com.dortus.bisonflex.parser.BisonElementen as B
import com.dortus.bisonflex.parser.FlexElementen as F
import com.dortus.bisonflex.pro.Licentie
import com.dortus.bisonflex.psi.Koppeling
import com.intellij.codeInspection.InspectionManager
import com.intellij.codeInspection.LocalInspectionTool
import com.intellij.codeInspection.ProblemDescriptor
import com.intellij.codeInspection.ProblemHighlightType
import com.intellij.lang.ASTNode
import com.intellij.openapi.project.DumbService
import com.intellij.psi.PsiFile
import com.intellij.psi.PsiManager
import com.intellij.psi.TokenType
import com.intellij.psi.search.FileTypeIndex
import com.intellij.psi.search.GlobalSearchScope

/**
 * Eis 7: ongedefinieerde en ongebruikte namen (ontwerp.md, "Ontwerp eis 7"). Vier inspecties, alleen met Pro
 * ([Licentie.proWerkt]); bij stand GEEN geven ze niets terug, ook geen Pro-melding (geen nag).
 */
object Analyse {
    /** Namen die nooit ongedefinieerd zijn. */
    val VAST = setOf("error", "\$accept", "\$end", "\$undefined", "YYEOF", "YYerror", "YYUNDEF")

    /** Waar een `SYMBOL_REF` meetelt als verwijzing (ongedefinieerd). */
    private fun telt(ref: ASTNode): Boolean = when (ref.treeParent?.elementType) {
        B.ALTERNATIVE, B.PREC, B.TYPE_DECL, B.NTERM_DECL, B.START -> true
        B.DIRECTIVE -> ref.treeParent.firstChildNode?.text in setOf("%destructor", "%printer")
        else -> false
    }

    fun bisonOngedefinieerd(f: PsiFile): List<ASTNode> =
        Koppeling.zoek(f.node, setOf(B.SYMBOL_REF)).filter {
            telt(it) && it.text !in VAST && Koppeling.bisonDoel(f, it.text) == null
        }

    /** Namen die in het regeldeel gebruikt worden (in een alternatief of `%prec`). */
    private fun inRegels(f: PsiFile): Set<String> =
        Koppeling.zoek(f.node, setOf(B.SYMBOL_REF))
            .filter { it.treeParent?.elementType == B.ALTERNATIVE || it.treeParent?.elementType == B.PREC }
            .map { it.text }.toSet()

    fun startSymbool(f: PsiFile): String? =
        Koppeling.zoek(f.node, setOf(B.START)).firstNotNullOfOrNull { s ->
            Koppeling.zoek(s, setOf(B.SYMBOL_REF)).firstOrNull()?.text
        } ?: Koppeling.zoek(f.node, setOf(B.RULE_NAME)).firstOrNull()?.text

    fun ongebruikteRegels(f: PsiFile): List<ASTNode> {
        val gebruikt = inRegels(f)
        val start = startSymbool(f)
        return Koppeling.bison(f).regels.filter { (n, _) -> n !in gebruikt && n != start }
            .mapNotNull { it.value.firstOrNull()?.node }
    }

    /** Het volgende blad dat geen witruimte of commentaar is. */
    private fun volgende(n: ASTNode): ASTNode? {
        var k = n.treeNext
        while (k != null && (k.elementType == TokenType.WHITE_SPACE || k.text.isBlank() || k.text.startsWith("/*") || k.text.startsWith("//"))) k = k.treeNext
        return k
    }

    /** `RUBY_TOKEN(UPLUS)`: een naam direct gevolgd door `(` is een macro, geen token. */
    fun isMacro(n: ASTNode): Boolean =
        n.treeNext?.text?.startsWith("(") == true || n.treePrev?.text?.endsWith("(") == true

    /** Of een declaratie van dit token een tekstnaam heeft (`%token NUM "number"`). */
    private fun heeftTekstnaam(n: ASTNode): Boolean {
        var k = volgende(n)
        if (k != null && k.text.all { it.isDigit() || it == 'x' || it in 'a'..'f' || it in 'A'..'F' } && k.text.first().isDigit()) k = volgende(k)
        return k?.text?.startsWith("\"") == true
    }

    /** `%define api.token.prefix` of `api.token.constructor`: de scanner geeft andere namen terug. */
    fun andereNamen(f: PsiFile): Boolean = Koppeling.zoek(f.node, setOf(B.DEFINE)).any { d ->
        val t = d.text
        "api.token.prefix" in t || "api.token.constructor" in t
    }

    /** Of er een scanner bij deze grammatica hoort (dezelfde regel als ga naar definitie). */
    fun heeftScanner(f: PsiFile): Boolean {
        val project = f.project
        val psi = PsiManager.getInstance(project)
        val eigen = f.originalFile
        return FileTypeIndex.getFiles(FlexFileType, GlobalSearchScope.projectScope(project))
            .mapNotNull { psi.findFile(it) }
            .any { s -> Koppeling.grammaticas(s) { true }.any { it.originalFile == eigen || it == f } }
    }

    fun ongebruikteTokens(f: PsiFile): List<ASTNode> {
        if (DumbService.isDumb(f.project)) return emptyList()
        if (andereNamen(f)) return emptyList()
        val tokens = Koppeling.bison(f).tokens.mapValues { (_, l) -> l.map { it.node }.filter { !isMacro(it) } }
            .filterValues { it.isNotEmpty() }
        if (tokens.isEmpty()) return emptyList()
        val gebruikt = inRegels(f)
        val inCode = HashSet<String>()
        for (c in Koppeling.zoek(f.node, Koppeling.BISON_CODE)) Koppeling.bladeren(c).forEach { inCode += it.text }
        for (c in Koppeling.zoek(f.node, Koppeling.BISON_CODE)) Regex("[A-Za-z_][A-Za-z0-9_]*").findAll(c.text).forEach { inCode += it.value }
        val kandidaten = tokens.filter { (n, l) -> n !in gebruikt && n !in inCode && n !in VAST && l.none { heeftTekstnaam(it) } }
        if (kandidaten.isEmpty() || !heeftScanner(f)) return emptyList()
        return kandidaten.mapNotNull { (_, l) ->
            val eerste = l.first()
            if (Koppeling.scannerGebruik(eerste.psi) == Koppeling.ScannerGebruik.Nee) eerste else null
        }
    }

    fun flexOngedefinieerd(f: PsiFile): List<ASTNode> {
        val c = Koppeling.flex(f).condities
        return Koppeling.zoek(f.node, setOf(F.START_CONDITION_REF))
            .filter { it.text != "INITIAL" && it.text != "*" && it.text !in c }
    }

    fun flexOngebruikt(f: PsiFile): List<ASTNode> {
        val n = Koppeling.flex(f)
        val refs = Koppeling.zoek(f.node, setOf(F.START_CONDITION_REF)).map { it.text }.toSet()
        return n.condities.filter { (k, _) -> k !in refs && k !in n.inActies }.mapNotNull { it.value.firstOrNull()?.node }
    }
}

/** Gedeelde basis: alleen met Pro, een melding per knoop. */
abstract class MeldingInspectie : LocalInspectionTool() {
    abstract fun vind(f: PsiFile): List<ASTNode>
    abstract fun tekst(naam: String): String
    abstract val soort: ProblemHighlightType
    open fun oplossing(n: ASTNode): com.intellij.codeInspection.LocalQuickFix? = null

    override fun checkFile(file: PsiFile, manager: InspectionManager, isOnTheFly: Boolean): Array<ProblemDescriptor>? {
        if (!Licentie.proWerkt()) return null
        return vind(file).map { n ->
            val fixes = listOfNotNull(oplossing(n)).toTypedArray()
            manager.createProblemDescriptor(n.psi, tekst(n.text), isOnTheFly, fixes, soort)
        }.toTypedArray()
    }
}

class BisonOngedefinieerd : MeldingInspectie() {
    override fun vind(f: PsiFile) = Analyse.bisonOngedefinieerd(f)
    override fun tekst(naam: String) = "Undefined symbol '$naam'"
    override val soort = ProblemHighlightType.WARNING
}

class BisonOngebruikt : MeldingInspectie() {
    override fun vind(f: PsiFile) = (Analyse.ongebruikteRegels(f) + Analyse.ongebruikteTokens(f)).sortedBy { it.startOffset }
    override fun tekst(naam: String) = "Unused symbol '$naam'"
    override val soort = ProblemHighlightType.LIKE_UNUSED_SYMBOL
    override fun oplossing(n: ASTNode) = if (n.elementType == B.RULE_NAME) WeghalenRegel(n.text) else WeghalenNaam(n.text, "token")
    override fun checkFile(file: PsiFile, manager: InspectionManager, isOnTheFly: Boolean): Array<ProblemDescriptor>? {
        if (!Licentie.proWerkt()) return null
        val regels = Analyse.ongebruikteRegels(file)
        return (regels.map { it to "Unused rule '${it.text}'" } + Analyse.ongebruikteTokens(file).map { it to "Unused token '${it.text}'" })
            .sortedBy { it.first.startOffset }
            .map { (n, t) -> manager.createProblemDescriptor(n.psi, t, isOnTheFly, arrayOf(oplossing(n)), soort) }
            .toTypedArray()
    }
}

class FlexOngedefinieerd : MeldingInspectie() {
    override fun vind(f: PsiFile) = Analyse.flexOngedefinieerd(f)
    override fun tekst(naam: String) = "Undefined start condition '$naam'"
    override val soort = ProblemHighlightType.WARNING
}

class FlexOngebruikt : MeldingInspectie() {
    override fun vind(f: PsiFile) = Analyse.flexOngebruikt(f)
    override fun tekst(naam: String) = "Unused start condition '$naam'"
    override val soort = ProblemHighlightType.LIKE_UNUSED_SYMBOL
    override fun oplossing(n: ASTNode) = WeghalenNaam(n.text, "start condition")
}
