package com.dortus.bisonflex

import com.intellij.lang.Language

// Unieke ID's: de gratis "Bison Language Support" gebruikt al de ID "Bison".
// Niet meer veranderen na de lancering, anders breken instellingen van gebruikers.

/** Bison- en Yacc-grammatica's (`*.y`, `*.yy`). */
object BisonLanguage : Language("BisonFlex.Bison") {
    override fun getDisplayName(): String = "Bison/Yacc"
}

/** Flex- en Lex-scanners (`*.l`, `*.ll`). */
object FlexLanguage : Language("BisonFlex.Flex") {
    override fun getDisplayName(): String = "Flex/Lex"
}
