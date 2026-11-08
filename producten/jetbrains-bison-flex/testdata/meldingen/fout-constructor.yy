%language "c++"
%define api.value.type variant
%define api.token.constructor
%token <int> NUM
%token ALLEEN_SCANNER
%token ONGEBRUIKT
%%
invoer: NUM ;
<weak_warning descr="Unused rule 'los'">los</weak_warning>: NUM ;
%%
