# Click Joints Pro: tags, categorie en titel voor Superhive en Gumroad (Bram, 26 nov 2026, issue #161)

Plakken door de hoofdchat (inloggen), na het ja van Daan, **vóór vr 27 nov 12:00** zodat het in de sale meetelt. Bewijs: kop "Gevonden worden" in `organisatie/lat/click-joints-pro.md` (alles GEZIEN met curl op 26 nov ±10:10 NL).

Vervangt deel 2 en 3 van `platformen/blender/superhive/zoekwoorden.md` (21 nov, nooit geplakt: op Superhive staan nog de oude 12 tags, GEZIEN). Het Keywords-blok uit deel 1 van dat bestand doet hier niet aan mee.

**Effect op verkoop: GOK.** Superhive: wie op "articulated" zoekt ziet ons nu op plek 32 (pagina 2), wie op "action figure blender" zoekt vindt ons niet. Gumroad: geen effect tijdens de sale, want we staan niet op Discover tot we $100 omzet hebben plus ±3 weken controle (DERDEN, https://gumroad.com/help/article/79-gumroad-discover). We zetten het wel goed, zodat het meteen werkt zodra we erop komen.

## 1. Superhive: tags (12, vervangen alle 12 van nu)
Elke concurrent heeft er precies 12; meer kan waarschijnlijk niet (GOK). In deze volgorde:

```
articulated-figure, articulated, articulation, action-figure, poseable, posable, ball-joint, hinge, 3d-print-joints, blender-addon, 3d-printing, rig-to-print
```

| Tag | Waarom |
|---|---|
| articulated, articulation | "articulated" plek 32; JointLab (plek 1) en NB Figure Joints hebben deze woorden |
| 3d-print-joints | "3d print joints" plek 11; Cut Flex (plek 5) heeft precies deze tag |
| blender-addon | "action figure blender": niet gevonden; NB Figure Joints (plek 1) heeft deze tag |
| articulated-figure, action-figure, poseable, posable, ball-joint, hinge, 3d-printing, rig-to-print | blijven: posable plek 1, hinge joint plek 2, ball joint plek 3, poseable figure plek 4 |

Eruit: **miniatures** (onze eigen tekst zegt dat de armen onder 150 mm te dun zijn), **stl**, **3mf** en **joints** (te algemeen; STL en 3MF staan in de tekst, joints zit in 3d-print-joints). Bewust niet: **print-in-place** (onze delen zijn los en gaan in elkaar; keuring Daan 19 nov).

## 2. Superhive: categorie
Nu alleen Add-ons > **Modeling** (GEZIEN). Erbij:
- **Rigging**: geen enkele concurrent staat daar (GEZIEN, Browse Rigging alle 28 pagina's, geen Cleave, CatPin, Split, NB Figure Joints, JointLab of Cut Flex), en alleen wij lezen de rig.
- **Import & Export**: Cleave en Split 3D Print staan daar ook (GEZIEN); wij exporteren STL en 3MF per deel.

Laat het formulier maar één categorie toe: Modeling houden (daar zoekt de koper van de top 3).

## 3. Superhive en Gumroad: één woord in de titel
NB Figure Joints en JointLab staan bovenaan op "articulated" en "action figure" met die woorden in de titel; bij ons staat het alleen in een tag en dat helpt weinig (plek 32 en 15).

Nu (beide winkels):
`Click Joints Pro - Poseable 3D Print Figures from Your Rig (Hinges with End Stops, Ball Joints, Fit Test Strip)`

Wordt:
```
Click Joints Pro - Articulated, Poseable 3D Print Action Figures from Your Rig (Hinges with End Stops, Ball Joints, Fit Test Strip)
```
Te lang voor het veld? Dan zonder "Strip". Alles in de titel doet het product echt (Figure from rig, scharnier met eindstop, kogels, Fit test strip).

## 4. Gumroad: categorie en tags (tabblad Share, deel "Gumroad Discover")
- **Categorie:** 3D > 3D Assets > Blender (zelfde als Cleave, CatPin en SlicerJoint Pro, GEZIEN). Zonder categorie komt een product nooit op Discover (DERDEN, link hierboven).
- **Ratings aan** laten (ook een eis voor Discover).
- **Tags** (Cleave heeft er 9 zichtbaar; laat het veld minder toe, dan van voren af):
```
articulated figure, poseable figure, action figure, ball joint, hinge joint, 3d print joints, 3d printing, blender addon, rig to 3d print
```
- Zelfde categorie en tags voor de gratis Click Joints op Gumroad, met "free" erbij in plaats van "rig to 3d print".

## Na het plakken (Bram)
Ik draai `producten/blender-gewrichten/vindbaar/zoek_superhive.py` opnieuw en zet de nieuwe plekken in de lat, kop Gevonden worden.
