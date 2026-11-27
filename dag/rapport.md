# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.69 tot $1.79 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 35 runs, 11755 minuten (195.9 uur) (GEZIEN). Markten in de data: 5107. Uitslag bekend voor 3898 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-243 (4847 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $-255 (4307 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $-911 (3937 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 1435 | 205 | $3,842 | $9,065 | $377 tot $805 | 5217 / 3336 | $19,178 | $-654 (32 nog zonder prijs) | $-80.11 (300 van 5217 beslist) | $-277 tot $151 |
| 2026-11-27 | 864 | 211 | $3,924 | $9,112 | $228 tot $485 | 3153 / 1974 | $11,725 | $-339 (334 nog zonder prijs) | $0.00 (0 van 3153 beslist) | $-111 tot $146 |
| **Totaal** | 11755 | | $3,799 | $10,171 | $3,028 tot $6,285 | 39022 / 27019 | $131,745 | $-3,805 | $-3,164 | $-777 tot $2,480 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-3,055 over 38949 vullingen en $131,524, dus -2.32% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.94% over $129,557 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.86%.

**Opgeschaald (GOK):** per dag $-103 (ondergrens) tot $296 (hoge schatting) netto (gemeten minuten × 1440 / 11755).

739 van de 39022 vullingen ($2,188) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.94%): $-64.27 (GOK).

Geld dat de bot nodig had: gemiddeld $3,799 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,970**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,328 tot $3,813 |
| €5,000 | $5,000 | $-3,320 tot $9,532 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-3,164 over 29672 vullingen en $97,280, dus -3.25% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.22% per dollar over 36970 vullingen, 1 uur later -2.85% over 36283 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.05% per dollar over 1979 vullingen, 1 uur later -4.30% over 1943 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $111 (1159 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $378 (994 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $-489 (859 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 1435 | 205 | $3,808 | $4,844 | $92.00 tot $246 | 1183 / 787 | $4,920 | $-147 (6 nog zonder prijs) | $-19.57 (70 van 1183 beslist) | $-54.54 tot $99.60 |
| 2026-11-27 | 864 | 211 | $3,920 | $4,795 | $54.64 tot $148 | 715 / 494 | $2,954 | $-52.97 (80 nog zonder prijs) | $0.00 (0 van 715 beslist) | $1.68 tot $94.77 |
| **Totaal** | 11755 | | $3,748 | $4,844 | $738 tot $1,960 | 8308 / 5421 | $32,494 | $-736 | $-309 | $2.46 tot $1,224 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-869 over 8285 vullingen en $32,405, dus -2.68% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.30% over $31,924 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.48%.

**Opgeschaald (GOK):** per dag $-1.31 (ondergrens) tot $148 (hoge schatting) netto (gemeten minuten × 1440 / 11755).

169 van de 8308 vullingen ($570) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.30%): $-13.14 (GOK).

Geld dat de bot nodig had: gemiddeld $3,748 in open orders plus de hoogste stand van $4,844 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,592**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-27.40 tot $3,107 |
| €5,000 | $5,000 | $-68.50 tot $7,768 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-309 over 6156 vullingen en $23,672, dus -1.30% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.69% per dollar over 7728 vullingen, 1 uur later -2.22% over 7573 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.61% per dollar over 557 vullingen, 1 uur later -3.31% over 550 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 2174 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.62 tot $3.37 | $-0.85 tot $0.90 | 2 | $40.07 tot $65.24 | $3.77 tot $28.94 |
| €150 | 2 | $3.25 tot $6.73 | $-1.69 tot $1.79 | 4 | $54.40 tot $93.17 | $-32.55 tot $6.22 |
| €200 | 3 | $4.87 tot $10.10 | $-2.54 tot $2.69 | 5 | $67.91 tot $119 | $-35.12 tot $16.17 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.94%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

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
| highest nyc-on-november-27 60-61°F | 3053 | $9.72 tot $18.90 | 44 | $-28.44 | $0.00 |
| highest austin-on-november-27 68-69°F | 1432 | $3.90 tot $7.88 | 72 | $-22.09 | $0.00 |
| highest warsaw-on-november-28 0°C | 2726 | $8.59 tot $15.71 | 55 | $-26.32 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| ... | | | | | |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest seoul-on-november-28 10°C | 1871 | $7.32 tot $15.82 | 82 | $4.69 | $0.00 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest nyc-on-november-26 58-59°F | 6461 | $14.00 tot $24.94 | 66 | $13.88 | $7.47 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $68.90 tot $137 | 529 | $55.75 | $125 |
| seoul (highest) | $82.37 tot $183 | 1265 | $-37.73 | $44.64 |
| chengdu (highest) | $60.48 tot $132 | 655 | $-19.73 | $40.74 |
| miami (lowest) | $55.44 tot $96.73 | 155 | $-21.99 | $33.44 |
| paris (lowest) | $58.93 tot $109 | 250 | $-31.60 | $27.34 |
| london (lowest) | $54.39 tot $99.23 | 315 | $-27.57 | $26.82 |
| munich (highest) | $78.79 tot $176 | 1091 | $-61.91 | $16.88 |
| shanghai (lowest) | $22.49 tot $42.66 | 92 | $-10.76 | $11.72 |
| karachi (highest) | $40.39 tot $78.78 | 330 | $-29.67 | $10.72 |
| singapore (highest) | $55.19 tot $119 | 753 | $-45.43 | $9.77 |
| beijing (highest) | $46.09 tot $101 | 687 | $-37.37 | $8.72 |
| shenzhen (highest) | $43.94 tot $93.19 | 712 | $-35.94 | $8.00 |
| manila (highest) | $31.84 tot $64.93 | 320 | $-25.02 | $6.82 |
| jeddah (highest) | $30.63 tot $61.75 | 233 | $-24.46 | $6.17 |
| sao-paulo (highest) | $41.33 tot $82.38 | 488 | $-36.79 | $4.54 |
| kuala-lumpur (highest) | $37.30 tot $72.99 | 437 | $-34.35 | $2.95 |
| london (highest) | $71.80 tot $156 | 1491 | $-70.56 | $1.24 |
| buenos-aires (highest) | $67.93 tot $148 | 778 | $-67.78 | $0.15 |
| tokyo (highest) | $72.94 tot $167 | 1115 | $-73.25 | $-0.31 |
| milan (highest) | $63.49 tot $130 | 867 | $-64.42 | $-0.93 |
| wuhan (highest) | $59.30 tot $126 | 611 | $-60.57 | $-1.26 |
| nyc (lowest) | $32.36 tot $56.79 | 228 | $-34.17 | $-1.81 |
| seoul (lowest) | $37.24 tot $70.84 | 219 | $-39.61 | $-2.37 |
| los-angeles (highest) | $62.72 tot $137 | 1041 | $-66.47 | $-3.75 |
| chongqing (highest) | $58.09 tot $123 | 522 | $-62.84 | $-4.76 |
| mexico-city (highest) | $49.03 tot $95.14 | 447 | $-55.57 | $-6.54 |
| taipei (highest) | $43.84 tot $82.04 | 472 | $-50.47 | $-6.63 |
| tokyo (lowest) | $23.16 tot $42.05 | 138 | $-36.42 | $-13.25 |
| qingdao (highest) | $33.12 tot $66.28 | 444 | $-46.44 | $-13.32 |
| ankara (highest) | $42.79 tot $83.84 | 618 | $-58.57 | $-15.77 |
| nyc (highest) | $89.90 tot $179 | 1100 | $-106 | $-16.19 |
| chicago (highest) | $61.78 tot $117 | 993 | $-82.78 | $-21.00 |
| miami (highest) | $71.16 tot $150 | 1090 | $-95.53 | $-24.36 |
| austin (highest) | $76.73 tot $159 | 986 | $-103 | $-26.33 |
| houston (highest) | $85.80 tot $177 | 1240 | $-113 | $-27.03 |
| tel-aviv (highest) | $72.74 tot $155 | 645 | $-100 | $-27.74 |
| moscow (highest) | $40.98 tot $82.06 | 519 | $-69.72 | $-28.74 |
| madrid (highest) | $62.16 tot $135 | 942 | $-95.53 | $-33.37 |
| shanghai (highest) | $58.42 tot $126 | 1098 | $-91.84 | $-33.43 |
| hong-kong (lowest) | $61.08 tot $130 | 586 | $-98.75 | $-37.67 |
| lucknow (highest) | $68.17 tot $141 | 748 | $-106 | $-38.02 |
| amsterdam (highest) | $60.93 tot $131 | 1019 | $-99.85 | $-38.92 |
| san-francisco (highest) | $47.81 tot $93.21 | 697 | $-95.30 | $-47.49 |
| guangzhou (highest) | $60.11 tot $126 | 868 | $-109 | $-48.57 |
| busan (highest) | $90.23 tot $195 | 957 | $-142 | $-52.17 |
| helsinki (highest) | $90.47 tot $184 | 1197 | $-152 | $-61.72 |
| hong-kong (highest) | $46.86 tot $100 | 1176 | $-110 | $-63.54 |
| toronto (highest) | $37.34 tot $75.31 | 666 | $-113 | $-75.97 |
| wellington (highest) | $56.87 tot $124 | 917 | $-139 | $-82.58 |
| dallas (highest) | $75.13 tot $159 | 1117 | $-161 | $-85.99 |
| atlanta (highest) | $74.91 tot $159 | 1443 | $-174 | $-98.62 |
| paris (highest) | $112 tot $253 | 1715 | $-234 | $-122 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
