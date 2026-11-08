package com.dortus.bisonflex.meldingen

import com.dortus.bisonflex.parser.BisonElementen as B
import com.dortus.bisonflex.parser.FlexElementen as F
import com.dortus.bisonflex.lexer.BisonTokens
import com.dortus.bisonflex.lexer.Soort
import com.dortus.bisonflex.psi.Koppeling
import com.intellij.codeInspection.LocalQuickFix
import com.intellij.codeInspection.ProblemDescriptor
import com.intellij.openapi.project.Project
import com.intellij.openapi.util.TextRange
import com.intellij.psi.PsiDocumentManager
import com.intellij.psi.PsiFile

/** Snelle oplossingen (Alt+Enter) op ongebruikt, eis 7. Werken op de tekst van het document, in één stap. */
private val DECL_MET_NAMEN = setOf(B.TOKEN_DECL, B.LEFT, B.RIGHT, B.NONASSOC, B.PRECEDENCE, B.TYPE_DECL, B.NTERM_DECL, B.DIRECTIVE, F.START_CONDITION_DECL)

/** Haalt de stukken weg, van achter naar voren. */
private fun weg(project: Project, f: PsiFile, stukken: List<TextRange>) {
    val pdm = PsiDocumentManager.getInstance(project)
    val doc = pdm.getDocument(f) ?: return
    for (r in stukken.distinct().sortedByDescending { it.startOffset }) doc.deleteString(r.startOffset, r.endOffset)
    pdm.commitDocument(doc)
}

/** Een hele regel tot en met het regeleinde, als er alleen witruimte achter staat. */
private fun metRegeleinde(tekst: CharSequence, r: TextRange): TextRange {
    var eind = r.endOffset
    while (eind < tekst.length && (tekst[eind] == ' ' || tekst[eind] == '\t')) eind++
    if (eind < tekst.length && tekst[eind] == '\n') eind++
    return TextRange(r.startOffset, eind)
}

/** Een naam uit een declaratie (met zijn nummer en de spatie ervoor), of de hele declaratie als er niets overblijft. */
private fun uitDeclaraties(f: PsiFile, naam: String, soorten: Set<com.intellij.psi.tree.IElementType>): List<TextRange> {
    val tekst = f.text
    val uit = ArrayList<TextRange>()
    for (d in Koppeling.zoek(f.node, DECL_MET_NAMEN)) {
        if (d.elementType == B.DIRECTIVE && d.firstChildNode?.text !in setOf("%destructor", "%printer")) continue
        val namen = Koppeling.zoek(d, soorten)
        val raak = namen.filter { it.text == naam }
        if (raak.isEmpty()) continue
        // Een teken als '+' in %left houdt de declaratie in leven: dat is ook een token met voorrang.
        val tekens = Koppeling.bladeren(d).any { BisonTokens.TYPES.soort(it.elementType) == Soort.TEKEN }
        if (raak.size == namen.size && d.elementType != B.DIRECTIVE && !tekens) { uit += metRegeleinde(tekst, d.textRange); continue }
        for (n in raak) {
            var begin = n.startOffset
            while (begin > 0 && (tekst[begin - 1] == ' ' || tekst[begin - 1] == '\t')) begin--
            var eind = n.textRange.endOffset
            val nummer = Regex("^\\s+(0x[0-9A-Fa-f]+|[0-9]+)").find(tekst.substring(eind))
            if (nummer != null) eind += nummer.value.length
            uit += TextRange(begin, eind)
        }
    }
    return uit
}

class WeghalenRegel(private val naam: String) : LocalQuickFix {
    override fun getFamilyName() = "Remove unused rule"
    override fun getName() = "Remove unused rule '$naam'"
    override fun applyFix(project: Project, descriptor: ProblemDescriptor) {
        val f = descriptor.psiElement?.containingFile ?: return
        val tekst = f.text
        val stukken = ArrayList<TextRange>()
        for (r in Koppeling.zoek(f.node, setOf(B.RULE))) {
            if (Koppeling.zoek(r, setOf(B.RULE_NAME)).firstOrNull()?.text != naam) continue
            var s = metRegeleinde(tekst, r.textRange)
            // de lege regel erna ook
            val na = metRegeleinde(tekst, TextRange(s.endOffset, s.endOffset))
            if (na.endOffset > s.endOffset && tekst.substring(s.endOffset, na.endOffset).isBlank()) s = TextRange(s.startOffset, na.endOffset)
            stukken += s
        }
        stukken += uitDeclaraties(f, naam, setOf(B.SYMBOL_REF))
        weg(project, f, stukken)
    }
}

class WeghalenNaam(private val naam: String, private val wat: String) : LocalQuickFix {
    override fun getFamilyName() = "Remove unused $wat"
    override fun getName() = "Remove unused $wat '$naam'"
    override fun applyFix(project: Project, descriptor: ProblemDescriptor) {
        val f = descriptor.psiElement?.containingFile ?: return
        val soorten = if (wat == "token") setOf(B.TOKEN_NAME, B.SYMBOL_REF) else setOf(F.START_CONDITION_NAME)
        weg(project, f, uitDeclaraties(f, naam, soorten))
    }
}
