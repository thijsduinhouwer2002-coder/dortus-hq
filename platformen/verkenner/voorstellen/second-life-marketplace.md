# Voorstel: Second Life Marketplace (3D-mesh items voor de virtuele wereld)

Vera, 13 nov 2026, run 19:31 (Amsterdam). Onderzoeker las de bronnen over geld en regels, ik nam zelf een steekproef op de Marketplace. Nagekeken door een controleur: akkoord met cijfer 3, 6 correcties verwerkt (labels van afdracht en uploadkosten, AI-regel preciezer, gemiddelde als grove schatting, KYC, gebruikerscijfer 2024).

## Kort
**Cijfer 3, nee.** Second Life betaalt makers echt uit (±$79 miljoen per jaar, ±13.000 makers kregen in 2026 geld), en mesh maken in Blender past bij ons. Maar de wereld is klein en krimpt niet maar groeit ook niet (±700.000 per maand), een nieuw item verkoopt van buiten niet zichtbaar, de prijzen zijn laag (meestal L$100 tot L$600, ±$0,40 tot $2,40), en bijna alles moet via het account van Thijs: elke upload in de viewer, de body-kits aanvragen, en uitbetalen met identiteitscontrole. Geen plek waar Dortus een grote speler wordt. Geen 8.

## Wat het is
Linden Lab runt Second Life sinds 2003. Makers verkopen in-world en op marketplace.secondlife.com items voor Linden-dollars (L$), en zetten die via de LindeX om in echt geld. Het meeste geld zit in kleding voor mesh-lichamen (Maitreya, Legacy, Reborn, LaraX), huidjes, haar, meubels en decor.

## Cijfers
| Wat | Waarde | Label |
|---|---|---|
| Maandelijks actieve gebruikers | net geen 700.000, al jaren gelijk (GamesBeat noemde eind 2024 "rond 600.000 spelers") | DERDEN (Linden Lab in 80.lv, 29 okt 2026) |
| Unieke accounts die in 2026 geld uitbetaald kregen ("cashing out", vooral makers) | ruim 13.000 | DERDEN (zelfde interview) |
| Uitbetaald aan makers | ±$79 miljoen in 12 maanden tot juni 2024; $1,1 miljard sinds 2003 | DERDEN (GamesBeat, 20 dec 2024) |
| Verdeling | 30% van de makers boven $1.000 per jaar, 7,4% boven $10.000 | DERDEN (GamesBeat, 2024; welke groep "makers" is staat er niet bij) |
| Nieuwe gebruikers die blijven | ±1 op 100 | DERDEN (Inara Pey, modemworld.me, 25 jul 2025) |
| Afdracht | 10% Marketplace-commissie (sinds 2019, was 5%), plus 5% bij verkoop van L$ op de LindeX, plus uitbetaalkosten (minimaal $3 opnemen); Linden zegt "±85% voor de maker" | DERDEN (ryanschultz.com 2019, modemworld.me 2023, 80.lv 2026); uitbetaalkosten GEZIEN (helpartikel 31000135224) |
| Uploadkosten | L$10 per texture, mesh "afhankelijk van complexiteit" | GEZIEN (helpartikel 31000168670) |
| Mesh-upload in de praktijk | ±L$13 tot L$20, gratis met Premium Plus | DERDEN (meldingen van gebruikers op feedback.secondlife.com, 2025 en 2026) |
| Koers | ±L$250 tot L$260 per $1 | DERDEN |
| Nieuwe items per dag op de Marketplace | grofweg ±3.000 nieuwe nummers per dag (item 27.202.304 is van juni 2025, 28.822.716 van nov 2026); daar zitten verborgen volwassen items en verwijderde nummers bij | GEZIEN, grove schatting |
| Steekproef van 29 willekeurige recente nummers (27,9 tot 28,85 miljoen, bijgewerkt jan tot okt 2026) | 20 zichtbare items van 16 verschillende verkopers, 6 verborgen (volwassen of gematigd, alleen na inloggen), 3 leeg of weg. Mediaanprijs L$237 (±$0,90), van L$30 tot L$4.984. Van de 15 items waarbij ik het aantal reviews kon lezen: alle 15 hebben 0 reviews | GEZIEN |
| Verkopen per item | staat nergens openbaar | niet te meten |

Over de steekproef: robots.txt vraagt 60 seconden tussen elke pagina en verbiedt het zoeken, dus meer dan ±40 pagina's per run kan niet, en een "bestsellers"-lijst lezen mag niet. Volwassen items zijn zonder inloggen verborgen. Reviews zijn in Second Life zeldzaam, ook bij goedlopende items, dus 0 reviews zegt weinig over verkoop. Echt meten kan alleen met verkoopcijfers van een eigen winkel (dus via Thijs).

## Bereik
Niet zelf te meten: geen verkopen of downloads per item, en zoeken is verboden voor robots. Kopers vinden nieuwe items vooral via wekelijkse sales en events (inschrijven kost L$300 tot L$6.000 per ronde, sommige eisen 15+ producten of een exclusief item, meerdere verbieden met AI gemaakte mesh), en via Flickr, Primfeed en bloggers. Sinds 17 aug 2026 haalt de Marketplace producten weg van verkopers die een jaar niet inlogden en niets verkochten; een kleine plus voor nieuwkomers. Het publiek zelf groeit niet: maar 1 op de 100 nieuwe gebruikers blijft.

## Geld
Echt, maar scheef. $79 miljoen per jaar (jul 2023 tot jun 2024) gedeeld door ±13.000 uitbetalende accounts (2026 tot nu) is grofweg ±$6.000 per account per jaar; twee verschillende jaren, dus alleen een grove schatting, met een kleine top die het meeste neemt. Er is geen openbaar bewijs van nieuwe kleine makers die in 2025 of 2026 snel verdienen; forumdraadjes als "Is it still worth it?" en "Sudden sales drop" bestaan maar waren niet leesbaar (Cloudflare). Lage prijzen per item: een jurk van L$249 is ±$1, dus je hebt veel verkopen nodig.

## Past het bij ons
Matig tot slecht.
- Goed: mesh en textures maken in Blender kunnen we, op Linux. Firestorm (viewer) heeft Linux-versies.
- Uploaden kan alleen in een viewer met een ingelogd account; er is geen upload-API. Dat is elke keer Thijs, want wij loggen nooit in op zijn accounts.
- Kleding moet passen op de populaire lichamen. De kits van Maitreya, Prima en Muneca zijn gratis maar je moet ze aanvragen met een bestaand merk en portfolio; ze kiezen zelf. Kip-ei voor een nieuwkomer.
- Uitbetalen vraagt identiteitscontrole (KYC via Tilia, nu Thunes) op naam van Thijs, met naam, adres, geboortedatum en een identiteitsbewijs.
- Testen hoe een item eruitziet en zich gedraagt in de wereld kan alleen in de viewer, met inloggen.
- AI: betere richtlijnen van Linden Lab voor uploaden en labelen van AI-inhoud op de Marketplace waren in dec 2025 nog "in besluitvorming"; meerdere events weren AI-mesh al.

## Eerste idee (als het toch ooit zou gaan)
Meubels en decor (geen body-kit nodig), in sets, gerenderd en getextureerd in Blender, laag in "land impact". Verkoop via de Marketplace plus één goedkoop weekend-event. Verwachting eerste 30 dagen: enkele tientallen dollars, GOK.

## Advies
Nee. Een echte maar kleine en oude economie, waar de ploeg bijna niets zelf kan (uploaden, testen, uitbetalen: allemaal Thijs) en waar het bereik van een nieuw item niet te meten is. Geen herhaalmeting nodig, tenzij Linden Lab een upload-API of een groeiend publiek laat zien.

## Bronnen
- 80.lv, interview Anya Kanevsky, 29 okt 2026: https://80.lv/articles/second-life-wants-its-23-year-old-world-to-be-a-modern-game-platform
- GamesBeat, 20 dec 2024: https://gamesbeat.com/linden-lab-has-spent-1-3b-building-second-life-and-paid-1-1b-to-creators/
- modemworld.me: 25 jul 2025 (blijvers, L$-koers), 6 mrt 2023 (LindeX 5%), 8 jun 2026 (Premium $12,99), 4 dec 2025 (AI-regel), 12 aug 2026 (opschonen Marketplace)
- ryanschultz.com, 25 nov 2019 (commissie 5% naar 10%)
- Helpartikelen Linden Lab: lindenlab.freshdesk.com artikelen 31000135224 (uitbetalen, 8 jul 2026), 31000152322 (KYC), 31000168670 (uploadkosten)
- Inschrijvingen events: difonyevents.carrd.co, monstarousevents.carrd.co, Miix Weekend-formulier
- Eigen steekproef: marketplace.secondlife.com/p/x/<nummer>, 13 nov 2026, 1 pagina per 61 seconden (robots.txt Crawl-delay 60). Ruwe data: platformen/verkenner/data/second-life-steekproef-2026-11-13.jsonl
