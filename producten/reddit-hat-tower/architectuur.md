# Opbouw: Gloop's Hat Tower op Reddit

Devvit Web-app op de officiële template `reddit/devvit-template-bare`. Alles staat in `app/`.

| Deel | Bestand | Wat het doet |
|---|---|---|
| Spelregels | `src/shared/spel.ts` | Het potje in vaste stappen van 4 ms, dagcode, dagregels, gouden helden, waarde van een vangst. Draait in browser en server. |
| Uitslagkaart | `src/shared/kaart.ts` | Tekst met vakjes; `reactie` zet witregels voor Reddit. |
| Afspraken | `src/shared/api.ts` | Routes en typen tussen browser en server (`api/init`, `api/start`, `api/score`, `api/share`, `api/join`). |
| Server op Reddit | `src/server/server.ts` | Leest wie het is (context), roept `logica.ts` aan met Redis. Dagpost via de scheduler. |
| Logica | `src/server/logica.ts` | Start (één sleutel per speler per dag, alleen als nieuw), naspelen van de tikken, claim van de uitslag vóór het tellen, ranglijst, gezamenlijke toren, dagen op rij. |
| Opslag | `src/server/redis-opslag.ts`, `geheugen-opslag.ts` | Zelfde koppelvlak: Redis op Reddit, een Map lokaal en in de toetsen. |
| Spel in de post | `src/client/game.ts` | Startscherm, spelen, invoer, einde. |
| Beeld en beweging | `src/client/basis.ts`, `scene.ts`, `held.ts`, `grot.ts`, `effecten.ts` | Maten en geheugen van het beeld; Gloop met squash en stretch, toren met veer, vliegende hoeden, HUD; de held (boog, tuimelen, slok, landen, weglopen); grot en gezamenlijke toren (beide eenmalig in een los doek getekend); veren, deeltjes, schermschok. |
| Uitslagvel | `src/client/uitslag.ts`, `public/uitslag.css` | Score, vakjes met uitleg, reactie met voorbeeld, lid worden, ranglijsten van vandaag en gisteren. |
| Post in de feed | `src/client/splash.ts`, `public/splash.html` | Gloop met toren, de dag, de knop die het spel groot opent. |
| Plaatjes | `public/kunst/` | Renders uit de 3D-modellen van Hats (`../kunst/render.sh`, `../kunst/knip.py`); maten en ankers in `kunst.json`. |
| Lokaal | `dev/local.ts`, `dev/schermen.py` | Server zonder Reddit; Playwright-speler die schermbeelden en een filmpje maakt. |

Toetsen: `src/shared/spel.test.ts` en `src/server/logica.test.ts` (`npm test`: types, lint, toetsen, bouw).
