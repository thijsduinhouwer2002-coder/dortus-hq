# Garmin Connect IQ: de nieuwe hoek microfoon en luidspreker (Toybox.Audio)

Noor, pionier, 17 nov 2026. Cijfer **7**. Advies: **ja, nu, met kleine inzet via het bestaande Garmin-team (Gijs)**: een brede spraakmemo-app, binnen 2 weken in de winkel.

Soort kans: "nieuwe hoek in een bestaande grote winkel" (voorstel Joris, verhaal 33). Geen nieuw platform, wel een functie die er een maand geleden nog niet was, in een winkel met miljoenen horloges, en de ploeg heeft het gereedschap al draaien.

## Wat er nieuw is
- Connect IQ SDK 9.3.0, uitgebracht **20 oktober 2026** (GEZIEN, https://developer.garmin.com/downloads/connect-iq/sdks/sdks.json: `'9.3.0', 'October 20, 2026'`).
- Nieuwe module `Toybox.Audio` met `Audio.Capture` (opnemen) en `Audio.Output` (afspelen), vanaf API-level 6.0.3, met de rechten `AudioInput` en `AudioOutput` (GEZIEN, https://developer.garmin.com/connect-iq/api-docs/Toybox/Audio.html en .../Audio/Capture.html). Formaten WAV en Ogg, ruisonderdrukking (FILTER_NREC). Werkt in watch-apps, glances en audio content providers, niet in wijzerplaten of datavelden (GEZIEN).
- Opnemen kan alleen met de app op de voorgrond (fout `CAPTURE_ERR_BACKGROUNDED`, GEZIEN). Tekst-naar-spraak zit er niet in (DERDEN, https://www.smartwatchlife.jp/84960/).
- Toestellen (GEZIEN, zelfde pagina): fēnix 8 en 8 Pro, fēnix 9, fēnix E, Forerunner 70, 170, 570 en 970, Venu 4, Venu X1, vívoactive 6, Enduro 3 en 4, MARQ Gen 3, Approach S72, D2 Mach 2. Dat zijn de nieuwste en duurste modellen.

## De vijf vragen

**1. Groot publiek en groeiend?** Ja. Garmin verkoopt jaarlijks miljoenen horloges; de toestellen met microfoon zijn de nieuwe lijnen van 2024 tot 2026, dus elke nieuwe koper van een fēnix, Forerunner 570/970 of Venu 4 hoort erbij. Aantal toestellen met microfoon: GOK, enkele miljoenen. Geen eigen telling mogelijk.

**2. Winkel of hoek jong?** Ja, de hoek is 4 weken oud. Eigen meting in de Connect IQ Store (GEZIEN, 17 nov 08:50 UTC, `data/garmin-audio-meet.py`, uitkomst `data/garmin-audio-2026-11-17.json`): in 586 watch-apps rond 16 zoekwoorden (voice memo, recorder, dictation, transcribe, tuner, decibel, walkie, voice assistant ...) vragen er **17 het recht AudioInput** en 12 AudioOutput. Alle 17 met AudioInput zijn in november bijgewerkt en hebben 1 tot 10 downloads, behalve AllTelegram (100). De winkel toont downloads in emmers (1, 10, 100, 1.000). Let op: dit is niet de hele winkel, alleen wat op die woorden terugkomt; GitHub gaf 2 repos met `Audio.Capture` (DERDEN via hulpagent).

**3. Kan er betaald worden?** Ja, nu al. Betaalde apps in de Connect IQ Store werken; in deze hoek vragen al Remote for Claude $2,99 en Decibel Meter $1,99 (GEZIEN, veld pricing). Ons Garmin-team verkoopt Ebb al voor $4,99, dus de route (account, Merchant) ligt er.

**4. Vraag te zien?** Indirect. Op de woorden "voice memo" en "voice assistant" geeft de winkel 236 en 286 treffers terug (GEZIEN), maar bijna alles daarvan zijn oude apps die via de telefoon werken of alleen een knop zijn. Garmin-forums vragen al jaren om een spraakmemo op het horloge (GOK, niet nagelezen deze run). De eerste golf (SayNote AI, Voxwrist Ask, WristVoice AI, AI Buddy, Remote for Claude) zit vooral op "praat met een AI"; dat vraagt een server en kost per gebruik.

**5. Eerste plek te pakken?** Ja. In de basistaak spraakmemo (knop, praten, terugluisteren, lijst, met datum en plek) staat nu WristMemo met 1 download en 0 reviews (GEZIEN); geen enkele app met AudioInput heeft meer dan 2 reviews, behalve AllTelegram (8). Er is geen nummer één. Joris (verhaal 33): de winnaars van een nieuwe hoek doen de brede basistaak en komen in de eerste weken. Dat is nu.

## Productidee (eerste versie)
**Spraakmemo voor hardlopers en wandelaars:** één knop, praten, klaar. Memo's in een lijst met tijd, duur en (als de app GPS mag) de plek op de route; terugluisteren via de luidspreker; trillen bij start en stop. Werkt zonder telefoon en zonder server.
Waarom wij: de huidige apps willen een AI-gesprek (server, account, kosten); wij doen de basistaak goed, snel en zonder abonnement. Gratis versie met een paar memo's, betaald (eenmalig, ±$3,99 GOK) voor onbeperkt en de plek op de kaart. Later: memo's naar de telefoon (via Garmin Connect of een web-upload, nog uitzoeken of binaire upload kan).

## Risico's, eerlijk
- **Memo's van het horloge krijgen** is de zwakke plek. Lukt dat niet zonder eigen server, dan blijft het bij terugluisteren op het horloge. Eerst uitzoeken (Gijs, 1 run).
- **Simulator en microfoon:** onbekend of de simulator in de cloud opnemen nabootst (GOK). Zo niet, dan test het team de stroom met nep-geluid en moet de echte test op een horloge (bij Thijs, als hij een toestel met microfoon heeft; staat bij Thijs).
- **Garmin doet het zelf:** de nieuwste horloges hebben al een ingebouwde spraakassistent en notities via de telefoon (GOK). Als Garmin een eigen memo-app op het horloge zet, is de basistaak weg.
- **Les van Ebb:** Thijs zei vanochtend dat Garmin "nu niks doet". Het verschil: Ebb kwam in een volle categorie (ademapps sinds jaren), dit is een hoek van 4 weken zonder nummer één. Meten: wordt het in 4 weken na livegang geen 100+ downloads, dan stoppen.

## Wat het team nodig heeft
SDK naar 9.3.0 (het team draait nu 9.2.0, GEZIEN in `platformen/garmin`), API-level 6.0.3 in de manifest, recht AudioInput en AudioOutput. Geen geld nodig behalve wat er al is.

## Herhaalmeting
`python3 -I data/garmin-audio-meet.py data/garmin-audio-<datum>.json`, elke week. Teken dat de kans sluit: een app met AudioInput in de basistaak memo boven 1.000 downloads of 20+ reviews.

## Cijfer en advies
**7.** Groot publiek, hoek 4 weken oud, 17 apps met microfoon zonder nummer één, betalen werkt, en wij kunnen binnen een week een eerste versie hebben omdat het Garmin-team al bouwt en test in de cloud. Geen 8: het aantal toestellen met microfoon is een gok, en of memo's het horloge af kunnen is nog niet uitgezocht.
Advies aan de hoofdchat: **ja**, geef het Garmin-team (Gijs) dit als volgende product, met eerst één run om de twee open punten (upload en simulator) uit te zoeken.
