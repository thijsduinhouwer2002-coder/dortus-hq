# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.84 tot $1.74 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 30 runs, 10075 minuten (167.9 uur) (GEZIEN). Markten in de data: 4519. Uitslag bekend voor 3346 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-243 (4847 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $46.47 (3263 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $53.52 (212 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 619 | 191 | $3,572 | $7,983 | $153 tot $329 | 2099 / 1340 | $7,308 | $-254 (207 nog zonder prijs) | $0.00 (0 van 2099 beslist) | $-100 tot $75.22 |
| **Totaal** | 10075 | | $3,768 | $10,171 | $2,576 tot $5,323 | 32751 / 23049 | $108,149 | $-3,065 | $-1,818 | $-489 tot $2,258 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-2,391 over 32695 vullingen en $107,984, dus -2.21% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.88% over $106,481 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.76%.

**Opgeschaald (GOK):** per dag $-76.78 (ondergrens) tot $316 (hoge schatting) netto (gemeten minuten × 1440 / 10075).

580 van de 32751 vullingen ($1,668) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.88%): $-48.01 (GOK).

Geld dat de bot nodig had: gemiddeld $3,768 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,939**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-991 tot $4,079 |
| €5,000 | $5,000 | $-2,479 tot $10,198 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-1,818 over 24603 vullingen en $79,877, dus -2.28% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.13% per dollar over 31222 vullingen, 1 uur later -2.79% over 30688 (GEZIEN).
- Laagste temperatuur: 5 minuten later -3.99% per dollar over 1473 vullingen, 1 uur later -4.59% over 1440 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $111 (1159 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $384 (710 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $-29.17 (52 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 619 | 191 | $3,538 | $4,193 | $36.43 tot $98.42 | 491 / 333 | $1,993 | $-63.53 (47 nog zonder prijs) | $0.00 (0 van 491 beslist) | $-27.11 tot $34.88 |
| **Totaal** | 10075 | | $3,712 | $4,193 | $628 tot $1,664 | 6901 / 4473 | $26,613 | $-600 | $177 | $28.22 tot $1,064 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-671 over 6885 vullingen en $26,547, dus -2.53% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.29% over $26,198 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.37%.

**Opgeschaald (GOK):** per dag $2.68 (ondergrens) tot $151 (hoge schatting) netto (gemeten minuten × 1440 / 10075).

130 van de 6901 vullingen ($415) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.29%): $-9.49 (GOK).

Geld dat de bot nodig had: gemiddeld $3,712 in open orders plus de hoogste stand van $4,193 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$7,905**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $60.95 tot $3,433 |
| €5,000 | $5,000 | $152 tot $8,583 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $177 over 4995 vullingen en $18,912, dus +0.93% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.50% per dollar over 6483 vullingen, 1 uur later -2.17% over 6364 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.96% per dollar over 402 vullingen, 1 uur later -4.09% over 396 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 1888 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.68 tot $3.46 | $-0.92 tot $0.87 | 2 | $55.91 tot $106 | $10.88 tot $61.44 |
| €150 | 2 | $3.35 tot $6.92 | $-1.84 tot $1.74 | 4 | $84.98 tot $165 | $35.26 tot $115 |
| €200 | 3 | $5.03 tot $10.39 | $-2.75 tot $2.60 | 5 | $99.00 tot $194 | $-82.30 tot $12.22 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.88%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest paris-on-november-26 6°C | 2083 | $8.96 tot $20.03 | 90 | $-34.19 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $-29.11 |
| highest paris-on-november-26 7°C | 1536 | $7.12 tot $16.89 | 84 | $-26.57 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest austin-on-november-27 68-69°F | 262 | $1.86 tot $3.50 | 26 | $-19.51 | $0.00 |
| highest taipei-on-november-24 21°C | 951 | $1.50 tot $3.00 | 33 | $-17.79 | $24.65 |
| highest atlanta-on-november-26 48-49°F | 1419 | $2.93 tot $5.80 | 49 | $-18.70 | $0.00 |
| ... | | | | | |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest nyc-on-november-27 62-63°F | 472 | $2.08 tot $3.78 | 5 | $8.21 | $0.00 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest nyc-on-november-26 58-59°F | 6461 | $14.00 tot $24.94 | 66 | $13.88 | $0.00 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $54.11 tot $110 | 454 | $89.75 | $144 |
| seoul (highest) | $71.08 tot $155 | 990 | $-22.25 | $48.83 |
| chengdu (highest) | $51.47 tot $113 | 541 | $-14.64 | $36.84 |
| miami (lowest) | $52.92 tot $92.22 | 143 | $-18.51 | $34.41 |
| london (lowest) | $44.61 tot $81.72 | 239 | $-12.47 | $32.14 |
| beijing (highest) | $40.42 tot $87.49 | 548 | $-11.25 | $29.18 |
| munich (highest) | $68.88 tot $151 | 921 | $-48.15 | $20.72 |
| paris (lowest) | $50.19 tot $92.75 | 192 | $-30.37 | $19.82 |
| chongqing (highest) | $50.50 tot $106 | 415 | $-33.75 | $16.75 |
| nyc (highest) | $75.55 tot $151 | 1039 | $-59.43 | $16.12 |
| wuhan (highest) | $49.52 tot $106 | 445 | $-33.97 | $15.55 |
| manila (highest) | $28.52 tot $57.80 | 281 | $-16.76 | $11.76 |
| tokyo (highest) | $56.69 tot $128 | 852 | $-45.15 | $11.54 |
| buenos-aires (highest) | $52.55 tot $112 | 611 | $-41.96 | $10.59 |
| shanghai (lowest) | $15.89 tot $29.96 | 71 | $-7.88 | $8.01 |
| karachi (highest) | $33.92 tot $67.44 | 261 | $-25.98 | $7.94 |
| singapore (highest) | $47.03 tot $102 | 614 | $-39.57 | $7.46 |
| jeddah (highest) | $26.52 tot $53.35 | 205 | $-19.20 | $7.31 |
| shenzhen (highest) | $36.56 tot $77.92 | 626 | $-31.60 | $4.96 |
| sao-paulo (highest) | $37.55 tot $74.73 | 433 | $-35.39 | $2.16 |
| kuala-lumpur (highest) | $32.99 tot $64.12 | 366 | $-31.25 | $1.74 |
| london (highest) | $60.71 tot $131 | 1177 | $-61.08 | $-0.37 |
| nyc (lowest) | $21.52 tot $37.51 | 181 | $-22.03 | $-0.51 |
| mexico-city (highest) | $41.78 tot $81.32 | 347 | $-42.61 | $-0.83 |
| milan (highest) | $54.40 tot $111 | 745 | $-58.26 | $-3.86 |
| seoul (lowest) | $31.30 tot $58.98 | 183 | $-36.39 | $-5.10 |
| tokyo (lowest) | $17.09 tot $30.34 | 69 | $-23.75 | $-6.66 |
| los-angeles (highest) | $54.02 tot $118 | 933 | $-62.49 | $-8.47 |
| qingdao (highest) | $28.97 tot $57.87 | 354 | $-38.01 | $-9.04 |
| taipei (highest) | $37.43 tot $70.39 | 397 | $-46.60 | $-9.17 |
| moscow (highest) | $34.38 tot $69.03 | 417 | $-44.47 | $-10.09 |
| ankara (highest) | $37.43 tot $73.15 | 555 | $-47.96 | $-10.53 |
| shanghai (highest) | $50.49 tot $109 | 966 | $-68.63 | $-18.14 |
| guangzhou (highest) | $54.17 tot $113 | 742 | $-73.99 | $-19.82 |
| miami (highest) | $62.84 tot $132 | 918 | $-82.73 | $-19.89 |
| chicago (highest) | $55.08 tot $104 | 866 | $-75.12 | $-20.04 |
| lucknow (highest) | $57.96 tot $119 | 623 | $-81.21 | $-23.25 |
| austin (highest) | $66.28 tot $137 | 818 | $-90.13 | $-23.85 |
| tel-aviv (highest) | $64.36 tot $137 | 528 | $-92.94 | $-28.59 |
| amsterdam (highest) | $52.21 tot $112 | 882 | $-81.12 | $-28.91 |
| houston (highest) | $76.26 tot $156 | 1128 | $-106 | $-29.86 |
| madrid (highest) | $56.36 tot $121 | 812 | $-87.83 | $-31.47 |
| hong-kong (lowest) | $37.24 tot $78.11 | 396 | $-78.20 | $-40.96 |
| san-francisco (highest) | $42.91 tot $83.57 | 633 | $-87.62 | $-44.71 |
| busan (highest) | $77.82 tot $166 | 814 | $-130 | $-52.65 |
| helsinki (highest) | $75.85 tot $154 | 1047 | $-134 | $-57.79 |
| hong-kong (highest) | $42.05 tot $89.56 | 1076 | $-102 | $-59.63 |
| dallas (highest) | $63.60 tot $134 | 924 | $-129 | $-65.28 |
| toronto (highest) | $32.21 tot $64.63 | 595 | $-107 | $-74.86 |
| wellington (highest) | $47.80 tot $104 | 731 | $-130 | $-82.00 |
| atlanta (highest) | $65.53 tot $138 | 1237 | $-150 | $-84.20 |
| paris (highest) | $98.60 tot $219 | 1410 | $-205 | $-106 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
