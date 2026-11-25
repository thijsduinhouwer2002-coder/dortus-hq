# Nakeuring Daan: Hats balk, drie moeten uit #36 (issue #41, commit 79d8cd8, 25 nov 2026)

**Akkoord: ja**

| Moet | Opgelost? | Bewijs (GEZIEN) |
|---|---|---|
| 1. sha-controle rood bij verschil, vaste mingw, exe opnieuw uit die bron | ja: ubuntu-24.04, vaste pakketversies, `apt-get update`, `exit 1` bij andere sha256, balk-job `needs: bron` | run 45533202873 op main 79d8cd8: job bron success, balk success |
| 2. TaskbarCreated opvangen en opnieuw aanmelden, met toets | ja: `RegisterWindowMessageW(L"TaskbarCreated")`, `opnieuw()`, plus elke seconde een werkruimte-controle | toets 9: "na herstart verkenner: werkruimte weer 96 px korter (720 -> 624)", schermafbeelding 9 |
| 3. stoppen met de muis bewezen | ja, tweede weg: rechtsklik op het hol geeft Windows-menu, Quit met echte muisklik stopt het spel | toets 11 en schermafbeelding `11-menu-rechtsklik.png` (Pause, Sound, 3 hoogtes, Quit), werkruimte daarna normaal |

Ook gedaan uit de kan-lijst: mutex (toets 10, exitcode 4), herstart na crash (hooguit 5, toets 8), WM_ENDSESSION, hoogte uit argv begrensd 48 tot 400, klem op eigen scherm. 40 regels OK, 0 FOUT.

## Kan (niet blokkerend)
- `hol_balk.c`: bij ERROR_ALREADY_EXISTS de mutex-handle sluiten voor `return 4` (netjes, geen gevolg).
- `herstellen` telt nooit terug; na 50 keer opnieuw aanmelden in één lange sessie stopt het herstel. Terugzetten na een geslaagde aanmelding of per uur.
- Het icoon in het systeemvak zelf blijft ongetoetst; de eerste-start-regel in de kroniek ("right-click the hole for the menu") helpt spelers het menu te vinden.
- Ondertekenen en virusscanners (punt 2 uit #36) blijft open; kost geld, dus pas na een ja van Thijs.
