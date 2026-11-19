# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

Gemeten: 2 runs, 681 minuten (11.3 uur) (GEZIEN). Markten in de data: 656. Uitslag bekend voor 0 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 681 | 252 | $4,746 | $4,041 | $180 tot $377 | 2350 / 1638 | $7,916 | $-154 (223 nog zonder prijs) | $0.00 (0 van 2350 beslist) | $25.59 tot $223 |
| **Totaal** | 681 | | $4,746 | $4,041 | $180 tot $377 | 2350 / 1638 | $7,916 | $-154 | $0.00 | $25.59 tot $223 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-127 over 2348 vullingen en $7,905, dus -1.61% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.12% over $7,252 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.05%.

**Opgeschaald (GOK):** per dag $24.28 (ondergrens) tot $441 (hoge schatting) netto (gemeten minuten × 1440 / 681).

223 van de 2350 vullingen ($664) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.12%): $-14.11 (GOK).

Geld dat de bot nodig had: gemiddeld $4,746 in open orders plus de hoogste stand van $4,041 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,788**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $497 tot $9,043 |
| €5,000 | $5,000 | $1,243 tot $22,607 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

- Hoogste temperatuur: 5 minuten later -1.55% per dollar over 2244 vullingen, 1 uur later -1.96% over 2029 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.00% per dollar over 104 vullingen, 1 uur later -6.04% over 98 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 681 | 252 | $4,707 | $1,052 | $42.29 tot $104 | 409 / 294 | $1,474 | $-51.72 (40 nog zonder prijs) | $0.00 (0 van 409 beslist) | $-9.42 tot $52.44 |
| **Totaal** | 681 | | $4,707 | $1,052 | $42.29 tot $104 | 409 / 294 | $1,474 | $-51.72 | $0.00 | $-9.42 tot $52.44 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-31.44 over 409 vullingen en $1,474, dus -2.13% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.91% over $1,322 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -5.26%.

**Opgeschaald (GOK):** per dag $-32.53 (ondergrens) tot $98.27 (hoge schatting) netto (gemeten minuten × 1440 / 681).

40 van de 409 vullingen ($152) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.91%): $-5.96 (GOK).

Geld dat de bot nodig had: gemiddeld $4,707 in open orders plus de hoogste stand van $1,052 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$5,759**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,017 tot $3,072 |
| €5,000 | $5,000 | $-2,542 tot $7,679 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

- Hoogste temperatuur: 5 minuten later -1.97% per dollar over 393 vullingen, 1 uur later -4.06% over 357 (GEZIEN).
- Laagste temperatuur: 5 minuten later -7.38% per dollar over 16 vullingen, 1 uur later +2.10% over 12 (GEZIEN).

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest guangzhou-on-november-20 17°C | 381 | $0.42 tot $0.91 | 33 | $-9.43 | $0.00 |
| highest london-on-november-21 10°C or higher | 638 | $1.22 tot $2.76 | 19 | $-7.98 | $0.00 |
| highest shenzhen-on-november-20 20°C | 379 | $0.40 tot $0.95 | 21 | $-6.96 | $0.00 |
| highest guangzhou-on-november-20 19°C | 372 | $0.90 tot $1.75 | 56 | $-7.03 | $0.00 |
| highest helsinki-on-november-21 2°C | 529 | $0.47 tot $1.00 | 6 | $-6.52 | $0.00 |
| highest moscow-on-november-21 5°C | 622 | $1.04 tot $2.30 | 4 | $-6.25 | $0.00 |
| highest atlanta-on-november-21 68-69°F | 303 | $0.54 tot $1.13 | 8 | $-4.89 | $0.00 |
| highest paris-on-november-21 10°C | 678 | $0.79 tot $1.79 | 9 | $-4.95 | $0.00 |
| highest chongqing-on-november-20 17°C | 216 | $0.61 tot $1.10 | 11 | $-4.75 | $0.00 |
| ... | | | | | |
| highest chicago-on-november-20 66-67°F | 650 | $0.62 tot $1.42 | 19 | $1.64 | $0.00 |
| highest taipei-on-november-21 21°C | 517 | $1.26 tot $2.39 | 8 | $1.11 | $0.00 |
| highest munich-on-november-21 8°C | 622 | $1.41 tot $3.03 | 5 | $1.00 | $0.00 |
| highest london-on-november-21 8°C | 564 | $0.50 tot $1.09 | 15 | $2.34 | $0.00 |
| highest helsinki-on-november-20 6°C | 652 | $0.97 tot $2.10 | 22 | $1.98 | $0.00 |
| highest austin-on-november-20 76-77°F | 676 | $1.19 tot $2.69 | 14 | $1.85 | $0.00 |
| highest helsinki-on-november-20 5°C | 665 | $1.66 tot $3.37 | 23 | $1.95 | $0.00 |
| highest milan-on-november-21 16°C | 529 | $4.28 tot $5.46 | 6 | $-0.55 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| munich (highest) | $4.72 tot $10.76 | 68 | $2.39 | $7.11 |
| manila (highest) | $2.97 tot $5.79 | 47 | $2.66 | $5.63 |
| san-francisco (highest) | $4.50 tot $8.99 | 27 | $0.67 | $5.17 |
| austin (highest) | $5.50 tot $11.39 | 44 | $-0.68 | $4.82 |
| taipei (highest) | $5.29 tot $7.93 | 27 | $-0.72 | $4.57 |
| qingdao (highest) | $3.39 tot $6.37 | 25 | $1.03 | $4.41 |
| nyc (highest) | $3.76 tot $8.88 | 65 | $0.47 | $4.23 |
| warsaw (highest) | $4.62 tot $9.69 | 58 | $-0.77 | $3.85 |
| los-angeles (highest) | $2.38 tot $5.74 | 30 | $1.32 | $3.70 |
| houston (highest) | $4.51 tot $9.89 | 29 | $-0.91 | $3.60 |
| busan (highest) | $2.78 tot $6.28 | 58 | $0.60 | $3.37 |
| tel-aviv (highest) | $3.69 tot $7.84 | 31 | $-0.36 | $3.32 |
| tokyo (highest) | $2.73 tot $6.57 | 34 | $0.52 | $3.25 |
| beijing (highest) | $2.95 tot $6.39 | 41 | $0.16 | $3.12 |
| wuhan (highest) | $3.02 tot $7.40 | 18 | $0.01 | $3.02 |
| seoul (lowest) | $2.80 tot $4.86 | 10 | $-0.06 | $2.73 |
| shanghai (lowest) | $3.47 tot $6.22 | 5 | $-0.78 | $2.69 |
| ankara (highest) | $2.45 tot $5.09 | 24 | $0.18 | $2.62 |
| jeddah (highest) | $1.94 tot $4.05 | 14 | $0.60 | $2.54 |
| seoul (highest) | $2.52 tot $5.72 | 51 | $-0.12 | $2.40 |
| wellington (highest) | $2.09 tot $4.95 | 37 | $0.27 | $2.36 |
| tokyo (lowest) | $2.51 tot $4.39 | 7 | $-0.39 | $2.12 |
| milan (highest) | $5.84 tot $8.87 | 27 | $-3.76 | $2.08 |
| singapore (highest) | $2.63 tot $5.85 | 29 | $-0.59 | $2.04 |
| chicago (highest) | $3.84 tot $8.13 | 60 | $-1.88 | $1.96 |
| chengdu (highest) | $3.42 tot $8.09 | 51 | $-1.78 | $1.64 |
| miami (lowest) | $4.04 tot $7.66 | 7 | $-2.45 | $1.59 |
| london (lowest) | $3.70 tot $7.47 | 37 | $-2.23 | $1.47 |
| mexico-city (highest) | $3.63 tot $7.30 | 18 | $-2.45 | $1.18 |
| buenos-aires (highest) | $1.70 tot $3.63 | 13 | $-0.70 | $1.00 |
| karachi (highest) | $4.01 tot $7.95 | 30 | $-3.08 | $0.94 |
| toronto (highest) | $2.04 tot $4.46 | 13 | $-1.59 | $0.45 |
| nyc (lowest) | $0.28 tot $0.55 | 0 | $0.00 | $0.28 |
| helsinki (highest) | $6.35 tot $13.39 | 66 | $-6.65 | $-0.30 |
| sao-paulo (highest) | $1.72 tot $3.38 | 47 | $-2.09 | $-0.37 |
| shanghai (highest) | $2.92 tot $6.77 | 44 | $-3.42 | $-0.50 |
| dallas (highest) | $3.71 tot $8.38 | 38 | $-4.83 | $-1.12 |
| hong-kong (highest) | $2.83 tot $5.91 | 152 | $-4.38 | $-1.55 |
| paris (lowest) | $3.86 tot $7.28 | 19 | $-5.68 | $-1.81 |
| atlanta (highest) | $4.35 tot $10.25 | 87 | $-6.35 | $-2.00 |
| chongqing (highest) | $4.08 tot $8.65 | 53 | $-6.36 | $-2.28 |
| amsterdam (highest) | $2.52 tot $5.95 | 60 | $-5.15 | $-2.62 |
| kuala-lumpur (highest) | $3.70 tot $7.13 | 38 | $-6.50 | $-2.80 |
| lucknow (highest) | $3.69 tot $8.36 | 43 | $-6.62 | $-2.92 |
| hong-kong (lowest) | $2.72 tot $5.50 | 19 | $-5.84 | $-3.12 |
| london (highest) | $3.94 tot $9.06 | 92 | $-7.34 | $-3.40 |
| shenzhen (highest) | $3.60 tot $7.64 | 155 | $-7.81 | $-4.21 |
| madrid (highest) | $3.05 tot $7.50 | 65 | $-7.29 | $-4.25 |
| paris (highest) | $3.26 tot $7.77 | 68 | $-8.06 | $-4.80 |
| moscow (highest) | $3.66 tot $7.71 | 42 | $-11.11 | $-7.45 |
| miami (highest) | $5.08 tot $11.44 | 72 | $-16.30 | $-11.21 |
| guangzhou (highest) | $4.87 tot $9.74 | 155 | $-17.88 | $-13.02 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
