# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.25 tot $1.82 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 16 runs, 5376 minuten (89.6 uur) (GEZIEN). Markten in de data: 2377. Uitslag bekend voor 1562 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-146 (3716 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $91.65 (2367 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-11.01 (25 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 219 | 173 | $3,276 | $8,779 | $41.08 tot $85.25 | 573 / 430 | $1,743 | $-8.95 (150 nog zonder prijs) | $0.00 (0 van 573 beslist) | $32.13 tot $76.30 |
| **Totaal** | 5376 | | $4,219 | $10,171 | $1,366 tot $2,808 | 16854 / 12115 | $54,078 | $-1,610 | $-608 | $-243 tot $1,198 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,198 over 16812 vullingen en $53,967, dus -2.22% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.04% over $52,957 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.91%.

**Opgeschaald (GOK):** per dag $-74.30 (ondergrens) tot $312 (hoge schatting) netto (gemeten minuten × 1440 / 5376).

411 van de 16854 vullingen ($1,121) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.04%): $-34.07 (GOK).

Geld dat de bot nodig had: gemiddeld $4,219 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,390**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-929 tot $3,900 |
| €5,000 | $5,000 | $-2,324 tot $9,750 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-608 over 9095 vullingen en $29,865, dus -2.03% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.12% per dollar over 16073 vullingen, 1 uur later -2.93% over 15695 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.26% per dollar over 739 vullingen, 1 uur later -5.02% over 722 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $80.79 (681 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-40.35 (446 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-0.11 (4 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 219 | 173 | $3,237 | $3,665 | $9.86 tot $26.98 | 110 / 72 | $336 | $0.99 (33 nog zonder prijs) | $0.00 (0 van 110 beslist) | $10.85 tot $27.97 |
| **Totaal** | 5376 | | $4,149 | $4,020 | $335 tot $877 | 3184 / 2057 | $11,575 | $-293 | $-44.20 | $41.87 tot $585 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-299 over 3168 vullingen en $11,514, dus -2.60% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.58% over $11,337 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.69%.

**Opgeschaald (GOK):** per dag $9.57 (ondergrens) tot $155 (hoge schatting) netto (gemeten minuten × 1440 / 5376).

95 van de 3184 vullingen ($238) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.58%): $-6.15 (GOK).

Geld dat de bot nodig had: gemiddeld $4,149 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,169**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $211 tot $3,414 |
| €5,000 | $5,000 | $527 tot $8,536 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-44.20 over 1621 vullingen en $6,041, dus -0.73% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.62% per dollar over 2983 vullingen, 1 uur later -2.65% over 2897 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.25% per dollar over 185 vullingen, 1 uur later -1.06% over 183 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1137 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.48 tot $3.02 | $-0.63 tot $0.91 | 2 | $22.29 tot $32.12 | $6.45 tot $16.28 |
| €150 | 2 | $2.97 tot $6.04 | $-1.25 tot $1.82 | 3 | $29.62 tot $42.62 | $-12.49 tot $0.51 |
| €200 | 3 | $4.45 tot $9.06 | $-1.88 tot $2.73 | 4 | $35.32 tot $52.81 | $-6.79 tot $10.71 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-3.04%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $0.00 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $0.00 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $0.00 |
| lowest seoul-on-november-23 3°C | 720 | $0.81 tot $1.65 | 27 | $-14.61 | $0.00 |
| highest atlanta-on-november-22 61°F or below | 1305 | $1.47 tot $3.28 | 60 | $-15.20 | $0.00 |
| highest helsinki-on-november-23 2°C | 1643 | $5.38 tot $10.33 | 51 | $-17.99 | $0.00 |
| highest chicago-on-november-22 60-61°F | 2273 | $3.53 tot $6.65 | 56 | $-15.90 | $0.00 |
| ... | | | | | |
| highest austin-on-november-22 74-75°F | 2464 | $4.94 tot $9.96 | 32 | $0.59 | $0.00 |
| lowest london-on-november-24 2°C | 889 | $1.17 tot $2.10 | 10 | $5.02 | $0.00 |
| lowest miami-on-november-22 72-73°F | 1769 | $5.03 tot $8.87 | 9 | $1.29 | $0.00 |
| highest warsaw-on-november-22 4°C | 2271 | $4.51 tot $9.55 | 43 | $2.34 | $23.20 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| miami (lowest) | $33.94 tot $59.72 | 78 | $-6.82 | $27.11 |
| chengdu (highest) | $25.77 tot $57.39 | 244 | $-6.91 | $18.86 |
| seoul (highest) | $24.44 tot $52.35 | 338 | $-6.25 | $18.19 |
| london (lowest) | $24.52 tot $45.49 | 151 | $-8.40 | $16.13 |
| los-angeles (highest) | $24.25 tot $55.01 | 462 | $-11.97 | $12.28 |
| austin (highest) | $40.05 tot $83.73 | 384 | $-28.31 | $11.75 |
| warsaw (highest) | $35.24 tot $74.07 | 350 | $-24.88 | $10.36 |
| taipei (highest) | $23.13 tot $42.40 | 190 | $-13.91 | $9.22 |
| jeddah (highest) | $18.01 tot $36.34 | 110 | $-8.81 | $9.20 |
| kuala-lumpur (highest) | $21.19 tot $40.56 | 205 | $-13.10 | $8.09 |
| beijing (highest) | $22.39 tot $47.43 | 260 | $-14.33 | $8.05 |
| manila (highest) | $15.94 tot $31.70 | 134 | $-7.93 | $8.01 |
| karachi (highest) | $20.43 tot $40.08 | 132 | $-13.41 | $7.02 |
| chongqing (highest) | $26.39 tot $55.20 | 222 | $-20.33 | $6.06 |
| mexico-city (highest) | $26.98 tot $51.94 | 159 | $-21.15 | $5.83 |
| wuhan (highest) | $22.26 tot $48.85 | 180 | $-16.56 | $5.70 |
| munich (highest) | $27.87 tot $59.86 | 428 | $-22.54 | $5.34 |
| sao-paulo (highest) | $20.26 tot $40.32 | 244 | $-14.93 | $5.33 |
| milan (highest) | $29.74 tot $60.05 | 376 | $-24.67 | $5.07 |
| shanghai (lowest) | $11.87 tot $21.74 | 41 | $-7.06 | $4.81 |
| london (highest) | $31.53 tot $69.22 | 612 | $-26.81 | $4.71 |
| tokyo (highest) | $22.03 tot $49.55 | 404 | $-17.93 | $4.10 |
| paris (lowest) | $27.15 tot $50.64 | 95 | $-23.54 | $3.61 |
| shenzhen (highest) | $18.10 tot $38.58 | 315 | $-14.81 | $3.29 |
| buenos-aires (highest) | $22.11 tot $43.36 | 259 | $-20.06 | $2.06 |
| singapore (highest) | $24.03 tot $52.33 | 359 | $-21.98 | $2.05 |
| houston (highest) | $42.08 tot $87.68 | 612 | $-40.16 | $1.92 |
| nyc (lowest) | $12.86 tot $21.86 | 86 | $-12.48 | $0.38 |
| lucknow (highest) | $31.11 tot $64.21 | 278 | $-32.19 | $-1.08 |
| hong-kong (highest) | $23.25 tot $49.63 | 544 | $-26.42 | $-3.17 |
| seoul (lowest) | $17.13 tot $32.13 | 99 | $-20.74 | $-3.61 |
| tel-aviv (highest) | $32.91 tot $71.17 | 277 | $-37.87 | $-4.96 |
| toronto (highest) | $23.40 tot $45.86 | 353 | $-28.50 | $-5.09 |
| nyc (highest) | $42.60 tot $89.78 | 769 | $-47.73 | $-5.13 |
| tokyo (lowest) | $11.97 tot $20.66 | 57 | $-18.55 | $-6.58 |
| moscow (highest) | $22.88 tot $45.34 | 203 | $-29.93 | $-7.04 |
| ankara (highest) | $23.04 tot $45.11 | 315 | $-30.17 | $-7.13 |
| guangzhou (highest) | $32.76 tot $66.57 | 453 | $-40.15 | $-7.39 |
| miami (highest) | $32.74 tot $69.19 | 427 | $-47.50 | $-14.76 |
| qingdao (highest) | $18.22 tot $36.42 | 206 | $-34.23 | $-16.01 |
| amsterdam (highest) | $27.47 tot $60.56 | 509 | $-45.30 | $-17.83 |
| chicago (highest) | $38.03 tot $70.86 | 547 | $-55.98 | $-17.94 |
| shanghai (highest) | $25.73 tot $56.45 | 375 | $-45.39 | $-19.66 |
| hong-kong (lowest) | $8.06 tot $14.41 | 134 | $-27.75 | $-19.69 |
| madrid (highest) | $29.04 tot $64.44 | 399 | $-48.89 | $-19.85 |
| san-francisco (highest) | $27.45 tot $54.29 | 343 | $-50.03 | $-22.58 |
| busan (highest) | $26.52 tot $57.21 | 274 | $-52.10 | $-25.58 |
| paris (highest) | $35.90 tot $78.01 | 602 | $-62.02 | $-26.13 |
| atlanta (highest) | $40.69 tot $86.09 | 804 | $-80.63 | $-39.94 |
| wellington (highest) | $25.01 tot $54.44 | 415 | $-83.45 | $-58.44 |
| helsinki (highest) | $39.97 tot $82.71 | 543 | $-98.98 | $-59.01 |
| dallas (highest) | $35.74 tot $74.60 | 498 | $-95.00 | $-59.25 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
