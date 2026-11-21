# Keuring Afkijken 2 A (Blender-kopers), 21 nov 2026, keurder namens Daan
Wat ik keurde: `platformen/ideeen/afkijken-2-2026-11-21/A-blender-kopers.md` (149 regels, stand 21 nov ±14:00 NL)
Akkoord: nee

De cijfers kloppen. Het nee komt alleen door twee regels in de doe-lijst over wie iets doet; beide zijn met één zin te herstellen.

## Deel A: doet het wat beloofd is?
Opdracht: hoe kwamen kleine Blender-makers aan hun eerste 10, 100 en 1000 kopers, met een doe-lijst voor ons.

Zelf nagemeten op 21 nov met `curl -sL` en een gewone browser user-agent:

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | CatPin Superhive: "Sales 400+", "4 ratings", "Published 3 months ago", prijzen $24 (was $30), $36 (was $45), $80 (was $100). Klopt. | feit | hoog | superhivemarket.com/products/catpin |
| 2 | Cleave Superhive: "Sales 200+", "3 ratings", "Published about 2 months ago", $23 en "Support the developer" $28 met "Same download as Standard". Klopt. Kanaal nu 158 abonnees en 94 video's (rapport: 157 en 93, één dag verschil). | feit | hoog | superhivemarket.com/products/cleave, YouTube-kanaalpagina |
| 3 | CatPin Gumroad: 84 beoordelingen, gemiddeld 4,8 (in de pagina-data en in de zoek-API), prijs in zoeken 2100 cent = $21. Klopt. | feit | hoog | alexsokol.gumroad.com/l/catpin, gumroad.com/products/search?query=catpin |
| 4 | MACHIN3tools Gumroad: "free/pay what you want" en "after 6 years and less than 1% of users paying voluntarily" staat er letterlijk. Klopt. | feit | hoog | machin3.gumroad.com/l/MACHIN3tools |
| 5 | SnapSplit: Sales 30+, Published 8 months ago, $20; Extensions 1.797 downloads (rapport 1.796). Click Joints Extensions 297 (rapport 295). Onze Superhive: $12 en $45, "Published 2 days ago". Klopt. | feit | hoog | de drie pagina's |
| 6 | BagaPie: BA-draad 129.993 keer bekeken, 560 berichten, 911 likes, 17 jun 2021; Superhive Sales 3.600+, Downloads 87.500+. CatPin "NEW 1.0.7 Update is HERE!" 22K. Klopt. | feit | hoog | blenderartists.org/t/1310959.json, Superhive bagapie-assets, kanaalpagina CatPin |
| 7 | Superhive-pagina's ingebedde video's: Cleave 3 YouTube-embeds (4 iframes), CatPin 8 frames, wij 1. Klopt met doe-punt 3. | feit | hoog | iframes geteld in de html |
| 8 | Doe-punt 1 rekent alle verkopen van Cleave en CatPin toe aan de Shorts (1 koper per 500 tot 2.000 weergaven). CatPin had ook 4 lange video's van 12K tot 23K, en ons kanaal is nieuw. De verwachting 15 tot 60 verkopen kan dus flink lager uitvallen. Is wel als GOK gemerkt. | vermoeden | midden | na 2 weken Shorts: weergaven en klikken op dortus.com/yt naast verkopen leggen |
| 9 | "Cleave 200+ in ±2 maanden": de Superhive-datum is 2 maanden, maar of Cleave daarvoor al op Gumroad verkocht is niet bekeken. Tempo kan dus iets lager zijn. | vermoeden | laag | eerste Gumroad-datum of eerste video van het kanaal |
| 10 | Het rapport beantwoordt de vraag (10, 100, 1000) eerlijk, en zegt zelf dat mijlpalen per maand nergens openbaar zijn. "Wat niet lukte" is duidelijk. | feit | hoog | |

Niet zelf nagemeten (wel geprobeerd of niet nodig): weergaven per losse Short, Arctic Shift-posts, MACHIN3-draden. YouTube geeft per video geen teller via curl op de watch-pagina; de kanaalpagina gaf de lange video's wel.

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | **Doe-punt 1 zegt "Roep, Maker via Metricool na de Keurder" voor YouTube Shorts.** Dat klopt niet meer: Shorts uploadt de hoofdchat zelf in YouTube Studio (CLAUDE.md regel 4, Thijs 21 nov; `marketing/REGELS.md` r. 85). Chris en de Maker van Roep maken alleen het concept. | feit | hoog | CLAUDE.md regel 4 |
| 2 | **Doe-punt 8 zegt "Thijs, mail, staat klaar".** Er staat niet bij dat er pas iets uitgaat na zijn ja op de tekst (de mails gaan vanaf zijn adres). Het bronbestand zegt het wel, dit rapport niet; een lezer kan "staat klaar" lezen als "kan weg". | feit | hoog | CLAUDE.md regel 4 |
| 3 | Geld: alle punten zijn $0 (gratis Pro-codes kosten geen geld). Klopt; er staat nergens een uitgave zonder ja. | feit | hoog | regel 1 |
| 4 | Doe-punten 3 tot 6 (Superhive-pagina, supporter-trede, prijs, coupon) liggen bij de hoofdchat. Goed. Doe-punt 5 en 6 gaan over prijs en korting: volgens `marketing/REGELS.md` is iets met prijs of korting oranje. Dat staat er niet bij, maar het gaat hier om de winkel, niet om een post. | vermoeden | midden | REGELS.md r. 86 |
| 5 | Doe-punt 2 (lange video, "Roep") noemt de keuring niet. Mag beter, geen fout: lange video's lopen via Metricool en de Maker. | feit | midden | regel 4 |
| 6 | Labels: bijna elk cijfer heeft GEZIEN, DERDEN of GOK, ook in de tabel (kolom Bron). Een paar tempo's staan als "berekend" (CatPin ±130 per maand, SnapSplit ±4 per maand, BagaPie 4 per 100). Dat is rekenen op GEZIEN-cijfers en eerlijk benoemd, maar geen van de drie woorden. | feit | hoog | regel 5 |
| 7 | Doe-punt 8: "5 verkopen bij 43.000 weergaven" staat als DERDEN, maar zonder link hier; de link zit pas twee stappen verder (makers-1.1, "ronde 13 punt 73"). | feit | midden | regel 5 |
| 8 | Geen persoonsgegevens; `organisatie/controle/check.py` op het bestand: "OK". Geen gedachtestreepjes gevonden. Nederlands, gewone woorden. 149 regels. | feit | hoog | regel 2 en 8 |

## Deel C: zou een lezer (Thijs, de hoofdchat) er iets aan hebben?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De doe-lijst bovenaan is concreet en direct bruikbaar; de vergelijkingstabel maakt het verhaal in 10 seconden duidelijk. | | |
| 2 | Tien doe-punten zonder volgorde naar geld. Prijs naar $19 (punt 5) en Shorts (punt 1) brengen het meest op; dat zie je nu niet. | zet de 3 punten met het meeste geld bovenaan | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Doe-punt 1: wie plaatst aanpassen naar "concept door Chris en de Maker van Roep, groen gekeurd, de hoofdchat uploadt zelf in YouTube Studio" (CLAUDE.md regel 4).
2. Doe-punt 8: erbij zetten "gaat pas uit na ja van Thijs op de tekst (zijn adres)".

**Kan**
- Doe-punt 1: de toerekening van alle verkopen aan Shorts als onzeker benoemen (lange video's deden mee; ons kanaal is nieuw).
- "berekend" vervangen door "berekend uit GEZIEN" of GOK.
- Link bij het DERDEN-cijfer in doe-punt 8.
- Doe-punt 5 en 6: "oranje (prijs/korting)" erbij.
- Doe-lijst ordenen naar verwacht geld.
