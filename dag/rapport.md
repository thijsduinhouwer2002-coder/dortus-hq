# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-0.32 tot $2.58 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 7 runs, 2358 minuten (39.3 uur) (GEZIEN). Markten in de data: 1237. Uitslag bekend voor 363 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-90.91 (1099 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $2.26 (1 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 43 | 211 | $3,954 | $8,407 | $7.96 tot $16.30 | 162 / 97 | $458 | $0.00 (162 nog zonder prijs) | $0.00 (0 van 162 beslist) | $7.96 tot $16.30 |
| **Totaal** | 2358 | | $4,742 | $9,026 | $638 tot $1,325 | 7223 / 5165 | $23,479 | $-573 | $-88.65 | $65.07 tot $752 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-431 over 7198 vullingen en $23,396, dus -1.84% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.53% over $22,649 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.29%.

**Opgeschaald (GOK):** per dag $26.90 (ondergrens) tot $446 (hoge schatting) netto (gemeten minuten × 1440 / 2358).

290 van de 7223 vullingen ($830) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.53%): $-21.02 (GOK).

Geld dat de bot nodig had: gemiddeld $4,742 in open orders plus de hoogste stand van $9,026 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,767**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $352 tot $5,837 |
| €5,000 | $5,000 | $879 tot $14,593 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-88.65 over 1100 vullingen en $3,935, dus -2.25% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -1.74% per dollar over 6844 vullingen, 1 uur later -2.32% over 6572 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.87% per dollar over 354 vullingen, 1 uur later -6.24% over 342 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $63.90 (222 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $0.00 (0 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 43 | 211 | $3,925 | $2,976 | $1.94 tot $5.37 | 19 / 10 | $60.46 | $0.00 (19 nog zonder prijs) | $0.00 (0 van 19 beslist) | $1.94 tot $5.37 |
| **Totaal** | 2358 | | $4,661 | $3,186 | $152 tot $392 | 1260 / 840 | $4,578 | $-127 | $63.90 | $24.24 tot $265 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-101 over 1252 vullingen en $4,534, dus -2.23% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.88% over $4,429 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.72%.

**Opgeschaald (GOK):** per dag $12.19 (ondergrens) tot $159 (hoge schatting) netto (gemeten minuten × 1440 / 2358).

56 van de 1260 vullingen ($149) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.88%): $-4.28 (GOK).

Geld dat de bot nodig had: gemiddeld $4,661 in open orders plus de hoogste stand van $3,186 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,848**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $280 tot $3,650 |
| €5,000 | $5,000 | $699 tot $9,124 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $63.90 over 222 vullingen en $834, dus +7.66% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.40% per dollar over 1162 vullingen, 1 uur later -2.86% over 1108 (GEZIEN).
- Laagste temperatuur: 5 minuten later +0.05% per dollar over 90 vullingen, 1 uur later -2.45% over 88 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 676 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.39 tot $2.84 | $-0.16 tot $1.29 | 2 | $12.18 tot $22.31 | $36.94 tot $47.08 |
| €150 | 2 | $2.78 tot $5.69 | $-0.32 tot $2.58 | 3 | $17.11 tot $32.20 | $35.73 tot $50.82 |
| €200 | 3 | $4.18 tot $8.53 | $-0.47 tot $3.88 | 4 | $21.85 tot $40.07 | $37.84 tot $56.06 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.53%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest london-on-november-21 10°C or higher | 2264 | $4.90 tot $11.44 | 100 | $-16.40 | $0.00 |
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest helsinki-on-november-21 4°C | 2105 | $6.64 tot $14.22 | 83 | $-15.83 | $0.00 |
| highest guangzhou-on-november-20 17°C | 381 | $0.42 tot $0.91 | 33 | $-9.43 | $-18.63 |
| highest helsinki-on-november-21 2°C | 1791 | $0.73 tot $1.71 | 26 | $-7.90 | $0.00 |
| highest qingdao-on-november-22 12°C | 914 | $1.43 tot $3.02 | 7 | $-8.60 | $0.00 |
| highest qingdao-on-november-22 11°C | 940 | $1.34 tot $2.65 | 10 | $-8.21 | $0.00 |
| highest milan-on-november-22 7°C | 912 | $1.59 tot $3.39 | 18 | $-8.44 | $0.00 |
| lowest tokyo-on-november-22 7°C | 818 | $1.59 tot $2.78 | 10 | $-8.20 | $0.00 |
| highest shenzhen-on-november-20 20°C | 379 | $0.40 tot $0.95 | 21 | $-6.96 | $-13.97 |
| ... | | | | | |
| highest milan-on-november-21 15°C | 2189 | $1.46 tot $3.32 | 39 | $2.55 | $0.00 |
| highest london-on-november-22 9°C | 1095 | $1.68 tot $3.83 | 16 | $2.43 | $0.00 |
| highest paris-on-november-21 11°C | 2247 | $3.20 tot $7.05 | 43 | $0.92 | $0.00 |
| lowest hong-kong-on-november-21 15°C | 576 | $1.36 tot $2.41 | 24 | $2.79 | $0.00 |
| highest tel-aviv-on-november-21 27°C | 1505 | $2.44 tot $5.69 | 26 | $1.88 | $0.00 |
| highest nyc-on-november-22 62-63°F | 981 | $1.35 tot $2.77 | 18 | $3.54 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $14.16 tot $30.37 | 114 | $1.30 | $15.46 |
| nyc (highest) | $16.76 tot $36.57 | 268 | $-2.51 | $14.25 |
| tokyo (highest) | $9.74 tot $22.43 | 133 | $3.17 | $12.91 |
| austin (highest) | $19.16 tot $40.25 | 140 | $-6.27 | $12.89 |
| beijing (highest) | $10.80 tot $23.15 | 96 | $1.18 | $11.99 |
| miami (lowest) | $15.11 tot $27.07 | 39 | $-3.62 | $11.48 |
| chengdu (highest) | $12.86 tot $28.93 | 120 | $-2.52 | $10.33 |
| manila (highest) | $8.57 tot $16.95 | 76 | $1.66 | $10.23 |
| milan (highest) | $15.05 tot $29.02 | 177 | $-5.25 | $9.80 |
| shanghai (lowest) | $10.12 tot $18.75 | 16 | $-2.31 | $7.82 |
| seoul (lowest) | $7.87 tot $14.38 | 20 | $-0.65 | $7.22 |
| jeddah (highest) | $9.02 tot $18.53 | 47 | $-1.89 | $7.13 |
| seoul (highest) | $9.91 tot $21.90 | 126 | $-3.26 | $6.65 |
| sao-paulo (highest) | $9.34 tot $18.75 | 123 | $-3.45 | $5.89 |
| wellington (highest) | $9.51 tot $21.34 | 117 | $-3.81 | $5.70 |
| singapore (highest) | $8.99 tot $20.35 | 95 | $-3.45 | $5.54 |
| mexico-city (highest) | $13.44 tot $26.33 | 70 | $-8.46 | $4.98 |
| karachi (highest) | $12.20 tot $23.39 | 66 | $-7.31 | $4.90 |
| taipei (highest) | $13.01 tot $22.70 | 86 | $-8.12 | $4.89 |
| kuala-lumpur (highest) | $11.38 tot $21.59 | 83 | $-6.88 | $4.49 |
| los-angeles (highest) | $10.98 tot $24.97 | 213 | $-6.80 | $4.18 |
| amsterdam (highest) | $12.09 tot $27.34 | 242 | $-7.93 | $4.16 |
| buenos-aires (highest) | $10.08 tot $19.16 | 91 | $-6.57 | $3.51 |
| toronto (highest) | $9.72 tot $20.00 | 105 | $-7.10 | $2.63 |
| chongqing (highest) | $11.76 tot $24.70 | 96 | $-9.48 | $2.28 |
| wuhan (highest) | $12.26 tot $27.53 | 94 | $-10.40 | $1.86 |
| paris (highest) | $13.19 tot $29.67 | 210 | $-13.00 | $0.18 |
| chicago (highest) | $17.95 tot $34.56 | 263 | $-17.91 | $0.04 |
| london (lowest) | $10.36 tot $19.62 | 69 | $-10.64 | $-0.28 |
| nyc (lowest) | $3.87 tot $6.43 | 9 | $-4.21 | $-0.34 |
| tokyo (lowest) | $8.62 tot $15.66 | 31 | $-9.32 | $-0.70 |
| houston (highest) | $18.65 tot $39.41 | 183 | $-19.36 | $-0.72 |
| munich (highest) | $14.23 tot $31.38 | 209 | $-15.26 | $-1.03 |
| shanghai (highest) | $10.69 tot $24.45 | 159 | $-12.45 | $-1.77 |
| dallas (highest) | $14.37 tot $30.58 | 158 | $-16.57 | $-2.20 |
| moscow (highest) | $12.86 tot $25.68 | 114 | $-15.20 | $-2.34 |
| shenzhen (highest) | $10.54 tot $22.46 | 204 | $-12.99 | $-2.45 |
| tel-aviv (highest) | $14.22 tot $30.95 | 122 | $-16.69 | $-2.47 |
| london (highest) | $14.40 tot $33.18 | 295 | $-17.47 | $-3.07 |
| busan (highest) | $12.24 tot $26.94 | 160 | $-15.32 | $-3.08 |
| san-francisco (highest) | $15.47 tot $30.53 | 184 | $-18.70 | $-3.23 |
| paris (lowest) | $11.79 tot $21.44 | 57 | $-16.98 | $-5.19 |
| ankara (highest) | $9.52 tot $19.41 | 101 | $-14.87 | $-5.35 |
| helsinki (highest) | $19.58 tot $41.28 | 270 | $-25.86 | $-6.28 |
| hong-kong (highest) | $8.06 tot $17.74 | 269 | $-15.37 | $-7.31 |
| lucknow (highest) | $15.40 tot $32.29 | 108 | $-23.41 | $-8.00 |
| qingdao (highest) | $10.59 tot $21.16 | 91 | $-20.11 | $-9.52 |
| guangzhou (highest) | $14.83 tot $30.15 | 249 | $-24.54 | $-9.71 |
| madrid (highest) | $12.39 tot $29.00 | 193 | $-22.73 | $-10.34 |
| hong-kong (lowest) | $7.08 tot $12.87 | 114 | $-20.37 | $-13.29 |
| atlanta (highest) | $16.90 tot $36.92 | 369 | $-31.60 | $-14.70 |
| miami (highest) | $16.64 tot $35.14 | 179 | $-31.59 | $-14.95 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
