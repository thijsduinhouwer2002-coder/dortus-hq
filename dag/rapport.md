# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-0.32 tot $2.71 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 6 runs, 2023 minuten (33.7 uur) (GEZIEN). Markten in de data: 1236. Uitslag bekend voor 220 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-79.10 (618 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1128 | 257 | $4,880 | $8,512 | $339 tot $698 | 3318 / 2412 | $10,545 | $-303 (151 nog zonder prijs) | $0.00 (0 van 3318 beslist) | $36.04 tot $395 |
| **Totaal** | 2023 | | $4,775 | $8,512 | $560 tot $1,164 | 6305 / 4515 | $20,438 | $-507 | $-79.10 | $52.96 tot $657 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-354 over 6283 vullingen en $20,356, dus -1.74% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.54% over $19,965 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.27%.

**Opgeschaald (GOK):** per dag $29.17 (ondergrens) tot $459 (hoge schatting) netto (gemeten minuten × 1440 / 2023).

165 van de 6305 vullingen ($472) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.54%): $-11.99 (GOK).

Geld dat de bot nodig had: gemiddeld $4,775 in open orders plus de hoogste stand van $8,512 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,287**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $395 tot $6,224 |
| €5,000 | $5,000 | $988 tot $15,561 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-79.10 over 618 vullingen en $2,192, dus -3.61% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -1.68% per dollar over 5957 vullingen, 1 uur later -2.35% over 5807 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.78% per dollar over 326 vullingen, 1 uur later -5.70% over 319 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $44.89 (157 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1128 | 257 | $4,793 | $3,005 | $81.06 tot $211 | 597 / 382 | $2,183 | $-39.48 (30 nog zonder prijs) | $0.00 (0 van 597 beslist) | $41.58 tot $171 |
| **Totaal** | 2023 | | $4,697 | $3,005 | $132 tot $338 | 1087 / 734 | $3,983 | $-91.98 | $44.89 | $40.14 tot $246 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-86.62 over 1079 vullingen en $3,939, dus -2.20% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.37% over $3,878 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.23%.

**Opgeschaald (GOK):** per dag $26.81 (ondergrens) tot $173 (hoge schatting) netto (gemeten minuten × 1440 / 2023).

36 van de 1087 vullingen ($104) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.37%): $-2.47 (GOK).

Geld dat de bot nodig had: gemiddeld $4,697 in open orders plus de hoogste stand van $3,005 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,702**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $627 tot $4,051 |
| €5,000 | $5,000 | $1,566 tot $10,127 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $44.89 over 157 vullingen en $563, dus +7.98% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.45% per dollar over 998 vullingen, 1 uur later -2.32% over 964 (GEZIEN).
- Laagste temperatuur: 5 minuten later +1.15% per dollar over 81 vullingen, 1 uur later -2.09% over 81 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 666 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.46 tot $2.98 | $-0.16 tot $1.36 | 2 | $12.16 tot $23.08 | $2.94 tot $13.86 |
| €150 | 2 | $2.92 tot $5.95 | $-0.32 tot $2.71 | 3 | $18.64 tot $35.20 | $34.19 tot $50.74 |
| €200 | 3 | $4.38 tot $8.93 | $-0.47 tot $4.07 | 4 | $23.97 tot $42.95 | $35.50 tot $54.48 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.54%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest helsinki-on-november-21 4°C | 1933 | $6.05 tot $13.00 | 72 | $-19.09 | $0.00 |
| highest london-on-november-21 10°C or higher | 1972 | $4.18 tot $9.80 | 82 | $-16.66 | $0.00 |
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest guangzhou-on-november-20 17°C | 381 | $0.42 tot $0.91 | 33 | $-9.43 | $-18.63 |
| highest qingdao-on-november-22 12°C | 599 | $1.04 tot $2.26 | 5 | $-8.62 | $0.00 |
| highest qingdao-on-november-22 11°C | 606 | $1.04 tot $1.96 | 10 | $-8.21 | $0.00 |
| highest helsinki-on-november-21 2°C | 1650 | $0.71 tot $1.64 | 23 | $-7.68 | $0.00 |
| highest shenzhen-on-november-20 20°C | 379 | $0.40 tot $0.95 | 21 | $-6.96 | $-13.97 |
| highest miami-on-november-21 84-85°F | 1681 | $2.61 tot $5.39 | 21 | $-9.09 | $0.00 |
| highest busan-on-november-22 8°C | 667 | $1.62 tot $3.36 | 11 | $-7.95 | $0.00 |
| ... | | | | | |
| highest munich-on-november-21 8°C | 1954 | $3.24 tot $7.02 | 24 | $0.67 | $0.00 |
| highest austin-on-november-20 76-77°F | 1240 | $2.64 tot $5.79 | 16 | $1.27 | $0.00 |
| highest amsterdam-on-november-22 8°C | 598 | $0.88 tot $1.70 | 9 | $3.08 | $0.00 |
| highest atlanta-on-november-21 60-61°F | 873 | $1.53 tot $2.58 | 26 | $2.45 | $0.00 |
| lowest hong-kong-on-november-21 15°C | 576 | $1.36 tot $2.41 | 24 | $2.79 | $0.00 |
| highest tel-aviv-on-november-21 27°C | 1338 | $2.13 tot $4.96 | 23 | $2.51 | $0.00 |
| highest milan-on-november-21 16°C | 1855 | $5.77 tot $8.80 | 22 | $0.18 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $0.00 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $11.89 tot $25.41 | 100 | $1.94 | $13.82 |
| tokyo (highest) | $9.22 tot $21.23 | 125 | $2.94 | $12.16 |
| austin (highest) | $16.63 tot $34.59 | 125 | $-4.73 | $11.90 |
| beijing (highest) | $10.16 tot $21.77 | 91 | $1.51 | $11.67 |
| manila (highest) | $7.71 tot $15.27 | 69 | $2.79 | $10.50 |
| miami (lowest) | $12.41 tot $22.25 | 36 | $-2.56 | $9.85 |
| chengdu (highest) | $11.97 tot $27.01 | 112 | $-2.25 | $9.72 |
| nyc (highest) | $14.65 tot $31.75 | 237 | $-5.33 | $9.32 |
| jeddah (highest) | $7.85 tot $16.28 | 43 | $-0.85 | $7.00 |
| munich (highest) | $12.01 tot $26.64 | 163 | $-5.01 | $7.00 |
| seoul (lowest) | $7.40 tot $13.49 | 20 | $-0.65 | $6.76 |
| shanghai (lowest) | $9.47 tot $17.34 | 13 | $-2.86 | $6.61 |
| seoul (highest) | $9.42 tot $20.75 | 124 | $-3.24 | $6.18 |
| karachi (highest) | $10.74 tot $20.82 | 56 | $-5.01 | $5.72 |
| los-angeles (highest) | $9.18 tot $21.06 | 169 | $-3.95 | $5.23 |
| wellington (highest) | $8.66 tot $19.48 | 106 | $-3.68 | $4.97 |
| tokyo (lowest) | $7.68 tot $14.01 | 19 | $-2.82 | $4.86 |
| taipei (highest) | $12.40 tot $21.48 | 82 | $-7.97 | $4.42 |
| singapore (highest) | $8.37 tot $19.00 | 83 | $-4.28 | $4.09 |
| kuala-lumpur (highest) | $10.74 tot $20.23 | 81 | $-6.88 | $3.85 |
| ankara (highest) | $8.20 tot $16.82 | 79 | $-4.73 | $3.47 |
| sao-paulo (highest) | $7.36 tot $14.58 | 108 | $-4.06 | $3.29 |
| mexico-city (highest) | $10.92 tot $21.50 | 65 | $-8.53 | $2.39 |
| chongqing (highest) | $10.91 tot $22.88 | 91 | $-8.59 | $2.32 |
| toronto (highest) | $7.74 tot $16.12 | 84 | $-5.97 | $1.77 |
| shanghai (highest) | $9.74 tot $22.32 | 144 | $-7.99 | $1.75 |
| amsterdam (highest) | $9.42 tot $21.66 | 199 | $-7.73 | $1.69 |
| london (lowest) | $9.85 tot $18.74 | 66 | $-8.33 | $1.52 |
| wuhan (highest) | $11.22 tot $25.41 | 86 | $-9.88 | $1.35 |
| houston (highest) | $15.89 tot $33.64 | 126 | $-14.84 | $1.05 |
| milan (highest) | $12.70 tot $24.02 | 126 | $-11.77 | $0.92 |
| buenos-aires (highest) | $7.28 tot $14.58 | 76 | $-6.52 | $0.75 |
| tel-aviv (highest) | $11.85 tot $25.94 | 110 | $-11.11 | $0.74 |
| nyc (lowest) | $2.55 tot $4.41 | 7 | $-3.60 | $-1.06 |
| chicago (highest) | $14.87 tot $28.50 | 221 | $-16.00 | $-1.12 |
| moscow (highest) | $10.98 tot $22.37 | 101 | $-13.26 | $-2.28 |
| san-francisco (highest) | $12.59 tot $25.24 | 144 | $-15.43 | $-2.84 |
| paris (highest) | $11.20 tot $25.34 | 176 | $-14.24 | $-3.04 |
| shenzhen (highest) | $9.97 tot $21.25 | 197 | $-13.05 | $-3.08 |
| london (highest) | $12.73 tot $29.24 | 251 | $-16.39 | $-3.66 |
| busan (highest) | $11.58 tot $25.45 | 157 | $-15.37 | $-3.79 |
| dallas (highest) | $12.04 tot $25.58 | 131 | $-16.09 | $-4.04 |
| paris (lowest) | $10.67 tot $19.55 | 52 | $-15.32 | $-4.65 |
| madrid (highest) | $10.29 tot $24.31 | 149 | $-16.27 | $-5.98 |
| hong-kong (highest) | $7.63 tot $16.70 | 257 | $-15.17 | $-7.54 |
| lucknow (highest) | $14.55 tot $30.46 | 105 | $-23.66 | $-9.11 |
| atlanta (highest) | $14.34 tot $31.43 | 300 | $-24.95 | $-10.60 |
| qingdao (highest) | $9.56 tot $19.11 | 88 | $-20.17 | $-10.61 |
| guangzhou (highest) | $13.84 tot $28.06 | 241 | $-24.98 | $-11.13 |
| helsinki (highest) | $16.92 tot $35.81 | 239 | $-28.15 | $-11.23 |
| hong-kong (lowest) | $7.00 tot $12.74 | 114 | $-20.37 | $-13.37 |
| miami (highest) | $14.69 tot $30.50 | 161 | $-31.27 | $-16.59 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
