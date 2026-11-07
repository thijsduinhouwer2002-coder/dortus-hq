package com.dortus.bisonflex

import com.dortus.bisonflex.lexer.Soort
import com.dortus.bisonflex.lexer.TokenTypes
import com.dortus.bisonflex.lexer.BisonTokens
import com.dortus.bisonflex.lexer.FlexTokens
import com.dortus.bisonflex.lexer.bisonLexer
import com.dortus.bisonflex.lexer.flexLexer
import com.intellij.lexer.Lexer
import com.intellij.openapi.editor.DefaultLanguageHighlighterColors as D
import com.intellij.openapi.editor.HighlighterColors
import com.intellij.openapi.editor.colors.TextAttributesKey
import com.intellij.openapi.editor.colors.TextAttributesKey.createTextAttributesKey
import com.intellij.openapi.fileTypes.SyntaxHighlighter
import com.intellij.openapi.fileTypes.SyntaxHighlighterBase
import com.intellij.openapi.fileTypes.SyntaxHighlighterFactory
import com.intellij.openapi.options.colors.AttributesDescriptor
import com.intellij.openapi.options.colors.ColorDescriptor
import com.intellij.openapi.options.colors.ColorSettingsPage
import com.intellij.openapi.project.Project
import com.intellij.openapi.vfs.VirtualFile
import javax.swing.Icon

/**
 * Kleuren. Elke sleutel valt terug op een standaardkleur van de IDE (DefaultLanguageHighlighterColors),
 * dus het klopt vanzelf in licht, donker en elk thema. Geen enkele vaste kleur (eis van Daan).
 */
class KleurSleutels(private val voorvoegsel: String) {
    private fun k(naam: String, terug: TextAttributesKey) = createTextAttributesKey("${voorvoegsel}_$naam", terug)

    val opdracht = k("DIRECTIVE", D.KEYWORD)
    val token = k("TOKEN", D.CONSTANT)
    val definitie = k("DEFINITION", D.FUNCTION_DECLARATION)
    val naam = k("IDENTIFIER", D.IDENTIFIER)
    val type = k("TYPE_TAG", D.CLASS_REFERENCE)
    val startconditie = k("START_CONDITION", D.LABEL)
    val string = k("STRING", D.STRING)
    val getal = k("NUMBER", D.NUMBER)
    val blokcommentaar = k("BLOCK_COMMENT", D.BLOCK_COMMENT)
    val regelcommentaar = k("LINE_COMMENT", D.LINE_COMMENT)
    val scheiding = k("SECTION", D.METADATA)
    val operator = k("OPERATOR", D.OPERATION_SIGN)
    val puntkomma = k("SEMICOLON", D.SEMICOLON)
    val komma = k("COMMA", D.COMMA)
    val accolade = k("BRACES", D.BRACES)
    val haakje = k("PARENTHESES", D.PARENTHESES)
    val blokhaak = k("BRACKETS", D.BRACKETS)
    val reKlasse = k("REGEX_CLASS", D.STRING)
    val reEscape = k("REGEX_ESCAPE", D.VALID_STRING_ESCAPE)
    val reOperator = k("REGEX_OPERATOR", D.OPERATION_SIGN)
    val reVerwijzing = k("REGEX_REFERENCE", D.IDENTIFIER)
    val cSleutelwoord = k("C_KEYWORD", D.KEYWORD)
    val cPreprocessor = k("C_PREPROCESSOR", D.METADATA)
    val bisonVariabele = k("SEMANTIC_VALUE", D.INSTANCE_FIELD)
    val flexMacro = k("FLEX_MACRO", D.PREDEFINED_SYMBOL)

    fun voor(s: Soort): TextAttributesKey? = when (s) {
        Soort.OPDRACHT, Soort.RE_EOF -> opdracht
        Soort.TOKEN -> token
        Soort.DEFINITIE -> definitie
        Soort.NAAM -> naam
        Soort.TYPE -> type
        Soort.STARTCONDITIE -> startconditie
        Soort.STRING, Soort.TEKEN, Soort.C_STRING, Soort.C_TEKEN -> string
        Soort.GETAL, Soort.C_GETAL, Soort.RE_HERHALING -> getal
        Soort.BLOKCOMMENTAAR -> blokcommentaar
        Soort.REGELCOMMENTAAR -> regelcommentaar
        Soort.SCHEIDING -> scheiding
        Soort.DUBBELEPUNT, Soort.STREEP, Soort.C_OPERATOR -> operator
        Soort.PUNTKOMMA -> puntkomma
        Soort.KOMMA -> komma
        Soort.ACCOLADE -> accolade
        Soort.HAAKJE -> haakje
        Soort.BLOKHAAK -> blokhaak
        Soort.RE_KLASSE -> reKlasse
        Soort.RE_ESCAPE -> reEscape
        Soort.RE_OPERATOR -> reOperator
        Soort.RE_VERWIJZING -> reVerwijzing
        Soort.C_SLEUTELWOORD -> cSleutelwoord
        Soort.C_PREPROCESSOR -> cPreprocessor
        Soort.C_BISONVARIABELE -> bisonVariabele
        Soort.C_FLEXMACRO -> flexMacro
        Soort.FOUT -> HighlighterColors.BAD_CHARACTER
        Soort.SPATIE, Soort.OVERIG, Soort.RE_TEKST, Soort.C_NAAM -> null
    }
}

object BisonKleuren { @JvmField val SLEUTELS = KleurSleutels("BISON") }
object FlexKleuren { @JvmField val SLEUTELS = KleurSleutels("FLEX") }

class KleurHighlighter(
    private val maakLexer: () -> Lexer,
    private val types: TokenTypes,
    private val sleutels: KleurSleutels,
) : SyntaxHighlighterBase() {
    override fun getHighlightingLexer(): Lexer = maakLexer()
    override fun getTokenHighlights(tokenType: com.intellij.psi.tree.IElementType?): Array<TextAttributesKey> {
        if (tokenType == com.intellij.psi.TokenType.BAD_CHARACTER) return arrayOf(HighlighterColors.BAD_CHARACTER)
        val s = types.soort(tokenType) ?: return emptyArray()
        return sleutels.voor(s)?.let { arrayOf(it) } ?: emptyArray()
    }
}

fun bisonHighlighter() = KleurHighlighter(::bisonLexer, BisonTokens.TYPES, BisonKleuren.SLEUTELS)
fun flexHighlighter() = KleurHighlighter(::flexLexer, FlexTokens.TYPES, FlexKleuren.SLEUTELS)

class BisonHighlighterFactory : SyntaxHighlighterFactory() {
    override fun getSyntaxHighlighter(project: Project?, virtualFile: VirtualFile?): SyntaxHighlighter = bisonHighlighter()
}

class FlexHighlighterFactory : SyntaxHighlighterFactory() {
    override fun getSyntaxHighlighter(project: Project?, virtualFile: VirtualFile?): SyntaxHighlighter = flexHighlighter()
}

/** Kleurenpagina in Settings, Editor, Color Scheme (punt 2 van Daan). */
abstract class KleurenPagina(
    private val naam: String,
    private val icoon: Icon,
    private val maak: () -> SyntaxHighlighter,
    private val beschrijvingen: Array<AttributesDescriptor>,
    private val voorbeeld: String,
) : ColorSettingsPage {
    override fun getDisplayName(): String = naam
    override fun getIcon(): Icon = icoon
    override fun getHighlighter(): SyntaxHighlighter = maak()
    override fun getDemoText(): String = voorbeeld
    override fun getAdditionalHighlightingTagToDescriptorMap(): Map<String, TextAttributesKey>? = null
    override fun getAttributeDescriptors(): Array<AttributesDescriptor> = beschrijvingen
    override fun getColorDescriptors(): Array<ColorDescriptor> = ColorDescriptor.EMPTY_ARRAY
}

private fun gedeeld(k: KleurSleutels) = listOf(
    AttributesDescriptor("Directive (%token, %option)", k.opdracht),
    AttributesDescriptor("Section separator (%%, %{ %})", k.scheiding),
    AttributesDescriptor("Identifier", k.naam),
    AttributesDescriptor("String and character", k.string),
    AttributesDescriptor("Number", k.getal),
    AttributesDescriptor("Comments//Block comment", k.blokcommentaar),
    AttributesDescriptor("Comments//Line comment", k.regelcommentaar),
    AttributesDescriptor("Braces and operators//Operator", k.operator),
    AttributesDescriptor("Braces and operators//Semicolon", k.puntkomma),
    AttributesDescriptor("Braces and operators//Comma", k.komma),
    AttributesDescriptor("Braces and operators//Braces", k.accolade),
    AttributesDescriptor("Braces and operators//Parentheses", k.haakje),
    AttributesDescriptor("Braces and operators//Brackets", k.blokhaak),
    AttributesDescriptor("C code//Keyword", k.cSleutelwoord),
    AttributesDescriptor("C code//Preprocessor directive", k.cPreprocessor),
)

class BisonKleurenPagina : KleurenPagina(
    "Bison/Yacc", BisonIconen.BISON, ::bisonHighlighter,
    (gedeeld(BisonKleuren.SLEUTELS) + listOf(
        AttributesDescriptor("Token", BisonKleuren.SLEUTELS.token),
        AttributesDescriptor("Rule definition", BisonKleuren.SLEUTELS.definitie),
        AttributesDescriptor("Type tag (<type>)", BisonKleuren.SLEUTELS.type),
        AttributesDescriptor("C code//Semantic value ($$, $1, @1)", BisonKleuren.SLEUTELS.bisonVariabele),
    )).toTypedArray(),
    Voorbeelden.BISON,
)

class FlexKleurenPagina : KleurenPagina(
    "Flex/Lex", BisonIconen.FLEX, ::flexHighlighter,
    (gedeeld(FlexKleuren.SLEUTELS) + listOf(
        AttributesDescriptor("Definition name", FlexKleuren.SLEUTELS.definitie),
        AttributesDescriptor("Token (upper-case name in actions)", FlexKleuren.SLEUTELS.token),
        AttributesDescriptor("Start condition", FlexKleuren.SLEUTELS.startconditie),
        AttributesDescriptor("Regular expression//Character class", FlexKleuren.SLEUTELS.reKlasse),
        AttributesDescriptor("Regular expression//Escape", FlexKleuren.SLEUTELS.reEscape),
        AttributesDescriptor("Regular expression//Operator", FlexKleuren.SLEUTELS.reOperator),
        AttributesDescriptor("Regular expression//Definition reference ({name})", FlexKleuren.SLEUTELS.reVerwijzing),
        AttributesDescriptor("C code//Flex macro (BEGIN, yytext)", FlexKleuren.SLEUTELS.flexMacro),
    )).toTypedArray(),
    Voorbeelden.FLEX,
)
