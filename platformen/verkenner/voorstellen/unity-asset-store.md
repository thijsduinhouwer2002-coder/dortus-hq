# Voorstel: Unity Asset Store (tools)

**Advies: nee voor nu. Cijfer: 3 van 10 (was 4).** Herzien op 6 nov 2026 (run 22:31) met een eigen meting van 4.268 tools. Een gewone nieuwe betaalde tool krijgt na 3 tot 6 maanden bijna nooit een beoordeling: 82% heeft er nul, en maar ±2% heeft er 5 of meer. De tools die wel goed scoren zijn bijna allemaal vervolgversies of bundels van bekende uitgevers, die hun oude beoordelingen meenemen. Bewijs dat een nieuwe kleine maker hier geld verdient vonden we niet. De oude versie van dit voorstel staat hieronder.

## Eigen meting (6 nov 2026)
Hoe: de sitemap van de winkel (20 delen) gaf 11.744 unieke tools. Alle 4.268 tools met id 300000 of hoger (gepubliceerd van eind 2024 tot nu) zijn gelezen met `data/unity-haal-script.py` (versie 2, leest alleen het product met het id uit de URL; de fout uit versie 1 is weg). Analyse met `data/unity-analyse-script.py`, data in `data/unity-tools-2026-11-06.json`. Verkopen toont Unity niet, dus het aantal sterbeoordelingen is de maat.

**Bereik (GEZIEN)**
- Betaalde tools van 3 tot 6 maanden oud (mei tot aug 2026), zonder vervolgversies en bundels: n=886. Mediaan 0 beoordelingen. 18% heeft er 1 of meer, ±2% 5 of meer, ±0% 10 of meer (na correctie door de controleur, die 11 geërfde gevallen vond).
- Uitgevers met 1 tot 3 tools in de meting: hetzelfde beeld (21% 1+, 2% 5+, 1% 10+).
- Ouder cohort, jan tot jun 2025 (16 tot 22 maanden oud): 40% 1+, 9% 5+, ±3% 10+. Dat verschil zegt vooral iets over leeftijd, niet dat de markt slechter wordt. Ook na anderhalf jaar heeft de meerderheid geen enkele beoordeling.
- Hoeveel verkopen bij één beoordeling horen is ONBEKEND. Geen betrouwbare bron gevonden (discussions.unity.com weigert curl). Zelfs bij een ruime GOK van 1 beoordeling per 30 tot 100 verkopen zit de mediane nieuwe tool onder de 30 verkopen.
- Unity neemt beoordelingen mee naar vervolgversies en bundels (GEZIEN: PlayMaker 2, gepubliceerd 21 juli 2026, toont 3.428 beoordelingen met reviews uit 2014; ook Online Maps v5, Compass Navigator Pro 4, Grabbit 2). Wie al een naam heeft, begint dus met een voorsprong; een nieuwe maker begint op nul.

**Geld**
- Maker houdt 70% (DERDEN, zie onder). Prijsmediaan van nieuwe betaalde tools ±$20 (GEZIEN). ±85% van de nieuwe tools is betaald (GEZIEN), dus betalen is hier normaal.
- Geen enkel recent cijfer (2025 tot 2026) van een kleine nieuwe maker gevonden. De enige echte cijfers zijn oud: $56 in de eerste maand en $316,8 na zes maanden, rond 2020 (DERDEN, [Game Developer](https://www.gamedeveloper.com/business/what-is-the-unity-asset-store-and-how-to-make-money-on-it-)). De bewering "$200 tot $800 per maand in het eerste jaar" van Exoa heeft geen eigen cijfers (DERDEN, [dev.to, juni 2026](https://dev.to/exoa/how-to-publish-a-unity-asset-to-the-asset-store-the-complete-publisher-guide-4iei)).

**Drukte (GEZIEN)**
- Nieuwe tools per maand: begin 2025 ±110, mei tot aug 2026 gemiddeld ±280, aug tot okt 2026 ±380. Ruwweg 2,5 tot 3,5 keer zo druk als begin 2025, terwijl de aandacht per tool daalt.

**Meetgrenzen**
- De sitemap mist ±15% van de gepubliceerde tools (de winkel meldt 15.232 tools; de controleur vond in 550 losse id's buiten de sitemap 4 gepubliceerde tools). Verwijderde tools ontbreken helemaal, dus oude cohorten ogen iets beter dan ze waren.
- De grens id 300000 mist een deel van jan 2025 (±6% van dat cohort).
- De filter op vervolgversies is een ondergrens; er kunnen nog een paar geërfde gevallen in zitten. Dat maakt het beeld voor nieuwe makers alleen maar slechter, niet beter.

## Waarom nee
Thijs zoekt een plek waar kleine makers aantoonbaar geld verdienen en waar Dortus groot kan worden. Hier haalt een nieuwe betaalde tool van een onbekende maker na een half jaar meestal geen enkele beoordeling, het aanbod groeit snel, en de winnaars zijn gevestigde uitgevers die hun beoordelingen meenemen naar nieuwe versies. Dat is het tegenovergestelde van een open kans.

## Wat het oordeel kan veranderen
- Een betrouwbare verhouding verkopen per beoordeling die veel hoger blijkt dan 100 (dan zou 1 tot 5 beoordelingen toch flink geld kunnen zijn).
- Cijfers van een kleine maker uit 2025 tot 2026 met echte verkoop in de eerste maanden.
- Herhaalmeting kan met dezelfde scripts; zinvol over ±3 maanden.

## Nakijken
Controleur (6 nov, run 22:31): script en rekenwerk akkoord, 10 pagina's zelf nagelezen en alles klopt. Vijf correcties, alle verwerkt: geërfde beoordelingen ook bij bundels en namen als "V8" eruit, cijfers mei tot aug bijgesteld naar 18 / 2 / 0%, sitemap mist ±15%, aanbod per maand bijgesteld, verhouding verkopen per beoordeling blijft onbekend.

---

# Oude versie (6 nov 2026, zonder eigen meting)


**Advies: nog niet klaar, voorlopig nee. Cijfer: 4 van 10.** Er zijn losse signalen dat makers verdienen, maar we vonden geen compleet cijfer van een nieuwe kleine maker uit 2024 tot en met 2026. Zonder eigen meting nemen we dit risico niet, ook door de 30% afdracht en de verkoop tegen zware korting. Opnieuw bekijken zodra we de winkel zelf kunnen lezen. Geschreven op 6 nov 2026.

## Meetgrens
assetstore.unity.com en gamedevthings.com waren in deze run geblokkeerd. Geen eigen meting: alles is DERDEN of GOK. De huidige afdracht staat niet op de gelezen officiële pagina. De winkel toont voor zover we weten geen verkoopcijfers per product, dat is niet bevestigd. Reddit en Discord zijn niet doorzocht, en het besloten forumdeel voor uitgevers is niet leesbaar, terwijl daar waarschijnlijk de echte cijfers staan. Het ontbreken van bewijs is dus zwak bewijs.

## Cijfers

**Bereik**
- Mediaan en percentage met 100+ verkopen: niet gemeten. Geen bron gevonden.

**Geld**
- Afdracht 30%, maker houdt 70% (DERDEN, niet officieel bevestigd). [Generalist Programmer, 2026](https://generalistprogrammer.com/tutorials/unity-asset-store-selling-guide-revenue)
- Een plug-inmaker uit China noemt $10.050 totale verkoop over 2025 (onduidelijk bruto of netto, koppelt het niet met zoveel woorden aan de winkel, aantal producten en looptijd onbekend). Dat is ±$838 per maand, bij bruto ±$586 na afdracht (eigen rekenwerk), dus rond ons doel van maart voor één gevestigde maker. [Unity-forum, 8 mrt 2026](https://discussions.unity.com/t/a-notice-for-asset-store-assets-from-publishers-in-greater-china/1711108?page=9)
- Een maker noemt 69 verkopen in augustus 2026, na 4 tot 5 maanden verkopen (prijs en aantal producten onbekend), gevolgd door 3 dagen zonder verkoop zonder bekende oorzaak. [Unity-forum, sept 2026](https://discussions.unity.com/t/sudden-drop-to-zero-sales-since-september-7-anyone-else-experiencing-this/1736248). Bij $10 tot $40 per stuk (GOK) is dat $690 tot $2.760 bruto. Ook een ander meldde dagen zonder verkoop na de nieuwe winkelpagina. [Unity-forum, nov 2025](https://discussions.unity.com/t/new-asset-store-layout-feels-like-a-downgrade/950178?page=12)
- Schatting van een maker, zonder bron: een nieuw product van $20 tot $40 met een goede lancering en blijvend 4+ sterren zakt in het eerste jaar naar $200 tot $800 per maand, de top haalt $2.000 tot $8.000. Onduidelijk of dat bruto of netto is. Die maker verkoopt ook advies. [Exoa, jan 2026, bijgewerkt juni](https://exoa.dev/blog/publishing-unity-asset-store)
- Oude eigen cijfers, 2016: van $50 in 15 maanden en $30 tot $60 per maand tot $1.000 tot $2.000 per maand na afdracht. Eén ruwe inschatting daar: alleen de top 25 tot 50 kan ervan leven. [Unity-forum, 2016](https://discussions.unity.com/t/how-much-asset-store-publishers-earn/628535). Te oud om op te bouwen.
- Inkomensniveaus in de gids van Generalist Programmer hebben geen bron. Niet gebruikt.
- Geen cijfer gevonden over de eerste maanden van een nieuw product.

**Drukte**
- ±112.000 producten en ±52 nieuwe per dag (±1.580 per maand, eigen rekenwerk), ±22% van de betaalde producten in 12 maanden bijgewerkt. Crawler GameDevThings, juli 2025, gelezen via een blog met onbekende auteur, die tools meer betalingsbereidheid toedicht dan art-pakketten en de winkel vooral aanraadt voor distributie, niet als inkomen. [Pixel Post](https://hashnode-hub.vercel.app/posts/68797f1d7d9b82780e9d5740)
- Keuring 2 tot 4 weken, zonder bron. [Generalist Programmer](https://generalistprogrammer.com/tutorials/unity-asset-store-selling-guide-revenue)

**Markt**
- Unity Create-omzet: $859 miljoen in 2023, $614 miljoen in 2024, vooral door een bewuste opschoning ([cijfers 2024](https://www.sec.gov/Archives/edgar/data/0001810806/000181080625000021/a2024q4ex-991draft.htm)). Daarna weer groei: Q3 2025 +3%, Q4 2025 +8% ([Q4 2025](https://www.businesswire.com/news/home/20260211343559/en/Unity-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results)). Over de Asset Store zegt dit niets, die wordt niet apart gerapporteerd.
- Enquête 2026 (naam onbekend): Unreal 42%, Unity 30% als hoofdprogramma. Unity houdt wel de meeste Steam-releases: 51% in 2024. [Levvvel](https://levvvel.com/statistics/unity/)
- Unity haalde per 31 maart 2026 producten van makers uit China, Hongkong en Macau uit de winkel. [Unity-forum](https://discussions.unity.com/t/a-notice-for-asset-store-assets-from-publishers-in-greater-china/1711108?page=9). Ruim 3.000 volgens een scan-tool van een maker via [GameFromScratch](https://gamefromscratch.com/major-schism-on-unity-asset-store/), niet van Unity. Dat kan wat ruimte geven (GOK), en laat ook zien hoe afhankelijk je bent.

**Vindbaarheid**
- Geen harde gegevens. De winkel lijkt het hoofdkanaal volgens losse makers, en zware afprijsacties horen erbij (zomeractie 2025: 50%, flitsaanbiedingen tot 98%).

**Past het bij ons**
- Editor-tools in C#: 1 tot 2 weken is mogelijk (GOK), maar goed testen over Unity-versies en support kost blijvend werk. Thijs moet een uitgeversaccount aanmaken.

## Voor
- Eenmalige verkoop zonder eigen betaalsysteem. Grote, bestaande kopersgroep.
- $200 tot $800 per maand zou, als het bruto is, $140 tot $560 netto zijn. Alleen de bovenkant haalt ons doel van maart (GOK dat de schatting klopt).

## Tegen
- Losse, onvolledige signalen dat het kan, geen enkel compleet cijfer van een nieuwe kleine maker.
- 30% afdracht, en veel verkoop tegen zware korting.
- Drukke winkel, en verkoop die zonder bekende oorzaak dagenlang kan wegvallen.

## Eerste idee (als het later toch ja wordt)
Eén editor-tool die fouten in projecten opspoort, als test. Eerst meten welke klachten in reviews van bestaande tools terugkomen.

## Wat er nog gemeten moet worden
Steekproef van minstens 30 tools uit 2026 met reviews en prijs, zodra assetstore.unity.com leesbaar is (netwerkpunt op de lijst voor Thijs). Daarnaast eigen cijfers van makers uit Reddit en Discord.

## Nakijken
Eerste versie afgekeurd door de controleur (6 nov). Zijn fouten 1 tot en met 4 en de kleine punten zijn verwerkt. Volgens zijn eigen oordeel is het stuk daarmee akkoord.
