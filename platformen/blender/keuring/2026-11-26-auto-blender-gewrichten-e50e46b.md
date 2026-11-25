# Keuring blender-gewrichten Check parts (wand vanaf de kom), 26-11-2026, automatische keurder
Wat ik keurde: commit e50e46b72 (9f5f815..e50e46b): `click_joints/betaald/check_delen.py`, `e2e/toetsen_check.py`, `ontwerp.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Moet 1 (scherpe rand langs de bolnaad telt als dunne wand) is aangepakt. `dunne_vlakken` neemt nu alleen vlakken op de bol om het centrum (straal kogel + speling) met de normaal naar het centrum, en meet vanaf daar naar buiten. | Feit dat de code zo werkt. Dat het nu geen vals alarm meer geeft is een vermoeden. | midden | Een groene e2e-run met de nieuwe stap 7 (staaf 6 mm, nul dunne vlakken) in 4.2, 5.2 en 5.3. |
| 2 | Moet 2 is aangepakt: `check_toon` weigert met een melding bij een verborgen, uitgesloten of gelinkt deel. | Feit (diff). Dat dit moet 2 uit issue 42 is, lees ik alleen uit de commitmelding. | midden | Issue 42 naast de diff. |
| 3 | Een echt dunne wand wordt hopelijk nog gevonden. Het filter is strenger geworden (afstandsband rond de kom, normaalrichting), en de bestaande toets met staaf 4 mm (stap 3) is niet aangepast. | Vermoeden | midden | Run waarin stap 3 (staaf 4 mm geeft dunne vlakken en de klik kiest precies die) nog groen is. |
| 4 | Pen en scharnier krijgen geen dunne-wandcontrole meer. Dat staat eerlijk in `ontwerp.md` en in de knoptekst ("ball joint sockets"). | Feit | hoog | Bewust minder dan voorheen. Zie kan 2. |
| 5 | Speling en soort worden gelezen uit `cj_speling_mm` en `cj_soort`, met standaard 0,2 mm en KOGEL. Ik kan niet zien of die sleutels zo op de delen staan. | Vermoeden | laag | Zoeken naar `cj_speling_mm` en `cj_soort` in `gewricht.py`. Een toets met speling 0,3 mm. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is een toets bijgekomen (stap 7) en er is niets verzwakt of weggehaald. | Feit | hoog | Tests niet aangepast om te slagen: ok |
| 2 | Er staat geen run-id of groen resultaat bij de commit. De regel "e2e groen in 4.2, 5.2 en 5.3" in `ontwerp.md` is dus nog een belofte. | Feit dat het ontbreekt | hoog | Cijfers met GEZIEN/DERDEN/GOK. Zie kan 1. |
| 3 | `architectuur.md` staat niet in de wijziging. Het zichtbare stuk noemt `check_delen` niet, maar de tekst is afgekapt. | Vermoeden | laag | architectuur.md bijgewerkt |
| 4 | `check_delen.py` is ruim onder de 400 regels. `ontwerp.md` is al lang en gaat om één alinea. | Feit | hoog | Bestanden onder ±400 regels: ok |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden gezien. | Feit | hoog | Geen persoonsgegevens: ok |
| 6 | Het gratis deel is niet aangeraakt, dus `toets_zips.py` blijft gelijk. | Feit (alleen bestanden in `betaald/` en e2e) | hoog | Gratis build gelijk aan de gekeurde stand: ok |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Ik kan niets zien of spelen. De verandering raakt alleen de telling "N socket faces with a thin wall" en de knoptekst. Vals alarm bij elk gewricht was storend, dus als dit klopt is het voor de gebruiker beter. | Een schermafbeelding van Check parts bij een Good fit (nul dunne vlakken) en bij een Tight-geval. | klein |
| 2 | Wie een pen of scharnier plaatst, ziet nu geen dunne-wandregel meer. Dat kan als "alles is in orde" lezen. | Een korte regel in het paneel dat dit alleen voor kogelgewrichten geldt. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing voor een cijfer. Er is geen beeld, hoofdbeeld, omslag of winkeltekst gewijzigd en ik heb niets gezien om mee te vergelijken. Een cijfer geven zou verzonnen zijn. Daan en Iris keuren plezier en beeld bij de uitgave na 1.2.9, zoals in `ontwerp.md` staat.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Zet de run-id van de groene e2e (4.2, 5.2 en 5.3) in `ontwerp.md` of de commit, met de regel uit stap 7 en uit stap 3 (dunne wand nog gevonden). Dit is mijn grootste twijfel: zonder die run is "gefixt" een vermoeden.
2. Werk de "Af als"-regel in `ontwerp.md` bij ("dunne wand bij een gewricht" geldt nu alleen voor een kogel), of schrijf de pen- en scharnierversie op als open taak.
3. Controleer dat `cj_speling_mm` en `cj_soort` echt op de delen gezet worden, en voeg een toets toe met een andere speling dan 0,2 mm.
4. Controleer `architectuur.md` op een beschrijving van `check_delen` en pas die aan.

---
Automatische keurder, model `claude-sonnet-5-5`, 24194 tokens in, 5608 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
