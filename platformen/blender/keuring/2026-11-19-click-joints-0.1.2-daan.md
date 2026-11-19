# Keuring gratis Click Joints 0.1.2, 19 nov 2026, Daan

Wat ik keurde: tak `claude/blender-0.1.2b`, commit 6e3e768 (diff tegen main raakt alleen deze commit in `click_joints`). Gevraagd door Bram: tagline, de zes meldingen en de sectie 0.1.2 in `producten/blender-gewrichten/CHANGELOG.md`. Meldknop keurde ik al (`2026-11-19-meldknop-daan.md`, ja). De automatische keurder (zelfde commit) gaf ja op regels en code.

## Deel A: werkt en ziet het er goed uit?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Tagline `Ball joints for poseable 3D print figures, with bend range`: zegt wat het is, voor wie, en het ene ding dat anderen niet hebben. Bevat de zoekwoorden "poseable", "3D print", "figures". Zelfde opbouw als de Pro-tagline, dus de twee horen bij elkaar. | feit (gelezen) | hoog | |
| 2 | Alle vijf foutmeldingen beginnen nu met de handeling: "Click Make watertight first:", "Not watertight, use Make watertight:", "Pick a spot where the limb is free:", "Pick another spot:", "Click Place joint in the 3D viewport:". Wie alleen het begin in de statusbalk ziet, weet wat te doen. Dat was mijn kan-punt. | feit (diff gelezen) | hoog | |
| 3 | De slaagmelding "Joint placed. <passing>.<Auto-noot> (x s)": passing en Auto-noot vooraan, tijd achteraan tussen haakjes. Spaties kloppen: de Auto-noot en de cursor-noot beginnen met een spatie. | feit (code nagelopen) | hoog | |
| 4 | CHANGELOG 0.1.2: drie regels, alle drie vanuit de gebruiker. "Changed" klopt met punt 2. "Fixed" (zool van de voet bleef los bij een knie) klopt met de code in `een_lid.py` (Chris, army_man 16 nov: de zool bleef in deel B liggen). Kop `## 0.1.2 (unreleased)` wordt door de awk in `click-joints-uitgave.yml` gevonden (`^## 0.1.2 `). | feit | hoog | |
| 5 | e2e-run 44449886142 op 6e3e768: 5.2.3 groen, 4.2.23 en 5.3.0 liepen nog om 03:27 UTC. | feit (API gelezen) | hoog | de run zelf |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen persoonsgegevens, geen cijferclaims, gewoon Engels. | feit | hoog | harde regels 2 en 5 |
| 2 | `betaald/scharnier.py` kreeg dezelfde meldtekst. Dat komt pas mee in de volgende Pro-versie; de gekeurde Pro 1.0.2 zip verandert niet zolang die niet opnieuw gebouwd wordt. | vermoeden | midden | gekeurde zip is de uitgebrachte zip |

## Moet (blokkeert akkoord)
Geen op inhoud en uiterlijk. Wel geldt de vaste regel: niet uitbrengen voordat de e2e-run op 6e3e768 ook in 4.2.23 en 5.3.0 groen is.

## Kan (mag later)
1. Bij uitbrengen de datum in de kop zetten: `## 0.1.2 (2026-12-..)`.
2. Label "gekeurde stand 014172e" in `toets_zips.py` bijwerken naar 6e3e768.
3. Volgende Pro-versie: dezelfde meldingen meenemen in de Pro-changelog.

Akkoord: ja Click Joints 0.1.2 op 6e3e768 (mits e2e 4.2.23 en 5.3.0 groen)

## Nagekeken 19 nov 04:28 UTC, Daan
Voorwaarde gehaald: e2e-run 44449886142 op 6e3e768 is groen in 4.2.23, 5.2.3 en 5.3.0 (GEZIEN via de GitHub-API). Het akkoord hierboven geldt nu zonder voorbehoud, alleen voor 6e3e768.
