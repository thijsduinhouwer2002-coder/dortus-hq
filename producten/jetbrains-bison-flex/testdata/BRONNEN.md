# Bronnen testset Bison/Flex

Alle bestanden zijn op 2026-11-07 gedownload van een vaste tag of commit (alle URL's gaven 200). Licentieteksten staan in `licenties/`.

| Bestand | Project | Licentie | Vaste URL | Regels | Nuttig om te testen |
|---|---|---|---|---|---|
| pg-gram.y | PostgreSQL | PostgreSQL | https://raw.githubusercontent.com/postgres/postgres/REL_17_0/src/backend/parser/gram.y | 19513 | groot bestand (prestaties); `%union`, 225 keer `%type <veld>`, oude vormen `%pure-parser` en `%name-prefix`, `%locations`, `%parse-param`/`%lex-param`, veel `%left`/`%nonassoc` |
| pg-scan.l | PostgreSQL | PostgreSQL | https://raw.githubusercontent.com/postgres/postgres/REL_17_0/src/backend/parser/scan.l | 1495 | 11 exclusieve start-condities (`%x`), 48 regels met `<conditie>`, 14 `%option`, veel benoemde definities |
| pg-bootparse.y | PostgreSQL | PostgreSQL | https://raw.githubusercontent.com/postgres/postgres/REL_17_0/src/backend/bootstrap/bootparse.y | 489 | klein; `%union`, `%token <veld>`, `%type <veld>`, `%name-prefix`, `%expect` |
| pg-bootscanner.l | PostgreSQL | PostgreSQL | https://raw.githubusercontent.com/postgres/postgres/REL_17_0/src/backend/bootstrap/bootscanner.l | 133 | klein; 8 `%option`, geen start-condities (eenvoudig basisgeval) |
| jq-parser.y | jq | MIT | https://raw.githubusercontent.com/jqlang/jq/jq-1.7.1/src/parser.y | 1014 | middel; `%code requires`, `%define api.pure`, `%define parse.error verbose`, `%union`, `%destructor`, `%precedence`, `%locations`, meerdere `%parse-param`/`%lex-param` |
| jq-lexer.l | jq | MIT | https://raw.githubusercontent.com/jqlang/jq/jq-1.7.1/src/lexer.l | 186 | inclusieve (`%s`) en exclusieve (`%x`) start-condities door elkaar, `%option` (o.a. reentrant, bison-bridge) |
| ruby-parse.y | Ruby | BSD-2 (Ruby is dubbel: Ruby-licentie of BSDL) | https://raw.githubusercontent.com/ruby/ruby/v3_3_0/parse.y | 16257 | groot; `%define api.pure`, `%printer`, `%initial-action`, `%require`, `%union`, 46 `%type <veld>`, ripper-commentaar `/*% %*/` en veel C-macro's in acties |
| openbsd-httpd-parse.y | OpenBSD httpd | ISC | https://raw.githubusercontent.com/openbsd/src/15f4fe8aa56d9fe749bcb4a9160334c7bec7317e/usr.sbin/httpd/parse.y | 2886 | middel; geen `%union` maar eigen `YYSTYPE` in de proloog, `%token <v.string>` met punt in veldnaam, tabs na directieven, lange proloog en epiloog met C-code |
| thrift-thrifty.yy | Apache Thrift | Apache-2.0 | https://raw.githubusercontent.com/apache/thrift/v0.20.0/compiler/cpp/src/thrift/thrifty.yy | 1341 | extensie `.yy`; `%code requires`, `%union`, 89 regels `%token`/`%type <veld>` |
| thrift-thriftl.ll | Apache Thrift | Apache-2.0 | https://raw.githubusercontent.com/apache/thrift/v0.20.0/compiler/cpp/src/thrift/thriftl.ll | 347 | extensie `.ll`; `%option` (lex-compat, noyywrap, nounput), grote proloog `%{ %}` |

## Licenties

- `licenties/postgresql-LICENSE.txt`: COPYRIGHT uit REL_17_0.
- `licenties/jq-LICENSE.txt`: COPYING uit jq-1.7.1 (MIT voor de jq-code; noemt ook andere delen zoals decNumber en de documentatie).
- `licenties/ruby-LICENSE.txt`: BSDL gevolgd door COPYING uit v3_3_0.
- `licenties/thrift-LICENSE.txt`: LICENSE uit v0.20.0.
- `licenties/openbsd-httpd-LICENSE.txt`: de ISC-kop van parse.y zelf (OpenBSD heeft geen los licentiebestand per programma).

## Wat ontbreekt

- Geen echte C++-grammatica (`%language "c++"` of `%skeleton "lalr1.cc"`) met ruime licentie gevonden: de Thrift-bestanden hebben wel de extensie `.yy`/`.ll` maar maken C-stijl code. De Bison-voorbeelden in C++ zijn GPL.
- onetrue awk (`awkgram.y`) gaf 404 op raw.githubusercontent.com (repo verplaatst of hernoemd) en is vervangen door Ruby.
- De OpenBSD-spiegel heeft geen tags; daarom vastgezet op commit 15f4fe8 (master op 2026-11-07).


Nagekeken door Jet (7 nov 08:17 UTC): aantallen regels gelijk aan de tabel, geen GPL-tekst in de bestanden. Controle door een aparte controleur volgt in de volgende run.
