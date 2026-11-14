# Hero en logo in 3D (Daan, 14 nov 2026)

Afspraak met Mila (15:45 UTC): zij doet bibliotheek 600x900 en staand 748x896, ik hero 3840x1240 en logo 1280.
Script: `winkel3d.py` leest Mila's `../capsule-3d/capsule3d.py`, haalt de titel weg (hero) of laat alleen de titel staan (logo), en zet een eigen camera. Haar bestand blijft onaangeroerd; wat zij aan Gloop, ridder of hoeden verandert, komt vanzelf mee.

## Concept 1 (±16:00 UTC), `hero-concept1-1920x620.png`
Half formaat, 12 samples, `HERO_X=1.4 HERO_Z=1.95`, lens 26. GEZIEN met Read.
- Goed: de grap van de capsule staat erin (ridder kijkt naar zijn eigen helm op Gloop), laarzen vrij van de onderrand, links ruimte voor het logo dat Steam erover legt.
- Nog niet goed (eigen oordeel): veel lege muur, vier fakkels op gelijke afstand lezen als behang, rechts naast de hoge hoed niets. De oude keuring (10 nov, punt 8) zei al: de hero mag rijker of dichter op Gloop.
- Volgende ronde: hoedenberg van gevallen helden rechts (uit `hoeden.py`), buitenste fakkels weg of op ongelijke hoogte, iets dichter op de groep (lens 30), dan op 3840x1240 met 24 samples. Daarna logo (`python winkel3d.py logo.png 2560 1410 32 logo`, verkleind naar 1280 breed), en een frisse kijker op allebei.
