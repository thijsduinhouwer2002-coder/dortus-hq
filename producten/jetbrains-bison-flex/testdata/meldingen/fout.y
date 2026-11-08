%{
int yylex(void);
void yyerror(const char *s);
%}
%token NUM
%token <weak_warning descr="Unused token 'ONGEBRUIKT'">ONGEBRUIKT</weak_warning>
%token IN_SCANNER
%token MET_TEKST "met tekst"
%token IN_CODE
%token tX RUBY_TOKEN(X)
%token <weak_warning descr="Unused token 'WEG'">WEG</weak_warning> 300
%left '+' WEG
%left <weak_warning descr="Unused token 'LINKS'">LINKS</weak_warning>
%nonassoc UMINUS
%type <int> los <warning descr="Undefined symbol 'onbekend_type'">onbekend_type</warning>
%destructor { } <warning descr="Undefined symbol 'nergens'">nergens</warning>
%start invoer
%expect 0
%%
invoer: %empty | invoer regel ;
regel: exp '\n' | error '\n' | <warning descr="Undefined symbol 'ONBEKEND'">ONBEKEND</warning> ;
exp: NUM | tX | exp '+' exp | '-' exp %prec UMINUS | exp '*' exp %prec <warning descr="Undefined symbol 'GEENPREC'">GEENPREC</warning> ;
<weak_warning descr="Unused rule 'los'">los</weak_warning>: NUM ;

los: exp ;
%%
int f(void) { return IN_CODE; }
