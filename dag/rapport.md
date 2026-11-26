# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.41 tot $2.06 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 29 runs, 9739 minuten (162.3 uur) (GEZIEN). Markten in de data: 4016. Uitslag bekend voor 3213 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-143 (4714 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $176 (2519 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $5.94 (10 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 283 | 181 | $3,413 | $7,502 | $59.43 tot $128 | 828 / 536 | $2,770 | $-78.20 (120 nog zonder prijs) | $0.00 (0 van 828 beslist) | $-18.78 tot $49.57 |
| **Totaal** | 9739 | | $3,771 | $10,171 | $2,482 tot $5,122 | 31480 / 22245 | $103,612 | $-2,890 | $-1,636 | $-408 tot $2,232 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-2,271 over 31428 vullingen en $103,465, dus -2.19% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.82% over $102,331 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.69%.

**Opgeschaald (GOK):** per dag $-65.61 (ondergrens) tot $325 (hoge schatting) netto (gemeten minuten × 1440 / 9739).

493 van de 31480 vullingen ($1,281) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.82%): $-36.18 (GOK).

Geld dat de bot nodig had: gemiddeld $3,771 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,942**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-847 tot $4,193 |
| €5,000 | $5,000 | $-2,118 tot $10,482 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,636 over 23524 vullingen en $76,033, dus -2.15% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.10% per dollar over 30062 vullingen, 1 uur later -2.74% over 29603 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.25% per dollar over 1366 vullingen, 1 uur later -4.60% over 1342 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $129 (1128 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $204 (550 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $0.00 (0 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 283 | 181 | $3,354 | $4,021 | $12.94 tot $36.99 | 206 / 153 | $787 | $-26.16 (33 nog zonder prijs) | $0.00 (0 van 206 beslist) | $-13.22 tot $10.83 |
| **Totaal** | 9739 | | $3,713 | $4,190 | $604 tot $1,603 | 6616 / 4293 | $25,407 | $-562 | $43.63 | $42.11 tot $1,040 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-634 over 6602 vullingen en $25,351, dus -2.50% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.24% over $25,100 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.27%.

**Opgeschaald (GOK):** per dag $5.21 (ondergrens) tot $153 (hoge schatting) netto (gemeten minuten × 1440 / 9739).

116 van de 6616 vullingen ($308) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.24%): $-6.89 (GOK).

Geld dat de bot nodig had: gemiddeld $3,713 in open orders plus de hoogste stand van $4,190 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,903**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $119 tot $3,480 |
| €5,000 | $5,000 | $296 tot $8,701 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $43.63 over 4752 vullingen en $17,852, dus +0.24% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.47% per dollar over 6219 vullingen, 1 uur later -2.14% over 6112 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.02% per dollar over 383 vullingen, 1 uur later -3.73% over 377 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1811 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.63 tot $3.37 | $-0.71 tot $1.03 | 2 | $38.50 tot $73.23 | $-11.60 tot $23.13 |
| €150 | 2 | $3.26 tot $6.74 | $-1.41 tot $2.06 | 3 | $51.48 tot $100 | $-49.79 tot $-1.16 |
| €200 | 3 | $4.90 tot $10.11 | $-2.12 tot $3.09 | 4 | $61.17 tot $117 | $-37.86 tot $17.76 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.82%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest paris-on-november-26 6°C | 2083 | $8.96 tot $20.03 | 90 | $-34.19 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $0.00 |
| highest paris-on-november-26 7°C | 1536 | $7.12 tot $16.89 | 84 | $-26.57 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $24.65 |
| highest atlanta-on-november-26 48-49°F | 1403 | $2.86 tot $5.68 | 45 | $-19.14 | $0.00 |
| highest hong-kong-on-november-24 22°C | 1464 | $4.44 tot $8.79 | 89 | $-20.19 | $61.12 |
| ... | | | | | |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest nyc-on-november-26 56-57°F | 6410 | $13.90 tot $24.72 | 63 | $16.38 | $0.00 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $52.50 tot $107 | 449 | $97.56 | $150 |
| seoul (highest) | $62.94 tot $138 | 924 | $-22.05 | $40.88 |
| london (lowest) | $41.94 tot $77.13 | 228 | $-5.05 | $36.88 |
| chengdu (highest) | $50.01 tot $109 | 521 | $-14.21 | $35.80 |
| miami (lowest) | $52.90 tot $92.20 | 143 | $-18.01 | $34.90 |
| beijing (highest) | $39.51 tot $85.44 | 535 | $-9.93 | $29.58 |
| munich (highest) | $67.76 tot $148 | 903 | $-49.66 | $18.09 |
| tokyo (highest) | $51.41 tot $116 | 764 | $-33.59 | $17.81 |
| nyc (highest) | $74.40 tot $149 | 1032 | $-56.82 | $17.58 |
| paris (lowest) | $48.07 tot $88.78 | 182 | $-30.51 | $17.56 |
| wuhan (highest) | $48.05 tot $102 | 439 | $-33.26 | $14.79 |
| chongqing (highest) | $49.39 tot $103 | 404 | $-34.87 | $14.52 |
| karachi (highest) | $33.16 tot $65.89 | 253 | $-20.93 | $12.23 |
| buenos-aires (highest) | $51.19 tot $109 | 592 | $-39.58 | $11.61 |
| manila (highest) | $28.06 tot $56.65 | 276 | $-17.33 | $10.73 |
| singapore (highest) | $46.09 tot $99.51 | 597 | $-39.41 | $6.68 |
| jeddah (highest) | $25.92 tot $52.12 | 203 | $-19.31 | $6.61 |
| shenzhen (highest) | $35.68 tot $75.82 | 615 | $-31.22 | $4.45 |
| sao-paulo (highest) | $36.73 tot $73.08 | 418 | $-32.33 | $4.40 |
| london (highest) | $58.75 tot $127 | 1116 | $-54.83 | $3.91 |
| austin (highest) | $63.03 tot $131 | 739 | $-59.36 | $3.67 |
| mexico-city (highest) | $40.06 tot $78.25 | 298 | $-37.56 | $2.50 |
| nyc (lowest) | $18.62 tot $32.46 | 147 | $-16.67 | $1.95 |
| shanghai (lowest) | $14.31 tot $26.73 | 66 | $-12.85 | $1.46 |
| kuala-lumpur (highest) | $32.32 tot $62.77 | 360 | $-31.12 | $1.20 |
| seoul (lowest) | $29.33 tot $54.94 | 175 | $-30.62 | $-1.28 |
| los-angeles (highest) | $51.20 tot $112 | 882 | $-54.10 | $-2.90 |
| milan (highest) | $53.37 tot $109 | 731 | $-57.47 | $-4.11 |
| tokyo (lowest) | $15.46 tot $27.11 | 69 | $-23.75 | $-8.29 |
| qingdao (highest) | $28.40 tot $56.55 | 351 | $-38.30 | $-9.90 |
| ankara (highest) | $36.73 tot $71.75 | 546 | $-47.10 | $-10.38 |
| taipei (highest) | $36.28 tot $68.26 | 388 | $-47.13 | $-10.85 |
| moscow (highest) | $33.28 tot $66.81 | 400 | $-44.79 | $-11.50 |
| lucknow (highest) | $56.69 tot $116 | 612 | $-75.06 | $-18.37 |
| chicago (highest) | $53.84 tot $101 | 842 | $-73.25 | $-19.41 |
| shanghai (highest) | $48.20 tot $104 | 917 | $-69.23 | $-21.03 |
| guangzhou (highest) | $53.08 tot $110 | 727 | $-74.49 | $-21.41 |
| houston (highest) | $74.31 tot $152 | 1087 | $-96.36 | $-22.05 |
| miami (highest) | $61.76 tot $130 | 898 | $-84.30 | $-22.54 |
| madrid (highest) | $54.71 tot $117 | 791 | $-80.22 | $-25.51 |
| amsterdam (highest) | $50.70 tot $109 | 867 | $-78.02 | $-27.32 |
| tel-aviv (highest) | $63.58 tot $135 | 519 | $-93.34 | $-29.76 |
| san-francisco (highest) | $41.03 tot $79.84 | 596 | $-84.72 | $-43.70 |
| hong-kong (lowest) | $31.75 tot $64.98 | 357 | $-77.02 | $-45.27 |
| busan (highest) | $74.89 tot $159 | 771 | $-121 | $-46.35 |
| helsinki (highest) | $74.55 tot $151 | 1030 | $-129 | $-54.88 |
| dallas (highest) | $62.08 tot $131 | 879 | $-120 | $-58.39 |
| hong-kong (highest) | $41.04 tot $87.30 | 1049 | $-100 | $-59.03 |
| toronto (highest) | $31.30 tot $62.71 | 573 | $-103 | $-71.62 |
| wellington (highest) | $45.10 tot $98.64 | 692 | $-123 | $-77.99 |
| atlanta (highest) | $64.08 tot $135 | 1183 | $-146 | $-81.60 |
| paris (highest) | $92.81 tot $206 | 1344 | $-195 | $-102 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
