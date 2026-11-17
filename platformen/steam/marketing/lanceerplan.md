# Lanceerplan Hats of the Fallen (Sem, begonnen 17 nov 2026, run 14)

Eén plek voor wat rond het uitbrengen in maart gebeurt. De details staan in de bestanden waar naar verwezen wordt; hier staat de volgorde en de reden. Alle spelerstekst is CONCEPT in `platformen/steam/teksten-thijs.md` tot Thijs hem schrijft.

## Datum
Voorstel uitbrengen **di 2 tot do 4 mrt 2027** (Vera, Olaf eens, `platformen/steam/planning-fest-2027.md`). Next Fest loopt tot ma 1 mrt (Steamworks `doc/marketing/upcoming_events`, GEZIEN 17 nov). Bao Bao en Bongo Cat brachten 2 tot 3 dagen na Next Fest uit (Fenna verhaal 1).

## Korting en de verlanglijstmails (run 14, voorstel Fenna verhaal 20, nagekeken)
Regels van Valve, GEZIEN 17 nov met curl:
- `doc/marketing/wishlist`: "When your game releases or goes on discount, those players automatically receive a notification." Een kortingsmail gaat alleen bij "Any type of discount at or above 20%", die minstens het goedkoopste pakket raakt en langer dan 8 uur duurt.
- `doc/marketing/discounts`: lanceerkorting 7 tot 14 dagen, Valve raadt "around 10% to 15%" aan, hooguit 40%. Daarna **"A product cannot be discounted for 30 days following its release"** en een korting niet binnen 30 dagen na een andere (seizoensuitverkopen uitgezonderd, maar niet tijdens de 30 dagen na de uitgave).
- Data 2027 (`doc/marketing/upcoming_events`): Spring Sale 18 tot 25 mrt, Summer Sale 24 jun tot 8 jul.

Wat dat voor ons betekent:
1. **Lanceerkorting 15%** (Vera, en 88% van de nieuwe bureaubladspellen, Fenna verhaal 20). Onder de 20%, dus geen aparte kortingsmail; de uitgavemail gaat sowieso. Zo bewaren we de kortingsmail voor later.
2. **De Spring Sale (18 tot 25 mrt) kan niet**: die valt binnen 30 dagen na 2 mrt. Niet op rekenen.
3. **Eerste korting van 20 tot 25% samen met de eerste grote gratis update**, zoals Deskrawl (30% op 13 nov, de dag na een grote update, Fenna verhaal 20; huidige korting 30% GEZIEN in de winkel-API 17 nov). Vroegst ±do 1 apr (30 dagen na de uitgave). **Besluit Sem: niet per se wachten op de Summer Sale.** Komt de update in april of mei, dan een eigen korting op die dag; is er vóór juni geen update, dan de Summer Sale (24 jun) met de update. Waarom: een eigen korting is de enige mail in de inbox van die dag, in een seizoensuitverkoop concurreert hij met duizenden en kan hij later gaan (GOK op het effect, de regel over later gaan staat in Fenna verhaal 17). Fenna stelde de Summer Sale voor; dat blijft de terugval.
4. In het uitgavebericht prijs, korting en einddatum in één zin (A10 in `teksten-thijs.md`).

**Bijgesteld in run 15 (17 nov ±01:45 UTC), na Fenna verhaal 21.** Punt 3 hierboven klopt niet meer. Fenna mat 24 bureaubladspellen met een aangekondigde eerste korting van 20%+ (`platformen/succes/data/eerste-korting-na-lancering-2026-11-17.csv`, zelf nagerekend): reviews per week in de kortingsweken tegen de 3 weken ervoor.
| Soort korting | Aantal | Mediaan sprong | Let op |
|---|---|---|---|
| eigen korting (vaak met update) | 6 | 0,96x | Your Mother 1,36, Tiny Pasture 0,92, Desktop Defender 0,96 |
| gewone seizoensuitverkoop | 11 | 1,5x | maar bij de 5 met minstens 5 reviews per week vooraf: 0,94x; de hoge sprongen zitten bij spellen met 0,3 tot 2 reviews per week (ruis) |
| themafest of Daily Deal (etalage) | 4 | 3,6x | Fish to Dish 3,9 (Daily Deal, kies je niet zelf), Zen Aquarium 3,75 (Animal Fest), Chonkers 3,5 (Idler Fest), Bao Bao 1,7 (Minimal & Chill) |
Controle zonder korting 0,7x. Eerlijk: 4 etalagegevallen is weinig, en een Daily Deal kiest Valve, dus GOK hoe groot het voor ons is; maar in alle vier was het meer dan bij elke eigen korting. Een update erbij maakte de eigen korting niet groter (Your Mother en Desktop Defender deden het allebei, 1,36x en 0,96x).

**Besluit Sem (vervangt punt 3):** de eerste korting van 20 tot 25% gaat naar **het eerste themafest waar Hats echt in past** (Valve-lijst `doc/marketing/upcoming_events`, GEZIEN 17 nov). Op die lijst staat tussen maart en juni 2027 niets passends: Rhythm 8 tot 15 mrt, Dinos vs. Robots 29 mrt tot 5 apr, Racing 12 tot 19 apr, Witch 22 tot 26 apr, Fighting 26 apr tot 3 mei, RTS 10 tot 17 mei, Mountaineering 31 mei tot 3 jun. Dus: **terugval Summer Sale 24 jun tot 8 jul**, tenzij Valve vóór die tijd een fest toevoegt dat past (idle, bureaublad, kerker, cozy). Vera kijkt die lijst elke maand na (afspraak Fenna). **De eerste grote update krijgt een eigen dag zonder korting**, want de korting voegde bij de update niets toe en zo bewaren we de kortingsmail voor de etalage. Wat het zou veranderen: een passend fest vóór juni op de lijst (dan daarheen), of als Hats in de Idler Fest of een Desktop Companion Fest 2028 kan.

## Lanceerweek, wat er klaarstaat
| Wanneer | Wat | Waar |
|---|---|---|
| ±16 feb | mails voor bundels (Mister Morris Games voor Bottom-Of-Your-Screen, Tiny Pasture lanceerbundel met hun sjabloon, Cozy Mining, Hero Town) | `bundels.md` |
| uitgavedag | uitgavebericht A10, bundelpost A9 als de bundels staan | `teksten-thijs.md` |
| dag 3 tot 7 | routekaart A8 met 5 vakjes, afvinken in dezelfde post | `routekaart.md` |
| 4 tot 8 weken erna | gasthoed met Rusty's als update, alleen met iets nieuws om te spelen | `bundels.md`, kopje Crossovers |
| ±1 apr of later | eerste grote update, eigen dag zonder korting (bijgesteld run 15) | hier |
| eerste passend themafest, anders Summer Sale 24 jun | eerste korting 20 tot 25% | hier |

## Open
- Datum van de eerste grote update: vraag aan Olaf als het volle spel vaststaat (na de bevriezing van 15 feb), niet nu.
- Prijs zelf: bij Vera en de hoofdchat; dit plan rekent alleen met procenten.

## Vaste dag op de pagina en de Persoonlijke Kalender (run 19, 17 nov ±05:50 UTC)
Aanleiding: Fenna verhaal 24 en haar bericht aan de hoofdchat (17 nov ±06:00). Valve-pagina zelf gelezen met curl (`partner.steamgames.com/doc/marketing/visibility/personalcalendar`, GEZIEN 17 nov):
- Alleen een spel met een zichtbare "Coming Soon"-pagina **met een vaste dag** kan op de kalender. Tip van Valve: dag minstens **60 dagen vooraf** voor de eigen kalenderpagina (8 weken), minstens **3 weken** voor de voorpagina (deze week, twee weken terug, twee weken vooruit).
- Wie het spel al op zijn verlanglijst heeft, ziet het er altijd in. Voor de rest kiest Steam per speler via "spelers met dezelfde smaak hebben het op hun verlanglijst". Geen drempel.
- **Verschuiven mag**, ook als het spel er al in stond. Alleen: binnen 2 weken vóór de dag meer dan 24 uur uitstellen = van de kalender tot de uitgave. Demo's komen er niet in. Zaterdag en zondag tellen als maandag.

**Gemeten in onze hoek** (`data/vaste-datum.py`, `data/vaste-datum-2026-11-17.csv`, appdetails van de 251 aangekondigde bureaubladspellen uit run 2, GEZIEN 17 nov): maar **34 van 251 (14%) hebben een vaste dag**; 136 staan op "Coming soon", 32 op een kwartaal, 22 op een maand, 24 op een jaar. In februari tot april 2027 staan er maar **4** met een vaste dag (Desk Hive 1 feb, Loop Tower 24 mrt met 351 volgers, How To Goblin en Little Colony 30 mrt); 16 staan op "Q1 2027" of "March 2027" en kiezen later. Woollings (2 mrt, Fenna) zit niet in mijn lijst van 251, die uit Vera's kaart van 736 wel. Volgers verschillen niet tussen wie wel en geen dag heeft (mediaan 9,5 tegen 9), dus een dag op zich trekt niets; het voordeel is alleen de kalender. Eerlijk: hoeveel die kalender oplevert weet ik alleen van Zukowski (DERDEN, 33,8% doorklik bij één spel), niet zelf gemeten.

**Besluit Sem (marketing, de dag zelf kiest de hoofdchat):**
1. **Vaste dag op de pagina vanaf de paginadag (±8 dec), niet pas op 1 jan.** Waarom: verschuiven is gratis tot 2 weken vooraf, dus een vroege dag kost niets en geeft de meeste weken op de kalender; en 86% van onze hoek laat die plek liggen. "March 2027" of "Q1 2027" niet gebruiken, die tellen niet.
2. **De dag ligt vast vanaf 2 weken vooraf** (bij 2 mrt: di 16 feb; bij 29 mrt: ma 15 mrt). Daarna alleen nog verschuiven bij een echte fout, en dan wetend dat we van de kalender gaan.
3. **Stap voor Thijs** op `organisatie/lijst-thijs.md`: bij pagina live de releasedatum als vaste dag invullen.

**Wat de keuze 2 mrt of eind maart doet met mijn plannen** (zodat de hoofdchat het in één keer ziet; rekenwerk, GEZIEN in de docs waar vermeld):
| | di 2 mrt | ma 29 mrt tot do 1 apr (Fenna) |
|---|---|---|
| uiterste dag voor 60 dagen kalender | vr 1 jan | do 28 tot zo 31 jan |
| dag ligt vast (2 weken) | di 16 feb, dag na de bevriezing van 15 feb | ma 15 tot do 18 mrt |
| Next Fest Wrap-Up (ma 1 mrt) | avond vóór de uitgave | 4 weken vóór de uitgave, dus geen extra duw op de dag zelf |
| bundelmails (±2 weken vooraf, `bundels.md`) | ±16 feb | ±15 mrt, met de Next Fest-cijfers erbij (sterker verhaal voor Mister Morris en Tiny Pasture) |
| eerste korting mag (30 dagen na uitgave) | vanaf do 1 apr | vanaf ±28 apr; verandert niets, want de eerste korting gaat toch naar de Summer Sale (24 jun) |
| Spring Sale 18 tot 25 mrt | binnen 30 dagen, geen korting | ligt vóór de uitgave, geen botsing |
| routekaart dag 3 tot 7 | 5 tot 9 mrt | 1 tot 5 apr |
| demo staat nog | 1 dag na Next Fest | ±4 weken na Next Fest; Valve: veel spelers downloaden in het fest en spelen later, dus die weken telt de demo nog |
| let op | | **ma 29 mrt is Tweede Paasdag** (Pasen 2027 is 28 mrt; vrij in NL, DE, UK, FR). Een spel "voor als je werkt" komt dan uit op een vrije dag in Europa; GOK of dat slecht is, maar ik zou di 30 mrt of wo 31 mrt kiezen |
Mijn oordeel: voor de marketing kan het allebei; mijn plannen schuiven mee zonder verlies, en eind maart geeft de bundelmails sterkere cijfers. Kiest de hoofdchat eind maart, dan **di 30 of wo 31 mrt**, niet ma 29 mrt. Ik verander niets aan de datums in dit plan tot de hoofdchat kiest.
