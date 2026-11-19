# Keuring Rollwright architectuur.md (beeldvergelijking l1), 19-11-2026, automatische keurder
Wat ik keurde: commit faf3effd (bereik 510aa24..faf3eff), alleen `producten/obsidian-rollwright/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt één zin toe aan de alinea over de beeldvergelijking: de drie kloktijden in het logboek op l1 tellen niet mee, het paneel zelf wel. Dat past bij "l1 alleen kloktijden" uit de commitmelding. | Feit | hoog | Staat in de diff. |
| 2 | De commitmelding noemt ook dialogen met verschuiving, een kopmasker alleen op het hele IDE-venster en `schermStil` voor hernoem-plaatjes. Daar staat niets van in de diff of in `architectuur.md`. | Vermoeden | midden | De wijzigingen in `beelden.sh` of de e2e-specs in dezelfde commit, als die er zijn. Anders is de melding breder dan de inhoud. |
| 3 | De melding noemt ook een bericht aan de hoofdchat over de Pro-zip. Dat bestand is niet meegestuurd en valt buiten dit oordeel. | Feit | hoog | Het berichtenbestand zelf. |
| 4 | Er is geen code en geen `src/` of `styles.css` veranderd. Het akkoord van Daan voor 0.3.5 blijft dus geldig. | Feit | hoog | Lijst met gewijzigde bestanden. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt, en alleen dat bestand is gewijzigd. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | Er is geen test aangepast. | Feit | hoog | Tests niet aangepast om te slagen |
| 3 | Of `architectuur.md` onder ±400 regels blijft, kan ik niet zien: het bestand is afgekapt. De diff voegt geen regels toe, alleen een zin in een bestaande regel. | Vermoeden | midden | Het regelaantal van het bestand. |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | hoog | Geen persoonsgegevens |
| 5 | De nieuwe zin over de kloktijden heeft geen GEZIEN-label en er is geen verschilbeeld bij genoemd. Het is een beschrijving van gedrag, geen cijfer, dus geen overtreding. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Zet in de commitmelding of in `architectuur.md` waar de maskers voor de dialogen, het hele IDE-venster en `schermStil` staan, zodat de melding klopt met wat er in de commit zit (A2).
- Voeg een GEZIEN-verwijzing toe voor de kloktijden op l1 (een run met alleen die tijden als verschil), zoals bij de andere uitzonderingen in dezelfde alinea (B5).
- Controleer dat het bestand onder ±400 regels blijft (B3).

---
Automatische keurder, model `claude-sonnet-5-5`, 20478 tokens in, 2176 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
