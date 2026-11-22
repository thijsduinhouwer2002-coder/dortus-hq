# Voorstel: MetaTrader Market (mql5.com)

Onderzocht 6 nov 2026, run 15:32 UTC, door Vera. Zelf aan de lijst toegevoegd omdat de winkel zelf betaalt en verkoopt (MT4 en MT5: indicatoren, handelsrobots, hulpprogramma's).

**Cijfer: 3 van 10. Advies: nee.**

## Cijfers

### Geld
- Afdracht 20%, minimumprijs $30, kopen of huren (1, 3, 6 of 12 maanden), minstens 5 activaties per koper. GEZIEN: https://www.metatrader5.com/en/terminal/help/market/market_sell en https://www.mql5.com/en/market/rules
- Geld staat een week vast, kopers kunnen niet retourneren. GEZIEN: rules-pagina (VII.5, IV.14).
- Prijzen: hulpprogramma's $30 tot $100, nieuwe robots $30 tot $299, toprobots $400 tot $1.700. GEZIEN in lijsten.
- Verkoopaantallen staan niet op productpagina's. Ook de grootste (Quantum Emperor MT5) toont alleen reviews (590) en demo-downloads (46.263). GEZIEN: https://www.mql5.com/en/market/product/103452
- Top 10 verkopers halen $15.000 tot $100.000 per maand volgens MetaQuotes zelf (bericht van januari 2021, dus oud). DERDEN, reclame van het platform: https://www.metatrader5.com/en/news/2181
- 430.000 verkopen in totaal sinds de start, tot februari 2022. In 2021 ruim 100.000 verkopen (https://www.metatrader5.com/en/news/2227). DERDEN: https://finance.yahoo.com/news/leading-algorithmic-trading-community-mql5-144500386.html
- Een verkoper met 29 producten claimde $3.000 tot $5.000 per maand, maar verkocht alles in juni 2026 voor $1.200. Wijst erop dat die omzet weg was. DERDEN, niet te controleren: https://www.earnforex.com/forum/threads/complete-mql5-store-portfolio-%E2%80%93-29-products-full-source-code.54600/
- Een blog op mql5.com van 29 okt 2026 schat voor de top 10 producten uit 2026 met 46 tot 219 verkopen in de laatste maand. Dat zijn wel gevestigde makers: de verkoper van Gold Beaver (177869) heeft 11 producten en een rating van 10.938. Het geld gaat dus naar bekende namen. DERDEN: https://www.mql5.com/en/blogs/post/778775
- **Geen enkele nieuwe kleine verkoper (gestart 2024 tot 2026) gevonden die aantoonbaar $300 of meer per maand haalt.**

### Bereik (steekproef 15 betaalde producten uit 2024 tot 2026, GEZIEN)
- Demo-downloads: 2, 2, 2, 7, 11, 12, 13, 17, 18, 22, 26, 37, 48, 69, 127 (product-ID's 173192, 168922, 167271, 174837, 110670, 114012, 177331, 167733, 136453, 179151, 169909, 122104, 112669, 135237, 167900).
- **Mediaan 17 demo-downloads. 1 van 15 (7%) haalt 100+.**
- Reviews (alleen kopers mogen reviewen, dus ondergrens voor verkopen): 10 met 0, 4 met 1, 1 met 3.
- Schatting: de meeste nieuwe producten verkopen 0 tot 5 keer in 6 maanden. GOK.
- Beperking: de steekproef gaat over nieuwe producten, niet over nieuwe makers (de verkoper van 173192 heeft al een rating van 176). Nieuwe makers zullen eerder lager uitkomen.
- Beperking: de steekproef komt uit pagina's die in zoekresultaten stonden, niet willekeurig uit de nieuw-lijst. Dat kan naar boven of beneden afwijken.

### Drukte
- Ongeveer 41.000 MT5-producten (591 pagina's van 70 in de nieuw-lijst), waarvan ±16.300 indicatoren en ±6.900 hulpprogramma's. GEZIEN: https://www.mql5.com/en/market/mt5/new/page87
- Ongeveer 3.000 nieuwe producten per maand (MT4 en MT5 samen). GOK, afgeleid uit product-ID's en publicatiedata (±132.600 in feb 2025, ±177.300 in mei 2026).
- Veel nieuwe producten zijn goud-robots van dezelfde groepen makers (49 van 70 op één nieuw-pagina). GEZIEN.

### Vindbaarheid
- Betaalde promotie binnen MQL5 bestaat niet. DERDEN: https://www.mql5.com/en/forum/509733
- De productpagina mag niet linken naar Telegram of eigen sites. GEZIEN: rules-pagina.
- Verkopers zeggen: de eerste review is het moeilijkst, groei komt van eigen publiek (YouTube, Telegram, lijsten). Toppers hebben lanceringspieken van honderden verkopen, de steekproef bijna niets. Eigen marketing is dus nodig. GOK op basis van dat verschil.

### Past het bij ons
- Bouwen kan: een hulpprogramma (bijvoorbeeld een bewaker voor de regels van prop firms, een risicocalculator, een copier van Telegram naar MT5) is in 1 tot 2 weken te maken in MQL5. GOK.
- Verkopen vraagt ID-verificatie van Thijs (paspoort of rijbewijs), validatie in de Strategy Tester, geen DLL's, geen winstbeloftes. GEZIEN: rules-pagina.

## Voordelen
- De winkel betaalt zelf, 20% afdracht, hoge prijzen ($30 tot $100 voor een hulpprogramma).
- Huur is ingebouwd, dus terugkerende inkomsten zijn mogelijk.
- Hulpprogramma's vragen geen handelskennis.

## Nadelen
- Bereik is zeer laag: mediaan 17 demo-downloads, 7% haalt 100+.
- Geen bewijs dat een nieuwe kleine maker er geld verdient.
- Zeer druk: ±3.000 nieuwe producten per maand en tientallen gratis trade managers en copiers.
- Reputatie: forum vol klachten over nepreviews en doorverkochte activaties, sector met veel oplichting. DERDEN: https://www.mql5.com/en/forum/415200/page5
- Eigen marketing (YouTube, Telegram) is nodig, en die mag niet eens vanaf de productpagina gelinkt worden.
- Risico voor Thijs: ID-verificatie en een sector waar al snel de indruk van financieel advies ontstaat.

## Eerste idee als we het toch zouden doen
Een gratis lite-versie en een betaalde pro-versie ($30 tot $60, ook als huur) van een bewaker voor prop-firm-regels (dagverlies, maximale drawdown, automatisch sluiten), voor MT4 en MT5 tegelijk.

## Waarom nee
De doelen vragen geld, en het rol-criterium is dat kleine makers aantoonbaar betaald krijgen. Dat is hier niet aangetoond, en het bereik van een nieuw product is lager dan bij Figma of VS Code. Het geld zit bij een kleine top met een eigen publiek.

## Wat het oordeel zou veranderen
- Twee verkopers die na 2024 begonnen en aantoonbaar (screenshot van verkopen of omzet) $300 of meer per maand halen zonder groot eigen publiek.
- Een willekeurige steekproef uit de nieuw-lijst (in een browser) met een mediaan van 100+ demo-downloads.

## Wat niet gemeten kon worden
- Echte verkoopaantallen: alleen met een eigen verkopersaccount, of door reviews en demo-downloads per product wekelijks te volgen.
- Lijsten gesorteerd op nieuw en populair: geblokkeerd. Kan met Chrome op Thijs' HP.
- Downloads van gratis producten: niet zichtbaar.
- De blogger van post 778775 komt ergens aan verkoopschattingen. Uitzoeken waar die vandaan komen: misschien zijn verkopen per product toch ergens te zien.

## Nagekeken
Controleur 6 nov 2026: akkoord. Regels (20%, $30, activaties, geen retour, geen externe links) en vier demo-tellingen nagekeken en juist. Tien minuten gericht gezocht naar een nieuwe kleine maker boven $300 per maand: niet gevonden. Correcties (datum en uitleg 430.000 verkopen, oude datum toppercijfer, retour-uitzondering geschrapt, blog top 10 toegevoegd, steekproef gaat over producten en niet makers) zijn verwerkt. Een 4 kon ook, het advies blijft nee.
