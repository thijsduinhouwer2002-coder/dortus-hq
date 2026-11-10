# Click Joints Pro: Superhive-pagina (concept, Bram 10 nov 2026)

Status: concept. Nog nodig voor indienen: winkelplaatjes met het ja van Daan (`Akkoord: ja` bovenaan `producten/blender-gewrichten/ontwerp.md` voor de Pro-zip), de betaalde zip uit `maak_zip.sh betaald` na een groene test, en het verkopersaccount van Thijs (staat op zijn lijst). Prijs is een voorstel; Chris mag hem bijstellen.

## Instellingen
- **Naam:** Click Joints Pro
- **Categorie:** Add-ons, Modeling / 3D Printing
- **Prijs (voorstel):** $12 gewone licentie, lanceerprijs $9 de eerste twee weken (GOK, ontwerp.md). Netto per verkoop van $12: 70% min $0,49 = ±$7,91.
- **Studiolicentie:** tot 5 personen, $45 (GOK; CatPin $80, Split-3DPrint $59, wij zijn kleiner en nieuwer).
- **Support Period (advies 7):** 12 maanden updates bij de koop, verlengen met 12 maanden voor 25% van de prijs. Na afloop blijft de gekochte versie gewoon werken.
- **Licentie:** GPL-3.0-or-later (code), zoals elke Blender-add-on.
- **Blender:** 4.2 LTS tot 5.2 (getest in 4.2.23 en 5.2.3 op GitHub Actions; 5.3 erbij zodra die uit is).

## Tekst (Engels, voor de pagina)

**Hinges that click and stop at 115°.**

Click Joints Pro adds a printable click hinge to your figures: a knee or elbow that bends from 0° to 115° and stops there, instead of flopping backwards. Place it on a limb, drag the pose slider, and you see the exact range in degrees before you print. Bend past the stop and the parts that collide turn red.

What you get:
- **Click hinge with an end stop**, for knees and elbows: measured range 0° to 115° on the hinge, shown as a degree arc around the axis.
- **Pose slider per hinge**: check the bend in the viewport. Exporting is not affected by the pose.
- **Red past the limit**: the spot that hits turns red, so you know before you print.
- **Spacing checks**: hinges and ball joints too close together are refused with a clear message.
- **Everything from the free Click Joints**: ball joints with a fit colour, ±degrees, split into parts, export to STL or 3MF.

Good to know:
- Clearance 0.2 mm by default; print a test first, every printer is different.
- The free Click Joints (extensions.blender.org) and Pro can not be enabled at the same time. Disable the free one first; your settings stay in the .blend file.
- Pure Python, no extra add-ons needed.
- Support: https://github.com/thijsduinhouwer2002-coder/click-joints/issues or thijs@dortus.com

## Na te kijken voor indienen
- Elke zin hierboven klopt met de code op main (controleur, zoals bij de gratis tekst). Getallen 115°, 0,2 mm en de weigermelding staan in de toetsen.
- Plaatjes alleen met wat de Pro echt doet (zie de punten van Daan; het script-groen op de proefposter mag niet zo naar de winkel).
