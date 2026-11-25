# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.42 tot $2.24 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 27 runs, 9067 minuten (151.1 uur) (GEZIEN). Markten in de data: 4016. Uitslag bekend voor 3003 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $61.65 (4286 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $-10.56 (1157 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1044 | 177 | $3,335 | $7,404 | $349 tot $738 | 3921 / 2514 | $13,939 | $-424 (270 nog zonder prijs) | $0.00 (0 van 3921 beslist) | $-75.34 tot $314 |
| **Totaal** | 9067 | | $3,792 | $10,171 | $2,304 tot $4,743 | 29356 / 20897 | $96,345 | $-2,723 | $-1,623 | $-419 tot $2,020 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-2,078 over 29283 vullingen en $96,125, dus -2.16% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.88% over $94,511 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.72%.

**Opgeschaald (GOK):** per dag $-74.93 (ondergrens) tot $312 (hoge schatting) netto (gemeten minuten × 1440 / 9067).

604 van de 29356 vullingen ($1,835) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.88%): $-52.86 (GOK).

Geld dat de bot nodig had: gemiddeld $3,792 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,963**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-966 tot $4,028 |
| €5,000 | $5,000 | $-2,415 tot $10,069 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,623 over 21724 vullingen en $69,535, dus -2.33% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.07% per dollar over 28036 vullingen, 1 uur later -2.80% over 27511 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.17% per dollar over 1247 vullingen, 1 uur later -4.51% over 1199 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $288 (1016 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $91.57 (218 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1044 | 177 | $3,294 | $3,833 | $80.31 tot $219 | 899 / 589 | $3,783 | $-98.38 (73 nog zonder prijs) | $0.00 (0 van 899 beslist) | $-18.07 tot $120 |
| **Totaal** | 9067 | | $3,733 | $4,020 | $563 tot $1,489 | 6126 / 3941 | $23,476 | $-535 | $90.42 | $27.95 tot $954 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-560 over 6101 vullingen en $23,383, dus -2.40% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.33% over $22,981 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.31%.

**Opgeschaald (GOK):** per dag $2.61 (ondergrens) tot $150 (hoge schatting) netto (gemeten minuten × 1440 / 9067).

149 van de 6126 vullingen ($494) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.33%): $-11.50 (GOK).

Geld dat de bot nodig had: gemiddeld $3,733 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,753**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $60.66 tot $3,477 |
| €5,000 | $5,000 | $152 tot $8,692 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $90.42 over 4308 vullingen en $15,894, dus +0.57% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.39% per dollar over 5763 vullingen, 1 uur later -2.28% over 5636 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.46% per dollar over 338 vullingen, 1 uur later -2.91% over 330 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1718 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.75 tot $3.58 | $-0.71 tot $1.12 | 2 | $55.27 tot $85.26 | $3.08 tot $33.07 |
| €150 | 2 | $3.49 tot $7.16 | $-1.42 tot $2.24 | 3 | $73.44 tot $123 | $17.98 tot $67.19 |
| €200 | 3 | $5.24 tot $10.73 | $-2.13 tot $3.36 | 5 | $103 tot $186 | $-11.52 tot $70.99 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.88%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest paris-on-november-26 6°C | 1752 | $7.84 tot $17.15 | 76 | $-33.69 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $0.00 |
| highest paris-on-november-26 7°C | 1206 | $6.07 tot $14.08 | 67 | $-24.65 | $0.00 |
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
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $0.00 |
| highest nyc-on-november-26 58-59°F | 3520 | $6.58 tot $12.38 | 39 | $13.73 | $0.00 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $47.44 tot $98.36 | 428 | $88.26 | $136 |
| seoul (highest) | $60.21 tot $131 | 881 | $-20.13 | $40.08 |
| chengdu (highest) | $47.15 tot $103 | 494 | $-11.97 | $35.18 |
| london (lowest) | $40.26 tot $73.58 | 217 | $-5.80 | $34.46 |
| miami (lowest) | $50.65 tot $88.52 | 139 | $-19.72 | $30.93 |
| beijing (highest) | $37.81 tot $80.98 | 510 | $-8.46 | $29.35 |
| paris (lowest) | $45.39 tot $84.00 | 155 | $-26.15 | $19.24 |
| munich (highest) | $61.64 tot $132 | 836 | $-45.23 | $16.40 |
| wuhan (highest) | $45.11 tot $95.67 | 406 | $-29.21 | $15.91 |
| tokyo (highest) | $49.39 tot $110 | 751 | $-33.66 | $15.73 |
| austin (highest) | $58.60 tot $122 | 661 | $-46.35 | $12.25 |
| chongqing (highest) | $46.09 tot $96.31 | 382 | $-35.50 | $10.59 |
| karachi (highest) | $31.05 tot $61.48 | 240 | $-21.28 | $9.76 |
| manila (highest) | $26.47 tot $53.24 | 248 | $-17.38 | $9.09 |
| jeddah (highest) | $23.80 tot $48.01 | 182 | $-15.93 | $7.87 |
| mexico-city (highest) | $37.69 tot $73.77 | 266 | $-29.82 | $7.87 |
| singapore (highest) | $43.81 tot $94.15 | 573 | $-38.12 | $5.69 |
| shenzhen (highest) | $33.50 tot $70.92 | 597 | $-29.95 | $3.55 |
| sao-paulo (highest) | $34.72 tot $69.00 | 385 | $-31.18 | $3.54 |
| london (highest) | $54.83 tot $119 | 1055 | $-51.45 | $3.38 |
| seoul (lowest) | $28.06 tot $52.53 | 167 | $-26.02 | $2.04 |
| kuala-lumpur (highest) | $30.60 tot $59.02 | 348 | $-29.37 | $1.23 |
| los-angeles (highest) | $45.21 tot $98.90 | 802 | $-44.45 | $0.76 |
| nyc (lowest) | $14.52 tot $24.90 | 110 | $-13.79 | $0.72 |
| shanghai (lowest) | $12.67 tot $23.30 | 61 | $-12.20 | $0.47 |
| nyc (highest) | $66.06 tot $135 | 1007 | $-67.79 | $-1.73 |
| buenos-aires (highest) | $39.47 tot $81.11 | 492 | $-41.51 | $-2.04 |
| milan (highest) | $48.27 tot $98.78 | 683 | $-51.25 | $-2.98 |
| qingdao (highest) | $26.89 tot $53.36 | 321 | $-34.45 | $-7.56 |
| moscow (highest) | $31.17 tot $62.38 | 377 | $-39.58 | $-8.41 |
| tokyo (lowest) | $14.08 tot $24.13 | 67 | $-23.17 | $-9.09 |
| houston (highest) | $68.90 tot $141 | 976 | $-79.39 | $-10.50 |
| ankara (highest) | $35.09 tot $68.24 | 530 | $-46.91 | $-11.83 |
| madrid (highest) | $48.26 tot $105 | 672 | $-60.59 | $-12.33 |
| taipei (highest) | $34.71 tot $64.92 | 378 | $-47.46 | $-12.75 |
| shanghai (highest) | $45.72 tot $99.11 | 883 | $-65.92 | $-20.20 |
| chicago (highest) | $50.54 tot $95.25 | 796 | $-73.15 | $-22.61 |
| lucknow (highest) | $53.89 tot $110 | 574 | $-76.98 | $-23.09 |
| guangzhou (highest) | $50.90 tot $105 | 701 | $-74.19 | $-23.29 |
| amsterdam (highest) | $45.28 tot $98.43 | 798 | $-72.94 | $-27.66 |
| miami (highest) | $56.62 tot $118 | 808 | $-85.94 | $-29.32 |
| tel-aviv (highest) | $59.70 tot $127 | 486 | $-89.82 | $-30.13 |
| hong-kong (lowest) | $27.39 tot $54.21 | 336 | $-62.29 | $-34.90 |
| san-francisco (highest) | $38.73 tot $75.45 | 540 | $-74.51 | $-35.78 |
| busan (highest) | $71.89 tot $151 | 737 | $-121 | $-49.38 |
| dallas (highest) | $57.19 tot $121 | 781 | $-116 | $-59.21 |
| helsinki (highest) | $70.42 tot $143 | 951 | $-131 | $-60.25 |
| hong-kong (highest) | $39.71 tot $84.09 | 1005 | $-101 | $-61.63 |
| atlanta (highest) | $59.38 tot $125 | 1117 | $-122 | $-62.73 |
| toronto (highest) | $29.58 tot $59.02 | 529 | $-95.69 | $-66.11 |
| wellington (highest) | $42.64 tot $93.23 | 660 | $-116 | $-73.83 |
| paris (highest) | $84.80 tot $185 | 1257 | $-196 | $-111 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
