# Keuring blender-gewrichten (Pro 1.2.9, label "Hinge placed"), 25-11-2026, automatische keurder
Wat ik keurde: commit 130d0416d (ae05e08..130d041), bestanden `click_joints/betaald/scharnier_boog.py` en `e2e/toetsen_paneel.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Opdracht: de commit zelf (issue 70, Daan #83 C2). Het ontwerp bevat geen eis over dit label.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het label in het scharnierblok verandert van "Hinge" in "Hinge placed". De reden staat in de code: stap 2 houdt Ball blauw voor het volgende gewricht, dus hier moet staan wat er al is. | Feit (diff) | hoog | n.v.t. |
| 2 | Het label staat in stap 3 (na "3  Fit and export"), zoals de commit zegt. De architectuur zegt dat het scharnierbereik in `STAP3` komt. | Vermoeden | midden | Een groene e2e-run van `test_betaald.py` met de nieuwe toets. Ik zie geen uitslag. |
| 3 | Bij "No end stop found" staat er nu "Hinge placed" met direct daaronder een foutregel. Dat kan tegenstrijdig lezen. | Vermoeden | laag | Een scherm van die situatie in Blender (Read). |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is een toets bijgekomen en er is geen bestaande toets aangepast of versoepeld. De toets slaagt alleen als beide labels bestaan en in de goede volgorde staan (`0 <= stap3 < klaar`). De nieuwe testobjecten worden opgeruimd. | Feit (diff) | hoog | Tests niet aangepast om te slagen: voldaan |
| 2 | `scharnier_boog.py` is langer dan 403 regels, dus rond of boven de grens van ±400. Deze wijziging voegt maar één commentaarregel toe. | Feit (diffnummer) | midden | Bestanden onder ±400 regels: grensgeval, niet door deze wijziging veroorzaakt |
| 3 | De wijziging staat niet in een changelog of releasetekst van Pro. In deze diff zit ook geen manifest. `architectuur.md` noemt versie 1.2.9 al. | Vermoeden | midden | Controleer of het manifest van Pro al 1.2.9 zegt. Een kleine tekst hoeft niet in `architectuur.md`. |
| 4 | De wijziging bevat geen persoonsgegevens, sleutels of cijfers zonder bron. | Feit (diff) | hoog | Geen persoonsgegevens: voldaan |
| 5 | Het label is Engels, zoals de panelregel eist. | Feit | hoog | Zichtbare tekst Engels: voldaan |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik zie geen beeld, alleen tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | "Hinge placed" is duidelijker dan "Hinge": je ziet na het plaatsen wat er staat. Of het in het paneel goed leest, kan ik niet zien. | Een scherm van stap 3 met een geplaatst scharnier laten bekijken door Daan. | klein |
| 2 | Het label heeft nog steeds het icoon `CON_PIVOT`. Een vinkje of ander icoon kan "geplaatst" sterker zeggen. | Smaak, geen eis. | klein |

## Is het goed genoeg?
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | niet te beoordelen | Eén tekstlabel, geen beeld. Ik kan niets naast een concurrent leggen. |
| Zou ik het zelf kopen of bekijken op basis van dit? | niet te beoordelen | Het is geen beeld dat een klant als eerste ziet, dus de blinde test geldt niet. |
| Zou Thijs er trots op zijn? | niet te beoordelen | Dit hoort bij Daan en Iris. |

Ik geef geen cijfers, dus er is ook geen cijfer onder 8. Het akkoord hangt alleen af van de moet-lijst.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Haal de groene e2e-run met de nieuwe toets erbij voor het uitbrengen (zie A2).
- Bekijk de situatie "Hinge placed" met "No end stop found" eronder op een scherm (A3).
- Het akkoord van Daan in `ontwerp.md` geldt tot Pro 1.2.8. Voor het uitbrengen van 1.2.9 is een nieuwe keuring door een agent of Daan nodig.
- `scharnier_boog.py` zit rond of boven de ±400 regels. Splits het bij de volgende grotere wijziging.

---
Automatische keurder, model `claude-sonnet-5-5`, 18949 tokens in, 3655 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
