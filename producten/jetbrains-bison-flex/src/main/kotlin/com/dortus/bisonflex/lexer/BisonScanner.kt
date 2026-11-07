package com.dortus.bisonflex.lexer

/**
 * Lexer voor Bison- en Yacc-grammatica's (`*.y`, `*.yy`).
 *
 * Toestand: bit 0-1 het deel (declaraties, regels, epiloog), bit 2-4 de stand
 * (gewoon, in een `{ }`-blok, in `%{ %}`, in de epiloog), bit 8 en hoger de accoladediepte.
 */
class BisonScanner : Scanner() {

    override fun lees(pos: Int, toestand: Int) {
        val deel = toestand and 3
        val stand = (toestand shr 2) and 7
        val diepte = toestand ushr 8
        when (stand) {
            BLOK -> {
                val (s, e) = leesC(pos, bison = true)
                val d = diepte + cDiepteVerschil
                klaar(s, e, if (d <= 0) maak(deel, GEWOON, 0) else maak(deel, BLOK, d))
            }
            PROLOOG -> {
                if (begintMet(pos, "%}")) { klaar(Soort.SCHEIDING, pos + 2, maak(deel, GEWOON, 0)); return }
                val (s, e) = leesC(pos, bison = true)
                // Een C-token mag niet over `%}` heen lezen, behalve strings en commentaar (die slaat Bison over).
                val heel = s == Soort.C_STRING || s == Soort.C_TEKEN || s == Soort.BLOKCOMMENTAAR || s == Soort.REGELCOMMENTAAR
                klaar(s, if (heel) e else kapAfBij(pos, e, "%}"), toestand)
            }
            EPILOOG -> { val (s, e) = leesC(pos, bison = true); klaar(s, e, toestand) }
            else -> leesGewoon(pos, deel)
        }
    }

    private fun leesGewoon(pos: Int, deel: Int) {
        val gewoon = maak(deel, GEWOON, 0)
        val ch = buf[pos]
        when {
            ch == '\n' || isSpatie(ch) -> klaar(Soort.SPATIE, eindeWit(pos), gewoon)
            ch == '/' && c(pos + 1) == '*' -> klaar(Soort.BLOKCOMMENTAAR, eindeBlokcommentaar(pos), gewoon)
            ch == '/' && c(pos + 1) == '/' -> klaar(Soort.REGELCOMMENTAAR, eindeRegel(pos), gewoon)
            begintMet(pos, "%%") -> {
                if (deel == DECLARATIES) klaar(Soort.SCHEIDING, pos + 2, maak(REGELS, GEWOON, 0))
                else klaar(Soort.SCHEIDING, pos + 2, maak(EPILOOGDEEL, EPILOOG, 0))
            }
            begintMet(pos, "%{") -> klaar(Soort.SCHEIDING, pos + 2, maak(deel, PROLOOG, 0))
            begintMet(pos, "%?") -> klaar(Soort.OPDRACHT, pos + 2, gewoon)
            ch == '%' && isNaamBegin(c(pos + 1)) -> klaar(Soort.OPDRACHT, eindeNaam(pos + 1, "-"), gewoon)
            ch == '{' -> klaar(Soort.ACCOLADE, pos + 1, maak(deel, BLOK, 1))
            ch == '<' -> {
                var j = pos + 1
                while (j < einde && buf[j] != '>' && buf[j] != '\n') j++
                if (c(j) == '>') klaar(Soort.TYPE, j + 1, gewoon) else klaar(Soort.FOUT, pos + 1, gewoon)
            }
            ch == '"' -> klaar(Soort.STRING, eindeAanhaling(pos, '"'), gewoon)
            ch == '\'' -> klaar(Soort.TEKEN, eindeAanhaling(pos, '\''), gewoon)
            ch.isDigit() || (ch == '-' && c(pos + 1).isDigit()) -> {
                var j = pos + 1
                while (j < einde && buf[j].isLetterOrDigit()) j++
                klaar(Soort.GETAL, j, gewoon)
            }
            isNaamBegin(ch) || ch == '.' -> {
                // Bison staat `.` en `-` toe in namen (`lr.default-reduction`, `if-stmt`).
                val e = eindeNaam(pos, ".-")
                klaar(soortVanNaam(pos, e, deel), e, gewoon)
            }
            ch == ':' -> klaar(Soort.DUBBELEPUNT, pos + 1, gewoon)
            ch == '|' -> klaar(Soort.STREEP, pos + 1, gewoon)
            ch == ';' -> klaar(Soort.PUNTKOMMA, pos + 1, gewoon)
            ch == ',' -> klaar(Soort.KOMMA, pos + 1, gewoon)
            ch == '[' || ch == ']' -> klaar(Soort.BLOKHAAK, pos + 1, gewoon)
            // Haakjes horen niet bij Bison zelf, maar Ruby gebruikt ze in %token (macro's). Geen foutkleur.
            ch == '(' || ch == ')' -> klaar(Soort.HAAKJE, pos + 1, gewoon)
            ch == '=' -> klaar(Soort.OVERIG, pos + 1, gewoon)
            else -> klaar(Soort.FOUT, pos + 1, gewoon)
        }
    }

    /** Regelnaam bij de definitie (`exp:` of `exp[alias]:`), token (hoofdletters) of gewone naam. */
    private fun soortVanNaam(start: Int, e: Int, deel: Int): Soort {
        if (deel == REGELS) {
            var j = eindeWitEnCommentaar(e)
            if (c(j) == '[') { while (j < einde && buf[j] != ']' && buf[j] != '\n') j++; j = eindeWitEnCommentaar(j + 1) }
            if (c(j) == ':' && c(j + 1) != ':') return Soort.DEFINITIE
        }
        var letter = false
        for (k in start until e) {
            val ch = buf[k]
            if (ch.isLowerCase()) return Soort.NAAM
            if (ch.isLetter()) letter = true
        }
        return if (letter) Soort.TOKEN else Soort.NAAM
    }

    private fun kapAfBij(pos: Int, e: Int, stop: String): Int {
        for (k in pos + 1 until e) if (begintMet(k, stop)) return k
        return e
    }

    companion object {
        const val DECLARATIES = 0
        const val REGELS = 1
        const val EPILOOGDEEL = 2
        const val GEWOON = 0
        const val BLOK = 1
        const val PROLOOG = 2
        const val EPILOOG = 3
        fun maak(deel: Int, stand: Int, diepte: Int): Int = deel or (stand shl 2) or (diepte shl 8)
        fun deel(toestand: Int) = toestand and 3
        fun stand(toestand: Int) = (toestand shr 2) and 7
    }
}
