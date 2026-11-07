package com.dortus.bisonflex.lexer

/**
 * De soorten tokens die de lexers maken, los van de IDE (zodat ze makkelijk te testen zijn).
 * `Tokens.kt` koppelt elke soort aan een IElementType per taal, `Kleuren.kt` aan een kleur.
 */
enum class Soort {
    SPATIE,
    BLOKCOMMENTAAR,
    REGELCOMMENTAAR,
    /** `%%`, `%{`, `%}`, `%top{`. */
    SCHEIDING,
    /** `%token`, `%define`, `%option`, `%x`, `%empty` enzovoort. */
    OPDRACHT,
    /** Naam van een regel waar hij gedefinieerd wordt (`exp:`), of van een Flex-definitie (`DIGIT [0-9]`). */
    DEFINITIE,
    /** Een token (Bison: naam in hoofdletters). Later verfijnd met de PSI. */
    TOKEN,
    NAAM,
    /** `<veld>` in Bison. */
    TYPE,
    /** Start-conditie in Flex (`%x COMMENT`, `<COMMENT>`). */
    STARTCONDITIE,
    STRING,
    TEKEN,
    GETAL,
    DUBBELEPUNT,
    STREEP,
    PUNTKOMMA,
    KOMMA,
    ACCOLADE,
    HAAKJE,
    BLOKHAAK,
    OVERIG,

    // Flex: reguliere expressies
    RE_TEKST,
    RE_KLASSE,
    RE_ESCAPE,
    RE_OPERATOR,
    RE_HERHALING,
    /** `{naam}` in een reguliere expressie. */
    RE_VERWIJZING,
    /** `<<EOF>>`. */
    RE_EOF,

    // C-code in acties, proloog en epiloog
    C_SLEUTELWOORD,
    C_NAAM,
    C_STRING,
    C_TEKEN,
    C_GETAL,
    C_OPERATOR,
    C_PREPROCESSOR,
    /** `$$`, `$1`, `@1`, `$<veld>$`, `$naam`. */
    C_BISONVARIABELE,
    /** `BEGIN`, `ECHO`, `yytext` en andere namen die Flex zelf geeft. */
    C_FLEXMACRO,

    FOUT,
}
