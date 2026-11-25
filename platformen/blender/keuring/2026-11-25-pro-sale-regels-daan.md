# Keuring saleregels, salelink en controle Click Joints Pro (sale 27 nov), 25 nov 2026, Daan
Wat ik keurde: `platformen/blender/pro-sale-27nov.md` en `platformen/blender/sale-controle.sh` op 2945513. Script zelf gedraaid om ±11:10 NL.
**Akkoord: ja**, met één moet voor de hoofdchat (prijsstap Superhive, zie onder). Aan de teksten zelf hoeft niets.

## Deel A: klopt het?
| # | Bevinding | Feit of vermoeden | Zekerheid |
|---|---|---|---|
| 1 | Jouw punt 1: "applied at checkout" staat alleen in regel B, en B gaat alleen online als stap 2 van het script `"valid":true` ziet op de gewone pagina. Mijn moet 1 van 20 nov is netjes opgelost | feit | hoog |
| 2 | Jouw punt 2: "No code needed" hangt aan stap 3 ($7.80 op de pagina); geen $7.80, dan geen Superhive-regel. Goed | feit | hoog |
| 3 | Jouw punt 3: $19 x 0,75 = $14.25 en $12 x 0,65 = $7.80 kloppen. Data kloppen met besluiten regel 28 en met de kalender (vr 27 nov, di 1 dec, wo 2 dec). 23:59 CET klopt in december | feit, nagerekend | hoog |
| 4 | Script draait: stap 1 inactive, stap 2 null, stap 3 [12.0, 45.0], uitgang 1. Precies wat je beschrijft voor twee dagen voor de sale | feit, GEZIEN | hoog |
| 5 | **Botsing in de besluiten:** regel 27 zegt Superhive naar $19/$59 "op wo 2 dec", regel 28 zegt de Superhive-sale loopt t/m wo 2 dec. Gaat de prijs op 2 dec omhoog, dan is 35% van $19 = $12.35 en klopt "Personal is $7.80 instead of $12" die dag niet meer | feit | hoog |

## Deel B: regels
| # | Bevinding | Regel |
|---|---|---|
| 1 | Elk cijfer heeft GEZIEN, DERDEN (met link) of GOK; niets beloofd wat we niet zagen | in orde |
| 2 | Geen tekst onder de naam van Thijs naar buiten; het zijn winkelregels op onze eigen productpagina | in orde |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Regel A en B zeggen in één zin wat, hoeveel, tot wanneer en wat je betaalt. Precies goed | niets | |
| 2 | Superhive: "35% off on Superhive" staat op de Superhive-pagina zelf, "on Superhive" is dubbel | "Cyber Sale: 35% off, Friday November 27 to Wednesday December 2. No code needed. Personal is $7.80 instead of $12." Mag, hoeft niet | klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer | Waarom |
|---|---|---|
| Op het niveau van de beste? | 8 | Split 3D Print toont een doorgestreepte prijs bovenaan; wij een duidelijke regel plus de doorgestreepte prijs via de salelink |
| Zou ik kopen op basis hiervan? | 8 | Ik weet meteen wat ik betaal en tot wanneer |
| Zou Thijs er trots op zijn? | 8 | Eerlijk, niets beloofd wat we niet zagen |

## Moet (voor de hoofdchat, niet voor Bram)
- Zet de prijsstap van Superhive naar $19/$59 op **do 3 dec**, als de sale voorbij is (dat staat ook in regel 27: "tot de sale voorbij is"). Lukt dat niet: haal de Superhive-saleregel op wo 2 dec 's ochtends weg in plaats van do 3 dec. Ik meld dit in `berichten/hoofdchat.md`.

## Kan
- "on Superhive" weglaten (Deel C punt 2).

Klaar om te plakken bij de hoofdchat, met de controle op vr 27 nov ochtend.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
