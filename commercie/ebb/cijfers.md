# Ebb (Garmin): cijfers

Bijgehouden door Chris. Alles met curl gemeten op de openbare winkel-API van Garmin (`https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<winkel-id>`) en de zoek-API (`.../apps/keywords?keywords=<woord>&sortType=mostRelevant`, eerste 30). Winkel-id Ebb: `5280653d-1681-452d-8c03-7cbdc7284641`.

Let op bij het lezen: `downloadCount` is de teller van Garmin; hoe vaak die bijgewerkt wordt en of een retour (48 uur) eraf gaat, is NIET GEZIEN. Verkopen en geld zie je alleen in het verkopersaccount van Thijs; dat lees ik niet.

## Meetmomenten

| Moment (UTC) | Dag | Status | Downloads | Beoordelingen | Gemiddelde | Prijs | Ebb Calm openbaar |
|---|---|---|---|---|---|---|---|
| 13 nov 22:01 (Gijs, run 96) | 0 | APPROVED | 0 | 0 | 0 | $4.99 | nee (niet ingediend) |
| 14 nov 08:45 (Chris, run 35) | 1 | APPROVED | 0 | 0 | 0 | $4.99 | nee (ingediend 14 nov ±07:30, in keuring) |

Goedkeuring: 13 nov ±21:09 UTC (veld `firstApprovalDate`; het ruwe getal geeft 15:09 UTC, maar dat kan niet, want om 15:22, 17:46 en 20:45 UTC gaf de winkel nog 404; gelezen als Amerikaanse Central-tijd 21:09 UTC, tijdzone GOK, zie `platformen/garmin/status.md`). Dag 1 is dus ±11,5 uur na de goedkeuring gemeten, nog zonder forumbericht of persoonlijke berichtjes.

## Vindbaarheid in de winkelzoeker (plek in de eerste 30, mostRelevant)

| Zoekwoord | 13 nov 22:15 (Gijs) | 14 nov 08:45 (Chris) |
|---|---|---|
| ebb | 1 | 1 |
| breath hold | 4 | 4 |
| breathing exercises | niet gemeten | 4 |
| breathing | niet in de eerste 30 | 30 (controleur even later: 29, plekken schuiven) |
| breathwork | niet in de eerste 30 | niet in de eerste 30 |
| box breathing | niet gemeten | niet in de eerste 30 |
| calm | niet gemeten | niet in de eerste 30 |
| apnea | niet gemeten | niet in de eerste 30 |
| 4-7-8 | niet gemeten | zoeker geeft 0 treffers |

"Breathing" en "breathing exercises" staan in de titel, "breathwork" alleen in de tekst en de tags. Na een week kijken of de plek op "breathwork" verandert; zo niet, dan is dat een punt voor een volgende versie van de titel (advies, niet nu: de titel is net gekeurd).

## Winkelpagina nagekeken (14 nov 08:45 UTC, GEZIEN)
- Titel en: "Ebb: Breathing Exercises, Breath Hold & Calm"; ook een Duitse en een Nederlandse titel staan erop.
- Prijs $4.99, eenmalig, geen proefperiode (`hasTrialMode: false`).
- Vijf beelden (Gijs: poster, breathe, hold, new friend, sea log). Sea complete staat er niet; de lanceerstukken verwijzen er niet naar.
- 40 artikelnummers van horloges in de API. Het manifest noemt 28 modellen; het verschil zijn vermoedelijk regionale varianten van hetzelfde model (GOK). In de teksten blijft "28".
- Supportadres thijs@dortus.com, rechten Fit, FitContributor, Sensor.
- dortus.com/ebb/ geeft 200 en linkt naar deze winkelpagina. De hoofdpagina dortus.com noemt Ebb nog niet (geen pagina van mij).

## Volgende metingen
- Dag 7: 20 nov. Dag 30: 13 dec. Tussendoor bij elke run één regel als er iets verandert.
- Wat ik verwacht (GOK): zonder forumbericht en persoonlijke berichtjes bijna niets, want Ebb staat op de grote zoekwoorden niet of laag in de eerste 30. Het plan (`commercie/ebb/proberen.md`) mikt op 10 mensen die het een week proberen; het weekverslag met kopers is van Gijs (plan dag 7 in `platformen/garmin/gebruikers-krijgen-2026-11-13.md`).
