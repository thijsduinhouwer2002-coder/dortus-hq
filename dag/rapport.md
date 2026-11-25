# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.64 tot $1.86 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 26 runs, 8731 minuten (145.5 uur) (GEZIEN). Markten in de data: 4016. Uitslag bekend voor 2816 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $275 (3776 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $16.76 (261 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 708 | 170 | $3,189 | $7,388 | $212 tot $448 | 2491 / 1620 | $8,961 | $-336 (235 nog zonder prijs) | $0.00 (0 van 2491 beslist) | $-123 tot $112 |
| **Totaal** | 8731 | | $3,798 | $10,171 | $2,167 tot $4,453 | 27926 / 20003 | $91,367 | $-2,634 | $-1,383 | $-467 tot $1,819 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,967 over 27876 vullingen en $91,223, dus -2.16% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.94% over $89,733 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.75%.

**Opgeschaald (GOK):** per dag $-84.94 (ondergrens) tot $292 (hoge schatting) netto (gemeten minuten × 1440 / 8731).

569 van de 27926 vullingen ($1,634) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.94%): $-47.98 (GOK).

Geld dat de bot nodig had: gemiddeld $3,798 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,969**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,094 tot $3,764 |
| €5,000 | $5,000 | $-2,736 tot $9,409 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,383 over 20318 vullingen en $65,267, dus -2.12% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.07% per dollar over 26799 vullingen, 1 uur later -2.86% over 26271 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.09% per dollar over 1077 vullingen, 1 uur later -4.62% over 1046 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $341 (909 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $27.37 (55 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 708 | 170 | $3,161 | $3,577 | $49.09 tot $135 | 592 / 383 | $2,517 | $-90.79 (70 nog zonder prijs) | $0.00 (0 van 592 beslist) | $-41.70 tot $44.00 |
| **Totaal** | 8731 | | $3,739 | $4,020 | $531 tot $1,405 | 5819 / 3735 | $22,210 | $-527 | $78.80 | $4.33 tot $878 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-525 over 5805 vullingen en $22,154, dus -2.37% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.42% over $21,761 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.41%.

**Opgeschaald (GOK):** per dag $-1.08 (ondergrens) tot $143 (hoge schatting) netto (gemeten minuten × 1440 / 8731).

146 van de 5819 vullingen ($449) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.42%): $-10.89 (GOK).

Geld dat de bot nodig had: gemiddeld $3,739 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,759**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-25.11 tot $3,319 |
| €5,000 | $5,000 | $-62.77 tot $8,297 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $78.80 over 4038 vullingen en $14,901, dus +0.53% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.36% per dollar over 5507 vullingen, 1 uur later -2.41% over 5374 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.53% per dollar over 298 vullingen, 1 uur later -2.50% over 288 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1650 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.67 tot $3.41 | $-0.82 tot $0.93 | 2 | $44.26 tot $88.71 | $-110 tot $-65.06 |
| €150 | 2 | $3.33 tot $6.83 | $-1.64 tot $1.86 | 3 | $65.02 tot $129 | $-128 tot $-64.66 |
| €200 | 3 | $5.00 tot $10.24 | $-2.46 tot $2.79 | 4 | $78.79 tot $157 | $-119 tot $-41.03 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.94%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest paris-on-november-26 6°C | 1416 | $6.17 tot $13.23 | 59 | $-33.03 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest helsinki-on-november-26 -1°C | 1006 | $3.94 tot $7.77 | 49 | $-21.48 | $0.00 |
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
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $0.00 |
| highest nyc-on-november-26 58-59°F | 2176 | $3.85 tot $7.16 | 32 | $13.46 | $0.00 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $44.92 tot $93.72 | 424 | $91.16 | $136 |
| seoul (highest) | $52.30 tot $114 | 831 | $-9.79 | $42.51 |
| miami (lowest) | $49.55 tot $86.59 | 129 | $-16.80 | $32.75 |
| london (lowest) | $38.19 tot $69.87 | 210 | $-5.77 | $32.42 |
| chengdu (highest) | $43.13 tot $94.50 | 443 | $-14.37 | $28.77 |
| beijing (highest) | $36.02 tot $77.24 | 481 | $-11.46 | $24.56 |
| paris (lowest) | $44.04 tot $81.46 | 149 | $-25.55 | $18.49 |
| wuhan (highest) | $42.58 tot $90.29 | 382 | $-29.02 | $13.56 |
| austin (highest) | $56.77 tot $119 | 606 | $-46.26 | $10.51 |
| manila (highest) | $25.26 tot $50.94 | 227 | $-16.05 | $9.20 |
| karachi (highest) | $30.18 tot $59.72 | 239 | $-21.17 | $9.01 |
| chongqing (highest) | $44.03 tot $92.06 | 367 | $-35.11 | $8.93 |
| jeddah (highest) | $23.21 tot $46.79 | 176 | $-15.86 | $7.35 |
| munich (highest) | $52.29 tot $111 | 756 | $-45.20 | $7.09 |
| mexico-city (highest) | $37.01 tot $72.26 | 259 | $-30.13 | $6.88 |
| tokyo (highest) | $43.15 tot $95.76 | 711 | $-36.76 | $6.39 |
| singapore (highest) | $42.69 tot $91.54 | 558 | $-36.81 | $5.89 |
| shanghai (lowest) | $11.92 tot $21.83 | 41 | $-7.06 | $4.86 |
| london (highest) | $51.02 tot $111 | 997 | $-46.83 | $4.20 |
| milan (highest) | $45.31 tot $92.80 | 629 | $-42.01 | $3.30 |
| sao-paulo (highest) | $34.04 tot $67.64 | 381 | $-31.32 | $2.72 |
| nyc (lowest) | $14.05 tot $23.84 | 89 | $-12.78 | $1.27 |
| shenzhen (highest) | $32.60 tot $68.71 | 576 | $-31.85 | $0.75 |
| kuala-lumpur (highest) | $29.42 tot $56.73 | 333 | $-29.26 | $0.15 |
| los-angeles (highest) | $44.26 tot $96.73 | 789 | $-44.38 | $-0.13 |
| seoul (lowest) | $27.21 tot $51.09 | 151 | $-28.56 | $-1.35 |
| nyc (highest) | $63.33 tot $129 | 1000 | $-68.07 | $-4.74 |
| qingdao (highest) | $26.19 tot $52.00 | 312 | $-31.51 | $-5.32 |
| buenos-aires (highest) | $35.17 tot $70.97 | 454 | $-41.96 | $-6.78 |
| moscow (highest) | $30.19 tot $60.44 | 365 | $-38.03 | $-7.83 |
| houston (highest) | $67.09 tot $137 | 948 | $-75.40 | $-8.32 |
| tokyo (lowest) | $13.49 tot $22.92 | 66 | $-21.97 | $-8.48 |
| ankara (highest) | $33.97 tot $66.14 | 520 | $-46.91 | $-12.95 |
| taipei (highest) | $33.39 tot $62.31 | 361 | $-47.00 | $-13.62 |
| madrid (highest) | $44.65 tot $97.64 | 631 | $-59.80 | $-15.15 |
| shanghai (highest) | $44.34 tot $95.81 | 841 | $-61.36 | $-17.02 |
| lucknow (highest) | $50.31 tot $104 | 526 | $-72.71 | $-22.41 |
| chicago (highest) | $49.93 tot $93.90 | 783 | $-73.70 | $-23.77 |
| guangzhou (highest) | $49.50 tot $102 | 679 | $-74.40 | $-24.90 |
| miami (highest) | $54.89 tot $115 | 779 | $-81.82 | $-26.93 |
| amsterdam (highest) | $42.83 tot $93.37 | 741 | $-71.47 | $-28.65 |
| hong-kong (lowest) | $18.08 tot $34.43 | 243 | $-50.43 | $-32.35 |
| san-francisco (highest) | $38.06 tot $74.16 | 522 | $-72.08 | $-34.02 |
| tel-aviv (highest) | $56.07 tot $120 | 455 | $-92.45 | $-36.38 |
| busan (highest) | $58.59 tot $123 | 676 | $-107 | $-48.27 |
| dallas (highest) | $55.61 tot $117 | 750 | $-115 | $-59.27 |
| hong-kong (highest) | $38.46 tot $81.39 | 977 | $-102 | $-63.39 |
| atlanta (highest) | $58.24 tot $123 | 1108 | $-122 | $-63.42 |
| toronto (highest) | $28.91 tot $57.53 | 515 | $-93.30 | $-64.39 |
| helsinki (highest) | $66.39 tot $135 | 903 | $-134 | $-67.12 |
| wellington (highest) | $41.26 tot $90.07 | 646 | $-116 | $-75.04 |
| paris (highest) | $73.39 tot $159 | 1191 | $-186 | $-113 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
