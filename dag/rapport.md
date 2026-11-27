# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.46 tot $2.06 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 36 runs, 12091 minuten (201.5 uur) (GEZIEN). Markten in de data: 5107. Uitslag bekend voor 4118 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-243 (4847 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $-255 (4307 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $-900 (4508 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 1435 | 205 | $3,842 | $9,065 | $377 tot $805 | 5217 / 3336 | $19,178 | $-654 (32 nog zonder prijs) | $-68.77 (1104 van 5217 beslist) | $-277 tot $151 |
| 2026-11-27 | 1200 | 212 | $3,948 | $9,973 | $335 tot $708 | 4318 / 2760 | $16,095 | $-473 (169 nog zonder prijs) | $0.00 (0 van 4318 beslist) | $-137 tot $235 |
| **Totaal** | 12091 | | $3,805 | $10,171 | $3,135 tot $6,507 | 40187 / 27805 | $136,114 | $-3,939 | $-3,141 | $-803 tot $2,569 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-3,165 over 40115 vullingen en $135,897, dus -2.33% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.93% over $134,654 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.89%.

**Opgeschaald (GOK):** per dag $-101 (ondergrens) tot $301 (hoge schatting) netto (gemeten minuten × 1440 / 12091).

574 van de 40187 vullingen ($1,460) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.93%): $-42.71 (GOK).

Geld dat de bot nodig had: gemiddeld $3,805 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,976**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,298 tot $3,874 |
| €5,000 | $5,000 | $-3,244 tot $9,686 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-3,141 over 31047 vullingen en $102,482, dus -3.07% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.23% per dollar over 38056 vullingen, 1 uur later -2.84% over 37529 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.09% per dollar over 2059 vullingen, 1 uur later -4.33% over 2023 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $111 (1159 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $378 (994 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $-523 (988 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 1435 | 205 | $3,808 | $4,844 | $92.00 tot $246 | 1183 / 787 | $4,920 | $-147 (6 nog zonder prijs) | $-34.86 (238 van 1183 beslist) | $-54.54 tot $99.60 |
| 2026-11-27 | 1200 | 212 | $3,935 | $5,104 | $84.78 tot $225 | 974 / 666 | $3,950 | $-93.33 (47 nog zonder prijs) | $0.00 (0 van 974 beslist) | $-8.55 tot $132 |
| **Totaal** | 12091 | | $3,755 | $5,104 | $768 tot $2,037 | 8567 / 5593 | $33,489 | $-776 | $-358 | $-7.77 tot $1,261 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-889 over 8545 vullingen en $33,403, dus -2.66% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.34% over $33,127 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.52%.

**Opgeschaald (GOK):** per dag $-1.94 (ondergrens) tot $149 (hoge schatting) netto (gemeten minuten × 1440 / 12091).

136 van de 8567 vullingen ($362) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.34%): $-8.49 (GOK).

Geld dat de bot nodig had: gemiddeld $3,755 in open orders plus de hoogste stand van $5,104 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,859**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-39.34 tot $3,030 |
| €5,000 | $5,000 | $-98.34 tot $7,576 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-358 over 6453 vullingen en $24,918, dus -1.44% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.66% per dollar over 7967 vullingen, 1 uur later -2.26% over 7843 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.65% per dollar over 578 vullingen, 1 uur later -3.39% over 569 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 2243 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.64 tot $3.40 | $-0.73 tot $1.03 | 2 | $36.21 tot $61.73 | $0.95 tot $26.48 |
| €150 | 2 | $3.28 tot $6.79 | $-1.46 tot $2.06 | 3 | $49.71 tot $87.76 | $-1.62 tot $36.42 |
| €200 | 3 | $4.92 tot $10.19 | $-2.19 tot $3.08 | 4 | $62.69 tot $115 | $-39.82 tot $12.14 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.93%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest seoul-on-november-28 11°C | 1947 | $3.71 tot $8.77 | 98 | $-29.95 | $0.00 |
| highest paris-on-november-26 6°C | 2083 | $8.96 tot $20.03 | 90 | $-34.19 | $-52.26 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest helsinki-on-november-28 1°C or higher | 1582 | $5.27 tot $10.26 | 61 | $-25.83 | $0.00 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $-29.11 |
| highest paris-on-november-26 7°C | 1536 | $7.12 tot $16.89 | 84 | $-26.57 | $5.42 |
| highest warsaw-on-november-28 0°C | 3347 | $10.47 tot $19.48 | 62 | $-29.68 | $0.00 |
| highest nyc-on-november-27 60-61°F | 3053 | $9.72 tot $18.90 | 44 | $-28.44 | $0.00 |
| ... | | | | | |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest nyc-on-november-26 58-59°F | 6461 | $14.00 tot $24.94 | 66 | $13.88 | $7.47 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $71.05 tot $141 | 537 | $54.69 | $126 |
| chengdu (highest) | $62.15 tot $136 | 667 | $-20.38 | $41.77 |
| miami (lowest) | $57.90 tot $101 | 157 | $-23.14 | $34.76 |
| paris (lowest) | $61.30 tot $113 | 260 | $-32.13 | $29.17 |
| london (lowest) | $56.82 tot $103 | 324 | $-27.96 | $28.86 |
| munich (highest) | $81.38 tot $182 | 1121 | $-59.44 | $21.94 |
| shanghai (lowest) | $24.12 tot $45.47 | 108 | $-8.07 | $16.05 |
| karachi (highest) | $41.42 tot $80.88 | 337 | $-28.48 | $12.94 |
| singapore (highest) | $57.73 tot $125 | 772 | $-48.98 | $8.75 |
| beijing (highest) | $47.50 tot $104 | 705 | $-38.85 | $8.65 |
| jeddah (highest) | $32.22 tot $64.87 | 236 | $-24.46 | $7.77 |
| manila (highest) | $32.98 tot $67.25 | 332 | $-27.11 | $5.87 |
| seoul (highest) | $84.24 tot $188 | 1313 | $-78.42 | $5.82 |
| kuala-lumpur (highest) | $38.20 tot $74.92 | 450 | $-33.88 | $4.31 |
| shenzhen (highest) | $45.52 tot $96.29 | 731 | $-41.86 | $3.67 |
| buenos-aires (highest) | $73.41 tot $161 | 811 | $-70.44 | $2.97 |
| sao-paulo (highest) | $42.37 tot $84.45 | 509 | $-39.48 | $2.89 |
| london (highest) | $73.48 tot $160 | 1538 | $-70.62 | $2.85 |
| nyc (highest) | $92.60 tot $184 | 1111 | $-90.25 | $2.35 |
| milan (highest) | $66.95 tot $137 | 885 | $-66.27 | $0.68 |
| tokyo (highest) | $74.60 tot $171 | 1142 | $-74.43 | $0.17 |
| wuhan (highest) | $61.84 tot $131 | 636 | $-61.94 | $-0.09 |
| seoul (lowest) | $38.09 tot $72.57 | 223 | $-39.54 | $-1.45 |
| los-angeles (highest) | $65.37 tot $142 | 1079 | $-69.25 | $-3.88 |
| chongqing (highest) | $59.67 tot $126 | 538 | $-64.55 | $-4.88 |
| mexico-city (highest) | $50.21 tot $97.33 | 454 | $-55.78 | $-5.57 |
| nyc (lowest) | $35.24 tot $61.75 | 244 | $-42.96 | $-7.71 |
| taipei (highest) | $44.91 tot $84.21 | 489 | $-54.29 | $-9.38 |
| qingdao (highest) | $34.39 tot $68.82 | 466 | $-45.54 | $-11.15 |
| ankara (highest) | $44.25 tot $86.89 | 637 | $-59.08 | $-14.83 |
| tokyo (lowest) | $23.77 tot $43.38 | 141 | $-42.05 | $-18.28 |
| chicago (highest) | $62.76 tot $119 | 1006 | $-83.29 | $-20.53 |
| austin (highest) | $78.81 tot $164 | 1014 | $-101 | $-22.28 |
| miami (highest) | $73.91 tot $156 | 1133 | $-96.74 | $-22.83 |
| tel-aviv (highest) | $75.91 tot $161 | 679 | $-103 | $-27.18 |
| moscow (highest) | $42.46 tot $85.11 | 535 | $-69.74 | $-27.28 |
| houston (highest) | $88.02 tot $182 | 1286 | $-117 | $-28.68 |
| shanghai (highest) | $60.02 tot $129 | 1134 | $-91.39 | $-31.38 |
| hong-kong (lowest) | $65.28 tot $139 | 607 | $-98.15 | $-32.86 |
| lucknow (highest) | $70.68 tot $146 | 770 | $-108 | $-37.53 |
| amsterdam (highest) | $64.18 tot $138 | 1061 | $-106 | $-42.31 |
| san-francisco (highest) | $48.77 tot $95.20 | 718 | $-97.07 | $-48.30 |
| busan (highest) | $94.85 tot $203 | 976 | $-144 | $-48.73 |
| guangzhou (highest) | $61.45 tot $129 | 885 | $-111 | $-49.30 |
| madrid (highest) | $64.86 tot $141 | 992 | $-117 | $-52.55 |
| hong-kong (highest) | $48.42 tot $104 | 1193 | $-112 | $-63.34 |
| toronto (highest) | $38.04 tot $76.78 | 673 | $-115 | $-76.92 |
| helsinki (highest) | $92.85 tot $189 | 1250 | $-170 | $-77.26 |
| wellington (highest) | $58.20 tot $127 | 930 | $-140 | $-81.63 |
| dallas (highest) | $77.96 tot $165 | 1150 | $-163 | $-85.48 |
| atlanta (highest) | $76.95 tot $163 | 1487 | $-174 | $-97.20 |
| paris (highest) | $115 tot $261 | 1755 | $-236 | $-121 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
