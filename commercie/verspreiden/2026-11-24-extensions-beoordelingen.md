# extensions.blender.org: eerste beoordelingen voor de gratis Click Joints, plus de steunzin die nog ontbreekt (Verspreider, run 9, 24 nov 2026)

Plek: onze eigen pagina op extensions.blender.org (vindbaarheid), via onze eigen kanalen. Kost 0 euro. Niets onder de naam van Thijs, niemand benaderen.

## Wat ik zag (GEZIEN, curl 24 nov ±11:45 tot 12:00 UTC)

1. **Elke lijst op extensions.blender.org staat standaard op "Rating".** De hoofdlijst `/add-ons/` (78 pagina's, 1.711 extensies in de API) en elke tagpagina gebruiken `sort_by=-rating_sortkey` als standaard. Wie zonder zoekwoord bladert, ziet eerst de best beoordeelde.
2. **Click Joints heeft 0 beoordelingen en staat daardoor achteraan.** Tag Mesh: plek 166 van 172 (pagina 11 van 11, de laatste). Tag Modeling: pagina 9 van 9, ook de laatste. Van de 172 add-ons op tag Mesh hebben er 122 een beoordeling; die staan allemaal voor ons.
3. **Een paar beoordelingen tillen ons ver op.** Op tag Mesh (16 add-ons per pagina) staat Rotor met 2 beoordelingen van 5,0 op plek 78 (pagina 5). Add-ons met 5 beoordelingen van 5,0 staan op plek 35 tot 43 (pagina 3). De sorteersleutel weegt dus aantal en gemiddelde samen.
4. **Zoeken gaat op woorden, niet op beoordeling.** Op "3d print" staan add-ons zonder beoordeling op plek 2, 6 en 7. Beoordelingen helpen dus vooral bij bladeren (hoofdlijst en tags), niet bij zoeken.
5. **De nieuwe eerste zin uit run 1 werkt.** Zoekplek nu: action figure #1, figurine #1, doll #1, toy #2, articulated #3, figure #2, joint #1, ball joint #1, poseable #1, 3d print #13. Op 23 nov waren we onzichtbaar op articulated, action figure, toy, figurine, doll en 3d print. Nog niet zichtbaar: "posable" (één e) en "printable" (niet in de eerste 11).
6. **De gekeurde steunzin staat er niet.** Daan keurde op 22 nov de zin van Bram voor onderaan de beschrijving (`platformen/blender/keuring/2026-11-22-steunzin-daan.md`, `platformen/blender/verwijzing-pro.md`). De beschrijving eindigt nu nog met "Support: thijs@dortus.com". Bij het plakken van de eerste zin (lijst punt 3b) is hij blijkbaar niet meegegaan.
7. **De regels zeggen niets over beoordelingen.** In de voorwaarden van extensions.blender.org (laatst bijgewerkt 10 aug 2026) staat geen regel over vragen om een beoordeling. Wel: geen reclame in Blender zelf (6.1 en 6.3). Dus vragen doen we buiten Blender, en zonder iets terug te beloven.

## Voorstel

### A. Steunzin plakken, vóór de sale (wo 26 nov), door de hoofdchat
Op de beheerpagina van Click Joints op extensions.blender.org (zelfde sessie als lijst punt 3b), onder "Support: thijs@dortus.com", de zin die Daan al keurde, letterlijk:

```
Click Joints is free and stays free. If it saves you time, you can support development by buying Click Joints Pro on Gumroad: https://duinhouwer8.gumroad.com/l/click-joints-pro
```

Waarom nu: de gratis pagina krijgt elke dag nieuwe bezoekers (downloads 365, GEZIEN op de pagina 24 nov ±11:50 UTC; +163 in 7 dagen, GEZIEN scorebord) en nergens op die pagina staat nu een weg naar Pro behalve het veld Website. Wie de zin in de sale-week ziet en via Gumroad koopt, kan CYBER25 gebruiken. Geen sale-tekst in de zin zelf: dat is reclame en riskeert regel 6.2.

Als er toch een nieuwe versie omhoog gaat (0.1.2 met tag Sculpt, staat klaar op tak `claude/blender-0.1.2b`): in dezelfde sessie. Op tag Sculpt staan maar 21 add-ons (GEZIEN), dus ook zonder beoordeling staan we daar op pagina 2 van 2 in plaats van pagina 11 van 11.

### B. Eén zin die om een beoordeling vraagt, op onze eigen plekken
Alleen voor mensen die de gratis versie al gebruiken. Geen beloning, geen ruil (dus niet koppelen aan "foto sturen, Pro gratis"), nooit in Blender zelf. Link naar de reviewpagina (GEZIEN: 200; "Leave a review" vraagt daar een Blender ID).

**B1. dortus.com/click-joints/, direct onder de knop voor de gratis download (Bram, repo dortus):**
```
Already using the free version? A review on Blender Extensions helps other people find it: https://extensions.blender.org/add-ons/click-joints/reviews/
```

**B2. README van repo click-joints, onder het gratis deel en boven "Report a problem" (Bram of hoofdchat):**
```
Using Click Joints? A review on [Blender Extensions](https://extensions.blender.org/add-ons/click-joints/reviews/) helps other people find it.
```
(De README kreeg 25 weergaven in 14 dagen, GEZIEN GitHub traffic; klein; de link "Report issues" op de listing gaat naar de issues, niet naar de README, dus dit bereik is beperkt.)

**B3. Vaste slotzin in de triage, alleen na een opgelost probleem van een gebruiker van de gratis versie, en alleen in antwoorden die volgens de triage al naar buiten mogen; nooit per mail onder de naam van Thijs zonder zijn ja (regel 4) (wie de triage doet):**
```
Glad it works now. If Click Joints is useful to you, a short review on Blender Extensions helps other people find it: https://extensions.blender.org/add-ons/click-joints/reviews/ No pressure, and thanks for reporting this.
```

## Wat het oplevert
- Van 0 naar 2 beoordelingen: tag Mesh van pagina 11 naar ±pagina 5; naar 5: ±pagina 3 (GEZIEN, afgeleid van de plek van add-ons met 2 en 5 beoordelingen van 5,0; dat onze beoordelingen 5,0 worden is een GOK).
- Hoeveel extra downloads dat geeft: GOK, klein tot midden; hoeveel mensen bladeren in plaats van zoeken weten we niet. Elke extra download is een kans op Pro via dortus.com en de steunzin.
- De steunzin (A): GOK 0 tot 2 extra Pro-verkopen in de sale-week. Kost de hoofdchat ±3 minuten in een sessie die er toch al is.

## Wie
- A: hoofdchat (beheerpagina extensions.blender.org, zelfde account als bij punt 3b). Geen nieuw punt voor Thijs.
- B1 en B2: Bram (dortus.com via de bekende mergeweg; README via push naar click-joints), Daan keurt de site.
- B3: triage-eigenaar.
- Meten (Verspreider, volgende runs): aantal beoordelingen en plek op tag Mesh en Modeling, met curl op `https://extensions.blender.org/tag/add-ons/mesh/?page=N`, met het aantal pagina's per tag erbij.

## Ook gezien, voor later
- **Gumroad Discover vindt ons op geen enkel woord**, ook niet op "click joints" (10 zoekwoorden, GEZIEN via `gumroad.com/products/search?query=`, 24 nov). CatPin (85 beoordelingen, $21, nu al met doorgestreepte $30), Split 3D Print en Cleave staan er wel. Past bij de eerdere vondst dat Discover pas opent na $100 omzet plus keuring (DERDEN, https://gumroad.com/help/article/79-gumroad-discover). Niets te doen tot we die omzet halen.
- Discord-lijsten (Disboard, top.gg): 403 met curl; Discadia laadt alleen met JavaScript. Geen weg zonder browser.
- Lesterbanks: laatste bericht 17 jul 2026, daarvoor 10 jun (GEZIEN, lesterbanks.com/feed): te stil om een tip waard te zijn.
- CG Channel: geen artikel over CatPin, Split 3D Print of Cleave (GEZIEN, zoeken op hun site); kleine printtools zijn daar geen nieuws. Blijft bij de Black Friday-lijst.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## Keuring (aparte keurder, 24 nov 2026)

Akkoord: nee (alleen om drie verkeerde plek-cijfers; de inhoud van het voorstel is goed en eerlijk. Na het rechtzetten van M1 tot M3 is het akkoord, opnieuw keuren hoeft alleen voor die punten.)

# Keuring extensions-beoordelingen Click Joints, 24 nov 2026, aparte keurder
Wat ik keurde: `commercie/verspreiden/2026-11-24-extensions-beoordelingen.md` (stand vóór deze sectie). Alles nagelopen met curl op 24 nov ±13:00 tot 13:15 UTC (GEZIEN, tenzij anders gezegd).

### Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Standaard sortering is Rating: op tag Mesh staat `?page=1&sort_by=-rating_sortkey` als "is-active" in het menu, op `/add-ons/` ook (`?sort_by=-rating_sortkey&page=1`). Hoofdlijst heeft 78 pagina's (pagina 78 heeft 8 kaarten, 79 is leeg). Klopt. | feit | hoog | |
| A2 | Tag Mesh: 172 add-ons, 122 met beoordeling, 50 zonder. Click Joints op plek 166, zonder beoordeling. Klopt. | feit | hoog | |
| A3 | **Aantal pagina's klopt niet.** Tag Mesh heeft 11 pagina's (10 x 16 + 12), niet 12: pagina 12 geeft 0 kaarten, de paginering op pagina 11 gaat niet verder. Click Joints staat dus op de **laatste** pagina, 11 van 11. Tag Modeling: Click Joints op pagina 9, en dat is de laatste (pagina 9 heeft 7 kaarten, pagina 10 is leeg), dus 9 van 9, niet 9 van 10. | feit | hoog | curl `tag/add-ons/mesh/?page=12` en `tag/add-ons/modeling/?page=10` |
| A4 | **Plek van Rotor klopt, pagina niet.** Rotor (5,0, 2 beoordelingen) staat op plek 78, maar dat is **pagina 5** (16 per pagina), niet pagina 7. Add-ons met 5,0 en 5 beoordelingen staan op plek 35 tot 43, allemaal op pagina 3 (niet "3 tot 4"). Daardoor is ook de opbrengst onder "Wat het oplevert" te somber: 2 beoordelingen = ±pagina 5, 5 beoordelingen = ±pagina 3. | feit | hoog | zelfde curl, 16 kaarten per pagina geteld |
| A5 | De sorteersleutel is geen simpel gemiddelde maal aantal: Moldforge (5,0, 5 beoordelingen) staat op plek 75, tussen add-ons met 3 beoordelingen. "Weegt aantal en gemiddelde samen" is dus ruwweg waar, maar de voorspelde plek is een schatting. | vermoeden | midden | meer plekken vergelijken na onze eerste beoordelingen |
| A6 | Zoeken: "action figure" Click Joints #1 (2 resultaten). "3d print" Click Joints #13; add-ons zonder beoordeling op plek 2, 6 en 7. Klopt. | feit | hoog | |
| A7 | Beschrijving eindigt met "Tested on Blender 4.2 LTS and 5.2 LTS / Support: thijs@dortus.com", daarna "What's New". Steunzin staat er niet. Downloads 366 (voorstel: 365, ±1 uur eerder; klopt). | feit | hoog | |
| A8 | Steunzin in voorstel A is letterlijk gelijk aan de zin in `verwijzing-pro.md` (bijwerking 22 nov) en in de keuring van Daan. | feit | hoog | |
| A9 | Voorwaarden: "Last updated: 10 August 2026"; 6.1 tot 6.3 zoals geciteerd in `verwijzing-pro.md`. Het woord "rating" komt er niet in voor, "review" alleen als "code must be reviewable" (3.5). Niets over vragen om beoordelingen. Klopt. | feit | hoog | |
| A10 | Reviewlink `extensions.blender.org/add-ons/click-joints/reviews/` geeft 200. Klopt. | feit | hoog | |
| A11 | Gumroad-zoeken "click joints": geen Click Joints in de uitslag; CatPin wel (85 beoordelingen, gemiddeld 4,8, 2100 cent = $21), Cleave ook. Klopt. | feit | hoog | |
| A12 | Tag Sculpt: 21 add-ons, 2 pagina's (16 + 5). Klopt. | feit | hoog | |
| A13 | Bij B2 staat dat de README "de link Report issues op de listing" is. De listing wijst naar `github.com/.../click-joints/issues`, de issuepagina, niet de README. Wie daar komt ziet de README niet direct. De zin onderaan de README bereikt dus vooral wie de repo zelf opent. | feit | hoog | |

### Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | De plekcijfers in A3 en A4 staan als GEZIEN maar kloppen niet. Kleine fout, geen verzinsel, maar een GEZIEN-cijfer moet kloppen. | feit | hoog | harde regel 5 |
| B2 | Overige cijfers hebben een label: downloads en zoekplekken GEZIEN, Discover-drempel DERDEN met link, opbrengst en "5,0" als GOK. Goed. | feit | hoog | harde regel 5 |
| B3 | Eerlijk: geen beloning of ruil voor een beoordeling (staat er zelfs expliciet), er wordt om "a rating" gevraagd en niet om vijf sterren, alleen aan bestaande gebruikers, niets in Blender zelf. Geen sale-tekst in de steunzin, dus 6.2 veilig. Goed. | feit | hoog | regel 6 voorwaarden, eerlijkheid |
| B4 | Geen persoonsgegevens: alleen het zakelijke adres thijs@dortus.com dat al openbaar op de listing staat, en de Gumroad-link die al gekeurd is. De GitHub-gebruikersnaam staat er niet in. Goed. | feit | hoog | harde regel 2 |
| B5 | Niets gaat zonder ja onder de naam van Thijs naar buiten via A, B1 en B2: dat zijn plekken van Dortus en de productrepo, met de gekeurde zin. B3 gaat mee in antwoorden aan gebruikers. Volgens de skill `triage` plaatst de hoofdchat die. Komt zo'n antwoord uit een account van Thijs (zijn GitHub-account) of als mail, dan geldt harde regel 4 al voor het hele antwoord. Gmail is alleen lezen. B3 voegt geen nieuwe weg toe, maar het voorstel zegt dit niet. | vermoeden | midden | harde regel 4 en 7 |
| B6 | Nederlands, gewone woorden, geen gedachtestreepjes gevonden. Plaatsteksten in goed Engels. Wie wat doet staat er helder bij (A hoofdchat, B1/B2 Bram met keuring Daan, B3 triage, meten Verspreider). | feit | hoog | harde regel 8 |
| B7 | Kost 0 euro. | feit | hoog | harde regel 1 |

### Deel C: zou een gebruiker het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | De site zegt "Leave a review" en "Reviews", onze zinnen zeggen "rating". Wie klikt, zoekt een knop die anders heet. | "a short review on Blender Extensions" in B1, B2 en B3, of beide woorden. | klein |
| C2 | Een beoordeling vraagt een Blender ID. Wie dat niet heeft, haakt af zonder te weten waarom. | Niet nodig om te zeggen in de zin; wel ok zo. Alleen noemen als blijkt dat niemand het doet. | klein |
| C3 | B3 is vriendelijk en zonder druk ("No pressure"). Goed: zo voelt het niet als een ruil voor de hulp. | | |

### Moet (blokkeert akkoord)
- **M1:** Punt 2: tag Mesh heeft 11 pagina's, Click Joints staat op pagina 11 van 11 (laatste). Tag Modeling: pagina 9 van 9.
- **M2:** Punt 3: Rotor staat op plek 78 = pagina 5, niet 7. Add-ons met 5 beoordelingen van 5,0: plek 35 tot 43, pagina 3.
- **M3:** "Wat het oplevert": van 0 naar 2 beoordelingen = tag Mesh van pagina 11 naar ±pagina 5; naar 5 = ±pagina 3 (met GOK dat de sleutel zo blijft werken, zie A5).

Voorstel A (steunzin plakken) hangt niet van M1 tot M3 af: de zin is letterlijk gelijk aan wat Daan op 22 nov keurde en de regels zijn niet veranderd. De hoofdchat mag A uitvoeren zonder op deze herstelronde te wachten.

### Kan (mag later)
- K1: Zet bij B3 één zin: "alleen in een antwoord dat volgens de triage al naar buiten mag; nooit per mail" (B5).
- K2: Gebruik "review" in plaats van (of naast) "rating" in B1 tot B3 (C1).
- K3: Bij B2 de reden bijstellen: de link op de listing gaat naar de issuepagina, niet de README (A13). De zin in de README is nog steeds goed, het bereik is alleen kleiner.
- K4: Bij meten ook het aantal pagina's per tag noteren, zodat een plek als "x van y" klopt als er add-ons bijkomen.

### Nakeuring (aparte keurder, 24 nov 2026)
Akkoord: ja

- M1: verwerkt. Punt 2 zegt nu Mesh pagina 11 van 11 en Modeling pagina 9 van 9, allebei de laatste. Bij Sculpt staat nu ook "pagina 11 van 11". Klopt met wat ik eerder telde.
- M2: verwerkt. Punt 3 zegt nu Rotor op plek 78 (pagina 5, 16 per pagina) en 5 beoordelingen op plek 35 tot 43 (pagina 3). Klopt.
- M3: verwerkt. Bij "Wat het oplevert" staat nu ±pagina 5 bij 2 beoordelingen en ±pagina 3 bij 5. De GOK op 5,0 staat er nog bij. Goed.
- K1: verwerkt. B3 alleen in antwoorden die volgens de triage al naar buiten mogen, en nooit per mail onder de naam van Thijs zonder zijn ja. Dat volgt regel 4, en Gmail is toch alleen lezen.
- K2: verwerkt. B1, B2 en B3 zeggen nu "review", net als de knop op de site. Het Engels is goed.
- K3: verwerkt. Bij B2 staat nu dat de link op de listing naar de issues gaat en niet naar de README.
- K4: verwerkt. Bij meten staat nu ook het aantal pagina's per tag.
- Geen gedachtestreepjes, geen nieuwe persoonsgegevens. Niets anders veranderd buiten deze punten.
