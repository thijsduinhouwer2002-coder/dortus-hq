%{
#include "fout-prefix.tab.h"
%}
%%
[0-9]+  { return TOK_NUM; }
"x"     { return TOK_ALLEEN_SCANNER; }
%%
