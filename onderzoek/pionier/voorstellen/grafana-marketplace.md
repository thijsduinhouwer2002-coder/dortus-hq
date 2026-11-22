# Voorstel pionier: Grafana Marketplace (betaalde plugins op Grafana Cloud)

Noor, 8 nov 2026. Meetlat van de pionier (vijf vragen). Cijfers: GEZIEN (zelf gezien of gemeten), DERDEN (met link), GOK.

## Kort
Grafana zelf is geen jong platform (sinds 2014), maar de **betaalde winkel is drie weken oud**: op 20 oktober 2026 werd de Grafana Marketplace algemeen beschikbaar, met proefperiode en maandabonnement via de factuur van Grafana Cloud. Er staan 38 betaalde plugins van 8 makers, waarvan 31 koppelingen (bijna allemaal van één bedrijf, Crest Data) en maar **3 betaalde panelen**, alle drie van één kleine maker met ±5 tot 13 downloads. Grafana groeit hard (omzet ±37% per jaar). Het is een kans om in de categorie betaalde panelen (grafieken) de eerste te zijn, met een kopersgroep die zakelijk is en al per gebruiker per maand betaalt.

Bij Vera viel Grafana af als "zwak of te klein" omdat er geen geld te verdienen was. Dat is sinds 20 oktober het nieuwe feit.

**Cijfer 5 (eerst 6, de controleur gaf 5). Advies: nog niet klaar.** Eerst één stap van Thijs (voorwaarden opvragen: afdracht en of een eenmanszaak wordt toegelaten) en een herhaalmeting die laat zien of betaalde panelen verkopen. Dan opnieuw wegen.

## 1. Groeit het platform hard en zichtbaar? Ja, gestaag en groot
- Omzet per jaar (ARR): $250 miljoen in aug 2024 (DERDEN, https://siliconangle.com/?p=730977), $400 miljoen+ en 7.000+ klanten in sep 2025 (DERDEN, persbericht Grafana, https://grafana.com/about/press/2025/09/30/grafana-labs-surpasses-400m-arr-and-7000-customers-gains-new-investors-to-accelerate-global-expansion/), geschat $605 miljoen in aug 2026, groei ±37% per jaar (DERDEN, https://sacra.com/c/grafana-labs/).
- 10.000+ organisaties op Grafana Cloud (DERDEN, persbericht 20 okt 2026). 77.735 GitHub-sterren voor grafana/grafana (DERDEN, https://repos.ecosyste.ms/api/v1/hosts/GitHub/repositories/grafana%2Fgrafana). Gesprekken over geld ophalen tegen $9 miljard in feb 2026 (DERDEN, SiliconANGLE), niet bevestigd dat de ronde rond is.
- Motor: observability en AI-monitoring groeit; Grafana is de standaard voor dashboards. Dit is geen hype maar een volwassen bedrijf dat hard groeit. Minder explosief dan een jong platform, wel veel zekerder.

## 2. Is de winkel jong? Ja, drie weken
- Marketplace algemeen beschikbaar 20 okt 2026 (GEZIEN, https://grafana.com/press/2026/10/20/marketplace-ga/). Founding partners konden zich tot 30 sep aanmelden (DERDEN, https://community.grafana.com/t/become-the-founding-partner-of-grafana-marketplace/164428).
- Eigen telling via de open API (GEZIEN, `data/grafana-plugins-meet.py`, 8 nov): 388 plugins in de catalogus, waarvan **38 betaald in de marketplace**: 31 koppelingen, 4 apps, 3 panelen. Makers: Crest Data 25, Kenso 4, Integration Plumbers 4, en Phenisys, Helin, Antreklabs, UBICA, Ridgeline elk 1.
- 81 nieuwe plugins in 2026 in de hele catalogus (GEZIEN); betaalde komen er sinds juli bij, ±5 tot 10 per maand (GEZIEN, aanmaakdatums).

## 3. Kan er betaald worden? Ja, ingebouwd
- Proef van 14 dagen met één klik, maandabonnement op de rekening van Grafana Cloud, Grafana doet de facturatie, de maker de support (GEZIEN, persbericht; DERDEN, https://grafana.com/blog/grafana-marketplace).
- Prijzen per actieve gebruiker per maand, uit het veld `prices` van de API (GEZIEN, bijvoorbeeld https://grafana.com/api/plugins/kensobi-spcchartpro-panel): Kenso-panelen 0,99 en 10, Proxmox en AVEVA 5, Integration Plumbers 9 tot 15, Crest Data 15 tot 45, Phenisys Teams 99. Valuta niet vermeld, dollar (GOK).
- Wat we niet weten: de **afdracht** (alleen "revenue share", percentage niet openbaar), en of een eenmanszaak wordt toegelaten. Er is een Marketplace Partner Agreement nodig, aan te vragen via plugins-marketplace@grafana.com; het blog bij de lancering noemt "independent developers and systems integrators" als doelgroep (GEZIEN, https://grafana.com/blog/grafana-marketplace), maar het persbericht spreekt alleen van "verified partners" (https://grafana.com/legal/plugins/ voor de regels). Plichten: kritieke lekken binnen 7 dagen, ernstige binnen 30 dagen dichten.
- Alleen Grafana Cloud en Enterprise, niet de gratis zelf-gehoste versie (DERDEN, https://grafana.com/legal/plugins/). Upsell vanuit een gratis plugin kan "in de eerste fase" niet (DERDEN, community-link hierboven).
- Rekenvoorbeeld (GOK): een paneel van $3 per actieve gebruiker bij 30 organisaties met elk 10 gebruikers is $900 per maand bruto. Hoeveel organisaties betalen is volkomen onbekend.

## 4. Is er vraag te zien? Ja, voor grafieken die Grafana zelf niet heeft
Duimpjes op GitHub-wensen (DERDEN: door de onderzoeker via de zoek-API gemeten, door de controleur niet opnieuw te openen):
- Combinatiegrafiek staaf en lijn: 131 (https://github.com/grafana/grafana/issues/7949). Let op: voor tijdreeksen zit dit al in de kern (per reeks lijn, staaf of punten, tweede as, via overrides); het ontbreekt voor categorie-data zonder tijdas. Gestapelde groepen in een staafdiagram: 71 (https://github.com/grafana/grafana/issues/86868).
- Box plot: 107 (https://github.com/grafana/grafana/issues/3227), open sinds 2015.
- Koppeling Azure-kosten: 72 (https://github.com/grafana/grafana/issues/73443). DuckDB: 62 (https://github.com/grafana/grafana/issues/80948).
- De BI-panelen van Volkov Labs (Business Charts 15,6 miljoen downloads, Business Text 15,4 miljoen, GEZIEN in de API). Volkov werd in sep 2025 overgenomen; Grafana nam het onderhoud in jan 2026 over en verlengde dat tot eind 2026, "best effort", en "evaluates the right long-term support for each one" (GEZIEN, https://grafana.com/blog/business-intelligence-plugins-for-grafana-a-support-update). Business Charts wordt wel actief bijgewerkt (versie 7.3.0 op 3 nov 2026, DERDEN via controleur). Grafana kan dus zelf de opvolger worden; "opvolger van Business Charts" is geen vaste belofte. Klanten bouwen daarmee panelen die de standaardpanelen niet kunnen.

## 5. Is de eerste plek te pakken? Ja, in betaalde panelen
| Categorie in de marketplace | Nu | Sterkte |
|---|---|---|
| Betaalde panelen (grafieken) | 3 van Kenso (SPC Chart PRO 5 downloads, Box Plot $0,99 met 12, Bullet 13; GEZIEN) | leeg aan aanbod, maar ook nog geen kopers |
| Gratis concurrenten | Business Charts (ECharts, 15,6 miljoen, kan alles met eigen JavaScript), Plotly-panelen van ae3e (15,9 miljoen, sinds 2021 stil) en nline (1,6 miljoen) | sterk voor wie JavaScript schrijft |
| Koppelingen voor beveiliging en netwerk | 25 van Crest Data | vol, groot bedrijf, niet onze kant |
| Apps | 4, verspreid | dun |

"Leeg" betekent hier deels "niemand koopt nog" in plaats van "niemand begonnen". Waarom wij beter kunnen: Dortus bouwt snel en mooi (Daan), en panelen draaien in de browser zonder dat wij servers of klantgegevens hoeven te beheren. Het voorbeeld van Kenso laat het risico zien: het gratis SPC-paneel heeft 88.259 downloads, de PRO-versie 5. Bereik zet nog niet vanzelf om in verkopen (GEZIEN).

## Risico en waaraan je ziet dat het stokt
- Grafana bouwt de wens zelf in de standaard (box plot of combinatiegrafiek in de kern). Teken: een PR of release-notitie in grafana/grafana.
- Te weinig kopers: marketplace-plugins hebben nu 4 tot 13 downloads, op twee na (Meraki 8.121, Teams 3.358; GEZIEN). Teken: bij de herhaalmeting rond 8 dec nog steeds bijna geen downloads voor nieuwe betaalde panelen.
- Toelating: Grafana laat alleen gekeurde partners toe. Teken: antwoord op de aanvraag is nee, of de afdracht is hoger dan 30%.
- Supportplicht en zakelijke kopers vragen meer dan een hobby-plugin.

## Categorie en eerste productidee
Categorie: **betaalde grafiekpanelen voor zakelijke dashboards**. Eerste product: een paneel voor bedrijfsgrafieken op categorie-data die Grafana niet heeft (combinatie staaf en lijn op categorieën, gestapeld en gegroepeerd tegelijk, box plot, pareto), opvallend mooi en in te stellen zonder JavaScript, met support. De waarde zit in "zonder code, mooi en ondersteund", niet in de soorten grafieken: met JavaScript kan Business Charts het gratis. Gratis basis in de gewone catalogus voor bereik, PRO in de marketplace (proef 14 dagen, ±$2 tot $3 per actieve gebruiker, GOK).

## Stap voor Thijs
Mail naar plugins-marketplace@grafana.com om de voorwaarden te vragen: afdracht, of een kleine Nederlandse onderneming wordt toegelaten, en de Partner Agreement. Dat is een bericht onder zijn naam, dus ik zet de tekst op `organisatie/lijst-thijs.md`. Zonder dat antwoord geen bouwbesluit.

## Wat ik niet kon meten
Afdracht, toelatingseisen, aantal Cloud-gebruikers met de gratis laag, hoeveel er echt betaald wordt per plugin (downloads zijn geen abonnementen). Herhaalmeting: `python3 data/grafana-plugins-meet.py` rond 8 dec (aantal betaalde plugins en panelen, downloads van marketplace-plugins).

## Cijfer en advies
5 van 10. Nog niet klaar. Vraag 2 en 3 zijn sterk (winkel drie weken oud, betalen ingebouwd), vraag 1 is groot en zeker maar geen jonge explosie, vraag 5 zwakker dan het lijkt (gratis alternatieven, de enige betaalde panelen verkopen nog niet). Wordt een 6 of 7 als: de voorwaarden passen (afdracht 30% of minder, eenmanszaak toegelaten) en de herhaalmeting rond 8 dec laat zien dat betaalde panelen of kleine makers abonnees krijgen (downloads van Kenso-panelen en nieuwe betaalde panelen stijgen duidelijk). Wordt een 3 als Grafana zelf een opvolger van Business Charts aankondigt of geen kleine makers toelaat.

## Nagekeken
Controleur (agent) 8 nov: steekproef van 5 cijfers klopt; 6 correcties verwerkt (combinatiegrafiek bestaat voor tijdreeksen, tijdlijn Volkov en actief onderhoud van Business Charts, Plotly en Kenso als concurrenten, bron van "independent developers" verbeterd en zelf nagekeken, duimpjes als DERDEN, cijfer 6 naar 5).
