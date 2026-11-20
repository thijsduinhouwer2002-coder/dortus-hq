# Ebb: inhouden en je horloge gaat onder water, met 24 zeedieren

- status: oranje
- kanaal: yt-short
- soort: video
- product: ebb
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/ebb-roep-1/ebb-roep-2-sea-friends-geluid.mp4
- geluid_check: GOED (gemiddeld -19,7 dB, piek -2,0 dB), 20 nov 2026 ±11:42 NL, lokale bouw met dezelfde code; na de workflow opnieuw op het releasebestand
- lengte: 0:15,2, staand 1080x1920
- tijd: 2026-12-02T18:00:00+01:00
- doel: https://dortus.com/ebb/ (niet klikbaar in een Short; telt mee onder "Ebb" op het scorebord, niet als eigen kanaal)
- gemaakt_door: filmmaker-hoofdchat
- vorige:

Quotum: de hoofdchat geeft voor november 1 reserveplek aan Ebb (TikTok); de Short mag in december. Elke Short is oranje: de hoofdchat beslist.

## Titel
Garmin breathing app: hold your breath and your watch goes under water

## Tekst
Garmin breathing app Ebb: hold your breath and your watch face goes under water with a sea animal. There are 24 sea animals, earned with sessions and weeks in a row, never by holding longer. Pick the one that swims with you. Holds on land only: sit or lie down, never in or near water, never while driving, and only while it feels easy. We made Ebb for Garmin watches: $2.99, one payment, no subscription. dortus.com/ebb or search Ebb in the Connect IQ Store. Screens from the Garmin simulator. #garmin #garminwatch #connectiq #breathwork #breathhold #shorts

## Eerste reactie

## Bronnen
- Beeld: echte schermen van Ebb uit de Garmin-simulator (fenix 8 47 mm, simulatorrun 43327097299 op e40269e1, de ingediende app), tak `schermen`, map `garmin-adem/plaatjes/namen/` (nachtscènes onder water met krab, octopus, zeepaard, schildpad, otter, kreeft, zeekomkommer; "new friend", sea log 24 van 24, veiligheidsscherm, menu). Gebouwd met `commercie/filmpjes/week-1/maak.py`, specificatie `platformen/garmin/marketing/film/ebb-roep-2.json`, bronnen met sha256. Geen AI-beeld, geen stem, geen persoon. Geluid met code via `geluid.py`, tijden in `geluid_ebb.py`; toets.py: beeld gelijk, -17,0 LUFS, piek -1,9 dBTP.
- In beeld: "Hold your breath and your watch goes under water" (0 tot 2,6 s), "24 sea animals can swim with you" (tot 5,0), "You earn them by showing up, never by holding longer" (tot 7,7), "Pick the one that swims with you" (tot 10,0), veiligheidsscherm met "Holds on land only, only while it feels easy" (tot 12,6), menu met "Ebb for Garmin, $2.99 / Search Ebb in the Connect IQ Store" (tot 15,2). De hele tijd klein: "Screens from the Garmin simulator".
- Onder water bij inhouden met een zeedier, "24 sea animals, earned with sessions and weeks in a row, never by holding longer", "Pick the one that swims with you", "Hold only while it feels easy", "on land only: sit or lie down, never in or near water, never while driving", "One payment ... No subscription": letterlijk in de winkeltekst (`platformen/garmin/upload/ebb-en.md`), GEZIEN in de live winkel-API 20 nov ±11:40 NL.
- De inhoudschermen tonen allemaal 1:45 en 61 bpm: één testscène met steeds een ander dier (zelfde punt als filmpje 6), daarom geen tijd of hartslag in de tekst.
- Veiligheidsscherm: echt scherm `veilig-1`, tekst in `Veilig.mc` op tak `claude/garmin-ebb-101` (GEZIEN).
- $2.99: GEZIEN winkel-API 20 nov. dortus.com/ebb/: 200, met Amami-script en de winkellink (GEZIEN met curl 20 nov ±11:40 NL). Zoeken op "ebb": Ebb plek 1 (GEZIEN, `zoek-plekken.py`).
- Links onder een Short zijn niet klikbaar (sinds 31 aug 2023, DERDEN, staat in REGELS.md), dus deze Short verkoopt weinig rechtstreeks (GOK).
- Geen medische claim. Niet gelijk aan de laatste 14 dagen (filmpje 9 ging over trillen met de ogen dicht).
- Zelf bekeken (skill kijken): 16 beelden (1 per seconde) en 4 op halve grootte (0,5 / 4,0 / 8,5 / 14,0 s): tekst leest, binnen beeld, dieren goed te zien.

## Let op (voor de hoofdchat, vóór dit naar de wachtrij gaat)
- Zelfde als bij de TikTok: eerst de workflow uit `platformen/garmin/marketing/film/ebb-roep-film.yml.voorstel` op main, dan URL (200) en geluid_check op het releasebestand nakijken, dan naar `marketing/wachtrij/`.

- **Gedaan door de hoofdchat, 20 nov 13:55 NL:** workflow `ebb-roep-film.yml` staat op main (gelijk aan het voorstel), run 1 op fe15a6dd geslaagd (20 nov 11:55 NL), inclusief de stap Geluidscontrole (`geluid_check.py`) op precies de bestanden in de release. Release `ebb-roep-1` heeft beide `-geluid.mp4` (1,8 MB elk); de URL hierboven geeft bij GitHub 302 naar het bestand (GEZIEN). Concept naar de wachtrij gezet.

## Keuring
- keurder: Roep-Keurder, 20 Nov 2026 20:45 NL
- 1 bron klopt: ja
- 2 geen AI-zin, geen AI-melding: ja
- 3 geen medische claim: ja
- 4 geen Hats-spelerstekst: ja
- 5 echt beeld zelf bekeken, -geluid.mp4 en geluid_check GOED: ja (beelden op 0,1, 1, 7,6 en einde bekeken: echte simulatorschermen, tekst binnen beeld; geluid_check zelf gedraaid: GOED)
- 6 geen persoonsgegevens: ja
- 7 past bij het kanaal: ja
- 8 niet gelijk aan een post van de laatste 14 dagen: ja
- 9 geen AI-beeld, AI-stem of AI-persoon: ja
- 10 schrijft als Dortus, niet als Thijs: ja
- techniek-check: oranje: YouTube Short (REGELS) en prijs; geen < of >, geen Gumroad, geen klikbare URL nodig; media-URL downloadt (GET), HEAD via de proxy geeft 401
- uitkomst: oranje
- reden: Elke YouTube Short is oranje; daarbij noemt de tekst de prijs ($2.99) en is de Short alleen uit de reserve toegestaan.
- 8 noot: niets over Ebb in commercie/geplaatst.md

## Oranje-besluit

## Na plaatsen
