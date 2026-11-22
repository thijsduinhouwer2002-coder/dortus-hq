# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.03 tot $1.96 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 12 runs, 4036 minuten (67.3 uur) (GEZIEN). Markten in de data: 1806. Uitslag bekend voor 946 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-248 (2553 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-229 (1930 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $14.44 (20 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 311 | 186 | $3,527 | $9,224 | $66.22 tot $133 | 930 / 701 | $2,926 | $-63.72 (177 nog zonder prijs) | $0.00 (0 van 930 beslist) | $2.49 tot $69.75 |
| **Totaal** | 4036 | | $4,431 | $10,171 | $1,040 tot $2,147 | 12789 / 9040 | $40,960 | $-1,175 | $-463 | $-135 tot $972 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-928 over 12755 vullingen en $40,861, dus -2.27% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.95% over $39,783 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.79%.

**Opgeschaald (GOK):** per dag $-60.58 (ondergrens) tot $334 (hoge schatting) netto (gemeten minuten × 1440 / 4036).

402 van de 12789 vullingen ($1,177) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.95%): $-34.76 (GOK).

Geld dat de bot nodig had: gemiddeld $4,431 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,602**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-747 tot $4,122 |
| €5,000 | $5,000 | $-1,867 tot $10,305 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-463 over 4503 vullingen en $15,060, dus -3.08% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.17% per dollar over 12144 vullingen, 1 uur later -2.84% over 11775 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.26% per dollar over 611 vullingen, 1 uur later -4.86% over 589 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-29.68 (414 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $-56.82 (339 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $1.53 (5 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 311 | 186 | $3,462 | $3,842 | $17.38 tot $45.36 | 193 / 122 | $729 | $-9.48 (40 nog zonder prijs) | $0.00 (0 van 193 beslist) | $7.90 tot $35.88 |
| **Totaal** | 4036 | | $4,358 | $4,020 | $253 tot $662 | 2400 / 1558 | $8,728 | $-231 | $-84.98 | $21.89 tot $431 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-239 over 2391 vullingen en $8,676, dus -2.76% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.74% over $8,455 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.72%.

**Opgeschaald (GOK):** per dag $5.14 (ondergrens) tot $151 (hoge schatting) netto (gemeten minuten × 1440 / 4036).

91 van de 2400 vullingen ($273) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.74%): $-7.48 (GOK).

Geld dat de bot nodig had: gemiddeld $4,358 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,378**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $110 tot $3,244 |
| €5,000 | $5,000 | $276 tot $8,111 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-84.98 over 758 vullingen en $2,880, dus -2.95% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.81% per dollar over 2230 vullingen, 1 uur later -2.88% over 2144 (GEZIEN).
- Laagste temperatuur: 5 minuten later -1.97% per dollar over 161 vullingen, 1 uur later -0.17% over 156 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 920 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.42 tot $2.92 | $-0.52 tot $0.98 | 2 | $13.36 tot $24.32 | $4.85 tot $15.82 |
| €150 | 2 | $2.85 tot $5.84 | $-1.03 tot $1.96 | 3 | $19.74 tot $35.57 | $-15.32 tot $0.50 |
| €200 | 3 | $4.27 tot $8.76 | $-1.55 tot $2.94 | 5 | $26.43 tot $46.59 | $-11.30 tot $8.86 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.95%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1236 | $4.08 tot $8.32 | 66 | $-34.31 | $0.00 |
| highest wellington-on-november-23 18°C | 1237 | $3.52 tot $7.28 | 52 | $-18.21 | $0.00 |
| highest san-francisco-on-november-22 54-55°F | 2261 | $3.01 tot $6.04 | 47 | $-17.52 | $0.00 |
| highest atlanta-on-november-22 61°F or below | 1305 | $1.47 tot $3.28 | 60 | $-15.20 | $0.00 |
| highest london-on-november-21 10°C or higher | 2264 | $4.90 tot $11.44 | 100 | $-16.40 | $-3.38 |
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest chicago-on-november-22 60-61°F | 2226 | $3.47 tot $6.54 | 56 | $-13.82 | $0.00 |
| highest madrid-on-november-22 15°C | 2226 | $3.11 tot $6.72 | 41 | $-13.30 | $0.00 |
| highest hong-kong-on-november-23 23°C | 902 | $1.10 tot $2.43 | 10 | $-10.90 | $0.00 |
| highest busan-on-november-22 8°C | 1830 | $3.65 tot $7.73 | 29 | $-13.42 | $0.00 |
| ... | | | | | |
| highest ankara-on-november-23 14°C | 545 | $0.90 tot $1.64 | 13 | $4.45 | $0.00 |
| highest austin-on-november-22 74-75°F | 2420 | $4.84 tot $9.73 | 32 | $0.59 | $0.00 |
| highest chicago-on-november-22 56-57°F | 2230 | $3.59 tot $6.03 | 54 | $2.07 | $0.00 |
| lowest miami-on-november-22 72-73°F | 1769 | $5.03 tot $8.87 | 9 | $1.29 | $0.00 |
| highest warsaw-on-november-22 4°C | 2271 | $4.51 tot $9.55 | 43 | $2.34 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $0.00 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| miami (lowest) | $25.36 tot $45.01 | 57 | $-4.26 | $21.10 |
| austin (highest) | $32.40 tot $68.08 | 295 | $-14.81 | $17.59 |
| chengdu (highest) | $20.12 tot $45.19 | 182 | $-5.52 | $14.60 |
| seoul (highest) | $17.41 tot $38.14 | 232 | $-5.70 | $11.71 |
| milan (highest) | $23.65 tot $47.25 | 275 | $-12.50 | $11.14 |
| seoul (lowest) | $13.18 tot $24.63 | 76 | $-2.50 | $10.68 |
| los-angeles (highest) | $16.45 tot $37.78 | 346 | $-6.04 | $10.41 |
| beijing (highest) | $16.47 tot $35.45 | 181 | $-6.44 | $10.04 |
| warsaw (highest) | $24.37 tot $52.01 | 242 | $-15.88 | $8.49 |
| tokyo (highest) | $15.56 tot $35.82 | 263 | $-7.63 | $7.93 |
| manila (highest) | $13.01 tot $25.70 | 103 | $-5.27 | $7.74 |
| kuala-lumpur (highest) | $17.09 tot $32.74 | 159 | $-10.45 | $6.64 |
| chongqing (highest) | $18.44 tot $39.11 | 155 | $-11.86 | $6.58 |
| taipei (highest) | $17.91 tot $32.20 | 130 | $-11.87 | $6.04 |
| houston (highest) | $32.37 tot $67.86 | 430 | $-27.03 | $5.35 |
| jeddah (highest) | $15.00 tot $30.07 | 82 | $-9.76 | $5.24 |
| london (lowest) | $18.53 tot $34.54 | 116 | $-13.68 | $4.85 |
| mexico-city (highest) | $21.77 tot $42.33 | 135 | $-16.93 | $4.84 |
| shanghai (lowest) | $11.82 tot $21.69 | 41 | $-7.06 | $4.76 |
| wuhan (highest) | $18.25 tot $40.34 | 153 | $-14.47 | $3.78 |
| paris (highest) | $22.86 tot $50.99 | 405 | $-19.58 | $3.28 |
| nyc (lowest) | $9.77 tot $16.56 | 67 | $-6.74 | $3.04 |
| karachi (highest) | $16.36 tot $31.62 | 105 | $-13.59 | $2.77 |
| london (highest) | $21.96 tot $49.99 | 473 | $-19.55 | $2.41 |
| toronto (highest) | $16.70 tot $33.60 | 222 | $-15.22 | $1.48 |
| munich (highest) | $22.02 tot $47.18 | 331 | $-20.58 | $1.44 |
| shenzhen (highest) | $14.98 tot $31.97 | 260 | $-13.73 | $1.25 |
| sao-paulo (highest) | $16.89 tot $33.55 | 211 | $-15.67 | $1.22 |
| lucknow (highest) | $23.93 tot $49.86 | 196 | $-25.28 | $-1.35 |
| buenos-aires (highest) | $17.54 tot $34.56 | 221 | $-19.30 | $-1.76 |
| ankara (highest) | $17.56 tot $34.41 | 230 | $-20.00 | $-2.44 |
| singapore (highest) | $17.33 tot $38.50 | 288 | $-19.95 | $-2.62 |
| paris (lowest) | $19.33 tot $36.49 | 83 | $-22.41 | $-3.08 |
| amsterdam (highest) | $20.79 tot $45.83 | 391 | $-24.33 | $-3.54 |
| moscow (highest) | $18.95 tot $37.54 | 169 | $-24.09 | $-5.14 |
| tokyo (lowest) | $11.23 tot $19.41 | 49 | $-17.38 | $-6.15 |
| dallas (highest) | $26.38 tot $55.83 | 350 | $-34.29 | $-7.91 |
| tel-aviv (highest) | $23.54 tot $50.46 | 213 | $-33.08 | $-9.55 |
| hong-kong (highest) | $17.27 tot $37.28 | 395 | $-27.61 | $-10.34 |
| shanghai (highest) | $16.02 tot $36.54 | 265 | $-26.42 | $-10.40 |
| nyc (highest) | $32.24 tot $66.97 | 572 | $-43.63 | $-11.39 |
| hong-kong (lowest) | $7.79 tot $13.98 | 123 | $-19.89 | $-12.10 |
| guangzhou (highest) | $25.33 tot $51.43 | 375 | $-39.05 | $-13.72 |
| qingdao (highest) | $15.02 tot $29.80 | 131 | $-29.54 | $-14.52 |
| miami (highest) | $26.45 tot $56.30 | 329 | $-42.39 | $-15.93 |
| chicago (highest) | $30.08 tot $56.83 | 450 | $-48.58 | $-18.50 |
| madrid (highest) | $20.44 tot $46.37 | 305 | $-40.33 | $-19.89 |
| san-francisco (highest) | $22.77 tot $45.38 | 299 | $-43.47 | $-20.70 |
| busan (highest) | $18.72 tot $41.06 | 230 | $-46.12 | $-27.40 |
| helsinki (highest) | $30.29 tot $62.84 | 393 | $-61.07 | $-30.78 |
| atlanta (highest) | $30.38 tot $65.07 | 690 | $-65.68 | $-35.30 |
| wellington (highest) | $19.47 tot $42.45 | 315 | $-66.40 | $-46.94 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
