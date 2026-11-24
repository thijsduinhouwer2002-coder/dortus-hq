# Keuring blender-gewrichten Pro 1.2.8 (knie-midden), 24-11-2026, automatische keurder
Wat ik keurde: commit 4e4166ada (reeks 4c18bfa..4e4166a), drie bestanden onder producten/blender-gewrichten
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De oorzaak is in de tekst logisch beschreven: de randstraal raakte de schuine onderkant van de kniekap (19 mm onder H) en gaf daardoor Tight. Nu tellen de randen niet mee als het lid onder de volle sleuf in het midden doorloopt en aan beide kanten minstens half zo breed is. | Feit (docstring en code), de werking is vermoeden | Midden | Een groene run van `toetsen_knie_midden.py` met `KLAAR 0 FOUT` in 4.2.23, 5.2.3 en 5.3.0. Die uitslag staat niet in de aangeleverde tekst. |
| 2 | De test eist een scharnier met "groen", twee gesloten delen en één stuk per deel, op het midden van beide knieën en 12 mm hoger. Dat dekt de opdracht van de koper die op het kniemidden klikt. | Feit | Hoog | Het log van de run met de regels `[cj-knie-toets]`. |
| 3 | `_anker_breed` kijkt alleen of het lid op diepte `nodig` minstens 0,5 keer de randafstand breed is. De sleuf loopt tot 0,95 keer de rand. Bij een lid dat onderaan scheef of smal toeloopt kan de sleuf aan de zijkant dus nog door de huid zagen, terwijl de randen nu worden overgeslagen. | Vermoeden | Laag tot midden | Een test met een scheef afgesneden of taps lid (bijvoorbeeld een enkel of kuit), vergeleken met het gedrag vóór 1.2.8. |
| 4 | `zaag_diepte` heeft nu een extra parameter `u` met standaardwaarde 1.0. Alleen `scharnier.py` geeft `u` door. Een andere aanroeper, bijvoorbeeld een oudere test, rekent dan stilzwijgend in de verkeerde eenheid. | Vermoeden | Midden | Een zoekopdracht naar `zaag_diepte(` in de hele repo. |
| 5 | `ZAAG` en `ZAAG_REST_MM` worden in `scharnier_neus.py` gebruikt maar komen niet in de diff voor. Ze bestaan waarschijnlijk al in dat bestand. | Vermoeden | Midden | De bestaande definities, of een groene run. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen bestaande test aangepast. Er is alleen een nieuwe toets bijgekomen, dus er is niets aangepast om te slagen. | Feit | Hoog | Tests niet aanpassen om te slagen |
| 2 | De nieuwe toets staat niet in de gewijzigde bestanden van een workflow. Zonder koppeling in `.github/workflows` draait hij nooit vanzelf. | Vermoeden | Midden | Toets in de echte Blender op Actions |
| 3 | `architectuur.md` is niet bijgewerkt, terwijl het gedrag van `zaag_diepte` (wanneer de randen meetellen) wel is veranderd. Het uitleggedeel staat alleen in de docstring. | Feit | Midden | architectuur.md bijgewerkt |
| 4 | De commit heet "Pro 1.2.8", maar er is geen manifest, changelog of versiebestand gewijzigd. De zip draagt dan misschien nog een oud versienummer. | Vermoeden | Laag tot midden | Kloppende versie en changelog bij uitbrengen |
| 5 | De test laadt `proef_mens.py` via `exec` met een tekstvervanging van `"\nmain()\n"`. Dat breekt stil als dat bestand een andere regelopmaak krijgt. | Feit | Midden | Onderhoudbaarheid, geen harde regel |
| 6 | Het testbestand is 126 regels. Bij `scharnier_neus.py` is de lengte niet te zien. In de aangeleverde tekst staan geen persoonsgegevens, sleutels of wachtwoorden. | Feit voor het testbestand en de geheimen, vermoeden voor `scharnier_neus.py` | Midden | Bestanden onder ±400 regels, geen persoonsgegevens |
| 7 | De cijfers in de docstring (19 mm, 12 mm, 5.3.0) zijn als GEZIEN uit regisseur-24 gemerkt. Dat past bij de regel. | Feit | Hoog | Cijfers met GEZIEN, DERDEN of GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan niets zien of spelen, dus dit zijn alleen vermoedens.
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een koper zet de cursor vanzelf op het midden van de knie. Dat geeft nu naar verwachting een scharnier in plaats van de verwarrende melding "Tight: too little limb past this joint to click." | Een run met een beeld van de scharnieren op het kniemidden voor Daan en Iris. | Klein |
| 2 | Zolang het lid ergens echt Tight is, blijft de melding hetzelfde. Een koper weet dan niet dat een paar mm hoger of lager wel past. | Een hint zoals "try 10 mm higher" in de melding. | Midden |
| 3 | De test dekt alleen de robot. Andere figuren (mens, dier) met een kniekap of ronde onderkant zijn niet getoetst op dezelfde knelling. | Een tweede testfiguur met een uitstekende rand, bijvoorbeeld een mens met laarzen. | Midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Draai `toetsen_knie_midden.py` in de workflow (4.2.23, 5.2.3, 5.3.0) en leg het groene log vast voordat 1.2.8 live gaat (B2, A1).
- Toets of de nieuwe regel een scheef of taps lid niet laat doorzagen: let op de afstand 0,5 tegenover 0,95 in `_anker_breed` (A3).
- Zoek alle aanroepen van `zaag_diepte` en geef overal `u` mee, of maak `u` verplicht (A4).
- Werk `architectuur.md` bij met de regel dat randen niet meetellen als het lid onder de sleuf doorloopt (B3).
- Controleer of het versienummer en de changelog van Pro 1.2.8 ergens zijn bijgewerkt (B4).
- Ontwerp.md heeft alleen een ja voor 1.2.6. Voor live zetten is een keuring door een agent en door Daan nodig.

---
Automatische keurder, model `claude-sonnet-5-5`, 22594 tokens in, 4764 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
