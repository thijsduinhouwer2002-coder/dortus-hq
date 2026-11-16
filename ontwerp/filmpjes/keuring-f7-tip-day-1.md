# Keuring filmpje 7: "Printable joints in Blender, day 1" (clearance)

Daan, 16 nov 2026 ±05:40 UTC. Gekeurd: `click-joints-7-tip-day-1-clearance.mp4` uit release `filmpjes-week-1` (12,5 s, 1080 x 1920), bron `commercie/filmpjes/week-1/f7.json`. Bekeken: blad met 2 beelden per seconde en losse beelden op halve grootte, alles GEZIEN met Read.

## Oordeel: ja met één moet (M1)

Akkoord van mij voor de versie die uit `ontwerp/filmpjes/voorstel-daan/f7.json` gebouwd wordt (mijn M1 plus Brams nieuwe tekst, zie onder). Daarnaast blijft nodig: Brams "klopt" op de tip en het ja van Thijs (zie `commercie/filmpjes/reeks.md`).

Wat goed is: de vraag staat er in de eerste tel en leest in één keer; ander begin dan de ring en de pop (mijn kan-punt van week 1 is gedaan); geen rood; alle tekst onder de bovenbalk (y 240 en lager); drie korte zinnen, één gedachte per beeld; groen alleen op het woord dat telt (snap in, clearance, 0.2 mm). De tip is nuttig zonder dat je de add-on hebt, precies wat een tip moet zijn.

- **M1: het paneel netjes uitsnijden.** Op 3,3 tot 7,8 s staat bovenaan de rij "Diameter (mm) 3.5 Auto" half afgesneden: je ziet alleen de onderste helft van de letters. Dat oogt slordig en het is precies het beeld waar je naar moet kijken. In `voorstel-daan/f7.json` begint de uitsnede bij de rij "Clearance (mm) 0.20" en eindigt hij net onder het groene kader: `"crop": [1131, 405, 374, 312]`, `"zoom": 0.015` (was `[1120, 385, 396, 330]` en 0.03). Gevolg: geen halve tekst meer, de letters zijn ±6% groter, het kader staat meer in het midden, en zowel "Clearance (mm) 0.20" als "Clearance: 0.20 mm (measured)" staan de hele tijd in beeld. Alleen dit segment verandert, `maak.py` blijft gelijk. Zelf gebouwd met jouw `maak.py` en dezelfde bronnen (sha256 van s5, 4-preview-paneel en v2 klopt): blad `voorstel-daan/click-joints-7-tip-day-1-blad.jpg`, voor en na op 5 s `voorstel-daan/click-joints-7-paneel-voor-na.jpg`.

## De nieuwe tekst van Bram (moet van hem, 16 nov 05:16): ook al in mijn json
Bram mat in de echte Blender dat de speling per kant is en het inklikken niet makkelijker maakt (`platformen/blender/tips-nagekeken.md`). Zijn tekst zit al in `voorstel-daan/f7.json`, zodat er maar één keer gebouwd hoeft te worden:
- haak: `Ball joint clicks in` / `but won't *turn*?` (past op twee regels, zelfde maat 68)
- midden: blijft `No gap, no movement. Leave clearance between ball and socket.`
- eind: `Try *0.2 mm per side* on FDM.` / `Then test on your printer.` Brams letterlijke zin "Start around 0.2 mm per side on FDM." werd op maat 64 drie regels en raakte de bovenrand van het beeld; "Try" zegt hetzelfde (een begin, daarna testen) en blijft op twee regels. Bram, zeg het als "Try" voor jou niet klopt; dan maak ik er `*0.2 mm per side* to start.` / `Then test on your printer.` van.
Gezien: `voorstel-daan/click-joints-7-tekst-bram.jpg` (haak op 1 s, eind op 10,5 s) en het blad. Het beeld past nu beter dan eerst: het eindstuk laat de arm draaien, precies wat de haak vraagt.

## Controleur (Agent, blind, A oud tegen B nieuw)
A 6, B 7 voor het middenstuk ("B begint netjes bij Clearance 0.20, grotere letters, je kijkt meteen naar 0.20"). Hij noemde ook de regel "Tool: Click Joints, a free Blender add-on" op y 1585 als moet, omdat die in de strook van de app valt. Dat neem ik niet als moet: zelfde regel en plek als in week 1 (daar ook zo besloten), het onderschrift noemt de add-on met de link, en hoger zetten botst met het beeld (paneel tot y 1540, film tot y 1553). Wel als kan voor de volgende tips, zie hieronder.

## Kan (niet nodig om te plaatsen)
- **Volgende tips (f8 en verder): de toolregel boven de strook van de app.** Bij tips is die regel de enige plek waar de add-on in beeld staat. Zet hem op y ±1450 en laat het beeld daarboven eindigen (bijvoorbeeld paneel `h` 800 op y 620, film `h` 860 op y 580). Dan blijft hij ook op TikTok zichtbaar.
- **Begin: laat het probleem zien.** Nu draaien kogel en kom 3,3 s rustig uit elkaar; dat de kogel niet in de kom past, zie je niet. Sterker zou zijn: kogel schuift naar de kom en stuit erop (een klein schokje), dan pas de vraag. Vraagt een nieuwe opname van Bram, dus voor een latere tip, niet voor deze.
- **Einde:** in de laatste seconde zakt de pop half uit beeld rechts. Een harde knip op 12,0 s of de film 0,5 s eerder laten beginnen (start 9,5) houdt de pop heel in beeld. Klein punt.
- Onder het groene kader piept een dun blauw randje van de knop "Show bend range". Mag blijven, het is het echte paneel.

## Onderschrift
Goed, maar dezelfde kant op als Brams moet: "too tight to snap in" wordt "clicks in but won't turn", en "0.2 mm" wordt "0.2 mm per side". Dat is aan Chris (zijn tekst). `AI agents write the code, I direct and test.` als vaste zin in alle nieuwe onderschriften: ja, eens.
