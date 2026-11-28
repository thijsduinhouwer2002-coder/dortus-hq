# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.32 tot $2.23 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 39 runs, 13097 minuten (218.3 uur) (GEZIEN). Markten in de data: 5656. Uitslag bekend voor 4428 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-243 (4847 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $-255 (4307 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $-1,107 (5172 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 1435 | 205 | $3,842 | $9,065 | $377 tot $805 | 5217 / 3336 | $19,178 | $-654 (32 nog zonder prijs) | $-674 (3262 van 5217 beslist) | $-277 tot $151 |
| 2026-11-27 | 1433 | 209 | $3,926 | $10,055 | $394 tot $831 | 4933 / 3176 | $18,346 | $-571 (41 nog zonder prijs) | $12.51 (305 van 4933 beslist) | $-177 tot $259 |
| 2026-11-28 | 773 | 195 | $3,664 | $10,053 | $200 tot $425 | 2502 / 1610 | $9,339 | $-228 (200 nog zonder prijs) | $0.00 (0 van 2502 beslist) | $-28.37 tot $197 |
| **Totaal** | 13097 | | $3,797 | $10,171 | $3,395 tot $7,055 | 43304 / 29831 | $147,705 | $-4,266 | $-3,941 | $-871 tot $2,790 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-3,469 over 43232 vullingen en $147,472, dus -2.35% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.92% over $146,054 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.90%.

**Opgeschaald (GOK):** per dag $-101 (ondergrens) tot $301 (hoge schatting) netto (gemeten minuten × 1440 / 13097).

646 van de 43304 vullingen ($1,651) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.92%): $-48.22 (GOK).

Geld dat de bot nodig had: gemiddeld $3,797 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,968**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,303 tot $3,884 |
| €5,000 | $5,000 | $-3,257 tot $9,710 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-3,941 over 34174 vullingen en $113,276, dus -3.48% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.25% per dollar over 40944 vullingen, 1 uur later -2.84% over 40350 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.07% per dollar over 2288 vullingen, 1 uur later -4.31% over 2246 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $111 (1159 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $378 (994 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $-600 (1175 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 1435 | 205 | $3,808 | $4,844 | $92.00 tot $246 | 1183 / 787 | $4,920 | $-147 (6 nog zonder prijs) | $10.25 (636 van 1183 beslist) | $-54.54 tot $99.60 |
| 2026-11-27 | 1433 | 209 | $3,897 | $5,156 | $99.95 tot $264 | 1113 / 755 | $4,501 | $-117 (5 nog zonder prijs) | $-32.98 (56 van 1113 beslist) | $-17.44 tot $146 |
| 2026-11-28 | 773 | 195 | $3,637 | $4,642 | $51.22 tot $133 | 581 / 377 | $2,280 | $-22.42 (40 nog zonder prijs) | $0.00 (0 van 581 beslist) | $28.81 tot $110 |
| **Totaal** | 13097 | | $3,747 | $5,156 | $835 tot $2,208 | 9287 / 6059 | $36,321 | $-822 | $-423 | $12.16 tot $1,385 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-979 over 9264 vullingen en $36,232, dus -2.70% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.29% over $35,967 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.52%.

**Opgeschaald (GOK):** per dag $0.45 (ondergrens) tot $151 (hoge schatting) netto (gemeten minuten × 1440 / 13097).

134 van de 9287 vullingen ($354) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.29%): $-8.09 (GOK).

Geld dat de bot nodig had: gemiddeld $3,747 in open orders plus de hoogste stand van $5,156 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,902**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $9.05 tot $3,062 |
| €5,000 | $5,000 | $22.62 tot $7,655 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-423 over 7094 vullingen en $27,385, dus -1.54% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.71% per dollar over 8622 vullingen, 1 uur later -2.19% over 8501 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.57% per dollar over 642 vullingen, 1 uur later -3.47% over 632 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 2390 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.65 tot $3.42 | $-0.66 tot $1.11 | 2 | $45.36 tot $90.71 | $-24.67 tot $20.67 |
| €150 | 2 | $3.30 tot $6.85 | $-1.32 tot $2.23 | 4 | $61.46 tot $125 | $-66.46 tot $-3.03 |
| €200 | 3 | $4.95 tot $10.27 | $-1.98 tot $3.34 | 5 | $74.96 tot $151 | $-69.04 tot $6.92 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.92%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest warsaw-on-november-28 -1°C | 3598 | $11.88 tot $22.23 | 73 | $-53.91 | $0.00 |
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest seoul-on-november-28 11°C | 1947 | $3.71 tot $8.77 | 98 | $-29.95 | $0.00 |
| highest paris-on-november-26 6°C | 2083 | $8.96 tot $20.03 | 90 | $-34.19 | $-52.26 |
| highest helsinki-on-november-28 1°C or higher | 1641 | $5.50 tot $10.67 | 64 | $-28.13 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $-29.11 |
| highest paris-on-november-26 7°C | 1536 | $7.12 tot $16.89 | 84 | $-26.57 | $5.42 |
| highest nyc-on-november-27 60-61°F | 3053 | $9.72 tot $18.90 | 44 | $-28.44 | $-21.79 |
| ... | | | | | |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest nyc-on-november-28 52-53°F | 4360 | $10.69 tot $20.85 | 42 | $0.65 | $0.00 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest warsaw-on-november-29 -1°C | 1025 | $3.18 tot $6.71 | 28 | $24.09 | $0.00 |
| highest nyc-on-november-26 58-59°F | 6461 | $14.00 tot $24.94 | 66 | $13.88 | $7.47 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $75.32 tot $150 | 574 | $48.44 | $124 |
| chengdu (highest) | $65.76 tot $145 | 697 | $-21.63 | $44.13 |
| miami (lowest) | $59.61 tot $103 | 165 | $-24.70 | $34.91 |
| paris (lowest) | $68.72 tot $126 | 286 | $-38.99 | $29.72 |
| london (lowest) | $61.40 tot $112 | 384 | $-32.16 | $29.24 |
| shanghai (lowest) | $29.46 tot $54.80 | 120 | $-11.12 | $18.34 |
| singapore (highest) | $62.24 tot $135 | 819 | $-48.57 | $13.67 |
| beijing (highest) | $49.83 tot $110 | 758 | $-36.77 | $13.06 |
| munich (highest) | $88.02 tot $199 | 1239 | $-76.34 | $11.68 |
| jeddah (highest) | $33.83 tot $68.38 | 248 | $-25.85 | $7.98 |
| nyc (highest) | $98.47 tot $196 | 1155 | $-92.98 | $5.49 |
| kuala-lumpur (highest) | $40.05 tot $78.65 | 488 | $-35.27 | $4.78 |
| manila (highest) | $34.71 tot $71.06 | 387 | $-31.02 | $3.69 |
| seoul (highest) | $93.58 tot $209 | 1432 | $-91.13 | $2.45 |
| karachi (highest) | $43.59 tot $85.58 | 394 | $-42.30 | $1.29 |
| sao-paulo (highest) | $44.95 tot $89.70 | 539 | $-43.82 | $1.13 |
| milan (highest) | $72.02 tot $146 | 931 | $-71.54 | $0.49 |
| seoul (lowest) | $41.25 tot $78.99 | 236 | $-40.96 | $0.29 |
| tokyo (highest) | $85.53 tot $198 | 1321 | $-85.54 | $-0.01 |
| london (highest) | $77.00 tot $169 | 1614 | $-77.14 | $-0.14 |
| shenzhen (highest) | $49.13 tot $104 | 778 | $-49.45 | $-0.31 |
| buenos-aires (highest) | $87.14 tot $192 | 919 | $-89.17 | $-2.03 |
| chongqing (highest) | $63.26 tot $134 | 571 | $-66.62 | $-3.36 |
| los-angeles (highest) | $71.96 tot $156 | 1142 | $-77.21 | $-5.26 |
| nyc (lowest) | $42.74 tot $74.39 | 282 | $-50.06 | $-7.31 |
| taipei (highest) | $47.31 tot $89.21 | 521 | $-54.98 | $-7.67 |
| mexico-city (highest) | $56.35 tot $109 | 524 | $-64.61 | $-8.26 |
| wuhan (highest) | $66.44 tot $141 | 702 | $-78.01 | $-11.56 |
| tokyo (lowest) | $27.55 tot $50.33 | 149 | $-41.82 | $-14.27 |
| qingdao (highest) | $35.99 tot $72.40 | 484 | $-50.39 | $-14.39 |
| chicago (highest) | $66.88 tot $127 | 1082 | $-84.12 | $-17.24 |
| ankara (highest) | $46.19 tot $90.91 | 664 | $-64.50 | $-18.32 |
| miami (highest) | $79.69 tot $167 | 1212 | $-98.50 | $-18.81 |
| houston (highest) | $94.88 tot $195 | 1369 | $-117 | $-21.87 |
| moscow (highest) | $44.53 tot $89.35 | 569 | $-70.53 | $-25.99 |
| hong-kong (lowest) | $79.26 tot $167 | 670 | $-107 | $-27.61 |
| austin (highest) | $84.17 tot $175 | 1087 | $-117 | $-32.90 |
| tel-aviv (highest) | $81.35 tot $173 | 758 | $-115 | $-33.24 |
| amsterdam (highest) | $69.94 tot $150 | 1136 | $-107 | $-37.45 |
| san-francisco (highest) | $53.58 tot $104 | 785 | $-95.53 | $-41.96 |
| shanghai (highest) | $63.96 tot $138 | 1224 | $-106 | $-42.03 |
| lucknow (highest) | $74.83 tot $154 | 822 | $-120 | $-45.58 |
| busan (highest) | $103 tot $221 | 1042 | $-156 | $-53.14 |
| guangzhou (highest) | $65.94 tot $138 | 964 | $-120 | $-54.37 |
| hong-kong (highest) | $51.06 tot $109 | 1274 | $-113 | $-62.20 |
| madrid (highest) | $69.34 tot $151 | 1048 | $-132 | $-62.92 |
| toronto (highest) | $41.18 tot $83.30 | 732 | $-118 | $-76.65 |
| dallas (highest) | $84.08 tot $179 | 1230 | $-164 | $-79.85 |
| helsinki (highest) | $97.16 tot $198 | 1304 | $-183 | $-85.34 |
| wellington (highest) | $62.57 tot $137 | 1024 | $-149 | $-86.34 |
| atlanta (highest) | $81.87 tot $173 | 1559 | $-182 | $-100 |
| paris (highest) | $126 tot $287 | 1890 | $-245 | $-119 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
