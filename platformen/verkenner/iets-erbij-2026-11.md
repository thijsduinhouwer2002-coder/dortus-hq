# Iets erbij naast Het Hol (opdracht Thijs 13 nov 14:10)

Vera, eerste versie 13 nov 2026, run 16:16 (Amsterdam). Uiterlijke datum voor de eerste versie was ma 16 nov 12:00. Controleur: zie onderaan.

Labels: GEZIEN (zelf gemeten), DERDEN (bron), GOK (schatting).

## Advies in vier zinnen
1. **Bouw een klein betaald spelletje voor Garmin-horloges met Gloop uit Het Hol, in Blender gerenderd** (kandidaat 1, cijfer 7). Betaalde spelletjes zijn op Garmin de sterkste soort betaalde app van 2026: van de nieuwe betaalde spellen van kleine makers haalt ±62% de 100+ en ±24% de 1.000+ downloads, tegen 46% en 10% voor alle betaalde apps.
2. Maak met dezelfde plaatjes een betaalde wijzerplaat (kandidaat 2, cijfer 5): een paar dagen extra werk, kleiner geld, extra zichtbaarheid en reclame voor Ebb en Het Hol.
3. Kandidaat 3 (een Blender-add-on die 3D-figuren omzet in sprites, op Superhive, cijfer 4) is alleen reserve: het bewijs is dun en geld hangt aan de Superhive-aanvraag die nog loopt.
4. **Niet doen: 3D-modellen of assetpakketten verkopen op Superhive.** Van 2.199 betaalde modellen van 0 tot 7 maanden oud heeft ±0,5% 10 of meer verkopen; er komen ±1.150 modellen per maand bij (GEZIEN, vandaag).

Waarom Garmin voor de top 2: de opdracht vraagt geld vanaf dag 1 zonder KvK. Bij Garmin betaalt de koper vóór het downloaden en is er geen proefperiode (forum Garmin, zie `platformen/garmin/concurrenten-2026-11-13.md` punt 7), het verkopersaccount bestaat en Ebb zit al in de keuring. JetBrains heeft een verplichte proef van 30 dagen, Steam vraagt een tweede fee en weken wachten, Obsidian heeft geen kassa (Rollwright: 0 verkopen), Superhive wacht nog op goedkeuring.

## Hoe gemeten
- Garmin: eigen analyse van de dataset van 9 nov (6.244 apps zonder wijzerplaat uit de open winkel-API, `data/garmin-niet-wijzerplaten-2026-11-09.json.gz`) en die van 6 nov (27.935 apps sinds juni 2025, met wijzerplaten, `data/garmin-nieuw-sinds-jun2025-2026-11-06.json`). Vandaag alle reviews gelezen van de 42 betaalde spellen uit jan t/m 15 aug 2026 (`data/garmin-spellen-gratis-eerst-script.py`, uitkomst `data/garmin-spellen-gratis-eerst-2026-11-13.jsonl`). Spellen = categorie 206 in de API.
- **Correctie op eerder werk:** in de dataset van 9 nov betekent `pay=1` niet "betaald in de winkel" maar "gratis, ontgrendelen buiten de winkel" (paymentModel 1; Caffeine Tracker en Beer Counter noemen zichzelf in hun beschrijving gratis met een premiumcode, GEZIEN). Betaald in de winkel is: het veld `pricing` heeft een prijs. Alle cijfers hier gebruiken `pricing`. Eerdere stukken die `pay` als "betaald" lazen (onder meer de tabel met zwakke betaalde apps in `kansen/garmin-zwakke-nummer-een.md`) moeten worden nagekeken.
- Superhive: 2.213 modelpagina's uit de categorie 3D-modellen (elke 3e lijstpagina van 1 tot 150 en elke 6e van 151 tot 417, nieuwste eerst), met verkoopteller (Superhive toont die vanaf 10). Script `data/superhive-modellen-script.py`, data `data/superhive-modellen-2026-11-13.jsonl.gz`. Add-ons uit de meting van 9 nov (`data/superhive-nieuwe-addons-2026-11-09.jsonl`).
- Geen onderzoeker-agent; wel een controleur (zie onderaan).

## Betaalde Garmin-apps in de winkel, eerste goedkeuring 1 jan tot 15 aug 2026 (GEZIEN)
| Soort | Aantal | Mediaan | 100+ | 1.000+ |
|---|---|---|---|---|
| Betaald in de winkel, alle soorten | 241 | 10+ | 46% | 10% |
| Gratis, ontgrendelen buiten de winkel | 164 | 100+ | 74% | 17% |
| Gratis | 966 | 100+ | 72% | 24% |
| **Betaalde spellen, zonder ThijsGer en QuadroGames** | 41 | 100+ | 68% | 29% |
| **Idem, ook zonder de 7 die eerst gratis waren** | 34 | 100+ | 62% | 24% |

Prijsmediaan betaald: $2,25; spellen bijna allemaal $1,99. Van de 24 betaalde apps met 1.000+ zijn er 12 spellen, en alle drie met 10.000+ zijn spellen.

---

## Kandidaat 1: betaald horlogespel met Gloop (Garmin). Cijfer 7.

**Wat:** een kort spelletje voor één knop en een paar seconden per potje, zoals de toppers (stapelen, springen, ontwijken), met Gloop en zijn hoeden uit Het Hol. De figuur wordt in Blender gerenderd tot kleine plaatjes per pose, met dezelfde stijl als Het Hol (`ontwerp/steam/3d-stijl.md`). Op het eindscherm: "Gloop lives in Het Hol, coming to Steam".

**Bewijs dat kleine makers verdienen (GEZIEN):**
- Betaalde spellen uit jan t/m 15 aug 2026, 3 tot 10 maanden oud: 34 spellen van kleine makers zonder aanwijzing dat ze eerst gratis waren; 62% heeft 100+ downloads, 24% heeft 1.000+. Bij betaalde apps in het algemeen is dat 46% en 10%.
- Voorbeelden zonder klachten over eerst gratis: Stack - Blocks Game (garminland, 10.000+, 60 reviews), ZigZag (garminland, 1.000+, 45), Chess Pro (Bitochi, 1.000+, 45), Blackjack (SilveroStudios, 1.000+, 39), Circle Pong, Snake (KBialy). Allemaal $1,99 tot $2,25.
- Rekenvoorbeeld (GOK, aangenomen dat downloads verkopen zijn): 100 tot 999 kopers x $1,99 x 0,85 = $170 tot $1.700 per spel over 3 tot 10 maanden; 1.000+ is minstens $1.700.
- **Eerlijk voorbehoud 1, eerst gratis:** 7 van de 42 betaalde spellen hebben klachten "it was free" in de reviews (MangoIQ met Crossy Road 3D, Stack en Google Dinosaur Game; KBialy Flags Quiz; drie van nioquant). Die tellen hierboven niet mee. Geen klachten bewijst niet dat een spel nooit gratis was, zeker bij weinig reviews.
- Wat wel betaald is bij een spel dat eerst gratis was: Crossy Road 3D kreeg na de omslag (eind juli) nog 14 reviews in september en 13 in oktober, met "Totally worth the money" (GEZIEN, 238 reviews gelezen). Ter vergelijking: WHM breathing+ ($4,99) krijgt ±26 per maand.
- **Eerlijk voorbehoud 2, het wordt drukker:** nieuwe betaalde spellen per maand: ±2 tot 12 in jan t/m jul 2026, daarna 27 in aug, 16 in sep, 39 in okt en 17 in de eerste 9 dagen van nov. De lichting 16 aug t/m 30 sep (1,5 tot 3 maanden oud, zonder ThijsGer en QuadroGames) staat op 6 van de 24 met 100+ (25%) en nog geen 1.000+. Dat is nog steeds beter dan betaalde apps in het algemeen op die leeftijd (±9% op 1 tot 2 maanden, Gijs, `platformen/garmin/onderzoek-thijsger-2026-11-10.md`), maar het venster gaat dicht. Wie dit doet, moet het snel doen.
- ThijsGer (187 apps) en QuadroGames (18) laten bijna elke betaalde app 100+ halen met 0 tot 1 review; Gijs vond dat geen gewoon koopgedrag. Ik laat ze weg.

**Waarom wij ons onderscheiden:** de toppers zijn platte blokjes, pixels en kloons van bekende spellen (Crossy Road, Google Dinosaur). Een echt in 3D gerenderde figuur met karakter (Gloop met hoed, wiebel bij landen) valt op tussen de vierkantjes, en het is ons eigen figuur, dus geen gedoe met merken. Het spel is daarnaast een reclamebord voor Het Hol bij mensen die graag iets op hun scherm hebben.

**Verwachte omzet eerste 30 dagen (GOK):** 20 tot 150 kopers x $1,99 x 0,85 = **$35 tot $250**. Onderkant: de lichting van aug en sep (25% haalt 100+ in 1,5 tot 3 maanden). Bovenkant: tempo van de beste spellen van begin 2026. Geen proef, dus elke download is een verkoop (met 48 uur terugbetalen).

**Uren werk (GOK):** Gijs 20 tot 35 uur (spel in Monkey C, één scherm, punten, beste score opslaan; hij kent de SDK en de simulator van Ebb), Bram of Daan 6 tot 10 uur (Gloop renderen in 6 tot 12 poses op 3 schermmaten, met de pijplijn van Het Hol). Kloktijd bij doorlopen: ±1 week. Risico: geheugen op oudere horloges; begin zoals Ebb met de ronde horloges die Ebb al ondersteunt.

**Wat Thijs moet doen:** niets nieuws. Op Verzend klikken in het Garmin-portaal zoals bij Ebb, en ja zeggen op de winkelbeelden. Geen geld: het verkopersaccount is al betaald.

**Open punten (volgende run):** (1) welke spelvorm nog geen sterke betaalde versie heeft (lijst van alle 605 spellen op soort); (2) of de keuringsregels van Garmin iets zeggen over spellen; (3) welke horloges de meeste spelkopers hebben.

---

## Kandidaat 2: betaalde wijzerplaat met Gloop of de Ebb-dieren (Garmin). Cijfer 5.

**Wat:** één tot drie wijzerplaten met een in 3D gerenderd figuur (Gloop, of de krab en schildpad uit Ebb) en de gewone gegevens (tijd, stappen, batterij). Prijs $1,99.

**Bewijs (GEZIEN, wijzerplaten met eerste goedkeuring 6 mei tot 6 aug 2026, dataset 6 nov):**
| Groep | Aantal | Mediaan | 100+ | 1.000+ |
|---|---|---|---|---|
| Betaalde wijzerplaten, alle makers | 1.002 | 1+ | 14% | 3% |
| Betaald, kleine makers (20 of minder wijzerplaten) | 157 | 10+ | 31% | 8% |
| Betaald, fabrieken (meer dan 50) | 745 | 1+ | 9% | 1% |

Voorbeelden van kleine makers op 1.000+: Cool Otter (MONYMAHONY, 3 wijzerplaten, $1,99, een dier), NDR One Pro ($4,99, 182 reviews), Quipu ($2,25, 10.000+, 222 reviews). Prijsmediaan $2,49. Ook hier is niet per wijzerplaat zeker dat een download een verkoop is.

**Onderscheid:** de massa komt uit fabrieken met hetzelfde sjabloon; een figuur met karakter en echte 3D-belichting valt op. Werkt als reclame voor Ebb of Het Hol.

**Omzet eerste 30 dagen (GOK):** 5 tot 40 kopers x $1,99 x 0,85 = **$8 tot $70** per wijzerplaat.

**Uren (GOK):** 8 tot 16 uur per wijzerplaat (Gijs), plaatjes uit kandidaat 1 hergebruikt. **Thijs:** Verzend klikken.

---

## Kandidaat 3: Blender-add-on "3D-figuur naar sprites" op Superhive. Cijfer 4, reserve.

**Wat:** een add-on die een 3D-figuur in een paar klikken rendert naar spritebladen en losse plaatjes op vaste kleine maten (horloge, pixelspel, Godot), met belichting en omtrek. Dat is precies het gereedschap dat wij voor kandidaat 1 en Het Hol zelf bouwen, dus het kost weinig extra.

**Bewijs (GEZIEN, meting 9 nov):** betaalde add-ons op Superhive van 3 tot 12 maanden oud halen in 42% van de gevallen 10+ verkopen (n=1.613). In deze hoek: Pixel Art Studio ($19,90, 100+ verkopen in 2 maanden), Pro Sprite Sheet Generator ($10, 30+), Pixel Kit ($9, 10+), Flipbook For Blender ($15, 10+). Dun bewijs: geen enkele maker in deze hoek haalt duidelijk honderden per maand, en er kwamen in 2 maanden 6 nieuwe bij. Het hele aanbod van add-ons is ±4 keer zo groot als een jaar geleden (`kansen/blender-nieuwkomers-en-vloed.md`).

**Omzet eerste 30 dagen (GOK):** 0 tot 15 verkopen x ±$12 x 0,70 = **$0 tot $125**, en pas zodra Superhive de makersaanvraag van Thijs heeft goedgekeurd (loopt sinds 10 nov).

**Uren (GOK):** Bram 15 tot 25 uur, plus winkelplaatjes. **Thijs:** niets nieuws (het Superhive-account staat al op zijn lijst).

---

## Wat afviel
- **3D-modellen en assetpakketten op Superhive (nieuw gemeten vandaag):** van 2.199 betaalde modellen van 0 tot 7 maanden oud hebben er 10 (0,5%) 10+ verkopen en 2 100+; per leeftijd 3 tot 7 maanden 0 tot 1%. Er komen ±1.150 modellen per maand bij, voor een groot deel van een paar massamakers (Md Rafikul Islam 428 in de steekproef, TurboCG 200, Viktor Fedorov 142). Nee, cijfer 1.
- **Tweede Garmin-hulpapp in een drukke hoek** (water, cafeïne, vasten, alcohol): Garmin heeft zelf watertracking (5.000.000+), de grootste zijn gratis met een code buiten de winkel. Onderscheidt zich niet met 3D.
- **Virtueel huisdier op Garmin:** past bij de Ebb-dieren, maar betaald in de winkel is er geen bewijs (Watchkin gratis 1.000+, WatchiBeastie gratis 50.000+, Critter Park ontgrendelt buiten de winkel). Kan later als variant van kandidaat 1.
- **Loopband koppelen (FTMS):** echte vraag, maar we hebben geen apparaat om te testen (`kansen/garmin-zwakke-nummer-een.md`).
- **Steam, tweede klein product:** tweede fee en weken wachten. **JetBrains:** verplichte proef van 30 dagen. **TikTok:** KvK nodig. **Cults3D** (3D-printbestanden): niet te meten, Cloudflare blokkeert lezen; niet omheen gewerkt.

## Controleur
(volgt in deze run)

## Bronnen
- Open winkel-API Garmin: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>` en `/reviews?startPageIndex=<n>&pageSize=30` (gelezen 13 nov 2026).
- Superhive: `https://superhivemarket.com/categories/models/browse?sort_date=desc&page=<n>` en de productpagina's (gelezen 13 nov 2026).
