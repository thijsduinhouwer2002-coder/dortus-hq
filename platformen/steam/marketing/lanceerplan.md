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

**Bijgesteld in run 15 (17 nov ±02:10 UTC), na Fenna verhaal 21.** Punt 3 hierboven klopt niet meer. Fenna mat 24 bureaubladspellen met een aangekondigde eerste korting van 20%+ (`platformen/succes/data/eerste-korting-na-lancering-2026-11-17.csv`, zelf nagerekend): reviews per week in de kortingsweken tegen de 3 weken ervoor.
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
