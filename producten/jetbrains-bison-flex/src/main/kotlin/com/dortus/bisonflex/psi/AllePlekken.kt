package com.dortus.bisonflex.psi

import com.dortus.bisonflex.lexer.BisonTokens
import com.dortus.bisonflex.lexer.FlexTokens
import com.dortus.bisonflex.lexer.Soort
import com.dortus.bisonflex.lexer.TokenTypes
import com.dortus.bisonflex.lexer.bisonLexer
import com.dortus.bisonflex.lexer.flexLexer
import com.dortus.bisonflex.parser.BisonElementen as B
import com.dortus.bisonflex.parser.FlexElementen as F
import com.intellij.lang.cacheBuilder.DefaultWordsScanner
import com.intellij.lang.cacheBuilder.WordsScanner
import com.intellij.lang.findUsages.FindUsagesProvider
import com.intellij.lexer.Lexer
import com.intellij.psi.PsiElement
import com.intellij.psi.tree.TokenSet

/**
 * Alle plekken vinden (Alt+F7) per taal (eis 6). De woordenlijst voor de index komt uit onze eigen lexer: namen
 * (ook in C-code) tellen als code, zodat `return NUM;` in een `.l` gevonden wordt vanaf `%token NUM`.
 */
abstract class AllePlekken(private val lexer: () -> Lexer, private val types: TokenTypes) : FindUsagesProvider {

    override fun getWordsScanner(): WordsScanner {
        val namen = TokenSet.create(*NAMEN.map { types.type(it) }.toTypedArray())
        return DefaultWordsScanner(lexer(), namen, types.commentaar, types.strings)
    }

    override fun canFindUsagesFor(element: PsiElement): Boolean = element is NaamElement
    override fun getHelpId(element: PsiElement): String? = null

    override fun getType(element: PsiElement): String = when (element.node?.elementType) {
        B.RULE_NAME -> "rule"
        B.TOKEN_NAME -> "token"
        F.START_CONDITION_NAME -> "start condition"
        else -> ""
    }

    override fun getDescriptiveName(element: PsiElement): String = (element as? NaamElement)?.name ?: element.text
    override fun getNodeText(element: PsiElement, useFullName: Boolean): String = getDescriptiveName(element)

    companion object {
        private val NAMEN = listOf(Soort.NAAM, Soort.TOKEN, Soort.DEFINITIE, Soort.STARTCONDITIE, Soort.C_NAAM)
    }
}

class BisonAllePlekken : AllePlekken(::bisonLexer, BisonTokens.TYPES)
class FlexAllePlekken : AllePlekken(::flexLexer, FlexTokens.TYPES)
