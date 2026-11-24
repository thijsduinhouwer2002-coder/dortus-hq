# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.42 tot $1.74 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 20 runs, 6717 minuten (112.0 uur) (GEZIEN). Markten in de data: 2917. Uitslag bekend voor 2068 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-381 (4372 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-26.12 (2090 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-20.60 (3 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 128 | 147 | $2,748 | $7,570 | $20.90 tot $43.79 | 309 / 217 | $983 | $-10.25 (134 nog zonder prijs) | $0.00 (0 van 309 beslist) | $10.65 tot $33.55 |
| **Totaal** | 6717 | | $4,004 | $10,171 | $1,675 tot $3,427 | 21437 / 15583 | $68,723 | $-2,011 | $-1,296 | $-336 tot $1,416 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,512 over 21398 vullingen en $68,601, dus -2.20% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.98% over $67,560 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.84%.

**Opgeschaald (GOK):** per dag $-79.49 (ondergrens) tot $296 (hoge schatting) netto (gemeten minuten × 1440 / 6717).

433 van de 21437 vullingen ($1,163) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.98%): $-34.62 (GOK).

Geld dat de bot nodig had: gemiddeld $4,004 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,174**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,009 tot $3,762 |
| €5,000 | $5,000 | $-2,523 tot $9,404 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,296 over 13526 vullingen en $44,263, dus -2.93% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.13% per dollar over 20566 vullingen, 1 uur later -2.91% over 20153 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.95% per dollar over 832 vullingen, 1 uur later -4.54% over 819 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-74.79 (882 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-25.47 (376 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $-11.00 (1 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 128 | 147 | $2,721 | $3,534 | $5.22 tot $14.74 | 60 / 30 | $246 | $-0.00 (30 nog zonder prijs) | $0.00 (0 van 60 beslist) | $5.22 tot $14.73 |
| **Totaal** | 6717 | | $3,935 | $4,020 | $414 tot $1,086 | 4293 / 2791 | $15,860 | $-392 | $-50.80 | $21.46 tot $693 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-371 over 4280 vullingen en $15,804, dus -2.35% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.52% over $15,554 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.57%.

**Opgeschaald (GOK):** per dag $2.95 (ondergrens) tot $147 (hoge schatting) netto (gemeten minuten × 1440 / 6717).

98 van de 4293 vullingen ($306) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.52%): $-7.72 (GOK).

Geld dat de bot nodig had: gemiddeld $3,935 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,955**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $66.65 tot $3,325 |
| €5,000 | $5,000 | $167 tot $8,313 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-50.80 over 2500 vullingen en $9,380, dus -0.54% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.35% per dollar over 4065 vullingen, 1 uur later -2.57% over 3974 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.20% per dollar over 215 vullingen, 1 uur later -1.27% over 211 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1334 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.54 tot $3.12 | $-0.71 tot $0.87 | 2 | $21.37 tot $38.94 | $-112 tot $-94.84 |
| €150 | 2 | $3.09 tot $6.25 | $-1.42 tot $1.74 | 3 | $30.88 tot $54.08 | $-104 tot $-80.40 |
| €200 | 3 | $4.63 tot $9.37 | $-2.13 tot $2.61 | 4 | $38.94 tot $69.95 | $-133 tot $-102 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.98%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $0.00 |
| highest hong-kong-on-november-24 22°C | 1464 | $4.44 tot $8.79 | 89 | $-20.19 | $0.00 |
| highest toronto-on-november-23 12°C | 1200 | $2.93 tot $5.19 | 44 | $-18.45 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $28.93 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $-14.69 |
| lowest seoul-on-november-23 3°C | 720 | $0.81 tot $1.65 | 27 | $-14.61 | $34.92 |
| ... | | | | | |
| lowest london-on-november-24 2°C | 1505 | $2.32 tot $4.23 | 15 | $6.31 | $0.00 |
| highest ankara-on-november-24 11°C | 1121 | $1.60 tot $3.18 | 36 | $7.26 | $0.00 |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $0.00 |
| highest warsaw-on-november-25 6°C or higher | 597 | $0.47 tot $0.95 | 8 | $17.58 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| miami (lowest) | $41.86 tot $72.71 | 103 | $-10.45 | $31.41 |
| warsaw (highest) | $39.23 tot $82.56 | 383 | $-8.35 | $30.89 |
| seoul (highest) | $33.50 tot $70.82 | 614 | $-6.28 | $27.22 |
| london (lowest) | $29.86 tot $55.12 | 177 | $-8.51 | $21.35 |
| chengdu (highest) | $32.97 tot $71.91 | 329 | $-12.17 | $20.81 |
| beijing (highest) | $28.44 tot $60.55 | 339 | $-14.58 | $13.86 |
| paris (lowest) | $33.51 tot $61.70 | 115 | $-21.49 | $12.02 |
| jeddah (highest) | $18.99 tot $38.29 | 126 | $-8.87 | $10.12 |
| manila (highest) | $19.12 tot $37.95 | 162 | $-9.31 | $9.81 |
| wuhan (highest) | $31.55 tot $67.23 | 282 | $-21.96 | $9.59 |
| kuala-lumpur (highest) | $24.55 tot $47.13 | 232 | $-15.10 | $9.46 |
| karachi (highest) | $24.12 tot $46.54 | 158 | $-15.20 | $8.92 |
| austin (highest) | $47.55 tot $98.72 | 491 | $-38.88 | $8.67 |
| milan (highest) | $36.18 tot $73.53 | 456 | $-27.78 | $8.40 |
| tokyo (highest) | $28.87 tot $63.52 | 501 | $-20.76 | $8.11 |
| shenzhen (highest) | $23.71 tot $49.95 | 417 | $-16.47 | $7.24 |
| mexico-city (highest) | $30.26 tot $58.19 | 183 | $-23.70 | $6.56 |
| munich (highest) | $37.23 tot $77.92 | 545 | $-31.14 | $6.09 |
| singapore (highest) | $33.94 tot $72.74 | 438 | $-27.94 | $6.00 |
| chongqing (highest) | $34.94 tot $72.59 | 286 | $-29.19 | $5.75 |
| shanghai (lowest) | $11.87 tot $21.74 | 41 | $-7.06 | $4.81 |
| shanghai (highest) | $33.25 tot $72.37 | 591 | $-29.41 | $3.84 |
| sao-paulo (highest) | $26.92 tot $53.62 | 314 | $-23.52 | $3.40 |
| los-angeles (highest) | $30.62 tot $68.21 | 594 | $-28.70 | $1.92 |
| houston (highest) | $50.94 tot $106 | 733 | $-49.02 | $1.92 |
| london (highest) | $42.06 tot $91.28 | 797 | $-41.07 | $0.99 |
| nyc (lowest) | $13.19 tot $22.45 | 88 | $-13.22 | $-0.03 |
| seoul (lowest) | $20.14 tot $37.89 | 110 | $-21.80 | $-1.66 |
| nyc (highest) | $49.93 tot $105 | 907 | $-52.06 | $-2.14 |
| moscow (highest) | $24.61 tot $49.23 | 242 | $-27.55 | $-2.94 |
| buenos-aires (highest) | $26.13 tot $49.90 | 325 | $-30.51 | $-4.38 |
| tokyo (lowest) | $13.41 tot $22.80 | 65 | $-19.69 | $-6.28 |
| lucknow (highest) | $40.06 tot $82.67 | 352 | $-50.66 | $-10.61 |
| ankara (highest) | $28.28 tot $54.92 | 427 | $-38.93 | $-10.65 |
| qingdao (highest) | $21.69 tot $43.23 | 252 | $-35.35 | $-13.65 |
| amsterdam (highest) | $34.12 tot $74.54 | 629 | $-49.19 | $-15.07 |
| taipei (highest) | $27.41 tot $50.75 | 308 | $-43.09 | $-15.68 |
| chicago (highest) | $43.26 tot $80.62 | 625 | $-59.29 | $-16.04 |
| tel-aviv (highest) | $41.57 tot $89.25 | 350 | $-57.83 | $-16.26 |
| guangzhou (highest) | $39.69 tot $80.95 | 544 | $-56.54 | $-16.85 |
| hong-kong (lowest) | $8.26 tot $14.66 | 134 | $-27.75 | $-19.49 |
| madrid (highest) | $34.62 tot $76.47 | 503 | $-55.83 | $-21.21 |
| miami (highest) | $42.84 tot $89.57 | 590 | $-65.73 | $-22.88 |
| san-francisco (highest) | $31.97 tot $62.16 | 406 | $-57.03 | $-25.06 |
| atlanta (highest) | $47.32 tot $100 | 901 | $-85.28 | $-37.96 |
| hong-kong (highest) | $29.38 tot $62.35 | 765 | $-67.70 | $-38.32 |
| toronto (highest) | $24.81 tot $48.82 | 450 | $-65.68 | $-40.87 |
| busan (highest) | $34.52 tot $72.99 | 476 | $-79.50 | $-44.98 |
| helsinki (highest) | $49.82 tot $102 | 661 | $-102 | $-52.50 |
| wellington (highest) | $30.86 tot $67.41 | 471 | $-87.72 | $-56.86 |
| dallas (highest) | $43.77 tot $92.45 | 605 | $-105 | $-60.81 |
| paris (highest) | $47.16 tot $102 | 844 | $-109 | $-62.13 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
