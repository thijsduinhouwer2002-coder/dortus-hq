# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.10 tot $2.11 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 14 runs, 4706 minuten (78.4 uur) (GEZIEN). Markten in de data: 2377. Uitslag bekend voor 1258 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-506 (2812 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-46.28 (3044 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $29.27 (1038 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 981 | 193 | $3,662 | $9,224 | $245 tot $493 | 3094 / 2356 | $9,890 | $-304 (217 nog zonder prijs) | $0.00 (0 van 3094 beslist) | $-58.16 tot $189 |
| **Totaal** | 4706 | | $4,330 | $10,171 | $1,219 tot $2,506 | 14953 / 10695 | $47,924 | $-1,415 | $-523 | $-196 tot $1,092 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,081 over 14920 vullingen en $47,830, dus -2.26% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.03% over $46,630 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.92%.

**Opgeschaald (GOK):** per dag $-71.89 (ondergrens) tot $322 (hoge schatting) netto (gemeten minuten × 1440 / 4706).

442 van de 14953 vullingen ($1,294) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.03%): $-39.25 (GOK).

Geld dat de bot nodig had: gemiddeld $4,330 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,501**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-892 tot $3,997 |
| €5,000 | $5,000 | $-2,231 tot $9,992 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-523 over 6894 vullingen en $22,316, dus -2.34% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.15% per dollar over 14234 vullingen, 1 uur later -2.91% over 13819 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.35% per dollar over 686 vullingen, 1 uur later -5.26% over 666 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-50.76 (443 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $23.30 (527 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $62.44 (185 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 981 | 193 | $3,591 | $3,842 | $61.39 tot $161 | 615 / 406 | $2,325 | $-54.32 (51 nog zonder prijs) | $0.00 (0 van 615 beslist) | $7.07 tot $107 |
| **Totaal** | 4706 | | $4,257 | $4,020 | $297 tot $778 | 2822 / 1842 | $10,324 | $-276 | $34.98 | $21.06 tot $502 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-280 over 2810 vullingen en $10,271, dus -2.72% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.77% over $9,974 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.85%.

**Opgeschaald (GOK):** per dag $3.48 (ondergrens) tot $151 (hoge schatting) netto (gemeten minuten × 1440 / 4706).

102 van de 2822 vullingen ($350) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.77%): $-9.69 (GOK).

Geld dat de bot nodig had: gemiddeld $4,257 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,277**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $75.66 tot $3,273 |
| €5,000 | $5,000 | $189 tot $8,184 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $34.98 over 1155 vullingen en $4,176, dus +0.84% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.76% per dollar over 2634 vullingen, 1 uur later -2.88% over 2540 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.10% per dollar over 176 vullingen, 1 uur later -0.62% over 171 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1051 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.57 tot $3.18 | $-0.55 tot $1.06 | 2 | $21.56 tot $38.73 | $21.10 tot $38.27 |
| €150 | 2 | $3.14 tot $6.36 | $-1.10 tot $2.11 | 3 | $31.51 tot $57.30 | $24.37 tot $50.16 |
| €200 | 3 | $4.72 tot $9.54 | $-1.66 tot $3.17 | 4 | $40.53 tot $73.15 | $4.89 tot $37.51 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-3.03%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $0.00 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $0.00 |
| highest helsinki-on-november-23 2°C | 1363 | $4.48 tot $8.40 | 37 | $-18.75 | $0.00 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $0.00 |
| lowest seoul-on-november-23 3°C | 720 | $0.81 tot $1.65 | 27 | $-14.61 | $0.00 |
| highest atlanta-on-november-22 61°F or below | 1305 | $1.47 tot $3.28 | 60 | $-15.20 | $0.00 |
| highest chicago-on-november-22 60-61°F | 2273 | $3.53 tot $6.65 | 56 | $-15.90 | $0.00 |
| highest london-on-november-21 10°C or higher | 2264 | $4.90 tot $11.44 | 100 | $-16.40 | $-3.38 |
| ... | | | | | |
| highest ankara-on-november-23 14°C | 1212 | $1.67 tot $3.17 | 22 | $3.54 | $0.00 |
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
| miami (lowest) | $29.98 tot $52.83 | 69 | $-4.59 | $25.39 |
| seoul (highest) | $22.95 tot $49.06 | 291 | $-6.33 | $16.62 |
| chengdu (highest) | $23.82 tot $53.19 | 215 | $-7.40 | $16.42 |
| austin (highest) | $34.69 tot $73.18 | 328 | $-19.69 | $15.00 |
| london (lowest) | $21.90 tot $40.49 | 128 | $-8.61 | $13.29 |
| beijing (highest) | $19.87 tot $42.16 | 230 | $-8.20 | $11.67 |
| warsaw (highest) | $29.99 tot $63.42 | 300 | $-18.44 | $11.55 |
| kuala-lumpur (highest) | $19.97 tot $38.11 | 193 | $-8.89 | $11.07 |
| manila (highest) | $14.80 tot $29.35 | 114 | $-4.18 | $10.62 |
| milan (highest) | $25.85 tot $51.97 | 323 | $-15.42 | $10.43 |
| los-angeles (highest) | $19.16 tot $43.46 | 392 | $-8.78 | $10.38 |
| chongqing (highest) | $23.06 tot $48.57 | 192 | $-13.84 | $9.22 |
| jeddah (highest) | $17.28 tot $34.64 | 101 | $-9.36 | $7.92 |
| taipei (highest) | $20.87 tot $37.89 | 164 | $-13.41 | $7.47 |
| london (highest) | $26.33 tot $58.99 | 531 | $-20.51 | $5.82 |
| shanghai (lowest) | $11.86 tot $21.74 | 41 | $-7.06 | $4.80 |
| karachi (highest) | $17.87 tot $34.83 | 124 | $-13.63 | $4.23 |
| mexico-city (highest) | $23.57 tot $45.76 | 143 | $-19.49 | $4.08 |
| sao-paulo (highest) | $19.14 tot $37.95 | 224 | $-15.46 | $3.68 |
| wuhan (highest) | $21.34 tot $46.86 | 171 | $-17.91 | $3.43 |
| munich (highest) | $25.17 tot $53.72 | 363 | $-21.79 | $3.38 |
| houston (highest) | $36.23 tot $75.60 | 530 | $-33.07 | $3.16 |
| singapore (highest) | $21.88 tot $47.74 | 335 | $-19.54 | $2.34 |
| tokyo (highest) | $20.59 tot $46.21 | 367 | $-18.43 | $2.16 |
| buenos-aires (highest) | $19.61 tot $38.28 | 236 | $-18.46 | $1.15 |
| nyc (lowest) | $11.78 tot $20.13 | 80 | $-10.99 | $0.79 |
| amsterdam (highest) | $23.19 tot $51.34 | 424 | $-23.15 | $0.04 |
| paris (lowest) | $23.85 tot $44.69 | 90 | $-24.19 | $-0.34 |
| shenzhen (highest) | $17.17 tot $36.67 | 295 | $-17.73 | $-0.56 |
| toronto (highest) | $20.27 tot $40.17 | 264 | $-21.33 | $-1.06 |
| lucknow (highest) | $28.41 tot $58.78 | 263 | $-30.18 | $-1.77 |
| ankara (highest) | $20.07 tot $39.51 | 268 | $-23.35 | $-3.27 |
| seoul (lowest) | $16.34 tot $30.49 | 96 | $-20.80 | $-4.46 |
| hong-kong (highest) | $21.33 tot $45.54 | 490 | $-25.99 | $-4.66 |
| paris (highest) | $29.67 tot $64.85 | 492 | $-34.48 | $-4.81 |
| tel-aviv (highest) | $28.94 tot $62.16 | 246 | $-34.42 | $-5.48 |
| tokyo (lowest) | $11.24 tot $19.45 | 49 | $-17.38 | $-6.14 |
| nyc (highest) | $37.47 tot $77.88 | 672 | $-45.81 | $-8.34 |
| moscow (highest) | $21.08 tot $41.74 | 194 | $-30.07 | $-9.00 |
| guangzhou (highest) | $30.80 tot $62.40 | 434 | $-39.85 | $-9.05 |
| qingdao (highest) | $17.14 tot $34.29 | 179 | $-26.77 | $-9.63 |
| miami (highest) | $29.25 tot $61.88 | 377 | $-40.97 | $-11.72 |
| madrid (highest) | $24.93 tot $55.61 | 348 | $-42.38 | $-17.45 |
| hong-kong (lowest) | $8.06 tot $14.40 | 134 | $-25.59 | $-17.53 |
| chicago (highest) | $33.87 tot $63.83 | 507 | $-54.90 | $-21.03 |
| shanghai (highest) | $22.49 tot $49.50 | 347 | $-44.51 | $-22.02 |
| san-francisco (highest) | $25.33 tot $50.14 | 327 | $-48.22 | $-22.90 |
| busan (highest) | $24.27 tot $52.25 | 258 | $-50.24 | $-25.97 |
| atlanta (highest) | $33.92 tot $72.85 | 734 | $-68.43 | $-34.51 |
| dallas (highest) | $29.95 tot $62.89 | 422 | $-85.87 | $-55.92 |
| helsinki (highest) | $36.70 tot $75.63 | 480 | $-93.15 | $-56.45 |
| wellington (highest) | $23.60 tot $51.05 | 378 | $-81.31 | $-57.71 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
