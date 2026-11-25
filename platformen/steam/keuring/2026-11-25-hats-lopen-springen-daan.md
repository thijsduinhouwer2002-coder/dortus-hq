# Keuring Hats: helden lopen, kijken, springen over een val (keurissue #46, issue #25), 25 nov 2026 ±07:00 NL, Daan
Wat ik keurde: commit 087c09a op main (`systemen/held_loop.gd`, `held.gd`, `held_beeld.gd`, `held_opslag.gd`, `toets_held.gd`), film en strip in `producten/steam-hol/bewijs-loop-25/`, Windows-run 45546980006.
Akkoord: ja.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| 1 | `held_loop.gd` schuift per beeldwissel precies `stap_px` (in stukjes van hooguit 8 px met `_onderweg()` ertussen, dus geen sprong over een kolom na een hapering) en het beeld volgt uit `afgelegd`. Glijden kan zo niet. | Feit, code gelezen | hoog |
| 2 | In de film (20 s, 30 fps, ware maat) wisselen de benen van de koning elke paar beelden en staat hij niet te glijden; het kijk-beeld komt los van het lopen. | Feit, beelden zelf uit de mp4 gehaald | midden (software-OpenGL, niet Windows) |
| 3 | Sprong over de put: held 3 knippert rood met "!", springt in ±0,6 s over de stekels, keert later om en springt terug met de zweetdruppel. Niemand loopt over een val. | Feit (GEZIEN in strip en mp4) | hoog |
| 4 | Windows-run 45546980006 groen op tak `claude/steam-hol-loop` 5d186e5. De vijf veranderde .gd-bestanden zijn daar blob voor blob gelijk aan main 087c09a (GEZIEN, sha vergeleken). | Feit | hoog |
| 5 | Eigen dobbelsteen `rng_loop` voor het kijken, zodat de uitkomsten van de vallen gelijk blijven. Netjes. | Feit | hoog |

## Deel B: regels
- `held.gd` 423 en `held_beeld.gd` 404 regels: net boven de ±400 uit `organisatie/regels/bouwen.md`. Geen moet, wel volgende keer splitsen.
- Geen tests versoepeld; toets_held kreeg er zwaardere bij (stappen op 10, 12, 15, 20 fps, 300 helden langs een put).

## Deel C: naast de beste concurrent (lat `organisatie/lat/hats.md`, Rusty's Retirement)
Rusty's robots lopen rustig en leesbaar; dat is de lat voor "stoort nooit". Onze helden lopen nu ook op hun voeten, staan af en toe stil om rond te kijken en een val doet altijd iets wat je kunt lezen. Dat haalt het gevoel van "virus" (gat 1) een stuk weg: het tempo is lager en rustiger. Cijfer 8.

## Kan
1. Gloop eet held 2 nu rond 36 s in plaats van ±27 s. De eerste beloning komt later, terwijl Thijs al zei dat het niet duidelijk is wat je moet doen. Laat Sanne kijken of het vaste begin een held eerder bij Gloop zet.
2. De "!"-ballon komt in de sprong boven de tunnel uit, op de rand van het gras. Leesbaar, maar een paar px lager oogt netter.
3. `held.gd` en `held_beeld.gd` onder de 400 brengen.
4. Duurtest van 60 min afwachten; valt die rood, dan vervalt dit ja.
