# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.68 tot $1.74 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 33 runs, 11083 minuten (184.7 uur) (GEZIEN). Markten in de data: 4563. Uitslag bekend voor 3732 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-243 (4847 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $-179 (4210 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $-462 (2722 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 1435 | 205 | $3,842 | $9,065 | $377 tot $805 | 5217 / 3336 | $19,178 | $-654 (32 nog zonder prijs) | $4.19 (5 van 5217 beslist) | $-277 tot $151 |
| 2026-11-27 | 192 | 192 | $3,419 | $8,713 | $40.49 tot $87.20 | 638 / 421 | $2,355 | $-68.52 (157 nog zonder prijs) | $0.00 (0 van 638 beslist) | $-28.03 tot $18.67 |
| **Totaal** | 11083 | | $3,783 | $10,171 | $2,841 tot $5,887 | 36507 / 25466 | $122,374 | $-3,535 | $-2,555 | $-694 tot $2,352 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-2,778 over 36446 vullingen en $122,191, dus -2.27% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.92% over $120,875 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.83%.

**Opgeschaald (GOK):** per dag $-95.85 (ondergrens) tot $300 (hoge schatting) netto (gemeten minuten × 1440 / 11083).

562 van de 36507 vullingen ($1,499) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.92%): $-43.83 (GOK).

Geld dat de bot nodig had: gemiddeld $3,783 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,954**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,236 tot $3,869 |
| €5,000 | $5,000 | $-3,091 tot $9,673 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-2,555 over 28065 vullingen en $91,633, dus -2.79% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.19% per dollar over 34720 vullingen, 1 uur later -2.84% over 34203 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.85% per dollar over 1726 vullingen, 1 uur later -4.44% over 1690 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $111 (1159 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $415 (966 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $-260 (564 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 1435 | 205 | $3,808 | $4,844 | $92.00 tot $246 | 1183 / 787 | $4,920 | $-147 (6 nog zonder prijs) | $6.80 (1 van 1183 beslist) | $-54.54 tot $99.60 |
| 2026-11-27 | 192 | 192 | $3,541 | $4,600 | $9.25 tot $25.76 | 148 / 109 | $626 | $-11.17 (23 nog zonder prijs) | $0.00 (0 van 148 beslist) | $-1.92 tot $14.59 |
| **Totaal** | 11083 | | $3,731 | $4,844 | $693 tot $1,838 | 7741 / 5036 | $30,166 | $-694 | $-16.67 | $-1.13 tot $1,144 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-819 over 7723 vullingen en $30,088, dus -2.72% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.32% over $29,873 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.48%.

**Opgeschaald (GOK):** per dag $-1.03 (ondergrens) tot $148 (hoge schatting) netto (gemeten minuten × 1440 / 11083).

112 van de 7741 vullingen ($294) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.32%): $-6.82 (GOK).

Geld dat de bot nodig had: gemiddeld $3,731 in open orders plus de hoogste stand van $4,844 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,575**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-21.68 tot $3,101 |
| €5,000 | $5,000 | $-54.20 tot $7,751 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-16.67 over 5764 vullingen en $22,061, dus -0.08% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.69% per dollar over 7255 vullingen, 1 uur later -2.21% over 7152 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.13% per dollar over 468 vullingen, 1 uur later -3.86% over 462 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 2042 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.60 tot $3.31 | $-0.84 tot $0.87 | 2 | $38.50 tot $73.23 | $-11.60 tot $23.13 |
| €150 | 2 | $3.19 tot $6.62 | $-1.68 tot $1.74 | 3 | $51.48 tot $100 | $-49.79 tot $-1.16 |
| €200 | 3 | $4.79 tot $9.93 | $-2.52 tot $2.62 | 4 | $61.17 tot $117 | $-37.86 tot $17.76 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.92%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest paris-on-november-26 6°C | 2083 | $8.96 tot $20.03 | 90 | $-34.19 | $-52.26 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $-29.11 |
| highest paris-on-november-26 7°C | 1536 | $7.12 tot $16.89 | 84 | $-26.57 | $5.42 |
| highest austin-on-november-27 68-69°F | 1266 | $3.45 tot $6.96 | 65 | $-22.43 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest madrid-on-november-27 14°C or higher | 2080 | $2.80 tot $5.46 | 66 | $-19.43 | $0.00 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $24.65 |
| ... | | | | | |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest nyc-on-november-28 54-55°F | 864 | $3.49 tot $5.82 | 4 | $8.69 | $0.00 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest nyc-on-november-26 58-59°F | 6461 | $14.00 tot $24.94 | 66 | $13.88 | $0.00 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $63.08 tot $126 | 491 | $75.06 | $138 |
| seoul (highest) | $74.36 tot $164 | 1082 | $-24.66 | $49.70 |
| chengdu (highest) | $56.58 tot $124 | 614 | $-20.13 | $36.45 |
| miami (lowest) | $53.81 tot $93.82 | 147 | $-19.30 | $34.51 |
| london (lowest) | $49.63 tot $91.01 | 289 | $-22.10 | $27.53 |
| munich (highest) | $73.69 tot $163 | 1003 | $-46.43 | $27.27 |
| paris (lowest) | $55.04 tot $102 | 227 | $-34.32 | $20.72 |
| manila (highest) | $30.41 tot $61.87 | 303 | $-19.46 | $10.94 |
| wuhan (highest) | $54.36 tot $116 | 519 | $-43.46 | $10.91 |
| shanghai (lowest) | $18.70 tot $35.56 | 82 | $-9.31 | $9.39 |
| nyc (highest) | $85.97 tot $171 | 1076 | $-77.14 | $8.83 |
| beijing (highest) | $45.03 tot $98.14 | 663 | $-37.41 | $7.62 |
| singapore (highest) | $51.75 tot $112 | 696 | $-44.21 | $7.54 |
| tokyo (highest) | $62.39 tot $142 | 971 | $-55.58 | $6.80 |
| buenos-aires (highest) | $64.60 tot $140 | 728 | $-59.06 | $5.54 |
| sao-paulo (highest) | $39.87 tot $79.49 | 463 | $-35.02 | $4.85 |
| shenzhen (highest) | $41.49 tot $88.19 | 688 | $-36.96 | $4.53 |
| karachi (highest) | $36.69 tot $73.01 | 305 | $-32.85 | $3.84 |
| jeddah (highest) | $28.80 tot $58.34 | 220 | $-25.00 | $3.80 |
| kuala-lumpur (highest) | $35.70 tot $69.79 | 413 | $-32.71 | $2.99 |
| nyc (lowest) | $28.29 tot $49.10 | 204 | $-27.69 | $0.60 |
| milan (highest) | $61.02 tot $125 | 813 | $-62.10 | $-1.08 |
| chongqing (highest) | $55.37 tot $116 | 504 | $-57.04 | $-1.67 |
| london (highest) | $67.70 tot $147 | 1410 | $-71.28 | $-3.58 |
| seoul (lowest) | $34.52 tot $65.25 | 208 | $-38.50 | $-3.98 |
| taipei (highest) | $41.86 tot $78.12 | 442 | $-47.12 | $-5.26 |
| los-angeles (highest) | $59.23 tot $129 | 998 | $-64.75 | $-5.53 |
| mexico-city (highest) | $46.66 tot $90.51 | 413 | $-52.89 | $-6.23 |
| tokyo (lowest) | $19.70 tot $35.45 | 89 | $-26.13 | $-6.43 |
| qingdao (highest) | $31.52 tot $63.15 | 409 | $-41.92 | $-10.40 |
| ankara (highest) | $40.54 tot $79.48 | 593 | $-56.14 | $-15.60 |
| chicago (highest) | $59.79 tot $113 | 940 | $-77.44 | $-17.65 |
| miami (highest) | $68.38 tot $144 | 1022 | $-90.92 | $-22.54 |
| shanghai (highest) | $55.70 tot $120 | 1036 | $-82.43 | $-26.73 |
| moscow (highest) | $39.16 tot $78.48 | 488 | $-66.00 | $-26.84 |
| houston (highest) | $81.81 tot $169 | 1209 | $-109 | $-27.32 |
| guangzhou (highest) | $57.23 tot $119 | 800 | $-85.87 | $-28.64 |
| austin (highest) | $73.00 tot $151 | 935 | $-105 | $-31.95 |
| tel-aviv (highest) | $69.77 tot $148 | 603 | $-102 | $-32.54 |
| madrid (highest) | $60.83 tot $132 | 910 | $-96.18 | $-35.34 |
| amsterdam (highest) | $58.59 tot $126 | 984 | $-94.04 | $-35.45 |
| lucknow (highest) | $63.81 tot $131 | 697 | $-103 | $-39.25 |
| hong-kong (lowest) | $47.26 tot $100 | 484 | $-90.31 | $-43.05 |
| san-francisco (highest) | $45.50 tot $88.61 | 671 | $-94.06 | $-48.56 |
| busan (highest) | $82.84 tot $179 | 872 | $-138 | $-55.24 |
| hong-kong (highest) | $44.23 tot $94.42 | 1122 | $-102 | $-58.09 |
| helsinki (highest) | $86.46 tot $176 | 1144 | $-150 | $-63.46 |
| toronto (highest) | $35.30 tot $71.14 | 620 | $-109 | $-73.45 |
| dallas (highest) | $71.75 tot $152 | 1069 | $-155 | $-83.18 |
| wellington (highest) | $52.33 tot $114 | 840 | $-142 | $-89.75 |
| atlanta (highest) | $71.88 tot $152 | 1363 | $-163 | $-91.19 |
| paris (highest) | $107 tot $239 | 1635 | $-233 | $-126 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
