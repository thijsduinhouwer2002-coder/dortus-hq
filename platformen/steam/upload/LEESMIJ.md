# Het Hol naar Steam: upload met één knop

Olaf, 21 nov 2026 (opdracht hoofdchat 12:35 NL: paginadag ±8 dec mag niet op handwerk wachten).

## De knop
`.github/workflows/steam-uitbrengen.yml`. Starten door een tak te pushen:
- `uitgave/hats-steam-v0.2.0-proef1`: droogloop. Alle controles, bouwt vol en demo, rooktoets, toetst de exportmappen en schrijft de app-build-bestanden naar de samenvatting. Geen sleutel nodig, niets gaat naar Steam.
- `uitgave/hats-steam-v0.2.0`: echte upload naar de Steam-tak `intern` (nooit `default` of `public`). Live zetten doet alleen Thijs in Steamworks.

Stappen en controles: zie `platformen/steam/uitgaven.md` en de kop van de workflow.

## De scripts in deze map
| bestand | doet |
|---|---|
| `controleer-exportmap.sh <map>` | exe aanwezig en echt (MZ, groter dan 1 MB), geen logs, saves, vdf's of andere verboden bestanden, niet leeg, onder 500 MB, geen rare tekens in namen |
| `maak-appbuild.sh <appid> <map> <tak> <omschrijving> <uit>` | schrijft het app-build-bestand voor steamcmd (één depot, appid+1), weigert `default` en `public` |
| `upload.sh [--droog] <map> [vol\|demo\|beide] [tak]` | reservepad vanaf een eigen pc met steamcmd, op de artifact `steam-depots` van een run. Gebruikt dezelfde twee scripts |

Let op bij `upload.sh`: het weigert een map zonder `VERSIE.txt` en een proefdraai (de knop zet dan "PROEFDRAAI" in `VERSIE.txt`), zodat alleen een echte run met akkoord van Daan naar Steam gaat. Het script slaat zelf niets op, maar steamcmd onthoudt na de eerste keer inloggen de login op die pc (in zijn eigen map `config/`). Draai het dus alleen op de eigen pc van Thijs, en log op een gedeelde pc uit of wis die map.

De workflow gebruikt dezelfde twee scripts, dus een droogloop op GitHub toetst ook het reservepad.

## Wat alleen Thijs kan (na goedkeuring van Valve, staat in `berichten/hoofdchat.md`)
1. In Steamworks: de app en de demo-app bestaan, elk met één depot (standaard appid+1), en een niet-openbare tak `intern`.
2. Een apart bouwaccount met alleen uploadrechten voor deze twee apps (geen geld- of winkelrechten).
3. In de repo, Settings, Variables: `STEAM_APPID` en `STEAM_DEMO_APPID` (appids zijn openbaar).
4. In de repo, Settings, Secrets: `STEAM_USERNAME` en `STEAM_CONFIG_VDF` (één keer met steamcmd inloggen op het bouwaccount met de Steam Guard-code, daarna `config/config.vdf` in base64; uitleg in de README van game-ci/steam-deploy).
Ontbreekt er iets, dan stopt de echte upload met een melding welk ding mist. De droogloop werkt nu al.
