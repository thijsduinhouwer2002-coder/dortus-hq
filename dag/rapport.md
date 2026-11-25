# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.48 tot $1.73 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 25 runs, 8396 minuten (139.9 uur) (GEZIEN). Markten in de data: 3861. Uitslag bekend voor 2706 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-307 (4307 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $42.36 (3149 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $14.07 (67 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 373 | 159 | $3,014 | $7,388 | $77.22 tot $162 | 1152 / 751 | $4,000 | $-116 (204 nog zonder prijs) | $0.00 (0 van 1152 beslist) | $-38.44 tot $46.34 |
| **Totaal** | 8396 | | $3,814 | $10,171 | $2,032 tot $4,167 | 26587 / 19134 | $86,406 | $-2,414 | $-1,545 | $-382 tot $1,753 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,805 over 26533 vullingen en $86,238, dus -2.09% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.84% over $84,896 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.67%.

**Opgeschaald (GOK):** per dag $-72.89 (ondergrens) tot $293 (hoge schatting) netto (gemeten minuten × 1440 / 8396).

538 van de 26587 vullingen ($1,510) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.84%): $-42.94 (GOK).

Geld dat de bot nodig had: gemiddeld $3,814 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,985**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-938 tot $3,774 |
| €5,000 | $5,000 | $-2,345 tot $9,436 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,545 over 19382 vullingen en $62,536, dus -2.47% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.02% per dollar over 25547 vullingen, 1 uur later -2.77% over 25055 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.99% per dollar over 986 vullingen, 1 uur later -4.54% over 957 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-249 (839 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $203 (770 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $30.36 (15 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 373 | 159 | $2,967 | $3,504 | $18.39 tot $50.39 | 254 / 154 | $1,049 | $-32.16 (46 nog zonder prijs) | $0.00 (0 van 254 beslist) | $-13.77 tot $18.23 |
| **Totaal** | 8396 | | $3,753 | $4,020 | $501 tot $1,321 | 5481 / 3506 | $20,742 | $-469 | $-21.40 | $32.25 tot $853 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-468 over 5464 vullingen en $20,661, dus -2.27% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.30% over $20,361 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.32%.

**Opgeschaald (GOK):** per dag $4.03 (ondergrens) tot $145 (hoge schatting) netto (gemeten minuten × 1440 / 8396).

122 van de 5481 vullingen ($381) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.30%): $-8.77 (GOK).

Geld dat de bot nodig had: gemiddeld $3,753 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,773**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $93.24 tot $3,351 |
| €5,000 | $5,000 | $233 tot $8,377 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-21.40 over 3831 vullingen en $14,207, dus -0.15% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.26% per dollar over 5199 vullingen, 1 uur later -2.30% over 5089 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.40% per dollar over 265 vullingen, 1 uur later -2.01% over 259 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1564 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.54 tot $3.14 | $-0.74 tot $0.86 | 2 | $21.12 tot $39.71 | $39.17 tot $57.76 |
| €150 | 2 | $3.07 tot $6.28 | $-1.48 tot $1.73 | 3 | $29.95 tot $55.54 | $35.81 tot $61.41 |
| €200 | 3 | $4.61 tot $9.43 | $-2.22 tot $2.59 | 4 | $37.31 tot $68.08 | $46.03 tot $76.80 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.84%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $24.65 |
| highest hong-kong-on-november-24 22°C | 1464 | $4.44 tot $8.79 | 89 | $-20.19 | $61.12 |
| highest toronto-on-november-23 12°C | 1200 | $2.93 tot $5.19 | 44 | $-18.45 | $21.60 |
| highest tel-aviv-on-november-25 24°C | 1688 | $6.04 tot $12.55 | 32 | $-20.91 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $28.93 |
| ... | | | | | |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $0.00 |
| highest nyc-on-november-26 58-59°F | 1045 | $1.29 tot $2.38 | 11 | $20.32 | $0.00 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $44.02 tot $92.00 | 421 | $89.59 | $134 |
| seoul (highest) | $42.27 tot $89.95 | 775 | $0.17 | $42.45 |
| london (lowest) | $35.92 tot $65.51 | 208 | $-3.91 | $32.01 |
| miami (lowest) | $48.56 tot $84.67 | 118 | $-16.82 | $31.74 |
| chengdu (highest) | $40.81 tot $89.27 | 420 | $-14.58 | $26.23 |
| beijing (highest) | $34.85 tot $74.48 | 445 | $-12.77 | $22.08 |
| paris (lowest) | $42.00 tot $77.34 | 143 | $-25.98 | $16.02 |
| austin (highest) | $54.18 tot $113 | 568 | $-40.92 | $13.25 |
| wuhan (highest) | $40.54 tot $85.90 | 370 | $-28.89 | $11.65 |
| munich (highest) | $46.71 tot $98.37 | 693 | $-37.68 | $9.03 |
| mexico-city (highest) | $36.41 tot $71.08 | 251 | $-28.58 | $7.83 |
| jeddah (highest) | $22.29 tot $45.11 | 169 | $-14.52 | $7.77 |
| chongqing (highest) | $42.78 tot $89.29 | 355 | $-35.03 | $7.75 |
| karachi (highest) | $28.98 tot $57.41 | 235 | $-21.28 | $7.69 |
| manila (highest) | $24.26 tot $48.96 | 210 | $-16.92 | $7.34 |
| milan (highest) | $43.89 tot $89.95 | 608 | $-38.08 | $5.81 |
| kuala-lumpur (highest) | $28.30 tot $54.65 | 282 | $-23.46 | $4.84 |
| shanghai (lowest) | $11.89 tot $21.79 | 41 | $-7.06 | $4.83 |
| singapore (highest) | $41.12 tot $88.24 | 541 | $-36.94 | $4.19 |
| tokyo (highest) | $36.11 tot $79.44 | 648 | $-34.02 | $2.09 |
| nyc (lowest) | $13.87 tot $23.48 | 89 | $-12.78 | $1.09 |
| sao-paulo (highest) | $33.08 tot $65.75 | 371 | $-32.02 | $1.05 |
| london (highest) | $48.84 tot $107 | 972 | $-47.92 | $0.92 |
| seoul (lowest) | $25.59 tot $48.06 | 145 | $-25.87 | $-0.28 |
| nyc (highest) | $60.78 tot $125 | 979 | $-61.21 | $-0.43 |
| shenzhen (highest) | $31.43 tot $66.00 | 564 | $-32.37 | $-0.94 |
| moscow (highest) | $28.57 tot $57.26 | 346 | $-30.05 | $-1.47 |
| los-angeles (highest) | $42.34 tot $92.57 | 766 | $-45.65 | $-3.31 |
| buenos-aires (highest) | $31.03 tot $61.26 | 428 | $-38.48 | $-7.45 |
| qingdao (highest) | $25.00 tot $49.75 | 295 | $-32.79 | $-7.79 |
| tokyo (lowest) | $13.47 tot $22.88 | 66 | $-21.97 | $-8.50 |
| houston (highest) | $65.04 tot $133 | 918 | $-73.77 | $-8.73 |
| ankara (highest) | $32.95 tot $64.20 | 506 | $-46.06 | $-13.11 |
| taipei (highest) | $32.25 tot $60.12 | 353 | $-46.39 | $-14.14 |
| madrid (highest) | $43.31 tot $94.84 | 615 | $-59.33 | $-16.02 |
| miami (highest) | $52.38 tot $110 | 734 | $-69.54 | $-17.17 |
| shanghai (highest) | $42.69 tot $92.31 | 812 | $-59.91 | $-17.22 |
| chicago (highest) | $48.81 tot $91.60 | 769 | $-67.70 | $-18.89 |
| lucknow (highest) | $48.47 tot $100 | 509 | $-70.75 | $-22.29 |
| hong-kong (lowest) | $9.82 tot $17.65 | 177 | $-34.62 | $-24.79 |
| guangzhou (highest) | $47.61 tot $97.84 | 645 | $-72.76 | $-25.15 |
| amsterdam (highest) | $40.49 tot $88.40 | 719 | $-68.71 | $-28.21 |
| tel-aviv (highest) | $54.90 tot $117 | 440 | $-86.05 | $-31.15 |
| san-francisco (highest) | $36.68 tot $71.43 | 499 | $-68.09 | $-31.42 |
| busan (highest) | $41.36 tot $88.44 | 572 | $-90.85 | $-49.50 |
| dallas (highest) | $54.64 tot $115 | 738 | $-110 | $-54.91 |
| helsinki (highest) | $62.91 tot $128 | 855 | $-118 | $-54.92 |
| atlanta (highest) | $56.75 tot $119 | 1081 | $-115 | $-58.26 |
| toronto (highest) | $28.10 tot $55.64 | 505 | $-88.52 | $-60.42 |
| wellington (highest) | $38.34 tot $83.63 | 598 | $-101 | $-63.13 |
| hong-kong (highest) | $37.26 tot $78.77 | 947 | $-103 | $-65.87 |
| paris (highest) | $57.56 tot $125 | 1073 | $-135 | $-77.86 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
