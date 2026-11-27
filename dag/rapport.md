# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.63 tot $1.88 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 34 runs, 11419 minuten (190.3 uur) (GEZIEN). Markten in de data: 5040. Uitslag bekend voor 3865 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-243 (4847 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $-272 (4296 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $-848 (3701 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 1435 | 205 | $3,842 | $9,065 | $377 tot $805 | 5217 / 3336 | $19,178 | $-654 (32 nog zonder prijs) | $-6.65 (212 van 5217 beslist) | $-277 tot $151 |
| 2026-11-27 | 528 | 200 | $3,693 | $8,713 | $131 tot $279 | 1753 / 1121 | $6,464 | $-196 (234 nog zonder prijs) | $0.00 (0 van 1753 beslist) | $-65.61 tot $82.72 |
| **Totaal** | 11419 | | $3,785 | $10,171 | $2,931 tot $6,079 | 37622 / 26166 | $126,484 | $-3,663 | $-3,044 | $-731 tot $2,416 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-2,901 over 37553 vullingen en $126,265, dus -2.30% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.94% over $124,704 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.85%.

**Opgeschaald (GOK):** per dag $-98.83 (ondergrens) tot $298 (hoge schatting) netto (gemeten minuten × 1440 / 11419).

639 van de 37622 vullingen ($1,779) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.94%): $-52.25 (GOK).

Geld dat de bot nodig had: gemiddeld $3,785 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,956**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,275 tot $3,845 |
| €5,000 | $5,000 | $-3,187 tot $9,613 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-3,044 over 29337 vullingen en $96,149, dus -3.17% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.20% per dollar over 35692 vullingen, 1 uur later -2.85% over 35122 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.00% per dollar over 1861 vullingen, 1 uur later -4.45% over 1809 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $111 (1159 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $378 (994 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $-455 (804 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 1435 | 205 | $3,808 | $4,844 | $92.00 tot $246 | 1183 / 787 | $4,920 | $-147 (6 nog zonder prijs) | $17.59 (55 van 1183 beslist) | $-54.54 tot $99.60 |
| 2026-11-27 | 528 | 200 | $3,702 | $4,677 | $30.64 tot $83.12 | 382 / 279 | $1,549 | $-37.40 (51 nog zonder prijs) | $0.00 (0 van 382 beslist) | $-6.76 tot $45.72 |
| **Totaal** | 11419 | | $3,733 | $4,844 | $714 tot $1,895 | 7975 / 5206 | $31,089 | $-720 | $-237 | $-5.97 tot $1,175 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-851 over 7955 vullingen en $31,001, dus -2.75% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.34% over $30,718 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.47%.

**Opgeschaald (GOK):** per dag $-1.85 (ondergrens) tot $147 (hoge schatting) netto (gemeten minuten × 1440 / 11419).

140 van de 7975 vullingen ($371) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.34%): $-8.70 (GOK).

Geld dat de bot nodig had: gemiddeld $3,733 in open orders plus de hoogste stand van $4,844 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,577**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-38.81 tot $3,086 |
| €5,000 | $5,000 | $-97.04 tot $7,715 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-237 over 6086 vullingen en $23,402, dus -1.01% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.74% per dollar over 7443 vullingen, 1 uur later -2.26% over 7322 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.80% per dollar over 512 vullingen, 1 uur later -3.39% over 498 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 2120 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.63 tot $3.39 | $-0.82 tot $0.94 | 2 | $43.72 tot $83.86 | $-27.56 tot $12.58 |
| €150 | 2 | $3.27 tot $6.78 | $-1.63 tot $1.88 | 3 | $56.93 tot $112 | $-40.58 tot $14.65 |
| €200 | 3 | $4.90 tot $10.18 | $-2.45 tot $2.83 | 4 | $70.44 tot $138 | $-43.15 tot $24.60 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.94%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest paris-on-november-26 6°C | 2083 | $8.96 tot $20.03 | 90 | $-34.19 | $-52.26 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $-29.11 |
| highest paris-on-november-26 7°C | 1536 | $7.12 tot $16.89 | 84 | $-26.57 | $5.42 |
| highest nyc-on-november-27 60-61°F | 3053 | $9.72 tot $18.90 | 44 | $-28.44 | $0.00 |
| highest austin-on-november-27 68-69°F | 1432 | $3.90 tot $7.88 | 72 | $-22.09 | $0.00 |
| highest paris-on-november-23 7°C | 2345 | $4.20 tot $9.02 | 69 | $-21.89 | $-93.47 |
| highest madrid-on-november-27 14°C or higher | 2080 | $2.80 tot $5.46 | 66 | $-19.43 | $0.00 |
| ... | | | | | |
| highest hong-kong-on-november-20 18°C | 291 | $0.22 tot $0.54 | 39 | $9.97 | $-5.92 |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest nyc-on-november-28 54-55°F | 1633 | $5.31 tot $9.56 | 9 | $10.45 | $0.00 |
| highest nyc-on-november-26 58-59°F | 6461 | $14.00 tot $24.94 | 66 | $13.88 | $7.47 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $65.84 tot $131 | 513 | $64.80 | $131 |
| seoul (highest) | $77.91 tot $173 | 1139 | $-33.90 | $44.01 |
| chengdu (highest) | $58.05 tot $127 | 628 | $-20.57 | $37.48 |
| miami (lowest) | $54.79 tot $95.59 | 151 | $-20.25 | $34.54 |
| paris (lowest) | $57.19 tot $106 | 243 | $-29.28 | $27.91 |
| london (lowest) | $52.50 tot $95.81 | 310 | $-28.54 | $23.96 |
| munich (highest) | $75.67 tot $168 | 1046 | $-55.60 | $20.08 |
| wuhan (highest) | $55.63 tot $119 | 537 | $-43.67 | $11.95 |
| shanghai (lowest) | $20.42 tot $38.96 | 84 | $-9.31 | $11.12 |
| singapore (highest) | $52.67 tot $114 | 711 | $-42.54 | $10.14 |
| beijing (highest) | $45.56 tot $99.38 | 675 | $-37.33 | $8.23 |
| manila (highest) | $30.84 tot $62.81 | 309 | $-22.79 | $8.05 |
| shenzhen (highest) | $42.52 tot $90.39 | 693 | $-36.63 | $5.90 |
| karachi (highest) | $37.62 tot $74.88 | 316 | $-32.03 | $5.59 |
| sao-paulo (highest) | $40.58 tot $80.94 | 477 | $-36.03 | $4.56 |
| jeddah (highest) | $29.50 tot $59.68 | 221 | $-25.00 | $4.50 |
| nyc (highest) | $88.51 tot $176 | 1088 | $-84.48 | $4.03 |
| tokyo (highest) | $69.48 tot $159 | 1061 | $-66.18 | $3.30 |
| buenos-aires (highest) | $65.43 tot $143 | 743 | $-63.03 | $2.40 |
| kuala-lumpur (highest) | $36.40 tot $71.16 | 423 | $-34.06 | $2.35 |
| chongqing (highest) | $56.66 tot $119 | 510 | $-57.13 | $-0.48 |
| seoul (lowest) | $35.64 tot $67.77 | 214 | $-38.42 | $-2.78 |
| london (highest) | $69.91 tot $152 | 1450 | $-73.09 | $-3.19 |
| nyc (lowest) | $30.20 tot $52.39 | 212 | $-33.59 | $-3.39 |
| taipei (highest) | $42.85 tot $80.06 | 456 | $-46.74 | $-3.90 |
| milan (highest) | $61.96 tot $127 | 839 | $-66.74 | $-4.77 |
| los-angeles (highest) | $61.70 tot $134 | 1033 | $-67.10 | $-5.40 |
| mexico-city (highest) | $47.95 tot $93.11 | 435 | $-54.56 | $-6.62 |
| qingdao (highest) | $32.34 tot $64.74 | 431 | $-40.74 | $-8.40 |
| tokyo (lowest) | $21.53 tot $38.92 | 123 | $-32.46 | $-10.93 |
| ankara (highest) | $41.49 tot $81.19 | 601 | $-56.19 | $-14.70 |
| chicago (highest) | $60.89 tot $116 | 975 | $-80.35 | $-19.47 |
| miami (highest) | $69.66 tot $147 | 1043 | $-89.77 | $-20.11 |
| houston (highest) | $84.01 tot $173 | 1221 | $-110 | $-25.61 |
| moscow (highest) | $40.12 tot $80.40 | 497 | $-66.18 | $-26.07 |
| shanghai (highest) | $56.44 tot $122 | 1054 | $-82.73 | $-26.29 |
| austin (highest) | $75.62 tot $157 | 968 | $-103 | $-27.39 |
| tel-aviv (highest) | $71.01 tot $151 | 619 | $-102 | $-30.65 |
| madrid (highest) | $61.36 tot $133 | 917 | $-95.29 | $-33.93 |
| amsterdam (highest) | $59.54 tot $128 | 990 | $-95.40 | $-35.86 |
| lucknow (highest) | $65.37 tot $135 | 715 | $-107 | $-41.78 |
| hong-kong (lowest) | $52.96 tot $113 | 529 | $-95.38 | $-42.42 |
| guangzhou (highest) | $58.68 tot $123 | 831 | $-105 | $-46.23 |
| san-francisco (highest) | $46.99 tot $91.55 | 683 | $-94.40 | $-47.41 |
| busan (highest) | $86.04 tot $185 | 896 | $-142 | $-55.84 |
| hong-kong (highest) | $45.46 tot $97.11 | 1149 | $-105 | $-59.49 |
| helsinki (highest) | $88.58 tot $180 | 1165 | $-151 | $-61.94 |
| toronto (highest) | $36.27 tot $73.21 | 643 | $-110 | $-73.58 |
| dallas (highest) | $73.72 tot $156 | 1097 | $-159 | $-85.56 |
| wellington (highest) | $54.95 tot $120 | 877 | $-141 | $-86.39 |
| atlanta (highest) | $73.88 tot $156 | 1410 | $-171 | $-97.45 |
| paris (highest) | $110 tot $248 | 1671 | $-234 | $-124 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
