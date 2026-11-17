# Geluid onder de korte filmpjes (Chris, 17 nov 2026)

**Waarom.** Verhaal 31 van Joris: onze mp4's hebben geen geluidsspoor, en Metricool kan op een persoonlijk TikTok-account geen muziek onder een video zetten (DERDEN, help.metricool.com). Zonder ingreep gaan filmpje 7 (vandaag 16:00 NL), 9 en 2 helemaal stil live. Bijna geen maker plaatst stil (7 van 421 beluisterd, GEZIEN door Joris), en welk geluid het is maakt weinig uit.

**Wat het doet.** `geluid.py` maakt met code een geluid per filmpje en zet het in de mp4. Het beeld wordt 1 op 1 gekopieerd (`-c:v copy`), dus het blijft precies wat Daan keurde. Alles is zelf gemaakt uit sinustonen en ruis: geen nummer of geluid van een ander, dus niets wat TikTok kan dempen, en geen AI.
- **Click Joints 7 en 2:** een rustige warme toon (A-majeur, zacht ademend), een zachte tik bij elke nieuwe tekst of knip, een zacht zoeven als de delen naar elkaar toe zweven, en een kort plastic "tok" precies op het moment dat het gewricht groen oplicht (gemeten per beeld: f7 op 10,97 s; f2 op 0,17 en 8,37 s). Bij 2 ook een heel zachte oplopende toon terwijl de arm buigt (2,6 tot 4,3 s).
- **Ebb tip 1:** zacht zee-achtig ruisen dat aanzwelt bij "in" en wegebt bij "uit", op de schermen van f9.json (in 0 tot 2, uit 2 tot 4, in 4 tot 6, uit 6 tot 8, rustig 8 tot 11), met een korte zachte zoem (als een trillend horloge) aan het begin van elke fase, en een heel zachte lage toon eronder.

**Wat het bewust niet doet.** Geen stem, geen nummer van internet, geen nieuw beeld. De ingebrande "link in bio" in de eindkaart van 1, 3, 4, 5 en 6 lost dit niet op (staat apart). De originele bestanden zonder geluid blijven in de release staan.

**Gekozen aanpak (van drie).** (a) Losse workflow die de gekeurde mp4's uit de release haalt en er geluid bij zet: gekozen, want het beeld blijft bit voor bit gelijk en de bouw-workflow (die geluid juist verbiedt) blijft heel. (b) Geluid in `maak.py` en alles opnieuw bouwen: nee, dan verandert mogelijk het gekeurde beeld en moet alles opnieuw langs Daan. (c) mp4's in de repo zetten: nee, geen grote bestanden in de repo.

**Af als (toets.py, draait in de workflow):** beeld bit voor bit gelijk aan het origineel (md5 van de videostroom), stereo AAC, lengte geluid gelijk aan beeld (±0,05 s), luidheid tussen -19 en -14 LUFS (doel -16), echte piek onder -1 dBTP, nergens een stil gat langer dan 0,5 s. Plus een plaatje van de golfvorm met de klikmomenten (`<naam>-geluid-golf.png`).

**Uit:** release `filmpjes-week-1`, bestanden `<naam>-geluid.mp4`. De hoofdchat vervangt daarmee de bestanden in Metricool.
