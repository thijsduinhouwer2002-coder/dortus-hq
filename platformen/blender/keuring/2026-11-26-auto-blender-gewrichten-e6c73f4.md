# Keuring blender-gewrichten Click Joints gratis 0.1.2, 26-11-2026, automatische keurder
Wat ik keurde: commit e6c73f47b (dd4bc0c..e6c73f4), alleen de tekstwijzigingen; de twee zips kreeg ik niet te zien
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De commit belooft een extensions-zip zonder Pro-regel en een direct-zip met Pro-knoppen. Beide zips ontbreken in wat ik kreeg. | Vermoeden | Laag | Een groene run van `e2e/toets_zips.py` op e6c73f4, of een lijst van de bestanden en tekst in beide zips (geen woord "Pro" in de extensions-zip). |
| 2 | Het manifest gaat naar 0.1.2, met een nieuwe tagline (58 tekens, onder de grens van 64) en de tag Sculpt, die in de lijst van Blender voorkomt. De CHANGELOG-sectie 0.1.2 heeft 3 regels, binnen de grens van 5. | Feit (uit de diff) | Hoog | Geen nodig. |
| 3 | De CHANGELOG meldt "Fixed: voetzool blijft los bij een knie". In deze commit is geen code gewijzigd; alleen de hash van het manifest veranderde in de toets. De fix moet dus al in een eerdere commit zitten. | Vermoeden | Midden | `git log` op de snijcode met die fix, plus een toets die laat zien dat de voet bij het been blijft. |
| 4 | In de bestanden die ik zag staat geen akkoord van Daan voor 0.1.2. KAART zegt zelf "Wacht op Daan". | Feit | Hoog | Een regel "Akkoord: ja" voor 0.1.2 bovenaan `ontwerp.md`, vóór het uitbrengen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | In `toets_zips.py` veranderde alleen de vastgezette hash van `blender_manifest.toml`, en dat past bij de manifestwijziging. De andere hashes bleven gelijk. De toets is niet versoepeld. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Het commentaar in de toets noemt de gekeurde tak `claude/blender-0.1.2b`. Of het manifest daarmee overeenkomt, kan ik niet nagaan. | Vermoeden | Midden | Gekeurd werk uitbrengen |
| 3 | In KAART staat dat de sha256 in `platformen/blender/indienen.md` staat. Dat bestand zit niet in deze commit, dus die verwijzing klopt waarschijnlijk niet. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | De beschrijving van `meld.py` in `architectuur.md` noemt nog "Click Joints 0.1.1" als voorbeeld. De doc is niet bijgewerkt, wat een kleinigheid is. | Feit | Hoog | architectuur.md bijgewerkt |
| 5 | In het manifest staat een zakelijk e-mailadres (al eerder aanwezig, bewust voor de winkel). Er zijn geen sleutels of wachtwoorden en geen nieuwe persoonsgegevens. | Feit | Hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De nieuwe tagline "Ball joints for poseable 3D print figures, with bend range" is duidelijker over de doelgroep dan de oude. Het is een tekstindruk; ik kan niet zien hoe hij in de winkel staat. | Een schermafbeelding van de winkelregel in Extensions. | klein |
| 2 | De changelog is geschreven vanuit de gebruiker. De rating-regel is rustig, want hij vraagt pas na een export. Of het voor de gebruiker prettig voelt, kan ik niet beoordelen. | Een korte speelproef door Daan of Iris. | klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | Niet te beoordelen | Er is alleen tekst en geen beeld; de zips zijn niet bekeken. Daan keurt het uiterlijk. |
| Zou ik het zelf kopen of bekijken op basis van dit? | Niet te beoordelen | Er is geen winkelpagina of plaatje om mee te vergelijken. |
| Zou Thijs er trots op zijn? | Niet te beoordelen | Dat hangt af van de uitslag van Daans keuring. |

Er zijn geen beelden die een klant als eerste ziet, dus de blinde test geldt hier niet. Zonder cijfers is dit geen akkoord voor uitbrengen: Daans keuring blijft nodig.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Meld de run van `toets_zips.py` op e6c73f4 (of de sha256 van beide zips) in KAART of `indienen.md`, zodat de claim GEZIEN is.
- Zorg dat `platformen/blender/indienen.md` echt de sha256 van beide zips heeft. Of pas de verwijzing in KAART aan.
- Noem in de commit of de changelog de commit of toets die de voetzool-fix bewijst.
- Werk het voorbeeld "Click Joints 0.1.1" in `architectuur.md` bij.
- Brengen mag pas na Daans akkoord voor 0.1.2.

---
Automatische keurder, model `claude-sonnet-5-5`, 20624 tokens in, 5495 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
