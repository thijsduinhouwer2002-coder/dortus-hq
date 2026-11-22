# Herweging: Reddit Devvit (Kees, 9 nov 2026)

Oud cijfer 6 (Noor, 8 nov). Hans: geld is een eenmalig fonds tot 31 dec 2026, moderators betalen niet.

## De doorslaggevende meting
Het geld voor een kleine maker bij mod-tools is het Developer Fund: $500 bij 50 installs (in subreddits met 300+ wekelijkse bezoekers), $1.500 bij 250, $3.500 bij 1.000. Dus de vraag voor punt 1 van een 8 is simpel te tellen: **hoeveel apps van de laatste zes maanden halen 50 installs?** Geteld op de hele openbare appgids (1.759 apps, data van Noor van 8 nov, `platformen/pionier/data/devvit-apps-2026-11-08.json`). Installs in de gids zijn alle installs, dus dit is een bovengrens voor wat het fonds telt.

## Wat eruit kwam (GEZIEN)
| Lichting | Nieuwe apps | 50+ installs | 250+ | 1.000+ | Mediaan |
|---|---|---|---|---|---|
| mei 2026 | 213 | 4 | 3 | 1 | 3 |
| jun 2026 | 141 | 0 | 0 | 0 | 2 |
| jul 2026 | 176 | 6 | 1 | 0 | 2 |
| aug t/m okt 2026 | 470 | 0 | 0 | 0 | 2 |

- Mei t/m okt samen: **10 van 1.000 apps (1%) halen de eerste trede van $500**, 4 halen 250, 1 haalt 1.000 (Image Magician).
- Alleen mod-tools (167 in die periode): 8 met 50+ (5%), 45 met 10+. Van die 8 zijn er 5 van ervaren Reddit-botmakers (fsv 2, berntout 3, Watchful1 1 bij 82). Echte nieuwkomers boven 50: Image Magician (1.319), Automated Sticky Comments (412), Mod Recruit (184), Mobile Markdown (50).
- Spellen (433 van de 1.000) verdienen via dagelijkse gebruikers ($4.000 bij 5.000 per dag) en gold; die tellers zijn niet openbaar. Het blog met uitbetalingen stopt bij november 2025 ($163.000 aan ±70 apps, toen nog de ruimere regels van H1).
- Geen opvolger van het fonds na 31 dec 2026 gevonden (één zoekopdracht, alleen oude aankondigingen) (GOK dat er geen komt).

## Nieuw cijfer: 5, valt af
Punt 1 faalt duidelijk: 1% van de nieuwe apps haalt de laagste uitbetaling, en sinds augustus geen enkele. Punt 2 (bereik voor nieuwkomers) faalt daarmee ook: de appgids levert nieuwe mod-tools nauwelijks installs op. De groei van de winkel die Noor zag, is vooral aanbod (veel nieuwe apps met 2 installs), geen vraag. En het geld stopt over 7 weken.

## Wat er nog schuurt
- Jonge apps hebben tijd nodig, maar ook de lichtingen van mei en juli (4 tot 6 maanden oud) halen maar 2 tot 3%.
- Spellen zijn niet gemeten: daar is het geld anders (gebruikers, gold) en niet openbaar. Wie Devvit ooit opnieuw wil wegen, moet daar beginnen, niet bij mod-tools.
- Niet nagekeken door een controleur: het is een telling op data die Noors controleur al nakeek, en het script hieronder geeft hetzelfde.

Telling opnieuw doen: per maand van `aangemaakt` het aantal apps met `installs` >= 50, 250 en 1000.
