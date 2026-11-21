# Keuring tak claude/steam-upload-knop, 21 nov 2026, Daan
Wat ik keurde: commit d17fa36 (`platformen/steam/upload/` en de stap "Depots toetsen" in `steam-uitbrengen.yml`)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `maak-appbuild.sh` weigert `default`, `Default`, `public ` (met spatie), leeg, en elke tak met andere tekens dan a-z 0-9 - _ (zelf gedraaid met nepmap). Hoofdletters worden klein gemaakt (`INTERN` wordt `intern`). | feit | hoog | |
| 2 | `upload.sh` stopt vóór steamcmd bij elke fout uit de exportcontrole of het app-build-script ("Gestopt: n FOUT, niets geüpload"); getest met een .log in vol/ en met tak public. Zonder steamcmd of zonder STEAM_USERNAME stopt hij ook. | feit | hoog | |
| 3 | `upload.sh` slaat zelf niets op: geen wachtwoord, geen geheim, alleen de app-build-bestanden (zonder sleutels) in een tijdelijke map. steamcmd zelf onthoudt na inloggen wel de sessie op die pc (gewoon gedrag van steamcmd). | feit (script) / vermoeden (steamcmd) | hoog / midden | Valve-docs over steamcmd config.vdf |
| 4 | De echte upload in de workflow loopt via game-ci/steam-deploy met `releaseBranch` = de tak die eerst door `maak-appbuild.sh` moest; bij default/public faalt de toetsstap dus vóór de upload. Plus de oude weigering in de bouwstap (regel 152) blijft. Dubbel slot. | feit | hoog | |
| 5 | Droogloop run 44902997403 op d17fa36: success (GEZIEN, GitHub API). | feit | hoog | |
| 6 | Het reservepad controleert het akkoord in `uitgaven.md` niet. Wie een artifact uit een proefdraai (waar controles alleen waarschuwingen zijn) aan `upload.sh` geeft, kan een ongekeurde build op tak `intern` zetten. Niet openbaar, en alleen Thijs draait het, dus klein risico. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen persoonsgegevens, geen sleutels in de repo; appids als variabele, geheimen als secret. | feit | hoog | harde regel 2 |
| 2 | Spelcode en bevroren build niet aangeraakt (diff: alleen workflow en de nieuwe map). | feit | hoog | |
| 3 | Bestanden klein (26 tot 49 regels). | feit | hoog | bouwen.md |
| 4 | Geen geld, geen inloggen door een agent: de echte stap blijft bij Thijs. | feit | hoog | harde regel 1 en 4 |

## Deel C: fijn voor wie het gebruikt (Thijs, paginadag)
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De samenvatting van de run laat per depot de bestandenlijst en het app-build-bestand zien: goed na te kijken. | | |
| 2 | Zonder VERSIE.txt wordt de omschrijving "Het Hol vol, " (de `|| echo` hoort bij `tr`, niet bij `head`). | `versie=$( (head -1 ... ) 2>/dev/null | tr -d '\r'); [ -n "$versie" ] || versie="zonder VERSIE.txt"` | klein |

## Moet (blokkeert akkoord)
Niets.

## Kan (mag later)
1. (A6) Laat `upload.sh` bij een echte upload weigeren als de artifact uit een proefdraai komt, bijvoorbeeld door in VERSIE.txt "proef: true/false" te zetten in de bouwstap en daarop te stoppen. Of noem het risico in LEESMIJ.
2. (C2) Lege omschrijving bij ontbrekende VERSIE.txt.
3. (A3) In de kop van `upload.sh`: "slaat zelf niets op; steamcmd onthoudt de login op deze pc, log uit met `steamcmd +logout +quit` als het een gedeelde pc is."
4. LEESMIJ zegt dat een droogloop op GitHub "ook het reservepad toetst": klopt voor de twee scripts, niet voor `upload.sh` zelf of de steamcmd-aanroep. Eén woord nuance.
