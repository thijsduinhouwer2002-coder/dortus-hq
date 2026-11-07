package com.dortus.bisonflex

import com.intellij.lang.Language

/** Bison- en Yacc-grammatica's (`*.y`, `*.yy`). */
object BisonLanguage : Language("Bison") {
    private fun readResolve(): Any = BisonLanguage
    override fun getDisplayName(): String = "Bison/Yacc"
}

/** Flex- en Lex-scanners (`*.l`, `*.ll`). */
object FlexLanguage : Language("Flex") {
    private fun readResolve(): Any = FlexLanguage
    override fun getDisplayName(): String = "Flex/Lex"
}
