# Herweging: Overwolf Appstore

Kees, 9 nov 2026 run 17:22 UTC. Oud cijfer: 6 (Vera, `platformen/verkenner/voorstellen/overwolf.md`). Nagekeken door een controleur (akkoord op alle punten).

## Welke meting de doorslag zou geven
Het enige gat bij Vera was geld: wat brengt een app per gebruiker op. Bereik leek sterk, maar alleen als totaal over de hele levensduur van een app. Ik zocht dus twee dingen: (1) een openbaar bedrag per gebruiker, en (2) hoeveel nieuwe installs een kleine app nu per dag haalt, zodat je met (1) kunt uitrekenen of $300 per maand haalbaar is.

## Wat eruit kwam

### 1. Opbrengst per gebruiker: niet openbaar te meten
- NIET GEVONDEN: geen enkele kleine maker die omzet en gebruikers samen noemt. Reddit blokkeert ons, HN, Indie Hackers en het Overwolf-blog hebben niets. Geen eCPM of rekentool op overwolf.com.
- DERDEN, bovengrens: Porofessor (één maker, beste app van het platform): €12,3 mln omzet per jaar bij 1,25 mln DAU (app plus website), dus ±$890 per 1.000 DAU per maand (https://techcrunch.com/2023/06/15/wargraphs-a-gaming-startup-with-only-one-employee-and-no-outside-funding-sells-for-54m/).
- DERDEN, hele platform: $300 mln+ uitbetaald in 2025 bij 113 mln MAU, ±$220 per 1.000 MAU per maand, maar inclusief mods en Tebex-servers (https://gamesbeat.com/overwolf-paid-out-300m-to-creators-so-far-this-year/).
- DERDEN: het dashboard van de maker toont ARPDAU, CPM en een gemiddelde van vergelijkbare apps (https://dev.overwolf.com/ow-native/developers-console/monetize/revenue-stats/). Het echte getal zie je dus pas met een eigen app.
- GOK: $100 tot $900 per 1.000 DAU per maand. Dan vraagt $300 per maand ergens tussen ±350 en ±3.000 dagelijkse gebruikers.

### 2. Nieuwe downloads per dag: GEZIEN
Alle 232 app-pagina's van Vera (8 nov ±01:30 UTC) opnieuw opgehaald op 9 nov ±17:30 UTC (40 uur). Data: `data/overwolf-apps-2026-11-09-1730.jsonl`, script `data/overwolf-vergelijk-script.py`.
- Kleinere apps (onder 60.000 downloads op 8 nov, n=134): mediaan **3,3 downloads per dag**. 45 halen 10+ per dag (34%), 21 halen 30+ (16%), 12 halen 100+ (9%), 3 halen 300+.
- De uitschieters zijn apps voor een verse lancering: World of Warcraft: Forever (live 4 nov 2026). WoW Forever Map (RA Studio) ±1.200 per dag, WoW Forever Companion (ConvexApps) ±1.050 per dag. Beide zijn seriemakers (RA Studio ook Minecraft Companion en Phantom Blade-kaart, ConvexApps ook Facecheck met 3,2 mln).
- Apps van kleine makers bij oudere games van 2025 en 2026 lopen nu bijna stil: ArcTerminal 3 per dag, ARC Forge 0,6, Echoclip 1,8, Deadlock Signal 35, Killer Vibe 0.
- Controleur: tien tellers live nagehaald, gelijk aan mijn meting; herberekening gelijk (45, 21, 12, mediaan 3,3). Gevoelig voor de tussentijd: bij 38 uur 46, 22, 13.

### Wat dat samen zegt
- Bereik voor nieuwkomers (punt 2) bestaat, maar alleen in een smal venster: de eerste dagen na een grote lancering. Daarna zakt een kleine app naar enkele downloads per dag. Wie dat venster pakt, zijn vooral seriemakers die er al klaar voor staan (zoals Vera ook zag in `kansen/overwolf-games-zonder-app.md`).
- Rekenvoorbeeld (GOK): een app met 100 nieuwe downloads per dag en 20% die blijft, heeft na een maand ±600 DAU. Dat is $60 tot $540 per maand. Bij 30 per dag $20 tot $160. Alleen 9% van de kleinere apps haalt die 100 per dag nu.
- Punt 1 (kleine makers verdienen nu) is daarmee niet bewezen en niet van buiten te bewijzen. De meting die de doorslag geeft is het dashboard van een eigen app.

## Nieuw cijfer: 6 (blijft, valt af voor een 8)
Waarom geen 7: punt 1 niet GEZIEN, punt 3 schuurt (de Overwolf-client draait op Windows met een ontwikkelaarsaccount, testen in de echte app op Actions is onzeker, en wij kennen de games alleen uit wiki's), punt 4 schuurt (eerst een voorstel indienen en wachten op goedkeuring, duur onbekend). Waarom geen 5: bereik bij een lancering is echt en meetbaar groot (1.000+ per dag voor een verse kaart-app), en het geld zit ingebouwd.

## Wat er nog schuurt en wat het zou veranderen
- Naar 7: een kleine maker die omzet en DAU noemt met minstens ±$0,30 per DAU per maand, of een eigen app met dashboard.
- Naar 5 of lager: bij de volgende grote lancering pakken weer alleen seriemakers het venster (Vera volgt dat al, taken.md 9 nov 09:31).
- Herhaalmeting: zelfde script rond 9 dec. Dan is te zien hoe snel WoW Forever-apps terugzakken.
