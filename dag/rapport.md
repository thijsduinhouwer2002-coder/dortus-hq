# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.38 tot $2.09 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 37 runs, 12426 minuten (207.1 uur) (GEZIEN). Markten in de data: 5107. Uitslag bekend voor 4262 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-243 (4847 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $-255 (4307 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $-980 (5033 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 1435 | 205 | $3,842 | $9,065 | $377 tot $805 | 5217 / 3336 | $19,178 | $-654 (32 nog zonder prijs) | $-403 (1965 van 5217 beslist) | $-277 tot $151 |
| 2026-11-27 | 1433 | 209 | $3,926 | $10,055 | $394 tot $831 | 4933 / 3176 | $18,346 | $-571 (41 nog zonder prijs) | $2.15 (3 van 4933 beslist) | $-177 tot $259 |
| 2026-11-28 | 102 | 181 | $3,350 | $9,607 | $22.77 tot $48.25 | 329 / 214 | $1,330 | $-5.96 (164 nog zonder prijs) | $0.00 (0 van 329 beslist) | $16.81 tot $42.29 |
| **Totaal** | 12426 | | $3,802 | $10,171 | $3,217 tot $6,679 | 41131 / 28435 | $139,696 | $-4,043 | $-3,553 | $-826 tot $2,635 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-3,286 over 41060 vullingen en $139,473, dus -2.36% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.93% over $138,080 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.90%.

**Opgeschaald (GOK):** per dag $-101 (ondergrens) tot $300 (hoge schatting) netto (gemeten minuten × 1440 / 12426).

610 van de 41131 vullingen ($1,616) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.93%): $-47.33 (GOK).

Geld dat de bot nodig had: gemiddeld $3,802 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,972**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,304 tot $3,864 |
| €5,000 | $5,000 | $-3,260 tot $9,659 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-3,553 over 32436 vullingen en $107,396, dus -3.31% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.26% per dollar over 38940 vullingen, 1 uur later -2.85% over 38372 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.05% per dollar over 2120 vullingen, 1 uur later -4.26% over 2088 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $111 (1159 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $378 (994 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $-527 (1131 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 1435 | 205 | $3,808 | $4,844 | $92.00 tot $246 | 1183 / 787 | $4,920 | $-147 (6 nog zonder prijs) | $-81.91 (375 van 1183 beslist) | $-54.54 tot $99.60 |
| 2026-11-27 | 1433 | 209 | $3,897 | $5,156 | $99.95 tot $264 | 1113 / 755 | $4,501 | $-117 (5 nog zonder prijs) | $3.40 (1 van 1113 beslist) | $-17.44 tot $146 |
| 2026-11-28 | 102 | 181 | $3,360 | $4,557 | $5.58 tot $14.91 | 74 / 46 | $310 | $-1.23 (41 nog zonder prijs) | $0.00 (0 van 74 beslist) | $4.36 tot $13.68 |
| **Totaal** | 12426 | | $3,750 | $5,156 | $789 tot $2,090 | 8780 / 5728 | $34,351 | $-801 | $-405 | $-12.29 tot $1,289 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-936 over 8757 vullingen en $34,263, dus -2.73% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.36% over $33,979 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.59%.

**Opgeschaald (GOK):** per dag $-2.44 (ondergrens) tot $148 (hoge schatting) netto (gemeten minuten × 1440 / 12426).

135 van de 8780 vullingen ($372) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.36%): $-8.78 (GOK).

Geld dat de bot nodig had: gemiddeld $3,750 in open orders plus de hoogste stand van $5,156 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,906**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-49.35 tot $2,998 |
| €5,000 | $5,000 | $-123 tot $7,496 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-405 over 6734 vullingen en $25,986, dus -1.56% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.74% per dollar over 8160 vullingen, 1 uur later -2.29% over 8037 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.63% per dollar over 597 vullingen, 1 uur later -3.18% over 589 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 2266 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.62 tot $3.35 | $-0.69 tot $1.04 | 2 | $38.50 tot $73.23 | $-11.60 tot $23.13 |
| €150 | 2 | $3.23 tot $6.69 | $-1.38 tot $2.09 | 3 | $51.48 tot $100 | $-49.79 tot $-1.16 |
| €200 | 3 | $4.85 tot $10.04 | $-2.06 tot $3.13 | 4 | $61.17 tot $117 | $-37.86 tot $17.76 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.93%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

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
| highest nyc-on-november-27 60-61°F | 3053 | $9.72 tot $18.90 | 44 | $-28.44 | $0.00 |
| ... | | | | | |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest nyc-on-november-28 52-53°F | 4089 | $9.65 tot $18.71 | 40 | $1.35 | $0.00 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest nyc-on-november-26 58-59°F | 6461 | $14.00 tot $24.94 | 66 | $13.88 | $7.47 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $72.47 tot $144 | 548 | $30.46 | $103 |
| chengdu (highest) | $62.96 tot $138 | 671 | $-20.34 | $42.62 |
| miami (lowest) | $58.95 tot $102 | 161 | $-23.78 | $35.18 |
| london (lowest) | $58.60 tot $107 | 343 | $-30.08 | $28.52 |
| paris (lowest) | $63.21 tot $116 | 271 | $-36.71 | $26.50 |
| munich (highest) | $83.08 tot $187 | 1149 | $-58.72 | $24.35 |
| shanghai (lowest) | $25.63 tot $48.07 | 110 | $-8.07 | $17.56 |
| beijing (highest) | $48.34 tot $106 | 717 | $-38.66 | $9.68 |
| jeddah (highest) | $33.18 tot $66.86 | 238 | $-24.56 | $8.63 |
| singapore (highest) | $58.92 tot $127 | 787 | $-50.56 | $8.37 |
| karachi (highest) | $42.35 tot $82.75 | 360 | $-36.98 | $5.37 |
| nyc (highest) | $94.85 tot $188 | 1124 | $-89.66 | $5.20 |
| kuala-lumpur (highest) | $38.91 tot $76.24 | 452 | $-33.78 | $5.12 |
| manila (highest) | $33.65 tot $68.69 | 349 | $-28.88 | $4.78 |
| sao-paulo (highest) | $43.58 tot $86.90 | 523 | $-39.07 | $4.51 |
| seoul (highest) | $85.25 tot $191 | 1336 | $-81.05 | $4.21 |
| shenzhen (highest) | $46.88 tot $99.21 | 742 | $-44.16 | $2.72 |
| london (highest) | $74.52 tot $163 | 1565 | $-72.00 | $2.53 |
| buenos-aires (highest) | $79.65 tot $175 | 870 | $-77.67 | $1.98 |
| milan (highest) | $70.16 tot $142 | 908 | $-69.47 | $0.69 |
| wuhan (highest) | $63.14 tot $134 | 648 | $-63.29 | $-0.15 |
| seoul (lowest) | $38.61 tot $73.63 | 223 | $-39.64 | $-1.03 |
| los-angeles (highest) | $68.23 tot $149 | 1096 | $-69.45 | $-1.21 |
| tokyo (highest) | $75.78 tot $174 | 1171 | $-77.70 | $-1.92 |
| nyc (lowest) | $37.73 tot $66.12 | 260 | $-41.10 | $-3.37 |
| chongqing (highest) | $60.45 tot $128 | 546 | $-65.09 | $-4.64 |
| mexico-city (highest) | $52.22 tot $101 | 488 | $-57.69 | $-5.47 |
| taipei (highest) | $45.68 tot $85.78 | 492 | $-54.29 | $-8.61 |
| qingdao (highest) | $34.94 tot $70.08 | 469 | $-45.47 | $-10.53 |
| ankara (highest) | $45.10 tot $88.61 | 646 | $-59.78 | $-14.68 |
| tokyo (lowest) | $24.30 tot $44.37 | 141 | $-42.05 | $-17.75 |
| chicago (highest) | $64.45 tot $122 | 1027 | $-84.96 | $-20.51 |
| miami (highest) | $76.05 tot $160 | 1181 | $-98.70 | $-22.65 |
| austin (highest) | $81.06 tot $169 | 1043 | $-106 | $-24.81 |
| tel-aviv (highest) | $78.11 tot $166 | 703 | $-105 | $-26.59 |
| houston (highest) | $89.72 tot $185 | 1307 | $-117 | $-27.23 |
| moscow (highest) | $43.15 tot $86.69 | 543 | $-70.62 | $-27.47 |
| shanghai (highest) | $60.72 tot $131 | 1145 | $-90.87 | $-30.15 |
| hong-kong (lowest) | $67.45 tot $144 | 615 | $-99.15 | $-31.70 |
| amsterdam (highest) | $66.52 tot $143 | 1082 | $-106 | $-39.31 |
| lucknow (highest) | $72.40 tot $149 | 788 | $-114 | $-42.02 |
| san-francisco (highest) | $50.12 tot $97.78 | 745 | $-96.26 | $-46.15 |
| guangzhou (highest) | $62.07 tot $131 | 893 | $-113 | $-50.68 |
| busan (highest) | $96.84 tot $208 | 1005 | $-148 | $-51.22 |
| madrid (highest) | $67.31 tot $146 | 1010 | $-121 | $-53.65 |
| hong-kong (highest) | $49.09 tot $105 | 1208 | $-111 | $-61.76 |
| toronto (highest) | $39.49 tot $79.69 | 702 | $-117 | $-78.01 |
| wellington (highest) | $59.12 tot $129 | 937 | $-139 | $-80.35 |
| dallas (highest) | $81.15 tot $172 | 1202 | $-165 | $-83.57 |
| helsinki (highest) | $94.34 tot $192 | 1273 | $-178 | $-83.79 |
| atlanta (highest) | $79.41 tot $168 | 1527 | $-180 | $-101 |
| paris (highest) | $117 tot $266 | 1791 | $-233 | $-116 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
