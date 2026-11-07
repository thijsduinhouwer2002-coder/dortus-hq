/* Scanner for the calculator. */
%{
#include "calc.tab.h"
%}

%option noyywrap
DIGIT    [0-9]

%%

{DIGIT}+("."{DIGIT}*)?   { yylval = atof(yytext); return NUM; }
[-+*/()\n]               { return yytext[0]; }
[ \t]+                   ; /* skip whitespace */
.                        { fprintf(stderr, "unknown character: %s\n", yytext); }

%%
