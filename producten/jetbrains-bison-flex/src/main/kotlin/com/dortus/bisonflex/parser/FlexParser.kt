package com.dortus.bisonflex.parser

import com.dortus.bisonflex.lexer.FlexTokens
import com.dortus.bisonflex.lexer.Soort
import com.dortus.bisonflex.parser.FlexElementen as E
import com.intellij.lang.ASTNode
import com.intellij.lang.PsiBuilder
import com.intellij.lang.PsiParser
import com.intellij.psi.tree.IElementType

/**
 * Handgeschreven parser voor Flex (geen generator): definities `%%` regels [`%%` gebruikerscode].
 * Flex hangt af van regels en spaties; de lexer heeft dat al gedaan (patroon en actie zijn
 * andere tokensoorten). De parser kijkt daarnaast naar het begin van de regel ([opNieuweRegel])
 * en naar spaties tussen tokens ([gatErvoor]): een patroon loopt tot de eerste spatie.
 */
class FlexParser : PsiParser {
    override fun parse(root: IElementType, builder: PsiBuilder): ASTNode {
        val m = builder.mark()
        FlexLezer(builder).bestand()
        m.done(root)
        return builder.treeBuilt
    }
}

private class FlexLezer(b: PsiBuilder) : Basis(b, FlexTokens.TYPES) {

    private fun isScheiding(t: String) = isTekst(Soort.SCHEIDING, t)
    private fun isPatroon() = soort in PATROON
    private fun isC() = soort in C_CODE

    fun bestand() {
        definities()
        if (eof) return
        stap() // %%
        regels()
        if (isScheiding("%%")) {
            stap()
            restIn(E.USER_CODE)
        }
    }

    // ---- definities ----

    private fun definities() {
        val m = b.mark()
        var dicht = true
        while (!eof && !isScheiding("%%")) {
            when {
                isScheiding("%{") -> dicht = proloog()
                isScheiding("%top{") -> dicht = top()
                isSoort(Soort.OPDRACHT) -> opdracht()
                isSoort(Soort.DEFINITIE) -> naamDefinitie()
                isC() -> code()
                else -> slaOver("Definition expected") { opNieuweRegel() }
            }
        }
        m.done(E.DEFINITIONS)
        if (eof && dicht) fout("'%%' expected")
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

    /** `%top{ ... }`: de `{` zit in het eerste token. */
    private fun top(): Boolean {
        val m = b.mark()
        stap()
        var diepte = 1
        while (!eof) {
            if (isSoort(Soort.ACCOLADE)) diepte += if (tekst == "{") 1 else -1
            stap()
            if (diepte == 0) break
        }
        val dicht = diepte == 0
        if (!dicht) fout("'}' expected")
        m.done(E.TOP_BLOCK)
        return dicht
    }

    /** `%option ...`, `%x A B`, `%s A`, `%array` enzovoort: tot het eind van de regel. */
    private fun opdracht() {
        val m = b.mark()
        val naam = tekst
        stap()
        val sc = naam == "%x" || naam == "%s" || naam == "%exclusive" || naam == "%start"
        while (!eof && !opNieuweRegel()) {
            if (isSoort(Soort.STARTCONDITIE)) wikkel(E.START_CONDITION_NAME) else stap()
        }
        m.done(when {
            sc -> E.START_CONDITION_DECL
            naam == "%option" -> E.OPTION
            else -> E.DIRECTIVE
        })
    }

    /** `NAAM patroon`. */
    private fun naamDefinitie() {
        val m = b.mark()
        wikkel(E.DEFINITION_NAME)
        if (isPatroon() && !opNieuweRegel()) patroon() else fout("Pattern expected")
        m.done(E.NAME_DEF)
    }

    /** Ingesprongen C-code (in de definities of vooraan de regels). */
    private fun code() {
        val m = b.mark()
        while (!eof && isC()) stap()
        m.done(E.CODE)
    }

    // ---- regels ----

    private fun regels() {
        val m = b.mark()
        regelLijst(binnenBlok = false)
        m.done(E.RULES)
    }

    /** Regels tot `%%` (of tot de `}` van een `<SC>{`-blok). */
    private fun regelLijst(binnenBlok: Boolean) {
        while (!eof && !isScheiding("%%")) {
            when {
                binnenBlok && isTekst(Soort.ACCOLADE, "}") && opNieuweRegel() -> return
                isScheiding("%{") -> proloog()
                isTekst(Soort.RE_OPERATOR, "<") && opNieuweRegel() -> regelMetCondities()
                isPatroon() -> regel(null)
                isC() && opNieuweRegel() -> code()
                else -> slaOver("Rule expected") { opNieuweRegel() }
            }
        }
    }

    /** `<A,B>patroon actie` of `<A,B>{ regels }`. */
    private fun regelMetCondities() {
        val m = b.mark()
        conditieLijst()
        while (isTekst(Soort.RE_OPERATOR, "<") && !gatErvoor()) conditieLijst()
        if (isTekst(Soort.ACCOLADE, "{") && !gatErvoor()) {
            stap()
            regelLijst(binnenBlok = true)
            if (isTekst(Soort.ACCOLADE, "}")) stap() else fout("'}' expected")
            m.done(E.SC_BLOCK)
        } else regel(m)
    }

    /** `<A,B>` of `<*>`. */
    private fun conditieLijst() {
        val m = b.mark()
        stap() // <
        while (!eof && !isTekst(Soort.RE_OPERATOR, ">")) {
            when {
                isSoort(Soort.STARTCONDITIE) -> wikkel(E.START_CONDITION_REF)
                isSoort(Soort.KOMMA) || isTekst(Soort.RE_OPERATOR, "*") -> stap()
                else -> break
            }
        }
        if (isTekst(Soort.RE_OPERATOR, ">")) stap() else fout("'>' expected")
        m.done(E.SC_LIST)
    }

    /** Patroon en actie. [m] is de al geopende regel als er condities voor stonden. */
    private fun regel(m: PsiBuilder.Marker?) {
        val r = m ?: b.mark()
        if (isPatroon() && (m == null || !gatErvoor())) patroon() else fout("Pattern expected")
        if (!eof && !opNieuweRegel()) actie()
        r.done(E.FLEX_RULE)
    }

    /** Tokens van een reguliere expressie zonder spatie ertussen. */
    private fun patroon() {
        val m = b.mark()
        stap()
        while (!eof && isPatroon() && !gatErvoor()) stap()
        m.done(E.PATTERN)
    }

    /** `|`, of C-code tot het eind van de regel; met `{` ook over meerdere regels. */
    private fun actie() {
        val m = b.mark()
        if (isSoort(Soort.STREEP)) { stap(); m.done(E.ACTION); return }
        if (!isC()) { m.drop(); slaOver("Action expected") { opNieuweRegel() }; return }
        var diepte = 0
        while (!eof && !(diepte == 0 && opNieuweRegel())) {
            if (isSoort(Soort.ACCOLADE)) diepte = maxOf(0, diepte + if (tekst == "{") 1 else -1)
            stap()
        }
        if (diepte > 0) fout("'}' expected")
        m.done(E.ACTION)
    }

    companion object {
        val PATROON = setOf(
            Soort.RE_TEKST, Soort.RE_KLASSE, Soort.RE_ESCAPE, Soort.RE_OPERATOR, Soort.RE_HERHALING,
            Soort.RE_VERWIJZING, Soort.RE_EOF, Soort.STRING,
        )
        val C_CODE = setOf(
            Soort.C_SLEUTELWOORD, Soort.C_NAAM, Soort.C_STRING, Soort.C_TEKEN, Soort.C_GETAL, Soort.C_OPERATOR,
            Soort.C_PREPROCESSOR, Soort.C_FLEXMACRO, Soort.TOKEN, Soort.STARTCONDITIE, Soort.ACCOLADE,
            Soort.HAAKJE, Soort.BLOKHAAK, Soort.PUNTKOMMA, Soort.KOMMA,
        )
    }
}
