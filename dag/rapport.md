# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-0.44 tot $2.42 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 8 runs, 2694 minuten (44.9 uur) (GEZIEN). Markten in de data: 1641. Uitslag bekend voor 462 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-97.45 (1478 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-13.57 (104 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 379 | 208 | $3,941 | $8,569 | $73.19 tot $150 | 1221 / 764 | $3,676 | $-141 (207 nog zonder prijs) | $0.00 (0 van 1221 beslist) | $-67.64 tot $9.08 |
| **Totaal** | 2694 | | $4,642 | $9,026 | $704 tot $1,459 | 8282 / 5832 | $26,697 | $-714 | $-111 | $-10.52 tot $745 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-542 over 8252 vullingen en $26,595, dus -2.04% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.78% over $25,670 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.56%.

**Opgeschaald (GOK):** per dag $-20.90 (ondergrens) tot $383 (hoge schatting) netto (gemeten minuten × 1440 / 2694).

335 van de 8282 vullingen ($1,028) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.78%): $-28.58 (GOK).

Geld dat de bot nodig had: gemiddeld $4,642 in open orders plus de hoogste stand van $9,026 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,667**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-275 tot $5,042 |
| €5,000 | $5,000 | $-688 tot $12,606 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-111 over 1582 vullingen en $5,346, dus -2.08% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -1.93% per dollar over 7847 vullingen, 1 uur later -2.59% over 7538 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.24% per dollar over 405 vullingen, 1 uur later -6.19% over 387 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $50.91 (267 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $-6.08 (19 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 379 | 208 | $3,879 | $3,199 | $17.65 tot $48.79 | 212 / 136 | $657 | $-29.12 (37 nog zonder prijs) | $0.00 (0 van 212 beslist) | $-11.47 tot $19.67 |
| **Totaal** | 2694 | | $4,563 | $3,199 | $167 tot $436 | 1453 / 966 | $5,175 | $-157 | $44.83 | $10.82 tot $279 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-129 over 1443 vullingen en $5,120, dus -2.52% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.16% over $4,950 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.83%.

**Opgeschaald (GOK):** per dag $2.00 (ondergrens) tot $145 (hoge schatting) netto (gemeten minuten × 1440 / 2694).

74 van de 1453 vullingen ($224) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.16%): $-7.09 (GOK).

Geld dat de bot nodig had: gemiddeld $4,563 in open orders plus de hoogste stand van $3,199 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,762**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $46.30 tot $3,372 |
| €5,000 | $5,000 | $116 tot $8,430 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $44.83 over 286 vullingen en $1,054, dus +4.25% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.71% per dollar over 1339 vullingen, 1 uur later -3.27% over 1270 (GEZIEN).
- Laagste temperatuur: 5 minuten later +0.06% per dollar over 104 vullingen, 1 uur later -1.16% over 101 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 690 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.35 tot $2.78 | $-0.22 tot $1.21 | 2 | $12.18 tot $22.31 | $36.94 tot $47.08 |
| €150 | 2 | $2.70 tot $5.56 | $-0.44 tot $2.42 | 3 | $16.92 tot $30.18 | $39.05 tot $52.31 |
| €200 | 3 | $4.06 tot $8.34 | $-0.66 tot $3.63 | 4 | $21.78 tot $38.58 | $42.10 tot $58.90 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.78%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest london-on-november-21 10°C or higher | 2264 | $4.90 tot $11.44 | 100 | $-16.40 | $0.00 |
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest hong-kong-on-november-23 23°C | 22 | $0.03 tot $0.06 | 2 | $-9.73 | $0.00 |
| highest helsinki-on-november-21 4°C | 2105 | $6.64 tot $14.22 | 83 | $-15.83 | $0.00 |
| highest guangzhou-on-november-20 17°C | 381 | $0.42 tot $0.91 | 33 | $-9.43 | $-18.63 |
| highest chicago-on-november-21 70-71°F | 2336 | $3.75 tot $7.16 | 63 | $-12.19 | $0.00 |
| highest qingdao-on-november-22 11°C | 1272 | $1.57 tot $3.08 | 17 | $-9.67 | $0.00 |
| highest qingdao-on-november-22 12°C | 1241 | $1.96 tot $4.05 | 11 | $-9.78 | $0.00 |
| highest atlanta-on-november-22 61°F or below | 753 | $0.44 tot $0.99 | 28 | $-8.13 | $0.00 |
| highest san-francisco-on-november-22 56-57°F | 980 | $1.60 tot $3.30 | 22 | $-9.04 | $0.00 |
| ... | | | | | |
| highest paris-on-november-21 11°C | 2247 | $3.20 tot $7.05 | 43 | $0.92 | $0.00 |
| lowest hong-kong-on-november-21 15°C | 576 | $1.36 tot $2.41 | 24 | $2.79 | $0.00 |
| highest mexico-city-on-november-21 24°C | 2046 | $3.70 tot $7.25 | 17 | $0.52 | $0.00 |
| highest tel-aviv-on-november-21 27°C | 1505 | $2.44 tot $5.69 | 26 | $1.88 | $0.00 |
| highest nyc-on-november-22 62-63°F | 1316 | $1.58 tot $3.26 | 23 | $2.90 | $0.00 |
| highest london-on-november-22 9°C | 1420 | $1.93 tot $4.36 | 25 | $4.36 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| tokyo (highest) | $10.82 tot $24.74 | 155 | $4.31 | $15.13 |
| austin (highest) | $21.97 tot $46.38 | 175 | $-8.66 | $13.31 |
| miami (lowest) | $17.12 tot $30.62 | 41 | $-4.35 | $12.77 |
| beijing (highest) | $11.75 tot $25.28 | 114 | $0.66 | $12.40 |
| warsaw (highest) | $14.83 tot $31.76 | 128 | $-2.49 | $12.34 |
| chengdu (highest) | $13.88 tot $31.30 | 134 | $-2.21 | $11.67 |
| wellington (highest) | $11.02 tot $24.45 | 150 | $-0.67 | $10.36 |
| nyc (highest) | $18.95 tot $40.96 | 308 | $-8.68 | $10.27 |
| manila (highest) | $9.46 tot $18.66 | 84 | $0.01 | $9.47 |
| seoul (highest) | $10.91 tot $24.11 | 139 | $-2.97 | $7.93 |
| sao-paulo (highest) | $10.18 tot $20.47 | 132 | $-2.96 | $7.23 |
| taipei (highest) | $13.78 tot $24.36 | 101 | $-7.33 | $6.46 |
| los-angeles (highest) | $12.18 tot $27.71 | 241 | $-6.47 | $5.71 |
| shanghai (lowest) | $11.07 tot $20.41 | 31 | $-5.51 | $5.55 |
| seoul (lowest) | $8.69 tot $16.03 | 23 | $-3.25 | $5.44 |
| milan (highest) | $15.99 tot $31.06 | 199 | $-11.13 | $4.86 |
| jeddah (highest) | $9.67 tot $19.81 | 51 | $-5.92 | $3.75 |
| nyc (lowest) | $5.06 tot $8.54 | 31 | $-1.43 | $3.63 |
| wuhan (highest) | $13.10 tot $29.41 | 106 | $-10.07 | $3.04 |
| karachi (highest) | $12.56 tot $24.14 | 74 | $-9.76 | $2.80 |
| chongqing (highest) | $12.41 tot $26.17 | 105 | $-9.78 | $2.62 |
| kuala-lumpur (highest) | $12.26 tot $23.30 | 96 | $-9.72 | $2.53 |
| paris (highest) | $14.13 tot $31.80 | 232 | $-12.13 | $2.00 |
| london (highest) | $15.56 tot $35.69 | 326 | $-13.56 | $2.00 |
| houston (highest) | $22.32 tot $46.87 | 227 | $-20.50 | $1.82 |
| mexico-city (highest) | $15.89 tot $30.96 | 92 | $-14.91 | $0.98 |
| buenos-aires (highest) | $11.01 tot $21.28 | 121 | $-10.26 | $0.75 |
| london (lowest) | $11.22 tot $21.24 | 71 | $-10.64 | $0.58 |
| tokyo (lowest) | $9.46 tot $16.99 | 32 | $-9.85 | $-0.39 |
| toronto (highest) | $11.63 tot $23.63 | 144 | $-12.39 | $-0.76 |
| moscow (highest) | $14.02 tot $27.75 | 116 | $-15.00 | $-0.98 |
| singapore (highest) | $10.53 tot $23.54 | 131 | $-11.85 | $-1.32 |
| munich (highest) | $14.61 tot $32.27 | 227 | $-16.51 | $-1.90 |
| shenzhen (highest) | $11.10 tot $23.70 | 213 | $-13.10 | $-2.01 |
| shanghai (highest) | $11.28 tot $25.90 | 172 | $-13.43 | $-2.14 |
| tel-aviv (highest) | $14.81 tot $32.27 | 126 | $-17.51 | $-2.71 |
| amsterdam (highest) | $12.91 tot $29.13 | 266 | $-15.70 | $-2.79 |
| dallas (highest) | $16.76 tot $35.60 | 204 | $-19.68 | $-2.91 |
| helsinki (highest) | $20.53 tot $43.49 | 288 | $-26.31 | $-5.78 |
| paris (lowest) | $12.47 tot $22.70 | 58 | $-19.28 | $-6.81 |
| ankara (highest) | $10.57 tot $21.41 | 123 | $-18.52 | $-7.95 |
| lucknow (highest) | $16.36 tot $34.35 | 119 | $-24.31 | $-7.95 |
| san-francisco (highest) | $17.89 tot $35.28 | 229 | $-26.56 | $-8.66 |
| guangzhou (highest) | $16.06 tot $32.72 | 257 | $-25.84 | $-9.78 |
| chicago (highest) | $20.98 tot $40.08 | 327 | $-30.80 | $-9.82 |
| madrid (highest) | $13.08 tot $30.37 | 203 | $-22.98 | $-9.90 |
| hong-kong (lowest) | $7.35 tot $13.32 | 119 | $-21.04 | $-13.70 |
| hong-kong (highest) | $9.22 tot $20.21 | 295 | $-24.63 | $-15.40 |
| qingdao (highest) | $11.56 tot $23.10 | 112 | $-28.33 | $-16.77 |
| atlanta (highest) | $20.31 tot $44.31 | 438 | $-37.77 | $-17.46 |
| miami (highest) | $18.62 tot $39.37 | 222 | $-37.25 | $-18.63 |
| busan (highest) | $13.66 tot $29.95 | 174 | $-35.05 | $-21.40 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
