# Keuring steam-hol, 19-11-2026, automatische keurder
Wat ik keurde: commits 9878bed..70b13d2 (d751513a, 69f14e54, 03bc5511), vier bestanden
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `ontwerp.md` zegt niets over de naamgenoot-regel. De wijziging volgt de aanleiding in de code: Iris keuring 23 punt 1, zes keer dezelfde regel tussen 884 en 1363 s. `naamgenoot_mag` laat hooguit één regel per 300 s door, alleen bij II of III en één keer per voornaam. | Feit (uit de diff) | Hoog | Een duurtest waarin binnen 300 s niet twee naamgenoot-regels staan. |
| 2 | Wordt de regel geweigerd, dan valt de held door naar de gewone binnenkomstregel en blijft zijn voornaam vrij. Dat past bij de code-opmerking en wordt niet gestraft. | Feit | Hoog | Niet nodig. |
| 3 | `s.t` is in de strook het tijdsveld in seconden en `naamgenoot_laatst` begint op -1000. Het veld `t` zelf staat niet in de diff. Alleen de nep-strook in de toets heeft het. | Vermoeden | Midden | Een regel `var t` in `strook.gd` die per speelbeurt in seconden telt. |
| 4 | De toets "40 II's in 800 s geven 3 regels" rekent op `NM.NAMEN` als platte lijst met 24 namen. De toets is verder logisch: 800, 1100 en 1400 s zijn de drie momenten. | Vermoeden | Midden | De run van `steam-hol.yml` met 0 FOUT, en `NAMEN` in `namen.gd` als platte stringlijst. |
| 5 | De toets voor `binnen_soort` dekt dief die vlucht met `vlucht_dief`, de terugkomer-kaart zonder `binnen_soort`, en de gewone vluchtlijst bij terugkeer. Ik kan de uitslag niet zien. | Vermoeden | Midden | Dezelfde toetsrun: de drie `binnen_soort`-regels en de vier `naamgenoot`-regels groen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn alleen toetsen toegevoegd, geen bestaande veranderd of versoepeld. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `toets_systemen.gd` staat al op ruim 1400 regels en krijgt er 61 bij. Dat is ver boven ±400. Het bestaande probleem wordt groter. Er bestaat al een los toetsbestand (`toets_berg_wand.gd`), dus splitsen kan. | Feit | Hoog | Bestanden onder ±400 regels |
| 3 | `strook.gd` krijgt één regel erbij. De huidige lengte staat niet in de diff. | Vermoeden | Laag | Regelaantal van `strook.gd` (was na splitsen onder ±400) |
| 4 | `architectuur.md` is bijgewerkt: nieuwe rij Binnenkomst en aangepaste rijen Namen, Afloop en Regels. | Feit | Hoog | architectuur.md bijgewerkt |
| 5 | De toets "binnen_soort" bootst de terugkomer-kaart na als Vos met pensioen gaat bij zaad 7. Dan is de controle "kaart zonder `binnen_soort`" vanzelf waar. Het uitstapje wordt wel geprint. | Feit | Midden | Tests niet aangepast om te slagen (kan-punt, geen versoepeling van een bestaande toets) |
| 6 | Er staan geen persoonsgegevens, sleutels, cijfers zonder bron of nieuwe spelerstekst in de wijziging. | Feit | Hoog | Persoonsgegevens, cijfers, CONCEPT-regel |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Zet de nieuwe toetsen in een eigen bestand, zoals `toets_berg_wand.gd`. `toets_systemen.gd` is ruim 1400 regels en groeit nu verder.
2. Laat de toets voor `binnen_soort` falen als Vos met pensioen gaat, of kies een zaad waarbij dat vaststaat, zodat de nagebootste kaart de controle niet meer vanzelf laat slagen.
3. Controleer in de run van `steam-hol.yml` dat `NM.NAMEN` een platte lijst is en dat `strook.gd` een veld `t` heeft. Ik kon beide niet uit de tekst halen. Een rood vinkje op die toets betekent dat het niet klopt.
4. Controleer het regelaantal van `strook.gd` na de nieuwe regel.

---
Automatische keurder, model `claude-sonnet-5-5`, 19386 tokens in, 3813 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
