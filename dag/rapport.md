# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.21 tot $1.93 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 15 runs, 5041 minuten (84.0 uur) (GEZIEN). Markten in de data: 2377. Uitslag bekend voor 1353 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-506 (2812 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-30.27 (3182 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-24.13 (1409 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1316 | 192 | $3,626 | $9,582 | $324 tot $652 | 4126 / 3115 | $13,377 | $-421 (179 nog zonder prijs) | $0.00 (0 van 4126 beslist) | $-97.96 tot $230 |
| **Totaal** | 5041 | | $4,277 | $10,171 | $1,297 tot $2,665 | 15985 / 11454 | $51,411 | $-1,532 | $-560 | $-235 tot $1,132 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,149 over 15952 vullingen en $51,317, dus -2.24% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.04% over $50,338 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.93%.

**Opgeschaald (GOK):** per dag $-76.60 (ondergrens) tot $314 (hoge schatting) netto (gemeten minuten × 1440 / 5041).

404 van de 15985 vullingen ($1,073) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.04%): $-32.66 (GOK).

Geld dat de bot nodig had: gemiddeld $4,277 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,447**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-954 tot $3,913 |
| €5,000 | $5,000 | $-2,386 tot $9,784 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-560 over 7403 vullingen en $23,933, dus -2.34% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.14% per dollar over 15242 vullingen, 1 uur later -2.94% over 14858 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.20% per dollar over 710 vullingen, 1 uur later -4.99% over 697 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-50.76 (443 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $-14.15 (557 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-43.60 (262 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1316 | 192 | $3,565 | $3,943 | $82.28 tot $216 | 806 / 510 | $3,008 | $-72.64 (49 nog zonder prijs) | $0.00 (0 van 806 beslist) | $9.64 tot $143 |
| **Totaal** | 5041 | | $4,206 | $4,020 | $318 tot $832 | 3013 / 1946 | $11,008 | $-295 | $-109 | $23.63 tot $538 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-291 over 3002 vullingen en $10,956, dus -2.66% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.74% over $10,755 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.79%.

**Opgeschaald (GOK):** per dag $4.77 (ondergrens) tot $152 (hoge schatting) netto (gemeten minuten × 1440 / 5041).

100 van de 3013 vullingen ($253) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.74%): $-6.94 (GOK).

Geld dat de bot nodig had: gemiddeld $4,206 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,226**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $104 tot $3,318 |
| €5,000 | $5,000 | $261 tot $8,295 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-109 over 1262 vullingen en $4,588, dus -2.37% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.69% per dollar over 2824 vullingen, 1 uur later -2.84% over 2728 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.07% per dollar over 178 vullingen, 1 uur later -0.78% over 176 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1108 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.53 tot $3.10 | $-0.60 tot $0.96 | 2 | $30.30 tot $40.25 | $-47.87 tot $-37.91 |
| €150 | 2 | $3.07 tot $6.20 | $-1.21 tot $1.93 | 3 | $38.61 tot $51.70 | $-29.15 tot $-16.06 |
| €200 | 3 | $4.60 tot $9.30 | $-1.81 tot $2.89 | 4 | $45.85 tot $66.18 | $-20.64 tot $-0.30 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-3.04%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $0.00 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $0.00 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $0.00 |
| lowest seoul-on-november-23 3°C | 720 | $0.81 tot $1.65 | 27 | $-14.61 | $0.00 |
| highest atlanta-on-november-22 61°F or below | 1305 | $1.47 tot $3.28 | 60 | $-15.20 | $0.00 |
| highest helsinki-on-november-23 2°C | 1643 | $5.38 tot $10.33 | 51 | $-17.97 | $0.00 |
| highest chicago-on-november-22 60-61°F | 2273 | $3.53 tot $6.65 | 56 | $-15.90 | $0.00 |
| highest london-on-november-21 10°C or higher | 2264 | $4.90 tot $11.44 | 100 | $-16.40 | $-3.38 |
| ... | | | | | |
| highest austin-on-november-22 74-75°F | 2464 | $4.94 tot $9.96 | 32 | $0.59 | $0.00 |
| lowest london-on-november-24 2°C | 647 | $0.90 tot $1.58 | 8 | $4.83 | $0.00 |
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
| miami (lowest) | $32.59 tot $57.28 | 73 | $-5.76 | $26.83 |
| london (lowest) | $23.84 tot $44.13 | 140 | $-7.09 | $16.75 |
| chengdu (highest) | $25.12 tot $55.88 | 231 | $-8.65 | $16.47 |
| seoul (highest) | $23.68 tot $50.63 | 313 | $-7.56 | $16.11 |
| warsaw (highest) | $33.07 tot $69.58 | 333 | $-21.01 | $12.06 |
| manila (highest) | $15.22 tot $30.14 | 125 | $-3.74 | $11.48 |
| beijing (highest) | $20.82 tot $44.18 | 240 | $-9.51 | $11.31 |
| los-angeles (highest) | $21.22 tot $48.44 | 422 | $-10.42 | $10.80 |
| austin (highest) | $37.03 tot $77.67 | 352 | $-27.38 | $9.65 |
| jeddah (highest) | $18.01 tot $36.33 | 110 | $-8.81 | $9.20 |
| taipei (highest) | $22.00 tot $40.14 | 175 | $-14.36 | $7.64 |
| london (highest) | $29.19 tot $64.60 | 573 | $-22.04 | $7.15 |
| chongqing (highest) | $25.01 tot $52.40 | 215 | $-18.13 | $6.88 |
| kuala-lumpur (highest) | $20.44 tot $38.91 | 199 | $-13.63 | $6.81 |
| milan (highest) | $28.84 tot $58.18 | 362 | $-22.18 | $6.66 |
| karachi (highest) | $19.36 tot $37.80 | 128 | $-13.47 | $5.88 |
| sao-paulo (highest) | $19.67 tot $39.05 | 229 | $-14.83 | $4.84 |
| shanghai (lowest) | $11.86 tot $21.74 | 41 | $-7.06 | $4.80 |
| wuhan (highest) | $22.00 tot $48.26 | 174 | $-17.39 | $4.61 |
| singapore (highest) | $23.29 tot $50.63 | 345 | $-19.08 | $4.22 |
| mexico-city (highest) | $24.45 tot $47.56 | 151 | $-20.56 | $3.89 |
| munich (highest) | $26.31 tot $56.40 | 401 | $-22.43 | $3.88 |
| tokyo (highest) | $21.24 tot $47.72 | 393 | $-18.52 | $2.72 |
| paris (lowest) | $25.86 tot $48.42 | 93 | $-23.88 | $1.98 |
| nyc (lowest) | $12.35 tot $21.06 | 84 | $-10.63 | $1.72 |
| buenos-aires (highest) | $20.67 tot $40.40 | 248 | $-19.92 | $0.75 |
| houston (highest) | $38.85 tot $80.97 | 580 | $-38.29 | $0.55 |
| shenzhen (highest) | $17.27 tot $36.83 | 295 | $-17.66 | $-0.39 |
| lucknow (highest) | $30.11 tot $62.02 | 271 | $-30.76 | $-0.65 |
| toronto (highest) | $21.81 tot $42.95 | 282 | $-23.07 | $-1.27 |
| seoul (lowest) | $16.73 tot $31.35 | 96 | $-20.80 | $-4.06 |
| hong-kong (highest) | $22.33 tot $47.65 | 517 | $-26.60 | $-4.27 |
| tel-aviv (highest) | $31.46 tot $68.09 | 268 | $-36.39 | $-4.94 |
| tokyo (lowest) | $11.38 tot $19.67 | 50 | $-17.26 | $-5.88 |
| nyc (highest) | $39.57 tot $82.68 | 713 | $-45.53 | $-5.96 |
| ankara (highest) | $22.00 tot $43.05 | 300 | $-28.89 | $-6.89 |
| guangzhou (highest) | $31.56 tot $63.85 | 437 | $-39.59 | $-8.03 |
| moscow (highest) | $22.16 tot $43.84 | 201 | $-30.24 | $-8.08 |
| amsterdam (highest) | $26.12 tot $57.72 | 488 | $-36.06 | $-9.94 |
| qingdao (highest) | $17.47 tot $34.97 | 194 | $-28.59 | $-11.12 |
| paris (highest) | $34.17 tot $74.13 | 587 | $-46.24 | $-12.07 |
| miami (highest) | $31.41 tot $66.48 | 405 | $-47.32 | $-15.90 |
| chicago (highest) | $36.27 tot $67.72 | 535 | $-55.22 | $-18.95 |
| hong-kong (lowest) | $8.06 tot $14.40 | 134 | $-27.75 | $-19.69 |
| madrid (highest) | $27.19 tot $60.53 | 386 | $-47.68 | $-20.49 |
| shanghai (highest) | $24.29 tot $53.41 | 365 | $-45.94 | $-21.65 |
| san-francisco (highest) | $26.22 tot $52.00 | 341 | $-48.73 | $-22.51 |
| busan (highest) | $25.17 tot $54.42 | 259 | $-49.91 | $-24.73 |
| atlanta (highest) | $37.50 tot $79.35 | 759 | $-76.02 | $-38.52 |
| helsinki (highest) | $39.29 tot $81.20 | 523 | $-100 | $-60.83 |
| wellington (highest) | $24.09 tot $52.18 | 387 | $-85.09 | $-61.00 |
| dallas (highest) | $31.29 tot $65.66 | 462 | $-94.59 | $-63.31 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
