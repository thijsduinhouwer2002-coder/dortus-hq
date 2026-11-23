# Keuring e2e plaatje 4 wacht op shaders, 23 nov 2026, Daan
Wat ik keurde: commits e890047 en 440a52d (en de logregel van na 04:10 UTC), `producten/blender-gewrichten/e2e/schermen.py` en `scherm_kleur.py`, run 45100503130.
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Run 45100503130 is groen op 4.2.23, 5.2.3 en 5.3.0 (head 440a52d). | feit (GEZIEN, API) | hoog | |
| 2 | In 4.2.23 en 5.3.0 greep de wacht: log "SHADERS klaar na 1 s extra wachten"; in 5.2.3 was er geen wacht nodig. | feit (GEZIEN, joblogs) | hoog | |
| 3 | Plaatje 4 (X-scherm) zelf bekeken voor 4.2.23 en 5.3.0: drie cilinders vol in kleur, geen "Compiling shaders" in beeld, labels leesbaar. | feit (GEZIEN, Read) | hoog | |
| 4 | De check eist kleur op alle drie cilinders (verzadiging boven 40), dus een half klaar beeld (twee kleur, één grijs) gaat niet door. | feit (code) | hoog | |
| 5 | Kan de wacht niet meten (geen schermafdruk), dan schiet hij meteen: geen eindeloze lus. Na 40 pogingen staat er nu een eigen regel "nog niet klaar", dus een mislukte wacht is te zien. | feit (code) | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen test versoepeld: de beeldvergelijking en de kleurmeting zijn gelijk gebleven, alleen het moment van schieten wacht langer. | feit | hoog | tests niet aangepast om te slagen |
| 2 | Bestanden blijven klein (schermen.py en scherm_kleur.py ruim onder 400 regels). | feit | hoog | bestandsgrootte |
| 3 | Logboek met GEZIEN bij de runs. | feit | hoog | eerlijk |

## Deel C: zou een gebruiker het merken?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Alleen testwerk; de koper ziet niets. Wel: minder valse "anders"-meldingen, dus minder tijd verloren aan nep-fouten. | | |

## Moet / Kan
Moet: geen.
Kan 1: de teller heet "s" maar telt pogingen (elke poging is 1 s plus een schermafdruk); prima, maar noem het in de logregel "pogingen" als het ooit verwart.
Kan 2: 4.2.23 meet donkerder kleuren dan 5.x (Good fit belicht #4EA181 tegen #67B193). Dat is een verschil tussen Blender-versies, geen fout; goed om te weten bij het vergelijken van winkelbeelden.
