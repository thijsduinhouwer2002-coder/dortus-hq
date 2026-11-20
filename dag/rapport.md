# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-0.67 tot $2.56 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 5 runs, 1687 minuten (28.1 uur) (GEZIEN). Markten in de data: 1236. Uitslag bekend voor 11 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-1.00 (3 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 792 | 246 | $4,676 | $7,335 | $230 tot $475 | 2152 / 1566 | $7,024 | $-237 (188 nog zonder prijs) | $0.00 (0 van 2152 beslist) | $-6.53 tot $239 |
| **Totaal** | 1687 | | $4,658 | $7,335 | $451 tot $941 | 5139 / 3669 | $16,917 | $-440 | $-1.00 | $10.39 tot $501 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-317 over 5118 vullingen en $16,858, dus -1.88% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.69% over $16,368 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.44%.

**Opgeschaald (GOK):** per dag $-3.72 (ondergrens) tot $415 (hoge schatting) netto (gemeten minuten × 1440 / 1687).

202 van de 5139 vullingen ($549) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.69%): $-14.76 (GOK).

Geld dat de bot nodig had: gemiddeld $4,658 in open orders plus de hoogste stand van $7,335 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$11,993**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-55.86 tot $6,230 |
| €5,000 | $5,000 | $-140 tot $15,574 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1.00 over 3 vullingen en $19.00, dus -5.26% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -1.85% per dollar over 4842 vullingen, 1 uur later -2.47% over 4675 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.42% per dollar over 276 vullingen, 1 uur later -6.51% over 248 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $0.00 (0 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 792 | 246 | $4,597 | $2,377 | $54.92 tot $142 | 396 / 257 | $1,440 | $-34.73 (31 nog zonder prijs) | $0.00 (0 van 396 beslist) | $20.19 tot $107 |
| **Totaal** | 1687 | | $4,586 | $2,377 | $106 tot $269 | 886 / 609 | $3,240 | $-87.23 | $0.00 | $18.75 tot $182 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-75.56 over 880 vullingen en $3,211, dus -2.35% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.77% over $3,150 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.58%.

**Opgeschaald (GOK):** per dag $13.87 (ondergrens) tot $153 (hoge schatting) netto (gemeten minuten × 1440 / 1687).

37 van de 886 vullingen ($90.28) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.77%): $-2.50 (GOK).

Geld dat de bot nodig had: gemiddeld $4,586 in open orders plus de hoogste stand van $2,377 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$6,963**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $359 tot $3,956 |
| €5,000 | $5,000 | $896 tot $9,891 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

- Hoogste temperatuur: 5 minuten later -2.67% per dollar over 811 vullingen, 1 uur later -2.78% over 781 (GEZIEN).
- Laagste temperatuur: 5 minuten later +1.64% per dollar over 69 vullingen, 1 uur later -1.52% over 62 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 626 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.57 tot $3.18 | $-0.33 tot $1.28 | 2 | $16.18 tot $29.19 | $-1.21 tot $11.80 |
| €150 | 2 | $3.13 tot $6.36 | $-0.67 tot $2.56 | 3 | $22.94 tot $42.15 | $-3.12 tot $16.10 |
| €200 | 3 | $4.70 tot $9.54 | $-1.00 tot $3.83 | 4 | $28.64 tot $52.35 | $2.58 tot $26.29 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.69%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest london-on-november-21 10°C or higher | 1636 | $3.33 tot $7.76 | 75 | $-16.48 | $0.00 |
| highest helsinki-on-november-21 4°C | 1599 | $4.83 tot $10.45 | 41 | $-16.15 | $0.00 |
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest guangzhou-on-november-20 17°C | 381 | $0.42 tot $0.91 | 33 | $-9.43 | $0.00 |
| highest qingdao-on-november-22 11°C | 272 | $0.60 tot $1.12 | 7 | $-8.52 | $0.00 |
| highest helsinki-on-november-21 3°C | 1191 | $2.23 tot $4.82 | 20 | $-9.18 | $0.00 |
| highest helsinki-on-november-21 2°C | 1484 | $0.68 tot $1.55 | 20 | $-7.28 | $0.00 |
| highest shenzhen-on-november-20 20°C | 379 | $0.40 tot $0.95 | 21 | $-6.96 | $0.00 |
| highest qingdao-on-november-22 12°C | 266 | $0.64 tot $1.33 | 3 | $-7.10 | $0.00 |
| highest guangzhou-on-november-21 22°C | 1537 | $2.50 tot $5.14 | 23 | $-8.63 | $0.00 |
| ... | | | | | |
| highest busan-on-november-21 9°C | 1628 | $3.75 tot $7.46 | 38 | $-0.56 | $0.00 |
| highest chicago-on-november-20 66-67°F | 1115 | $1.84 tot $3.51 | 34 | $1.35 | $0.00 |
| highest busan-on-november-21 8°C | 1554 | $1.75 tot $4.27 | 31 | $1.51 | $0.00 |
| highest munich-on-november-21 8°C | 1619 | $2.82 tot $6.06 | 16 | $0.51 | $0.00 |
| highest los-angeles-on-november-20 66-67°F | 1360 | $1.19 tot $3.07 | 42 | $2.23 | $0.00 |
| highest austin-on-november-20 76-77°F | 1240 | $2.64 tot $5.79 | 16 | $1.27 | $0.00 |
| highest milan-on-november-21 16°C | 1523 | $5.30 tot $7.79 | 17 | $0.25 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $9.85 tot $20.95 | 87 | $1.64 | $11.49 |
| austin (highest) | $12.90 tot $26.95 | 84 | $-3.77 | $9.13 |
| munich (highest) | $9.84 tot $21.79 | 119 | $-1.12 | $8.72 |
| manila (highest) | $6.25 tot $12.46 | 62 | $2.18 | $8.43 |
| chengdu (highest) | $9.62 tot $21.84 | 97 | $-1.70 | $7.92 |
| tokyo (highest) | $7.96 tot $18.45 | 108 | $-0.10 | $7.86 |
| beijing (highest) | $8.46 tot $18.06 | 64 | $-0.93 | $7.53 |
| seoul (highest) | $7.48 tot $16.79 | 94 | $-1.11 | $6.37 |
| seoul (lowest) | $6.53 tot $11.77 | 16 | $-0.23 | $6.30 |
| miami (lowest) | $10.03 tot $18.11 | 29 | $-3.83 | $6.20 |
| shanghai (lowest) | $8.18 tot $14.87 | 11 | $-2.15 | $6.03 |
| los-angeles (highest) | $7.07 tot $16.48 | 132 | $-1.47 | $5.60 |
| jeddah (highest) | $5.78 tot $11.99 | 38 | $-0.90 | $4.88 |
| nyc (highest) | $11.91 tot $26.06 | 207 | $-7.05 | $4.87 |
| san-francisco (highest) | $10.21 tot $20.55 | 116 | $-6.15 | $4.06 |
| tokyo (lowest) | $6.48 tot $11.83 | 15 | $-2.61 | $3.87 |
| wellington (highest) | $7.51 tot $17.03 | 98 | $-3.72 | $3.79 |
| mexico-city (highest) | $9.01 tot $17.78 | 49 | $-5.40 | $3.61 |
| milan (highest) | $10.30 tot $18.74 | 91 | $-7.11 | $3.19 |
| karachi (highest) | $8.31 tot $16.40 | 43 | $-5.15 | $3.16 |
| buenos-aires (highest) | $5.76 tot $11.72 | 47 | $-2.64 | $3.13 |
| ankara (highest) | $6.10 tot $12.70 | 59 | $-3.05 | $3.04 |
| houston (highest) | $13.14 tot $27.89 | 106 | $-10.39 | $2.75 |
| singapore (highest) | $6.28 tot $14.32 | 58 | $-3.55 | $2.72 |
| chongqing (highest) | $8.52 tot $18.12 | 75 | $-6.05 | $2.48 |
| kuala-lumpur (highest) | $8.13 tot $16.01 | 71 | $-6.31 | $1.82 |
| shanghai (highest) | $7.83 tot $18.09 | 116 | $-6.05 | $1.79 |
| wuhan (highest) | $9.06 tot $20.76 | 67 | $-7.29 | $1.76 |
| london (lowest) | $8.65 tot $16.57 | 62 | $-6.95 | $1.70 |
| sao-paulo (highest) | $5.72 tot $11.20 | 95 | $-4.56 | $1.16 |
| paris (highest) | $8.61 tot $19.68 | 126 | $-7.45 | $1.16 |
| toronto (highest) | $6.10 tot $12.80 | 68 | $-5.76 | $0.34 |
| tel-aviv (highest) | $9.11 tot $20.00 | 89 | $-9.26 | $-0.15 |
| taipei (highest) | $10.27 tot $17.61 | 67 | $-10.59 | $-0.32 |
| shenzhen (highest) | $8.23 tot $17.56 | 184 | $-9.92 | $-1.70 |
| dallas (highest) | $9.66 tot $20.74 | 102 | $-11.48 | $-1.82 |
| nyc (lowest) | $1.50 tot $2.63 | 6 | $-3.48 | $-1.98 |
| amsterdam (highest) | $6.70 tot $15.43 | 141 | $-8.86 | $-2.16 |
| busan (highest) | $9.67 tot $21.34 | 142 | $-12.28 | $-2.61 |
| moscow (highest) | $8.36 tot $17.41 | 82 | $-11.96 | $-3.60 |
| paris (lowest) | $8.78 tot $16.17 | 38 | $-12.61 | $-3.83 |
| london (highest) | $10.24 tot $23.59 | 228 | $-15.71 | $-5.47 |
| chicago (highest) | $11.72 tot $22.43 | 187 | $-17.21 | $-5.50 |
| hong-kong (highest) | $6.49 tot $14.08 | 231 | $-13.14 | $-6.64 |
| madrid (highest) | $8.03 tot $19.06 | 110 | $-15.71 | $-7.69 |
| qingdao (highest) | $7.94 tot $15.75 | 78 | $-19.80 | $-11.86 |
| hong-kong (lowest) | $6.54 tot $12.00 | 100 | $-18.49 | $-11.95 |
| atlanta (highest) | $11.51 tot $25.87 | 238 | $-24.05 | $-12.55 |
| lucknow (highest) | $11.09 tot $23.45 | 89 | $-23.84 | $-12.74 |
| guangzhou (highest) | $11.53 tot $23.20 | 221 | $-25.10 | $-13.57 |
| miami (highest) | $12.74 tot $26.48 | 141 | $-26.57 | $-13.84 |
| helsinki (highest) | $12.92 tot $27.66 | 155 | $-29.40 | $-16.48 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
