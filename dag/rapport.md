# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.24 tot $2.35 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 28 runs, 9403 minuten (156.7 uur) (GEZIEN). Markten in de data: 4016. Uitslag bekend voor 3080 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-42.82 (4398 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $86.97 (1634 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1380 | 181 | $3,384 | $8,264 | $456 tot $964 | 5073 / 3236 | $17,943 | $-511 (187 nog zonder prijs) | $0.00 (0 van 5073 beslist) | $-54.71 tot $453 |
| **Totaal** | 9403 | | $3,783 | $10,171 | $2,411 tot $4,969 | 30508 / 21619 | $100,349 | $-2,809 | $-1,630 | $-398 tot $2,160 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-2,183 over 30450 vullingen en $100,185, dus -2.18% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.84% over $98,950 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.69%.

**Opgeschaald (GOK):** per dag $-67.09 (ondergrens) tot $325 (hoge schatting) netto (gemeten minuten × 1440 / 9403).

521 van de 30508 vullingen ($1,400) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.84%): $-39.73 (GOK).

Geld dat de bot nodig had: gemiddeld $3,783 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,954**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-865 tot $4,188 |
| €5,000 | $5,000 | $-2,164 tot $10,469 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,630 over 22313 vullingen en $71,895, dus -2.27% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.08% per dollar over 29156 vullingen, 1 uur later -2.76% over 28671 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.21% per dollar over 1294 vullingen, 1 uur later -4.40% over 1274 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $213 (1049 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $117 (367 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1380 | 181 | $3,353 | $4,190 | $106 tot $287 | 1154 / 767 | $4,825 | $-108 (30 nog zonder prijs) | $0.00 (0 van 1154 beslist) | $-1.32 tot $180 |
| **Totaal** | 9403 | | $3,726 | $4,190 | $589 tot $1,558 | 6381 / 4119 | $24,518 | $-544 | $40.17 | $44.71 tot $1,014 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-601 over 6367 vullingen en $24,462, dus -2.46% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.24% over $24,244 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.22%.

**Opgeschaald (GOK):** per dag $5.91 (ondergrens) tot $154 (hoge schatting) netto (gemeten minuten × 1440 / 9403).

106 van de 6381 vullingen ($274) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.24%): $-6.14 (GOK).

Geld dat de bot nodig had: gemiddeld $3,726 in open orders plus de hoogste stand van $4,190 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,916**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $134 tot $3,509 |
| €5,000 | $5,000 | $336 tot $8,774 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $40.17 over 4490 vullingen en $16,803, dus +0.24% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.44% per dollar over 6014 vullingen, 1 uur later -2.19% over 5914 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.71% per dollar over 353 vullingen, 1 uur later -3.01% over 350 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1785 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.70 tot $3.49 | $-0.62 tot $1.17 | 2 | $39.69 tot $77.99 | $2.80 tot $41.10 |
| €150 | 2 | $3.39 tot $6.98 | $-1.24 tot $2.35 | 3 | $53.49 tot $107 | $11.79 tot $65.16 |
| €200 | 3 | $5.09 tot $10.47 | $-1.86 tot $3.52 | 5 | $73.55 tot $139 | $29.40 tot $95.31 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.84%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest paris-on-november-26 6°C | 2083 | $8.96 tot $20.03 | 90 | $-33.66 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $0.00 |
| highest paris-on-november-26 7°C | 1536 | $7.12 tot $16.89 | 84 | $-25.34 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $24.65 |
| highest hong-kong-on-november-24 22°C | 1464 | $4.44 tot $8.79 | 89 | $-20.19 | $61.12 |
| highest toronto-on-november-23 12°C | 1200 | $2.93 tot $5.19 | 44 | $-18.45 | $21.60 |
| ... | | | | | |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest nyc-on-november-26 56-57°F | 4997 | $11.09 tot $19.49 | 53 | $11.98 | $0.00 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $51.30 tot $105 | 441 | $90.62 | $142 |
| seoul (highest) | $61.72 tot $135 | 910 | $-21.97 | $39.76 |
| chengdu (highest) | $48.93 tot $107 | 504 | $-11.67 | $37.26 |
| london (lowest) | $41.32 tot $75.82 | 222 | $-6.11 | $35.20 |
| miami (lowest) | $52.17 tot $91.06 | 141 | $-19.49 | $32.68 |
| beijing (highest) | $38.69 tot $83.39 | 523 | $-9.29 | $29.40 |
| paris (lowest) | $47.28 tot $87.23 | 168 | $-29.66 | $17.62 |
| munich (highest) | $66.95 tot $146 | 884 | $-49.50 | $17.45 |
| tokyo (highest) | $50.63 tot $114 | 753 | $-33.24 | $17.39 |
| wuhan (highest) | $46.49 tot $98.78 | 428 | $-31.02 | $15.46 |
| chongqing (highest) | $48.18 tot $101 | 397 | $-35.17 | $13.01 |
| karachi (highest) | $32.51 tot $64.49 | 249 | $-21.45 | $11.06 |
| manila (highest) | $27.44 tot $55.28 | 267 | $-17.94 | $9.50 |
| nyc (highest) | $70.59 tot $142 | 1022 | $-61.22 | $9.37 |
| mexico-city (highest) | $38.55 tot $75.40 | 272 | $-30.30 | $8.25 |
| singapore (highest) | $44.92 tot $96.82 | 580 | $-38.34 | $6.58 |
| london (highest) | $57.70 tot $125 | 1083 | $-51.32 | $6.38 |
| jeddah (highest) | $25.06 tot $50.49 | 203 | $-19.51 | $5.56 |
| buenos-aires (highest) | $45.62 tot $95.55 | 547 | $-40.31 | $5.31 |
| shenzhen (highest) | $34.76 tot $73.69 | 601 | $-30.65 | $4.12 |
| austin (highest) | $60.52 tot $126 | 693 | $-56.81 | $3.71 |
| sao-paulo (highest) | $35.56 tot $70.69 | 400 | $-31.87 | $3.69 |
| nyc (lowest) | $16.30 tot $28.14 | 122 | $-13.04 | $3.26 |
| seoul (lowest) | $28.47 tot $53.33 | 169 | $-27.42 | $1.05 |
| shanghai (lowest) | $13.61 tot $25.29 | 62 | $-12.85 | $0.76 |
| kuala-lumpur (highest) | $31.67 tot $61.36 | 356 | $-31.10 | $0.56 |
| milan (highest) | $52.59 tot $107 | 724 | $-54.16 | $-1.57 |
| los-angeles (highest) | $47.93 tot $105 | 847 | $-50.58 | $-2.65 |
| qingdao (highest) | $27.58 tot $54.78 | 340 | $-35.43 | $-7.85 |
| tokyo (lowest) | $14.89 tot $25.85 | 69 | $-23.75 | $-8.86 |
| ankara (highest) | $36.16 tot $70.51 | 544 | $-47.23 | $-11.06 |
| taipei (highest) | $35.55 tot $66.74 | 381 | $-46.85 | $-11.30 |
| moscow (highest) | $32.70 tot $65.53 | 393 | $-44.35 | $-11.65 |
| houston (highest) | $71.24 tot $146 | 1033 | $-86.24 | $-14.99 |
| lucknow (highest) | $55.67 tot $114 | 603 | $-73.20 | $-17.54 |
| madrid (highest) | $52.76 tot $113 | 743 | $-72.59 | $-19.84 |
| shanghai (highest) | $46.97 tot $102 | 902 | $-66.83 | $-19.87 |
| chicago (highest) | $52.61 tot $98.61 | 818 | $-73.28 | $-20.67 |
| guangzhou (highest) | $52.05 tot $108 | 710 | $-74.03 | $-21.98 |
| miami (highest) | $59.69 tot $125 | 848 | $-86.69 | $-27.00 |
| amsterdam (highest) | $49.27 tot $106 | 844 | $-78.33 | $-29.06 |
| tel-aviv (highest) | $62.78 tot $134 | 518 | $-93.49 | $-30.72 |
| hong-kong (lowest) | $30.47 tot $61.39 | 342 | $-63.46 | $-32.99 |
| san-francisco (highest) | $39.61 tot $77.13 | 568 | $-78.51 | $-38.90 |
| busan (highest) | $73.94 tot $156 | 759 | $-121 | $-47.35 |
| helsinki (highest) | $73.29 tot $149 | 1020 | $-129 | $-56.10 |
| hong-kong (highest) | $40.35 tot $85.63 | 1016 | $-101 | $-60.71 |
| dallas (highest) | $59.18 tot $125 | 802 | $-122 | $-62.47 |
| atlanta (highest) | $60.84 tot $129 | 1136 | $-128 | $-67.33 |
| toronto (highest) | $30.09 tot $60.22 | 560 | $-97.72 | $-67.63 |
| wellington (highest) | $43.91 tot $96.11 | 672 | $-120 | $-76.34 |
| paris (highest) | $91.69 tot $203 | 1319 | $-200 | $-108 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
