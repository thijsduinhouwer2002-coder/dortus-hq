# Keuring blender-gewrichten winkelschermbeelden ronde 8, 24-11-2026, automatische keurder
Wat ik keurde: commit 01d560572, bestand producten/blender-gewrichten/e2e/scherm_winkel.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen het proefscript voor winkelbeelden (`zijbalk_omlaag`). De add-on zelf, het manifest en de gratis zip veranderen niet, dus het akkoord op Pro 1.2.6 en de gratis versies blijft ongemoeid. | Feit | hoog | De lijst gewijzigde bestanden bevat alleen `e2e/scherm_winkel.py`. |
| 2 | Het doel is dat bij 2x de zijbalk omlaag staat, met "3 Fit and export" bovenaan en Export STL in beeld. Of dat lukt, kan ik uit de tekst niet halen. De commit zegt dat het lokaal in 5.3.0 getest is, maar er zit geen beeld of loguitslag bij. | Vermoeden | midden | Het nieuwe plaatje van ronde 8 (w2) met Export STL zichtbaar, of de logregel "WINKEL zijbalk omlaag view2d=... hoogte=..." in een groene run. |
| 3 | De opmerking dat het wiel en `deltay` in ronde 7 niets deden, staat als GEZIEN in de commit, maar het bewijs zit niet in deze wijziging. | Vermoeden | midden | Het log van ronde 7 met een ongewijzigde view2d. |
| 4 | Het aantal stappen (9) is vast en afgestemd op één paneellengte. Een andere paneelhoogte of schermgrootte kan de stappen te kort of te lang maken. Er is een override via `CJ_WINKEL_STAPPEN`. | Vermoeden | midden | Plaatjes bij een tweede schermgrootte of Blender-versie. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen test is aangepast om te slagen. Het is een schermscript voor winkelbeelden, geen toets. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | De wijziging is kort: 14 regels erbij, 20 eraf. De bestandslengte van `scherm_winkel.py` is niet te zien, dus ±400 regels is niet te controleren. | Vermoeden | laag | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier niet, want er verandert niets aan de opbouw van de add-on. | Feit | hoog | architectuur.md bijgewerkt |
| 4 | Geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | hoog | Geen persoonsgegevens |
| 5 | Geen cijfers of spelerstekst erbij. De winkelbeelden tonen alleen gratis en Pro-functies zoals eerder goedgekeurd. Welke van de twee op dit plaatje staat, zie ik niet. | Vermoeden | laag | Winkelbeelden op extensions.blender.org alleen gratis functies (ToS 6.2) |
| 6 | De vaste muispositie `venster.x + 1100, venster.y + 950` gaat uit van een groot scherm (minstens ±1100 bij ±950 pixels). Dat is een kwetsbare aanname in een testscript, maar geen regelbreuk. | Vermoeden | midden | Het scherm van de Xvfb-sessie in de workflow |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Ik kan geen beeld zien. Het plaatje met Export STL in beeld is het eigenlijke doel, en dat is nu niet te beoordelen. | Daan keurt het plaatje van ronde 8 zelf, zoals gebruikelijk. | klein |
| 2 | De muis gaat bewust naar een leeg stuk van het beeld tegen een hulpballon. Dat is goed voor het plaatje. | Controleer op het plaatje dat er geen cursor of ballon in beeld staat. | klein |
| 3 | Het paneel is langer dan de zijbalk bij 2x. Voor een koper op een kleine monitor is dat een signaal dat stap 3 snel onzichtbaar wordt. | Overweeg het paneel in te korten of de zijbalk hoger te maken. Dit is een idee voor later. | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet het aantal stappen (9) en de muispositie (1100, 950) af tegen de venstergrootte in plaats van vaste getallen.
- Laat het script de plaatsing controleren: log of "3 Fit and export" en Export STL in beeld liggen, en meld het als dat niet zo is.
- Bevestig met het plaatje of de logregel dat Export STL in beeld staat (Daan, M2).

---
Automatische keurder, model `claude-sonnet-5-5`, 18268 tokens in, 1959 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
