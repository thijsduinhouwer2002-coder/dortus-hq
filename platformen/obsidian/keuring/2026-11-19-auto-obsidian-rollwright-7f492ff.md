# Keuring Rollwright architectuur.md (beeldvergelijking R4), 19-11-2026, automatische keurder
Wat ik keurde: commit 7f492ff2 (417f1b3..7f492ff), alleen `producten/obsidian-rollwright/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen `architectuur.md`. `src/`, `styles.css`, `manifest.json`, `versions.json` en de plaatjes zijn niet veranderd. Het akkoord van Daan voor 0.3.5 blijft dus gelden. | Feit | Hoog | Niets nodig, de lijst met gewijzigde bestanden zegt dit. |
| 2 | De commitregel noemt veel meer: vaste projectmap en maskers voor Bison & Flex, sparse schermen, klok. Die zitten niet in dit stuk en horen in `organisatie/controle/beelden.sh` en de workflow. Ik kan niet zien of die werk echt gedaan is. | Vermoeden | Midden | De diff van `beelden.sh`, `week-test.yml` en `keurder.yml` in dezelfde push. |
| 3 | De tekst beschrijft één bericht per run in `berichten/olaf.md`. Het wordt alleen gemeld als het verschil nieuw is, met de sleutel in `referentie/<product>/main/GEMELD.md`. Een bijna eenkleurig plaatje telt als groot (LEEG). De rode test blijft uit. Dit is een duidelijke, controleerbare beschrijving. | Feit (over de tekst), vermoeden (dat de code het zo doet) | Midden | `beelden.sh meld` en de job `beeldbericht` in de workflow nalopen. |
| 4 | "Eén keer per ISO-week (maandag 04:37 NL, of bij de eerste push naar main van die week)" is een nieuwe belofte over de planning. Ik zie het rooster zelf niet. | Vermoeden | Laag | Het `cron`-veld en de weekcontrole in `.github/workflows/week-test.yml`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt voor de nieuwe werking van de week-test en de beeldvergelijking. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | Er zijn geen tests aangepast en er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | Hoog | Tests niet aangepast om te slagen, geen persoonsgegevens |
| 3 | De bestaande cijfers behouden hun GEZIEN-label (0,36 procent, run 44420801178). De nieuwe zinnen bevatten geen nieuwe cijfers, alleen de planning in punt A4. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | Of het bestand onder ±400 regels blijft, kan ik niet zien, want de tekst is afgekapt. Dit blok is wel één zeer lange regel. | Vermoeden | Laag | Bestanden onder ±400 regels (`wc -l`) |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
1. Controleer in de push dat de scripts en workflows echt zijn aangepast zoals de commitregel en de tekst zeggen (A2 en A3).
2. Controleer het roosterdetail "maandag 04:37 NL" in `week-test.yml` (A4).
3. Splits de lange alinea over de week-test in een paar korte punten, dan blijft hij leesbaar.

---
Automatische keurder, model `claude-sonnet-5-5`, 20265 tokens in, 2312 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
