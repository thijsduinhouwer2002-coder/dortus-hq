# Keuring blender-gewrichten, 25-11-2026, automatische keurder
Wat ik keurde: commit b8e7e456d (reeks 369bfca..b8e7e45), alleen `KAART.md` en `architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen twee documenten. Er is geen code, add-on of zip veranderd, dus de belofte aan de gebruiker blijft gelijk. | Feit | Hoog | Niets nodig, de lijst met gewijzigde bestanden toont het. |
| 2 | De nieuwe alinea in architectuur.md zegt dat `GEVRAAGD` het merkje onthoudt, dat er per hertekening één `os.path.exists` is, en dat de voorwaarden in `vraag_beoordeling` eerst gaan. Dat past bij de CHANGELOG ("does not ask again", geen popup). | Vermoeden | Midden | Ik zie de code niet. Een blik in `meld.py` en `vraag_beoordeling` zou de volgorde van de voorwaarden bevestigen. |
| 3 | De KAART zegt dat note regel 20 gelijk is getrokken met de CHANGELOG. `platformen/blender/pro-1.2.9.md` staat niet in deze wijziging. | Vermoeden | Midden | Een diff van dat bestand in een eerdere commit, of de huidige regel 20 naast de CHANGELOG. |
| 4 | De KAART noemt Daans akkoord (#103) en een keuringsbestand. Dat bestand en #103 zie ik hier niet. | Vermoeden | Midden | `platformen/blender/keuring/2026-11-25-pro-1.2.9-beoordeelregel-daan.md` openen en kijken of "Akkoord: ja" erin staat. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen tests aangepast in deze wijziging. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | architectuur.md is bijgewerkt en sluit aan bij de code zoals Daan het vroeg (kan 3). | Feit voor de tekst, vermoeden voor de overeenkomst met de code | Midden | architectuur.md bijgewerkt |
| 3 | De KAART zet GEZIEN bij de e2e-runs en winkellinks, en geeft de herstart en de rode run eerlijk aan. Nieuwe cijfers komen er niet bij. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de gewijzigde regels. | Feit | Hoog | Geen persoonsgegevens |
| 5 | De grootte van de bestanden kan ik niet zien. De regels zijn wel erg lang, maar de wijziging verandert er maar één. | Vermoeden | Laag | `wc -l` op architectuur.md (±400 regels) |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niet van toepassing: er is niets te zien of te spelen veranderd. | Niets nodig. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing. Er is geen beeld, winkeltekst, spel of site veranderd en geen eerste klantbeeld, dus geen blinde test of cijfers nodig.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer of `platformen/blender/pro-1.2.9.md` regel 20 echt gelijk is aan de CHANGELOG. Het bestand zit niet in deze wijziging.
- Zet bij het akkoord van Daan (#103) de link naar het keuringsbestand erbij, zodat het te controleren is.
- Kan 2 uit de KAART (schermbeeld van de beoordeelregel op 600 px) blijft open. Pak dat op bij de volgende schermbeeldrun.
- De alinea over `meld.py` in architectuur.md is erg lang geworden. Splits hem eventueel in een eigen kopje voor de beoordeelregel.

---
Automatische keurder, model `claude-sonnet-5-5`, 23319 tokens in, 2506 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
