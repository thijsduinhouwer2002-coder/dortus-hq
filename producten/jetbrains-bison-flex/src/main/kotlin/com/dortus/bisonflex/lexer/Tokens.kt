package com.dortus.bisonflex.lexer

import com.intellij.lang.Language
import com.intellij.lexer.LexerBase
import com.intellij.psi.TokenType
import com.intellij.psi.tree.IElementType
import com.intellij.psi.tree.TokenSet
import com.dortus.bisonflex.BisonLanguage
import com.dortus.bisonflex.FlexLanguage

/** Eén IElementType per [Soort] voor een taal. Witruimte en fouten gebruiken de vaste types van de IDE. */
class TokenTypes(taal: Language, voorvoegsel: String) {
    private val types: Map<Soort, IElementType> = Soort.entries.associateWith { s ->
        when (s) {
            Soort.SPATIE -> TokenType.WHITE_SPACE
            Soort.FOUT -> TokenType.BAD_CHARACTER
            else -> IElementType("${voorvoegsel}_${s.name}", taal)
        }
    }
    private val terug: Map<IElementType, Soort> = types.entries.associate { (k, v) -> v to k }

    fun type(s: Soort): IElementType = types.getValue(s)
    fun soort(t: IElementType?): Soort? = t?.let { terug[it] }

    val commentaar: TokenSet = TokenSet.create(type(Soort.BLOKCOMMENTAAR), type(Soort.REGELCOMMENTAAR))
    val strings: TokenSet = TokenSet.create(type(Soort.STRING), type(Soort.TEKEN), type(Soort.C_STRING), type(Soort.C_TEKEN))
}

object BisonTokens { @JvmField val TYPES = TokenTypes(BisonLanguage, "BISON") }
object FlexTokens { @JvmField val TYPES = TokenTypes(FlexLanguage, "FLEX") }

/** Zet een [Scanner] om naar een lexer van de IDE. */
class ScannerLexer(private val scanner: Scanner, private val types: TokenTypes) : LexerBase() {
    private var buffer: CharSequence = ""
    private var einde = 0
    private var tokenStart = 0
    private var toestand = 0

    override fun start(buffer: CharSequence, startOffset: Int, endOffset: Int, initialState: Int) {
        this.buffer = buffer; einde = endOffset; tokenStart = startOffset; toestand = initialState
        scanner.stap(buffer, tokenStart, einde, toestand)
    }

    override fun getState(): Int = toestand
    override fun getTokenType(): IElementType? = scanner.soort?.let { types.type(it) }
    override fun getTokenStart(): Int = tokenStart
    override fun getTokenEnd(): Int = scanner.tokenEinde

    override fun advance() {
        if (scanner.soort == null) return
        // Elk token moet minstens één teken lang zijn, anders blijft de IDE hangen.
        tokenStart = maxOf(scanner.tokenEinde, tokenStart + 1).coerceAtMost(einde)
        toestand = scanner.nieuweToestand
        scanner.stap(buffer, tokenStart, einde, toestand)
    }

    override fun getBufferSequence(): CharSequence = buffer
    override fun getBufferEnd(): Int = einde
}

fun bisonLexer() = ScannerLexer(BisonScanner(), BisonTokens.TYPES)
fun flexLexer() = ScannerLexer(FlexScanner(), FlexTokens.TYPES)
