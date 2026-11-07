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

%%

input:
    %empty
  | input line
  ;

line:
    '\n'
  | exp '\n'      { printf ("%.10g\n", $1); }
  ;

exp:
    NUM
  | exp '+' exp   { $$ = $1 + $3; }
  | exp '-' exp   { $$ = $1 - $3; }
  | exp '*' exp   { $$ = $1 * $3; }
  | exp '/' exp   { $$ = $1 / $3; }
  | '(' exp ')'   { $$ = $2; }
  ;

%%

void yyerror(const char *s) { fprintf(stderr, "%s\n", s); }
