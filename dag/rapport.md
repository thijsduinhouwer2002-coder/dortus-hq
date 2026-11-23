# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.29 tot $1.88 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 18 runs, 6047 minuten (100.8 uur) (GEZIEN). Markten in de data: 2917. Uitslag bekend voor 1716 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-86.50 (3553 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-224 (366 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 890 | 181 | $3,436 | $8,779 | $214 tot $435 | 3211 / 2438 | $10,484 | $-287 (271 nog zonder prijs) | $0.00 (0 van 3211 beslist) | $-72.84 tot $148 |
| **Totaal** | 6047 | | $4,138 | $10,171 | $1,539 tot $3,157 | 19492 / 14123 | $62,819 | $-1,888 | $-1,178 | $-348 tot $1,269 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,445 over 19443 vullingen en $62,668, dus -2.31% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.08% over $61,357 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.99%.

**Opgeschaald (GOK):** per dag $-93.65 (ondergrens) tot $292 (hoge schatting) netto (gemeten minuten × 1440 / 6047).

532 van de 19492 vullingen ($1,462) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.08%): $-44.97 (GOK).

Geld dat de bot nodig had: gemiddeld $4,138 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,309**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,178 tot $3,668 |
| €5,000 | $5,000 | $-2,945 tot $9,169 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,178 over 10980 vullingen en $35,919, dus -3.28% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.22% per dollar over 18650 vullingen, 1 uur later -3.00% over 18149 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.15% per dollar over 793 vullingen, 1 uur later -4.72% over 782 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $106 (698 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-30.84 (95 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 890 | 181 | $3,370 | $3,881 | $52.88 tot $141 | 772 / 516 | $3,033 | $-73.92 (59 nog zonder prijs) | $0.00 (0 van 772 beslist) | $-21.04 tot $67.05 |
| **Totaal** | 6047 | | $4,067 | $4,020 | $378 tot $991 | 3846 / 2501 | $14,272 | $-368 | $136 | $9.97 tot $624 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-357 over 3830 vullingen en $14,208, dus -2.51% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.66% over $13,845 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.88%.

**Opgeschaald (GOK):** per dag $-0.33 (ondergrens) tot $146 (hoge schatting) netto (gemeten minuten × 1440 / 6047).

121 van de 3846 vullingen ($428) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.66%): $-11.37 (GOK).

Geld dat de bot nodig had: gemiddeld $4,067 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,087**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-7.38 tot $3,246 |
| €5,000 | $5,000 | $-18.44 tot $8,114 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $136 over 2034 vullingen en $7,475, dus +1.81% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.51% per dollar over 3630 vullingen, 1 uur later -2.71% over 3518 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.55% per dollar over 200 vullingen, 1 uur later -1.23% over 198 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1260 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.55 tot $3.13 | $-0.64 tot $0.94 | 2 | $24.09 tot $33.26 | $-106 tot $-96.76 |
| €150 | 2 | $3.09 tot $6.26 | $-1.29 tot $1.88 | 3 | $35.46 tot $55.27 | $-100 tot $-80.27 |
| €200 | 3 | $4.64 tot $9.39 | $-1.93 tot $2.82 | 4 | $44.47 tot $70.89 | $-91.64 tot $-65.22 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-3.08%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $0.00 |
| highest toronto-on-november-23 12°C | 1200 | $2.93 tot $5.19 | 44 | $-18.45 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $28.93 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $-14.69 |
| lowest seoul-on-november-23 3°C | 720 | $0.81 tot $1.65 | 27 | $-14.61 | $0.00 |
| highest atlanta-on-november-22 61°F or below | 1305 | $1.47 tot $3.28 | 60 | $-15.20 | $8.29 |
| highest hong-kong-on-november-24 22°C | 1406 | $4.07 tot $8.07 | 79 | $-17.70 | $0.00 |
| ... | | | | | |
| highest austin-on-november-22 74-75°F | 2464 | $4.94 tot $9.96 | 32 | $0.59 | $15.35 |
| lowest miami-on-november-22 72-73°F | 1769 | $5.03 tot $8.87 | 9 | $1.29 | $14.94 |
| highest warsaw-on-november-22 4°C | 2271 | $4.51 tot $9.55 | 43 | $2.34 | $23.20 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest warsaw-on-november-25 6°C or higher | 74 | $0.20 tot $0.30 | 8 | $17.58 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| miami (lowest) | $37.97 tot $66.81 | 92 | $-5.68 | $32.29 |
| warsaw (highest) | $37.54 tot $79.10 | 377 | $-8.69 | $28.85 |
| chengdu (highest) | $30.37 tot $66.65 | 302 | $-10.00 | $20.38 |
| london (lowest) | $27.66 tot $51.41 | 167 | $-10.71 | $16.95 |
| austin (highest) | $43.56 tot $91.11 | 426 | $-30.42 | $13.14 |
| beijing (highest) | $25.96 tot $55.20 | 318 | $-13.42 | $12.54 |
| shenzhen (highest) | $21.65 tot $45.96 | 389 | $-9.73 | $11.92 |
| manila (highest) | $18.18 tot $36.14 | 150 | $-7.89 | $10.29 |
| taipei (highest) | $25.23 tot $46.61 | 266 | $-15.07 | $10.16 |
| kuala-lumpur (highest) | $23.95 tot $45.96 | 226 | $-14.07 | $9.88 |
| jeddah (highest) | $18.66 tot $37.63 | 122 | $-8.90 | $9.76 |
| los-angeles (highest) | $27.72 tot $62.17 | 511 | $-18.14 | $9.58 |
| paris (lowest) | $31.47 tot $57.76 | 103 | $-22.97 | $8.51 |
| chongqing (highest) | $30.64 tot $63.96 | 251 | $-22.86 | $7.78 |
| karachi (highest) | $22.87 tot $44.98 | 150 | $-15.14 | $7.74 |
| tokyo (highest) | $27.34 tot $60.05 | 488 | $-19.88 | $7.46 |
| wuhan (highest) | $27.09 tot $58.34 | 238 | $-20.76 | $6.33 |
| milan (highest) | $31.26 tot $63.52 | 399 | $-25.15 | $6.11 |
| houston (highest) | $46.36 tot $96.51 | 663 | $-41.04 | $5.31 |
| mexico-city (highest) | $29.21 tot $56.05 | 167 | $-24.02 | $5.19 |
| sao-paulo (highest) | $22.07 tot $44.31 | 261 | $-17.16 | $4.91 |
| shanghai (lowest) | $11.87 tot $21.74 | 41 | $-7.06 | $4.81 |
| singapore (highest) | $30.22 tot $64.91 | 410 | $-26.19 | $4.03 |
| munich (highest) | $32.72 tot $69.76 | 491 | $-31.00 | $1.72 |
| nyc (lowest) | $13.17 tot $22.41 | 88 | $-13.22 | $-0.05 |
| seoul (highest) | $31.88 tot $67.29 | 573 | $-32.32 | $-0.44 |
| buenos-aires (highest) | $24.10 tot $46.50 | 288 | $-25.16 | $-1.05 |
| seoul (lowest) | $19.44 tot $36.53 | 104 | $-21.55 | $-2.12 |
| moscow (highest) | $24.16 tot $48.20 | 227 | $-27.58 | $-3.42 |
| london (highest) | $37.05 tot $80.71 | 733 | $-42.01 | $-4.96 |
| tokyo (lowest) | $13.40 tot $22.78 | 65 | $-19.69 | $-6.29 |
| tel-aviv (highest) | $37.15 tot $80.03 | 325 | $-44.93 | $-7.78 |
| ankara (highest) | $25.95 tot $50.61 | 367 | $-36.24 | $-10.29 |
| nyc (highest) | $46.79 tot $98.27 | 867 | $-57.74 | $-10.95 |
| lucknow (highest) | $35.70 tot $73.98 | 335 | $-49.17 | $-13.47 |
| chicago (highest) | $40.58 tot $75.77 | 583 | $-56.42 | $-15.84 |
| qingdao (highest) | $20.68 tot $41.18 | 231 | $-36.60 | $-15.92 |
| amsterdam (highest) | $28.97 tot $63.93 | 554 | $-45.81 | $-16.84 |
| guangzhou (highest) | $37.08 tot $75.54 | 499 | $-54.03 | $-16.95 |
| hong-kong (lowest) | $8.26 tot $14.64 | 134 | $-27.75 | $-19.50 |
| miami (highest) | $36.72 tot $77.38 | 493 | $-57.74 | $-21.02 |
| madrid (highest) | $31.44 tot $69.71 | 427 | $-52.48 | $-21.04 |
| san-francisco (highest) | $29.80 tot $58.20 | 362 | $-55.70 | $-25.90 |
| shanghai (highest) | $30.26 tot $66.17 | 484 | $-57.57 | $-27.32 |
| hong-kong (highest) | $27.68 tot $58.37 | 711 | $-56.01 | $-28.34 |
| atlanta (highest) | $44.29 tot $93.77 | 833 | $-78.88 | $-34.59 |
| busan (highest) | $33.73 tot $71.17 | 452 | $-71.67 | $-37.94 |
| toronto (highest) | $24.32 tot $47.73 | 427 | $-63.69 | $-39.37 |
| paris (highest) | $42.08 tot $91.23 | 726 | $-90.55 | $-48.47 |
| helsinki (highest) | $43.60 tot $89.98 | 599 | $-100 | $-56.83 |
| dallas (highest) | $40.42 tot $84.93 | 542 | $-98.44 | $-58.01 |
| wellington (highest) | $28.98 tot $63.22 | 455 | $-88.20 | $-59.22 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
