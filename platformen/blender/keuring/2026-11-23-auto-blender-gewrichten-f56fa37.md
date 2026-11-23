# Keuring blender-gewrichten (TIGHT_KORT-zin en architectuur), 23-11-2026, automatische keurder
Wat ik keurde: commit f56fa3737 (65b05f1..f56fa37): `architectuur.md` en `click_joints/betaald/scharnier_neus.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één tekstregel: `TIGHT_KORT` is korter ("Tight: too little limb past this joint to click. Try a spot further from the end."). De betekenis blijft gelijk: een kort lid onder H, ga verder van het uiteinde zitten. | Feit | Hoog | Het diff laat alleen die constante veranderen. |
| 2 | De rig-knop zoekt op "tight" in kleine letters om de volgende plek te proberen. De nieuwe zin begint nog met "Tight", dus dat gedrag blijft werken. | Feit | Hoog | Architectuurtekst (`kogel_reden`-alinea) en de nieuwe zin samen gelezen. |
| 3 | Dit past niet bij de akkoordregel in `ontwerp.md` (gratis 0.1.1, Pro 1.0.2). Het gaat om Pro 1.1 (rig). De opdracht noemt geen eis voor deze tekst. | Feit | Midden | Een eis voor Pro 1.1 in `ontwerp.md` zou dit bevestigen of weerleggen. |
| 4 | Een toets die de oude zin letterlijk vergelijkt, kan nu falen. Het diff bevat geen toetsbestand. | Vermoeden | Laag | Een groene run van `toetsen_rig.py` en `toetsen_scharnier.py` op deze commit. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt: de nieuwe zin staat erin en `kogel_reden` is beschreven. | Feit | Hoog | Architectuur bijgewerkt |
| 2 | In het diff is geen toets aangepast om te slagen. | Feit | Hoog | Tests niet aangepast |
| 3 | Het diff bevat geen persoonsgegevens, sleutels of cijfers zonder label. | Feit | Hoog | Geen persoonsgegevens, cijferlabels |
| 4 | Bestandsgrootte onder ±400 regels is niet te zien, want het diff toont alleen de gewijzigde regels. `architectuur.md` heeft zeer lange regels. | Vermoeden | Laag | Regelaantal van `scharnier_neus.py` en `architectuur.md` |
| 5 | Het diff laat de code van `kogel_reden` niet zien. De beschrijving verwijst naar een eerdere commit of een andere wijziging. | Vermoeden | Midden | `rig.py` en `toetsen_rig.py` in de commits ervoor |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De nieuwe melding is korter en zegt wat te doen. Of hij op een echt scherm in het paneel past, kan ik niet zien. | Een schermafbeelding van de melding in de zijbalk en de statusbalk. | Klein |
| 2 | "past this joint" is voor een niet-Engelse koper net iets abstract. | "Too little limb beyond this joint" is mogelijk duidelijker. Dit is smaak. | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer in de CI of de toetsen voor `TIGHT_KORT` nog groen zijn (A4).
- Zet de "akkoord Daan" over de nieuwe zin ook in `ontwerp.md`, zodat de keten te volgen is. Nu staat het alleen in `architectuur.md` en ik kan het niet nagaan.
- Voeg bij de melding een schermafbeelding toe, dan kan Daan hem op plek en leesbaarheid beoordelen.

---
Automatische keurder, model `claude-sonnet-5-5`, 24233 tokens in, 2157 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
