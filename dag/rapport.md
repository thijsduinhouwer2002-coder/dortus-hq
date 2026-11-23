# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.33 tot $1.84 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 17 runs, 5712 minuten (95.2 uur) (GEZIEN). Markten in de data: 2849. Uitslag bekend voor 1693 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-310 (4034 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-73.87 (3313 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-77.49 (286 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 555 | 179 | $3,410 | $8,779 | $129 tot $262 | 1710 / 1304 | $5,520 | $-159 (209 nog zonder prijs) | $0.00 (0 van 1710 beslist) | $-30.32 tot $103 |
| **Totaal** | 5712 | | $4,177 | $10,171 | $1,454 tot $2,985 | 17991 / 12989 | $57,855 | $-1,760 | $-1,004 | $-306 tot $1,225 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-1,289 over 17944 vullingen en $57,715, dus -2.23% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -3.11% over $56,504 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -4.00%.

**Opgeschaald (GOK):** per dag $-87.69 (ondergrens) tot $298 (hoge schatting) netto (gemeten minuten × 1440 / 5712).

470 van de 17991 vullingen ($1,350) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -3.11%): $-42.05 (GOK).

Geld dat de bot nodig had: gemiddeld $4,177 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,348**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,100 tot $3,742 |
| €5,000 | $5,000 | $-2,750 tot $9,354 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,004 over 10620 vullingen en $34,384, dus -2.92% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.14% per dollar over 17169 vullingen, 1 uur later -3.02% over 16739 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.15% per dollar over 775 vullingen, 1 uur later -4.86% over 756 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $134 (741 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-52.26 (633 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $6.61 (78 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 555 | 179 | $3,348 | $3,671 | $31.49 tot $83.64 | 367 / 241 | $1,257 | $-43.09 (38 nog zonder prijs) | $0.00 (0 van 367 beslist) | $-11.60 tot $40.55 |
| **Totaal** | 5712 | | $4,106 | $4,020 | $356 tot $934 | 3441 / 2226 | $12,496 | $-337 | $3.93 | $19.42 tot $597 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-305 over 3425 vullingen en $12,429, dus -2.46% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.77% over $12,166 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.99%.

**Opgeschaald (GOK):** per dag $2.59 (ondergrens) tot $148 (hoge schatting) netto (gemeten minuten × 1440 / 5712).

100 van de 3441 vullingen ($330) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.77%): $-9.15 (GOK).

Geld dat de bot nodig had: gemiddeld $4,106 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,126**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $57.38 tot $3,284 |
| €5,000 | $5,000 | $143 tot $8,210 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $3.93 over 1942 vullingen en $7,076, dus +0.06% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.46% per dollar over 3229 vullingen, 1 uur later -2.85% over 3142 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.34% per dollar over 196 vullingen, 1 uur later -1.11% over 190 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1211 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.53 tot $3.12 | $-0.66 tot $0.92 | 2 | $17.33 tot $30.35 | $-38.26 tot $-25.24 |
| €150 | 2 | $3.07 tot $6.24 | $-1.33 tot $1.84 | 3 | $24.47 tot $45.56 | $-39.63 tot $-18.55 |
| €200 | 3 | $4.60 tot $9.35 | $-1.99 tot $2.76 | 4 | $32.87 tot $58.44 | $-31.69 tot $-6.12 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-3.11%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $0.00 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $0.00 |
| highest toronto-on-november-23 12°C | 1200 | $2.93 tot $5.19 | 44 | $-18.45 | $0.00 |
| highest wellington-on-november-23 18°C | 1574 | $4.34 tot $9.03 | 56 | $-18.80 | $0.00 |
| highest san-francisco-on-november-22 54-55°F | 2416 | $3.52 tot $6.93 | 50 | $-17.70 | $0.00 |
| lowest seoul-on-november-23 3°C | 720 | $0.81 tot $1.65 | 27 | $-14.61 | $0.00 |
| highest atlanta-on-november-22 61°F or below | 1305 | $1.47 tot $3.28 | 60 | $-15.20 | $8.29 |
| highest helsinki-on-november-23 2°C | 1643 | $5.38 tot $10.33 | 51 | $-17.99 | $0.00 |
| ... | | | | | |
| highest munich-on-november-23 2°C | 1524 | $4.87 tot $9.08 | 36 | $0.59 | $0.00 |
| highest austin-on-november-22 74-75°F | 2464 | $4.94 tot $9.96 | 32 | $0.59 | $15.35 |
| lowest miami-on-november-22 72-73°F | 1769 | $5.03 tot $8.87 | 9 | $1.29 | $14.94 |
| highest warsaw-on-november-22 4°C | 2271 | $4.51 tot $9.55 | 43 | $2.34 | $23.20 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest chicago-on-november-22 56-57°F | 2262 | $3.74 tot $6.27 | 57 | $6.34 | $11.46 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| miami (lowest) | $36.15 tot $63.67 | 90 | $-4.91 | $31.24 |
| chengdu (highest) | $28.00 tot $61.82 | 276 | $-10.89 | $17.11 |
| london (lowest) | $26.19 tot $48.69 | 161 | $-10.43 | $15.77 |
| los-angeles (highest) | $27.02 tot $60.52 | 476 | $-11.64 | $15.37 |
| beijing (highest) | $24.13 tot $51.16 | 285 | $-11.29 | $12.85 |
| warsaw (highest) | $36.39 tot $76.65 | 360 | $-23.73 | $12.65 |
| austin (highest) | $43.04 tot $89.90 | 417 | $-30.59 | $12.44 |
| seoul (highest) | $27.94 tot $59.51 | 411 | $-17.73 | $10.21 |
| taipei (highest) | $24.16 tot $44.64 | 237 | $-14.76 | $9.40 |
| manila (highest) | $16.96 tot $33.79 | 145 | $-7.56 | $9.40 |
| jeddah (highest) | $18.22 tot $36.73 | 114 | $-8.87 | $9.35 |
| karachi (highest) | $21.71 tot $42.66 | 137 | $-13.53 | $8.17 |
| kuala-lumpur (highest) | $22.38 tot $42.86 | 214 | $-14.24 | $8.14 |
| chongqing (highest) | $28.05 tot $58.57 | 231 | $-20.55 | $7.50 |
| mexico-city (highest) | $28.51 tot $54.77 | 167 | $-21.71 | $6.80 |
| paris (lowest) | $29.92 tot $55.20 | 101 | $-23.65 | $6.28 |
| milan (highest) | $30.47 tot $61.70 | 383 | $-24.51 | $5.96 |
| wuhan (highest) | $24.47 tot $53.09 | 205 | $-18.65 | $5.82 |
| shanghai (lowest) | $11.87 tot $21.74 | 41 | $-7.06 | $4.81 |
| sao-paulo (highest) | $21.32 tot $42.61 | 257 | $-16.55 | $4.77 |
| shenzhen (highest) | $19.97 tot $42.52 | 333 | $-15.28 | $4.69 |
| singapore (highest) | $26.07 tot $56.54 | 374 | $-22.19 | $3.87 |
| tokyo (highest) | $23.77 tot $53.19 | 436 | $-20.10 | $3.67 |
| houston (highest) | $45.05 tot $93.76 | 648 | $-42.50 | $2.55 |
| nyc (lowest) | $13.09 tot $22.29 | 87 | $-11.60 | $1.49 |
| munich (highest) | $30.37 tot $65.00 | 466 | $-29.13 | $1.24 |
| nyc (highest) | $45.24 tot $95.23 | 834 | $-46.49 | $-1.26 |
| buenos-aires (highest) | $22.66 tot $44.52 | 276 | $-25.27 | $-2.61 |
| seoul (lowest) | $18.66 tot $34.91 | 102 | $-21.56 | $-2.90 |
| lucknow (highest) | $32.65 tot $67.53 | 299 | $-35.88 | $-3.23 |
| tel-aviv (highest) | $34.50 tot $74.50 | 294 | $-38.11 | $-3.61 |
| london (highest) | $33.71 tot $73.61 | 643 | $-37.97 | $-4.26 |
| moscow (highest) | $23.30 tot $46.37 | 212 | $-29.54 | $-6.24 |
| tokyo (lowest) | $13.02 tot $22.21 | 61 | $-20.35 | $-7.34 |
| guangzhou (highest) | $34.81 tot $70.97 | 472 | $-42.86 | $-8.04 |
| ankara (highest) | $24.15 tot $47.39 | 343 | $-35.53 | $-11.38 |
| qingdao (highest) | $19.82 tot $39.40 | 219 | $-34.21 | $-14.39 |
| amsterdam (highest) | $28.24 tot $62.19 | 530 | $-44.56 | $-16.32 |
| miami (highest) | $34.69 tot $73.07 | 458 | $-51.23 | $-16.54 |
| chicago (highest) | $39.30 tot $73.35 | 571 | $-56.79 | $-17.49 |
| hong-kong (lowest) | $8.22 tot $14.61 | 134 | $-27.75 | $-19.53 |
| hong-kong (highest) | $25.60 tot $54.01 | 606 | $-46.07 | $-20.48 |
| madrid (highest) | $30.11 tot $66.91 | 405 | $-50.67 | $-20.56 |
| san-francisco (highest) | $29.33 tot $57.31 | 356 | $-55.27 | $-25.94 |
| shanghai (highest) | $27.79 tot $60.86 | 427 | $-54.21 | $-26.42 |
| busan (highest) | $29.36 tot $62.96 | 296 | $-55.92 | $-26.56 |
| paris (highest) | $38.59 tot $83.82 | 648 | $-71.00 | $-32.40 |
| atlanta (highest) | $42.89 tot $90.67 | 820 | $-79.42 | $-36.53 |
| toronto (highest) | $23.97 tot $46.99 | 416 | $-63.73 | $-39.76 |
| dallas (highest) | $38.53 tot $80.88 | 513 | $-95.72 | $-57.19 |
| helsinki (highest) | $41.88 tot $86.51 | 567 | $-99.29 | $-57.41 |
| wellington (highest) | $27.77 tot $60.46 | 437 | $-86.71 | $-58.94 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
