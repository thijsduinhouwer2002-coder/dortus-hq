# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-0.29 tot $2.64 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 3 runs, 1017 minuten (16.9 uur) (GEZIEN). Markten in de data: 662. Uitslag bekend voor 0 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $0.00 (0 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 122 | 216 | $4,123 | $4,875 | $19.46 tot $42.78 | 324 / 229 | $1,025 | $-12.50 (148 nog zonder prijs) | $0.00 (0 van 324 beslist) | $6.96 tot $30.28 |
| **Totaal** | 1017 | | $4,580 | $4,875 | $240 tot $509 | 3311 / 2332 | $10,917 | $-216 | $0.00 | $23.88 tot $293 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-171 over 3308 vullingen en $10,908, dus -1.56% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.07% over $10,409 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -2.83%.

**Opgeschaald (GOK):** per dag $18.88 (ondergrens) tot $400 (hoge schatting) netto (gemeten minuten × 1440 / 1017).

162 van de 3311 vullingen ($508) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.07%): $-10.55 (GOK).

Geld dat de bot nodig had: gemiddeld $4,580 in open orders plus de hoogste stand van $4,875 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$9,455**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $359 tot $7,606 |
| €5,000 | $5,000 | $899 tot $19,016 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

- Hoogste temperatuur: 5 minuten later -1.53% per dollar over 3166 vullingen, 1 uur later -1.91% over 3017 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.46% per dollar over 142 vullingen, 1 uur later -6.41% over 131 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $0.00 (0 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 122 | 216 | $4,032 | $1,515 | $4.42 tot $11.69 | 58 / 36 | $233 | $1.60 (34 nog zonder prijs) | $0.00 (0 van 58 beslist) | $6.02 tot $13.29 |
| **Totaal** | 1017 | | $4,511 | $1,515 | $55.48 tot $139 | 548 / 388 | $2,033 | $-50.91 | $0.00 | $4.58 tot $87.81 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-42.66 over 548 vullingen en $2,033, dus -2.10% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.68% over $1,901 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.91%.

**Opgeschaald (GOK):** per dag $1.50 (ondergrens) tot $119 (hoge schatting) netto (gemeten minuten × 1440 / 1017).

40 van de 548 vullingen ($131) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.68%): $-3.51 (GOK).

Geld dat de bot nodig had: gemiddeld $4,511 in open orders plus de hoogste stand van $1,515 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$6,026**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $44.94 tot $3,566 |
| €5,000 | $5,000 | $112 tot $8,914 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

- Hoogste temperatuur: 5 minuten later -2.04% per dollar over 526 vullingen, 1 uur later -2.73% over 489 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.71% per dollar over 22 vullingen, 1 uur later -0.94% over 19 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 415 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.33 tot $2.79 | $-0.15 tot $1.32 | 2 | $13.74 tot $17.38 | $0.15 tot $3.79 |
| €150 | 2 | $2.65 tot $5.58 | $-0.29 tot $2.64 | 3 | $20.22 tot $29.50 | $31.39 tot $40.67 |
| €200 | 3 | $3.98 tot $8.37 | $-0.44 tot $3.96 | 4 | $25.68 tot $39.48 | $36.86 tot $50.65 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.07%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest london-on-november-21 10°C or higher | 972 | $1.69 tot $3.93 | 32 | $-12.75 | $0.00 |
| highest guangzhou-on-november-20 17°C | 381 | $0.42 tot $0.91 | 33 | $-9.43 | $0.00 |
| highest shenzhen-on-november-20 20°C | 379 | $0.40 tot $0.95 | 21 | $-6.96 | $0.00 |
| highest guangzhou-on-november-20 19°C | 372 | $0.90 tot $1.75 | 56 | $-7.03 | $0.00 |
| highest helsinki-on-november-20 6°C | 729 | $1.12 tot $2.39 | 29 | $-7.18 | $0.00 |
| highest miami-on-november-20 80-81°F | 995 | $1.51 tot $3.46 | 29 | $-7.36 | $0.00 |
| highest helsinki-on-november-21 2°C | 865 | $0.54 tot $1.16 | 10 | $-5.99 | $0.00 |
| highest amsterdam-on-november-20 8°C | 828 | $0.74 tot $1.95 | 33 | $-5.88 | $0.00 |
| highest moscow-on-november-21 5°C | 950 | $1.46 tot $3.25 | 9 | $-6.01 | $0.00 |
| ... | | | | | |
| highest london-on-november-21 8°C | 898 | $0.63 tot $1.41 | 21 | $1.98 | $0.00 |
| highest munich-on-november-21 8°C | 952 | $1.92 tot $4.09 | 11 | $0.74 | $0.00 |
| highest los-angeles-on-november-20 66-67°F | 1014 | $0.92 tot $2.37 | 34 | $1.77 | $0.00 |
| highest austin-on-november-20 76-77°F | 1011 | $1.84 tot $4.14 | 15 | $1.07 | $0.00 |
| highest chicago-on-november-20 66-67°F | 968 | $1.18 tot $2.50 | 32 | $2.18 | $0.00 |
| highest nyc-on-november-20 70-71°F | 1014 | $0.50 tot $1.11 | 36 | $3.25 | $0.00 |
| highest milan-on-november-21 16°C | 853 | $4.47 tot $5.90 | 10 | $-0.41 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $6.35 tot $13.35 | 69 | $1.42 | $7.77 |
| los-angeles (highest) | $3.89 tot $9.40 | 85 | $3.19 | $7.08 |
| manila (highest) | $3.96 tot $7.76 | 56 | $2.04 | $5.99 |
| munich (highest) | $6.15 tot $13.96 | 97 | $-0.22 | $5.94 |
| san-francisco (highest) | $5.96 tot $12.32 | 40 | $-0.53 | $5.43 |
| austin (highest) | $7.62 tot $15.99 | 56 | $-2.72 | $4.90 |
| houston (highest) | $6.90 tot $14.97 | 44 | $-2.24 | $4.66 |
| tel-aviv (highest) | $5.11 tot $11.08 | 57 | $-0.61 | $4.50 |
| wellington (highest) | $2.87 tot $6.87 | 49 | $1.63 | $4.50 |
| jeddah (highest) | $2.40 tot $5.12 | 25 | $1.96 | $4.36 |
| seoul (highest) | $3.16 tot $7.25 | 61 | $0.97 | $4.13 |
| nyc (highest) | $6.16 tot $14.15 | 152 | $-2.21 | $3.95 |
| wuhan (highest) | $3.76 tot $9.17 | 31 | $0.06 | $3.83 |
| beijing (highest) | $3.72 tot $8.15 | 46 | $-0.23 | $3.49 |
| tokyo (highest) | $3.43 tot $8.32 | 48 | $-0.04 | $3.39 |
| milan (highest) | $6.45 tot $10.38 | 36 | $-3.08 | $3.37 |
| shanghai (lowest) | $4.13 tot $7.51 | 6 | $-0.77 | $3.36 |
| miami (lowest) | $6.00 tot $10.93 | 17 | $-2.72 | $3.28 |
| seoul (lowest) | $3.21 tot $5.68 | 11 | $-0.01 | $3.20 |
| chengdu (highest) | $4.08 tot $9.62 | 58 | $-1.25 | $2.82 |
| ankara (highest) | $3.00 tot $6.39 | 32 | $-0.40 | $2.60 |
| tokyo (lowest) | $2.96 tot $5.26 | 8 | $-0.39 | $2.57 |
| busan (highest) | $4.01 tot $9.23 | 83 | $-2.24 | $1.78 |
| karachi (highest) | $4.53 tot $9.12 | 31 | $-2.78 | $1.76 |
| qingdao (highest) | $4.15 tot $8.07 | 43 | $-2.69 | $1.46 |
| sao-paulo (highest) | $3.20 tot $6.31 | 78 | $-2.32 | $0.88 |
| buenos-aires (highest) | $3.52 tot $7.49 | 26 | $-2.73 | $0.80 |
| nyc (lowest) | $0.39 tot $0.74 | 1 | $0.06 | $0.45 |
| chicago (highest) | $5.85 tot $12.08 | 120 | $-5.61 | $0.24 |
| singapore (highest) | $3.45 tot $7.69 | 35 | $-3.31 | $0.15 |
| atlanta (highest) | $6.54 tot $15.63 | 139 | $-6.53 | $0.01 |
| mexico-city (highest) | $5.15 tot $10.44 | 37 | $-5.36 | $-0.21 |
| paris (highest) | $4.57 tot $10.83 | 92 | $-4.95 | $-0.38 |
| kuala-lumpur (highest) | $4.57 tot $8.92 | 45 | $-5.20 | $-0.62 |
| hong-kong (highest) | $3.34 tot $7.19 | 162 | $-4.14 | $-0.80 |
| taipei (highest) | $6.13 tot $9.71 | 41 | $-7.18 | $-1.05 |
| helsinki (highest) | $7.76 tot $16.49 | 104 | $-8.90 | $-1.14 |
| london (lowest) | $4.94 tot $10.08 | 50 | $-6.33 | $-1.39 |
| dallas (highest) | $5.77 tot $12.83 | 68 | $-7.17 | $-1.40 |
| chongqing (highest) | $4.94 tot $10.66 | 65 | $-6.59 | $-1.65 |
| hong-kong (lowest) | $3.87 tot $7.32 | 25 | $-5.91 | $-2.04 |
| lucknow (highest) | $4.05 tot $9.43 | 47 | $-6.38 | $-2.33 |
| toronto (highest) | $3.73 tot $7.95 | 45 | $-6.15 | $-2.42 |
| amsterdam (highest) | $3.41 tot $8.11 | 90 | $-5.96 | $-2.55 |
| paris (lowest) | $4.96 tot $9.27 | 24 | $-8.67 | $-3.71 |
| shenzhen (highest) | $4.41 tot $9.57 | 161 | $-8.27 | $-3.86 |
| madrid (highest) | $4.35 tot $10.73 | 87 | $-9.36 | $-5.00 |
| moscow (highest) | $4.71 tot $9.90 | 51 | $-10.37 | $-5.66 |
| shanghai (highest) | $3.73 tot $8.54 | 69 | $-9.48 | $-5.75 |
| london (highest) | $5.44 tot $12.65 | 136 | $-12.78 | $-7.34 |
| guangzhou (highest) | $5.62 tot $11.46 | 161 | $-18.18 | $-12.56 |
| miami (highest) | $7.43 tot $16.54 | 111 | $-24.31 | $-16.88 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
