# Samen spelen in de demo van Hats of the Fallen (Sanne, versie 1, 16 nov 2026)

Opdracht: `platformen/steam/fest-plan.md` punt 1 en `berichten/sanne.md` (16 nov 12:25). Drie opties die passen bij onze haak (de hoeden op Gloop, helden met een wrok), zonder eigen server. Olaf toetst de haalbaarheid (vraag staat in `berichten/olaf.md`). Thijs kiest na de speeltest van za 21 nov.

## Waarom dit moet (kort)
- Deskrawl gaf demospelers een ranglijst, een gezamenlijke baas ("about 4000 players") en bèta voor de top 100, met "invite your friends": 3.631 reviews. Minimon in hetzelfde Next Fest gaf patches en wiste de voortgang: 7 reviews (Fenna verhaal 2 en 8, DERDEN).
- Desktop Defender zette doelen op gelijktijdige spelers (100, 200, 400, 1.000), met bij elk doel extra levels en een aankondiging op Steam; piek 1.548 spelers en "most played demos" (Fenna verhaal 5, DERDEN).
- Les: spelers moeten een reden hebben om te blijven en om anderen te halen. Bij een bureaubladspel komt daar iets bij: wie het spel aan laat staan, telt mee als speler (GOK uit verhaal 5). Een samen-functie die beloont dat het spel open staat, helpt dus twee keer.

## Toets voor elke optie
T1 tussendoor (een blik van 30 seconden is genoeg), T2 grappig om te onderhouden, T3 niet tijdrovend en niets missen als je weg bent (geen "kom nu terug of je mist het"), T4 eerlijk (niets te koop, geen loterij). Plus drie eisen uit het fest-plan: zonder eigen server, nooit voortgang wissen, en het moet tijdens het fest iets te melden geven.

## Wat Steam ons gratis geeft (GEZIEN in de Steamworks-docs, 16 nov, met curl)
- **Opgetelde stats** (partner.steamgames.com/doc/features/achievements, "Global Stats"): een stat met vinkje "Aggregated" telt Steam op over alle spelers. Het spel leest het totaal met `RequestGlobalStats` en `GetGlobalStat`, ook de groei per dag (`GetGlobalStatHistory`). Valsspelen afremmen kan met min, max, "increment only" en "max change" (hoeveel één upload het totaal mag laten stijgen).
- **Ranglijsten** (partner.steamgames.com/doc/features/leaderboards): tot 10.000 per spel, geen grens op het aantal spelers, een score is meteen terug te lezen. Een lijst kan op "Friends" (het spel leest alleen vrienden) en op "Trusted" (alleen een server mag schrijven; dat willen wij niet). Bij een score kun je een klein bestand hangen (`AttachLeaderboardUGC`) en, volgens de API, een rijtje getallen ("details").
- **Demo is een eigen app** (partner.steamgames.com/doc/store/application/demos): "Demos are a separate App ID". Stats en ranglijsten van de demo staan dus los van het volle spel. De docs raden prestaties in de demo af en geven die liever in het volle spel na de koop.
- **GodotSteam** (godotsteam.com/classes/user_stats, GEZIEN) heeft deze functies voor Godot: `requestGlobalStats`, `getGlobalStatInt`, `getGlobalStatIntHistory`, `uploadLeaderboardScore`, `downloadLeaderboardEntries`, `attachLeaderboardUGC`.
- **Lezen zonder spel:** de openbare Web API `api.steampowered.com/ISteamUserStats/GetGlobalStatsForGame/v1/` antwoordde zonder sleutel (getest op app 440, GEZIEN). Een getal van de demo kunnen we dus ook op dortus.com of in een aankondiging zetten. Of dat zonder sleutel ook voor onze app werkt, weten we pas als de demo-app bestaat (GOK).
- Nog niet in de build: Steamworks zit nog niet in het spel (geen GodotSteam in `producten/steam-hol/godot/`, GEZIEN met grep). Elke optie hieronder kost dus eerst die koppeling (zie "Wat elke optie eerst nodig heeft").

## Rekensom: hoeveel hoeden komen er samen? (GOK, om de doelen op te zetten)
- Gloop eet ±27 helden per uur open tijd (Bram, `sim/UITKOMST.md`, sim 9 nov; het spel kan inmiddels iets anders zijn). Na het demo-einde (2 uur) lopen helden en Gloop gewoon door (`kern/demo_einde.gd`, GEZIEN), dus een demo die aan staat blijft hoeden opleveren.
- Klein fest: gemiddeld 20 spelers tegelijk, 5 dagen = 2.400 speeluren = **±65.000 hoeden**.
- Goed fest: gemiddeld 200 tegelijk = 24.000 uur = **±650.000 hoeden**.
- Doorbraak zoals Desktop Defender (280.000 uur in zijn fest, DERDEN) = **±7,5 miljoen hoeden**.

---

## Optie A: De Grote Hoedenberg (alle Glooppen samen)
**Wat de speler ziet.** Achter in het hol, naast de schatkist, staat een klein bordje van hout met een getal dat langzaam oploopt: "All Gloops: 41,203 hats". Elke hoed die jouw Gloop opeet telt mee. Klik op het bordje en er klapt één regel open: "Next: 50,000. Then every Gloop gets the Tin Crown." Bij elk doel komt er voor iedereen in de demo een nieuwe hoed bij die helden kunnen dragen (dus Gloop kan hem winnen), met een regel in de kroniek: "The world's Gloops ate 50,000 hats. A hero in a tin crown is on his way." Doelen bijvoorbeeld 10.000, 50.000, 250.000, 1.000.000; de laatste is een verrassing (zoals bij Desktop Defender).

**Waarom hij het deelt.** Het doel komt sneller als er meer mensen spelen, en het spel aan laten staan helpt al. Elk doel is een aankondiging op Steam en een clip voor TikTok ("we hit 250,000 hats, here's the Wizard Hat raining down"). Het getal is ook iets voor een maker of streamer: "chat, zet de demo aan, we halen de miljoen".

**Bouw.** Klein. Eén opgetelde stat `hoeden_samen` (increment only, max change per upload bijvoorbeeld 200), ophogen bij elke hap (de plek is er al: hoed naar de toren), elke 10 minuten uploaden en het totaal lezen. De beloningshoeden komen vooraf in de build (3 nieuwe hoeden, zie "Beeld dat erbij hoort") en gaan open als het totaal boven het doel staat (één `if`); geen update nodig tijdens het fest, wel een aankondiging per doel. Het bordje is één klein 3D-stuk plus tekst (Mila en Daan). Schatting Olaf nog vragen; mijn gok 2 tot 3 dagen bouw na de Steam-koppeling.

**Risico.**
- Bij weinig spelers ziet een klein getal er zielig uit ("All Gloops: 312 hats"). Oplossing: het bordje toont pas iets vanaf 5.000 en de eerste doelen liggen laag (rekensom hierboven).
- Hoe snel Steam het totaal bijwerkt staat niet in de docs (GOK: niet per seconde). Moet getest worden zodra de demo-app er is; bij een trage telling toont het bordje "about".
- Valsspelen kan het getal opblazen. Max change dempt het, en de beloning is alleen een hoed; erg is het niet.
- Demo en vol spel tellen apart (eigen app-ID). In het volle spel kan het bordje het eindgetal van de demo als begin nemen.
- T3: een hoed die je "mist" bestaat niet: wie later begint krijgt alle behaalde hoeden ook, en ze gaan mee naar het volle spel. Niets verloopt.

**Toets:** T1 ja (één blik op het bordje), T2 ja (hoeden zijn de haak), T3 ja, T4 ja.

## Optie B: Wrok over de grens (helden uit het hol van een vriend)
**Wat de speler ziet.** Een held die uit het hol van een Steam-vriend vlucht, kan bij jou langskomen, met zijn wrok en zijn hoed. Boven zijn hoofd staat niet "Odo" maar "Odo, fled from Mara's Gloop". De kroniek: "Sir Odo escaped Mara's Gloop last night. He came here to recover. Bad choice." Eet jouw Gloop hem op, dan draagt Gloop de hoed die Mara net misliep, en Mara ziet bij haar volgende bezoek: "Your Sir Odo was eaten by Thijs's Gloop. He kept the hat." Zonder vrienden met het spel komen er ook geen vrienden-helden; het spel is dan precies hetzelfde als nu.

**Waarom hij het deelt.** "Invite your friends" krijgt een echte reden: hoe meer vrienden het spelen, hoe meer helden met een verhaal er langskomen, en je kunt elkaars helden opeten. Het is ook het soort moment dat mensen screenshotten ("mijn Gloop at de held van mijn broer").

**Bouw.** Middel. Een ranglijst `vluchters` op "Friends": elke speler zet er een score op (aantal gevluchte helden) met in de details de laatste gevluchte held (naam-nummer, soort, hoed, wrok). Jouw spel haalt elke 30 minuten de lijst van vrienden op, kiest er af en toe één en laat die held binnenkomen via de gewone wachtrij. De vriendennaam komt van Steam zelf (`GetFriendPersonaName`). Plus kroniekregels voor beide kanten. Schatting: mijn gok een week na de Steam-koppeling, omdat binnenkomst, kroniek en save er allemaal iets bij krijgen.

**Risico.**
- **Koude start:** in het fest heeft bijna niemand vrienden die de demo ook spelen. Dan merkt de grote meerderheid er niets van. Dat is het grootste bezwaar voor januari.
- Alleen vrienden, nooit vreemden: namen van onbekende spelers in je spel zetten vraagt om ellende (rare namen, privacy). Alleen "Friends" lezen houdt het netjes.
- Het "terugmelden" naar Mara kan alleen als haar spel weer kijkt; zonder server is het altijd met vertraging.
- Meer randgevallen (vriend speelt een oudere versie, held van een vriend die zelf nog niet bestaat in jouw soortenlijst).

**Toets:** T1 ja, T2 sterk (de wrok wordt persoonlijk), T3 ja, T4 ja. Maar in het fest bereikt hij weinig spelers.

## Optie C: De Reuzenheld (één baas voor alle holen, tijdens het fest)
**Wat de speler ziet.** Op de eerste dag van het fest (14 jan) staat er een reus in de kroniek: "Sir Ponderous the Enormous is visiting every hole in the world. He has 500,000 HP." Bij elke speler komt hij af en toe binnen, te groot voor de gang (alleen zijn laars en zijn hoed passen erin, dat is de grap). Gloop neemt een hap, de reus loopt boos door naar het volgende hol. Het bordje toont zijn leven: "Sir Ponderous: 312,400 HP left". Valt hij, dan krijgt elke speler zijn reuzenhoed (een hoed waar Gloop onder verdwijnt), voor altijd, ook in het volle spel, en Steam krijgt een aankondiging. Wie de demo na het fest start, krijgt de hoed ook, met de regel "The world beat him in January."

**Waarom hij het deelt.** Een duidelijk gezamenlijk doel met een einde in het fest, dus een moment om over te praten. Precies wat Deskrawl deed (±4.000 spelers versloegen de baas). Een streamer kan zijn kijkers laten meehelpen.

**Bouw.** Middel. Techniek gelijk aan optie A (één opgetelde stat `reus_happen`, plus een start op datum). Het werk zit in de reus zelf: een groot 3D-figuur dat niet in de gang past, zijn laars, zijn hoed en een paar regels (Daan, Mila, Bram). Moet getest worden met een nep-datum. Mijn gok 3 tot 4 dagen na de Steam-koppeling, waarvan de helft beeld.

**Risico.**
- Valt hij niet in 5 dagen, dan is het een mislukking voor iedereen te zien. Het leven moet dus laag genoeg (bij de kleine schatting van ±65.000 happen: leven 40.000), en er moet een vangnet zijn (na het fest valt hij altijd, "with one last bite").
- Een evenement op datum is iets dat je kunt missen; dat botst met T3. Daarom krijgt iedereen de hoed, ook wie later komt.
- Geen ranglijst "wie hapte het meest": dat nodigt uit tot valsspelen en tot het spel vol open houden voor een plekje, en de top 100 een bèta geven vraagt sleutels per speler (stap voor Thijs). Kan later.
- Eén keer gebruikt. Na het fest is het weg, behalve de hoed.

**Toets:** T1 ja, T2 ja (een reus die niet past is grappig), T3 ja met het vangnet, T4 ja.

---

## Mijn advies (Thijs kiest na 21 nov)
**A als vaste basis, C als het fest-moment bovenop A, B later (versie 1 of na de lancering).**
- A en C gebruiken dezelfde techniek (één opgetelde stat en een bordje), dus samen kosten ze weinig meer dan A alleen. A blijft altijd, C geeft het fest een verhaal met een einde en een aankondiging.
- B is het grappigst op de lange duur, maar in januari heeft bijna niemand vrienden met de demo. Na de lancering, als er kopers zijn, is B de beste reden om een vriend het spel te laten kopen.
- Variant als Olaf weinig tijd heeft: alleen A, met de doelen ook op gelijktijdige spelers (zoals Desktop Defender), want dat getal bepaalt de lijst "most played demos". Het spel kan dat lezen met `GetNumberOfCurrentPlayers`.

## Kroniekregels (Engels, gemeten: allemaal 42 tekens of minder, de grens uit `kroniek-regels.md`)
De voorbeeldzinnen in de opties hierboven zijn uitleg; dit zijn de regels die in het spel passen. Getallen gemeten met de langste vorm (bijvoorbeeld "312,400").

| Optie | Moment | Regel | Tekens |
|---|---|---|---|
| A | bordje | `All Gloops: 41,203 hats` | 23 |
| A | klik op bordje | `Next: 50,000. Then: the Tin Crown.` | 34 |
| A | doel gehaald | `Gloops everywhere ate 50,000 hats!` | 34 |
| A | regel erna | `A hero in a tin crown is on his way.` | 36 |
| A | eerste start na doelen | `The world earned you 3 hats. Wear them.` | 39 |
| B | vriendenheld komt binnen | `Odo fled Mara's Gloop. Bad choice.` | 34 |
| B | Gloop eet hem | `Gloop ate Mara's Odo. Kept the crown.` | 37 |
| B | bij de vriend daarna | `Your Odo met Thijs's Gloop. Gone.` | 33 |
| C | begin fest | `A giant is visiting every hole.` | 31 |
| C | reus komt binnen | `Sir Ponderous. Only his boot fits.` | 34 |
| C | hap | `Gloop bit the giant's toe. +1 for all` | 37 |
| C | bordje | `Giant: 312,400 HP left` | 22 |
| C | reus valt | `The world's Gloops felled the giant!` | 36 |
| C | start na het fest | `The world beat him in January.` | 30 |
| C | vangnet na het fest | `The giant fell. With one last bite.` | 35 |

Let op bij B: Steam-namen zijn tot 32 tekens lang. Vriendennamen afkappen op 8 tekens (`Mara`, `Thijs`, `xXGloo…`), anders past de regel niet. Alle regels gaan via de vertaaltabel (besluit hoofdchat 16 nov, alle tekst in één tabel).

## Beeld dat erbij hoort (voor Mila en Daan, pas na de keuze)
- A: het bordje (klein houten bord, getal leesbaar op 120 px) en **3 nieuwe hoeden** voor de doelen; nu zijn er 10 (`slijm.gd`, `HOED_SOORTEN`). Voorstel: Tin Crown, Wizard Hat (de grote paarse met sterren), en een verrassing voor de laatste.
- C: de reus (alleen laars en hoed zichtbaar in de gang, dat scheelt een heel figuur) en zijn reuzenhoed waar Gloop onder verdwijnt.
- B: niets nieuws, de gewone helden met een naambordje.

## Wat elke optie eerst nodig heeft (vraag aan Olaf, en stappen voor Thijs zodra er een keuze is)
1. **Steamworks in de build:** GodotSteam (GDExtension) in `producten/steam-hol/godot/`, met een nette terugval: zonder Steam (de Windows-toets op GitHub Actions, of offline) verdwijnt het bordje en werkt de rest zoals nu. Vraag aan Olaf: hoeveel werk, en past het vóór de demo van vr 18 dec?
2. **Demo-app-ID** in Steamworks en de stat (en eventueel de ranglijst) instellen op de beheerpagina. Dat is inloggen, dus een stap voor Thijs. Ik zet die stap pas op `organisatie/lijst-thijs.md` als Thijs gekozen heeft, met precies de velden (naam, Aggregated aan, increment only, max change).
3. **Save:** het bordje en de behaalde doelen gaan in de save en blijven altijd geldig (fest-plan punt 7, nooit wissen).

## Open
- Haalbaarheid en bouwtijd per optie: Olaf (gevraagd 16 nov).
- Hoe snel Steam een opgeteld totaal bijwerkt: testen zodra de demo-app er is.
- Bij de speeltest van 21 nov kijken of spelers het hol na een paar minuten nog open laten staan; zo niet, dan helpt geen enkele samen-functie en gaat de kern voor.
