# Keuring steam-hol laarsgrap, naamgenoot-pauze en toetsen verhuisd, 19-11-2026, automatische keurder
Wat ik keurde: commits 8f4a6a7..3ff874a (1f63c2792, dd58c2ca8, fef45d11a, d751513a5, 69f14e54e, 03bc55110), 9 bestanden in producten/steam-hol
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De laarsgrap staat nu apart (`naamgenoot_laars`) en uit de gewone voorraad en de kroniekvoorraad. `held_klaar` noteert de naam als de valregel "boot" bevat, en `nieuwe_held` kiest de laarsregel alleen als `ouder_naam(naam)` daarin staat. Dat past bij Iris' klacht (19 nov). | Feit (uit de diff) | hoog | Een toets die een valregel met "boot" laat vallen en daarna een II-held laat binnenkomen. |
| 2 | De pauze van 300 s tussen naamgenoot-regels zit in `naamgenoot_mag`. De toets met 40 II's in 800 s geeft terecht 3 regels (800, 1100, 1400). | Feit (uit de toetscode) | hoog | Een groene run van `toets_namen.gd`. |
| 3 | De koppeling tussen vallen en binnenkomen is niet getoetst: `laars_namen[naam] = true` in `afloop.gd` en `ng_soort` in `binnenkomst.gd`. De toetsen bekijken alleen de voorraad en `ouder_naam`. Het commitbericht zegt "met toets". | Feit | midden | Een toets die `held_klaar` met een "boot"-valregel en `nieuwe_held` samen doorloopt. |
| 4 | `naamgenoot_laars` heeft één regel. Of `regels.kies` bij een lijst van één regel (de laatste 4 per soort en de laatste 10 overgeslagen) een lege tekst teruggeeft, kan ik niet zien. | Vermoeden | laag | Een toets die `kies("naamgenoot_laars", ...)` twee keer achter elkaar aanroept en niet-leeg verwacht. |
| 5 | `laars_namen` en `naamgenoot_laatst` staan niet in de save. Na een herstart komt de laarsgrap voor oudere vallers niet meer. Dat is veilig (de grap komt dan te weinig, nooit onterecht), en `naamgenoot_gezien` is ook per speelbeurt. | Feit | hoog | Geen actie nodig als dit zo bedoeld is. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Ongeveer 145 regels toetsen zijn uit `toets_systemen.gd` naar het nieuwe `toets_namen.gd` verhuisd. Ik zie alle oude toetsen terug, aangevuld met nieuwe. Alleen `LEESMIJ.md` noemt het nieuwe bestand; `steam-hol.yml` zit niet in de wijziging. Als de workflow bestanden één voor één noemt, draaien deze toetsen niet meer in CI. | Vermoeden | midden | Toetsen niet stilletjes laten wegvallen |
| 2 | De oude toetsen zijn niet versoepeld. Ze zijn verplaatst en uitgebreid (laars, pauze, binnen_soort). | Feit | hoog | Tests niet aangepast om te slagen: in orde |
| 3 | `architectuur.md` is bijgewerkt voor Binnenkomst, Namen, Afloop en Regels. De laarsgrap en `laars_namen` staan er niet in. | Feit | hoog | architectuur.md bijgewerkt: grotendeels in orde |
| 4 | `toets_namen.gd` heeft 207 regels. Het bestandsformaat van `strook.gd` na de twee extra regels kan ik niet zien (eerder 512 voor de splitsing). | Vermoeden | laag | Bestanden onder ±400 regels |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden gezien. De laarsregel is bestaande tekst, alleen verplaatst, geen nieuwe spelerstekst. | Feit | hoog | Geen persoonsgegevens, CONCEPT-regel |
| 6 | Commit d751513a5 noemt "logboek", maar er staat geen logboekbestand in de lijst met gewijzigde bestanden. | Vermoeden | laag | Werkafspraak |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Het laarsgrapje is nu rustiger (hooguit eens per 5 min) en klopt met wat er viel. Dat voelt waarschijnlijk minder herhalend, maar ik kon het niet spelen. | Een duurtest van 30 min bekijken, zoals Iris deed. | klein |
| 2 | `naamgenoot_laars` heeft maar één zin. Elke keer dezelfde grap valt na een paar keer op. | Eén of twee varianten erbij, bijvoorbeeld over de laars van de ouder. Sanne schrijft ze, als CONCEPT. | klein |
| 3 | Na een herstart is de laarsband weg (niet bewaard). Een speler merkt dat nauwelijks. | Pas bewaren als het iemand opvalt. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- Bevestig dat `steam-hol.yml` `systemen/toetsen/toets_namen.gd` draait en op 0 FOUT test. Als het niet zo is, voeg de stap toe. Anders valt een groot deel van de naam-, terugslag- en hap-toetsen uit CI.

**Kan**
- Toets de koppeling tussen vallen met "boot" en binnenkomst met `naamgenoot_laars` (A3).
- Toets `kies("naamgenoot_laars", ...)` meerdere keren achter elkaar op niet-leeg (A4).
- Noem `laars_namen` en `naamgenoot_laars` in `architectuur.md` (B3).
- Controleer de lengte van `strook.gd` tegen de grens van ±400 regels (B4).
- Voeg een tweede laarsregel toe, als CONCEPT (C2).
- Controleer waar het genoemde logboek staat (B6).

---
Automatische keurder, model `claude-sonnet-5-5`, 33441 tokens in, 6945 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
