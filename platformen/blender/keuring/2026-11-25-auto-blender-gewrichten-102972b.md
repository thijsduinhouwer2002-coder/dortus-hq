# Keuring blender-gewrichten (KAART.md, Pro 1.2.8 geheugen), 25-11-2026, automatische keurder
Wat ik keurde: commit 102972be2 (a1a4a50..102972b), alleen `producten/blender-gewrichten/KAART.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De wijziging is een statusnotitie op de kaart en bevat geen code. De opdracht (`ontwerp.md`) vraagt hier niets over, dus ik toets alleen of de notitie klopt en bruikbaar is.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Er komt één zin bij: Daan #29 zegt ja op de code en nee op uitbrengen tot M1/M2. Dat is een duidelijke stop voor de uitgave. | Feit (uit de diff) | hoog | n.v.t. |
| 2 | De kaart noemt oorzaak en oplossing van het geheugenprobleem in 4.2: omhulsel H van 214.150 vlakken, nu hooguit 30.000, piek 2,5 GB lokaal en 4,6 GB in CI. Ik kan niet nagaan of dat klopt, want de code (commit 95a72a4) zit niet in deze wijziging. | Vermoeden | midden | Run 45526260663 in het log (groen in 4.2.23, 5.2.3, 5.3.0) en de geheugenregel van de Rigify-stap |
| 3 | De commitmelding zegt dat "Pro 1.2.8 note regel 5" is aangepast, maar `platformen/blender/pro-1.2.8.md` staat niet in de gewijzigde bestanden. | Feit (melding en bestandenlijst spreken elkaar tegen) | hoog | Een `git show --stat` van 102972b, of die note in een eerdere commit |
| 4 | "M1/M2" wordt op de kaart niet uitgelegd. | Feit | hoog | Een verwijzing naar issue #29 of #37 |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De cijfers dragen GEZIEN waar het om eigen metingen gaat (lokaal boven 5 GB, piek 2,5 GB, CI 4,6 GB). Mijn tekst kan dat niet controleren. | Vermoeden | midden | Cijfers met GEZIEN/DERDEN/GOK: label staat er |
| 2 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in. | Feit | hoog | Geen persoonsgegevens |
| 3 | Geen tests aangepast en geen bestand boven ±400 regels erbij. `architectuur.md` hoeft hier niet mee, want dit is geen codewijziging. Of de eerdere codecommit dat bijwerkte, zie ik hier niet. | Feit voor deze diff | hoog | Tests, bestandsgrootte, architectuur.md |
| 4 | De kaart zegt nog "E2e op main: ... 4.2 rood (issue #14)", terwijl de nieuwe zin groen meldt. Dat is groen op commit 95a72a4 en niet per se op main, maar een lezer kan de tegenstrijdigheid verkeerd lezen. | Feit | midden | Een kaart moet de huidige stand geven |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niet van toepassing: het is een interne kaart en niets wat een klant ziet of speelt.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De "Klaar om te plakken"-regel is één lange alinea met oud en nieuw door elkaar. | De stand bovenaan zetten en het verloop eronder splitsen. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing, want er is geen klantbeeld, spel, winkeltekst of site. De blinde test is niet nodig. Er zijn geen cijfers gegeven.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer of `platformen/blender/pro-1.2.8.md` regel 5 echt is aangepast, want de commitmelding en de bestandenlijst kloppen niet met elkaar (Deel A 3).
- Leg M1/M2 uit of verwijs naar het issue (Deel A 4).
- Maak de oude zin "4.2 rood (issue #14)" bij of schrap hem, nu er een groene run is (Deel B 4).
- Splits de lange kaartregel in stand en verloop (Deel C 1).
- Dat 95a72a4 de geheugenoplossing werkelijk bevat en dat run 45526260663 groen is, ligt buiten deze tekstwijziging. De volgende keuring (nakeuring #37) moet dat bij de bron nakijken.

---
Automatische keurder, model `claude-sonnet-5-5`, 18980 tokens in, 2500 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
