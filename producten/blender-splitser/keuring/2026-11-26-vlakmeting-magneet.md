# Vlakmeting magneetgaten (Daan #150 M1), 26 nov 2026 ±09:20 NL, Productbouwer

**Vraag (Daan #150 M1):** is het stadionvormige lijntje tussen de twee linker magneetgaten op snijvlak 5-7 een groef in de mesh, of alleen schaduw in het beeld?

**Antwoord: geen groef. Het vlak is vlak.** (GEZIEN, e2e run 45777213614, groen in 4.2.23 en 5.3.0, commit 435b457)

## Hoe gemeten
`e2e/toetsen_magneet.py`, functie `vlak_tussen_gaten`, draait elke e2e mee op Suzanne 330 mm, A1 mini, Joint Magnets 8x3:
- per stuk elk paar magneetgaten op hetzelfde vlak (28 paren);
- rays van 1 mm buiten het vlak recht naar binnen, op een raster over de hele stadionvorm om het paar: om de 0,25 mm langs de lijn tussen de middens en om de 0,05 mm dwars erop, tot 0,8 mm buiten de rand van de gaten (de lijn die Daan zag ligt op 4,1 mm, de rand van het gat);
- de gaten zelf en het nummer laten we weg;
- dieper dan 0,02 mm met aan beide kanten dwars binnen 1 mm weer vlak = groef (fout); alleen aan de binnenkant vlak = rand van het snijvlak, daar begint de huid van het model.

**Proef dat de meting werkt:** dezelfde meting op een doos met twee gaten erop, eens vlak en eens met een groef van 0,2 mm diep en 0,3 mm breed op 4,0 tot 4,3 mm naast de lijn (precies waar het lijntje zat). Vlak: 0 groefpunten. Met groef: 1920 groefpunten, diepst 0,200 mm. (GEZIEN, zelfde run)

## Uitslag snijvlak 5-7 (stuk 5 en stuk 7, gaten 2, 3 en 4: het vlak uit het testbeeld)
| Paar | Afstand | Rays raak | Groef | Rand | Scheefste normaal |
|---|---|---|---|---|---|
| 2-4 | 74,9 mm | 57911 | 0 | 0 | 0,00 graden |
| 3-4 | 74,3 mm | 53991 | 0 | 0 | 0,00 graden |
| 2-3 | 117,8 mm | 46706 | 0 | 0 | 0,00 graden |

Gelijk in 4.2.23 en 5.3.0, en aan beide kanten van de snede (stuk 5 en stuk 7). Het vlak ligt binnen 0,02 mm en de normaal staat overal recht. Het lijntje in het beeld zit dus niet in de mesh. Waarschijnlijk (GOK) komt het van de driehoeken: het snijvlak is één veelhoek met gaten, Blender knipt die in lange dunne driehoeken die precies langs de buitenkant van twee gaten lopen (de omhullende van twee cirkels is een stadion), en de cavity-schaduw van het testbeeld tekent die randen.

## Bijvangst
Snijvlak 7-8 (stuk 7 gaten 5-6, stuk 8 gaten 4-5, 89,1 mm): 27 en 26 punten aan de rand van het vlak, waar de huid van Suzanne onder 41,7 graden wegloopt, 24 mm van het dichtstbijzijnde gat. Dat is de vorm van het model, geen gat of groef. De eerste versie van de meting telde 7 daarvan als groef (run 45776302877, ook in de lengterichting gekeken); dwars op de lijn kijken is wat Daans vraag meet.

## Wat dit betekent voor de galerij
Moment 6 gebruikt het magneetbeeld van de Beeldmaker (#137, GESLAAGD, Daan ja #141), niet dit testbeeld (hoofdmanager #144). Daans kan-punt (schuine blik met licht van opzij) geldt alleen voor het testbeeld; dat gaat niet naar de klant, dus niet opnieuw gerenderd.

Opgemerkt, niet van mij om te veranderen: het beeld van de Beeldmaker zegt "Magnet holes in every cut" en "Both sides of every cut get a hole". Daan #12 M1 schreef voor de winkeltekst "the cut faces ... where they fit", omdat de code een gat overslaat waar het niet past (bijvoorbeeld 10x3 in een arm van 12 mm). Gemeld bij de Beeldmaker en Daan.
