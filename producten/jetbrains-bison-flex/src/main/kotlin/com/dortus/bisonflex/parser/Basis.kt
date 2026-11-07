package com.dortus.bisonflex.parser

import com.dortus.bisonflex.lexer.Soort
import com.dortus.bisonflex.lexer.TokenTypes
import com.intellij.lang.PsiBuilder
import com.intellij.psi.TokenType
import com.intellij.psi.tree.IElementType

/**
 * Gedeelde hulpjes voor de handgeschreven parsers. De parser leest de tokens van de lexer
 * via [PsiBuilder]; witruimte en commentaar slaat de builder zelf over.
 *
 * Foutteksten zijn Engels in de stijl van de IDE ("';' expected"), want gebruikers zien ze.
 */
abstract class Basis(protected val b: PsiBuilder, protected val types: TokenTypes) {

    protected val soort: Soort? get() = types.soort(b.tokenType)
    protected val tekst: String get() = b.tokenText ?: ""
    protected val eof: Boolean get() = b.eof()

    protected fun stap() = b.advanceLexer()
    protected fun isSoort(s: Soort) = soort == s
    protected fun isTekst(s: Soort, t: String) = soort == s && tekst == t

    /** Zet het huidige token in een eigen knoop van [type]. */
    protected fun wikkel(type: IElementType) { val m = b.mark(); stap(); m.done(type) }

    /** Lege fout op de huidige plek (voor het volgende token, of aan het eind). */
    protected fun fout(tekst: String) = b.error(tekst)

    /** Slaat tokens over tot [stop] waar is en zet ze samen in één foutknoop. Neemt minstens één token. */
    protected fun slaOver(tekst: String, stop: () -> Boolean) {
        val m = b.mark()
        if (!eof) stapOver()
        while (!eof && !stop()) stapOver()
        m.error(tekst)
    }

    /** Eén token, of een heel `{ ... }`-blok als het een openende accolade is. */
    protected fun stapOver() {
        if (isTekst(Soort.ACCOLADE, "{")) leesAccoladeBlok(null) else stap()
    }

    /**
     * Leest `{ ... }` met de accoladediepte van de lexer (accolades in strings en commentaar
     * zijn andere tokens). Staat het huidige token op `{`. Geeft false als het bestand eindigt
     * voor de sluitende `}`; dan staat er een fout aan het eind.
     */
    protected fun leesAccoladeBlok(type: IElementType?): Boolean {
        val m = b.mark()
        var diepte = 0
        do {
            if (soort == Soort.ACCOLADE) diepte += if (tekst == "{") 1 else -1
            stap()
        } while (!eof && diepte > 0)
        val dicht = diepte <= 0
        if (!dicht) fout("'}' expected")
        if (type != null) m.done(type) else m.drop()
        return dicht
    }

    /** Eerste token op zijn regel (alleen witruimte en commentaar ervoor)? */
    protected fun opNieuweRegel(): Boolean {
        var i = -1
        while (true) {
            val t = b.rawLookup(i) ?: return true
            if (t != TokenType.WHITE_SPACE && t !in types.commentaar) return false
            val van = b.rawTokenTypeStart(i)
            val tot = b.rawTokenTypeStart(i + 1)
            for (k in van until tot) if (b.originalText[k] == '\n') return true
            i--
        }
    }

    /** Staat er witruimte of commentaar direct voor het huidige token? */
    protected fun gatErvoor(): Boolean {
        val t = b.rawLookup(-1) ?: return false
        return t == TokenType.WHITE_SPACE || t in types.commentaar
    }

    /** Alles tot het eind van het bestand in één knoop. */
    protected fun restIn(type: IElementType) {
        if (eof) return
        val m = b.mark()
        while (!eof) stap()
        m.done(type)
    }

    protected fun isFout() = b.tokenType == TokenType.BAD_CHARACTER
}
