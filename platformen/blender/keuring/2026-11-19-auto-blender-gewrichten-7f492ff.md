# Keuring blender-gewrichten beeldvergelijking R4, 19-11-2026, automatische keurder
Wat ik keurde: commit 7f492ff2 (417f1b3..7f492ff), alleen `producten/blender-gewrichten/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen de beschrijving van de week-test in `architectuur.md`. De add-on, de beloofde functies en het akkoord van Daan in `ontwerp.md` veranderen niet. | Feit | hoog | De lijst met gewijzigde bestanden bevat alleen dit ene bestand. |
| 2 | De tekst beschrijft nu: één run per ISO-week (maandag 04:37 NL of de eerste push naar main), één kort bericht per run, geen herhaling via een sleutel in `GEMELD.md`, en een leeg plaatje telt als LEEG. Dat past bij de commitbericht. | Feit (over de tekst) | hoog | Vergelijking van het diff met het commitbericht. |
| 3 | Of `week-test.yml`, `beelden.sh` en `beeldvergelijk.py` echt zo werken (job `beeldbericht`, `beelden.sh meld`, LEEG-regel), staat niet in deze wijziging en kan ik niet nagaan. | Vermoeden | midden | De workflowbestanden in dezelfde commit, of een groene week-run met precies één bericht in `berichten/bram.md`. |
| 4 | Het commitbericht noemt ook Bison & Flex (projectmap, maskers), sparse schermen en een klok. Dat valt buiten dit product en staat niet in het diff. | Vermoeden | laag | Keuring van die producten, of de volledige diff van de commit. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt in dezelfde commit als de verandering die het beschrijft. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | Er zijn geen tests of testgrenzen aangepast. De grens van 0,02 procent staat er al en blijft gelijk. | Feit | hoog | Tests niet aangepast om te slagen |
| 3 | Persoonsgegevens, sleutels of wachtwoorden staan niet in het diff. De "sleutel" in `GEMELD.md` is een meldingssleutel, geen geheim. | Feit | hoog | Geen persoonsgegevens |
| 4 | De lengte van `architectuur.md` is niet te zien, want de tekst is afgekapt. Het bestand is wel erg lang en bevat veel in één regel. | Vermoeden | laag | Regel: bestanden onder ±400 regels. `wc -l` op het bestand zou het bevestigen. |
| 5 | De nieuwe beweringen "geplande runs vallen hier vaak weg" en "nu 5.4.0-alpha / 5.2.4-stable" hebben geen label GEZIEN, DERDEN of GOK. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | Er zijn geen spelerstekst van Hats en geen AI-beeld of -geluid voor Steam in de wijziging. | Feit | hoog | Hats en Steam |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij "geplande runs vallen hier vaak weg" een label (GEZIEN met een runnummer, of GOK).
- Controleer de lengte van `architectuur.md`. Splits het bestand als het ruim boven de 400 regels zit, en zet de week-test dan in een eigen bestand.
- Laat het commitbericht alleen noemen wat in de commit zit. Zo blijft het werk aan Bison & Flex vindbaar bij dat product.
- Controleer in de eerstvolgende week-run dat er echt één bericht komt en dat een tweede run met hetzelfde verschil stil blijft. Daarmee is de nieuwe werking bevestigd.

---
Automatische keurder, model `claude-sonnet-5-5`, 18431 tokens in, 2216 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
