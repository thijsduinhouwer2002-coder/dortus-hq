# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.73 tot $1.74 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 32 runs, 10747 minuten (179.1 uur) (GEZIEN). Markten in de data: 4563. Uitslag bekend voor 3588 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-243 (4847 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $-13.03 (3832 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $-94.65 (1420 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 1291 | 207 | $3,858 | $9,065 | $335 tot $717 | 4774 / 3062 | $17,517 | $-544 (236 nog zonder prijs) | $0.00 (0 van 4774 beslist) | $-208 tot $173 |
| **Totaal** | 10747 | | $3,791 | $10,171 | $2,758 tot $5,711 | 35426 / 24771 | $118,358 | $-3,355 | $-2,025 | $-597 tot $2,356 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-2,684 over 35365 vullingen en $118,175, dus -2.27% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.88% over $116,692 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.77%.

**Opgeschaald (GOK):** per dag $-86.45 (ondergrens) tot $309 (hoge schatting) netto (gemeten minuten × 1440 / 10747).

609 van de 35426 vullingen ($1,666) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.88%): $-47.91 (GOK).

Geld dat de bot nodig had: gemiddeld $3,791 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,961**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,115 tot $3,987 |
| €5,000 | $5,000 | $-2,786 tot $9,968 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-2,025 over 26380 vullingen en $85,581, dus -2.37% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.18% per dollar over 33699 vullingen, 1 uur later -2.79% over 33139 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.95% per dollar over 1666 vullingen, 1 uur later -4.36% over 1628 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $111 (1159 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $463 (860 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $-97.08 (271 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 1291 | 207 | $3,825 | $4,844 | $82.00 tot $219 | 1087 / 724 | $4,526 | $-106 (44 nog zonder prijs) | $0.00 (0 van 1087 beslist) | $-23.75 tot $113 |
| **Totaal** | 10747 | | $3,736 | $4,844 | $673 tot $1,784 | 7497 / 4864 | $29,146 | $-642 | $187 | $31.58 tot $1,142 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-765 over 7479 vullingen en $29,067, dus -2.63% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.23% over $28,787 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.36%.

**Opgeschaald (GOK):** per dag $3.16 (ondergrens) tot $152 (hoge schatting) netto (gemeten minuten × 1440 / 10747).

127 van de 7497 vullingen ($359) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.23%): $-8.01 (GOK).

Geld dat de bot nodig had: gemiddeld $3,736 in open orders plus de hoogste stand van $4,844 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,580**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $66.24 tot $3,189 |
| €5,000 | $5,000 | $166 tot $7,972 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $187 over 5364 vullingen en $20,412, dus +0.92% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.60% per dollar over 7021 vullingen, 1 uur later -2.13% over 6907 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.10% per dollar over 458 vullingen, 1 uur later -3.54% over 449 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 2026 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.62 tot $3.36 | $-0.87 tot $0.87 | 2 | $38.50 tot $73.23 | $-11.60 tot $23.13 |
| €150 | 2 | $3.25 tot $6.72 | $-1.73 tot $1.74 | 3 | $51.48 tot $100 | $-49.79 tot $-1.16 |
| €200 | 3 | $4.87 tot $10.09 | $-2.60 tot $2.61 | 4 | $61.17 tot $117 | $-37.86 tot $17.76 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.88%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest paris-on-november-26 6°C | 2083 | $8.96 tot $20.03 | 90 | $-34.19 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest austin-on-november-27 68-69°F | 930 | $2.96 tot $5.85 | 50 | $-23.50 | $0.00 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $-29.11 |
| highest paris-on-november-26 7°C | 1536 | $7.12 tot $16.89 | 84 | $-26.57 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $24.65 |
| highest madrid-on-november-27 14°C or higher | 1996 | $2.66 tot $5.18 | 64 | $-18.49 | $0.00 |
| ... | | | | | |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest nyc-on-november-27 58-59°F | 2025 | $6.20 tot $12.60 | 25 | $6.71 | $0.00 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest warsaw-on-november-27 2°C | 2030 | $8.68 tot $15.90 | 30 | $5.87 | $0.00 |
| highest nyc-on-november-28 56-57°F | 367 | $1.94 tot $2.98 | 3 | $15.69 | $0.00 |
| highest nyc-on-november-26 58-59°F | 6461 | $14.00 tot $24.94 | 66 | $13.88 | $0.00 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $60.43 tot $122 | 472 | $93.49 | $154 |
| seoul (highest) | $73.46 tot $162 | 1053 | $-25.14 | $48.32 |
| nyc (highest) | $81.62 tot $163 | 1062 | $-45.25 | $36.37 |
| chengdu (highest) | $54.89 tot $120 | 587 | $-20.25 | $34.63 |
| miami (lowest) | $52.97 tot $92.32 | 143 | $-18.51 | $34.46 |
| london (lowest) | $47.76 tot $87.70 | 271 | $-19.95 | $27.81 |
| munich (highest) | $73.20 tot $162 | 990 | $-46.54 | $26.66 |
| paris (lowest) | $53.13 tot $98.27 | 219 | $-33.25 | $19.89 |
| beijing (highest) | $43.81 tot $95.40 | 628 | $-26.22 | $17.58 |
| manila (highest) | $29.75 tot $60.52 | 299 | $-18.11 | $11.63 |
| singapore (highest) | $50.67 tot $110 | 676 | $-42.02 | $8.65 |
| shanghai (lowest) | $17.82 tot $33.71 | 81 | $-9.27 | $8.54 |
| jeddah (highest) | $28.14 tot $56.94 | 208 | $-19.60 | $8.54 |
| wuhan (highest) | $53.01 tot $113 | 501 | $-45.43 | $7.58 |
| karachi (highest) | $36.04 tot $71.71 | 295 | $-29.25 | $6.79 |
| buenos-aires (highest) | $58.84 tot $127 | 690 | $-54.21 | $4.63 |
| tokyo (highest) | $60.97 tot $139 | 939 | $-56.38 | $4.59 |
| shenzhen (highest) | $40.33 tot $85.72 | 682 | $-36.47 | $3.85 |
| sao-paulo (highest) | $38.93 tot $77.53 | 450 | $-35.38 | $3.55 |
| kuala-lumpur (highest) | $35.03 tot $68.44 | 405 | $-32.39 | $2.65 |
| nyc (lowest) | $26.38 tot $45.53 | 194 | $-26.88 | $-0.50 |
| milan (highest) | $59.60 tot $122 | 789 | $-61.83 | $-2.22 |
| los-angeles (highest) | $56.92 tot $124 | 972 | $-59.20 | $-2.28 |
| chongqing (highest) | $54.28 tot $114 | 499 | $-57.01 | $-2.73 |
| mexico-city (highest) | $44.62 tot $86.81 | 388 | $-48.09 | $-3.47 |
| london (highest) | $66.00 tot $143 | 1344 | $-70.24 | $-4.23 |
| seoul (lowest) | $33.61 tot $63.40 | 207 | $-38.50 | $-4.89 |
| taipei (highest) | $40.97 tot $76.37 | 432 | $-47.03 | $-6.06 |
| tokyo (lowest) | $18.89 tot $33.85 | 85 | $-25.33 | $-6.44 |
| qingdao (highest) | $30.64 tot $61.32 | 373 | $-39.37 | $-8.73 |
| ankara (highest) | $39.70 tot $77.88 | 587 | $-55.86 | $-16.16 |
| chicago (highest) | $57.97 tot $109 | 905 | $-78.57 | $-20.60 |
| miami (highest) | $66.83 tot $141 | 995 | $-89.25 | $-22.42 |
| tel-aviv (highest) | $67.98 tot $145 | 574 | $-91.59 | $-23.61 |
| moscow (highest) | $38.17 tot $76.63 | 484 | $-65.39 | $-27.22 |
| shanghai (highest) | $54.69 tot $118 | 1029 | $-83.12 | $-28.43 |
| houston (highest) | $78.84 tot $162 | 1181 | $-107 | $-28.44 |
| guangzhou (highest) | $56.58 tot $118 | 797 | $-86.01 | $-29.43 |
| austin (highest) | $70.77 tot $146 | 891 | $-102 | $-31.29 |
| madrid (highest) | $59.72 tot $129 | 888 | $-92.26 | $-32.54 |
| amsterdam (highest) | $56.93 tot $123 | 947 | $-89.78 | $-32.86 |
| lucknow (highest) | $62.53 tot $129 | 679 | $-99.83 | $-37.30 |
| hong-kong (lowest) | $43.27 tot $91.37 | 470 | $-81.42 | $-38.15 |
| san-francisco (highest) | $44.61 tot $86.78 | 660 | $-93.84 | $-49.23 |
| busan (highest) | $81.15 tot $174 | 853 | $-133 | $-51.63 |
| hong-kong (highest) | $43.74 tot $93.34 | 1114 | $-103 | $-58.90 |
| helsinki (highest) | $83.87 tot $171 | 1130 | $-146 | $-62.30 |
| dallas (highest) | $68.96 tot $146 | 989 | $-137 | $-68.32 |
| toronto (highest) | $33.80 tot $68.04 | 611 | $-108 | $-73.76 |
| wellington (highest) | $51.00 tot $111 | 806 | $-137 | $-86.04 |
| atlanta (highest) | $69.76 tot $147 | 1325 | $-160 | $-90.45 |
| paris (highest) | $104 tot $233 | 1577 | $-222 | $-117 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
