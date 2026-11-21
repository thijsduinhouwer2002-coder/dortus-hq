# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.32 tot $1.77 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 11 runs, 3701 minuten (61.7 uur) (GEZIEN). Markten in de data: 1806. Uitslag bekend voor 869 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-235 (2416 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-217 (1420 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1386 | 216 | $4,101 | $10,171 | $337 tot $692 | 4730 / 3229 | $14,829 | $-515 (254 nog zonder prijs) | $0.00 (0 van 4730 beslist) | $-177 tot $178 |
| **Totaal** | 3701 | | $4,511 | $10,171 | $968 tot $2,002 | 11791 / 8297 | $37,850 | $-1,088 | $-452 | $-120 tot $914 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-865 over 11765 vullingen en $37,766, dus -2.29% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.95% over $36,821 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.80%.

**Opgeschaald (GOK):** per dag $-58.63 (ondergrens) tot $344 (hoge schatting) netto (gemeten minuten × 1440 / 3701).

382 van de 11791 vullingen ($1,029) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.95%): $-30.41 (GOK).

Geld dat de bot nodig had: gemiddeld $4,511 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$14,682**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-719 tot $4,213 |
| €5,000 | $5,000 | $-1,797 tot $10,531 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-452 over 3836 vullingen en $12,679, dus -3.57% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.21% per dollar over 11206 vullingen, 1 uur later -2.83% over 10845 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.00% per dollar over 559 vullingen, 1 uur later -5.20% over 541 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $36.61 (392 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $-26.80 (237 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1386 | 216 | $4,041 | $4,020 | $84.92 tot $226 | 949 / 599 | $3,439 | $-87.92 (46 nog zonder prijs) | $0.00 (0 van 949 beslist) | $-3.00 tot $138 |
| **Totaal** | 3701 | | $4,437 | $4,020 | $235 tot $613 | 2190 / 1429 | $7,957 | $-215 | $9.81 | $19.30 tot $398 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-225 over 2181 vullingen en $7,905, dus -2.85% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.79% over $7,718 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.67%.

**Opgeschaald (GOK):** per dag $4.92 (ondergrens) tot $152 (hoge schatting) netto (gemeten minuten × 1440 / 3701).

83 van de 2190 vullingen ($239) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.79%): $-6.66 (GOK).

Geld dat de bot nodig had: gemiddeld $4,437 in open orders plus de hoogste stand van $4,020 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,457**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $105 tot $3,238 |
| €5,000 | $5,000 | $262 tot $8,096 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $9.81 over 629 vullingen en $2,342, dus +0.42% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.94% per dollar over 2037 vullingen, 1 uur later -2.91% over 1958 (GEZIEN).
- Laagste temperatuur: 5 minuten later -1.42% per dollar over 144 vullingen, 1 uur later -0.43% over 140 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 897 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.48 tot $3.02 | $-0.66 tot $0.88 | 2 | $19.29 tot $34.62 | $-56.79 tot $-41.47 |
| €150 | 2 | $2.96 tot $6.05 | $-1.32 tot $1.77 | 3 | $28.15 tot $50.74 | $-83.04 tot $-60.45 |
| €200 | 3 | $4.44 tot $9.07 | $-1.98 tot $2.65 | 4 | $35.76 tot $66.19 | $-79.03 tot $-48.60 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.95%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 917 | $3.20 tot $6.58 | 51 | $-30.32 | $0.00 |
| highest wellington-on-november-23 18°C | 908 | $2.38 tot $4.87 | 43 | $-17.60 | $0.00 |
| highest san-francisco-on-november-22 54-55°F | 1929 | $2.66 tot $5.26 | 42 | $-15.41 | $0.00 |
| highest london-on-november-21 10°C or higher | 2264 | $4.90 tot $11.44 | 100 | $-16.40 | $0.00 |
| highest hong-kong-on-november-20 20°C | 311 | $0.81 tot $1.58 | 63 | $-11.98 | $0.00 |
| highest atlanta-on-november-22 61°F or below | 1141 | $1.25 tot $2.73 | 53 | $-12.32 | $0.00 |
| highest helsinki-on-november-23 2°C | 388 | $2.68 tot $4.53 | 16 | $-13.46 | $0.00 |
| highest madrid-on-november-22 15°C | 2226 | $3.11 tot $6.72 | 41 | $-13.30 | $0.00 |
| highest busan-on-november-22 8°C | 1830 | $3.65 tot $7.73 | 29 | $-13.42 | $0.00 |
| highest hong-kong-on-november-23 23°C | 581 | $0.72 tot $1.62 | 8 | $-9.95 | $0.00 |
| ... | | | | | |
| highest warsaw-on-november-22 5°C | 2238 | $3.79 tot $7.83 | 29 | $0.59 | $0.00 |
| highest buenos-aires-on-november-22 28°C | 1881 | $3.02 tot $4.99 | 17 | $2.02 | $0.00 |
| lowest miami-on-november-22 72-73°F | 1586 | $4.32 tot $7.51 | 8 | $1.42 | $0.00 |
| highest paris-on-november-22 8°C | 2322 | $3.46 tot $7.90 | 59 | $2.83 | $0.00 |
| highest warsaw-on-november-22 4°C | 2271 | $4.51 tot $9.55 | 43 | $2.34 | $0.00 |
| highest shenzhen-on-november-20 19°C | 321 | $1.44 tot $2.70 | 52 | $5.52 | $-13.57 |
| highest london-on-november-22 9°C | 2421 | $3.22 tot $7.11 | 44 | $5.80 | $0.00 |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $0.00 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $0.00 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| miami (lowest) | $23.05 tot $41.52 | 56 | $-4.13 | $18.92 |
| warsaw (highest) | $23.69 tot $50.45 | 234 | $-10.02 | $13.66 |
| austin (highest) | $28.98 tot $61.20 | 252 | $-15.49 | $13.49 |
| chengdu (highest) | $18.95 tot $42.60 | 168 | $-6.16 | $12.79 |
| seoul (highest) | $16.09 tot $35.48 | 208 | $-4.42 | $11.68 |
| los-angeles (highest) | $14.92 tot $34.24 | 314 | $-3.43 | $11.49 |
| milan (highest) | $22.31 tot $44.37 | 262 | $-12.43 | $9.87 |
| beijing (highest) | $15.39 tot $33.29 | 166 | $-6.22 | $9.17 |
| seoul (lowest) | $12.11 tot $22.60 | 54 | $-3.20 | $8.91 |
| paris (highest) | $21.72 tot $48.50 | 382 | $-12.93 | $8.80 |
| manila (highest) | $12.02 tot $23.89 | 93 | $-4.28 | $7.74 |
| kuala-lumpur (highest) | $16.06 tot $30.67 | 138 | $-9.16 | $6.90 |
| chongqing (highest) | $17.21 tot $36.46 | 143 | $-10.58 | $6.62 |
| houston (highest) | $29.26 tot $61.48 | 362 | $-22.96 | $6.30 |
| sao-paulo (highest) | $15.04 tot $29.98 | 186 | $-9.20 | $5.84 |
| tokyo (highest) | $14.59 tot $33.59 | 247 | $-8.84 | $5.75 |
| taipei (highest) | $16.65 tot $29.77 | 120 | $-11.09 | $5.56 |
| nyc (lowest) | $8.81 tot $14.94 | 46 | $-3.64 | $5.17 |
| shanghai (lowest) | $11.82 tot $21.69 | 41 | $-7.06 | $4.76 |
| jeddah (highest) | $13.76 tot $27.59 | 77 | $-9.58 | $4.17 |
| london (lowest) | $17.69 tot $33.08 | 109 | $-13.94 | $3.75 |
| london (highest) | $21.16 tot $48.18 | 444 | $-17.77 | $3.38 |
| mexico-city (highest) | $19.58 tot $38.29 | 125 | $-16.71 | $2.88 |
| buenos-aires (highest) | $15.81 tot $31.10 | 182 | $-12.95 | $2.86 |
| wuhan (highest) | $16.77 tot $37.04 | 145 | $-14.91 | $1.86 |
| karachi (highest) | $15.69 tot $30.26 | 101 | $-13.92 | $1.78 |
| munich (highest) | $19.79 tot $43.63 | 316 | $-19.34 | $0.45 |
| ankara (highest) | $16.26 tot $31.87 | 207 | $-15.96 | $0.30 |
| toronto (highest) | $14.93 tot $30.07 | 192 | $-14.85 | $0.08 |
| shenzhen (highest) | $14.05 tot $29.97 | 252 | $-14.01 | $0.04 |
| singapore (highest) | $16.39 tot $36.39 | 269 | $-16.81 | $-0.42 |
| lucknow (highest) | $22.91 tot $47.69 | 195 | $-25.28 | $-2.36 |
| amsterdam (highest) | $19.69 tot $43.32 | 364 | $-22.75 | $-3.07 |
| paris (lowest) | $18.95 tot $35.77 | 82 | $-22.19 | $-3.24 |
| moscow (highest) | $17.94 tot $35.53 | 164 | $-23.65 | $-5.71 |
| shanghai (highest) | $15.28 tot $34.94 | 243 | $-21.41 | $-6.13 |
| tokyo (lowest) | $11.23 tot $19.41 | 49 | $-17.38 | $-6.15 |
| dallas (highest) | $23.76 tot $50.43 | 307 | $-30.92 | $-7.16 |
| hong-kong (highest) | $16.00 tot $34.50 | 382 | $-27.13 | $-11.13 |
| chicago (highest) | $27.08 tot $51.63 | 408 | $-38.53 | $-11.45 |
| hong-kong (lowest) | $7.79 tot $13.98 | 123 | $-19.89 | $-12.10 |
| nyc (highest) | $29.03 tot $60.55 | 503 | $-41.15 | $-12.12 |
| tel-aviv (highest) | $22.43 tot $48.00 | 201 | $-34.91 | $-12.49 |
| guangzhou (highest) | $23.52 tot $47.69 | 359 | $-38.83 | $-15.31 |
| qingdao (highest) | $14.06 tot $27.87 | 122 | $-29.81 | $-15.75 |
| san-francisco (highest) | $21.62 tot $42.94 | 281 | $-38.24 | $-16.62 |
| miami (highest) | $24.30 tot $51.50 | 286 | $-41.01 | $-16.72 |
| madrid (highest) | $19.12 tot $43.49 | 294 | $-39.69 | $-20.58 |
| busan (highest) | $17.90 tot $39.27 | 222 | $-44.53 | $-26.63 |
| helsinki (highest) | $29.29 tot $60.67 | 384 | $-61.95 | $-32.66 |
| atlanta (highest) | $27.95 tot $60.08 | 648 | $-60.65 | $-32.71 |
| wellington (highest) | $17.36 tot $38.10 | 283 | $-62.13 | $-44.77 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
