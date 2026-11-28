# Voorleestekst Short Click Joints Pro "STL zonder rig", voor ElevenLabs "Max - Witty Commercial Actor"

Regisseur, za 28 nov 2026 ±19:40 NL. Opdracht hoofdmanager in #332 (18:45), antwoord op punt 2 van de Afkijker (#416, `organisatie/lat/click-joints-pro.md`: wie een STL zonder rig heeft leest "Rig in." en haakt af).

Hoofdchat: lees deze 8 zinnen in deze volgorde voor, één opname, gewone pauze tussen de zinnen (±0,3 s), en zet hem als `commercie/filmpjes/regisseur-34/pro-stl-elevenlabs.mp3`. Vlot en vriendelijk, uitleggend zoals iemand die het op zijn eigen pc laat zien, geen reclamestem. Geschatte lengte 24 tot 28 s (GOK, 70 woorden bij ±160 woorden per minuut).

## Zinnen (Engels, letterlijk zo voorlezen)
1. Got an STL with no rig?
2. You can still make it poseable in Blender.
3. Shift and right click on the shoulder, and the 3D cursor jumps there.
4. Now click Shoulder: Click Joints Pro cuts a ball joint right there, with the clearance you set.
5. The list shows how far it bends, in degrees, before you print.
6. Knee or elbow? Same two clicks, and you get a hinge with an end stop.
7. Print the Fit test strip first: every printer is different.
8. Click Joints Pro, an add-on for Blender.

## Waarom elke zin waar is (Pro 1.2.8 live, 1.2.9 gelijk voor deze knoppen)
- 1, 2: zonder rig werkt het paneel "Figure joints" met de tekst "Put the 3D cursor on a joint, then:" (`producten/blender-gewrichten/click_joints/betaald/figuur.py` r. 242 tot 243); winkeltekst B3 "No rig? Put the 3D cursor on a knee..." (Daan ja, #11).
- 3: hoofdpaneel stap 1 zegt "Shift + right click sets the 3D cursor" (`paneel.py` r. 87); fix in 1.2.7 (`platformen/blender/pro-1.2.7.md`).
- 4: preset Shoulder = kogel, het snijden doet de bestaande kogeloperator; Clearance in mm in stap 2 (`figuur.py` r. 1 tot 30, `paneel.py` r. 102).
- 5: elke regel in de lijst toont het gemeten bereik, bijvoorbeeld "Knee · Hinge · 0–135° · preset" (`figuur.py` r. 73 tot 78); bij een kogel "±N°".
- 6: preset Knee en Elbow = scharnier met eindstop op 135° (`figuur.py` PRESETS). Twee kliks = Shift + rechtsklik en de knop.
- 7: vaste zin uit CLAUDE.md regel 5 en de filmpjesregels; Fit test strip zit in Pro (`betaald/testkaart.py`).
- 8: productnaam, geen sale in beeld (Thijs 27 nov 11:05: "geen reclame"); sale en link alleen in de beschrijving.

Niet gezegd: geen "one click" voor het hele figuur (dat is Figure from rig, alleen mét rig), geen printclaim, geen "it clicks", nergens AI.

## Beeld (plan, voor de opname met xdotool)
Echte Blender-interface, N-paneel Click Joints. Gekleurde figuur zonder armature (geïmporteerde STL, geen grijze mannequin). Zin 3: echte Shift + rechtsklik op de schouder. Zin 4: klik op Shoulder, kogel en kom verschijnen. Zin 5: muis wijst de regel in de lijst aan. Zin 6: Shift + rechtsklik op de knie, klik Knee, knie buigt tot de stop. Zin 8: draaiende eindstand. Hook als tekst in beeld vanaf beeld 1: "Got an STL with no rig?". Eerste beeld eerst door de blinde test.
