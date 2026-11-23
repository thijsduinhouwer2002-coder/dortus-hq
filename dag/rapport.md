# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-0.77 tot $2.40 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 19 runs, 6382 minuten (106.4 uur) (GEZIEN). Markten in de data: 2917. Uitslag bekend voor 1914 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-219 (3922 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-202 (1200 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1225 | 172 | $3,265 | $8,779 | $289 tot $582 | 4290 / 3252 | $13,778 | $-347 (201 nog zonder prijs) | $0.00 (0 van 4290 beslist) | $-58.21 tot $235 |
| **Totaal** | 6382 | | $4,068 | $10,171 | $1,614 tot $3,304 | 20571 / 14937 | $66,112 | $-1,948 | $-1,289 | $-334 tot $1,357 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,477 over 20532 vullingen en $65,990, dus -2.24% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.00% over $64,858 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.88%.

**Opgeschaald (GOK):** per dag $-83.78 (ondergrens) tot $298 (hoge schatting) netto (gemeten minuten × 1440 / 6382).

462 van de 20571 vullingen ($1,254) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.00%): $-37.66 (GOK).

Geld dat de bot nodig had: gemiddeld $4,068 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,239**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,059 tot $3,762 |
| €5,000 | $5,000 | $-2,648 tot $9,405 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,289 over 12183 vullingen en $39,507, dus -3.26% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.15% per dollar over 19721 vullingen, 1 uur later -2.92% over 19281 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.17% per dollar over 811 vullingen, 1 uur later -4.81% over 797 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-11.70 (770 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-6.36 (232 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1225 | 172 | $3,210 | $3,931 | $73.77 tot $194 | 1039 / 694 | $3,952 | $-97.42 (43 nog zonder prijs) | $0.00 (0 van 1039 beslist) | $-23.65 tot $96.69 |
| **Totaal** | 6382 | | $4,000 | $4,020 | $399 tot $1,045 | 4113 / 2679 | $15,192 | $-391 | $42.39 | $7.37 tot $653 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-363 over 4100 vullingen en $15,136, dus -2.40% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.62% over $14,915 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.72%.

**Opgeschaald (GOK):** per dag $0.02 (ondergrens) tot $146 (hoge schatting) netto (gemeten minuten × 1440 / 6382).

105 van de 4113 vullingen ($277) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.62%): $-7.28 (GOK).

Geld dat de bot nodig had: gemiddeld $4,000 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,020**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $0.47 tot $3,272 |
| €5,000 | $5,000 | $1.17 tot $8,180 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $42.39 over 2243 vullingen en $8,257, dus +0.51% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.39% per dollar over 3894 vullingen, 1 uur later -2.66% over 3795 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.51% per dollar over 206 vullingen, 1 uur later -1.59% over 203 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1302 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.56 tot $3.15 | $-0.39 tot $1.20 | 2 | $25.42 tot $31.80 | $27.05 tot $33.44 |
| €150 | 2 | $3.12 tot $6.30 | $-0.77 tot $2.40 | 3 | $34.49 tot $49.45 | $46.49 tot $61.45 |
| €200 | 3 | $4.68 tot $9.44 | $-1.16 tot $3.60 | 4 | $44.18 tot $67.80 | $40.68 tot $64.29 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-3.00%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $0.00 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $0.00 |
| highest hong-kong-on-november-24 22°C | 1464 | $4.44 tot $8.79 | 89 | $-20.19 | $0.00 |
| highest toronto-on-november-23 12°C | 1200 | $2.93 tot $5.19 | 44 | $-18.45 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $28.93 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $-14.69 |
| lowest seoul-on-november-23 3°C | 720 | $0.81 tot $1.65 | 27 | $-14.61 | $34.92 |
| ... | | | | | |
| highest warsaw-on-november-22 4°C | 2271 | $4.51 tot $9.55 | 43 | $2.34 | $23.20 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $0.00 |
| highest warsaw-on-november-25 6°C or higher | 75 | $0.20 tot $0.30 | 8 | $17.58 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| miami (lowest) | $40.02 tot $69.72 | 95 | $-8.83 | $31.19 |
| warsaw (highest) | $38.65 tot $81.25 | 382 | $-8.49 | $30.16 |
| seoul (highest) | $32.54 tot $68.71 | 588 | $-2.45 | $30.08 |
| chengdu (highest) | $31.92 tot $69.80 | 326 | $-12.79 | $19.12 |
| london (lowest) | $28.59 tot $53.08 | 170 | $-11.60 | $16.99 |
| beijing (highest) | $27.22 tot $57.84 | 335 | $-12.65 | $14.57 |
| milan (highest) | $34.15 tot $69.50 | 436 | $-20.32 | $13.83 |
| los-angeles (highest) | $28.82 tot $64.60 | 549 | $-17.11 | $11.71 |
| manila (highest) | $18.35 tot $36.51 | 152 | $-8.06 | $10.28 |
| jeddah (highest) | $18.95 tot $38.22 | 125 | $-9.06 | $9.89 |
| kuala-lumpur (highest) | $24.22 tot $46.44 | 228 | $-14.93 | $9.29 |
| karachi (highest) | $24.00 tot $46.30 | 154 | $-15.19 | $8.82 |
| paris (lowest) | $32.53 tot $59.85 | 109 | $-23.73 | $8.80 |
| wuhan (highest) | $29.89 tot $63.86 | 268 | $-21.37 | $8.52 |
| sao-paulo (highest) | $24.09 tot $48.19 | 289 | $-16.59 | $7.51 |
| shenzhen (highest) | $22.66 tot $47.68 | 406 | $-15.31 | $7.35 |
| tokyo (highest) | $28.21 tot $61.98 | 496 | $-21.14 | $7.07 |
| austin (highest) | $45.11 tot $94.04 | 465 | $-38.93 | $6.18 |
| munich (highest) | $36.13 tot $75.56 | 511 | $-30.39 | $5.74 |
| chongqing (highest) | $33.68 tot $69.99 | 276 | $-28.18 | $5.50 |
| mexico-city (highest) | $29.62 tot $56.83 | 176 | $-24.29 | $5.32 |
| houston (highest) | $48.86 tot $101 | 707 | $-43.75 | $5.11 |
| shanghai (lowest) | $11.87 tot $21.74 | 41 | $-7.06 | $4.81 |
| singapore (highest) | $32.61 tot $69.86 | 424 | $-28.41 | $4.20 |
| shanghai (highest) | $31.89 tot $69.54 | 550 | $-31.59 | $0.30 |
| nyc (lowest) | $13.19 tot $22.44 | 88 | $-13.22 | $-0.03 |
| buenos-aires (highest) | $24.92 tot $47.54 | 296 | $-25.39 | $-0.47 |
| seoul (lowest) | $19.70 tot $37.06 | 110 | $-21.80 | $-2.10 |
| london (highest) | $40.03 tot $86.92 | 765 | $-42.66 | $-2.63 |
| moscow (highest) | $24.46 tot $48.88 | 242 | $-27.55 | $-3.09 |
| nyc (highest) | $48.25 tot $101 | 889 | $-53.41 | $-5.17 |
| tokyo (lowest) | $13.41 tot $22.80 | 65 | $-19.69 | $-6.28 |
| lucknow (highest) | $38.97 tot $80.44 | 346 | $-50.84 | $-11.87 |
| amsterdam (highest) | $31.96 tot $70.14 | 595 | $-46.08 | $-14.12 |
| chicago (highest) | $41.61 tot $77.68 | 603 | $-56.29 | $-14.69 |
| qingdao (highest) | $20.79 tot $41.43 | 234 | $-35.74 | $-14.94 |
| tel-aviv (highest) | $40.37 tot $86.63 | 344 | $-55.65 | $-15.28 |
| taipei (highest) | $26.36 tot $48.84 | 292 | $-43.00 | $-16.63 |
| guangzhou (highest) | $38.39 tot $78.17 | 524 | $-55.88 | $-17.49 |
| madrid (highest) | $33.38 tot $73.79 | 486 | $-51.26 | $-17.87 |
| miami (highest) | $39.62 tot $82.90 | 533 | $-58.19 | $-18.57 |
| ankara (highest) | $27.13 tot $52.78 | 397 | $-46.26 | $-19.12 |
| hong-kong (lowest) | $8.26 tot $14.64 | 134 | $-27.75 | $-19.50 |
| san-francisco (highest) | $30.66 tot $60.02 | 396 | $-56.65 | $-25.98 |
| atlanta (highest) | $45.85 tot $97.06 | 862 | $-81.52 | $-35.67 |
| hong-kong (highest) | $28.80 tot $60.79 | 748 | $-67.62 | $-38.82 |
| toronto (highest) | $24.43 tot $47.98 | 438 | $-65.37 | $-40.94 |
| busan (highest) | $34.06 tot $71.93 | 464 | $-79.59 | $-45.53 |
| helsinki (highest) | $47.57 tot $98.12 | 624 | $-102 | $-54.91 |
| paris (highest) | $45.11 tot $97.45 | 806 | $-102 | $-57.08 |
| wellington (highest) | $30.02 tot $65.55 | 460 | $-88.05 | $-58.03 |
| dallas (highest) | $42.18 tot $88.81 | 572 | $-101 | $-59.18 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
