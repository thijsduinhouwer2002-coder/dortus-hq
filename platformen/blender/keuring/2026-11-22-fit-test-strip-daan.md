# Keuring Fit test strip (losse STL plus tekst), 22 nov 2026, Daan
Wat ik keurde: `commercie/blender-click-joints/testprint/fit-test-strip.stl` en `fit-test-strip-plus-testset.stl` (commit 63706eb), beelden in `testprint/beeld/`, tekst in `platformen/blender/fit-test-strip-tekst.md`.
Akkoord: nee (twee moet-punten, allebei klein)

Hoe ik keek: zelf met trimesh geladen, doorsnede op 0,3 mm boven het bed gemaakt en van onder bekeken (gespiegeld, zoals je de onderkant in je hand ziet): `2026-11-22-fit-test-strip-onderkant.png` en `-cijfers-van-onder.png`.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | 14 losse delen, waterdicht, alles op z = 0, 140 x 84,1 x 44,5 mm. A (bol boven) op y 10, B (kom boven) op y 42, op volgorde 0.10 tot 0.30. | feit (GEZIEN, trimesh) | hoog | |
| A2 | Cijfers staan in beide delen en lezen goed als je de onderkant bekijkt: A recht, B 180 graden gedraaid (niet gespiegeld, punt staat boven). Gewoon het deel omdraaien. | feit (GEZIEN, doorsnede) | hoog | |
| A3 | **Cijfers te klein en te dun voor het bed.** Letterhoogte 2,5 mm (LETTER_MM 3,6 uit `testkaart.py`), lijnen 0,3 tot 0,5 mm breed: bij 8 van de 40 lettervormen is de groef smaller dan 0,4 mm (GEZIEN, shapely buffer). Ze liggen in de eerste laag; die wordt platgedrukt (olifantsvoet) en een groef van één spuitmond breed loopt dan dicht. | maat: feit; dichtlopen: vermoeden | midden | Een echte print, of slicen met PrusaSlicer/Cura en de eerste laag bekijken. |
| A4 | Overhang klein (plafonds cijfers, onderkant bol), geen support nodig. | feit volgens Bram (trimesh), beeld klopt | midden | slicer |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Cijfers in de tekst hebben GEZIEN of GOK, "±15 min" eerlijk weggelaten, "Not print tested by us yet" staat erin. Goed. | feit | hoog | eerlijk |
| B2 | Aanbod "Send a photo, get Pro free" volgt het besluit van 22 nov 12:40. | feit | hoog | besluiten |
| B3 | Geen persoonsgegevens. | feit | hoog | |

## Deel C: zou een maker het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | **"Send a photo" zegt niet waarheen.** Wie print en blij is, loopt hier vast; dan krijgen we ook geen foto, en die foto is het hele doel van het besluit. | Eén plek noemen (mailadres van Dortus, Discord of formulier op dortus.com) en wat je terugkrijgt (een code). | klein |
| C2 | "Print them flat" leest vreemd: de delen zijn 29 tot 44 mm hoog. | "Print them as they are in the file, flat end down. No supports." | klein |
| C3 | Na het lospakken is het enige houvast het cijfer onderop (zie A3). | Naast grotere cijfers ook 1 tot 5 korte groeven op de zijkant van beide delen: verticale wanden printen scherp, en tellen lukt altijd. | klein |
| C4 | Het beeld schuin is grijs op grijs; voor dortus.com mag er één beeld bij van twee delen die in elkaar zitten, schuin gebogen. Dat verkoopt de klik. | Render van één paar in elkaar, 30 graden gebogen. | klein |
| C5 | Bestandsgrootte 3,3 en 4,0 MB is prima voor een download. | | |

## Moet (blokkeert akkoord)
1. **A3:** cijfers groter en dikker: letterhoogte minstens 4 mm en lijnen minstens 0,8 mm (vet lettertype of een kleinere tekst "10", "15", "20", "25", "30" zonder "0."), schijf is 20 mm breed dus het past. Bijleggen: nieuwe meting van de smalste groef.
2. **C1:** in de tekst zeggen waar de foto heen moet en wat je krijgt. Welke plek kan, beslist de hoofdchat (geen adres van Thijs).

## Kan (mag later)
- C2 zinnetje "flat end down".
- C3 groeven op de zijkant.
- C4 beeld van een paar in elkaar.

Na de twee moet-punten keur ik alleen die opnieuw.

## Nakeuring 22 nov 2026 ±15:25 UTC, Daan (commit b3d85df)
Akkoord: **ja**. Beide moet-punten zijn opgelost.

| # | Punt | Uitslag | Hoe |
|---|---|---|---|
| 1 | Cijfers groter (A3) | Opgelost. "10" tot "30", 7,6 tot 7,7 mm hoog, 8 tot 10 mm breed op een schijf van 20 mm. Smalste groef 0,82 mm, geen onder 0,8 mm (GEZIEN, `meet_strip.py` zelf gedraaid op beide STL's). Strenger nagemeten: openen met 0,4 mm haalt hooguit 0,8% van een groef weg, met 0,8 mm hooguit 2,9% (alleen hoeken), dus geen lijn smaller dan een spuitmond (GEZIEN, shapely). De 6 binnenvormen van de "0" hangen vast aan het deel boven de 0,6 mm groef. A recht, B 180 graden gedraaid, niet gespiegeld (GEZIEN, beeld eerste laag). Beide STL's waterdicht, op z = 0. | trimesh, doorsnede 0,3 mm |
| 2 | Waar de foto heen moet (C1) | Opgelost: "Email a photo to thijs@dortus.com (subject: Fit test photo) and get a free Pro code." Dat is het zakelijke adres van Dortus volgens het besluit van de hoofdchat 13:40; geen persoonsgegeven. | tekst gelezen |

Kan (nieuw, klein):
- K1: bovenaan de tekst staat nog "140 x 52,1 x 44,5 mm"; nu is het 140 x 52,4 (GEZIEN). Gelijk trekken.
- K2: de "1" in Bfont is een kaal streepje; "10" kan als "IO" lezen. In de reeks 10 tot 30 is het duidelijk genoeg, dus geen moet.
- C3 en C4 van de eerste keuring staan nog open (mag later).

Mag op de tak in repo dortus en daarna op dortus.com, volgens het besluit van 12:40.
