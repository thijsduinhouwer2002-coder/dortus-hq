# Opbouw: Gloop's Hat Tower op Reddit

Devvit Web-app op de officiële template `reddit/devvit-template-bare`. Alles staat in `app/`.

| Deel | Bestand | Wat het doet |
|---|---|---|
| Spelregels | `src/shared/spel.ts` | Het potje in vaste stappen van 4 ms, dagcode, dagregels, gouden helden, waarde van een vangst. Draait in browser en server. |
| Uitslagkaart | `src/shared/kaart.ts` | Tekst met vakjes; `reactie` zet witregels voor Reddit. |
| Afspraken | `src/shared/api.ts` | Routes en typen tussen browser en server (`api/init`, `api/start`, `api/score`, `api/share`, `api/join`). |
| Server op Reddit | `src/server/server.ts` | Leest wie het is (context), roept `logica.ts` aan met Redis. Dagpost via de scheduler. |
| Logica | `src/server/logica.ts` | Dag per post (`post:<id>`), start (één sleutel per speler per toren, alleen als nieuw, met starttijd; insturen tot 60 s na het eind), naspelen van de tikken, claim van de uitslag vóór het tellen, ranglijst, gezamenlijke toren, dagen op rij. |
| Opslag | `src/server/redis-opslag.ts`, `geheugen-opslag.ts` | Zelfde koppelvlak: Redis op Reddit, een Map lokaal en in de toetsen. |
| Spel in de post | `src/client/game.ts` | Startscherm, spelen, invoer, einde. |
| Beeld en beweging | `src/client/basis.ts`, `scene.ts`, `held.ts`, `grot.ts`, `effecten.ts` | Maten en geheugen van het beeld; Gloop met squash en stretch, toren met veer, vliegende hoeden, HUD; de held (boog, tuimelen, slok, landen, weglopen); grot en gezamenlijke toren (beide eenmalig in een los doek getekend); veren, deeltjes, schermschok. |
| Eindmoment | `src/client/slot.ts` | Camera (nooit verder dan 0,5 uitgezoomd, anders van de top naar Gloop), je hoeden naar de gezamenlijke toren, mijlpaal. |
| Uitslagvel | `src/client/uitslag.ts`, `public/uitslag.css` | Score, vakjes met uitleg, reactie met voorbeeld, lid worden, ranglijsten van vandaag en gisteren. |
| Post in de feed | `src/client/splash.ts`, `public/splash.html` | Gloop met toren, de dag, de knop die het spel groot opent. |
| Plaatjes | `public/kunst/` | Renders uit de 3D-modellen van Hats (`../kunst/render.sh`, `../kunst/knip.py`); maten en ankers in `kunst.json`. |
| Lokaal | `dev/local.ts`, `dev/schermen.py`, `dev/film.py` | Server zonder Reddit (`?dag=N` speelt als een oude post); Playwright-speler voor schermbeelden; het inzendfilmpje op 1080x1920 met geluid. |

Toetsen: `src/shared/spel.test.ts` en `src/server/logica.test.ts` (`npm test`: types, lint, toetsen, bouw).
