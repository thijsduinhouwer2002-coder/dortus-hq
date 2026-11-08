# Home Assistant Marketplace (HACS in de kern)

Onderzocht 8 nov 2026 door Noor (pionier). Onderzoeker: één agent voor groei, geld, vraag en reacties. Zelf gemeten: de release-post, de hele catalogus via data-v2.hacs.xyz (script `data/ha-marketplace-meet.py`, eerste regel in `data/ha-marketplace.csv`).

**Cijfer: 2. Advies: nee.** Het platform groeit hard, maar de winkel is niet jong (HACS bestaat sinds 2019, ±6.200 items) en Home Assistant zegt letterlijk dat betalen er nooit komt. Volgens de rol is geen enkel plan voor geld een nee; hier is het zelfs een plan tegen geld.

## Wat er nieuw is
In release 2026.11 (4 nov 2026) zit HACS als "Marketplace" onder Instellingen, op elk soort installatie, zonder GitHub-account, en een integratie installeert zonder herstart (GEZIEN, https://www.home-assistant.io/blog/2026/11/04/release-202611/). Geen review: "It is not tested, audited, or supported by the Home Assistant project" (GEZIEN, zelfde pagina). HACS is door de maker (ludeeus) geschonken aan de Open Home Foundation (GEZIEN, zelfde pagina).

## De vijf vragen

**1. Groeit het platform hard? Ja.**
- Installaties met analytics aan: 391.213 (7 nov 2024), 532.929 (7 nov 2025), 723.629 (7 nov 2026), dus ±35% per jaar, twee jaar op rij (DERDEN via agent, uit https://analytics.home-assistant.io/data.json).
- Totaal ±2,28 miljoen huishoudens; Open Home Foundation CHF 8,84 mln omzet in 2025 uit licentiepartners en giften (DERDEN, https://www.openhomefoundation.org/media-room/annual-report-factsheet/).
- Core op GitHub ±92.000 sterren (DERDEN, https://repos.ecosyste.ms).
- Motor: stichting met eigen inkomen (Nabu Casa-abonnementen, hardware), trend naar lokaal en privé slim huis. Dit platform blijft; het risico zit niet in het platform.

**2. Is de winkel jong? Nee.** Alleen de plek is nieuw. De catalogus is dezelfde als HACS:
- 4.982 integraties, 1.078 kaarten (plugins), 122 thema's, 12 templates (GEZIEN, data-v2.hacs.xyz, 8 nov 2026).
- Downloads staan alleen bij integraties. Van de 4.982 hebben er 1.611 een teller boven 0; mediaan 0, het 90e percentiel 94, 198 integraties boven 1.000 (GEZIEN). Top: Alarmo 79.009, Xiaomi Miot 78.742, Bambu Lab 76.827 (GEZIEN). De teller telt waarschijnlijk alleen installaties met analytics aan (GOK).
- Kaarten: Mushroom 5.243 sterren, Bubble Card 4.694, mini-graph-card 3.910, button-card 2.524, apexcharts-card 1.892 (GEZIEN). Mediaan van alle kaarten 9 sterren.
- Er komt nu een vloed aan door AI gemaakte integraties bij, onder andere één maker met 91 pakketvolg-integraties "with the help of Claude"; gebruikers vragen om filters en om makers te kunnen verbergen (DERDEN, https://community.home-assistant.io/t/1032171).

**3. Kan er betaald worden? Nee, en dat blijft zo.**
- Letterlijk: "Everything in the Marketplace is free, and that will not change." (GEZIEN, release-post).
- Toon in de community overwegend tegen betaalde uitbreidingen ("Look up what the S in HACS stands for") (DERDEN, https://community.home-assistant.io/t/tell-me-im-wrong/1029682).
- Geld verdienen lukt alleen met een eigen dienst buiten de winkel: Frigate+ $50 per jaar (DERDEN, https://frigate.video/plus). Giften leveren bijna niets op: Mushroom 11 sponsors ooit, 0 actief; Advanced Camera Card 15 en 0; Powercalc 1 en 0 (DERDEN, https://sponsors.ecosyste.ms).

**4. Is er vraag? Ja, maar vooral voor dingen die in de kern horen.** Meeste stemmen in Feature Requests: inloggen met OIDC/SSO (1.020), tweerichtingsaudio deurbel (475), temperatuursensor HomePod mini (398), meerdere gebruikers met rechten (295), Eufy-camera's (269), pincode op een view (115) (DERDEN via agent, https://community.home-assistant.io/c/feature-requests/13/l/top.json?period=all). Terugkerend thema: gezinsgebruik en rechten, energiekosten per apparaat. Veel daarvan kan een uitbreiding niet goed oplossen (rechten zitten in de kern).

**5. Is de eerste plek te pakken? Nauwelijks, en het levert geen geld op.** Kaarten hebben sterke, gratis leiders met duizenden sterren (Mushroom, Bubble Card). Een hoek als "energiekosten per apparaat" heeft al Powercalc en de ingebouwde energiepagina. Nummer één worden kan in een kleine hoek, maar dan als gratis project zonder weg naar geld binnen de winkel.

## Risico
Het platform haalt het zeker. Het risico voor ons is anders: we bouwen gratis werk tussen een vloed AI-projecten, zonder betaalroute. Een teken dat het verandert: de Open Home Foundation kondigt een betaalde laag, een "Works with"-programma voor software of een omzetdeling aan. Gezien de letterlijke belofte verwacht ik dat niet (GOK).

## Eerste productidee (alleen als trechter, niet voor nu)
Een gratis kaart of integratie die naar een eigen betaalde dienst leidt (het Frigate+-model), bijvoorbeeld een gezinsdashboard met pincode en kindweergave. Dat is een gewoon SaaS-bedrijf met een gratis lokmiddel, geen pionierskans op een jonge winkel. Bovendien botst een betaalde cloud met de cultuur van lokaal en privé.

## Wat ik niet kon meten
- Downloads van kaarten en thema's: niet in de openbare data.
- Reddit en github.com gaven de agent 403.
- Nabu Casa-abonnees en verkoop van Green en Voice: niet openbaar.
- Of de teller downloads van vóór de Marketplace meetelt. Herhaalmeting: `python3 data/ha-marketplace-meet.py` rond 8 dec laat zien hoe hard de tellers stijgen nu elke installatie de winkel ziet. Dat is nuttig als maat voor bereik, mocht Dortus ooit een gratis trechter willen.

## Advies
Nee (2). Hard groeiend platform, maar geen jonge winkel en een uitgesproken nee op betalen. Komt alleen terug als Home Assistant die belofte intrekt, wat ik niet verwacht.
