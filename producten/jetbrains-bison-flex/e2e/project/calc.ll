/* Scanner voor de rekenmachine. */
%{
#include "calc.tab.h"
%}

%option noyywrap
DIGIT    [0-9]

%%

{DIGIT}+("."{DIGIT}*)?   { yylval = atof(yytext); return NUM; }
[-+*/()\n]               { return yytext[0]; }
[ \t]+                   ; /* spaties overslaan */
.                        { fprintf(stderr, "onbekend teken: %s\n", yytext); }

%%
