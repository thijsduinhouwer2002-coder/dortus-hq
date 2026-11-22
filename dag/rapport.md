# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.28 tot $1.93 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 13 runs, 4371 minuten (72.8 uur) (GEZIEN). Markten in de data: 2377. Uitslag bekend voor 1089 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-506 (2812 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-154 (2699 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $90.13 (308 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 646 | 188 | $3,559 | $9,224 | $150 tot $305 | 1907 / 1429 | $6,298 | $-255 (136 nog zonder prijs) | $0.00 (0 van 1907 beslist) | $-105 tot $49.61 |
| **Totaal** | 4371 | | $4,366 | $10,171 | $1,123 tot $2,318 | 13766 / 9768 | $44,332 | $-1,366 | $-570 | $-243 tot $952 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,044 over 13735 vullingen en $44,242, dus -2.36% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.15% over $43,319 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -4.08%.

**Opgeschaald (GOK):** per dag $-90.54 (ondergrens) tot $303 (hoge schatting) netto (gemeten minuten × 1440 / 4371).

361 van de 13766 vullingen ($1,013) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.15%): $-31.96 (GOK).

Geld dat de bot nodig had: gemiddeld $4,366 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,537**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,121 tot $3,752 |
| €5,000 | $5,000 | $-2,803 tot $9,381 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-570 over 5819 vullingen en $19,106, dus -2.98% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.25% per dollar over 13092 vullingen, 1 uur later -3.05% over 12747 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.56% per dollar over 643 vullingen, 1 uur later -5.07% over 632 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-50.76 (443 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $-11.39 (468 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-6.06 (50 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 646 | 188 | $3,492 | $3,842 | $36.82 tot $97.68 | 394 / 258 | $1,471 | $-54.06 (35 nog zonder prijs) | $0.00 (0 van 394 beslist) | $-17.24 tot $43.62 |
| **Totaal** | 4371 | | $4,293 | $4,020 | $273 tot $714 | 2601 / 1694 | $9,470 | $-276 | $-68.21 | $-3.25 tot $438 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-273 over 2590 vullingen en $9,418, dus -2.90% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.99% over $9,227 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -4.02%.

**Opgeschaald (GOK):** per dag $-3.47 (ondergrens) tot $142 (hoge schatting) netto (gemeten minuten × 1440 / 4371).

86 van de 2601 vullingen ($244) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.99%): $-7.29 (GOK).

Geld dat de bot nodig had: gemiddeld $4,293 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,313**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-75.21 tot $3,075 |
| €5,000 | $5,000 | $-188 tot $7,688 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-68.21 over 961 vullingen en $3,541, dus -1.93% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.95% per dollar over 2425 vullingen, 1 uur later -3.12% over 2343 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.05% per dollar over 165 vullingen, 1 uur later -0.61% over 163 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1000 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.54 tot $3.14 | $-0.64 tot $0.97 | 2 | $19.50 tot $34.28 | $-42.79 tot $-28.00 |
| €150 | 2 | $3.08 tot $6.28 | $-1.28 tot $1.93 | 3 | $28.87 tot $54.07 | $-34.80 tot $-9.60 |
| €200 | 3 | $4.61 tot $9.43 | $-1.91 tot $2.90 | 5 | $40.85 tot $78.55 | $-103 tot $-65.53 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-3.15%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1564 | $4.66 tot $9.52 | 69 | $-35.22 | $0.00 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $0.00 |
| highest wellington-on-november-23 18°C | 1564 | $4.31 tot $8.97 | 55 | $-19.00 | $0.00 |
| highest helsinki-on-november-23 2°C | 1057 | $3.43 tot $6.30 | 28 | $-17.62 | $0.00 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $0.00 |
| lowest seoul-on-november-23 3°C | 720 | $0.81 tot $1.65 | 27 | $-14.61 | $0.00 |
| highest atlanta-on-november-22 61°F or below | 1305 | $1.47 tot $3.28 | 60 | $-15.20 | $0.00 |
| highest chicago-on-november-22 60-61°F | 2273 | $3.53 tot $6.65 | 56 | $-15.90 | $0.00 |
| highest helsinki-on-november-23 1°C | 1040 | $3.19 tot $6.08 | 28 | $-15.29 | $0.00 |
| ... | | | | | |
| highest paris-on-november-22 8°C | 2322 | $3.46 tot $7.90 | 59 | $1.45 | $0.00 |
| highest austin-on-november-22 74-75°F | 2464 | $4.94 tot $9.96 | 32 | $0.59 | $0.00 |
| lowest miami-on-november-22 72-73°F | 1769 | $5.03 tot $8.87 | 9 | $1.29 | $0.00 |
| highest warsaw-on-november-22 4°C | 2271 | $4.51 tot $9.55 | 43 | $2.34 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $0.00 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| miami (lowest) | $27.39 tot $48.58 | 61 | $-4.44 | $22.95 |
| chengdu (highest) | $22.28 tot $49.90 | 193 | $-6.51 | $15.77 |
| austin (highest) | $33.95 tot $71.60 | 317 | $-18.82 | $15.12 |
| seoul (highest) | $20.12 tot $43.69 | 256 | $-5.73 | $14.38 |
| london (lowest) | $20.65 tot $38.39 | 121 | $-6.63 | $14.03 |
| beijing (highest) | $18.23 tot $39.25 | 208 | $-6.75 | $11.49 |
| manila (highest) | $13.69 tot $27.07 | 109 | $-4.66 | $9.03 |
| kuala-lumpur (highest) | $18.32 tot $35.42 | 175 | $-9.33 | $8.98 |
| los-angeles (highest) | $17.48 tot $40.32 | 371 | $-9.08 | $8.39 |
| milan (highest) | $24.71 tot $49.59 | 301 | $-16.36 | $8.35 |
| warsaw (highest) | $26.84 tot $57.37 | 262 | $-19.18 | $7.66 |
| chongqing (highest) | $19.54 tot $41.63 | 168 | $-12.51 | $7.04 |
| taipei (highest) | $19.09 tot $34.59 | 148 | $-12.69 | $6.40 |
| jeddah (highest) | $15.91 tot $32.01 | 88 | $-9.61 | $6.30 |
| shanghai (lowest) | $11.85 tot $21.71 | 41 | $-7.06 | $4.79 |
| london (highest) | $23.68 tot $53.43 | 489 | $-19.53 | $4.15 |
| wuhan (highest) | $19.82 tot $43.59 | 161 | $-15.88 | $3.94 |
| karachi (highest) | $17.18 tot $33.38 | 110 | $-13.54 | $3.64 |
| mexico-city (highest) | $22.86 tot $44.40 | 138 | $-19.86 | $3.01 |
| sao-paulo (highest) | $18.10 tot $35.89 | 214 | $-15.23 | $2.87 |
| nyc (lowest) | $10.83 tot $18.48 | 75 | $-8.43 | $2.40 |
| houston (highest) | $34.40 tot $72.03 | 496 | $-33.62 | $0.79 |
| munich (highest) | $22.92 tot $49.14 | 340 | $-22.62 | $0.29 |
| singapore (highest) | $19.10 tot $42.09 | 305 | $-18.87 | $0.23 |
| lucknow (highest) | $25.53 tot $53.31 | 227 | $-26.59 | $-1.06 |
| buenos-aires (highest) | $18.16 tot $35.87 | 227 | $-19.50 | $-1.34 |
| paris (lowest) | $21.84 tot $40.89 | 85 | $-23.78 | $-1.94 |
| amsterdam (highest) | $21.82 tot $48.33 | 401 | $-23.97 | $-2.16 |
| toronto (highest) | $18.47 tot $36.91 | 248 | $-20.71 | $-2.24 |
| shenzhen (highest) | $15.87 tot $34.00 | 271 | $-18.13 | $-2.26 |
| tokyo (highest) | $18.09 tot $41.08 | 309 | $-20.60 | $-2.50 |
| paris (highest) | $25.18 tot $55.98 | 457 | $-28.71 | $-3.52 |
| seoul (lowest) | $15.24 tot $28.23 | 89 | $-20.31 | $-5.08 |
| ankara (highest) | $18.88 tot $37.09 | 249 | $-24.85 | $-5.97 |
| tokyo (lowest) | $11.24 tot $19.45 | 49 | $-17.38 | $-6.14 |
| hong-kong (highest) | $19.39 tot $41.52 | 432 | $-28.55 | $-9.17 |
| tel-aviv (highest) | $25.88 tot $55.46 | 223 | $-35.42 | $-9.54 |
| moscow (highest) | $19.95 tot $39.62 | 185 | $-30.68 | $-10.73 |
| nyc (highest) | $34.39 tot $71.47 | 613 | $-45.56 | $-11.17 |
| hong-kong (lowest) | $7.79 tot $13.99 | 123 | $-19.89 | $-12.10 |
| qingdao (highest) | $15.91 tot $31.70 | 145 | $-28.46 | $-12.55 |
| guangzhou (highest) | $28.13 tot $57.06 | 400 | $-40.75 | $-12.62 |
| miami (highest) | $27.93 tot $59.32 | 358 | $-42.31 | $-14.38 |
| madrid (highest) | $22.19 tot $50.09 | 312 | $-42.54 | $-20.35 |
| shanghai (highest) | $19.04 tot $42.53 | 303 | $-41.53 | $-22.49 |
| chicago (highest) | $32.10 tot $60.55 | 485 | $-55.48 | $-23.38 |
| san-francisco (highest) | $24.65 tot $48.80 | 318 | $-48.31 | $-23.67 |
| busan (highest) | $21.34 tot $46.42 | 240 | $-49.65 | $-28.32 |
| atlanta (highest) | $32.03 tot $68.71 | 712 | $-66.49 | $-34.45 |
| helsinki (highest) | $32.01 tot $66.59 | 412 | $-73.68 | $-41.67 |
| wellington (highest) | $22.40 tot $48.61 | 345 | $-69.95 | $-47.55 |
| dallas (highest) | $28.92 tot $60.80 | 401 | $-85.41 | $-56.49 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
