# GamePix, Italiaanse webspelportal en verdeler

Onderzocht door Vera, 15 nov 2026 run 14:31 (Amsterdam). Snelle schifting, geen volledige meting. Geen aparte controleur: het oordeel hangt aan wat niet te meten is, niet aan een eigen telling.

## Wat ik zag
- **Website niet leesbaar:** elke spelpagina op www.gamepix.com geeft een Cloudflare-blokkade (403), ook de voorpagina (GEZIEN, 15 nov). Niet omzeild. De sitemap is wel leesbaar: 20.013 spelpagina's.
- **Open feed voor uitgevers:** feeds.gamepix.com/v2/json met de voorbeeldcode sid=1 uit de eigen RSS-pagina geeft 15.081 spellen met datum en een quality_score van GamePix, maar **geen plays, stemmen of maker** (GEZIEN). Data: `data/gamepix-feed-2026-11-15.csv`.
- **Drukte:** nieuwe spellen in de feed per maand: jul 312, aug 216, sep 409, okt 620, en al 574 in de eerste helft van november (GEZIEN). Het tempo stijgt hard, net als bij Playgama.
- **Rang als zwakke maat voor bereik:** van 775 spellen van 3 tot 6 maanden oud staan er 20 (2,6%) in de top 500 op quality_score; de mediaan staat op plaats 8.814 van 15.081 (GEZIEN). Wat quality_score precies meet zegt GamePix niet; nieuwe spellen hebben bijna allemaal dezelfde waarde 0,324, dus waarschijnlijk een startwaarde zonder data (GOK).
- **Geld (GEZIEN, partners.gamepix.com/developers en /guidelines/submission):** maker krijgt 50% van de netto reclame-inkomsten, niet exclusief. Met "Allow Distribution" gaat het spel ook naar sites van derden, zonder dat vinkje alleen naar gamepix.com. Drempel, betaalwijze en of een particulier mag: niet gevonden (voorwaarden niet leesbaar).
- **Bewijs dat kleine makers verdienen:** niet gevonden.

## Advies
**Cijfer 2, nee zonder volledige meting.** Kassa met 50% bestaat, maar bereik van nieuwe spellen is niet te meten (site geblokkeerd, feed zonder plays) en er is geen geldbewijs. Het model lijkt op GameDistribution (cijfer 2): een verdeler naar duizenden sites. Bij webspellen beslist de portal waar spelers zelf komen, en dan zijn Poki en CrazyGames sterker gemeten. Hooguit een bijkanaal voor een spel dat niet exclusief bij Poki zit.

**Hoe het wel te meten is:** met een makersaccount (dashboard met RPM en plays per spel, door Thijs aan te maken) of als de Cloudflare-blokkade ooit wegvalt. Niet de moeite waard zolang Poki en Playables voorgaan.
