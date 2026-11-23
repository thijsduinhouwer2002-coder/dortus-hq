# Split Joints (werknaam): ontwerp kern v0.1

Akkoord: nee (eerst de ontwerper, zie `merk/` zodra die er is)

Bouwer: agent van de hoofdchat, ma 23 nov 2026. Verder bouwen: de vaste Productbouwer.
Besluit: Thijs 23 nov ±16:25 NL, tweede product is een splitser met verbinders, beter dan CatPin en Cleave (`organisatie/besluiten.md`, onderaan).

## 1. Begrijpen
Een Blender-add-on die een model dat te groot is voor de printer in stukken snijdt die elk op het bed passen, met zo weinig mogelijk stukken, met pennen en gaten met gemeten speling op elk snijvlak, en een nummer in elk snijvlak zodat je weet wat waar hoort. Voor wie figuren, beelden en props print (dezelfde kopers als Click Joints).

Af voor deze kern (toetsbaar, in echte Blender 4.2 en 5.3 in CI):
- elk stuk past op het gekozen bed (A1 mini in de test) en is waterdicht;
- elke pen past in zijn twee gaten met de ingestelde speling (0,2 mm, gemeten met stralen in het stuk) en is niet langer dan de twee gaten samen;
- elk stuk heeft een verdiept nummer op elk snijvlak;
- export naar STL en 3MF werkt (bestand teruggelezen: maat gelijk, millimeter);
- een snijvlak dat je verschuift, verschuift de stukken mee;
- een vlak dat te klein is voor een pen geeft een duidelijke melding.

## 2. Wat er al was (hergebruikt uit Click Joints)
- `producten/blender-gewrichten/click_joints/gewricht.py` r. 29-73: keuze Manifold of Exact en de Boolean-modifier. Overgenomen in `splitsen.py`.
- `click_joints/gesloten.py`: telling van slechte randen, volume, Maak gesloten (voxel). Overgenomen in `gesloten.py`.
- `click_joints/drie_mf.py`: eigen 3MF-schrijver. Letterlijk overgenomen (alleen de naam in de metadata).
- `click_joints/exporteer.py` en `uit_elkaar.py`: export in mm met de echte plek, opengewerkt beeld met delta_location.
- `.github/workflows/blender-gewrichten-e2e.yml`: Blender ophalen met spiegels, zip valideren, tak schermen.

## 3. Open vragen, zelf beantwoord
- **Rechte assen of schuin snijden?** Eerst langs de wereldassen: voorspelbaar, snel, en een stuk ligt plat op een snijvlak. Draaien om Z om stukken te sparen komt later (zie 6).
- **Wanneer past een stuk?** Als zijn maat in een van de zes standen (90 graden draaien) binnen het bed valt, min de marge (standaard 2 mm, GOK). Wie print, draait een stuk toch in de slicer.
- **Hoeveel stukken?** We proberen alle roosters (nx, ny, nz) waarin elke cel past, en nemen het rooster met de minste cellen waar echt iets van het model in zit (een L-vorm spaart zo de lege hoek). Bij gelijkspel: de kleinste snijvlakken samen, dan liggende sneden.
- **Speling: per kant of in totaal?** Per kant, net als Click Joints: gat = pen + 2 x speling in doorsnede. De gatwand bestaat uit platte vlakken op precies de gatstraal (de punten liggen iets verder), de pen heeft zijn punten op de penstraal. De kleinste opening is dus precies de speling.
- **Pen te groot voor een vlak?** Eerst kleiner (5, 4, 3 mm). Past ook 3 mm niet, dan geen pen en een melding met de breedte van het vlak en wat een pen nodig heeft: "Glue this joint".
- **Nummer?** "3-5" op stuk 3 waar het aan stuk 5 vastzit, en "5-3" op stuk 5. Het eerste getal is altijd het stuk zelf. 0,6 mm diep, 3 tot 8 mm hoog, waar het vlak de meeste ruimte heeft, weg van de gaten.
- **Model niet waterdicht?** Splitsen weigert met een melding en de knop Make watertight (voxel) staat ernaast.
- **Wat bij rood?** Het stuk wordt wel gemaakt, maar rood gekleurd met de reden in het paneel (te groot, niet waterdicht, wand onder 0,8 mm).

## 4. Drie aanpakken
1. **Snel: bmesh bisect plus gaten vullen.** Snel en zonder Booleans, maar het vullen van een doorsnede met gaten erin (vaas, ring) is in Blender onbetrouwbaar en geeft open stukken. Nee.
2. **Netjes: eigen mesh-snijder in numpy.** Volledige controle, maar weken werk en elk randgeval zelf oplossen. Nee.
3. **Middenweg (gekozen): Boolean per cel plus een eigen plan in numpy.** Elk stuk is model doorsnede doos (Intersect), daarna gaten en nummers eraf (Difference). Dezelfde solvers die in Click Joints al bewezen waterdicht werken (Manifold op 4.5+, Exact op 4.2). Het plannen (welke sneden, waar de pennen, waar het nummer) doen we zelf op een raster van de doorsnede, los van Blender, dus snel te testen zonder Blender (`e2e/test_logica.py`).

## 5. Wat de kern doet (v0.1)
1. **Printer**: keuze uit 9 printers (maten uit de profielen van OrcaSlicer, DERDEN: `split_joints/printers.py`) of een eigen maat, en een marge.
2. **Plan cuts**: snijvlakken als platte objecten in de collectie "Split Joints cuts". Je schuift er een met G langs zijn as (de andere assen staan op slot) of typt de plek in het paneel; erbij en weg kan ook. Het paneel toont live hoeveel cellen op het bed passen.
3. **Split**: per cel een stuk, genummerd van onder naar boven. Op elk gedeeld vlak 1 tot 4 pennen per eiland (een los deel van het vlak, zoals twee benen), verspreid zodat de stukken niet draaien, minstens gatstraal plus 1,2 mm wand van de rand (3 mm meer waar het kan), en in 3D getoetst: genoeg diepte aan beide kanten, wand rond het hele gat, niet tegen een gat van een ander vlak.
4. **Controle per stuk**: past (groen) of niet (rood), waterdicht, kleinste wand rond de gaten. Kleur als materiaal en objectkleur.
5. **Export**: per stuk een STL of 3MF in mm, plus per pendikte een plaatje met alle pennen staand (een print).

## 6. Later (volgorde naar wat kopers het eerst merken, GOK)
1. Klikverbinders (snap) en zwaluwstaart naast pennen; pen vast aan een kant (geen losse pennen).
2. Draaien van het model om Z (en een vrije snijhoek) om stukken te sparen; sneden die naar een smalle plek schuiven.
3. Live voorbeeld van stukken en pennen voor je splitst, met kleuren op de snijvlakken.
4. Stukken plat op het bed leggen bij export (beste kant naar onder) en alles in één 3MF met platen.
5. Holle stukken (wanddikte instellen) voor grote beelden: minder plastic.
6. Testkaart voor de speling (zoals de Fit test strip van Click Joints Pro).
7. Uiterlijk en namen volgens de ontwerper (`merk/`), winkelplaatjes, README.

## 7. Wat getest wordt
Zie `architectuur.md`, deel Testen.
