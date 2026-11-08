package com.dortus.bisonflex.parser

import com.dortus.bisonflex.lexer.BisonTokens
import com.dortus.bisonflex.lexer.Soort
import com.dortus.bisonflex.parser.BisonElementen as E
import com.intellij.lang.ASTNode
import com.intellij.lang.PsiBuilder
import com.intellij.lang.PsiParser
import com.intellij.psi.tree.IElementType

/**
 * Handgeschreven parser voor Bison (geen generator). Volgt de grammatica van Bison zelf
 * (`parse-gram.y`) zo ver als nodig voor de boom:
 * declaraties `%%` regels [`%%` epiloog]. De `;` na een regel mag weg, net als in Bison:
 * de lexer merkt `naam :` al aan als begin van een nieuwe regel (Soort.DEFINITIE).
 */
class BisonParser : PsiParser {
    override fun parse(root: IElementType, builder: PsiBuilder): ASTNode {
        val m = builder.mark()
        BisonLezer(builder).bestand()
        m.done(root)
        return builder.treeBuilt
    }
}

private class BisonLezer(b: PsiBuilder) : Basis(b, BisonTokens.TYPES) {

    private fun isScheiding(t: String) = isTekst(Soort.SCHEIDING, t)

    fun bestand() {
        declaraties()
        if (eof) return
        stap() // %%
        regels()
        if (isScheiding("%%")) {
            stap()
            restIn(E.EPILOGUE)
        }
    }

    // ---- declaraties ----

    private fun declaraties() {
        val m = b.mark()
        var dichtAanEinde = true
        while (!eof && !isScheiding("%%")) {
            when {
                isScheiding("%{") -> dichtAanEinde = proloog()
                isSoort(Soort.OPDRACHT) -> dichtAanEinde = declaratie(inRegels = false)
                isSoort(Soort.PUNTKOMMA) -> stap() // Bison staat een losse `;` toe
                else -> slaOver("Declaration expected") {
                    isSoort(Soort.OPDRACHT) || isSoort(Soort.SCHEIDING)
                }
            }
        }
        m.done(E.DECLARATIONS)
        // Geen tweede fout als een open blok het bestand al heeft opgegeten.
        if (eof && dichtAanEinde) fout("'%%' expected")
    }

    /** `%{ ... %}`. Geeft false als het bestand eindigt voor de `%}`. */
    private fun proloog(): Boolean {
        val m = b.mark()
        stap()
        while (!eof && !isScheiding("%}")) stap()
        val dicht = !eof
        if (dicht) stap() else fout("'%}' expected")
        m.done(E.PROLOGUE)
        return dicht
    }

    private fun typeVan(opdracht: String): IElementType = when (opdracht) {
        "%token" -> E.TOKEN_DECL
        "%nterm" -> E.NTERM_DECL
        "%type" -> E.TYPE_DECL
        "%union" -> E.UNION
        "%define" -> E.DEFINE
        "%start" -> E.START
        "%left" -> E.LEFT
        "%right" -> E.RIGHT
        "%nonassoc" -> E.NONASSOC
        "%precedence" -> E.PRECEDENCE
        "%code" -> E.CODE_DECL
        else -> E.DIRECTIVE
    }

    /**
     * Eén `%`-opdracht met alles wat erbij hoort. In het declaratiedeel loopt hij tot de
     * volgende opdracht; in het regeldeel tot de `;` (die Bison daar eist).
     */
    private fun declaratie(inRegels: Boolean): Boolean {
        val m = b.mark()
        val type = typeVan(tekst)
        stap()
        var dicht = true
        fun einde(): Boolean = eof || isSoort(Soort.SCHEIDING) || isSoort(Soort.OPDRACHT) ||
            (inRegels && (isSoort(Soort.PUNTKOMMA) || isSoort(Soort.DEFINITIE)))
        while (!einde()) {
            when {
                isTekst(Soort.ACCOLADE, "{") -> dicht = leesAccoladeBlok(E.CODE_BLOCK)
                (isSoort(Soort.TOKEN) || isSoort(Soort.NAAM)) && type in DEFINIEERT_TOKENS -> wikkel(E.TOKEN_NAME)
                (isSoort(Soort.TOKEN) || isSoort(Soort.NAAM)) && type in VERWIJST -> wikkel(E.SYMBOL_REF)
                isFout() -> slaOver("Unexpected character") { true }
                else -> stap()
            }
        }
        if (inRegels) {
            if (isSoort(Soort.PUNTKOMMA)) stap() else if (dicht) fout("';' expected")
        }
        m.done(type)
        return dicht
    }

    // ---- regels ----

    private fun regels() {
        val m = b.mark()
        while (!eof && !isScheiding("%%")) {
            when {
                isSoort(Soort.DEFINITIE) || isSoort(Soort.NAAM) || isSoort(Soort.TOKEN) -> regel()
                isSoort(Soort.OPDRACHT) -> declaratie(inRegels = true)
                isScheiding("%{") -> { val p = b.mark(); proloog(); p.error("Prologue is not allowed in the rules section") }
                isSoort(Soort.PUNTKOMMA) -> stap() // `a: b ;;` mag in Bison
                else -> slaOver("Rule expected") { regelGrens() }
            }
        }
        m.done(E.RULES)
    }

    /** Plekken waar na een fout weer gewoon gelezen kan worden. */
    private fun regelGrens() = isSoort(Soort.PUNTKOMMA) || isSoort(Soort.DEFINITIE) || isScheiding("%%")

    /** `naam [alias] : alternatief | alternatief ... ;` */
    private fun regel() {
        val m = b.mark()
        wikkel(E.RULE_NAME)
        if (isTekst(Soort.BLOKHAAK, "[")) benoemd()
        // Zonder `:` (de lexer gaf dan NAAM of TOKEN): fout, en lees de rest als alternatieven.
        if (isSoort(Soort.DUBBELEPUNT)) stap() else fout("':' expected")
        val alts = b.mark()
        alternatief()
        // Bison (`parse-gram.y`): `rhses.1: rhs | rhses.1 "|" rhs | rhses.1 ";"`. Na een `;` mag dus
        // nog een `|` met een alternatief van dezelfde regel komen (`a: b ; | c ;`). Die `;` nemen we
        // alleen mee als er (na eventueel meer `;`) echt een `|` volgt; anders blijft het einde gewoon.
        while (true) {
            if (isSoort(Soort.STREEP)) { stap(); alternatief() }
            else if (isSoort(Soort.PUNTKOMMA) && streepNaPuntkommas()) stap()
            else break
        }
        alts.done(E.ALTERNATIVES)
        when {
            isSoort(Soort.PUNTKOMMA) -> stap()
            // Zonder `;` mag alleen een nieuwe regel, een declaratie of `%%` volgen (zoals Bison).
            eof || isSoort(Soort.DEFINITIE) || isSoort(Soort.OPDRACHT) || isScheiding("%%") -> {}
            else -> {
                slaOver("'|' or ';' expected, got '$tekst'") { regelGrens() }
                if (isSoort(Soort.PUNTKOMMA)) stap()
            }
        }
        m.done(E.RULE)
    }

    /** Staat het huidige token op `;` en volgt er na nul of meer `;` een `|`? */
    private fun streepNaPuntkommas(): Boolean {
        var i = 1
        while (types.soort(b.lookAhead(i)) == Soort.PUNTKOMMA) i++
        return types.soort(b.lookAhead(i)) == Soort.STREEP
    }

    /** Eén alternatief: symbolen, acties, `%prec`, `%empty` enzovoort. Mag leeg zijn. */
    private fun alternatief() {
        val m = b.mark()
        loop@ while (!eof) {
            when {
                isSoort(Soort.TOKEN) || isSoort(Soort.NAAM) -> { wikkel(E.SYMBOL_REF); naBenoemd() }
                isSoort(Soort.TEKEN) || isSoort(Soort.STRING) -> { stap(); naBenoemd() }
                isTekst(Soort.ACCOLADE, "{") -> { leesAccoladeBlok(E.ACTION); naBenoemd() }
                isSoort(Soort.TYPE) -> stap() // `<tag>{ ... }`: getypeerde actie halverwege
                isTekst(Soort.OPDRACHT, "%prec") -> prec()
                isSoort(Soort.OPDRACHT) && tekst in REGELOPDRACHTEN -> regelopdracht()
                else -> break@loop
            }
        }
        m.done(E.ALTERNATIVE)
    }

    private fun naBenoemd() { if (isTekst(Soort.BLOKHAAK, "[")) benoemd() }

    /** `[naam]`. */
    private fun benoemd() {
        val m = b.mark()
        stap()
        if (isSoort(Soort.NAAM) || isSoort(Soort.TOKEN)) stap() else fout("Name expected")
        if (isTekst(Soort.BLOKHAAK, "]")) stap() else fout("']' expected")
        m.done(E.NAMED_REF)
    }

    private fun prec() {
        val m = b.mark()
        stap()
        when {
            isSoort(Soort.TOKEN) || isSoort(Soort.NAAM) -> wikkel(E.SYMBOL_REF)
            isSoort(Soort.TEKEN) || isSoort(Soort.STRING) -> stap()
            else -> fout("Symbol expected")
        }
        m.done(E.PREC)
    }

    /** `%empty`, `%dprec 1`, `%merge <f>`, `%expect 1`, `%expect-rr 1`, `%?{ ... }`. */
    private fun regelopdracht() {
        val m = b.mark()
        val t = tekst
        stap()
        when (t) {
            "%dprec", "%expect", "%expect-rr" -> if (isSoort(Soort.GETAL)) stap() else fout("Number expected")
            "%merge" -> if (isSoort(Soort.TYPE)) stap() else fout("'<' expected")
            "%?" -> if (isTekst(Soort.ACCOLADE, "{")) leesAccoladeBlok(E.ACTION) else fout("'{' expected")
        }
        m.done(E.RULE_DIRECTIVE)
    }

    companion object {
        val DEFINIEERT_TOKENS = setOf(E.TOKEN_DECL, E.LEFT, E.RIGHT, E.NONASSOC, E.PRECEDENCE)
        val VERWIJST = setOf(E.TYPE_DECL, E.NTERM_DECL, E.START, E.DIRECTIVE)
        val REGELOPDRACHTEN = setOf("%empty", "%dprec", "%merge", "%expect", "%expect-rr", "%?")
    }
}
