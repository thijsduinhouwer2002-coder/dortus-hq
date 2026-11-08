%{
#include "fout-constructor.tab.hh"
%}
%%
[0-9]+  { return yy::parser::make_NUM(atoi(yytext)); }
"x"     { return yy::parser::make_ALLEEN_SCANNER(); }
%%
