# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.92 tot $1.61 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 31 runs, 10411 minuten (173.5 uur) (GEZIEN). Markten in de data: 4563. Uitslag bekend voor 3401 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-243 (4847 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $200 (3459 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $67.37 (573 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 955 | 203 | $3,800 | $8,241 | $250 tot $536 | 3515 / 2259 | $12,875 | $-385 (250 nog zonder prijs) | $0.00 (0 van 3515 beslist) | $-135 tot $151 |
| **Totaal** | 10411 | | $3,783 | $10,171 | $2,673 tot $5,531 | 34167 / 23968 | $113,717 | $-3,196 | $-1,650 | $-524 tot $2,334 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-2,527 over 34092 vullingen en $113,482, dus -2.23% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.85% over $111,961 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.75%.

**Opgeschaald (GOK):** per dag $-79.38 (ondergrens) tot $316 (hoge schatting) netto (gemeten minuten × 1440 / 10411).

623 van de 34167 vullingen ($1,755) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.85%): $-50.11 (GOK).

Geld dat de bot nodig had: gemiddeld $3,783 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,954**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,024 tot $4,075 |
| €5,000 | $5,000 | $-2,560 tot $10,188 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,650 over 25160 vullingen en $81,715, dus -2.02% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.14% per dollar over 32495 vullingen, 1 uur later -2.78% over 31935 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.92% per dollar over 1597 vullingen, 1 uur later -4.28% over 1562 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $111 (1159 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $432 (761 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $-41.82 (126 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 955 | 203 | $3,764 | $4,313 | $62.29 tot $164 | 784 / 520 | $3,236 | $-85.05 (41 nog zonder prijs) | $0.00 (0 van 784 beslist) | $-22.77 tot $79.20 |
| **Totaal** | 10411 | | $3,727 | $4,313 | $654 tot $1,730 | 7194 / 4660 | $27,856 | $-621 | $212 | $32.56 tot $1,109 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-709 over 7173 vullingen en $27,765, dus -2.55% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.26% over $27,478 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.37%.

**Opgeschaald (GOK):** per dag $3.32 (ondergrens) tot $152 (hoge schatting) netto (gemeten minuten × 1440 / 10411).

124 van de 7194 vullingen ($377) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.26%): $-8.53 (GOK).

Geld dat de bot nodig had: gemiddeld $3,727 in open orders plus de hoogste stand van $4,313 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,040**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $74.42 tot $3,407 |
| €5,000 | $5,000 | $186 tot $8,517 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $212 over 5120 vullingen en $19,387, dus +1.10% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.53% per dollar over 6732 vullingen, 1 uur later -2.16% over 6624 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.93% per dollar over 441 vullingen, 1 uur later -3.66% over 433 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1968 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.64 tot $3.41 | $-0.96 tot $0.81 | 2 | $37.72 tot $72.35 | $2.50 tot $37.13 |
| €150 | 2 | $3.29 tot $6.81 | $-1.92 tot $1.61 | 3 | $51.23 tot $98.38 | $-0.07 tot $47.08 |
| €200 | 3 | $4.93 tot $10.22 | $-2.88 tot $2.42 | 4 | $64.21 tot $125 | $-38.27 tot $22.79 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.85%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest paris-on-november-26 6°C | 2083 | $8.96 tot $20.03 | 90 | $-34.19 | $0.00 |
| highest austin-on-november-27 68-69°F | 594 | $2.64 tot $5.10 | 38 | $-24.24 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $-29.11 |
| highest paris-on-november-26 7°C | 1536 | $7.12 tot $16.89 | 84 | $-26.57 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $24.65 |
| highest atlanta-on-november-26 48-49°F | 1419 | $2.93 tot $5.80 | 49 | $-18.70 | $0.00 |
| ... | | | | | |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest nyc-on-november-26 58-59°F | 6461 | $14.00 tot $24.94 | 66 | $13.88 | $0.00 |
| highest nyc-on-november-27 58-59°F | 1160 | $4.57 tot $8.98 | 13 | $24.64 | $0.00 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $57.21 tot $116 | 461 | $91.16 | $148 |
| seoul (highest) | $73.18 tot $161 | 1035 | $-25.85 | $47.33 |
| nyc (highest) | $78.07 tot $156 | 1048 | $-39.90 | $38.17 |
| chengdu (highest) | $53.15 tot $116 | 564 | $-15.03 | $38.12 |
| miami (lowest) | $52.96 tot $92.30 | 143 | $-18.51 | $34.45 |
| london (lowest) | $45.98 tot $84.10 | 251 | $-15.24 | $30.74 |
| munich (highest) | $72.39 tot $159 | 974 | $-47.41 | $24.99 |
| beijing (highest) | $42.84 tot $93.08 | 593 | $-19.15 | $23.69 |
| paris (lowest) | $51.01 tot $94.36 | 209 | $-29.27 | $21.74 |
| wuhan (highest) | $51.45 tot $110 | 477 | $-39.61 | $11.84 |
| manila (highest) | $29.27 tot $59.42 | 296 | $-17.68 | $11.59 |
| buenos-aires (highest) | $55.12 tot $118 | 636 | $-44.03 | $11.09 |
| jeddah (highest) | $27.22 tot $54.83 | 206 | $-19.30 | $7.92 |
| karachi (highest) | $34.96 tot $69.60 | 278 | $-27.19 | $7.77 |
| shanghai (lowest) | $17.09 tot $32.26 | 80 | $-9.32 | $7.77 |
| singapore (highest) | $49.53 tot $107 | 650 | $-42.33 | $7.20 |
| tokyo (highest) | $59.74 tot $136 | 918 | $-53.57 | $6.17 |
| chongqing (highest) | $53.35 tot $112 | 475 | $-47.85 | $5.50 |
| shenzhen (highest) | $38.55 tot $82.11 | 656 | $-33.49 | $5.05 |
| kuala-lumpur (highest) | $34.00 tot $66.26 | 385 | $-30.39 | $3.61 |
| sao-paulo (highest) | $38.24 tot $76.10 | 442 | $-35.60 | $2.64 |
| nyc (lowest) | $24.97 tot $42.68 | 183 | $-23.68 | $1.29 |
| milan (highest) | $56.92 tot $117 | 770 | $-58.13 | $-1.21 |
| mexico-city (highest) | $43.43 tot $84.60 | 366 | $-46.58 | $-3.16 |
| seoul (lowest) | $32.80 tot $61.77 | 199 | $-36.96 | $-4.16 |
| taipei (highest) | $40.00 tot $74.55 | 407 | $-45.62 | $-5.62 |
| tokyo (lowest) | $18.19 tot $32.49 | 80 | $-23.84 | $-5.65 |
| los-angeles (highest) | $55.22 tot $120 | 951 | $-61.62 | $-6.40 |
| moscow (highest) | $35.54 tot $71.50 | 439 | $-43.97 | $-8.43 |
| qingdao (highest) | $29.90 tot $59.74 | 368 | $-38.70 | $-8.80 |
| london (highest) | $63.03 tot $137 | 1257 | $-71.84 | $-8.81 |
| ankara (highest) | $38.14 tot $74.65 | 568 | $-50.11 | $-11.96 |
| miami (highest) | $64.36 tot $135 | 949 | $-81.92 | $-17.56 |
| chicago (highest) | $56.69 tot $107 | 888 | $-75.87 | $-19.18 |
| shanghai (highest) | $53.68 tot $116 | 1003 | $-76.48 | $-22.80 |
| tel-aviv (highest) | $65.77 tot $140 | 559 | $-92.51 | $-26.74 |
| guangzhou (highest) | $55.92 tot $116 | 778 | $-82.91 | $-26.99 |
| madrid (highest) | $58.08 tot $125 | 844 | $-87.49 | $-29.41 |
| austin (highest) | $68.06 tot $141 | 851 | $-97.50 | $-29.44 |
| houston (highest) | $77.44 tot $159 | 1153 | $-109 | $-31.32 |
| amsterdam (highest) | $54.87 tot $118 | 920 | $-86.68 | $-31.81 |
| hong-kong (lowest) | $42.40 tot $89.43 | 459 | $-79.38 | $-36.98 |
| lucknow (highest) | $60.75 tot $125 | 662 | $-99.40 | $-38.65 |
| san-francisco (highest) | $43.77 tot $85.19 | 648 | $-92.56 | $-48.79 |
| busan (highest) | $80.01 tot $171 | 844 | $-133 | $-52.64 |
| hong-kong (highest) | $43.04 tot $91.76 | 1102 | $-104 | $-61.03 |
| helsinki (highest) | $79.27 tot $161 | 1087 | $-142 | $-62.65 |
| dallas (highest) | $65.01 tot $138 | 943 | $-134 | $-69.35 |
| toronto (highest) | $32.87 tot $66.03 | 602 | $-107 | $-74.42 |
| atlanta (highest) | $66.90 tot $141 | 1266 | $-153 | $-85.62 |
| wellington (highest) | $49.63 tot $108 | 789 | $-136 | $-86.70 |
| paris (highest) | $101 tot $224 | 1455 | $-205 | $-105 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
