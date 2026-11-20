# Ebb: de wijzerplaat wordt een patrijspoort

- status: open
- kanaal: tiktok
- soort: video
- product: ebb
- bestand: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/ebb-roep-1/ebb-roep-1-porthole-geluid.mp4
- geluid_check: GOED (gemiddeld -18,7 dB, piek -3,0 dB), 20 nov 2026 ±11:42 NL, lokale bouw met dezelfde code; na de workflow opnieuw op het releasebestand
- lengte: 0:15,6, staand 1080x1920
- tijd: 2026-11-24T18:00:00+01:00
- doel: geen meetadres voor Ebb; over te typen zoekregel "Search Ebb in the Connect IQ Store"
- gemaakt_door: filmmaker-hoofdchat
- vorige:

Quotum: de hoofdchat geeft voor november 1 reserveplek aan Ebb (TikTok); de Short mag in december.

## Titel
Garmin breathing app: your watch face becomes a porthole

## Tekst
Garmin breathing app: your round watch face becomes a porthole on a small sea. Breathe in and the water rises, breathe out and it falls. Hold your breath and you go under water, and new sea friends join as you keep coming back. Holds on land only: sit or lie down, never in or near water, never while driving, and only while it feels easy. We made Ebb for Garmin watches: $2.99, one payment, no subscription. Search Ebb in the Connect IQ Store. Screens from the Garmin simulator. #garmin #garminwatch #connectiq #breathwork #breathing #smartwatch

## Eerste reactie

## Bronnen
- Beeld: echte schermen van Ebb uit de Garmin-simulator (fenix 8 47 mm, simulatorrun 43327097299 op e40269e1, de ingediende app), tak `schermen`, map `garmin-adem/plaatjes/namen/`, plus `commercie/ebb/ebb-film.mp4` (dezelfde schermen met overvloeiers tussen in en uit, ook de bron van filmpje 4). Gebouwd met `commercie/filmpjes/week-1/maak.py`, specificatie `platformen/garmin/marketing/film/ebb-roep-1.json`, bronnen met sha256 in `bronnen.sha256`. Geen AI-beeld, geen stem, geen persoon. Geluid met code (sinustonen en ruis) via `commercie/filmpjes/geluid/geluid.py`, tijden in `geluid_ebb.py`; toets.py: beeld gelijk, -16,0 LUFS, piek -3,0 dBTP.
- In beeld, op volgorde: "Your watch face becomes a porthole" (0 tot 2,6 s), "Breathe in: the sea rises / Breathe out: it falls" (tot 5,5), "Hold your breath, and you go under water" (tot 7,8), "New sea friends join as you keep coming back" (tot 10,4), veiligheidsscherm van de app met "Holds on land only, only while it feels easy" (tot 13,0), menu met "Ebb for Garmin, $2.99 / Search Ebb in the Connect IQ Store" (tot 15,6). De hele tijd klein: "Screens from the Garmin simulator".
- Patrijspoort, water stijgt bij in en zakt bij uit, onder water bij inhouden, "new sea friends join as you keep coming back", "Hold only while it feels easy", "For practice on land only: sit or lie down, never in or near water, never while driving", "One payment ... No subscription": letterlijk in de Engelse winkeltekst (`platformen/garmin/upload/ebb-en.md`), en GEZIEN in de live winkel-API (apps.garmin.com, beschrijving en, 20 nov ±11:40 NL).
- Veiligheidsscherm in beeld ("Sit or lie down. Never while standing, never in or near water, never while driving."): het echte scherm `veilig-1`, tekst staat in `producten/garmin-adem/source/Veilig.mc` op tak `claude/garmin-ebb-101` (GEZIEN).
- $2.99: GEZIEN in de winkel-API 20 nov ±11:40 NL (`listPrice` 2.99 USD). Europrijs niet in de API gezien, dus niet genoemd.
- "Search Ebb in the Connect IQ Store": zoeken op "ebb" geeft Ebb op plek 1, Ebb Calm op 2 (GEZIEN 20 nov ±11:40 NL met `commercie/ebb/zoek-plekken.py`). Er is geen apart meetadres voor Ebb: dortus.com/ebb/ bestaat (200, met Amami) maar telt samen met alle andere bezoekers van die pagina, net als dortus.com/click-joints volgens REGELS.md; dus niet in de TikTok. Geen klikbare link, geen "link in bio", geen https.
- Geen medische claim: niets over stress, slaap, rust of longen; "Ebb has no CO2 or O2 tables and is not a medical device" staat in de winkel.
- Niet gelijk aan de laatste 14 dagen: het enige Ebb-filmpje dat uitging is filmpje 9 (ogen dicht, trillen per fase, ingepland 18 nov volgens `commercie/filmpjes/planning.md`); dit is een ander idee en ander beeld. Niets over Ebb in `commercie/geplaatst.md`.
- Haak in de eerste seconde: beeld 0,0 s is al het ronde scherm met de zee en de krab, met de tekst "Your watch face becomes a porthole" (zelf bekeken).
- Zelf bekeken (skill kijken): 16 beelden (1 per seconde) en 4 op halve grootte (0,5 / 6,5 / 11,5 / 14,5 s): tekst leest, binnen beeld, horloge rond op donker, geen simulatorrand, onderste derde leeg voor de tekst van TikTok.

## Let op (voor de hoofdchat, vóór dit naar de wachtrij gaat)
- Het filmpje staat nog niet op een openbare URL. De release `ebb-roep-1` vraagt een workflow; die heb ik niet gepusht (de toestemmingscontrole hield een nieuwe workflow tegen). Het voorstel staat klaar in `platformen/garmin/marketing/film/ebb-roep-film.yml.voorstel`. Zet de hoofdchat die als `.github/workflows/ebb-roep-film.yml` op main, dan bouwt hij beide filmpjes en zet hij ze in de release. Daarna: `curl -sIL` op de URL hierboven (200), `geluid_check.py` op het releasebestand, en dit bestand naar `marketing/wachtrij/`.

- **Gedaan door de hoofdchat, 20 nov 13:55 NL:** workflow `ebb-roep-film.yml` staat op main (gelijk aan het voorstel), run 1 op fe15a6dd geslaagd (20 nov 11:55 NL), inclusief de stap Geluidscontrole (`geluid_check.py`) op precies de bestanden in de release. Release `ebb-roep-1` heeft beide `-geluid.mp4` (1,8 MB elk); de URL hierboven geeft bij GitHub 302 naar het bestand (GEZIEN). Concept naar de wachtrij gezet.

## Keuring

## Oranje-besluit

## Na plaatsen
