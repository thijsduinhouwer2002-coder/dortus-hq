# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.52 tot $1.37 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 9 runs, 3030 minuten (50.5 uur) (GEZIEN). Markten in de data: 1806. Uitslag bekend voor 550 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-74.64 (1790 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-49.67 (271 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 715 | 219 | $4,159 | $9,150 | $147 tot $303 | 2275 / 1449 | $7,227 | $-288 (316 nog zonder prijs) | $0.00 (0 van 2275 beslist) | $-141 tot $14.92 |
| **Totaal** | 3030 | | $4,615 | $9,150 | $777 tot $1,612 | 9336 / 6517 | $30,248 | $-861 | $-124 | $-84.10 tot $751 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-647 over 9296 vullingen en $30,137, dus -2.15% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.98% over $28,915 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.86%.

**Opgeschaald (GOK):** per dag $-58.84 (ondergrens) tot $338 (hoge schatting) netto (gemeten minuten × 1440 / 3030).

444 van de 9336 vullingen ($1,333) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.98%): $-39.70 (GOK).

Geld dat de bot nodig had: gemiddeld $4,615 in open orders plus de hoogste stand van $9,150 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,765**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-769 tot $4,419 |
| €5,000 | $5,000 | $-1,924 tot $11,047 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-124 over 2061 vullingen en $6,922, dus -1.80% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.04% per dollar over 8833 vullingen, 1 uur later -2.79% over 8425 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.26% per dollar over 463 vullingen, 1 uur later -6.32% over 445 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-1.62 (295 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $-28.72 (34 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 715 | 219 | $4,099 | $3,346 | $37.16 tot $97.01 | 425 / 274 | $1,411 | $-58.68 (60 nog zonder prijs) | $0.00 (0 van 425 beslist) | $-21.52 tot $38.33 |
| **Totaal** | 3030 | | $4,539 | $3,346 | $187 tot $484 | 1666 / 1104 | $5,928 | $-186 | $-30.34 | $0.77 tot $298 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-162 over 1655 vullingen en $5,874, dus -2.76% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.30% over $5,641 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.86%.

**Opgeschaald (GOK):** per dag $-4.13 (ondergrens) tot $137 (hoge schatting) netto (gemeten minuten × 1440 / 3030).

97 van de 1666 vullingen ($287) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.30%): $-9.47 (GOK).

Geld dat de bot nodig had: gemiddeld $4,539 in open orders plus de hoogste stand van $3,346 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,885**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-94.28 tot $3,128 |
| €5,000 | $5,000 | $-236 tot $7,820 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-30.34 over 329 vullingen en $1,239, dus -2.45% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.89% per dollar over 1539 vullingen, 1 uur later -3.46% over 1449 (GEZIEN).
- Laagste temperatuur: 5 minuten later -0.84% per dollar over 116 vullingen, 1 uur later -0.57% over 112 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 788 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.38 tot $2.82 | $-0.76 tot $0.68 | 2 | $20.78 tot $27.63 | $-71.00 tot $-64.15 |
| €150 | 2 | $2.76 tot $5.65 | $-1.52 tot $1.37 | 3 | $26.48 tot $37.82 | $-65.31 tot $-53.96 |
| €200 | 3 | $4.14 tot $8.47 | $-2.28 tot $2.05 | 4 | $32.96 tot $49.94 | $-34.06 tot $-17.08 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.98%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest san-francisco-on-november-22 54-55°F | 1288 | $1.73 tot $3.28 | 30 | $-13.95 | $0.00 |
| highest wellington-on-november-23 19°C | 281 | $1.33 tot $2.63 | 17 | $-13.54 | $0.00 |
| highest london-on-november-21 10°C or higher | 2264 | $4.90 tot $11.44 | 100 | $-16.40 | $0.00 |
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest busan-on-november-22 8°C | 1673 | $3.19 tot $6.69 | 22 | $-13.32 | $0.00 |
| highest hong-kong-on-november-23 23°C | 134 | $0.05 tot $0.12 | 2 | $-9.73 | $0.00 |
| highest helsinki-on-november-21 4°C | 2105 | $6.64 tot $14.22 | 83 | $-15.83 | $0.00 |
| highest guangzhou-on-november-20 17°C | 381 | $0.42 tot $0.91 | 33 | $-9.43 | $-18.63 |
| highest qingdao-on-november-22 11°C | 1604 | $2.10 tot $4.01 | 20 | $-10.16 | $0.00 |
| highest chicago-on-november-21 70-71°F | 2336 | $3.75 tot $7.16 | 63 | $-11.79 | $0.00 |
| ... | | | | | |
| highest paris-on-november-21 11°C | 2247 | $3.20 tot $7.05 | 43 | $0.92 | $0.00 |
| lowest miami-on-november-22 72-73°F | 1366 | $3.04 tot $5.40 | 7 | $1.09 | $0.00 |
| lowest hong-kong-on-november-21 15°C | 576 | $1.36 tot $2.41 | 24 | $2.79 | $0.00 |
| highest tel-aviv-on-november-21 27°C | 1505 | $2.44 tot $5.69 | 26 | $1.88 | $0.00 |
| highest mexico-city-on-november-21 24°C | 2046 | $3.70 tot $7.25 | 17 | $0.65 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest london-on-november-22 9°C | 1756 | $2.17 tot $4.91 | 32 | $5.13 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $16.15 tot $34.65 | 155 | $-1.48 | $14.67 |
| austin (highest) | $23.19 tot $49.11 | 195 | $-8.63 | $14.56 |
| beijing (highest) | $12.64 tot $27.34 | 127 | $1.35 | $13.99 |
| miami (lowest) | $19.18 tot $34.62 | 52 | $-5.81 | $13.37 |
| chengdu (highest) | $15.65 tot $35.26 | 151 | $-6.31 | $9.34 |
| sao-paulo (highest) | $10.95 tot $22.02 | 142 | $-3.08 | $7.86 |
| nyc (highest) | $21.54 tot $45.79 | 346 | $-14.03 | $7.51 |
| manila (highest) | $10.57 tot $20.89 | 87 | $-3.32 | $7.24 |
| tokyo (highest) | $12.43 tot $28.50 | 205 | $-5.21 | $7.23 |
| taipei (highest) | $15.00 tot $26.67 | 114 | $-8.91 | $6.09 |
| shanghai (lowest) | $11.54 tot $21.25 | 38 | $-5.90 | $5.64 |
| milan (highest) | $17.07 tot $33.31 | 213 | $-11.49 | $5.58 |
| los-angeles (highest) | $12.61 tot $28.76 | 263 | $-7.17 | $5.45 |
| nyc (lowest) | $6.64 tot $11.31 | 35 | $-1.44 | $5.20 |
| seoul (highest) | $12.97 tot $28.58 | 171 | $-8.02 | $4.96 |
| seoul (lowest) | $10.52 tot $19.45 | 32 | $-5.76 | $4.76 |
| wuhan (highest) | $14.36 tot $32.12 | 130 | $-9.65 | $4.70 |
| kuala-lumpur (highest) | $13.63 tot $25.94 | 104 | $-9.68 | $3.96 |
| chongqing (highest) | $13.23 tot $28.10 | 106 | $-9.78 | $3.45 |
| mexico-city (highest) | $16.90 tot $33.05 | 108 | $-14.15 | $2.75 |
| jeddah (highest) | $11.12 tot $22.49 | 67 | $-9.73 | $1.39 |
| london (lowest) | $13.93 tot $25.88 | 79 | $-12.71 | $1.21 |
| london (highest) | $17.43 tot $40.06 | 367 | $-16.27 | $1.17 |
| toronto (highest) | $12.29 tot $24.98 | 149 | $-11.63 | $0.67 |
| singapore (highest) | $12.61 tot $28.11 | 189 | $-12.21 | $0.40 |
| shenzhen (highest) | $12.29 tot $26.26 | 237 | $-12.04 | $0.25 |
| houston (highest) | $23.48 tot $49.44 | 250 | $-23.72 | $-0.25 |
| karachi (highest) | $13.62 tot $26.46 | 89 | $-13.87 | $-0.26 |
| munich (highest) | $15.51 tot $34.44 | 258 | $-16.47 | $-0.96 |
| amsterdam (highest) | $14.10 tot $31.66 | 285 | $-15.27 | $-1.17 |
| buenos-aires (highest) | $12.06 tot $23.48 | 142 | $-13.35 | $-1.29 |
| paris (highest) | $16.01 tot $36.17 | 266 | $-18.64 | $-2.63 |
| tel-aviv (highest) | $15.77 tot $34.47 | 144 | $-18.75 | $-2.98 |
| dallas (highest) | $18.70 tot $39.39 | 229 | $-23.15 | $-4.46 |
| tokyo (lowest) | $10.45 tot $18.45 | 42 | $-15.17 | $-4.72 |
| ankara (highest) | $12.96 tot $25.35 | 162 | $-17.78 | $-4.82 |
| moscow (highest) | $15.17 tot $29.87 | 139 | $-20.38 | $-5.21 |
| shanghai (highest) | $12.18 tot $28.18 | 185 | $-17.76 | $-5.58 |
| paris (lowest) | $14.69 tot $27.78 | 66 | $-21.22 | $-6.53 |
| helsinki (highest) | $21.52 tot $45.90 | 298 | $-28.44 | $-6.92 |
| lucknow (highest) | $17.82 tot $37.62 | 133 | $-24.85 | $-7.03 |
| guangzhou (highest) | $18.02 tot $36.46 | 291 | $-28.11 | $-10.09 |
| hong-kong (lowest) | $7.56 tot $13.63 | 120 | $-20.84 | $-13.28 |
| madrid (highest) | $14.57 tot $33.67 | 228 | $-28.07 | $-13.50 |
| chicago (highest) | $22.98 tot $43.87 | 352 | $-37.16 | $-14.18 |
| hong-kong (highest) | $11.57 tot $25.43 | 333 | $-25.80 | $-14.23 |
| atlanta (highest) | $21.56 tot $47.10 | 455 | $-37.13 | $-15.57 |
| qingdao (highest) | $12.89 tot $25.70 | 119 | $-29.13 | $-16.24 |
| miami (highest) | $19.60 tot $41.52 | 241 | $-36.22 | $-16.62 |
| san-francisco (highest) | $19.10 tot $37.78 | 253 | $-36.60 | $-17.50 |
| wellington (highest) | $13.61 tot $30.12 | 201 | $-33.68 | $-20.07 |
| busan (highest) | $15.23 tot $33.56 | 193 | $-46.63 | $-31.40 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
