package com.dortus.bisonflex

/** Voorbeeldtekst voor de kleurenpagina's: de rekenmachine uit de Bison-handleiding. Engels, want gebruikers zien dit. */
object Voorbeelden {
    val BISON = """
        /* Calculator, after the example in the Bison manual. */
        %{
        #include <stdio.h>
        int yylex(void);
        void yyerror(const char *s);
        %}

        %define api.value.type {double}
        %token NUM
        %left '-' '+'
        %left '*' '/'
        %type <double> exp

        %%

        input:
            %empty
          | input line
          ;

        line:
            '\n'
          | exp '\n'      { printf("%.10g\n", $1); }
          ;

        exp:
            NUM
          | exp '+' exp   { $$ = $1 + $3; }
          | exp '-' exp   { $$ = $1 - $3; }
          | '(' exp ')'   { $$ = $2; @$ = @2; }
          ;

        %%

        // Called by the parser on a syntax error.
        void yyerror(const char *s) { fprintf(stderr, "%s\n", s); }
    """.trimIndent() + "\n"

    val FLEX = """
        /* Scanner for the calculator. */
        %{
        #include "calc.tab.h"
        %}

        %option noyywrap yylineno
        %x COMMENT

        DIGIT    [0-9]
        EXP      [eE][-+]?{DIGIT}+

        %%

        {DIGIT}+("."{DIGIT}*)?{EXP}?   { yylval = atof(yytext); return NUM; }
        [-+*/()\n]                     { return yytext[0]; }
        "/*"                           BEGIN(COMMENT);
        <COMMENT>{
          "*/"                         BEGIN(INITIAL);
          .|\n                         ;
        }
        [ \t]+                         ; /* skip blanks */
        <<EOF>>                        { return 0; }
        .                              { fprintf(stderr, "unknown: %s\n", yytext); }

        %%
    """.trimIndent() + "\n"
}
