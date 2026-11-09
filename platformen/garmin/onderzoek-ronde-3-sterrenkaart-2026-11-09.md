# Ronde 3: sterrenkaart (9 november 2026, Gijs)

Vraag: is een betaalde sterrenkaart (wat staat er nu boven je, richten met het kompas) een goed eerste product?
Bronnen: winkel-API van Garmin (`https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>`, opgehaald 9 nov 22:40), dataset `platformen/verkenner/data/garmin-niet-wijzerplaten-2026-11-09.json.gz`, en een onderzoeker (forums, API-docs).

## Uitkomst: valt af
De hoek die in ronde 2 open leek ("richt je horloge op de hemel, zie wat daar staat") is in 2026 al door vijf apps bezet, drie daarvan sinds september. Wij zouden nummer zes zijn, en een sterke maker (Rampo) heeft er al vier apps en verkoopt goed. Dat is dezelfde regel als in ronde 1: een hoek die vol loopt valt af, ook als er verkocht wordt.

## Wat er al staat (GEZIEN, winkel-API, tenzij anders vermeld)
| App | Maker | Sinds | Downloads | Cijfer (reviews) | Prijs | Richten met kompas? |
|---|---|---|---|---|---|---|
| SkyWatcher | Jeff_Crystal | jun 2025 | 10.000+ | 3,5 (17) | gratis, Pro via code buiten de winkel | nee (geen Sensor-permissie) |
| AstroRadar | Brapps_Garmin | jan 2026 | 1.000+ | 4,7 (6) | betaald, prijs niet in API | ja: "point the watch at the horizon to activate the vertical view" (Sensor) |
| Planet Compass | Rampo | jan 2026 | 100+ | 4,8 (14) | $1,99 | ja (Sensor) |
| Stargazer (wijzerplaat) | Rampo | mrt 2026 | 1.000+ | 4,5 (39) | $3,99 | nee, wijzerplaat |
| Skyfix: Point at the Sky | ThijsGer | sep 2026 | 100+ | 5,0 (1) | $1,99 | ja, kompas plus versnellingsmeter: "hold your wrist up towards something bright, and it tells you what you are looking at" |
| Night Sky Atlas | Rampo | sep 2026 | 100+ | 4,2 (5) | $1,99 | ja: "turns the compass into a window on the real sky", 2000+ sterren, 88 sterrenbeelden, deep-sky, kometen |
| Planet Finder | Lenoc | okt 2026 | 100+ | 4,0 (1) | gratis | ja: "Turn around and the display turns with you" |
| The Planets | flug32 | dec 2024 | 10.000+ | 3,6 (18) | gratis | nee |

Ook van Rampo: Peak Finder Compass ($3,49, 1.000+ sinds mei 2026, 30 reviews). Rampo bouwt dus snel, mooi en in dezelfde hoek.

## Wat wel klopte
- Kopers vragen om richten op de hemel: SkyWatcher krijgt 1 ster met "nothing is moving on my screen" (GEZIEN, review), een oude MARQ-draad vraagt "just move your hand around the sky and see stars" (GEZIEN: https://forums.garmin.com/outdoor-recreation/outdoor-recreation-archive/f/marq-series/226071/marq-astronomer).
- Garmin doet het zelf niet: alleen zon- en maantijden en maanfase (GEZIEN: handleiding tactix 8; Sun & Moon van Garmin 500.000+ met 2,7).
- Technisch kan het: `Sensor.Info.heading`, `mag` en `accel` in Connect IQ (GEZIEN: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/Info.html).

## Waarom toch nee
1. De vraag wordt al bediend, door makers die precies ons idee al hebben uitgebracht (tabel).
2. Nieuwe sterrenkaarten van 2026 halen meestal 100+, alleen AstroRadar 1.000+ (GEZIEN). Als zesde komen we met $1,99 tot $3,99 op een paar honderd dollar in totaal (GOK).
3. Ons enige onderscheid zou uiterlijk zijn. Dat is te weinig tegen Rampo, die al 4 tot 5 sterren haalt.

## Wat ik ervan leer voor ronde 4
- Zoek niet op idee maar op bewijs: van de 757 apps die sinds 2025 via de Garmin-kassa betaald zijn, haalden er 37 de 1.000+ (GEZIEN, dataset). Begin bij die 37 en zoek waar één verkoper alleen staat, Garmin het niet zelf doet, en de hoek niet vol loopt.
- Kijk bij elke kandidaat eerst naar nieuwe apps van de laatste drie maanden, niet alleen naar de nummer één. Die check had ronde 2 meteen moeten doen.
- Betalen via de Garmin-kassa (geen code per mail) blijft een pluspunt: Stargazer kreeg "I've paid for it but not received any unlock code" (GEZIEN).
