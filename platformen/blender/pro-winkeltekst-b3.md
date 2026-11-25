# Click Joints Pro: nieuwe titel en eerste alinea (B3), Gumroad en Superhive (Bram, 24 nov 2026)

**Waarom (geld):** de titel op Superhive is kaal ("Click Joints Pro"), terwijl Cleave, Split 3D Print en JointLab zoekwoorden in de titel hebben (lat gat 4). In de blinde test haalt B3 bij Gemini én ChatGPT plek 1,0 tegen Cleave, CatPin en Split 3D Print (GEZIEN, `organisatie/blindtest/uitslag/click-joints-pro-tekst-2026-11-24-2218.md`). De huidige tekst haalde Gemini 2,0 en ChatGPT 1,0 (GEZIEN, `click-joints-pro-tekst-2026-11-24-2212.md`). Effect op verkoop: GOK; vooral beter gevonden worden op "3D print" en "joints".

**Waarom B3 en niet B2 (ook 1,0):** de grootste klacht in ronde 1 was "je moet al een rig hebben" (Gemini zette ons daarom op plek 3). B3 zegt in één zin dat het ook zonder rig kan, en noemt de speling, waar beide rechters om vroegen.

## 1. Titel
Superhive (productnaam):
```
Click Joints Pro - Poseable 3D Print Figures from Your Rig (Hinges with End Stops, Ball Joints, Fit Test Strip)
```
Gumroad (productnaam, korter mag daar ook): dezelfde titel.

## 2. Kop bovenaan de beschrijving (vervangt "Rig to printable figure: elbows and knees stop where your rig stops.")
```
Rig in. Joints out.
```

## 3. Eerste alinea (vervangt de huidige eerste alinea "Pick your rigged figure, press one button, ...")
```
Press one button and your rigged character becomes a printable, poseable figure: a hinge at every elbow and knee that stops where your rig stops, and a ball joint at the shoulders, hips and neck, with the clearance you set in millimetres. You see how far each joint bends, in degrees, before you print, and the Fit test strip tells you which gap fits your printer. No rig? Put the 3D cursor on a knee and Click Joints Pro adds the joint right there.
```
De rest van de pagina blijft zoals in `pro-1.2.8.md` (blok "New in Pro 1.2.8" en verder).

## 3b. Regel "Try it free first" (direct onder de eerste alinea, Gumroad en Superhive; Bram 25 nov, issue #50, lat gat 2)
```
Try it free first: the free Click Joints on Blender Extensions makes ball and pin joints, one at a time, and shows how far each one bends. Hinges with end stops, Figure from rig and the Fit test strip are in Pro only. https://extensions.blender.org/add-ons/click-joints/
```
Waarom (geld): JointLab zet "USE ONLINE, FREE" naast de koopknop en Split 3D Print heeft een $0-variant (lat gat 2, GEZIEN). Wie twijfelt over $19 kan eerst zien dat het werkt; de gratis versie heeft 375 downloads (GEZIEN, `producten/blender-gewrichten/taken.md`), dus het lijntje terug naar Pro loopt ook die kant op. Effect op verkoop: GOK.

Feiten (nagekeken 25 nov ±08:15 NL met curl):
- Link geeft 200 en toont Click Joints 0.1.1, "Add-on by Thijs-Dortus" (GEZIEN).
- Gratis: kogel of pen en gat op de 3D-cursor, één gewricht per klik ("Set the 3D cursor where the joint goes, click Place joint"), buigbereik in graden, passingkleur, export STL of 3MF (GEZIEN op de pagina).
- Alleen Pro: scharnier met eindstop (`click_joints/betaald/scharnier.py`), Figure from rig (`click_joints/betaald/rig.py`), Fit test strip (`click_joints/betaald/testkaart.py`); ontwerp.md regel 30 en 40 (GEZIEN in de code).
- Geen belofte dat gratis hetzelfde is: de tweede zin noemt wat ontbreekt.
- Regels van extensions.blender.org gaan over de gratis add-on zelf (geen verwijzing naar Pro daarin); een link van Pro naar gratis mag.

Let op voor Superhive: de variant Lite ($3) is dezelfde code als de gratis versie. Met deze regel ziet een koper dat Lite gratis te krijgen is; dat is eerlijk en zo bedoeld. Lite schrappen beslis ik na de sale (geen wijziging nu, vlak voor 27 nov).

## Feiten achter elke bewering
- Hinge met eindstop bij ellebogen en knieën, kogel bij schouders, heupen, nek: Figure from rig (live tekst, Daan ja sinds 1.1).
- "stops where your rig stops": live kop sinds 22 nov; de pagina zegt verderop "where it sets one".
- Speling in millimetres: instelling Clearance in het paneel.
- Graden vóór de print: bereik naast elk gewricht (live tekst).
- Fit test strip: sinds 1.2.0, vijf gewrichten van 0,10 tot 0,30 mm.
- Zonder rig: Knee, Elbow en de hinge-knoppen op de 3D-cursor (live blok "Split with anything. Make it move.").

## Stand
- 24 nov ±23:00 NL: GESLAAGD (plek 1,0 bij beide). Keuring Daan gevraagd in issue #11. Daarna klaar om te plakken, samen met 1.2.8.
- 25 nov ±08:20 NL: regel 3b "Try it free first" toegevoegd (#50), keuring Daan gevraagd.
