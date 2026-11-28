# Schaduwbot Polymarket: rapport

Denkbeeldige makerbot in jonge temperatuurmarkten. Geen account, geen geld, niets geplaatst. Beloning = GOK (formule van Polymarket; voor de concurrentie een ondergrens en een hoge schatting). Vullingen en verlies = GEZIEN (echte trades en gemeten midden), behalve waar GOK staat.

**Met €150: netto $-1.29 tot $2.20 per dag (GOK)**, in 2 gemiddelde markten tegelijk (variant 1c, ondergrens tot hoge schatting van de beloning, min het verlies op vullingen).

Gemeten: 38 runs, 12761 minuten (212.7 uur) (GEZIEN). Markten in de data: 5529. Uitslag bekend voor 4395 markten.

## Variant 1c (orders op 1 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,642 | $4,694 | $220 tot $466 | 2987 / 2103 | $9,892 | $-203 (14 nog zonder prijs) | $-543 (2987 van 2987 beslist) | $16.92 tot $262 |
| 2026-11-20 | 1420 | 254 | $4,828 | $9,026 | $410 tot $843 | 4074 / 2965 | $13,129 | $-370 (114 nog zonder prijs) | $-325 (4074 van 4074 beslist) | $40.19 tot $473 |
| 2026-11-21 | 1410 | 216 | $4,096 | $10,171 | $343 tot $704 | 4798 / 3271 | $15,012 | $-538 (97 nog zonder prijs) | $-427 (4798 van 4798 beslist) | $-195 tot $166 |
| 2026-11-22 | 1432 | 191 | $3,616 | $9,582 | $352 tot $709 | 4422 / 3346 | $14,301 | $-490 (36 nog zonder prijs) | $-380 (4422 van 4422 beslist) | $-138 tot $220 |
| 2026-11-23 | 1432 | 168 | $3,195 | $8,779 | $329 tot $661 | 4847 / 3681 | $15,405 | $-400 (38 nog zonder prijs) | $-243 (4847 van 4847 beslist) | $-71.36 tot $261 |
| 2026-11-24 | 1434 | 162 | $3,042 | $7,728 | $301 tot $621 | 4307 / 3017 | $14,667 | $-298 (35 nog zonder prijs) | $-255 (4307 van 4307 beslist) | $3.18 tot $324 |
| 2026-11-25 | 1433 | 181 | $3,388 | $8,264 | $468 tot $990 | 5217 / 3326 | $18,436 | $-513 (39 nog zonder prijs) | $-1,115 (5153 van 5217 beslist) | $-45.16 tot $476 |
| 2026-11-26 | 1435 | 205 | $3,842 | $9,065 | $377 tot $805 | 5217 / 3336 | $19,178 | $-654 (32 nog zonder prijs) | $-616 (3004 van 5217 beslist) | $-277 tot $151 |
| 2026-11-27 | 1433 | 209 | $3,926 | $10,055 | $394 tot $831 | 4933 / 3176 | $18,346 | $-571 (41 nog zonder prijs) | $11.04 (212 van 4933 beslist) | $-177 tot $259 |
| 2026-11-28 | 437 | 183 | $3,456 | $9,760 | $103 tot $217 | 1220 / 765 | $4,656 | $-72.45 (125 nog zonder prijs) | $0.00 (0 van 1220 beslist) | $30.46 tot $145 |
| **Totaal** | 12761 | | $3,793 | $10,171 | $3,297 tot $6,848 | 42022 / 28986 | $143,022 | $-4,110 | $-3,892 | $-813 tot $2,738 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-3,346 over 41951 vullingen en $142,798, dus -2.34% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.90% over $141,559 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.88%.

**Opgeschaald (GOK):** per dag $-96.48 (ondergrens) tot $304 (hoge schatting) netto (gemeten minuten × 1440 / 12761).

571 van de 42022 vullingen ($1,463) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.90%): $-42.46 (GOK).

Geld dat de bot nodig had: gemiddeld $3,793 in open orders plus de hoogste stand van $10,171 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$13,964**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $-1,244 tot $3,920 |
| €5,000 | $5,000 | $-3,109 tot $9,801 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-3,892 over 33804 vullingen en $112,149, dus -3.47% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.25% per dollar over 39750 vullingen, 1 uur later -2.82% over 39231 (GEZIEN).
- Laagste temperatuur: 5 minuten later -4.02% per dollar over 2201 vullingen, 1 uur later -4.33% over 2158 (GEZIEN).

## Variant 3c (orders op 3 cent van het midden)

| Dag (UTC) | Minuten gemeten | Markten gem. | Orders op het boek gem. | Hoogste stand voorraadgeld | Beloning ondergrens tot hoge schatting (GOK) | Vullingen los / streng | Gevuld | Resultaat vullingen 1 uur later | Tegen uitslag | Netto (ondergrens tot hoge schatting, alleen vullingen met prijs 1 uur later) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 | 895 | 245 | $4,576 | $1,364 | $51.06 tot $127 | 490 / 352 | $1,800 | $-52.50 (6 nog zonder prijs) | $-84.53 (490 van 490 beslist) | $-1.45 tot $74.53 |
| 2026-11-20 | 1420 | 254 | $4,737 | $3,186 | $98.64 tot $260 | 751 / 478 | $2,718 | $-74.90 (31 nog zonder prijs) | $145 (751 van 751 beslist) | $23.74 tot $185 |
| 2026-11-21 | 1410 | 216 | $4,034 | $4,020 | $86.17 tot $230 | 966 / 606 | $3,482 | $-94.48 (14 nog zonder prijs) | $-66.21 (966 van 966 beslist) | $-8.31 tot $135 |
| 2026-11-22 | 1432 | 191 | $3,551 | $3,943 | $88.97 tot $234 | 867 / 549 | $3,240 | $-71.94 (11 nog zonder prijs) | $-284 (867 van 867 beslist) | $17.03 tot $162 |
| 2026-11-23 | 1432 | 168 | $3,136 | $3,949 | $83.83 tot $220 | 1159 / 776 | $4,375 | $-98.61 (6 nog zonder prijs) | $111 (1159 van 1159 beslist) | $-14.78 tot $122 |
| 2026-11-24 | 1434 | 162 | $3,013 | $3,774 | $73.70 tot $200 | 994 / 591 | $4,078 | $-43.91 (8 nog zonder prijs) | $378 (994 van 994 beslist) | $29.78 tot $156 |
| 2026-11-25 | 1433 | 181 | $3,353 | $4,190 | $109 tot $295 | 1183 / 788 | $4,927 | $-99.80 (7 nog zonder prijs) | $-605 (1167 van 1183 beslist) | $9.30 tot $195 |
| 2026-11-26 | 1435 | 205 | $3,808 | $4,844 | $92.00 tot $246 | 1183 / 787 | $4,920 | $-147 (6 nog zonder prijs) | $6.33 (584 van 1183 beslist) | $-54.54 tot $99.60 |
| 2026-11-27 | 1433 | 209 | $3,897 | $5,156 | $99.95 tot $264 | 1113 / 755 | $4,501 | $-117 (5 nog zonder prijs) | $-29.62 (44 van 1113 beslist) | $-17.44 tot $146 |
| 2026-11-28 | 437 | 183 | $3,413 | $4,642 | $26.14 tot $68.21 | 259 / 159 | $1,063 | $3.58 (22 nog zonder prijs) | $0.00 (0 van 259 beslist) | $29.73 tot $71.79 |
| **Totaal** | 12761 | | $3,742 | $5,156 | $810 tot $2,144 | 8965 / 5841 | $35,104 | $-796 | $-429 | $13.08 tot $1,347 |

Resultaat vullingen 5 minuten later (vroege aanwijzing, GEZIEN): $-953 over 8942 vullingen en $35,015, dus -2.72% per gevulde dollar.

Verlies per gevulde dollar, 1 uur later: -2.29% over $34,813 (GEZIEN; B mat −1,05% voor alle makers binnen 1 cent, D −0,1 tot −0,3% voor alle makers in temperatuurmarkten). Alleen strenge vullingen: -3.54%.

**Opgeschaald (GOK):** per dag $0.72 (ondergrens) tot $151 (hoge schatting) netto (gemeten minuten × 1440 / 12761).

116 van de 8965 vullingen ($291) hebben nog geen prijs 1 uur later. Die tellen niet als 0: hun verlies is geschat met het verlies per dollar van de andere vullingen (1 uur later, -2.29%): $-6.66 (GOK).

Geld dat de bot nodig had: gemiddeld $3,742 in open orders plus de hoogste stand van $5,156 vastzittend in gevulde voorraad tot de uitslag (JA en NEE per markt tegen elkaar weggestreept; vrij ±30 uur na het begin van de dag, GOK) = **$8,898**. De voorraad groeit tot de eerste markten beslist zijn (2 tot 3 dagen na de start), dus tot dan is dit getal te laag.

| Inleg | Te gebruiken (× 1.0 $/€, hooguit orders plus voorraad) | Netto over 90 dagen (GOK) |
|---|---|---|
| €2,000 | $2,000 | $14.64 tot $3,060 |
| €5,000 | $5,000 | $36.61 tot $7,650 |

Opschalen gaat lineair met het geld dat de bot nodig had (orders plus voorraad), en nooit daarboven: meer geld in dezelfde markten geeft geen evenredig grotere beloning (je deelt de pot). Kansspelbelasting (37,8%, mogelijk) en het verbod in Nederland staan hier niet in; zie README.

Tegen de uitslag (de bot houdt zijn voorraad tot de uitslag): $-429 over 7022 vullingen en $27,121, dus -1.58% per gevulde dollar (GEZIEN).

- Hoogste temperatuur: 5 minuten later -2.73% per dollar over 8323 vullingen, 1 uur later -2.21% over 8220 (GEZIEN).
- Laagste temperatuur: 5 minuten later -2.62% per dollar over 619 vullingen, 1 uur later -3.26% over 609 (GEZIEN).

## Met weinig geld: €100, €150 en €200 (variant 1c, GOK)

Een kleine inleg staat maar in een paar markten tegelijk. Per markt is nodig: de orders zelf (minimale grootte van die markt, vaak 20 aandelen, soms 100, afgerond op de tick van de markt, zoals gemeten) plus ruimte voor voorraad tot de rem (2 keer de ordergrootte aan de duurste kant). Markten die meer vragen dan de hele inleg vallen af. Gerekend over 2309 markten met minstens 60 gemeten minuten.

| Inleg | Gemiddelde markten: aantal | Beloning per dag | Netto per dag | Achteraf beste markten: aantal | Beloning per dag | Netto per dag |
|---|---|---|---|---|---|---|
| €100 | 1 | $1.63 tot $3.37 | $-0.64 tot $1.10 | 2 | $37.53 tot $74.40 | $-20.63 tot $16.24 |
| €150 | 2 | $3.25 tot $6.74 | $-1.29 tot $2.20 | 3 | $51.54 tot $105 | $-48.87 tot $4.17 |
| €200 | 3 | $4.88 tot $10.11 | $-1.93 tot $3.30 | 4 | $65.05 tot $131 | $-51.44 tot $14.12 |

Lees zo: per dag = gemeten opbrengst per markt-minuut × 1440 × aantal markten (GOK). "Achteraf beste" kiest de markten die in deze data het meest opleverden per dollar; dat is te mooi, want vooraf weet je niet welke dat zijn. Netto = beloning min het verlies op vullingen 1 uur later; vullingen zonder prijs 1 uur later zijn geschat met het verlies per dollar van de rest (-2.90%). Polymarket betaalt pas uit vanaf $1 beloning per dag (docs Liquidity Rewards); daaronder krijg je niets, maar het verlies op vullingen blijft. Geen belasting of verbod in Nederland meegerekend.

## Per markt (variant 1c)

Slechtste 10 en beste 10 op netto (beloning ondergrens plus resultaat 1 uur later).

| Markt | Minuten | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Tegen uitslag |
|---|---|---|---|---|---|
| highest warsaw-on-november-28 -1°C | 3598 | $11.88 tot $22.23 | 73 | $-53.91 | $0.00 |
| highest wellington-on-november-23 19°C | 1574 | $4.66 tot $9.54 | 70 | $-35.02 | $-59.48 |
| highest dallas-on-november-22 68-69°F | 2374 | $3.83 tot $7.62 | 52 | $-31.50 | $-104 |
| highest seoul-on-november-28 11°C | 1947 | $3.71 tot $8.77 | 98 | $-29.95 | $0.00 |
| highest paris-on-november-26 6°C | 2083 | $8.96 tot $20.03 | 90 | $-34.19 | $-52.26 |
| highest helsinki-on-november-28 1°C or higher | 1641 | $5.50 tot $10.67 | 64 | $-28.13 | $0.00 |
| highest dallas-on-november-22 64-65°F | 2463 | $2.93 tot $6.04 | 36 | $-24.15 | $-54.33 |
| highest nyc-on-november-25 48-49°F | 3278 | $9.66 tot $17.36 | 62 | $-29.88 | $-29.11 |
| highest paris-on-november-26 7°C | 1536 | $7.12 tot $16.89 | 84 | $-26.57 | $5.42 |
| highest nyc-on-november-27 60-61°F | 3053 | $9.72 tot $18.90 | 44 | $-28.44 | $-21.79 |
| ... | | | | | |
| highest london-on-november-22 9°C | 2445 | $3.23 tot $7.12 | 45 | $7.23 | $18.39 |
| highest milan-on-november-21 16°C | 2085 | $6.23 tot $9.85 | 31 | $4.59 | $15.46 |
| highest nyc-on-november-28 52-53°F | 4360 | $10.69 tot $20.85 | 42 | $0.65 | $0.00 |
| highest shanghai-on-november-24 13°C | 1688 | $4.18 tot $8.74 | 69 | $7.87 | $3.57 |
| highest helsinki-on-november-20 5°C | 740 | $1.97 tot $3.93 | 35 | $10.10 | $-2.39 |
| highest warsaw-on-november-29 2°C or higher | 459 | $1.59 tot $3.35 | 6 | $10.67 | $0.00 |
| highest seoul-on-november-24 6°C | 1617 | $3.16 tot $6.36 | 96 | $10.08 | $6.78 |
| highest helsinki-on-november-25 0°C | 1679 | $5.71 tot $10.92 | 69 | $8.72 | $37.98 |
| highest nyc-on-november-26 58-59°F | 6461 | $14.00 tot $24.94 | 66 | $13.88 | $7.47 |
| highest warsaw-on-november-25 5°C | 4353 | $5.15 tot $10.21 | 43 | $115 | $-22.38 |

## Per stad (variant 1c)

| Stad | Beloning ondergrens tot hoge schatting (GOK) | Vullingen | 1 uur later | Netto ondergrens |
|---|---|---|---|---|
| warsaw (highest) | $73.73 tot $146 | 552 | $35.02 | $109 |
| chengdu (highest) | $63.80 tot $140 | 680 | $-19.40 | $44.40 |
| miami (lowest) | $59.20 tot $103 | 162 | $-23.78 | $35.42 |
| london (lowest) | $60.33 tot $110 | 374 | $-29.68 | $30.65 |
| paris (lowest) | $65.75 tot $121 | 275 | $-37.58 | $28.18 |
| munich (highest) | $83.78 tot $188 | 1167 | $-61.27 | $22.51 |
| shanghai (lowest) | $27.53 tot $51.33 | 116 | $-10.95 | $16.58 |
| beijing (highest) | $48.82 tot $107 | 737 | $-37.28 | $11.54 |
| singapore (highest) | $60.52 tot $131 | 803 | $-49.84 | $10.68 |
| jeddah (highest) | $33.61 tot $67.82 | 241 | $-24.66 | $8.96 |
| seoul (highest) | $86.33 tot $193 | 1366 | $-78.78 | $7.55 |
| nyc (highest) | $97.27 tot $193 | 1147 | $-90.73 | $6.54 |
| kuala-lumpur (highest) | $39.45 tot $77.40 | 462 | $-33.05 | $6.41 |
| manila (highest) | $34.13 tot $69.80 | 364 | $-28.80 | $5.33 |
| karachi (highest) | $43.13 tot $84.60 | 379 | $-38.84 | $4.28 |
| london (highest) | $75.55 tot $165 | 1584 | $-72.73 | $2.82 |
| milan (highest) | $71.16 tot $144 | 920 | $-69.20 | $1.96 |
| sao-paulo (highest) | $44.65 tot $89.11 | 534 | $-43.23 | $1.43 |
| shenzhen (highest) | $47.71 tot $101 | 761 | $-47.22 | $0.49 |
| wuhan (highest) | $64.38 tot $136 | 663 | $-64.08 | $0.29 |
| seoul (lowest) | $39.83 tot $76.15 | 228 | $-39.81 | $0.02 |
| tokyo (highest) | $78.91 tot $182 | 1208 | $-79.12 | $-0.21 |
| los-angeles (highest) | $70.93 tot $154 | 1115 | $-73.21 | $-2.28 |
| chongqing (highest) | $61.41 tot $130 | 555 | $-66.29 | $-4.88 |
| buenos-aires (highest) | $82.49 tot $182 | 888 | $-88.71 | $-6.21 |
| nyc (lowest) | $40.33 tot $70.64 | 275 | $-46.88 | $-6.55 |
| mexico-city (highest) | $55.82 tot $108 | 510 | $-64.01 | $-8.19 |
| taipei (highest) | $46.61 tot $87.74 | 513 | $-55.07 | $-8.45 |
| ankara (highest) | $45.60 tot $89.67 | 649 | $-60.13 | $-14.53 |
| chicago (highest) | $66.18 tot $125 | 1056 | $-80.81 | $-14.64 |
| qingdao (highest) | $35.39 tot $71.08 | 478 | $-50.50 | $-15.11 |
| tokyo (lowest) | $26.24 tot $47.81 | 144 | $-43.00 | $-16.76 |
| miami (highest) | $77.52 tot $164 | 1196 | $-97.90 | $-20.38 |
| houston (highest) | $93.32 tot $192 | 1352 | $-119 | $-25.65 |
| moscow (highest) | $43.63 tot $87.67 | 551 | $-69.78 | $-26.15 |
| austin (highest) | $83.21 tot $173 | 1072 | $-112 | $-28.94 |
| hong-kong (lowest) | $73.25 tot $156 | 631 | $-103 | $-29.43 |
| tel-aviv (highest) | $79.00 tot $168 | 720 | $-109 | $-30.00 |
| shanghai (highest) | $61.50 tot $133 | 1169 | $-91.93 | $-30.43 |
| amsterdam (highest) | $67.77 tot $145 | 1102 | $-104 | $-36.66 |
| san-francisco (highest) | $52.34 tot $102 | 769 | $-94.59 | $-42.25 |
| lucknow (highest) | $73.08 tot $151 | 800 | $-117 | $-43.92 |
| busan (highest) | $99.77 tot $215 | 1027 | $-149 | $-49.64 |
| madrid (highest) | $68.39 tot $148 | 1023 | $-121 | $-52.59 |
| guangzhou (highest) | $63.63 tot $134 | 925 | $-117 | $-53.85 |
| hong-kong (highest) | $49.75 tot $107 | 1236 | $-112 | $-61.93 |
| toronto (highest) | $40.70 tot $82.29 | 712 | $-117 | $-76.58 |
| wellington (highest) | $59.91 tot $131 | 961 | $-139 | $-78.92 |
| dallas (highest) | $83.35 tot $177 | 1218 | $-164 | $-80.36 |
| helsinki (highest) | $95.85 tot $195 | 1286 | $-181 | $-85.52 |
| atlanta (highest) | $81.25 tot $172 | 1549 | $-181 | $-99.88 |
| paris (highest) | $120 tot $272 | 1817 | $-236 | $-116 |

Grenzen: de beloning is een schatting (het echte aangepaste midden en de scores per maker zijn niet openbaar); een vulling telt 'los' als een trade op of door onze prijs gaat en 'streng' als hij erdoorheen gaat (de wachtrij is onbekend); trades staan 1 tot 2 minuten later in de Data API, dus de voorraadrem reageert iets te laat. Dit is meten, geen advies.
