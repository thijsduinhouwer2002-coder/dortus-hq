# Keuring blender-gewrichten, 25-11-2026, automatische keurder
Wat ik keurde: commits 7621b22..43e79e3 (43e79e3e8), alleen `KAART.md` en `architectuur.md` van het product
Akkoord: ja

Ik zie alleen twee tekstbestanden. Er is geen code, geen test en geen beeld meegestuurd. Dit akkoord gaat dus over de documentatie en niet over het uitbrengen van Pro 1.2.8. Dat ja geeft Daan nog (vraag in #47).

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De KAART noemt moet 2 uit Daans keuring (CI-piek in architectuur.md) als opgelost. Architectuur.md noemt nu 4614 MB in CI op 4.2.23, run 45526260663, en de marge tot 6000 MB (±1,4 GB) klopt met die som. | Feit | Hoog | Het log van run 45526260663 zou het getal 4614 MB bevestigen. |
| 2 | De KAART zegt eerlijk dat het laatste ja op uitbrengen en de regel in `ontwerp.md` nog bij Daan liggen. In `ontwerp.md` staat het laatste Akkoord ja voor Pro 1.2.6, niet voor 1.2.8. | Feit | Hoog | Een nieuw Akkoord-ja van Daan bovenaan `ontwerp.md`. |
| 3 | De commitboodschap noemt ook "tak Bram 1.2.8 op main", "#13 dicht", "Click Cuts hoofdbeeld op plaklijst", "Pro-galerij (#49)" en "Bram gat 2 (#50)". In de diff zie ik daarvan niets, alleen de twee tekstbestanden. | Vermoeden | Midden | De volledige diff, of merge 2fd4925 in de geschiedenis. |
| 4 | Dat het robot-hoofdbeeld GESLAAGD is (Gumroad 1,0 en 1,0; Superhive 2,0 en 1,5) en dat Daan ja zei (#17) kan ik niet nalopen. De uitslagbestanden zijn niet meegestuurd. | Vermoeden | Midden | De bestanden `organisatie/blindtest/uitslag/click-joints-pro-robot-*`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De wijziging bevat geen testbestanden, dus er is geen test aangepast om te slagen. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | Architectuur.md is bijgewerkt met de nieuwe meting en de bijbehorende run. De nieuwe cijfers (±2,5 GB lokaal, 4614 MB in CI) hebben GEZIEN. | Feit | Hoog | architectuur.md bijgewerkt; cijfers met GEZIEN/DERDEN/GOK |
| 2b | "Verkopen: 1 in totaal ($19, 22 nov)" en de blindtestcijfers hebben geen label. Ze verwijzen wel naar een bron of datum. Dit stond er al of heeft een bron. | Feit | Midden | Cijfers met label |
| 3 | In de diff staan geen persoonsgegevens, sleutels of wachtwoorden. | Feit | Hoog | Geen persoonsgegevens |
| 4 | Of `architectuur.md` onder ±400 regels blijft, kan ik niet zien. De regels zijn extreem lang, soms een hele alinea per regel. Leesbaarheid en omvang verdienen aandacht. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 5 | Commit 06:50 valt na het keurmoment (06:37). De tijden in de KAART verschillen ook: eerst "25 nov 04:20", nu "gemeld 25 nov 04:09". | Feit | Hoog | Alleen netheid, geen regelbreuk |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Dit is alleen intern bestandswerk. Een speler of koper ziet er niets van, dus ik kan hier niets beoordelen.
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De KAART wordt een dichte muur van tekst met veel bestandspaden en nummers. | Per versie een korte statusregel bovenaan en de details eronder. | Klein |

## Deel C: is het goed genoeg?
Er zit geen beeld, video, winkeltekst of spel in deze wijziging, dus ik geef geen cijfers. Het robot-hoofdbeeld heeft volgens de KAART de blinde test gehaald (GESLAAGD). Dat is een vermoeden, want ik heb de uitslag niet gezien. Het beeld zelf heb ik ook niet gezien. Voor het plakken blijft Daans keuring op beeld nodig.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Uitbrengen van Pro 1.2.8 pas na het ja van Daan op `ontwerp.md` (#47). Dit akkoord vervangt dat niet.
- De commitboodschap noemt werk (#13, #49, #50, Click Cuts) dat in deze diff niet te zien is. Laat dat in een eigen keuring meekijken.
- `architectuur.md` splitsen of inkorten, als het bestand echt boven ±400 regels is.
- De KAART korter en overzichtelijker maken, en tijden gelijk houden (04:09 tegenover 04:20).

---
Automatische keurder, model `claude-sonnet-5-5`, 24233 tokens in, 3676 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
