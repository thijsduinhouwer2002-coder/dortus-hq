# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.22 tot $1.98 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 24 runs, 8060 minuten (134.3 uur) (GEZIEN). Markten in de data: 3464. Uitslag bekend voor 2607 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-54.13 (4072 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-221 (2456 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (66 nog zonder prijs) | $0.00 (0 van 4307 beslist) | $2.93 tot $323 |
| 2026-11-25 | 37 | 160 | $2,924 | $7,198 | $6.35 tot $13.48 | 121 / 69 | $420 | $0.00 (121 nog zonder prijs) | $0.00 (0 van 121 beslist) | $6.35 tot $13.48 |
| **Totaal** | 8060 | | $3,847 | $10,171 | $1,961 tot $4,019 | 25556 / 18452 | $82,827 | $-2,299 | $-1,570 | $-338 tot $1,720 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,686 over 25508 vullingen en $82,685, dus -2.04% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.82% over $81,491 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.61%.

**Opgeschaald (GOK):** per dag $-67.04 (ondergrens) tot $301 (hoge schatting) netto (gemeten minuten × 1440 / 8060).

486 van de 25556 vullingen ($1,336) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.82%): $-37.69 (GOK).

Geld dat de bot nodig had: gemiddeld $3,847 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,018**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-861 tot $3,859 |
| €5,000 | $5,000 | $-2,152 tot $9,647 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,570 over 18387 vullingen en $59,045, dus -2.66% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -1.97% per dollar over 24575 vullingen, 1 uur later -2.74% over 24117 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.90% per dollar over 933 vullingen, 1 uur later -4.86% over 916 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-231 (795 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $27.03 (607 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-41.88 (13 nog zonder prijs) | $0.00 (0 van 994 beslist) | $31.81 tot $158 |
| 2026-11-25 | 37 | 160 | $2,977 | $3,395 | $1.64 tot $4.77 | 25 / 14 | $108 | $0.00 (25 nog zonder prijs) | $0.00 (0 van 25 beslist) | $1.64 tot $4.77 |
| **Totaal** | 8060 | | $3,786 | $4,020 | $484 tot $1,275 | 5252 / 3366 | $19,801 | $-434 | $-209 | $49.69 tot $841 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-447 over 5238 vullingen en $19,745, dus -2.26% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.23% over $19,490 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.23%.

**Opgeschaald (GOK):** per dag $7.64 (ondergrens) tot $149 (hoge schatting) netto (gemeten minuten × 1440 / 8060).

106 van de 5252 vullingen ($311) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.23%): $-6.94 (GOK).

Geld dat de bot nodig had: gemiddeld $3,786 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,806**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $176 tot $3,436 |
| €5,000 | $5,000 | $440 tot $8,591 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-209 over 3609 vullingen en $13,327, dus -1.57% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.24% per dollar over 4994 vullingen, 1 uur later -2.21% over 4893 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.83% per dollar over 244 vullingen, 1 uur later -2.24% over 242 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1535 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.54 tot $3.14 | $-0.61 tot $0.99 | 2 | $24.62 tot $43.88 | $83.02 tot $102 |
| €150 | 2 | $3.08 tot $6.28 | $-1.22 tot $1.98 | 3 | $36.85 tot $60.17 | $80.71 tot $104 |
| €200 | 3 | $4.62 tot $9.43 | $-1.84 tot $2.97 | 5 | $49.63 tot $80.53 | $50.25 tot $81.14 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.82%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $24.65 |
| highest hong-kong-on-november-24 22°C | 1464 | $4.44 tot $8.79 | 89 | $-20.19 | $0.00 |
| highest toronto-on-november-23 12°C | 1200 | $2.93 tot $5.19 | 44 | $-18.45 | $21.60 |
| highest tel-aviv-on-november-25 24°C | 1688 | $6.04 tot $12.55 | 32 | $-20.91 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $28.93 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $-14.69 |
| ... | | | | | |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest nyc-on-november-26 58-59°F | 477 | $0.59 tot $0.83 | 6 | $9.57 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $0.00 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $43.92 tot $91.83 | 418 | $88.69 | $133 |
| seoul (highest) | $40.11 tot $84.85 | 751 | $-2.31 | $37.80 |
| miami (lowest) | $47.11 tot $82.25 | 115 | $-17.91 | $29.20 |
| london (lowest) | $34.93 tot $63.56 | 203 | $-9.38 | $25.55 |
| chengdu (highest) | $39.86 tot $86.86 | 412 | $-14.48 | $25.37 |
| beijing (highest) | $33.87 tot $72.15 | 429 | $-11.88 | $21.99 |
| paris (lowest) | $40.62 tot $74.94 | 133 | $-25.78 | $14.84 |
| austin (highest) | $52.21 tot $109 | 555 | $-39.96 | $12.25 |
| manila (highest) | $23.71 tot $47.82 | 200 | $-12.41 | $11.30 |
| kuala-lumpur (highest) | $27.97 tot $53.83 | 270 | $-17.04 | $10.92 |
| wuhan (highest) | $39.15 tot $82.97 | 346 | $-28.39 | $10.76 |
| karachi (highest) | $28.20 tot $55.76 | 229 | $-17.95 | $10.25 |
| chongqing (highest) | $41.51 tot $86.52 | 343 | $-33.23 | $8.28 |
| munich (highest) | $44.38 tot $93.39 | 665 | $-36.13 | $8.26 |
| mexico-city (highest) | $34.02 tot $66.64 | 241 | $-25.80 | $8.21 |
| milan (highest) | $42.66 tot $87.28 | 590 | $-35.27 | $7.39 |
| jeddah (highest) | $21.93 tot $44.27 | 166 | $-14.74 | $7.20 |
| singapore (highest) | $40.12 tot $85.97 | 533 | $-35.19 | $4.93 |
| shanghai (lowest) | $11.88 tot $21.78 | 41 | $-7.06 | $4.83 |
| moscow (highest) | $27.66 tot $55.30 | 333 | $-23.46 | $4.20 |
| london (highest) | $48.31 tot $105 | 950 | $-47.49 | $0.82 |
| sao-paulo (highest) | $32.43 tot $64.42 | 366 | $-31.79 | $0.63 |
| shenzhen (highest) | $29.96 tot $62.70 | 523 | $-29.33 | $0.63 |
| nyc (lowest) | $13.84 tot $23.41 | 89 | $-13.22 | $0.62 |
| seoul (lowest) | $24.27 tot $45.67 | 136 | $-24.75 | $-0.48 |
| tokyo (highest) | $34.70 tot $76.39 | 601 | $-36.67 | $-1.97 |
| nyc (highest) | $58.75 tot $121 | 966 | $-62.01 | $-3.27 |
| los-angeles (highest) | $38.47 tot $85.04 | 722 | $-42.10 | $-3.63 |
| houston (highest) | $61.85 tot $127 | 888 | $-65.97 | $-4.12 |
| buenos-aires (highest) | $28.81 tot $56.22 | 396 | $-35.32 | $-6.51 |
| ankara (highest) | $32.05 tot $62.43 | 487 | $-40.42 | $-8.38 |
| tokyo (lowest) | $13.47 tot $22.88 | 66 | $-21.97 | $-8.50 |
| qingdao (highest) | $24.34 tot $48.39 | 275 | $-34.60 | $-10.26 |
| taipei (highest) | $31.05 tot $57.70 | 344 | $-43.48 | $-12.43 |
| chicago (highest) | $47.64 tot $89.25 | 727 | $-61.12 | $-13.48 |
| madrid (highest) | $42.20 tot $92.48 | 605 | $-58.67 | $-16.47 |
| lucknow (highest) | $46.81 tot $96.85 | 483 | $-66.35 | $-19.54 |
| shanghai (highest) | $41.25 tot $89.11 | 770 | $-63.49 | $-22.24 |
| miami (highest) | $49.51 tot $104 | 692 | $-72.88 | $-23.37 |
| hong-kong (lowest) | $8.62 tot $15.32 | 151 | $-32.56 | $-23.94 |
| guangzhou (highest) | $46.54 tot $95.25 | 628 | $-70.64 | $-24.10 |
| tel-aviv (highest) | $53.64 tot $114 | 422 | $-79.23 | $-25.59 |
| san-francisco (highest) | $35.84 tot $69.82 | 490 | $-64.16 | $-28.32 |
| amsterdam (highest) | $39.97 tot $87.07 | 706 | $-68.79 | $-28.82 |
| atlanta (highest) | $52.62 tot $112 | 986 | $-90.23 | $-37.61 |
| busan (highest) | $39.94 tot $84.96 | 561 | $-91.26 | $-51.32 |
| dallas (highest) | $51.60 tot $109 | 697 | $-103 | $-51.55 |
| helsinki (highest) | $61.48 tot $125 | 833 | $-118 | $-56.30 |
| toronto (highest) | $27.38 tot $54.20 | 500 | $-84.07 | $-56.69 |
| wellington (highest) | $36.84 tot $80.59 | 577 | $-99.59 | $-62.75 |
| paris (highest) | $55.35 tot $120 | 1027 | $-122 | $-66.44 |
| hong-kong (highest) | $35.96 tot $75.91 | 919 | $-104 | $-68.30 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
