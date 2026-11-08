# Meta Horizon Store (apps en games voor Meta Quest)

Vera, 8 nov 2026, run 08:31 (UTC). Zelf toegevoegd.

## Advies: nee voor nu, cijfer 4

In de Quest-winkel wordt echt verdiend, ook door kleine makers met betaalde spellen: een op de acht nieuwe betaalde titels van mei t/m aug 2026 haalt naar schatting $10.000 netto of meer in 3 tot 6 maanden. Maar dat geld zit bijna helemaal bij spellen in 3D, en precies daar past Dortus slecht: we hebben geen headset om te testen, geen 3D-kunst, en de echte app is niet in GitHub Actions te testen. In het deel dat wel bij ons past (de categorie Apps: hulpprogramma's, mixed reality, productiviteit) haalt een nieuwe betaalde app mediaan 0 beoordelingen en maar 1 van de 126 haalt er 100. Daarbij krimpt de markt: minder headsets verkocht, duurdere headsets sinds april 2026 en bezuinigingen bij Meta.

Wat het zou veranderen: Dortus kiest bewust voor spellen en Thijs koopt een Quest om te testen. Dan is het voor spellen een 5, en de moeite van een tweede meting waard (welke soorten spellen van kleine makers boven de 50 beoordelingen komen).

## Nagekeken
Controleur akkoord met nee voor nu, cijfer 4 (een 3 vond hij ook te verdedigen, een 5 niet): alle tellingen herberekend en gelijk, geen dubbelen, 15 van 15 titels live gelijk op vrdb.app, 4 bronnen gecontroleerd. Correcties verwerkt: makers geteld op id, 13 titels zonder prijs, juiste auteur en spreiding bij de vuistregel, beperking bij GameDiscoverCo, vertekening door de prijs van nu, drukte als piek in plaats van trend.

## Waarom gekozen
- Groot gesloten platform met betalen in de winkel, sinds aug 2024 zonder selectie (App Lab is opgegaan in de gewone winkel), dus open voor kleine makers.
- Meta zegt dat 2025 het jaar met de meeste gebruikers ooit was en dat ruim 100 titels meer dan $1 miljoen haalden (DERDEN, UploadVR 17-03-2026).

## Hoe gemeten
- meta.com zelf is niet te lezen: de sitemaps geven 403 en de winkelpagina's geven een foutpagina aan automatische lezers. Dat respecteren we.
- Wel te lezen: **vrdb.app**, een open database die de hele Quest-winkel volgt (robots.txt staat het toe). De lijst "new releases" geeft per pagina 50 titels met releasedatum, aantal beoordelingen (ratings), prijs in dollars, maker en soort. Totaal in de winkel: 20.104 titels (GEZIEN, numTotal, gelijk aan de sitemap van vrdb).
- Opgehaald: alle 6.850 titels van 7 nov 2026 terug tot eind sep 2025 (GEZIEN, 137 pagina's, data/meta-horizon-vrdb-2026-11-08.jsonl, scripts data/meta-vrdb-haal-script.py en meta-vrdb-analyse-script.py).
- Let op: de prijs is de prijs van nu (een titel die later gratis werd telt als gratis). Het aantal beoordelingen is het totaal tot 8 nov. 13 titels hebben geen prijs in de data (meestal verwijderd, 0 beoordelingen) en tellen als gratis; dat verandert de cijfers bijna niet.

## Cijfers

### Drukte (GEZIEN)
Nieuwe titels per maand: dec 2025 t/m aug 2026 ±440 tot 560, sep 2026 764, okt 2026 797. Dat is een piek in sep en okt (150 tot 240 per week); de laatste twee weken zijn het er weer ±90 per week, zoals midden 2026. Of dat een piek voor de feestdagen is of dat vrdb nieuwe titels later opneemt, weet ik niet. Van de 1.873 titels uit mei t/m aug zijn er 1.334 makers (geteld op developer_id), 1.070 met maar één titel.

### Bereik (GEZIEN): beoordelingen van nieuwe titels, mei t/m aug 2026 (3 tot 6 maanden oud)

| Groep | n | mediaan | 0 | 10+ | 50+ | 100+ |
|---|---|---|---|---|---|---|
| Alles | 1.873 | 2 | 32% | 26% | 8,1% | 5,6% |
| Gratis | 1.380 | 3 | 27% | 31% | 9,8% | 6,8% |
| Betaald | 493 | 1 | 46% | 14% | 3,4% | 2,0% |
| Betaald, Games | 366 | 1 | 39% | 17% | 4,1% | 2,5% |
| Betaald, Apps | 126 | 0 | 68% | 6% | 1,6% | 0,8% |
| Betaald nov 2025 t/m feb 2026 (9 tot 12 mnd oud) | 507 | 1 | 34% | 22% | 11,6% | 8,3% |

- Mediaanprijs betaald (mei t/m aug): $6,99. 37% van de betaalde titels is early access.
- Gratis met add-ons of in-app aankopen: 223 titels, mediaan 6 beoordelingen, 32 halen 100+.
- Beste nieuwe betaalde titels mei t/m aug: Gas N Cars VR (Yorf Studio, $13,99, 8.856), Ghosts of Tabor: LEGACY (1.349), I Am Janitor (746), Roboquest VR (588, port van een bekend pc-spel). Beste betaalde App: RetroGameDev VR ($18,99, 109).

### Van beoordelingen naar installs en geld
- Vuistregel: op Quest komt mediaan **1 beoordeling per ±110 verkochte exemplaren**, soms lager (75), soms 250 of meer (DERDEN, onderzoek van Cassia Curran, aangehaald door Ryan Rigney in Push to Talk, 17-01-2025, https://www.pushtotalk.gg/p/are-random-vr-games-making-100-million). Die regel komt van titels met veel verkoop; of hij klopt voor titels met 1 tot 10 beoordelingen weet ik niet (GOK).
- Toegepast op de betaalde titels mei t/m aug, met 30% afdracht aan Meta: mediaan ±$300 netto in totaal, 25% haalt ±$2.000 of meer, 12% ±$10.000 of meer (GOK, gerekend met de vuistregel). Voor betaalde Apps ligt dat veel lager: 68% heeft nog geen enkele beoordeling.
- Vertekening door de prijs van nu: in oudere maanden is ±68 tot 74% gratis, in sep 57% en okt 50%. Betaalde titels die later gratis werden tellen nu als $0 (schatting te laag), kortingen worden genegeerd (schatting te hoog). Welke kant het netto op gaat is onbekend.
- GameDiscoverCo: de meeste nieuwe spellen in 2025 buiten sim, sport, schieten en apenspellen verkochten "a few thousand units at best"; Quest-gebruikers zitten ±70% van hun tijd in gratis spellen (DERDEN, https://newsletter.gamediscover.co/p/what-happened-to-vr-games-in-2025, 13-01-2026).
- Meta: winkelomzet 2025 "up very slightly", in-app aankopen +10%, Horizon+ betaalde makers bijna $20 miljoen (DERDEN, https://www.uploadvr.com/meta-says-2025-saw-record-quest-users-more-than-100-apps-made-over-1-million/, 17-03-2026). Totale winkelomzet blijft steken op "meer dan $2 miljard", hetzelfde getal als in 2023 (DERDEN, https://roadtovr.com/meta-quest-store-revenue-milestone-2025-update/, 04-04-2025).
- Een solo-maker met omzet van na 2024 vond de onderzoeker niet; Reddit en mixed-news.com blokkeerden.

### Regels en vindbaarheid (DERDEN)
- Afdracht 30% (geen verlaging gevonden in 2025 en 2026). Officiële regels op developers.meta.com niet gelezen.
- App Lab opgegaan in de winkel, aug 2024; keuring alleen op techniek en inhoud (https://www.uploadvr.com/quest-app-lab-merged-into-meta-horizon-store/, 23-08-2024). Keuring tot ±2 weken.
- Bijna twintig studio's meldden in feb 2025 dalende verkoop door de vloed aan titels en weinig zichtbaarheid (https://www.uploadvr.com/from-quest-to-horizon-how-metas-shifting-priorities-are-affecting-developers/, 05-02-2025). Kopers kopen vooral vlak na het uitpakken en rond Black Friday en Kerst; nieuwe kopers komen via TikTok, YouTube en streamers (https://www.androidcentral.com/gaming/virtual-reality/gdc-2025-oculus-publishing-head-challenges-meta-criticism-on-quest-store-profitability, 20-03-2025).
- Meta draait de Horizon-voorrang terug: Navigator wordt het startscherm (UploadVR 27-01-2026), Horizon Worlds stopt met nieuwe VR-werelden na 15 juni 2026 (Android Central 19-03-2026).

### Markt (DERDEN)
- ±1,7 miljoen Quests geleverd in de eerste drie kwartalen van 2025, 16% minder (IDC via een tweedehands bron, tech-insider.org). Headsets $50 tot $100 duurder sinds 19 april 2026, Quest 3S nu $349 (Game Informer 16-04-2026).
- Reality Labs: ±10% banen weg in jan 2026, drie eigen VR-studio's dicht (Engadget 13-01-2026).

## Voordelen
- Betalen in de winkel, geen selectie meer, en kleine makers met betaalde spellen verdienen aantoonbaar (14% van de nieuwe betaalde titels haalt 10+ beoordelingen, dat is naar de vuistregel ±1.000+ verkocht).
- Eigen meting mogelijk via vrdb.app, ook voor een herhaalmeting.

## Nadelen
- Het geld zit in 3D-spellen; Dortus heeft geen headset, geen 3D-kunst en kan de echte app niet in GitHub Actions testen.
- De categorie die bij ons past (Apps) doet het slecht: betaald mediaan 0, 0,8% haalt 100+.
- Krimpende verkoop van headsets, stilstaande winkelomzet, bezuinigingen bij Meta.
- Druk: ±440 tot 560 nieuwe titels per maand, met een piek van ±800 in sep en okt 2026.
- Een ontwikkelaarsaccount bij Meta moet Thijs zelf aanmaken en laten verifiëren.

## Eerste idee als we het toch doen
Een klein, goedkoop mixed reality-spel of speeltje voor tieners (prijs $4,99 tot $6,99, of gratis met add-ons), lancering vlak voor Black Friday, met korte filmpjes voor TikTok. Alleen met een Quest om te testen.

## Wat nog gemeten kan worden
- Of de vuistregel van 110 ook klopt bij kleine titels (alleen met cijfers van makers zelf).
- Over 4 weken de lichting sep en okt opnieuw met data/meta-vrdb-haal-script.py (stijgen de beoordelingen na Black Friday?).
