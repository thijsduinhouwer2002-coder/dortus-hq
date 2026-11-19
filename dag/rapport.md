# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket, twee grenzen voor de concurrentie: laag en hoog). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

Gemeten: 1 runs, 346 minuten (5.8 uur) (GEZIEN). Markten in de data: 645. Uitslag bekend voor 0 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Kapitaal gem. | Beloning laag tot hoog (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (laag tot hoog, 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 346 | 262 | $4,880 | $98.33 tot $202 | 1250 / 864 | $4,317 | $-94.69 (269 nog zonder prijs) | $0.00 (0 van 1250 beslist) | $3.64 tot $108 |
| **Totaal** | 346 | | $4,880 | $98.33 tot $202 | 1250 / 864 | $4,317 | $-94.69 | $0.00 | $3.64 tot $108 |

Verlies per gevulde dollar, 1 uur later: -2.70% over $3,509 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.57%.

**Opgeschaald (GOK):** per dag $15.14 tot $448 netto met gemiddeld $4,880 aan orders op het boek (gemeten minuten × 1440 / 346).

| Inleg | Op de boeken (× 1.0 $/€, hooguit wat de bot gebruikte) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $558 tot $16,511 |
| €5,000 | $4,880 | $1,363 tot $40,287 |

Opschalen gaat lineair met het geld op de boeken, en nooit boven wat de bot echt gebruikte: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Kapitaal gem. | Beloning laag tot hoog (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (laag tot hoog, 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 346 | 262 | $4,870 | $24.74 tot $58.43 | 225 / 174 | $807 | $-17.26 (55 nog zonder prijs) | $0.00 (0 van 225 beslist) | $7.49 tot $41.17 |
| **Totaal** | 346 | | $4,870 | $24.74 tot $58.43 | 225 / 174 | $807 | $-17.26 | $0.00 | $7.49 tot $41.17 |

Verlies per gevulde dollar, 1 uur later: -2.66% over $648 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.28%.

**Opgeschaald (GOK):** per dag $31.17 tot $171 netto met gemiddeld $4,870 aan orders op het boek (gemeten minuten × 1440 / 346).

| Inleg | Op de boeken (× 1.0 $/€, hooguit wat de bot gebruikte) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $1,152 tot $6,332 |
| €5,000 | $4,870 | $2,805 tot $15,421 |

Opschalen gaat lineair met het geld op de boeken, en nooit boven wat de bot echt gebruikte: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning laag plus resultaat 1 uur later).

| Markt | Minuten | Beloning laag tot hoog (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest hong-kong-on-november-20 20°C | 295 | $0.56 tot $1.17 | 48 | $-11.45 | $0.00 |
| highest shenzhen-on-november-20 20°C | 314 | $0.31 tot $0.77 | 15 | $-8.22 | $0.00 |
| highest helsinki-on-november-21 2°C | 194 | $0.33 tot $0.61 | 5 | $-6.52 | $0.00 |
| highest moscow-on-november-21 5°C | 299 | $0.66 tot $1.43 | 3 | $-6.50 | $0.00 |
| highest guangzhou-on-november-20 17°C | 326 | $0.32 tot $0.69 | 13 | $-4.10 | $0.00 |
| highest london-on-november-21 10°C or higher | 309 | $0.53 tot $1.17 | 12 | $-4.26 | $0.00 |
| highest paris-on-november-21 10°C | 344 | $0.42 tot $0.88 | 5 | $-4.03 | $0.00 |
| highest kuala-lumpur-on-november-20 34°C | 241 | $0.30 tot $0.63 | 5 | $-3.58 | $0.00 |
| highest guangzhou-on-november-20 19°C | 320 | $0.67 tot $1.32 | 20 | $-3.94 | $0.00 |
| highest miami-on-november-21 82-83°F | 325 | $0.49 tot $1.15 | 6 | $-3.50 | $0.00 |
| ... | | | | | |
| highest manila-on-november-20 33°C | 346 | $0.07 tot $0.17 | 4 | $1.66 | $0.00 |
| highest busan-on-november-21 8°C | 286 | $0.21 tot $0.46 | 3 | $1.59 | $0.00 |
| highest taipei-on-november-21 22°C | 191 | $1.88 tot $1.93 | 1 | $0.00 | $0.00 |
| highest shenzhen-on-november-20 18°C | 314 | $0.40 tot $0.82 | 40 | $1.59 | $0.00 |
| highest helsinki-on-november-20 5°C | 346 | $0.78 tot $1.66 | 11 | $1.64 | $0.00 |
| highest helsinki-on-november-20 6°C | 342 | $0.47 tot $1.10 | 15 | $2.49 | $0.00 |
| highest milan-on-november-21 16°C | 295 | $3.75 tot $4.36 | 2 | $0.03 | $0.00 |
| highest hong-kong-on-november-20 19°C | 237 | $0.63 tot $1.33 | 25 | $6.14 | $0.00 |
| highest shenzhen-on-november-20 19°C | 284 | $1.04 tot $1.97 | 46 | $7.41 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning laag tot hoog (GOK) | Vullingen | 1 uur later | Netto laag |
|---|---|---|---|---|
| milan (highest) | $4.44 tot $5.79 | 7 | $0.56 | $4.99 |
| hong-kong (highest) | $1.65 tot $3.56 | 117 | $2.58 | $4.23 |
| manila (highest) | $1.38 tot $2.75 | 37 | $2.83 | $4.21 |
| munich (highest) | $2.22 tot $5.12 | 29 | $1.25 | $3.47 |
| seoul (highest) | $1.62 tot $3.62 | 35 | $1.42 | $3.04 |
| taipei (highest) | $3.24 tot $4.69 | 11 | $-0.42 | $2.83 |
| chengdu (highest) | $2.15 tot $5.21 | 41 | $0.38 | $2.53 |
| los-angeles (highest) | $0.68 tot $1.62 | 17 | $1.66 | $2.34 |
| san-francisco (highest) | $1.95 tot $3.94 | 12 | $0.19 | $2.13 |
| seoul (lowest) | $2.25 tot $3.81 | 5 | $-0.22 | $2.03 |
| beijing (highest) | $1.92 tot $4.01 | 27 | $0.04 | $1.96 |
| wuhan (highest) | $1.97 tot $4.75 | 13 | $-0.02 | $1.95 |
| qingdao (highest) | $2.14 tot $4.07 | 17 | $-0.23 | $1.91 |
| busan (highest) | $1.79 tot $4.13 | 29 | $0.11 | $1.90 |
| wellington (highest) | $1.28 tot $2.89 | 27 | $0.21 | $1.49 |
| shanghai (lowest) | $2.06 tot $3.70 | 2 | $-0.59 | $1.47 |
| tokyo (highest) | $2.07 tot $4.90 | 22 | $-0.69 | $1.38 |
| ankara (highest) | $1.14 tot $2.34 | 7 | $0.21 | $1.35 |
| tokyo (lowest) | $1.76 tot $3.06 | 5 | $-0.52 | $1.24 |
| amsterdam (highest) | $0.96 tot $2.29 | 11 | $0.27 | $1.23 |
| mexico-city (highest) | $1.75 tot $3.35 | 9 | $-0.56 | $1.19 |
| shenzhen (highest) | $2.29 tot $4.74 | 112 | $-1.15 | $1.14 |
| nyc (highest) | $1.87 tot $4.42 | 19 | $-0.76 | $1.11 |
| jeddah (highest) | $0.88 tot $1.85 | 4 | $0.17 | $1.05 |
| singapore (highest) | $1.49 tot $3.27 | 20 | $-0.69 | $0.80 |
| hong-kong (lowest) | $1.90 tot $3.87 | 13 | $-1.11 | $0.79 |
| houston (highest) | $1.90 tot $4.11 | 10 | $-1.27 | $0.62 |
| miami (lowest) | $2.28 tot $4.42 | 2 | $-1.68 | $0.60 |
| nyc (lowest) | $0.28 tot $0.55 | 0 | $0.00 | $0.28 |
| lucknow (highest) | $2.01 tot $4.50 | 26 | $-2.02 | $-0.01 |
| toronto (highest) | $1.08 tot $2.31 | 6 | $-1.10 | $-0.03 |
| warsaw (highest) | $1.96 tot $3.97 | 33 | $-2.04 | $-0.08 |
| karachi (highest) | $2.48 tot $4.85 | 18 | $-2.57 | $-0.10 |
| shanghai (highest) | $1.71 tot $3.84 | 22 | $-1.90 | $-0.19 |
| dallas (highest) | $1.79 tot $4.01 | 22 | $-2.09 | $-0.29 |
| sao-paulo (highest) | $0.86 tot $1.65 | 16 | $-1.30 | $-0.45 |
| london (lowest) | $2.25 tot $4.39 | 18 | $-2.99 | $-0.74 |
| chicago (highest) | $1.94 tot $4.06 | 27 | $-2.69 | $-0.76 |
| austin (highest) | $2.34 tot $5.11 | 16 | $-3.23 | $-0.89 |
| buenos-aires (highest) | $0.66 tot $1.38 | 5 | $-1.56 | $-0.90 |
| madrid (highest) | $1.52 tot $3.70 | 36 | $-2.72 | $-1.20 |
| paris (lowest) | $2.28 tot $4.31 | 5 | $-4.25 | $-1.97 |
| tel-aviv (highest) | $1.01 tot $2.31 | 17 | $-3.12 | $-2.11 |
| helsinki (highest) | $3.66 tot $7.63 | 42 | $-5.88 | $-2.22 |
| chongqing (highest) | $2.37 tot $4.84 | 38 | $-5.15 | $-2.79 |
| atlanta (highest) | $2.08 tot $4.88 | 25 | $-5.06 | $-2.98 |
| london (highest) | $1.66 tot $3.79 | 34 | $-5.31 | $-3.66 |
| kuala-lumpur (highest) | $2.09 tot $3.97 | 24 | $-6.26 | $-4.17 |
| paris (highest) | $1.57 tot $3.71 | 29 | $-6.14 | $-4.57 |
| guangzhou (highest) | $3.24 tot $6.43 | 76 | $-9.71 | $-6.47 |
| miami (highest) | $2.70 tot $6.10 | 34 | $-10.14 | $-7.44 |
| moscow (highest) | $1.75 tot $3.70 | 21 | $-9.38 | $-7.64 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
