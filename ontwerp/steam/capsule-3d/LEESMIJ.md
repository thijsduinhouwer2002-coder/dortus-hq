# Capsule in 3D (Mila, 14 nov 2026)

Eerste 3D-versie van de winkelafbeelding van Hats of the Fallen, voor het toetsmoment van Thijs (ma 16 nov) en de capsules van wo 25 nov (`platformen/steam/planning-fest-2027.md`).

## Het idee
De haak in één beeld, zonder uitleg: **Gloop zit grijnzend op zijn goud met een toren van gestolen hoeden** (helm, kroon, heksenhoed, rode muts). Links komt een ridder binnen en schrikt: onderaan de toren draagt Gloop precies dezelfde zilveren helm als hij. Je snapt wat er met de vorige ridder gebeurd is, en dat hij de volgende is. Dat is de naam: Hats of the Fallen.

Eerlijk: alles in beeld zit in het spel. Gloop en de ridder komen ongewijzigd uit Daans `gloop.py` (versie 2, 4 hoeden, stand rust) en `held.py` (ridder, stand schrik); de hoedentoren, de schat, de fakkels en de stenen boog van de schatkamer bestaan in het spel.

## Bestanden
- `capsule3d.py`: het model. Draai met Blender als Python-pakket (`bpy==5.2.4`):
  - header: `capsule3d.py header-920x430.png 920 430 64` (±1,5 min op 2 kernen)
  - klein: `capsule3d.py klein-462x174.png 462 174 96 klein`
- `LilitaOne-Regular.ttf`: letter van de titel (SIL Open Font License, Google Fonts; mag mee in een product en in winkelbeelden).
- `header-920x430.png`, `klein-462x174.png`: de renders.
- `klein-oud-nieuw.png`: de oude pixelcapsule klein naast de nieuwe.
- `vergelijk-header3d-toppers.png`: onze header naast Rusty's, Bongo Cat, Spirit City, Tiny Pasture en Deskrawl op dezelfde hoogte.

## Keuzes
- **Besluit: de capsule mag een lichte perspectief hebben (lens 42), anders dan de strook (orthografisch).** Waarom: een capsule is een poster; met diepte staan Gloop en de ridder in een kamer in plaats van op een plank. Kleuren en licht blijven die van `3d-stijl.md` (pruim, muntgroen, goud, warm fakkellicht).
- **Besluit: titel als 3D-letters in goud met een donkere pruimen rand, geen pixelletter meer.** Waarom: de pixelletter vloekte naast de 3D-figuren; Lilita One is rond en dik zoals Gloop, en leest op 174 px nog.
- Gloop zit op de berg (niet erin): eerst zakte hij in het goud en was zijn vorm weg.
- Gloop is groter dan de ridder: hij is de ster en de grap zit in zijn toren.

## Eigen toets (GEZIEN met Read)
- Naast de toppers op 231 px hoog: veel rijker dan de pixelheader van v5; titel leest, de toren leest als hoeden. Zwakker dan de toppers: hun figuren vullen het vak, bij ons is er nog veel muur. Rusty's en Tiny Pasture zijn feller en lichter.

## Volgende ronde
1. Frisse kijker alleen op `header-920x430.png` en op ware grootte; letterlijk opschrijven wat hij ziet en of de helm-grap leest.
2. Meer vullen: de boog en de muur kleiner in beeld, Gloop nog dichterbij.
3. Hoofdbeeld 1232x706 en bibliotheek 600x900 (staand: toren past daar juist goed).
4. Idee uit de oude pixelcapsule terughalen: kleine hoeden op de letters van HATS (klein-oud-nieuw.png links). Dat maakt de titel zelf de grap.
5. Daan keurt op fouten en leesbaarheid.
