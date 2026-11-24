# Keuring blender-gewrichten winkelschermbeelden ronde 7 (w2), 24-11-2026, automatische keurder
Wat ik keurde: commit dfcb55fcd, bestand `producten/blender-gewrichten/e2e/scherm_winkel.py` (alleen de tekst van de diff, geen beelden of runs gezien)
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is hier de belofte van de winkelplaatjes, plus Daans keuring (M1 en M2) waar deze commit naar verwijst. De add-on zelf verandert niet.
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|-----------|-------------------|------------------------------|--------------------------------------|
| 1 | M1: na het snijden krijgt het actieve deel (object en mesh) de naam "Human" (of `CJ_WINKEL_NAAM`), vlak voor `kijk_figuur()`. Dat is wat Daan vroeg. | Feit (uit de diff) | hoog | Het nieuwe w2-beeld op tak `schermen` met "Human" in het paneel. |
| 2 | M2: `SCHAAL_W2` gaat van 1,25 naar 2,0. De opmerking zegt dat stap 2 en 3 dan groot in beeld staan. Zonder run of beeld is niet te zien of stap 3 op 600 px leesbaar is. | Vermoeden | midden | Het w2-beeld op 600 px breed bekijken met de Read-tool. |
| 3 | De opmerking bij `SCHAAL_W2` noemt dat bij 1,5x Folder, STL/3MF en Export al onder de rand bleven, ook na scrollen (run 45447006294). Bij 2x is dat waarschijnlijk erger, dus de Export-knop valt misschien buiten beeld terwijl de nieuwe opmerking "Export STL" in beeld belooft. | Vermoeden | midden | Het w2-beeld: staat de knop "Export STL" er helemaal op? |
| 4 | `gewone_naam()` staat vóór `kijk_figuur()` en na `kies_romp()`. Of `kijk_figuur()` of latere stappen (`testkaart`) het object nog op de oude naam zoeken, staat niet in de diff. | Vermoeden | laag | Run groen, en w1 en w3 nog even goed als eerder. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|-----------|-------------------|-----------|-------|
| 1 | Er zijn geen tests aangepast om te slagen. Het gaat om een proefscript voor schermbeelden. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | Er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | hoog | Geen persoonsgegevens |
| 3 | De bestandslengte is niet te zien (de diff is +14 regels). Waarschijnlijk ruim onder ±400. | Vermoeden | midden | Bestanden onder ±400 regels |
| 4 | `architectuur.md` is niet bijgewerkt. Dat hoeft hier niet, want er verandert niets aan de add-on. | Feit | hoog | architectuur.md bijgewerkt |
| 5 | Het beeld hernoemt het deel naar "Human", terwijl de add-on zelf "mens_A_A_A" levert. Het winkelbeeld laat dus een andere naam zien dan een koper krijgt. Dat is meer een uitleg dan een leugen, maar het is wel een verschil. | Feit | hoog | Winkelplaatjes tonen wat de add-on echt doet |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|-----------|---------------------|------------------------------|
| 1 | Daan vond de naam "mens_A_A_A" een fout lijken. Een koper ziet die naam in het echte gebruik ook. | De add-on zelf nette namen laten geven, bijvoorbeeld "Human_A" en "Human_B", en niet alleen in het winkelbeeld. | klein |
| 2 | Bij 2x zoom past er minder in het paneel, en stap 1 valt bewust weg. | Beoordeel het beeld op de vraag of een koper in één blik ziet dat het gewricht klikt en hoe ver het buigt. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Bekijk het nieuwe w2-beeld met de Read-tool voor je het in de winkel zet. Controleer vooral of "Export STL" nog in beeld is bij 2x (Deel A 2 en 3).
- Laat de add-on de delen zelf een nette naam geven, zodat beeld en echt gebruik gelijk zijn (Deel C 1).
- Werk de opmerking bij `SCHAAL_W2` bij als blijkt dat de exportknop buiten beeld valt.
- Beeld en speelplezier blijven voor Daan en Iris.

---
Automatische keurder, model `claude-sonnet-5-5`, 18309 tokens in, 2870 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
