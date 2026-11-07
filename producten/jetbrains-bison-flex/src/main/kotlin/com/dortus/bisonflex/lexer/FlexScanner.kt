package com.dortus.bisonflex.lexer

/**
 * Lexer voor Flex- en Lex-scanners (`*.l`, `*.ll`).
 *
 * Flex hangt sterk af van de plek op de regel: een naam vooraan is een definitie, een
 * ingesprongen regel is C-code, en in het regeldeel loopt een reguliere expressie tot de
 * eerste spatie buiten aanhalingstekens. Daarom houdt de toestand bij: bit 0-1 het deel
 * (definities, regels, eigen code), bit 2-5 de stand, bit 6-9 hoe diep we in `<SC>{ }`-blokken
 * zitten, bit 10 en hoger de accoladediepte van de C-code.
 */
class FlexScanner : Scanner() {

    override fun lees(pos: Int, toestand: Int) {
        val deel = toestand and 3
        val stand = (toestand shr 2) and 15
        val scope = (toestand shr 6) and 15
        val diepte = toestand ushr 10
        fun t(st: Int, d: Int = 0, sc: Int = scope, dl: Int = deel) = maak(dl, st, sc, d)
        val ch = buf[pos]

        when (stand) {
            PROLOOG -> {
                if (begintMet(pos, "%}")) { klaar(Soort.SCHEIDING, pos + 2, t(GEWOON)); return }
                val (s, e) = leesC(pos, bison = false)
                var eind = e
                for (k in pos + 1 until e) if (begintMet(k, "%}")) { eind = k; break }
                klaar(s, eind, toestand)
            }
            TOP -> {
                val (s, e) = leesC(pos, bison = false)
                val d = diepte + cDiepteVerschil
                klaar(s, e, if (d <= 0) t(GEWOON) else t(TOP, d))
            }
            CREGEL -> when {
                ch == '\n' && diepte == 0 -> klaar(Soort.SPATIE, pos + 1, t(GEWOON))
                ch == '\n' -> klaar(Soort.SPATIE, eindeWit(pos), toestand)
                isSpatie(ch) -> klaar(Soort.SPATIE, eindeSpaties(pos), toestand)
                else -> {
                    val (s, e) = leesC(pos, bison = false)
                    klaar(s, e, t(CREGEL, maxOf(0, diepte + cDiepteVerschil)))
                }
            }
            CODE -> { val (s, e) = leesC(pos, bison = false); klaar(s, e, toestand) }
            DEFRE -> when {
                ch == '\n' -> klaar(Soort.SPATIE, pos + 1, t(GEWOON))
                isSpatie(ch) -> klaar(Soort.SPATIE, eindeSpaties(pos), toestand)
                else -> leesRegex(pos, toestand)
            }
            REGELRE -> when {
                ch == '\n' -> klaar(Soort.SPATIE, pos + 1, t(GEWOON))
                isSpatie(ch) -> klaar(Soort.SPATIE, eindeSpaties(pos), t(NAREGEX))
                else -> leesRegex(pos, toestand)
            }
            NAREGEX -> when {
                ch == '\n' -> klaar(Soort.SPATIE, pos + 1, t(GEWOON))
                isSpatie(ch) -> klaar(Soort.SPATIE, eindeSpaties(pos), toestand)
                ch == '|' && restVanRegelLeeg(pos + 1) -> klaar(Soort.STREEP, pos + 1, t(CREGEL))
                else -> lees(pos, t(CREGEL))
            }
            OPTIES, STARTCOND -> when {
                ch == '\n' -> klaar(Soort.SPATIE, pos + 1, t(GEWOON))
                isSpatie(ch) -> klaar(Soort.SPATIE, eindeSpaties(pos), toestand)
                ch == '/' && c(pos + 1) == '*' -> klaar(Soort.BLOKCOMMENTAAR, eindeBlokcommentaar(pos), toestand)
                ch == '"' -> klaar(Soort.STRING, eindeAanhaling(pos, '"'), toestand)
                isNaamBegin(ch) -> klaar(if (stand == STARTCOND) Soort.STARTCONDITIE else Soort.NAAM,
                    eindeNaam(pos, "-"), toestand)
                ch.isDigit() -> klaar(Soort.GETAL, eindeNaam(pos), toestand)
                else -> klaar(Soort.OVERIG, pos + 1, toestand)
            }
            SCLIJST -> when {
                isNaamBegin(ch) -> klaar(Soort.STARTCONDITIE, eindeNaam(pos), toestand)
                ch == ',' -> klaar(Soort.KOMMA, pos + 1, toestand)
                ch == '*' -> klaar(Soort.RE_OPERATOR, pos + 1, toestand)
                ch == '>' -> klaar(Soort.RE_OPERATOR, pos + 1, t(NASC))
                else -> klaar(Soort.FOUT, pos + 1, t(REGELRE))
            }
            NASC -> when {
                ch == '{' && restVanRegelLeeg(pos + 1) -> klaar(Soort.ACCOLADE, pos + 1, t(GEWOON, sc = minOf(15, scope + 1)))
                ch == '<' && begintMet(pos, "<<EOF>>") -> klaar(Soort.RE_EOF, pos + 7, t(REGELRE))
                ch == '<' -> klaar(Soort.RE_OPERATOR, pos + 1, t(SCLIJST))
                else -> leesRegex(pos, t(REGELRE))
            }
            else -> if (deel == DEFINITIES) leesDefinities(pos, scope) else leesRegels(pos, scope)
        }
    }

    private fun leesDefinities(pos: Int, scope: Int) {
        val gewoon = maak(DEFINITIES, GEWOON, scope, 0)
        val ch = buf[pos]
        val begin = isRegelbegin(pos)
        when {
            begin && begintMet(pos, "%%") -> klaar(Soort.SCHEIDING, pos + 2, maak(REGELS, GEWOON, 0, 0))
            begintMet(pos, "%{") -> klaar(Soort.SCHEIDING, pos + 2, maak(DEFINITIES, PROLOOG, 0, 0))
            begin && begintMet(pos, "%top{") -> klaar(Soort.SCHEIDING, pos + 5, maak(DEFINITIES, TOP, 0, 1))
            begin && ch == '%' && isNaamBegin(c(pos + 1)) -> {
                val e = eindeNaam(pos + 1)
                val naam = buf.subSequence(pos + 1, e).toString()
                val st = if (naam == "x" || naam == "s") STARTCOND else OPTIES
                klaar(Soort.OPDRACHT, e, maak(DEFINITIES, st, 0, 0))
            }
            ch == '/' && c(pos + 1) == '*' -> klaar(Soort.BLOKCOMMENTAAR, eindeBlokcommentaar(pos), gewoon)
            ch == '\n' -> klaar(Soort.SPATIE, pos + 1, gewoon)
            isSpatie(ch) -> {
                val e = eindeSpaties(pos)
                // Een ingesprongen regel in het definitiedeel is C-code, behalve commentaar.
                if (begin && c(e) != '\n' && e < einde && !begintMet(e, "/*")) lees(pos, maak(DEFINITIES, CREGEL, 0, 0))
                else klaar(Soort.SPATIE, if (c(e) == '\n') e + 1 else e, gewoon)
            }
            begin && isNaamBegin(ch) -> klaar(Soort.DEFINITIE, eindeNaam(pos, "-"), maak(DEFINITIES, DEFRE, 0, 0))
            else -> klaar(Soort.FOUT, pos + 1, gewoon)
        }
    }

    private fun leesRegels(pos: Int, scope: Int) {
        val gewoon = maak(REGELS, GEWOON, scope, 0)
        val ch = buf[pos]
        val begin = isRegelbegin(pos)
        val regelStart = begin || (scope > 0 && alleenSpatiesErvoor(pos))
        when {
            begin && begintMet(pos, "%%") -> klaar(Soort.SCHEIDING, pos + 2, maak(GEBRUIKER, CODE, 0, 0))
            begintMet(pos, "%{") && alleenSpatiesErvoor(pos) -> klaar(Soort.SCHEIDING, pos + 2, maak(REGELS, PROLOOG, scope, 0))
            ch == '\n' -> klaar(Soort.SPATIE, pos + 1, gewoon)
            isSpatie(ch) -> {
                val e = eindeSpaties(pos)
                val leeg = e >= einde || c(e) == '\n'
                if (begin && scope == 0 && !leeg && !begintMet(e, "/*") && !begintMet(e, "%{"))
                    lees(pos, maak(REGELS, CREGEL, 0, 0)) // ingesprongen C-code
                else klaar(Soort.SPATIE, if (leeg && e < einde) e + 1 else e, gewoon)
            }
            ch == '/' && c(pos + 1) == '*' && (!begin || scope > 0) ->
                klaar(Soort.BLOKCOMMENTAAR, eindeBlokcommentaar(pos), gewoon)
            regelStart && scope > 0 && ch == '}' && restVanRegelLeeg(pos + 1) ->
                klaar(Soort.ACCOLADE, pos + 1, maak(REGELS, GEWOON, scope - 1, 0))
            regelStart && begintMet(pos, "<<EOF>>") -> klaar(Soort.RE_EOF, pos + 7, maak(REGELS, REGELRE, scope, 0))
            regelStart && ch == '<' -> klaar(Soort.RE_OPERATOR, pos + 1, maak(REGELS, SCLIJST, scope, 0))
            regelStart -> leesRegex(pos, maak(REGELS, REGELRE, scope, 0))
            else -> klaar(Soort.FOUT, pos + 1, gewoon)
        }
    }

    private fun alleenSpatiesErvoor(pos: Int): Boolean {
        var j = pos - 1
        while (j >= 0 && isSpatie(buf[j])) j--
        return j < 0 || buf[j] == '\n'
    }

    /** Eén stukje van een reguliere expressie; de toestand blijft [toestand]. */
    private fun leesRegex(pos: Int, toestand: Int) {
        val ch = buf[pos]
        when {
            ch == '"' -> klaar(Soort.STRING, eindeAanhaling(pos, '"'), toestand)
            ch == '[' -> klaar(Soort.RE_KLASSE, eindeKlasse(pos), toestand)
            ch == '\\' -> klaar(Soort.RE_ESCAPE, eindeEscape(pos), toestand)
            begintMet(pos, "<<EOF>>") -> klaar(Soort.RE_EOF, pos + 7, toestand)
            begintMet(pos, "{-}") || begintMet(pos, "{+}") -> klaar(Soort.RE_OPERATOR, pos + 3, toestand)
            ch == '{' && isNaamBegin(c(pos + 1)) -> {
                val e = eindeNaam(pos + 1, "-")
                if (c(e) == '}') klaar(Soort.RE_VERWIJZING, e + 1, toestand) else klaar(Soort.RE_TEKST, pos + 1, toestand)
            }
            ch == '{' && c(pos + 1).isDigit() -> {
                var j = pos + 1
                while (c(j).isDigit() || c(j) == ',') j++
                if (c(j) == '}') klaar(Soort.RE_HERHALING, j + 1, toestand) else klaar(Soort.RE_TEKST, pos + 1, toestand)
            }
            ch in "*+?|()/^$.{}<>" -> klaar(Soort.RE_OPERATOR, pos + 1, toestand)
            ch.isLetterOrDigit() -> { var j = pos + 1; while (c(j).isLetterOrDigit()) j++; klaar(Soort.RE_TEKST, j, toestand) }
            else -> klaar(Soort.RE_TEKST, pos + 1, toestand)
        }
    }

    private fun eindeKlasse(pos: Int): Int {
        var j = pos + 1
        if (c(j) == '^') j++
        if (c(j) == ']') j++
        while (j < einde) {
            val ch = buf[j]
            when {
                ch == '\\' -> j += 2
                ch == '[' && c(j + 1) == ':' -> { val k = indexVan(j + 2, ":]"); j = if (k < 0) j + 1 else k + 2 }
                ch == ']' -> return j + 1
                ch == '\n' -> return j
                else -> j++
            }
        }
        return einde
    }

    private fun eindeEscape(pos: Int): Int {
        val n = c(pos + 1)
        return when {
            n == 'x' -> { var j = pos + 2; while (j < pos + 4 && c(j).isLetterOrDigit() && c(j).lowercaseChar() in "0123456789abcdef") j++; j }
            n in '0'..'7' -> { var j = pos + 1; while (j < pos + 4 && c(j) in '0'..'7') j++; j }
            n == '\n' || pos + 1 >= einde -> pos + 1
            else -> pos + 2
        }
    }

    private fun indexVan(van: Int, s: String): Int {
        var j = van
        while (j < einde && buf[j] != '\n') { if (begintMet(j, s)) return j; j++ }
        return -1
    }

    companion object {
        const val DEFINITIES = 0
        const val REGELS = 1
        const val GEBRUIKER = 2
        const val GEWOON = 0
        const val PROLOOG = 1
        const val TOP = 2
        const val CREGEL = 4
        const val DEFRE = 5
        const val REGELRE = 6
        const val NAREGEX = 7
        const val OPTIES = 8
        const val STARTCOND = 9
        const val SCLIJST = 10
        const val NASC = 11
        const val CODE = 12
        fun maak(deel: Int, stand: Int, scope: Int, diepte: Int): Int =
            deel or (stand shl 2) or (scope shl 6) or (diepte shl 10)
        fun deel(toestand: Int) = toestand and 3
        fun stand(toestand: Int) = (toestand shr 2) and 15
        fun scope(toestand: Int) = (toestand shr 6) and 15
        fun diepte(toestand: Int) = toestand ushr 10
    }
}
