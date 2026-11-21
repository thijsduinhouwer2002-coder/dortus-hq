# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.60 tot $1.50 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 10 runs, 3365 minuten (56.1 uur) (GEZIEN). Markten in de data: 1806. Uitslag bekend voor 748 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-47.46 (2178 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-225 (841 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1050 | 220 | $4,172 | $9,635 | $243 tot $503 | 3634 / 2417 | $11,310 | $-398 (312 nog zonder prijs) | $0.00 (0 van 3634 beslist) | $-155 tot $106 |
| **Totaal** | 3365 | | $4,574 | $9,635 | $874 tot $1,812 | 10695 / 7485 | $34,331 | $-971 | $-272 | $-97.39 tot $841 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-788 over 10668 vullingen en $34,245, dus -2.30% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.94% over $32,981 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.84%.

**Opgeschaald (GOK):** per dag $-58.69 (ondergrens) tot $343 (hoge schatting) netto (gemeten minuten × 1440 / 3365).

440 van de 10695 vullingen ($1,350) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.94%): $-39.76 (GOK).

Geld dat de bot nodig had: gemiddeld $4,574 in open orders plus de hoogste stand van $9,635 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,209**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-743 tot $4,346 |
| €5,000 | $5,000 | $-1,859 tot $10,865 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-272 over 3019 vullingen en $9,943, dus -2.74% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.20% per dollar over 10144 vullingen, 1 uur later -2.81% over 9720 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.22% per dollar over 524 vullingen, 1 uur later -5.20% over 512 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $17.37 (363 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $-65.68 (121 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1050 | 220 | $4,115 | $3,911 | $61.94 tot $162 | 721 / 460 | $2,540 | $-75.70 (62 nog zonder prijs) | $0.00 (0 van 721 beslist) | $-13.77 tot $86.50 |
| **Totaal** | 3365 | | $4,500 | $3,911 | $212 tot $549 | 1962 / 1290 | $7,058 | $-203 | $-48.31 | $8.53 tot $346 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-202 over 1952 vullingen en $7,005, dus -2.88% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.02% over $6,719 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.71%.

**Opgeschaald (GOK):** per dag $-0.73 (ondergrens) tot $144 (hoge schatting) netto (gemeten minuten × 1440 / 3365).

99 van de 1962 vullingen ($339) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.02%): $-10.25 (GOK).

Geld dat de bot nodig had: gemiddeld $4,500 in open orders plus de hoogste stand van $3,911 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,411**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-15.72 tot $3,075 |
| €5,000 | $5,000 | $-39.31 tot $7,686 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-48.31 over 484 vullingen en $1,780, dus -2.71% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.97% per dollar over 1817 vullingen, 1 uur later -3.18% over 1723 (GEZIEN).
- Laagste temperatuur: 5 minuten later -1.57% per dollar over 135 vullingen, 1 uur later -0.38% over 131 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 844 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.48 tot $3.03 | $-0.80 tot $0.75 | 2 | $27.91 tot $39.34 | $-19.15 tot $-7.73 |
| €150 | 2 | $2.97 tot $6.07 | $-1.60 tot $1.50 | 3 | $38.24 tot $58.46 | $-78.80 tot $-58.58 |
| €200 | 3 | $4.45 tot $9.10 | $-2.39 tot $2.25 | 5 | $48.27 tot $79.32 | $-131 tot $-100 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.94%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 608 | $2.37 tot $4.83 | 35 | $-15.59 | $0.00 |
| highest atlanta-on-november-22 61°F or below | 1014 | $0.86 tot $1.86 | 35 | $-13.66 | $0.00 |
| highest san-francisco-on-november-22 54-55°F | 1598 | $2.22 tot $4.34 | 40 | $-14.26 | $0.00 |
| highest london-on-november-21 10°C or higher | 2264 | $4.90 tot $11.44 | 100 | $-16.40 | $0.00 |
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest hong-kong-on-november-23 23°C | 291 | $0.22 tot $0.49 | 7 | $-10.32 | $0.00 |
| highest busan-on-november-22 8°C | 1830 | $3.65 tot $7.73 | 29 | $-13.42 | $0.00 |
| highest helsinki-on-november-21 4°C | 2105 | $6.64 tot $14.22 | 83 | $-15.83 | $0.00 |
| highest guangzhou-on-november-20 17°C | 381 | $0.42 tot $0.91 | 33 | $-9.43 | $-18.63 |
| highest qingdao-on-november-22 11°C | 1796 | $2.58 tot $4.74 | 22 | $-10.81 | $0.00 |
| ... | | | | | |
| highest paris-on-november-21 11°C | 2247 | $3.20 tot $7.05 | 43 | $0.92 | $0.00 |
| lowest hong-kong-on-november-21 15°C | 576 | $1.36 tot $2.41 | 24 | $2.79 | $0.00 |
| highest tel-aviv-on-november-21 27°C | 1505 | $2.44 tot $5.69 | 26 | $1.88 | $0.00 |
| highest mexico-city-on-november-21 24°C | 2046 | $3.70 tot $7.25 | 17 | $0.65 | $0.00 |
| lowest miami-on-november-22 72-73°F | 1493 | $3.79 tot $6.61 | 8 | $1.42 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest london-on-november-22 9°C | 2086 | $3.00 tot $6.57 | 36 | $4.76 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| miami (lowest) | $21.38 tot $38.57 | 55 | $-4.24 | $17.14 |
| austin (highest) | $25.28 tot $53.63 | 225 | $-10.77 | $14.51 |
| beijing (highest) | $14.24 tot $30.83 | 154 | $-1.77 | $12.47 |
| warsaw (highest) | $19.85 tot $42.61 | 208 | $-8.02 | $11.83 |
| chengdu (highest) | $17.88 tot $40.26 | 163 | $-6.74 | $11.14 |
| seoul (highest) | $14.64 tot $32.46 | 202 | $-4.20 | $10.44 |
| milan (highest) | $19.21 tot $37.89 | 233 | $-9.63 | $9.58 |
| seoul (lowest) | $11.66 tot $21.67 | 50 | $-2.55 | $9.12 |
| manila (highest) | $11.41 tot $22.67 | 91 | $-2.94 | $8.47 |
| los-angeles (highest) | $13.54 tot $31.01 | 279 | $-5.58 | $7.96 |
| kuala-lumpur (highest) | $14.91 tot $28.44 | 124 | $-7.90 | $7.01 |
| tokyo (highest) | $13.73 tot $31.62 | 238 | $-8.19 | $5.54 |
| london (lowest) | $15.72 tot $29.40 | 96 | $-10.57 | $5.15 |
| taipei (highest) | $16.09 tot $28.58 | 118 | $-11.02 | $5.07 |
| nyc (lowest) | $7.94 tot $13.50 | 39 | $-2.94 | $5.00 |
| chongqing (highest) | $15.75 tot $33.45 | 142 | $-10.84 | $4.91 |
| shanghai (lowest) | $11.82 tot $21.69 | 41 | $-7.06 | $4.76 |
| sao-paulo (highest) | $12.44 tot $24.86 | 162 | $-7.80 | $4.64 |
| houston (highest) | $25.71 tot $54.17 | 286 | $-22.11 | $3.60 |
| mexico-city (highest) | $17.99 tot $35.35 | 120 | $-15.32 | $2.67 |
| jeddah (highest) | $12.31 tot $24.93 | 73 | $-9.86 | $2.45 |
| toronto (highest) | $13.39 tot $27.19 | 166 | $-11.66 | $1.72 |
| karachi (highest) | $15.38 tot $29.60 | 99 | $-14.14 | $1.24 |
| buenos-aires (highest) | $13.78 tot $26.96 | 154 | $-12.61 | $1.17 |
| wuhan (highest) | $16.01 tot $35.53 | 143 | $-15.01 | $0.99 |
| nyc (highest) | $24.89 tot $52.37 | 424 | $-23.93 | $0.97 |
| ankara (highest) | $14.43 tot $28.37 | 175 | $-14.10 | $0.33 |
| lucknow (highest) | $21.28 tot $44.35 | 185 | $-21.20 | $0.08 |
| shenzhen (highest) | $13.88 tot $29.64 | 249 | $-14.09 | $-0.21 |
| paris (highest) | $18.70 tot $42.22 | 340 | $-19.32 | $-0.62 |
| munich (highest) | $16.98 tot $38.01 | 288 | $-17.82 | $-0.84 |
| london (highest) | $19.67 tot $44.93 | 404 | $-21.43 | $-1.76 |
| amsterdam (highest) | $16.08 tot $36.13 | 321 | $-19.11 | $-3.03 |
| singapore (highest) | $15.04 tot $33.39 | 249 | $-18.85 | $-3.81 |
| tel-aviv (highest) | $18.62 tot $40.24 | 170 | $-22.48 | $-3.86 |
| moscow (highest) | $16.43 tot $32.57 | 150 | $-20.80 | $-4.37 |
| paris (lowest) | $17.11 tot $32.22 | 72 | $-21.55 | $-4.44 |
| dallas (highest) | $20.93 tot $44.60 | 259 | $-27.07 | $-6.14 |
| tokyo (lowest) | $11.23 tot $19.41 | 49 | $-17.38 | $-6.15 |
| shanghai (highest) | $14.03 tot $32.26 | 225 | $-23.11 | $-9.07 |
| hong-kong (lowest) | $7.79 tot $13.98 | 123 | $-19.89 | $-12.10 |
| hong-kong (highest) | $14.32 tot $30.84 | 374 | $-27.26 | $-12.94 |
| helsinki (highest) | $24.47 tot $51.95 | 341 | $-38.13 | $-13.66 |
| chicago (highest) | $24.67 tot $47.28 | 376 | $-38.49 | $-13.83 |
| madrid (highest) | $16.17 tot $37.53 | 253 | $-31.50 | $-15.33 |
| qingdao (highest) | $13.82 tot $27.38 | 121 | $-29.81 | $-15.99 |
| guangzhou (highest) | $21.32 tot $43.13 | 333 | $-37.81 | $-16.48 |
| san-francisco (highest) | $20.23 tot $40.18 | 268 | $-36.84 | $-16.61 |
| miami (highest) | $21.85 tot $46.47 | 267 | $-40.17 | $-18.33 |
| wellington (highest) | $15.44 tot $34.12 | 241 | $-38.80 | $-23.36 |
| busan (highest) | $16.97 tot $37.32 | 220 | $-45.66 | $-28.69 |
| atlanta (highest) | $25.19 tot $54.61 | 557 | $-60.92 | $-35.73 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
