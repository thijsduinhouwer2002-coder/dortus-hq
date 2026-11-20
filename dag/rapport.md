# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $0.06 tot $3.39 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 4 runs, 1352 minuten (22.5 uur) (GEZIEN). Markten in de data: 1169. Uitslag bekend voor 0 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $0.00 (0 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 457 | 213 | $4,044 | $5,984 | $108 tot $223 | 1198 / 868 | $3,867 | $-73.61 (231 nog zonder prijs) | $0.00 (0 van 1198 beslist) | $34.58 tot $149 |
| **Totaal** | 1352 | | $4,440 | $5,984 | $329 tot $689 | 4185 / 2971 | $13,759 | $-277 | $0.00 | $51.50 tot $412 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-224 over 4160 vullingen en $13,684, dus -1.64% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.14% over $12,969 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -2.85%.

**Opgeschaald (GOK):** per dag $36.87 (ondergrens) tot $421 (hoge schatting) netto (gemeten minuten × 1440 / 1352).

245 van de 4185 vullingen ($791) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.14%): $-16.89 (GOK).

Geld dat de bot nodig had: gemiddeld $4,440 in open orders plus de hoogste stand van $5,984 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$10,424**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $637 tot $7,263 |
| €5,000 | $5,000 | $1,592 tot $18,157 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

- Hoogste temperatuur: 5 minuten later -1.62% per dollar over 3947 vullingen, 1 uur later -1.98% over 3743 (GEZIEN).
- Laagste temperatuur: 5 minuten later -1.92% per dollar over 213 vullingen, 1 uur later -5.36% over 194 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $0.00 (0 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 457 | 213 | $3,978 | $1,928 | $27.11 tot $69.17 | 229 / 147 | $827 | $-1.37 (57 nog zonder prijs) | $0.00 (0 van 229 beslist) | $25.73 tot $67.80 |
| **Totaal** | 1352 | | $4,374 | $1,928 | $78.16 tot $196 | 719 / 499 | $2,627 | $-53.88 | $0.00 | $24.29 tot $142 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-45.87 over 710 vullingen en $2,588, dus -1.77% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.23% over $2,421 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.29%.

**Opgeschaald (GOK):** per dag $20.97 (ondergrens) tot $147 (hoge schatting) netto (gemeten minuten × 1440 / 1352).

63 van de 719 vullingen ($207) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.23%): $-4.60 (GOK).

Geld dat de bot nodig had: gemiddeld $4,374 in open orders plus de hoogste stand van $1,928 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$6,302**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $599 tot $4,190 |
| €5,000 | $5,000 | $1,497 tot $10,474 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

- Hoogste temperatuur: 5 minuten later -2.15% per dollar over 659 vullingen, 1 uur later -2.51% over 608 (GEZIEN).
- Laagste temperatuur: 5 minuten later +3.60% per dollar over 51 vullingen, 1 uur later +1.98% over 48 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 474 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.61 tot $3.27 | $0.03 tot $1.69 | 2 | $20.10 tot $38.84 | $16.03 tot $34.77 |
| €150 | 2 | $3.21 tot $6.54 | $0.06 tot $3.39 | 3 | $28.33 tot $54.10 | $24.26 tot $50.03 |
| €200 | 3 | $4.82 tot $9.81 | $0.09 tot $5.08 | 4 | $37.82 tot $65.33 | $31.34 tot $58.85 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.14%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest london-on-november-21 10°C or higher | 1306 | $2.53 tot $5.92 | 56 | $-15.01 | $0.00 |
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest guangzhou-on-november-20 17°C | 381 | $0.42 tot $0.91 | 33 | $-9.43 | $0.00 |
| highest shenzhen-on-november-20 20°C | 379 | $0.40 tot $0.95 | 21 | $-6.96 | $0.00 |
| highest guangzhou-on-november-20 19°C | 372 | $0.90 tot $1.75 | 56 | $-7.03 | $0.00 |
| highest helsinki-on-november-20 6°C | 729 | $1.12 tot $2.39 | 29 | $-7.18 | $0.00 |
| highest guangzhou-on-november-21 22°C | 1208 | $1.85 tot $3.81 | 18 | $-7.70 | $0.00 |
| highest helsinki-on-november-21 2°C | 1200 | $0.60 tot $1.36 | 12 | $-5.92 | $0.00 |
| highest nyc-on-november-21 64-65°F | 1110 | $1.74 tot $3.78 | 22 | $-7.01 | $0.00 |
| highest amsterdam-on-november-20 8°C | 828 | $0.74 tot $1.95 | 33 | $-5.88 | $0.00 |
| ... | | | | | |
| highest lucknow-on-november-21 28°C | 1326 | $2.35 tot $5.42 | 10 | $0.42 | $0.00 |
| highest los-angeles-on-november-20 64-65°F | 1349 | $1.16 tot $2.85 | 26 | $1.68 | $0.00 |
| highest munich-on-november-21 8°C | 1286 | $2.37 tot $5.03 | 13 | $0.64 | $0.00 |
| highest chicago-on-november-20 66-67°F | 1115 | $1.84 tot $3.51 | 34 | $1.35 | $0.00 |
| highest los-angeles-on-november-20 66-67°F | 1349 | $1.15 tot $2.97 | 41 | $2.43 | $0.00 |
| highest austin-on-november-20 76-77°F | 1240 | $2.64 tot $5.79 | 16 | $1.27 | $0.00 |
| highest milan-on-november-21 16°C | 1188 | $4.84 tot $6.80 | 16 | $0.22 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $7.80 tot $16.39 | 76 | $2.30 | $10.10 |
| austin (highest) | $10.25 tot $21.48 | 63 | $-2.58 | $7.68 |
| los-angeles (highest) | $5.43 tot $12.88 | 102 | $2.23 | $7.66 |
| munich (highest) | $7.61 tot $17.00 | 102 | $-0.20 | $7.41 |
| manila (highest) | $4.89 tot $9.63 | 59 | $2.05 | $6.94 |
| milan (highest) | $7.71 tot $13.31 | 64 | $-1.77 | $5.95 |
| atlanta (highest) | $8.63 tot $20.21 | 172 | $-2.91 | $5.73 |
| beijing (highest) | $5.96 tot $12.65 | 58 | $-0.43 | $5.53 |
| jeddah (highest) | $3.48 tot $7.30 | 33 | $1.46 | $4.94 |
| chengdu (highest) | $6.19 tot $14.21 | 77 | $-1.27 | $4.92 |
| tokyo (highest) | $5.42 tot $12.60 | 84 | $-0.65 | $4.77 |
| wellington (highest) | $5.14 tot $11.64 | 72 | $-0.48 | $4.66 |
| seoul (lowest) | $4.60 tot $8.34 | 11 | $-0.01 | $4.59 |
| tokyo (lowest) | $4.42 tot $8.00 | 10 | $0.11 | $4.54 |
| san-francisco (highest) | $8.29 tot $16.92 | 87 | $-4.01 | $4.28 |
| wuhan (highest) | $5.70 tot $13.24 | 44 | $-1.72 | $3.99 |
| shanghai (lowest) | $6.02 tot $10.87 | 9 | $-2.15 | $3.86 |
| tel-aviv (highest) | $6.78 tot $14.66 | 79 | $-2.95 | $3.83 |
| miami (lowest) | $7.44 tot $13.41 | 27 | $-3.73 | $3.71 |
| seoul (highest) | $5.61 tot $12.34 | 83 | $-1.91 | $3.70 |
| busan (highest) | $5.57 tot $12.60 | 109 | $-1.93 | $3.64 |
| ankara (highest) | $3.95 tot $8.36 | 46 | $-0.67 | $3.27 |
| mexico-city (highest) | $7.80 tot $15.34 | 46 | $-4.92 | $2.87 |
| karachi (highest) | $5.66 tot $11.20 | 35 | $-2.98 | $2.68 |
| houston (highest) | $9.53 tot $20.63 | 79 | $-6.98 | $2.55 |
| nyc (highest) | $8.82 tot $19.70 | 179 | $-6.46 | $2.35 |
| qingdao (highest) | $5.20 tot $10.20 | 52 | $-3.27 | $1.93 |
| hong-kong (lowest) | $5.75 tot $10.42 | 58 | $-4.09 | $1.66 |
| taipei (highest) | $7.41 tot $12.20 | 55 | $-5.92 | $1.49 |
| buenos-aires (highest) | $4.47 tot $9.44 | 35 | $-3.18 | $1.29 |
| paris (highest) | $6.29 tot $14.52 | 106 | $-5.35 | $0.94 |
| singapore (highest) | $4.25 tot $9.68 | 47 | $-3.47 | $0.78 |
| dallas (highest) | $7.58 tot $16.81 | 86 | $-6.83 | $0.74 |
| kuala-lumpur (highest) | $5.79 tot $11.40 | 53 | $-5.10 | $0.69 |
| sao-paulo (highest) | $4.31 tot $8.47 | 90 | $-3.72 | $0.59 |
| london (lowest) | $6.95 tot $13.53 | 58 | $-7.00 | $-0.06 |
| chongqing (highest) | $6.15 tot $13.26 | 69 | $-6.75 | $-0.59 |
| toronto (highest) | $5.33 tot $11.18 | 59 | $-6.82 | $-1.50 |
| shenzhen (highest) | $5.91 tot $12.75 | 169 | $-8.07 | $-2.17 |
| nyc (lowest) | $0.52 tot $0.92 | 6 | $-3.14 | $-2.62 |
| helsinki (highest) | $9.48 tot $20.22 | 123 | $-12.14 | $-2.66 |
| shanghai (highest) | $5.61 tot $12.61 | 87 | $-8.53 | $-2.93 |
| amsterdam (highest) | $4.46 tot $10.46 | 116 | $-7.42 | $-2.95 |
| lucknow (highest) | $6.70 tot $14.67 | 62 | $-9.99 | $-3.29 |
| hong-kong (highest) | $4.10 tot $8.89 | 184 | $-7.79 | $-3.70 |
| moscow (highest) | $6.11 tot $12.79 | 66 | $-10.25 | $-4.14 |
| madrid (highest) | $5.63 tot $13.90 | 95 | $-10.09 | $-4.46 |
| paris (lowest) | $6.82 tot $12.52 | 35 | $-12.32 | $-5.50 |
| london (highest) | $7.82 tot $18.05 | 192 | $-13.41 | $-5.59 |
| chicago (highest) | $8.58 tot $17.14 | 164 | $-18.21 | $-9.63 |
| miami (highest) | $10.45 tot $21.72 | 126 | $-25.88 | $-15.43 |
| guangzhou (highest) | $8.17 tot $16.12 | 186 | $-25.73 | $-17.56 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
