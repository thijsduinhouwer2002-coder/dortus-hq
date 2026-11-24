# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.16 tot $2.00 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 21 runs, 7053 minuten (117.5 uur) (GEZIEN). Markten in de data: 3397. Uitslag bekend voor 2233 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-445 (4783 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $25.96 (3119 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-65.25 (298 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 464 | 152 | $2,851 | $7,722 | $85.69 tot $176 | 1191 / 837 | $4,312 | $-101 (230 nog zonder prijs) | $0.00 (0 van 1191 beslist) | $-15.23 tot $75.45 |
| **Totaal** | 7053 | | $3,950 | $10,171 | $1,740 tot $3,560 | 22319 / 16203 | $72,052 | $-2,102 | $-1,353 | $-362 tot $1,458 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,569 over 22265 vullingen en $71,885, dus -2.18% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.99% over $70,344 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.84%.

**Opgeschaald (GOK):** per dag $-84.34 (ondergrens) tot $287 (hoge schatting) netto (gemeten minuten × 1440 / 7053).

529 van de 22319 vullingen ($1,708) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.99%): $-51.03 (GOK).

Geld dat de bot nodig had: gemiddeld $3,950 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,121**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,075 tot $3,662 |
| €5,000 | $5,000 | $-2,687 tot $9,156 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,353 over 15261 vullingen en $49,169, dus -2.75% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.11% per dollar over 21416 vullingen, 1 uur later -2.92% over 20923 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.81% per dollar over 849 vullingen, 1 uur later -4.60% over 835 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-63.85 (965 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-188 (588 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $11.10 (95 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 464 | 152 | $2,818 | $3,568 | $22.30 tot $57.76 | 267 / 152 | $1,157 | $-14.47 (58 nog zonder prijs) | $0.00 (0 van 267 beslist) | $7.82 tot $43.29 |
| **Totaal** | 7053 | | $3,884 | $4,020 | $431 tot $1,129 | 4500 / 2913 | $16,772 | $-407 | $-181 | $24.07 tot $722 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-393 over 4484 vullingen en $16,709, dus -2.35% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.49% over $16,352 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.57%.

**Opgeschaald (GOK):** per dag $2.78 (ondergrens) tot $145 (hoge schatting) netto (gemeten minuten × 1440 / 7053).

126 van de 4500 vullingen ($420) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.49%): $-10.45 (GOK).

Geld dat de bot nodig had: gemiddeld $3,884 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,904**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $63.32 tot $3,307 |
| €5,000 | $5,000 | $158 tot $8,268 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-181 over 2889 vullingen en $10,611, dus -1.70% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.35% per dollar over 4264 vullingen, 1 uur later -2.53% over 4147 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.34% per dollar over 220 vullingen, 1 uur later -1.35% over 217 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1368 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.53 tot $3.10 | $-0.58 tot $1.00 | 2 | $23.10 tot $36.16 | $-14.20 tot $-1.15 |
| €150 | 2 | $3.05 tot $6.21 | $-1.16 tot $2.00 | 3 | $33.50 tot $46.93 | $-3.56 tot $9.88 |
| €200 | 3 | $4.58 tot $9.31 | $-1.73 tot $3.00 | 4 | $42.42 tot $63.51 | $-9.54 tot $11.56 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.99%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

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
| highest toronto-on-november-23 12°C | 1200 | $2.93 tot $5.19 | 44 | $-18.45 | $21.60 |
| highest tel-aviv-on-november-25 24°C | 906 | $2.88 tot $5.90 | 21 | $-17.98 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $28.93 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $-14.69 |
| ... | | | | | |
| highest ankara-on-november-24 11°C | 1121 | $1.60 tot $3.18 | 36 | $7.26 | $0.00 |
| highest nyc-on-november-25 48-49°F | 308 | $2.54 tot $3.12 | 20 | $7.10 | $0.00 |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $0.00 |
| highest warsaw-on-november-25 6°C or higher | 1274 | $0.89 tot $2.09 | 9 | $19.63 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $39.65 tot $83.71 | 384 | $-6.30 | $33.36 |
| miami (lowest) | $43.27 tot $75.10 | 106 | $-13.04 | $30.23 |
| seoul (highest) | $34.51 tot $73.15 | 632 | $-5.36 | $29.15 |
| london (lowest) | $31.50 tot $57.44 | 183 | $-7.80 | $23.70 |
| chengdu (highest) | $34.14 tot $74.70 | 336 | $-12.39 | $21.75 |
| beijing (highest) | $29.69 tot $63.02 | 361 | $-16.97 | $12.72 |
| wuhan (highest) | $33.33 tot $70.90 | 288 | $-20.85 | $12.48 |
| paris (lowest) | $34.94 tot $64.74 | 117 | $-22.99 | $11.95 |
| manila (highest) | $20.57 tot $41.10 | 170 | $-9.74 | $10.83 |
| jeddah (highest) | $19.40 tot $39.10 | 136 | $-8.92 | $10.48 |
| karachi (highest) | $25.26 tot $49.14 | 162 | $-14.82 | $10.44 |
| tokyo (highest) | $29.63 tot $65.37 | 521 | $-19.60 | $10.02 |
| kuala-lumpur (highest) | $25.47 tot $48.98 | 243 | $-15.52 | $9.95 |
| austin (highest) | $48.64 tot $101 | 505 | $-38.99 | $9.65 |
| nyc (highest) | $52.36 tot $108 | 926 | $-44.54 | $7.82 |
| singapore (highest) | $35.49 tot $75.99 | 458 | $-28.05 | $7.43 |
| munich (highest) | $38.33 tot $80.45 | 558 | $-30.92 | $7.41 |
| mexico-city (highest) | $31.34 tot $60.31 | 185 | $-24.07 | $7.27 |
| chongqing (highest) | $36.63 tot $76.10 | 297 | $-31.46 | $5.17 |
| shanghai (lowest) | $11.87 tot $21.74 | 41 | $-7.06 | $4.81 |
| shenzhen (highest) | $25.39 tot $53.32 | 437 | $-22.08 | $3.31 |
| milan (highest) | $37.73 tot $76.78 | 494 | $-34.62 | $3.11 |
| london (highest) | $43.13 tot $93.81 | 820 | $-40.72 | $2.40 |
| sao-paulo (highest) | $28.76 tot $57.24 | 329 | $-27.90 | $0.86 |
| nyc (lowest) | $13.19 tot $22.45 | 88 | $-13.22 | $-0.03 |
| houston (highest) | $54.12 tot $111 | 786 | $-54.46 | $-0.34 |
| seoul (lowest) | $21.27 tot $40.10 | 116 | $-21.66 | $-0.39 |
| buenos-aires (highest) | $26.55 tot $51.01 | 342 | $-28.77 | $-2.22 |
| moscow (highest) | $25.20 tot $50.58 | 260 | $-29.21 | $-4.00 |
| los-angeles (highest) | $34.07 tot $75.36 | 647 | $-38.41 | $-4.33 |
| shanghai (highest) | $35.05 tot $75.92 | 646 | $-40.00 | $-4.95 |
| tokyo (lowest) | $13.41 tot $22.80 | 65 | $-19.69 | $-6.28 |
| lucknow (highest) | $40.92 tot $84.73 | 365 | $-50.83 | $-9.91 |
| ankara (highest) | $28.80 tot $56.04 | 437 | $-40.09 | $-11.30 |
| qingdao (highest) | $22.49 tot $44.78 | 265 | $-35.48 | $-13.00 |
| chicago (highest) | $45.18 tot $84.33 | 647 | $-59.01 | $-13.84 |
| taipei (highest) | $28.42 tot $52.60 | 322 | $-42.65 | $-14.23 |
| amsterdam (highest) | $35.37 tot $77.24 | 645 | $-53.70 | $-18.34 |
| hong-kong (lowest) | $8.26 tot $14.66 | 134 | $-27.75 | $-19.49 |
| madrid (highest) | $35.65 tot $78.84 | 516 | $-55.60 | $-19.95 |
| guangzhou (highest) | $41.79 tot $84.99 | 575 | $-62.96 | $-21.17 |
| miami (highest) | $45.10 tot $94.59 | 629 | $-67.53 | $-22.43 |
| san-francisco (highest) | $32.86 tot $63.93 | 426 | $-57.09 | $-24.23 |
| tel-aviv (highest) | $42.82 tot $91.98 | 360 | $-69.67 | $-26.85 |
| atlanta (highest) | $48.51 tot $103 | 913 | $-85.39 | $-36.88 |
| toronto (highest) | $25.22 tot $49.62 | 461 | $-65.89 | $-40.68 |
| busan (highest) | $35.51 tot $75.27 | 484 | $-79.09 | $-43.57 |
| helsinki (highest) | $51.13 tot $105 | 699 | $-104 | $-52.76 |
| wellington (highest) | $32.05 tot $70.20 | 492 | $-86.95 | $-54.90 |
| hong-kong (highest) | $31.14 tot $65.77 | 817 | $-88.98 | $-57.83 |
| dallas (highest) | $46.14 tot $97.28 | 626 | $-107 | $-60.93 |
| paris (highest) | $48.42 tot $105 | 867 | $-112 | $-63.51 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
