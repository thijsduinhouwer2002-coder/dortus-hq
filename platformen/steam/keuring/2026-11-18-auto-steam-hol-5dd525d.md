# Keuring steam-hol (71edf43..5dd525d), 18-11-2026, automatische keurder
Wat ik keurde: commits 71edf43..5dd525d (terugslag en hap per soort, Dame/{ouder}, 24 namen zonder families, zuinige spinrag-grens) tegen `producten/steam-hol/ontwerp.md`
Akkoord: ja

Ik las alleen tekst. Ik draaide geen toetsen en zag geen beelden of testlog. "0 FOUT" uit de commitberichten kon ik dus niet nakijken. Het bestand `lokaal-a1ca6f6-kroniek.txt` kreeg ik niet mee en heb ik niet beoordeeld.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `{titel}` (Sir/Dame) en `{ouder}` (mom/dad) vullen zichzelf uit `{naam}`, in zowel `regels.gd` als `kroniek_regels.gd`, en de naamgenoot-regels gebruiken `{ouder}`. De toets loopt alle binnen/val/vlucht/hap-regels af met elke naam plus III op Sir bij vrouwennamen, ongevulde accolades en lengte. | Feit (uit de code en de toetstekst) | Hoog | Een groene toetsrun in het workflow-log. |
| 2 | `hap_soort()` volgt de belofte in ontwerp.md: eigen hap-regel bij een opzet, geen terugkomer en geen demofilm, en alleen als er geen `hap_hoed` kwam. Zoniet blijft het `val_bewoner`. Alle 7 soorten hebben 2 regels, en de toets eist dat ze passen met " +9". | Feit | Hoog | Toetsrun. |
| 3 | De terugslag zit in `held_klaar`: `binnen_soort` wordt bij binnenkomst gezet en bij afloop weer gewist, zodat het niet in de terugkomers belandt. De getoetste logica (`terugslag()`, `hap_soort()`) klopt. De toetsen roepen alleen die losse functies aan. Dat `held_klaar` ze ook echt kiest, en dat `binnen_soort` niet lekt, wordt nergens getoetst. | Vermoeden | Midden | Een toets die een held door `held_klaar` stuurt met `binnen_soort="ridder"` en de gekozen soort controleert. |
| 4 | `vrije_naam` doet wat de commentaren beloven: 24 namen van hooguit 5 letters, laagste telling eerst, niet uit de laatste 6, en een lege telling zodra alle vrije namen op 3 staan. De bron van de regel (`features.md`, Sanne 16:50) zag ik niet. Het kan dus afwijken van haar tekst zonder dat ik het merk. Randgeval: de telling wordt ook gewist voor namen die op dat moment bezet zijn. Een volgende "Kees" kan dan weer "Kees II" heten terwijl er al een Kees II is gevallen. | Vermoeden | Laag | Dezelfde reeks lopen met een terugkomer erbij, en `features.md` naast de code leggen. |
| 5 | `berg_n` in `hol_vast.gd` telt nu `hoeden.size()` via `berg_zichtbaar_bij`, niet meer de zichtbare berg. Tijdens de ±4 s dat een nachthoed valt kan de spinrag-grens dus anders staan dan de getekende berg. De aanroep heeft geen `has_method`-controle meer en `slijm.gd` stond niet in deze wijziging. Als `berg_zichtbaar_bij` daar ontbreekt, geeft dat een fout bij het tekenen. | Vermoeden | Midden | Zoeken naar `func berg_zichtbaar_bij` in `slijm.gd` (grep), en `toets_berg_wand.gd` plus een beeld tijdens een nachtval. |
| 6 | Heldenboek en soortuitleg zijn zonder he/his/him herschreven, en de toets leest daarvoor de bronbestanden. De boektoetsen kloppen met de nieuwe tekst. "The pit won." wijkt bewust af van Sanne en dat staat in ontwerp.md. | Feit | Hoog | Toetsrun. |
| 7 | `begraven.png.import` staat in de diff met een nieuwe uid en een nieuw pad-hash, terwijl `begraven.png` zelf niet wijzigde. Het commitbericht zegt dat het van main blijft. Dat kan alleen kloppen als main een nieuwere versie heeft dan 71edf43. Het is kunst van Daan, buiten deze opdracht. | Vermoeden | Midden | `git diff main -- producten/steam-hol/godot/kunst/3d/begraven.png.import` moet leeg zijn. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen toets is verwijderd of verzwakt. Alleen de verwachte boek-teksten zijn aangepast, samen met de bewuste tekstwijziging, en er zijn veel nieuwe toetsen bij. | Feit | Hoog | Tests niet aangepast om te slagen: ok |
| 2 | `toets_systemen.gd` was al ver boven de ±400 regels (de diff begint op regel ~1362) en groeit nu met ~140 regels. Er bestaat al een aparte toetsmap en een los toetsbestand (`toets_berg_wand.gd`), dus splitsen kan. | Feit | Hoog | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. De regels voor Namen en Afloop noemen niets over de titel/ouder, de lijst van 24 namen met recente-6-regel, de terugslag en `hap_soort`. In ontwerp.md staat alleen "Dame en hap per soort". De 24 namen, de terugslag en de zuinige spinrag-grens ontbreken. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | In de wijziging staan geen persoonsgegevens, sleutels of wachtwoorden. Alleen verzonnen heldennamen en teamnamen in commentaar. | Feit | Hoog | Geen persoonsgegevens |
| 5 | Cijfers in commentaar missen een label: "20 keer in 75 min", "val_bewoner van ±5 naar ±3 keer per regel per uur", "Iris: hooguit 6". | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | De nieuwe terugslag- en hap-regels zijn in het commentaar als CONCEPT gemarkeerd. De gewijzigde Heldenboek- en uitlegte

---
Automatische keurder, model `claude-sonnet-5-5`, 39287 tokens in, 16000 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
