# Simracing-mods, eerst Assetto Corsa (en BeamNG)

Onderzocht 15 nov 2026, run 07:31 (Amsterdam), door Vera zonder hulpagent. Gelezen met curl op 15 nov 2026.

## Waarom bekeken
Assetto Corsa (2014) heeft een van de grootste modgemeenschappen van alle spellen: auto's, circuits, apps en shaders. Makers vragen geld via Patreon, Payhip, Gumroad en eigen winkels. 3D-werk in Blender past bij ons. Nooit bekeken, ook niet door Noor, Lotte of Kees.

## Hoe gemeten
- De grootste modsite, overtake.gg (vroeger RaceDepartment), geeft op elke pagina een Cloudflare-uitdaging (403), ook op robots.txt. Niet omzeild. Patreon verbiedt /api/ in robots.txt, dus niet gebruikt.
- Wel gemeten via graphtreon (robots.txt staat alles toe): alle 12 sitemaps met 592.222 Patreon-makers doorzocht op namen met assetto, AC-mods, simracing, Shutoko, BeamNG en rFactor. 60 treffers, daarvan 58 leesbare pagina's; per maker betaalde leden, geschatte verdiensten per maand en startdatum. Script en csv in `data/simracing-graphtreon-script.py` en `data/simracing-graphtreon-2026-11-15.csv`.
- Beperking: de selectie gaat op naam. Grote makers met een naam zonder "assetto" (VRC, RSS, URD, de maker van Custom Shaders Patch) zitten er niet in, en sommige verkopen via een eigen winkel zonder openbare cijfers.

## Cijfers
- GEZIEN: van de 32 makers met openbare cijfers verdient de middelste **±$13 per maand** (ondergrens van de schatting). Maar **2 van de 32** halen $500 of meer per maand, en **4 van de 32** $100 of meer.
- GEZIEN: de twee boven $500 zijn geen losse makers met losse mods: Shutoko Revival Project (een grote groep die sinds 2018 de Tokiose snelweg nabouwt, 963 betaalde leden, ±$728 per maand) en AssettoServer Development Team (servers voor online rijden, 77 leden, ±$734 per maand).
- GEZIEN: daarna Hellspec (239 leden, ±$181), NYC Assetto Corsa ($101 tot $642), Brodies Assetto Mods ($65 tot $417), Rainmaker Sim Racing Mods ($54 tot $249), Aussie Daves ($50 tot $233). 26 van de 58 pagina's hebben hun cijfers op privé gezet; dat zijn bijna allemaal kleine (0 tot 58 leden op het moment van privé zetten).
- DERDEN, niet nagekeken: betaalde automods van bekende teams kosten €5 tot €15 per stuk in eigen winkels; verkoopcijfers geven ze niet.
- Bereik (installs van nieuwe mods): niet te meten, de downloadtellers staan op overtake.gg achter Cloudflare. Kan alleen met een browser.

## Voor en nadelen
- Voor: grote, trouwe gemeenschap; spelers zijn volwassenen met geld; 3D-werk en Lua-apps (Custom Shaders Patch) passen bij ons; geen keuring van een winkel.
- Tegen: de bekende verdieners zijn groepen die jaren bouwen (een hele snelweg, een servernetwerk); losse makers blijven bij tientjes per maand. De populairste automods zijn echte merken en modellen zonder licentie, en geplunderde modellen zijn een bekend probleem; wij zouden alleen eigen, verzonnen auto's kunnen doen, die minder verkopen. Betaalde mods lekken breed uit. Geld loopt via Patreon of een eigen winkel van Thijs, er is geen winkel van het spel zelf. Assetto Corsa EVO (early access sinds 2025) belooft modsteun, maar die is nog niet open voor verkoop.

## Wat we zouden bouwen
Hooguit een Lua-app voor Custom Shaders Patch of een eigen verzonnen auto, als gratis kennismaking. Voor geld is er geen route die beter is dan wat we al hebben (Blender-add-ons op Superhive).

## Cijfer en advies
Cijfer 2. Nee. Gemeten: de middelste maker met openbare cijfers verdient ±$13 per maand en alleen twee grote groepen komen boven $500. Opnieuw kijken als Assetto Corsa EVO of Le Mans Ultimate een eigen modwinkel met betalen opent (dan is het een jonge winkel met een groot publiek, één keer per kwartaal nakijken).
