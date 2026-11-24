# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.09 tot $2.07 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 22 runs, 7389 minuten (123.2 uur) (GEZIEN). Markten in de data: 3464. Uitslag bekend voor 2266 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $187 (3290 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-69.76 (377 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 800 | 158 | $2,944 | $7,728 | $160 tot $330 | 2292 / 1655 | $8,011 | $-146 (157 nog zonder prijs) | $0.00 (0 van 2292 beslist) | $13.94 tot $184 |
| **Totaal** | 7389 | | $3,911 | $10,171 | $1,814 tot $3,714 | 23420 / 17021 | $75,751 | $-2,147 | $-1,177 | $-333 tot $1,567 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,623 over 23373 vullingen en $75,620, dus -2.15% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.88% over $74,605 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.73%.

**Opgeschaald (GOK):** per dag $-71.30 (ondergrens) tot $299 (hoge schatting) netto (gemeten minuten × 1440 / 7389).

456 van de 23420 vullingen ($1,146) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.88%): $-32.98 (GOK).

Geld dat de bot nodig had: gemiddeld $3,911 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,081**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-911 tot $3,821 |
| €5,000 | $5,000 | $-2,278 tot $9,552 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,177 over 15526 vullingen en $50,160, dus -2.35% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.07% per dollar over 22503 vullingen, 1 uur later -2.79% over 22073 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.90% per dollar over 870 vullingen, 1 uur later -4.86% over 857 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-169 (616 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $22.83 (107 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 800 | 158 | $2,926 | $3,593 | $40.22 tot $105 | 519 / 311 | $2,198 | $-24.77 (34 nog zonder prijs) | $0.00 (0 van 519 beslist) | $15.45 tot $80.11 |
| **Totaal** | 7389 | | $3,847 | $4,020 | $449 tot $1,176 | 4752 / 3072 | $17,812 | $-417 | $-152 | $31.69 tot $759 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-418 over 4739 vullingen en $17,756, dus -2.35% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.38% over $17,550 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.51%.

**Opgeschaald (GOK):** per dag $4.96 (ondergrens) tot $147 (hoge schatting) netto (gemeten minuten × 1440 / 7389).

102 van de 4752 vullingen ($263) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.38%): $-6.25 (GOK).

Geld dat de bot nodig had: gemiddeld $3,847 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,867**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $113 tot $3,355 |
| €5,000 | $5,000 | $284 tot $8,387 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-152 over 2930 vullingen en $10,777, dus -1.41% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.33% per dollar over 4509 vullingen, 1 uur later -2.37% over 4412 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.85% per dollar over 230 vullingen, 1 uur later -2.31% over 228 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1417 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.53 tot $3.11 | $-0.55 tot $1.03 | 2 | $12.24 tot $15.71 | $21.03 tot $24.49 |
| €150 | 2 | $3.05 tot $6.21 | $-1.09 tot $2.07 | 3 | $17.94 tot $25.91 | $26.72 tot $34.69 |
| €200 | 3 | $4.58 tot $9.32 | $-1.64 tot $3.10 | 4 | $23.64 tot $35.87 | $20.77 tot $32.99 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.88%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest tel-aviv-on-november-25 24°C | 1207 | $4.27 tot $8.77 | 27 | $-20.74 | $0.00 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $0.00 |
| highest hong-kong-on-november-24 22°C | 1464 | $4.44 tot $8.79 | 89 | $-20.19 | $0.00 |
| highest toronto-on-november-23 12°C | 1200 | $2.93 tot $5.19 | 44 | $-18.45 | $21.60 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $28.93 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $-14.69 |
| ... | | | | | |
| highest ankara-on-november-24 11°C | 1121 | $1.60 tot $3.18 | 36 | $7.26 | $0.00 |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $0.00 |
| highest nyc-on-november-25 48-49°F | 1185 | $5.18 tot $8.48 | 31 | $12.09 | $0.00 |
| highest warsaw-on-november-25 5°C | 2062 | $1.60 tot $3.69 | 16 | $64.14 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $40.36 tot $85.31 | 391 | $38.21 | $78.57 |
| seoul (highest) | $37.41 tot $79.01 | 691 | $-1.49 | $35.92 |
| miami (lowest) | $44.37 tot $77.16 | 108 | $-15.64 | $28.73 |
| london (lowest) | $32.42 tot $58.96 | 185 | $-8.90 | $23.52 |
| chengdu (highest) | $36.02 tot $78.79 | 363 | $-15.04 | $20.98 |
| nyc (highest) | $55.37 tot $114 | 938 | $-38.85 | $16.52 |
| beijing (highest) | $31.00 tot $65.86 | 397 | $-15.94 | $15.06 |
| wuhan (highest) | $35.30 tot $74.85 | 312 | $-21.56 | $13.74 |
| paris (lowest) | $37.10 tot $68.69 | 119 | $-23.89 | $13.20 |
| manila (highest) | $22.04 tot $44.29 | 185 | $-9.78 | $12.26 |
| kuala-lumpur (highest) | $26.54 tot $50.98 | 258 | $-15.37 | $11.17 |
| mexico-city (highest) | $31.95 tot $61.57 | 199 | $-22.09 | $9.86 |
| munich (highest) | $40.25 tot $84.52 | 590 | $-31.81 | $8.44 |
| karachi (highest) | $26.31 tot $51.63 | 208 | $-18.20 | $8.11 |
| austin (highest) | $50.25 tot $104 | 530 | $-42.31 | $7.94 |
| singapore (highest) | $36.91 tot $79.10 | 474 | $-28.98 | $7.94 |
| jeddah (highest) | $20.45 tot $41.12 | 147 | $-12.88 | $7.57 |
| milan (highest) | $39.23 tot $79.85 | 526 | $-32.78 | $6.45 |
| chongqing (highest) | $38.44 tot $79.95 | 313 | $-32.44 | $6.00 |
| shanghai (lowest) | $11.87 tot $21.74 | 41 | $-7.06 | $4.81 |
| shenzhen (highest) | $27.23 tot $56.93 | 455 | $-24.37 | $2.86 |
| sao-paulo (highest) | $29.98 tot $59.60 | 339 | $-29.40 | $0.57 |
| nyc (lowest) | $13.62 tot $23.00 | 88 | $-13.22 | $0.41 |
| tokyo (highest) | $32.62 tot $71.66 | 570 | $-34.06 | $-1.43 |
| london (highest) | $44.97 tot $97.91 | 866 | $-47.30 | $-2.33 |
| houston (highest) | $55.46 tot $115 | 806 | $-59.46 | $-4.00 |
| los-angeles (highest) | $35.67 tot $78.72 | 665 | $-39.80 | $-4.13 |
| seoul (lowest) | $22.51 tot $42.39 | 121 | $-26.65 | $-4.14 |
| buenos-aires (highest) | $26.92 tot $51.91 | 351 | $-33.19 | $-6.27 |
| moscow (highest) | $26.06 tot $52.43 | 306 | $-32.68 | $-6.63 |
| shanghai (highest) | $37.19 tot $80.52 | 696 | $-45.08 | $-7.88 |
| tokyo (lowest) | $13.47 tot $22.88 | 66 | $-21.97 | $-8.50 |
| lucknow (highest) | $42.36 tot $87.78 | 382 | $-51.88 | $-9.51 |
| ankara (highest) | $29.76 tot $57.94 | 446 | $-40.52 | $-10.76 |
| qingdao (highest) | $23.37 tot $46.45 | 271 | $-34.90 | $-11.54 |
| taipei (highest) | $29.38 tot $54.39 | 329 | $-42.77 | $-13.39 |
| chicago (highest) | $46.06 tot $86.08 | 668 | $-60.28 | $-14.23 |
| amsterdam (highest) | $36.38 tot $79.49 | 651 | $-52.91 | $-16.54 |
| madrid (highest) | $36.52 tot $80.64 | 546 | $-54.66 | $-18.13 |
| hong-kong (lowest) | $8.50 tot $15.10 | 143 | $-27.12 | $-18.62 |
| guangzhou (highest) | $43.73 tot $88.90 | 599 | $-63.55 | $-19.82 |
| miami (highest) | $46.48 tot $97.54 | 650 | $-67.96 | $-21.48 |
| san-francisco (highest) | $34.47 tot $67.15 | 448 | $-61.37 | $-26.91 |
| tel-aviv (highest) | $45.62 tot $97.90 | 391 | $-75.39 | $-29.77 |
| atlanta (highest) | $50.25 tot $106 | 934 | $-88.26 | $-38.01 |
| toronto (highest) | $26.33 tot $51.90 | 468 | $-66.15 | $-39.82 |
| busan (highest) | $36.79 tot $78.24 | 518 | $-82.07 | $-45.28 |
| wellington (highest) | $34.39 tot $75.33 | 528 | $-90.12 | $-55.73 |
| helsinki (highest) | $52.66 tot $108 | 721 | $-111 | $-58.47 |
| hong-kong (highest) | $33.09 tot $69.59 | 852 | $-92.56 | $-59.47 |
| dallas (highest) | $47.59 tot $100 | 639 | $-108 | $-59.95 |
| paris (highest) | $50.97 tot $110 | 932 | $-112 | $-60.75 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
