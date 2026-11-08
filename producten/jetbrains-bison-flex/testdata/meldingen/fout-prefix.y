%{
int yylex(void);
void yyerror(const char *s);
%}
%define api.token.prefix {TOK_}
%token NUM
%token ALLEEN_SCANNER
%token ONGEBRUIKT
%%
invoer: NUM ;
<weak_warning descr="Unused rule 'los'">los</weak_warning>: NUM ;
%%
