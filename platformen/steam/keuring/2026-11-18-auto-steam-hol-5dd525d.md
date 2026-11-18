# Keuring steam-hol, 18-11-2026, automatische keurder
Wat ik keurde: commits 71edf43..5dd525d (de tekst van de wijziging; ik heb niets gedraaid of gezien)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `namen.gd` heeft 24 namen van hooguit 5 letters, kiest de laagste telling en neemt geen naam uit de laatste 6. De telling gaat leeg als alle vrije namen op 3 staan, en een recente naam houdt zijn II of III. | Feit (code gelezen) | hoog | De toetsrun van `toets_systemen.gd` (0 FOUT). De toets doorloopt 226 namen en test ook de randgevallen. |
| 2 | `{titel}` (Sir of Dame) en `{ouder}` (mom of dad) vullen zichzelf uit `{naam}`, zowel in `regels.gd` als in `kroniek_regels.gd`. De toets loopt alle binnen-, val-, vlucht- en hapregels langs met elke naam plus III. | Feit | hoog | Dezelfde toetsrun. |
| 3 | Terugslag en hap per soort gebruiken dezelfde voorwaarden: een opzet, geen terugkomer en geen demofilm. `binnen_soort` wordt in `held_klaar` gewist, dus een terugkomer krijgt hem nooit. | Feit voor de logica, vermoeden voor de bedrading | midden | Een toets of `film.log` waarin `nieuwe_held` en `held_klaar` samen draaien. De huidige toetsen testen `terugslag()` en `hap_soort()` met een nep-strook, niet de keten vanaf de binnenkomst. |
| 4 | `berg_n` rekent nu met `sl.hoeden.size()`. Het ontwerp zegt dat hoeden die nog vallen of vliegen niet meetellen (`berg_tel()`). Tijdens een plof kan de spinraggrens dus voor een grotere berg gelden dan de zichtbare. | Vermoeden | laag | Een beeld of toets tijdens een plof (`toets_berg_wand.gd` of de schermafbeeldingen) die de spinragplaatsing vergelijkt. |
| 5 | De controle `has_method("berg_zichtbaar_bij")` is weggehaald. Die methode staat niet in deze wijziging; `slijm.gd` zit er niet in. | Vermoeden dat hij al bestaat | midden | Zoek `func berg_zichtbaar_bij` in `systemen/slijm.gd`, of een groene scriptlaad-stap in `steam-hol.yml`. |
| 6 | Heldenboek en uitleg zijn zonder he/his/him herschreven (`boek.gd`, `heldensoort.gd`). Een toets leest die bestanden op de oude zinnen. | Feit | hoog | Toetsrun. |
| 7 | Het bewijsbestand voor de terugslag (`lokaal-a1ca6f6-kroniek.txt`) is niet meegestuurd. De claim "2 keer in 13 min, beide na hun opzet" kan ik niet nalezen. | Vermoeden | laag | Het bestand lezen, of de `film.log` van de Windows-run. |
| 8 | Hoe de regels, namen en de spinrag er in de strook uitzien en lezen, kan ik niet beoordelen. | Vermoeden | laag | Daan keurt het beeld en Iris keurt op plezier. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De boektoetsen zijn aangepast aan de nieuwe tekst ("got this one", "The pit won."). Dat volgt uit een bedoelde tekstwijziging, en er zijn veel nieuwe toetsen bij. Het is geen aanpassing om te slagen. | Feit | hoog | Tests niet aangepast om te slagen: voldaan. |
| 2 | `toets_systemen.gd` groeit met ±140 regels en staat al ruim boven de 1500 regels. Het bestand was al te groot, maar wordt nog groter. | Feit | hoog | Bestanden onder ±400 regels: overtreden, bestaand. Zie Kan. |
| 3 | `architectuur.md` is niet bijgewerkt. De rijen Namen, Afloop en Regels noemen titel, ouder, `terugslag()`, `hap_soort()` en `recente_namen` niet. | Feit | hoog | architectuur.md bijgewerkt: niet gedaan. Zie Kan. |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. Alleen verzonnen heldennamen. | Feit | hoog | Geen persoonsgegevens: voldaan. |
| 5 | In commentaar staan cijfers zonder label ("20 keer in 75 min", "±5 naar ±3 keer per uur"). | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK. Zie Kan. |
| 6 | De nieuwe terugslag- en hapregels zijn als CONCEPT gemarkeerd. De wijzigingen in `boek.gd` en `heldensoort.gd` hebben die markering niet. De commits heten "Hats", maar het gaat om Het Hol. | Feit | midden | Spelerstekst alleen als CONCEPT. Zie Kan. |
| 7 | `systemen/kroniek.gd` en `kroniek_regels.gd` laden nu `kern/namen.gd` (via `load`). Dat is een nieuwe koppeling van systemen naar kern, buiten de afspraak met `hol.gd`. | Feit | midden | Afspraak kern en systemen. Zie Kan. |
| 8 | `kunst/3d/begraven.png.import` is gewijzigd (uid en pad). De commit zegt dat de versie van main behouden moet blijven. De kunst is van Daan. | Vermoeden dat het alleen de stand van main volgt | midden | Vergelijk dit bestand met `main`: geen verschil betekent in orde. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Splits `toets_systemen.gd` in themabestanden (ver boven ±400 regels, en nu nog groter).
- Werk `architectuur.md` bij voor `namen.gd`, `afloop.gd` en `regels.gd` (titel, ouder, terugslag, hap per soort, recente namen).
- Controleer in `slijm.gd` of `berg_zichtbaar_bij` bestaat (deel A punt 5).
- Controleer of `berg_n` met `hoeden.size()` tijdens een plof nog klopt met `berg_tel()` (deel A punt 4).
- Voeg een toets toe die `binnen_soort` van `nieuwe_held` tot `held_klaar` volgt.
- Label de losse cijfers in het commentaar met GEZIEN, DERDEN of GOK.
- Zet ook de nieuwe teksten in `boek.gd` en `heldensoort.gd` als CONCEPT tot Thijs ze goedkeurt.
- Controleer of `begraven.png.import` gelijk is aan de versie op main.
- Lever het bewijsbestand voor de terugslag mee.

---
Automatische keurder, model `claude-sonnet-5-5`, 39368 tokens in, 11054 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
