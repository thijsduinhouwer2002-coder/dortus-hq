# Blender Stack Exchange: antwoord op "3D-print friendly joints" (bij de lancering van Click Cuts)

Door de Verspreider, do 26 nov 2026 ±10:05 NL (run 22, A). Niets geplaatst. Keuring: Daan (#166) ja (8), K1 en K2 letterlijk verwerkt 26 nov ±12:00 NL, geen nakeuring nodig. Klaar voor de bundel van de lanceerdag van Click Cuts. Plaatsen: Thijs, met zijn eigen Stack Exchange-account (account maken en plaatsen kan alleen hij), pas als Click Cuts echt live staat en de link werkt (week van 30 nov). Dit is geen Reddit, dus het telt niet voor "één Reddit-ding per dag", maar het staat onder zijn naam: zijn ja op de tekst is nodig, daarom gaat het na Daans ja in de bundel van de dag van de lancering.

## De plek
- Vraag: https://blender.stackexchange.com/questions/209724/3d-print-friendly-joints (januari 2021). Iemand wil een figuur splitsen zodat hij in zijn printer past, de stukken met een kogel- of zwaluwstaartverbinding weer op elkaar lijmen, en loopt vast op: de rand van elk stuk selecteren, op beide stukken precies hetzelfde dichte vlak maken, en de verbinding erin zetten.
- 2.198 weergaven, 1 antwoord (score 2), vraag open, niet beschermd, niet op slot (GEZIEN, api.stackexchange.com, 26 nov ±10:10 NL). Dat is ongeveer 1 weergave per dag over bijna 6 jaar (GEZIEN, gerekend). Weinig, maar een antwoord blijft staan en Stack Exchange wordt goed gevonden in zoekmachines (GOK, niet gemeten).
- Waarom dit Click Cuts is en niet Pro: hij wil stukken die passen en vastgelijmd worden, geen beweging. Precies "Split to fit" met pennen en de passingproef.
- Regels (DERDEN, https://blender.stackexchange.com/help/promotion): eigen product noemen mag in een goed antwoord, "you must disclose your affiliation in your post", en niet elk antwoord mag over je product gaan. Daarom: het antwoord helpt ook zonder Click Cuts (handmatige route, ook voor de naad langs een mes-lijn die Click Cuts niet doet), het product staat in één alinea met "Disclosure".
- Risico (GOK): een gloednieuw account waarvan het enige antwoord een product noemt, wordt sneller als spam gemarkeerd. Kan Thijs eerst één ander gewoon antwoord geven, dan is dat beter; zonder blijft dit antwoord eerlijk en nuttig.

## Tekst om te kopiëren (Engels, Markdown zoals Stack Exchange het leest)
Link ingevuld 27 nov ±16:05 NL (run 52): Click Cuts staat live, https://duinhouwer8.gumroad.com/l/click-cuts?utm_source=stackexchange geeft 200 (GEZIEN). Plaatsen blijft: een paar dagen na het kogelgewricht-antwoord uit `bundel-2026-11-30.md`, niet dezelfde dag.

```
Two parts to this: closing both pieces with an identical cap, and adding the connector.

**Straight cut (easiest, and the caps match automatically)**

1. Duplicate the object (Shift+D, right-click to cancel the move), so you have two copies on top of each other.
2. On the first copy: Edit Mode, select all, Mesh > Bisect. Draw the cut line, then in the Adjust Last Operation panel tick **Fill** and **Clear Inner**.
3. On the second copy: the same cut with **Fill** and **Clear Outer**. Put the plane in exactly the same place (type the same Plane Point and Plane Normal values in that panel).

Both halves now have a flat cap on the same plane, so they meet without a gap.

**Cut along your knife line (to hide the seam)**

Keep the method from the other answer (knife, rip with V, separate with P). Before you separate, with the ring of edges on the cut still selected, press F (or Face > Grid Fill for a cleaner cap) to close it. Then Shift+D and right-click to duplicate that cap in place. Now separate with P > By Loose Parts: you get three objects, the two pieces and the cap copy. Join the copy to the other piece (Ctrl+J), Merge by Distance on the cut edges, and recalculate normals (Shift+N) so it faces outward. Both pieces now have exactly the same cap surface.

**The connector**

For parts that get glued, a separate printed pin is easier than a ball or dovetail: it needs no overhang and lets you line the parts up before the glue sets.

1. Add a cylinder for the pin, for example 4 mm across and 10 mm long, centered on the cut face, half in each part.
2. Duplicate it and scale the copy up by your clearance (a hole a few tenths of a millimetre wider than the pin).
3. Boolean modifier, Difference, with the larger cylinder on both parts. Print the smaller cylinder as the pin.

Print a small test block with a few clearances first: every printer and filament is different.

Set the scene to millimetres (Scene Properties > Units: Unit Scale 0.001, Length Millimeters) so your sizes match the slicer, and check both parts with the 3D Print Toolbox extension (Checks > Solid) before export.

**If you do this a lot**

Disclosure: I'm Thijs from Dortus, and we make Click Cuts, a paid Blender add-on for exactly this. You pick your printer, click Split to fit, and it cuts the model into parts that fit your bed, with pins or magnet holes and part numbers on the cut faces. Each part shows green, orange or red with the reason, and a small fit test block tells you which clearance fits your printer. Free cut adds one extra cut at any angle through a part, for example an arm at the shoulder. It cuts along flat planes, so it does not follow a knife line like in your gif; for a hidden seam, the manual route above is still the way. https://duinhouwer8.gumroad.com/l/click-cuts?utm_source=stackexchange
```

## Nagekeken
- Elke bewering over Click Cuts staat in de gekeurde winkeltekst `platformen/blender/superhive/click-cuts-winkeltekst.md` (Daan ja #110 en #131): Split to fit, printer kiezen, pins, pin holes and part numbers, magnet holes, green orange red with the reason, fit test block, Free cut at any angle through one part ("an arm at the shoulder" staat er letterlijk), sneden langs X, Y en Z ("cuts along flat planes" volgt daaruit). Geen belofte dat het past, klikt of dat wij printten. Geen AI.
- Blender-stappen: Bisect met Fill, Clear Inner en Clear Outer, Grid Fill, Merge by Distance, Boolean Difference, Unit Scale 0.001 en de 3D Print Toolbox als extensie zijn gewone Blender-functies (4.2 en nieuwer). Niet in een draaiende Blender nagelopen in deze run (GOK op de precieze menunamen; de keurder mag dat in Blender checken).
- "a few tenths of a millimetre": bewust geen getal als belofte; de testzin staat erbij.

## Ook gewogen deze run, en waarom niet
- **Blender Artists, "Help Creating a Custom Articulated 3D-Printable Figure" (t/1656400):** beste vondst, maar in run 19 al gebruikt voor de hulpreactie zonder link (`2026-11-26-blenderartists-pro.md`). Niet nog eens.
- **Reddit (r/blender, r/BlenderHelp, r/3Dprinting, laatste 2 tot 4 dagen):** geen verse vraag waar een antwoord past. De enige figuurvraag (r/3Dprinting, transformer die echt transformeert) vraagt iemand die de bestanden maakt, geen add-on. De Reddit-dagen van Thijs zijn ook vol (vr 27 r/blender, za 28 r/NomadSculpting).
- **Bambu Lab-forum (forum.bambulab.com):** regels verbieden alleen spam en verkeerde rubrieken (DERDEN, https://forum.bambulab.com/guidelines). Eigen tools staan er in "Share your prints", met een echte print (FlexySliceSTL, 430 weergaven in 3 maanden, GEZIEN). Wij hebben geen print en Thijs zou een account moeten maken. Valt af tot er foto's van testers zijn.
- **Discord:** Blender Community 224.080 leden, Bambu Lab Official 42.408, 3DMeltdown 12.877 (DERDEN, discord.com/api/v10/invites). De regels staan binnen de server, niet te lezen zonder inloggen. Valt af tot iemand met een account de regels leest.
- **Superhive-tags Pro:** staan al goed, 12 passende (ball-joint, hinge, articulated figure, action figure, poseable, posable, 3d printing, STL, 3MF, ...; GEZIEN, curl op de productpagina).
- **Stack Exchange "Ball joint on robot" (128034, 1.114 weergaven):** gaat over riggen in Blender, niet over printen. Valt af.
- Bijvangst voor de Afkijker (lat Click Joints Pro): FlexySliceSTL van TomczukCustoms, los programma dat STL's gelede prints maakt, gefinancierd op MakerWorld (DERDEN, https://forum.bambulab.com/t/259062). Geen Blender-add-on, dus geen directe concurrent.
