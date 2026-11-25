# Broncode: KeeperRL (Steam, kerker-simulator)

Uitgeplozen door de Afkijker op 25 nov 2026, voor issue #20. Code gelezen met `git clone --depth 1` van https://github.com/miki151/keeperrl (laatste commit 27 okt 2025), alleen gelezen, niets uitgevoerd. Steam-pagina's met curl.

## Waarom dit project
- Het spel dat het dichtst bij Hats ligt: jij bent de kwaaie, je bouwt een kerker en **helden en dorpen komen je aanvallen, met een reden**. Hats: een hol vol vallen met helden die terugkomen met wrok.
- **1.693 Steam-reviews, 83% positief ("Very Positive")** (GEZIEN, https://store.steampowered.com/app/329970/, 25 nov 2026). Prijs 16,79 euro, nu 8,39 euro (50% korting), volledig uit sinds 29 feb 2024, Early Access sinds 2015 (GEZIEN, Steam appdetails-API).
- Eén maker (Michał Brzozowski), ±83.000 regels C++.
- Licentie: code **GPL-2.0** (GEZIEN, `COPYING.txt`), beelden in `data` alleen voor hun eigen spel, `data_free` CC BY-SA (`COPYING-MEDIA.txt`). Hats is gesloten: **geen regel code of data overnemen, alleen ideeën.**

## Wat ze slim doen (bestand en regels)
1. **Elke aanval heeft een reden die de speler ziet.** Per vijandelijke groep staat in een lijst "Triggered by: Killed tribe members, Item theft", gesorteerd van sterk naar zwak, en hoe roder het woord, hoe groter de kans op een aanval. Code: `player_control.cpp` r. 950 tot 990 (`getTriggerLabel`: "Your evil", "Killed tribe members", "Item theft", "Breach of territory"), r. 995 tot 1040 (`getVillageInfo`), `gui_builder.cpp` r. 850 tot 852 (`getTriggerColor`: wit naar rood met de kans), r. 897 tot 916 (de regel "Triggered by:"), r. 1068 tot 1075 (in de zijbalk: rood "attacking", oranje "triggered"). Teksten in `data_free/game_config/translations/english.txt` r. 461, 685, 741, 883.
2. **Wat jij doet, bepaalt wie komt.** Elke groep heeft eigen redenen in `data_free/game_config/enemies.txt`: dorpelingen komen als je er een doodde (r. 115 `SelfVictims`), bandieten komen af op je goud vanaf 500 (r. 254 `Resource "GOLD" 500`) en willen het stelen, ridders komen af op je troon en gespietste hoofden (r. 397 tot 401). De kansen per reden: `village_behaviour.cpp` r. 169 tot 239 (bijvoorbeeld diefstal 1 op 300 per beurt, gewoon sterk zijn maar 1 op 10.000: "rather small chance that they attack just because you are strong", r. 175).
3. **De wrok begint met één zin, direct.** Steel je iets van een dorp, dan krijg je meteen "You are going to regret this." en telt het dorp mee (`village_control.cpp` r. 119 tot 153). Elke dode van hun stam telt 1, van een ander dorp van dezelfde stam 0,15 (r. 83 tot 92).
4. **Aftellen voor de volgende golf.** In de modus met golven staat er "Attacking in 40 turns!" met de naam van wie komt (`gui_builder.cpp` r. 949 tot 956, `player_control.cpp` r. 2083 tot 2094). De speler kan zich voorbereiden: dat is baas zijn.
5. **Aanvallen alleen als de speler erbij is.** Geen aanval als je met je leger elders bent, en ondoden worden niet overdag aangevallen (`village_control.cpp` r. 346 tot 358, `canPerformAttack`).
6. **Helden geven het op en vluchten.** Is de helft van de aanvallers gevallen, of staat er nog één zwaargewonde, dan keren ze om, en de speler krijgt "Resisting the attack of ..." in zijn verhaal (`village_control.cpp` r. 310 tot 329, `considerCancellingAttack`).
7. **Losgeld als keuze.** Bandieten eisen een deel van je goud (`ransom = 0.5 80`: 30 tot 50% van je goud, minstens 80); betaal je, dan gaan ze weg (`village_control.cpp` r. 194 tot 198 en `onRansomPaid` r. 331 tot 338). Een keuze, geen straf.
8. **Hinderlaag:** onderweg kunnen vijanden je op 3 vakjes afstand omsingelen, net buiten zicht (`village_control.cpp` r. 219 tot 282).

## Wat spelers zeggen (Steam, GEZIEN 25 nov 2026, top-reviews op https://steamcommunity.com/app/329970/negativereviews/ en /positivereviews/)
**Klachten:**
- "I spend a lot of time just waiting around for recruits and for my minions to dig ... you will easily spend over an hours worth of time doing absolutely nothing but watching your screen" (7 mrt 2024).
- "Like the game doesn't know what it wants to be ... the actual gameplay is shorter than you would imagine" (29 jul 2022).
- "Multiple factions that play 90% the same" (27 dec 2024) en "a strangely linear game ... a series of samey encounters" (13 mei 2024).
- "My minions simply would not reliably collect them" (7 jul 2025): poppetjes die niet doen wat je verwacht, kosten het gevoel van controle.
- Moeilijkheid springt: "a band of demons ... one shot my entire army effortlessly" (23 jul 2025).
- "Very cluttered on the one side, at the same time not enough to do" (7 aug 2025).
**Lof:**
- Verhalen die vanzelf ontstaan: "Suddenly I got a message: my lair is under attack. Knights and archers were entering my dungeon" (12 apr 2015).
- "Dwarf Fortress for sane people" (23 sep 2015): de diepte zonder de moeite.
- De maker antwoordt snel: "It was fixed in less than a day" (24 mrt 2022); "the lone dev is extremely responsive" (29 feb 2024).
- Mods via de Workshop houden spelers jaren vast ("without mods, I doubt I would play this", 14 jan 2021).

## Wat Dortus ervan leert
**Product: Hats of the Fallen** (`producten/steam-hol/godot/`).

Hats heeft de wrok al rijk uitgewerkt in tekst (`systemen/kroniek_regels.gd` r. 16 tot 92, `systemen/boek.gd` aartsvijanden), maar de speler ziet hem pas als de held er al is. Wie wanneer komt, beslist de klok (`kern/ritme.gd` r. 12 en 16) en het toeval (`kern/binnenkomst.gd` r. 30 tot 40: 25% terugkomer). Er is geen vooruitblik (GEZIEN: geen "next hero" of aftellen in `kern/`). KeeperRL laat zien dat "baas zijn" komt uit **oorzaak zien vóór het gevolg**: wie komt, waarom, en wanneer.

1. **Beste idee (issue bij Sanne): de deur.** Een klein vak aan de rand van de strook met de volgende held: zijn hoed, naam en één woord waarom ("for Gloop", "your gold", "revenge"), en een balkje dat vol loopt tot hij binnenkomt. Dicht gat 5 uit #19 en #26 (de speler is de baas, niet duidelijk wat er gebeurt) zonder nieuwe tekstregels in de kroniek.
2. **Laat de speler de oorzaak zijn:** een grote schat lokt hebzuchtige helden (KeeperRL r. 254), een gevluchte held komt terug voor wie hem pijn deed (dat hebben we). Dan voelt een held als gevolg van jouw keuze, niet als toeval.
3. **Eén zin op het moment van de wrok** ("You'll regret this." als een held vlucht) en pas daarna de terugkomst: de kroniek doet dit al deels ("Swore revenge."); houd het bij één zin.
4. **Klachten vermijden:** niet een uur niets te doen (rustpauzes kort en met iets om naar te kijken), helden doen altijd zichtbaar wat ze zeggen (sluit aan op #25: een val doet altijd iets), geen sprong in moeilijkheid.
5. **Later, na de lancering:** snel antwoorden op reviews en meldingen (hun sterkste lof); mods zijn voor Hats niet nodig.

Niets overgenomen. GitHub-issues van KeeperRL niet gelezen (buiten de repo's van deze taak).
