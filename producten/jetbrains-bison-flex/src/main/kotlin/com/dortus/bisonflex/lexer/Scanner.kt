package com.dortus.bisonflex.lexer

/**
 * Gedeelde basis voor de Bison- en de Flex-lexer: leest één token vanaf een positie,
 * met alle context in een getal (de toestand). Zo kan de IDE na een wijziging midden
 * in het bestand opnieuw beginnen, zonder het hele bestand opnieuw te lezen.
 *
 * Ook de C-code (acties, proloog, epiloog) wordt hier gelezen: een eigen eenvoudige
 * kleuring, geen echte C-ondersteuning (zie ontwerp.md).
 */
abstract class Scanner {
    protected var buf: CharSequence = ""
    protected var einde = 0

    // Uitkomst van de laatste stap.
    var soort: Soort? = null; protected set
    var tokenEinde = 0; protected set
    var nieuweToestand = 0; protected set

    /** Leest het token dat op [pos] begint, in [toestand]. Zet [soort], [tokenEinde] en [nieuweToestand]. */
    fun stap(buffer: CharSequence, pos: Int, eindePositie: Int, toestand: Int) {
        buf = buffer; einde = eindePositie
        if (pos >= einde) { soort = null; tokenEinde = pos; nieuweToestand = toestand; return }
        lees(pos, toestand)
        // Elk token minstens één teken, anders blijft de IDE hangen.
        if (tokenEinde <= pos) tokenEinde = pos + 1
    }

    protected abstract fun lees(pos: Int, toestand: Int)

    protected fun klaar(s: Soort, eindPos: Int, toestand: Int) {
        soort = s; tokenEinde = maxOf(eindPos, 0).coerceAtMost(einde); nieuweToestand = toestand
    }

    // ---- kleine hulpjes ----
    protected fun c(i: Int): Char = if (i < einde) buf[i] else '\u0000'
    protected fun begintMet(i: Int, s: String): Boolean {
        if (i + s.length > einde) return false
        for (k in s.indices) if (buf[i + k] != s[k]) return false
        return true
    }
    protected fun isRegelbegin(i: Int): Boolean = i == 0 || buf[i - 1] == '\n'
    protected fun isSpatie(ch: Char) = ch == ' ' || ch == '\t' || ch == '\r' || ch == '\u000c'
    protected fun isNaamBegin(ch: Char) = ch.isLetter() || ch == '_'
    protected fun isNaamTeken(ch: Char) = ch.isLetterOrDigit() || ch == '_'

    /** Einde van spaties en tabs (zonder regeleinde). */
    protected fun eindeSpaties(i: Int): Int { var j = i; while (j < einde && isSpatie(buf[j])) j++; return j }
    /** Einde van alle witruimte, ook regeleinden. */
    protected fun eindeWit(i: Int): Int { var j = i; while (j < einde && (isSpatie(buf[j]) || buf[j] == '\n')) j++; return j }
    protected fun eindeNaam(i: Int, extra: String = ""): Int {
        var j = i
        while (j < einde && (isNaamTeken(buf[j]) || buf[j] in extra)) j++
        return j
    }
    /** Alleen spaties tot het einde van de regel (of het bestand)? */
    protected fun restVanRegelLeeg(i: Int): Boolean { val j = eindeSpaties(i); return j >= einde || buf[j] == '\n' }
    /** Alleen spaties en eventueel `/* ... */` tot het einde van de regel? */
    protected fun restLeegOfCommentaar(i: Int): Boolean {
        var j = eindeSpaties(i)
        if (begintMet(j, "/*")) j = eindeSpaties(eindeBlokcommentaar(j))
        return j >= einde || buf[j] == '\n'
    }
    /** Einde van witruimte en commentaar. */
    protected fun eindeWitEnCommentaar(i: Int): Int {
        var j = eindeWit(i)
        while (true) {
            j = when {
                begintMet(j, "/*") -> eindeWit(eindeBlokcommentaar(j))
                begintMet(j, "//") -> eindeWit(eindeRegel(j))
                else -> return j
            }
        }
    }
    protected fun eindeRegel(i: Int): Int { var j = i; while (j < einde && buf[j] != '\n') j++; return j }

    protected fun eindeBlokcommentaar(i: Int): Int {
        var j = i + 2
        while (j < einde) { if (buf[j] == '*' && c(j + 1) == '/') return j + 2; j++ }
        return einde
    }

    /** Einde van een string of teken dat met [aanhalingsteken] begint; stopt bij een regeleinde. */
    protected fun eindeAanhaling(i: Int, aanhalingsteken: Char): Int {
        var j = i + 1
        while (j < einde) {
            val ch = buf[j]
            if (ch == '\\' && j + 1 < einde) { j += if (buf[j + 1] == '\r' && c(j + 2) == '\n') 3 else 2; continue }
            if (ch == '\n') return j
            j++
            if (ch == aanhalingsteken) return j
        }
        return einde
    }

    // ---- C-code ----

    /**
     * Leest één C-token op [pos]. Geeft het verschil in accoladediepte terug (+1, -1 of 0)
     * via [cDiepteVerschil]. [bison] zet herkenning van `$$`, `$1`, `@1` aan, anders die van Flex-namen.
     */
    protected var cDiepteVerschil = 0

    protected fun leesC(pos: Int, bison: Boolean): Pair<Soort, Int> {
        cDiepteVerschil = 0
        val ch = buf[pos]
        when {
            ch == '\n' || isSpatie(ch) -> return Soort.SPATIE to eindeWit(pos)
            ch == '/' && c(pos + 1) == '*' -> return Soort.BLOKCOMMENTAAR to eindeBlokcommentaar(pos)
            ch == '/' && c(pos + 1) == '/' -> return Soort.REGELCOMMENTAAR to eindeRegel(pos)
            ch == '"' -> return Soort.C_STRING to eindeAanhaling(pos, '"')
            ch == '\'' -> return Soort.C_TEKEN to eindeAanhaling(pos, '\'')
            ch == '{' -> { cDiepteVerschil = 1; return Soort.ACCOLADE to pos + 1 }
            ch == '}' -> { cDiepteVerschil = -1; return Soort.ACCOLADE to pos + 1 }
            ch == '(' || ch == ')' -> return Soort.HAAKJE to pos + 1
            ch == '[' || ch == ']' -> return Soort.BLOKHAAK to pos + 1
            ch == ';' -> return Soort.PUNTKOMMA to pos + 1
            ch == ',' -> return Soort.KOMMA to pos + 1
            ch == '<' && naInclude(pos) -> {
                var j = pos + 1
                while (j < einde && buf[j] != '>' && buf[j] != '\n') j++
                return Soort.C_STRING to if (c(j) == '>') j + 1 else j
            }
            ch == '#' && isEersteOpRegel(pos) -> {
                val woordEinde = eindeNaam(eindeSpaties(pos + 1))
                return Soort.C_PREPROCESSOR to woordEinde
            }
            bison && (ch == '$' || ch == '@') -> {
                val e = eindeBisonVariabele(pos)
                if (e > pos + 1) return Soort.C_BISONVARIABELE to e
                return Soort.C_OPERATOR to pos + 1
            }
            ch.isDigit() || (ch == '.' && c(pos + 1).isDigit()) -> {
                var j = pos + 1
                while (j < einde && (buf[j].isLetterOrDigit() || buf[j] == '.' || buf[j] == '_' ||
                        ((buf[j] == '+' || buf[j] == '-') && buf[j - 1] in "eEpP"))) j++
                return Soort.C_GETAL to j
            }
            isNaamBegin(ch) -> {
                val e = eindeNaam(pos)
                val woord = buf.subSequence(pos, e).toString()
                val s = when {
                    woord in C_SLEUTELWOORDEN -> Soort.C_SLEUTELWOORD
                    !bison && (woord in FLEX_NAMEN || woord.startsWith("YY_")) -> Soort.C_FLEXMACRO
                    !bison && naBegin(pos) -> Soort.STARTCONDITIE
                    // Namen in hoofdletters zijn in C macro's of constanten, en in acties meestal tokens.
                    woord.count { it.isLetter() } >= 2 && woord.none { it.isLowerCase() } -> Soort.TOKEN
                    else -> Soort.C_NAAM
                }
                return s to e
            }
            else -> return Soort.C_OPERATOR to pos + 1
        }
    }

    /** Staat er `BEGIN(` of `BEGIN ` (of `yy_push_state(`) direct voor [pos]? */
    private fun naBegin(pos: Int): Boolean {
        var j = pos - 1
        while (j >= 0 && isSpatie(buf[j])) j--
        if (j >= 0 && buf[j] == '(') j--
        while (j >= 0 && isSpatie(buf[j])) j--
        val eind = j + 1
        while (j >= 0 && isNaamTeken(buf[j])) j--
        val w = buf.subSequence(j + 1, eind).toString()
        return w == "BEGIN" || w == "yy_push_state"
    }

    /** Staat er op deze regel alleen `#include` voor [pos]? Dan is `<...>` een bestandsnaam. */
    private fun naInclude(pos: Int): Boolean {
        var j = pos - 1
        while (j >= 0 && isSpatie(buf[j])) j--
        val eind = j + 1
        while (j >= 0 && isNaamTeken(buf[j])) j--
        if (buf.subSequence(j + 1, eind).toString() !in setOf("include", "include_next", "import")) return false
        while (j >= 0 && isSpatie(buf[j])) j--
        return j >= 0 && buf[j] == '#' && isEersteOpRegel(j)
    }

    private fun isEersteOpRegel(pos: Int): Boolean {
        var j = pos - 1
        while (j >= 0 && isSpatie(buf[j])) j--
        return j < 0 || buf[j] == '\n'
    }

    /** `$$`, `$1`, `$-1`, `$naam`, `$[naam]`, `$<veld>$`, `$<veld>1`, en hetzelfde met `@`. */
    private fun eindeBisonVariabele(pos: Int): Int {
        var j = pos + 1
        if (buf[pos] == '$' && c(j) == '<') {
            var k = j + 1
            while (k < einde && buf[k] != '>' && buf[k] != '\n') k++
            if (c(k) != '>') return pos + 1
            j = k + 1
        }
        val ch = c(j)
        return when {
            ch == '$' -> j + 1
            ch.isDigit() -> { var k = j; while (c(k).isDigit()) k++; k }
            ch == '-' && c(j + 1).isDigit() -> { var k = j + 1; while (c(k).isDigit()) k++; k }
            isNaamBegin(ch) -> eindeNaam(j, ".")
            ch == '[' -> { var k = j + 1; while (k < einde && buf[k] != ']' && buf[k] != '\n') k++; if (c(k) == ']') k + 1 else pos + 1 }
            else -> pos + 1
        }
    }

    companion object {
        val C_SLEUTELWOORDEN = setOf(
            "auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum",
            "extern", "float", "for", "goto", "if", "inline", "int", "long", "register", "restrict", "return",
            "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void",
            "volatile", "while", "bool", "true", "false", "nullptr", "NULL",
            // C++ (voor .yy en .ll)
            "class", "namespace", "new", "delete", "this", "template", "typename", "public", "private",
            "protected", "virtual", "using", "try", "catch", "throw", "const_cast", "static_cast",
            "dynamic_cast", "reinterpret_cast", "operator", "friend", "explicit", "override", "final",
            "constexpr", "noexcept", "auto", "decltype",
        )
        val FLEX_NAMEN = setOf(
            "BEGIN", "ECHO", "REJECT", "INITIAL", "yytext", "yyleng", "yylval", "yylloc", "yyin", "yyout",
            "yylineno", "yyterminate", "yyless", "yymore", "unput", "input", "yywrap", "yylex",
            "yy_push_state", "yy_pop_state", "yy_top_state", "yyextra", "yyscanner",
        )
    }
}
