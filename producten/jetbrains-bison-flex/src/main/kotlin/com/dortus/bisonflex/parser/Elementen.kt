package com.dortus.bisonflex.parser

import com.dortus.bisonflex.BisonLanguage
import com.dortus.bisonflex.FlexLanguage
import com.intellij.psi.tree.IElementType
import com.intellij.psi.tree.IFileElementType

/**
 * De knopen van de boom (PSI) per taal. De namen zijn Engels en vast: tests en later
 * structuurweergave, folding en referenties gaan erop.
 */
class BisonElementType(naam: String) : IElementType(naam, BisonLanguage)
class FlexElementType(naam: String) : IElementType(naam, FlexLanguage)

object BisonElementen {
    @JvmField val BESTAND = IFileElementType(BisonLanguage)

    // Declaratiedeel
    @JvmField val DECLARATIONS = BisonElementType("DECLARATIONS")
    /** `%{ ... %}`. */
    @JvmField val PROLOGUE = BisonElementType("PROLOGUE")
    @JvmField val CODE_DECL = BisonElementType("CODE_DECL")
    @JvmField val TOKEN_DECL = BisonElementType("TOKEN_DECL")
    @JvmField val NTERM_DECL = BisonElementType("NTERM_DECL")
    @JvmField val TYPE_DECL = BisonElementType("TYPE_DECL")
    @JvmField val UNION = BisonElementType("UNION")
    @JvmField val DEFINE = BisonElementType("DEFINE")
    @JvmField val START = BisonElementType("START")
    @JvmField val LEFT = BisonElementType("LEFT")
    @JvmField val RIGHT = BisonElementType("RIGHT")
    @JvmField val NONASSOC = BisonElementType("NONASSOC")
    @JvmField val PRECEDENCE = BisonElementType("PRECEDENCE")
    /** Elke andere `%`-opdracht (`%expect`, `%destructor`, `%parse-param`, ...). */
    @JvmField val DIRECTIVE = BisonElementType("DIRECTIVE")
    /** `{ ... }` in een declaratie (`%union`, `%code`, `%define x {...}`, `%destructor`). */
    @JvmField val CODE_BLOCK = BisonElementType("CODE_BLOCK")
    /** Naam van een token waar het gedeclareerd wordt (`%token NUM`, `%left PLUS`). */
    @JvmField val TOKEN_NAME = BisonElementType("TOKEN_NAME")

    // Regeldeel
    @JvmField val RULES = BisonElementType("RULES")
    @JvmField val RULE = BisonElementType("RULE")
    /** Naam van een regel waar hij gedefinieerd wordt (`exp:`). */
    @JvmField val RULE_NAME = BisonElementType("RULE_NAME")
    @JvmField val ALTERNATIVES = BisonElementType("ALTERNATIVES")
    @JvmField val ALTERNATIVE = BisonElementType("ALTERNATIVE")
    /** Gebruik van een regel of token (in een regel, `%type`, `%start`, `%prec`). */
    @JvmField val SYMBOL_REF = BisonElementType("SYMBOL_REF")
    /** `[naam]` achter een symbool of regelnaam. */
    @JvmField val NAMED_REF = BisonElementType("NAMED_REF")
    @JvmField val ACTION = BisonElementType("ACTION")
    /** `%prec X`. */
    @JvmField val PREC = BisonElementType("PREC")
    /** `%empty`, `%dprec 1`, `%merge <f>`, `%expect 0`, `%?{ }` in een alternatief. */
    @JvmField val RULE_DIRECTIVE = BisonElementType("RULE_DIRECTIVE")

    @JvmField val EPILOGUE = BisonElementType("EPILOGUE")
}

object FlexElementen {
    @JvmField val BESTAND = IFileElementType(FlexLanguage)

    @JvmField val DEFINITIONS = FlexElementType("DEFINITIONS")
    /** `%{ ... %}`. */
    @JvmField val PROLOGUE = FlexElementType("PROLOGUE")
    /** `%top{ ... }`. */
    @JvmField val TOP_BLOCK = FlexElementType("TOP_BLOCK")
    /** Ingesprongen C-code. */
    @JvmField val CODE = FlexElementType("CODE")
    /** `DIGIT [0-9]`. */
    @JvmField val NAME_DEF = FlexElementType("NAME_DEF")
    @JvmField val DEFINITION_NAME = FlexElementType("DEFINITION_NAME")
    @JvmField val OPTION = FlexElementType("OPTION")
    /** `%x` of `%s`. */
    @JvmField val START_CONDITION_DECL = FlexElementType("START_CONDITION_DECL")
    @JvmField val START_CONDITION_NAME = FlexElementType("START_CONDITION_NAME")
    @JvmField val DIRECTIVE = FlexElementType("DIRECTIVE")

    @JvmField val RULES = FlexElementType("RULES")
    @JvmField val FLEX_RULE = FlexElementType("FLEX_RULE")
    /** `<A,B>` vooraan een regel. */
    @JvmField val SC_LIST = FlexElementType("SC_LIST")
    @JvmField val START_CONDITION_REF = FlexElementType("START_CONDITION_REF")
    /** `<SC>{ ... }`: een groep regels. */
    @JvmField val SC_BLOCK = FlexElementType("SC_BLOCK")
    @JvmField val PATTERN = FlexElementType("PATTERN")
    @JvmField val ACTION = FlexElementType("ACTION")

    @JvmField val USER_CODE = FlexElementType("USER_CODE")
}
