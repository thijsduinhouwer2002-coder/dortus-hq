# Keuring blender-gewrichten (toets CJ_HERKANS=2), 23-11-2026, automatische keurder
Wat ik keurde: commit 5aa4aa5e7, bestand `producten/blender-gewrichten/e2e/toetsen_mens.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is het akkoord voor 0.1.1 en 1.0.2 (kniefout). Deze wijziging raakt de add-on niet, alleen een proefscript dat alleen draait met `CJ_HERKANS=2`.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Alleen `e2e/toetsen_mens.py` is gewijzigd, dus de beloofde werking van 0.1.1 en 1.0.2 verandert niet. | Feit (diff) | hoog | Een diff van de add-on-map zonder wijzigingen. |
| 2 | De nieuwe tak staat achter `os.environ.get("CJ_HERKANS") == "2"`. Zonder die variabele wordt er niets vervangen en blijft de gewone run gelijk. | Feit (diff) | hoog | Een groene CI-run zonder de variabele. |
| 3 | De opmerking zegt dat de proef lokaal faalt op elk lid (heup: "too close", schouder: "blocked"). Dat is een claim van de bouwer; ik heb het niet kunnen draaien. | Vermoeden | midden | Een lokale run met `CJ_HERKANS=2` met het log van de regels `laatste plek=... ok=...`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toets wordt niet verzwakt om te slagen. Er komt een strenge toets bij die lokaal rood is, en de bouwer zegt dat eerlijk en houdt hem buiten de e2e. | Feit (diff en commitbericht) | hoog | Tests niet aangepast om te slagen |
| 2 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | hoog | Geen persoonsgegevens |
| 3 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier niet, want er verandert niets aan de add-on. | Feit | hoog | architectuur.md bijgewerkt |
| 4 | De bestandslengte van `toetsen_mens.py` zie ik niet. De diff voegt ±50 regels toe. | Vermoeden | laag | Bestanden onder ±400 regels (`wc -l`) |
| 5 | De cijfers in de opmerking ("0,3 mm", "220 mm", "400 mm") staan er zonder GEZIEN of GOK, maar de tekst zegt wel "Gemeten 23 nov 17:40". | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Niets te zien of te spelen: dit is alleen een proefscript. Geen bevindingen.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niet van toepassing. | n.v.t. | n.v.t. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet in de code of de opmerking wat de proef doet als `CJ_HERKANS=1` en `=2` samen gezet worden. Nu pakt de tweede vervanging de nep van de eerste als "echt" en herstelt de volgorde verkeerd.
- Noem de variabelen om. `heup` en `DOEL2="Left shoulder"` zijn verwarrend, want het advies gaat over de heup. Zet in de opmerking dat je `CJ_HERKANS_LID` moet zetten om de heup te toetsen.
- Zet het herstel van `rigm2` en `figm2` in een `finally`. Bij een andere fout dan `RuntimeError` blijven de vervangingen staan.
- Controleer de bestandslengte van `toetsen_mens.py`. Staat hij boven ±400 regels, splits hem dan.

---
Automatische keurder, model `claude-sonnet-5-5`, 19056 tokens in, 2561 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
