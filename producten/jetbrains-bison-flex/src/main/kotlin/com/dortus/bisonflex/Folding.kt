package com.dortus.bisonflex

import com.dortus.bisonflex.lexer.BisonTokens
import com.dortus.bisonflex.lexer.FlexTokens
import com.dortus.bisonflex.lexer.Soort
import com.dortus.bisonflex.lexer.TokenTypes
import com.dortus.bisonflex.parser.BisonElementen as B
import com.dortus.bisonflex.parser.FlexElementen as F
import com.intellij.lang.ASTNode
import com.intellij.lang.folding.FoldingBuilderEx
import com.intellij.lang.folding.FoldingDescriptor
import com.intellij.openapi.editor.Document
import com.intellij.openapi.project.DumbAware
import com.intellij.openapi.util.TextRange
import com.intellij.psi.PsiElement

/**
 * Folding per taal, alleen op de boom van de parser (dus ook tijdens indexeren: [DumbAware]).
 * Alleen gebieden die over meer dan één regel lopen. Geneste gebieden mogen (een actie in een regel).
 */
abstract class TaalFolding(private val types: TokenTypes) : FoldingBuilderEx(), DumbAware {

    /** Placeholder voor [node], of null als deze knoop niet vouwt. */
    protected abstract fun placeholder(node: ASTNode): String?

    override fun buildFoldRegions(root: PsiElement, document: Document, quick: Boolean): Array<FoldingDescriptor> {
        val uit = ArrayList<FoldingDescriptor>()
        val tekst = document.charsSequence
        fun loop(n: ASTNode) {
            val p = if (types.soort(n.elementType) == Soort.BLOKCOMMENTAAR) "/*…*/" else placeholder(n)
            if (p != null) {
                val r = n.textRange
                val eind = r.startOffset + n.text.trimEnd().length
                if (eind - r.startOffset > 1 && (r.startOffset until eind).any { tekst[it] == '\n' }) {
                    uit += FoldingDescriptor(n, TextRange(r.startOffset, eind), null, p)
                }
            }
            var c = n.firstChildNode
            while (c != null) { loop(c); c = c.treeNext }
        }
        loop(root.node)
        return uit.toTypedArray()
    }

    override fun getPlaceholderText(node: ASTNode): String = placeholder(node) ?: "…"
    override fun isCollapsedByDefault(node: ASTNode): Boolean = false
}

class BisonFolding : TaalFolding(BisonTokens.TYPES) {
    override fun placeholder(node: ASTNode): String? = when (node.elementType) {
        B.RULE -> node.findChildByType(B.RULE_NAME)?.text?.let { "$it: …" } ?: "…"
        B.ACTION -> if (node.text.startsWith("%?")) "%?{…}" else "{…}"
        // Het blok van `%union` vouwt mee met de hele `%union`.
        B.CODE_BLOCK -> if (node.treeParent?.elementType == B.UNION) null else "{…}"
        B.UNION -> "%union {…}"
        B.PROLOGUE -> "%{…%}"
        B.EPILOGUE -> "…"
        else -> null
    }
}

class FlexFolding : TaalFolding(FlexTokens.TYPES) {
    override fun placeholder(node: ASTNode): String? = when (node.elementType) {
        F.PROLOGUE -> "%{…%}"
        F.TOP_BLOCK -> "%top{…}"
        F.ACTION -> if (node.text.startsWith("{")) "{…}" else "…"
        F.SC_BLOCK -> {
            val condities = generateSequence(node.firstChildNode) { it.treeNext }
                .takeWhile { it.elementType == F.SC_LIST }.joinToString("") { it.text }
            "$condities{…}"
        }
        F.USER_CODE -> "…"
        else -> null
    }
}
