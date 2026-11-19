# Keuring projectendashboard, 19 nov 2026, keurder (losse Claude, niet de bouwer)
Wat ik keurde: `dashboard/bouw.py`, `dashboard/sjabloon.html`, `dashboard/ploeg.json`, `dashboard/beelden/`, `organisatie/projecten.json`, `organisatie/projecten-leesmij.md` op main 75d3b087, en de live pagina https://thijsduinhouwer2002-coder.github.io/dortus-hq/ (gebouwd do 19 nov 12:00, tak `dashboard` 11:00 UTC).
Akkoord: nee (drie moet-punten, alle drie klein: samen GOK een uur werk voor de hoofdchat en de bouwer)

Hoe ik keek: Playwright (Chrome) op 390x844 en 1440x900, licht en donker, alle 11 tabs (overzicht, ploeg, 9 projecten), bovenkant en hele pagina: 88 schermen, bekeken met de Read-tool. Geen fouten in de console (één 404, de favicon). Geen horizontaal scrollen op 390. Data naast de bronnen gelegd; `bouw.py` in een eigen worktree gedraaid met een aangepaste `projecten.json`; runs van `dashboard.yml` via de GitHub-API.

## Deel A: doet het wat beloofd is?
(toets tegen de opdracht: Thijs ziet elke dag hoe elk project loopt en kan snel bijsturen, en het moet er echt goed uitzien)

### A1. UI, gesorteerd op hoeveel het oplevert
| # | Bevinding | Feit of vermoeden | Zekerheid | Hoe beter |
|---|---|---|---|---|
| U1 | **Op 1440x900 zie je maar 1,5 project boven de vouw.** Elke rij is 140 tot 190 px hoog: drie regels grijze statuszin plus een blauw "Jij:"-blok dat letterlijk herhaalt wat in de strook "Jij moet doen" erboven staat (Roep, Reddit, Hats). De hele ranglijst is 1.060 px; op de telefoon is het overzicht 3.888 px lang. Het doel "in één blik hoe elk project loopt" haal je zo niet. | feit (scherm `lap-light-overzicht-top.png`, `tel-light-overzicht-full.png`) | hoog | Haal het "Jij:"-blok uit de rij en zet er een klein merkje "actie voor jou" naast de status. Kap de statuszin af op één regel (volledige zin op de projectpagina). Dan passen alle zeven Dortus-projecten op één laptopscherm. |
| U2 | **De geldlat is moeilijk te lezen en weegt verkeerd.** Log-as van €0 tot €20.000: het blauwe blok van €350 tot €800 is 30 px breed en lijkt klein; drie projecten met "€0 tot €80 samen" krijgen elk een volle stippellijn en zien er even zwaar uit als echte bedragen; Hats krijgt een hele lege lat voor €0. Het bedrag zweeft boven het blok en schuift per rij naar een andere plek, dus je ogen springen. De askop "€10.000" schuift tegen de kolom "Kans op geld" en loopt op de projectpagina over de rand van het vak (`lap-light-reddit-hat-tower-full.png`, rechts van "€10.000"). | feit | hoog | Zet het bedrag als vast getal links in de cel (altijd op dezelfde plek, vet), met een dunne lat eronder. Toon de lat alleen bij een eigen bedrag; bij €0 en bij "samen" alleen tekst ("€0", "€0 tot €80 voor drie samen"). Laat de laatste askop rechts uitlijnen in plaats van centreren. |
| U3 | **Te veel kleine labels, te weinig contrast.** Op het overzicht staan ±25 labels GOK van 9,5 px, ook achter tekst zonder getal ("nog geen schatting GOK", "middel GOK"). Grijs `--zacht` (#8a93a3) op wit is 3,1:1 en op de tabelkop 2,96:1 (norm 4,5:1) en wordt gebruikt voor kolomkoppen, groepsnamen in het menu, "geen" bij deadlines en de commit-hashes. Het pilletje "geparkeerd" is 3,3:1. | feit (gemeten met de WCAG-formule) | hoog | Label alleen bij een getal; maak het label 10,5 tot 11 px en rustiger (geen rand, alleen kleur). Of één regel per sectie "alle bedragen en kansen hier: GOK uit de keuring snel-geld" en een label alleen waar het afwijkt. `--zacht` naar ±#6b7485 (licht). |
| U4 | **Eerstvolgende deadlines begint met de meetprojecten van Thijs zelf** (Scanner vr 20 nov, Schaduwbot za 21 nov) tussen de geld-deadlines, terwijl het overzicht ze verder netjes apart zet. De Reddit-inzending (wo 9 dec, het grootste geld) valt buiten de vier die je ziet. | feit | hoog | Alleen Dortus-projecten in de strook, of meetprojecten grijs en onderaan. Toon er 5, of altijd de deadline van het project met het meeste geld. |
| U5 | **De pagina ziet er net en verzorgd uit, maar niet als iets eigens.** system-ui, één blauw accent, overal dezelfde witte kaart met 10 px hoek en zachte schaduw: het standaard SaaS-pakket (punt 4 in `frontend-design`). Niets is lelijk; het is degelijk, maar Thijs vroeg "echt goed". | vermoeden (smaak) | midden | Eén ding opvallend maken en de rest stil laten: het getal "verwacht in 12 weken" groot als kop van de pagina, met daaronder per project een strakke rij. Een eigen letter voor koppen en cijfers (bijvoorbeeld een smalle grotesk met tabelcijfers) geeft het meteen een eigen gezicht. Geen extra kaarten of verlopen. |
| U6 | **Ploeg-tab: de 18 agents die uit staan nemen 60% van de pagina in** (`lap-light-ploeg-full.png`). "Laatste runs" toont "groen" voor workflows die alleen de klok raadpleegden en niets deden (bijvoorbeeld "Scorebord (elke dag 06:41 UTC) groen, 4 min geleden" na een gewone push; `scorebord.yml` start bij elke push, `klok.py` slaat het werk over en de run heet dan toch success). Dat zegt Thijs dat iets draaide wat niet draaide. | feit | hoog | Uit-agents in één ingeklapte regel ("18 uit: Noor, Patrick, ..."). Bij runs alleen rood en overgeslagen tonen, of de laatste run waarin de werkjob echt draaide (de tak `klok` heeft die tijd per taak). |
| U7 | **"Laatste wijzigingen" op de projectpagina is vooral ruis.** Bij Hats zijn 4 van de 6 regels "logboek, niets te doen" of "run 09:15, niets te doen". | feit (`tel-dark-hats-full.png`) | hoog | Commits met "niets te doen" of alleen "logboek" overslaan in `bouw.py`. |
| U8 | **Teksten zijn voor agents geschreven, niet voor Thijs.** Statuszin Reddit noemt een commit-hash ("opgelost in ba1e1aee") en "moet-punten"; de keuringsregels tonen koppen als "Keuring snel-geld-onderzoek, ..., keurder (losse Claude, niet de maker)". | feit | hoog | In de leesmij: statuszin zonder hashes en vaktaal, in de woorden van een eigenaar ("Speelt lokaal, wacht op tweede keuring"). |
| U9 | **Telefoon: de pagina herlaadt elke 15 minuten** (`meta refresh 900`) en springt dan naar boven, ook midden in het lezen. Het menu is een rij van 11 pilletjes die je zijwaarts moet vegen zonder teken dat er meer is. | feit (code), vermoeden (hinder) | midden | Herladen alleen als het tabblad verborgen is, of een knop "nieuwe stand" tonen. Een zachte vervaging rechts aan het menu. |
| U10 | **Kleine fouten in de cijfertabel.** "verkoopklasse ? GEZIEN" (een vraagteken met het label gezien), "omzet USD 0.00" met een punt, waar de rest Nederlands is. Reddit Game of the Day toont als enig echt cijfer de downloads van de Garmin-versie (10); dat is een ander product. | feit (`lap-dark-click-joints-pro-full.png`, `lap-light-reddit-hat-tower-full.png`) | hoog | Onbekend = "niet gelezen" zonder label; bedragen met komma; Garmin-downloads weg bij Reddit (of als "basis: Garmin-versie" apart). |

Wat goed is: de strook bovenaan beantwoordt meteen de twee vragen van Thijs (wat moet ik doen, hoeveel komt er); status heeft kleur, vorm en woord samen; donker is goed uitgewerkt (geen zwart vlak, eigen kleuren, contrast in orde); telefoon breekt nergens; projectpagina's zijn rustig en volledig met bron-links bij elke schatting.

### A2. Data
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| D1 | Kansen en prognoses kloppen met de keuring snel-geld (`platformen/ideeen/snel-geld-2026-11-19/KEURING.md`): route 1 Reddit 10 tot 20%, €350 tot €800, uitkomst €0 / €860 / €5.200 / €12.900, deadline wo 9 dec 03:00 NL; route 2 Click Joints Pro middel, €50 tot €300; route 15 €0 tot €80 samen; route 16 Hats €0. Roep "nog geen schatting" past bij de keuring marketing-tak (moet 6: tientallen dollars). Optelsom €400 tot €1.100 = 350+50 tot 800+300. | feit | hoog | |
| D2 | Bij Reddit toont het dashboard 10 tot 20% groot, terwijl dezelfde keurder in A3 5 tot 12% eerlijker vindt. Het staat wel eerlijk in de reden. | feit | hoog | Na 9 dec: aantal ports in de galerij |
| D3 | **"Jij moet doen" klopt niet met de bronnen.** (a) De speeltest van za 21 nov doet Thijs zelf (`platformen/steam/speeltest-21-nov.md`, besluit 15 nov 19:25), maar staat niet bij "Jij moet doen"; het veld `thijs` heeft maar plek voor één punt per project, en bij Hats staat Insider Gaming. (b) Twee van de vier punten (Roep: twee geplande taken; Reddit: devvit login) staan niet op `organisatie/lijst-thijs.md`. Regel 6: alleen de hoofdchat zet iets op de lijst van Thijs. Zo heeft Thijs twee lijsten die uit elkaar kunnen lopen. De bouwer meldde (b) zelf aan de hoofdchat. | feit | hoog | Na de fix: elk punt in de strook staat ook op lijst-thijs, of is door de hoofdchat bevestigd |
| D4 | De datum "vóór vr 20 nov" bij de geplande taken van Roep vond ik in geen bron (`marketing/VOORSTEL-hoofdchat.md` noemt geen datum). | vermoeden | midden | Een bericht of besluit met die datum |
| D5 | De devvit login klopt met `organisatie/toegang.md` (account u/DortusGames gemaakt door Thijs, Devpost ingeschreven 19 nov 11:11). `stand.md` noemt nog ±15 min met drie stappen die al gedaan zijn; het dashboard (±5 min) is hier juister. | feit | hoog | |
| D6 | Gloop's Hat Tower (Garmin) krijgt "€0 tot €80 samen", maar het spel is gratis; in route 15 hoort "Garmin" vooral bij Ebb ($2,99, live, geparkeerd), dat helemaal niet als project op het dashboard staat. | vermoeden | midden | Keurder snel-geld vragen wat "Garmin" in route 15 omvat |
| D7 | Ploeg zegt "Roep aan" (uit `ploeg.json`, `actief: true`), maar het project Roep zegt "de twee geplande taken draaien nog niet" en de bouwer zag in `list_triggers` geen Roep-taken. Ook "10 aan" tegen 6 op het bord: Hoofdchat, Keurder, Roep en Reddit-bouwer komen uit `ploeg.json`, niet uit het bord. | feit | hoog | |
| D8 | Geen persoonsgegevens: geen mailadres, adres of nummer in de live pagina (gezocht op @, IBAN, cijferreeksen); `check.py` zegt OK. Meetprojecten van Thijs zelf staan er zonder bedragen. Elk getal in `projecten.json` heeft een label. | feit | hoog | |

### A3. Bijwerken
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| W1 | Een wijziging in `projecten.json` komt goed door: in een eigen worktree status, prognose en een punt voor Thijs bij Bison & Flex aangepast; `bouw.py` zet het project bovenaan, telt het totaal op en zet het punt in de strook. Het pad staat in `--paden`, dus zo'n push bouwt altijd. | feit | hoog | |
| W2 | **Niemand is opgedragen `projecten.json` bij te werken.** De leesmij zegt "de hoofdchat-ronde werkt het elk uur bij", maar `organisatie/hoofdchat-ronde.md` noemt `projecten.json` en het dashboard nergens. Zonder die stap staan status, deadlines en "Jij moet doen" morgen al verkeerd. | feit | hoog | Een stap in de ronde, en `bijgewerkt` die elke ronde verschuift |
| W3 | **Het overzicht toont alleen "Gebouwd do 19 nov 12:00", niet hoe oud de projectstand is.** Dat ziet er vers uit, ook als de ronde dagen overslaat. `projecten_bijgewerkt` zit wel in de data, maar het sjabloon toont het alleen onderaan elke projectpagina. | feit | hoog | |
| W4 | De workflow bouwt vanzelf: 30 van de laatste 30 runs zijn pushes (allemaal groen behalve e5bf1d3, de conflictstrepen, hersteld in 6f52c74). Het schema zelf vuurt maar ±elke 8 uur (laatste 07:50, 00:13, 17:56 UTC). Overdag komen er genoeg pushes; 's nachts kan de pagina tot ±8 uur oud zijn. De oranje melding na 120 minuten vangt dat op. | feit | hoog | |
| W5 | Een tikfout in `projecten.json` breekt de bouw: met `"verwacht": "veel"` stopt `bouw.py` met een TypeError; ongeldige JSON idem. De oude pagina blijft dan staan, zonder melding op de pagina zelf. | feit (geprobeerd) | hoog | |
| W6 | De leesmij is duidelijk: elk veld met voorbeeld, sorteerregel, wat de ronde elk uur doet. Mist: dat `thijs` maar één punt kan bevatten, en hoe de statuszin klinkt (zie U8). | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen persoonsgegevens, geen bedragen bij de meetprojecten van Thijs, controle OK. | feit | hoog | harde regel 2 |
| B2 | Elk getal in `projecten.json` heeft GEZIEN, DERDEN of GOK met reden en bron; cijfers uit het scorebord nemen het label van de bron over. Uitzondering: "?" krijgt GEZIEN (U10). | feit | hoog | harde regel 5 |
| B3 | Punten voor Thijs buiten `lijst-thijs.md` (D3b). | feit | hoog | harde regel 6 |
| B4 | `sjabloon.html` is 506 regels (norm ±400); CSS in een eigen bestand halveert het. Geen `architectuur.md` voor het dashboard. | feit | hoog | `regels/bouwen.md` |
| B5 | Er zijn geen tests voor `bouw.py`; een kleine schemacheck van `projecten.json` in de controle vóór elke push zou W5 vangen. | feit | hoog | werk is af als tests groen zijn |
| B6 | Nederlands, geen gedachtestreepjes in de teksten op de pagina. | feit | hoog | harde regel 8 |

## Moet (blokkeert akkoord)
1. **Bijwerken vastleggen (W2):** een stap in `organisatie/hoofdchat-ronde.md`: "werk `organisatie/projecten.json` bij volgens `organisatie/projecten-leesmij.md`". Hoofdchat, 5 minuten.
2. **Ouderdom van de stand tonen (W3):** bovenaan het overzicht "Stand projecten: <datum> door <wie>", oranje als die ouder is dan ±3 uur. Bouwer, 15 minuten.
3. **"Jij moet doen" gelijk aan de bronnen (D3):** de speeltest van za 21 nov erbij (het veld `thijs` een lijst maken, of de speeltest op lijst-thijs); de hoofdchat kiest voor Roep-taken en devvit login: op lijst-thijs (dan 4 van de 5) of weg uit `projecten.json`. Hoofdchat en bouwer, 30 minuten.

## Kan (mag later), op volgorde van opbrengst
1. U1 rijen korter, "Jij:"-blok weg uit de rij (grootste winst voor de blik van Thijs).
2. U2 geldlat: vast bedrag links, lat alleen bij een eigen bedrag, askop rechts uitlijnen.
3. U3 labels rustiger en alleen bij getallen; `--zacht` donkerder.
4. U4 deadlines alleen van Dortus, de Reddit-inzending zichtbaar.
5. U6 en U7: ploeg en wijzigingen zonder ruis, geen "groen" voor runs die niets deden.
6. U8 statuszinnen in gewone woorden (leesmij).
7. U10 en D6: "?" zonder label, komma in bedragen, Garmin-cijfer weg bij Reddit, Ebb opnemen of Garmin-schatting herzien.
8. W5 en B5: schemacheck van `projecten.json` vóór elke push.
9. U9 niet herladen tijdens het lezen; U5 eigen letter en één opvallend element.
10. D7 ploeg: aan of uit voor Roep en Reddit-bouwer uit het bord halen; B4 CSS apart en `architectuur.md`.

Schermen: gemaakt in /tmp tijdens de keuring (88 stuks, niet in de repo); de vier van de bouwer in `dashboard/beelden/` komen overeen met wat ik live zag.
