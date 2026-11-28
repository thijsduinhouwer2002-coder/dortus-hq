# Keuring Click Joints sleeplink (#380), 28-11-2026 14:18 NL, automatische keurder
Wat ik keurde: commit bf3208614 (4a0d095..bf32086), 6 bestanden in `producten/blender-gewrichten/`, alleen tekst, een script en een controlescript.
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De README krijgt onder de winkellink een sleeplink naar 0.1.1. De Install-regel noemt hem eerst. Dat is wat #380 vraagt. | Feit (in de diff) | Hoog | De diff zelf. |
| 2 | "Getest in 4.2.23 en 5.3.0: de link installeert en zet aan." Ik zie alleen de bewering en het script, geen log van de run. | Vermoeden | Midden | De uitvoer van `toets_sleeplink.py` met "INSTALL click_joints aan: True" voor beide versies. |
| 3 | Het script doet de stappen van Blender na zonder het dialoogvenster. Het echte slepen met de muis is niet gedaan, en dat staat er eerlijk bij. "It installs in one step" is dus nog niet aangetoond. | Vermoeden | Midden | Eén keer echt slepen in een Blender met browser ernaast (Daan #398). |
| 4 | De zin "Blender tells you when there is an update" is voorzichtig en past bij wat het script meet: de bron blijft aan en zoekt updates bij het starten. | Feit | Midden | De regels "bron blijft aan" in het log. |
| 5 | Het script geeft alleen uitvoer en eist niets (geen assert of exit-code). Het draait niet in de gewone e2e, want het heeft internet nodig. Het is dus een handmatige proef, geen vangnet. | Feit | Hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen add-on-code gewijzigd en geen test aangepast. `architectuur.md` hoeft daarom niet mee. | Feit | Hoog | Tests niet aangepast om te slagen; architectuur.md |
| 2 | De cijfers zijn gelabeld: 156k downloads van JewelCraft als DERDEN, het effect op installs als GOK, de proeven als GEZIEN. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | Ik zie geen persoonsgegevens of sleutels. De sha256 in de links is een openbare bestandshash. | Feit | Hoog | Geen persoonsgegevens |
| 4 | Alle gewijzigde bestanden zijn korter dan 400 regels (het script is 29 regels). | Feit | Hoog | Bestanden onder ±400 regels |
| 5 | Het plakbestand zegt dat het plakken pas na een ja van Daan mag. Dat past bij de regel dat de hoofdchat en Daan live zetten keuren. | Feit | Hoog | Keuring vóór live zetten |
| 6 | Regel 5 van het controlescript vergelijkt de link uit de README (afgekapt vóór `?`) met `archive_url` uit de API. Staat er in de API een `?...` achter, dan geeft hij ten onrechte FOUT. Het FOUT-pad is nagedaan, het GOED-pad nergens aangetoond. | Vermoeden | Laag tot midden | Eén run waarin de README-link gelijk is aan de nieuwste versie en regel 5 `GOED` geeft. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | De zin is kort en duidelijk, en de belofte over updates is eerlijk. | Niets nodig. | klein |
| 2 | Het linkwoord "this link" zegt weinig. De knop op het platform heet "Drag and Drop into Blender". | Gebruik dezelfde woorden als anker, zodat herkenning direct is. | klein |
| 3 | Wie "Allow Online Access" in Blender uit heeft, krijgt mogelijk geen werkende sleep (vermoeden over Blender 4.2 en nieuwer). | Eén korte hint erbij, na de test in een schone Blender zonder online toegang. | klein |
| 4 | Tussen het goedkeuren van 0.1.3 op het platform en het wisselen van de link zit een gat. Dan krijgt een bezoeker "not found". | Draai regel 5 elke dag op een tijdstip, of in een workflow die meldt bij FOUT. | midden |

## Deel C: is het goed genoeg?
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken (link naar het beste voorbeeld van een concurrent) |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | Niet te geven | Ik zie alleen tekst en geen weergave van README of site. De vergelijking met JewelCraft is alleen op idee gedaan, niet naast elkaar. Daan keurt dit in #398. |
| Zou ik het zelf kopen of bekijken op basis van dit? | Niet te geven | Het is één regel. Het verwijdert wel een extra klik, maar of het overtuigt kan ik niet zien. |
| Zou Thijs er trots op zijn? | Niet te geven | Dat hangt af van hoe het er op 390 en 1280 px uitziet, en dat zie ik niet. |

Het gaat om één zin zonder nieuw beeld of hoofdbeeld, dus ik gebruik de blinde test hier niet. Daan beoordeelt het uiterlijk nog (#398). Zonder zijn ja mag het niet geplakt worden.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Laat zien dat de test echt draaide: voeg de uitvoer van `toets_sleeplink.py` voor 4.2.23 en 5.3.0 toe, of verwijs naar het log (A2).
2. Laat het script na afloop een duidelijke uitslag geven, met een exit-code ongelijk aan 0 bij "NIET GEVONDEN" of niet geïnstalleerd (A5).
3. Draai het GOED-pad van regel 5 één keer tegen een versie waarvan je weet dat die klopt. Zo weet je zeker dat de `archive_url` uit de API geen `?...` bevat (B6).
4. Gebruik als linktekst "Drag and drop into Blender", zoals de platformknop (C2).
5. Een hint voor wie online toegang in Blender uit heeft, na een test (C3).
6. Controleer elke dag of de sleeplink de nieuwste is, zodat er geen dagen "not found" staat tussen goedkeuring en wissel (C4).

---
Automatische keurder, model `claude-sonnet-5-5`, 25432 tokens in, 6102 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
