# Microsoft Store (Windows-apps)

Onderzocht door Vera op 8 nov 2026, run 04:32 UTC. Eigen meting plus een onderzoeker en een controleur.

**Advies: nee voor nu. Cijfer 3.**

Kort: beginnen kost niets, de afdracht is laag en er zijn veel gebruikers. Maar nieuwe betaalde apps laten geen enkel teken van bereik zien, er is geen kleine maker die omzet deelt, en de winkel loopt sinds dit voorjaar vol met nieuwe apps (±11.000 per maand). Bereik en geld zijn allebei niet aangetoond.

## Hoe gemeten
- Sitemap van apps.microsoft.com (robots.txt staat alles toe): 157.032 productpagina's, waarvan 52.676 met een XP-ID (win32-apps, die tonen geen uitbrengdatum).
- 4.000 willekeurige pagina's gelezen (VS-pagina, hl=en-US, gl=US): uitbrengdatum, aantal ratings (alleen VS), prijs, add-ons, soort. 3.987 bruikbaar na het opnieuw ophalen van 435 mislukte pagina's. Data: `data/msstore-steekproef-2026-11-08.jsonl`, scripts `data/msstore-haal-script.py` en `data/msstore-analyse-script.py`.
- Alleen apps (mediaType "Apps"), geen games. Alleen 9-ID's, want XP-ID's hebben geen datum.

## Belangrijk om de cijfers te lezen
- De winkel toont geen downloads, alleen ratings, en **per land**. GEZIEN.
- **Onder 5 ratings per land toont de winkel 0.** In de steekproef komen 1 tot 4 nooit voor, de controleur vond apps met "0" die via de ratings-API wel 1 of 2 Amerikaanse reviews hebben. GEZIEN.
- IJkpunt (DERDEN, KDE e.V. met Partner Center-schermen, kate-editor.org 3 jun 2025): wereldwijd 2 tot 4 ratings per 1.000 installs, alleen de VS ±0,3 tot 0,5 per 1.000. Gratis open-source apps van één uitgever; voor betaalde apps onbekend.
- Dus: 5 of meer VS-ratings past bij grofweg 10.000+ installs (gratis app, GOK). Alles daaronder is onzichtbaar. De mediaan is niet te meten, alleen de kop.

## Cijfers
| Lichting (apps, geen games) | Alle | met 5+ VS-ratings | Betaald | betaald met 5+ |
|---|---|---|---|---|
| 2024 | 94 | 16 (17%) | 23 | 5 |
| jan t/m aug 2025 | 103 | 10 (10%) | 37 | 2 |
| sep 2025 t/m feb 2026 | 134 | 10 (7%) | 43 | 1 |
| mrt t/m apr 2026 | 87 | 2 | 25 | 0 |
| mei t/m aug 2026 (3 tot 6 maanden oud) | 325 | 3 (1%) | 104 | **0** |
GEZIEN, eigen steekproef. Kleine groepen, maar in elke recente lichting bijna nul.

- **Bereik:** van de lichting mei t/m aug 2026 haalt 1% de grens van 5 VS-ratings, van de betaalde 0 van 104. Mediaan niet te meten. GEZIEN.
- **Wie wel bereik haalt:** goedkope algemene hulpprogramma's van app-studio's, zoals AI Voice Changer ($1,39, okt 2025, 381 VS-ratings), Pro Unzip & RAR Extractor ($1,39, jan 2025, 349), Torrent Download Manager+ ($4,89, 81), Mirror phone to PC ($4,69, 45). GEZIEN. Omzet onbekend.
- **Drukte:** okt 2026 283 nieuwe apps op 2.699 pagina's met een 9-ID, dus ±11.000 nieuwe apps per maand in de hele winkel (GOK op steekproef, plus nog onbekend aantal win32-apps). Dat was ±1.000 per maand in 2024. Een deel van die stijging komt doordat oude apps uit de sitemap verdwijnen, maar de golf sinds juli 2026 is duidelijk (feb 22, jun 59, aug 126, okt 283 in de steekproef). Waarschijnlijk door de gratis registratie (individueel sinds sep 2025, bedrijven sinds 7 mei 2026) en AI. GEZIEN (telling), DERDEN (registratie).
- **Geld:** afdracht 15% voor apps, 12% voor games, 0% bij in-app-aankopen met eigen betaalsysteem (App Developer Agreement v8.11, 17 apr 2026). DERDEN. Gebruikers kunnen dus betalen. Maar de onderzoeker vond **geen enkele kleine maker** die sinds 2023 Store-omzet deelt (HN, dev.to, Zenn, Qiita, Hackernoon, websearch). Alleen Krita (een team) schreef in 2023 dat een hogere prijs "eerst de inkomsten verhoogde", zonder bedragen. DERDEN.
- **Gebruikers:** Microsoft noemt steeds "meer dan 250 miljoen maandgebruikers" (mei 2025 t/m mei 2026). DERDEN.
- **Vindbaarheid:** zoeken in de Store (sinds 2025 op betekenis), installeren vanuit Windows Search, persoonlijke startpagina, betaalde App Campaigns, winget. Een Japanse solo-maker (AuText, gratis, geen reclame) kreeg ±50 downloads in de eerste maand en later tot ±50 per week. DERDEN (zenn.dev, 2023).
- **Past het bij ons:** ja, technisch. Een Windows-app (MSIX) is in 1 tot 2 weken te bouwen en via GitHub Actions te verpakken. Keuring tot 3 werkdagen. Geen verbod op met AI gemaakte apps. Thijs moet wel een account maken met identiteitsbewijs en selfie (gratis). DERDEN.

## Voordelen
- Gratis beginnen, lage afdracht, 0% met eigen betaling.
- Groot publiek dat in de winkel zoekt.
- Technisch past het goed bij wat wij kunnen bouwen.

## Nadelen
- Nieuwe betaalde apps laten geen meetbaar bereik zien (0 van 104).
- Geen enkel openbaar geldbewijs van kleine makers.
- Sinds juli 2026 een stortvloed aan nieuwe apps, vaak simpele AI-apps; de lat om op te vallen stijgt snel.
- De winkel toont te weinig om een product goed te volgen (geen downloads, ratings per land, drempel van 5).

## Eerste idee als we het toch doen
Een klein betaald hulpprogramma in een hoek waar mensen zoeken en weinig goede apps staan (bijvoorbeeld een nette systeemvak-tool), freemium met eigen betaling (0% afdracht). Alleen als bijproduct, niet als hoofdplatform.

## Wat nog gemeten kan worden
- Over 4 weken dezelfde scripts draaien: groeit de golf door, en krijgen apps uit sep en okt ratings?
- Ratings in meer landen optellen (let op: per land de eigen taal gebruiken, hl en gl samen, anders tel je veel te weinig).
- Een maker vinden die Partner Center-cijfers van een betaalde app deelt. Zonder dat blijft geld een gat.

## Controle
Controleur akkoord met de kern: 15 van 15 records live gelijk, regex pakt het goede veld, drempel van 5 bevestigd. Correcties verwerkt: 433 mislukte pagina's opnieuw opgehaald (in de eerste telling stonden ze als 0), games eruit gefilterd (productType "Application" bevat ook games), schatting nieuwe apps per maand verlaagd van 11.800 naar ±11.000 met de juiste noemer, label "0 ratings" heet nu "onder 5".
