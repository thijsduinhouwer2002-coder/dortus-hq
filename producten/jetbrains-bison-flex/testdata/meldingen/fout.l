%{
#include "fout.tab.h"
%}
%x GEBRUIKT
%x <weak_warning descr="Unused start condition 'WEG'">WEG</weak_warning>
%x IN_CODE_SC
%%
"a"             { BEGIN(IN_CODE_SC); return IN_SCANNER; }
<GEBRUIKT>"b"   { return NUM; }
<IN_CODE_SC>"c" { BEGIN(INITIAL); }
<<warning descr="Undefined start condition 'ONBEKEND'">ONBEKEND</warning>>"d" { }
<INITIAL>"e"    { }
<*>"f"          { }
%%
