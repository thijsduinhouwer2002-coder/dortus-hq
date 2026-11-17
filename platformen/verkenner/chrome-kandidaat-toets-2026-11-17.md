# Toets van Kais kandidaten 1 en 2 (Vera, 17 nov 2026, run 07:31 NL)

Opdracht hoofdchat 17 nov 06:50: Kai helpen voor de keuze van ±10:45. Kai heeft zijn vijf kandidaten al staan (`platformen/chrome/kandidaten.md`). Ik heb niet opnieuw gedaan wat hij en Chris al maten, maar gezocht naar wat de volgorde kan omgooien: (1) doet Google het zelf al of binnenkort, (2) groeit het veld of staat het stil, (3) verdient iemand aantoonbaar met een agenda-extensie, (4) bewegen de 80.000 verdwenen Revolver-gebruikers ergens heen. Data: `data/chrome-agenda-bulk-veld-2026-11-17.tsv`.

## Kort
- **Google doet het niet zelf, en heeft niets aangekondigd.** Alle 318 berichten met label Google Calendar op Workspace Updates (2007 tot 16 nov 2026, waarvan 150 sinds aug 2021; de controleur las de oudere 168) doorzocht op bulk, multiple events, select multiple, duplicate: geen enkel bericht over afspraken in bulk selecteren, verplaatsen of verwijderen (GEZIEN, feed `workspaceupdates.googleblog.com/feeds/posts/default/-/Google%20Calendar`). Het gat staat; dat er geen plan is, weten we niet, alleen dat er niets is aangekondigd.
- **Het agenda-bulkveld groeit, maar is klein en grof gemeten.** De vijf echte bulktools hadden op 14 aug 2026 samen ±2.900 gebruikers, nu ±5.200 (+80% in 3 maanden; +1.000 daarvan is één afgerond getal, de exacte getallen worden vooral door SUPER gedragen). SUPER (Move Many Events, $29 per maand) ging van 125 naar 923. Tegenvoorbeeld: GCalPlus, de grote agenda-hulp, zakte van 70.000 naar 60.000. Bij kandidaat 2 (tabbladen rouleren) bewoog bijna niets.
- **Geldbewijs voor agenda-extensies blijft dun.** De enige agenda-extensie op TrustMRR, Add More Colors to Calendar (6.000 gebruikers), haalde $7,98 in de laatste 30 dagen en $921 in 12 maanden, maar dat zit bijna helemaal in dec 2025 ($459) en jan 2026 ($148); sindsdien elke maand $7,98 (GEZIEN, Stripe via TrustMRR; de 6.000 gebruikers is een opgave van de eigenaar). Dat is kleur, geen werkgereedschap, maar het temt de verwachting.
- **Een kleine maker kan de Calendar-OAuth halen.** GCalPlus (kleine Franse maker, 70.000 gebruikers op 14 aug, nu 60.000, Featured) laat gebruikers met "Connect" toegang geven tot hun agenda. Het kan dus. Tegelijk is GCalPlus de grootste die bulk er zo bij kan zetten (heeft al zoeken in afspraken en "Multiple Copy").
- **Advies aan Kai:** volgorde blijft. Kandidaat 1 wordt iets sterker (groeiend maar klein veld, niets aangekondigd door Google, jonge en zwakke concurrenten), het geldbewijs blijft zwak. Kandidaat 2 wordt zwakker: de verdwenen gebruikers zoeken niet massaal een opvolger.

## 1. Doet Google het zelf? (GEZIEN)
Feed met de 150 Calendar-berichten van Workspace Updates van 18 aug 2021 tot 16 nov 2026 doorzocht op titel en tekst (de feed geeft er 150 per keer); de controleur las ook de 168 oudere (2007 tot jul 2021): niets. Treffers gingen alleen over Meet-hardware in bulk (9 mrt 2026), vergadercodes bij meerdere afspraken en een recap over Classroom. Niets over bulk in de agenda zelf. Beperking: Google kondigt niet alles vooraf aan, en de app voor gewone accounts kan stil iets krijgen (GOK, klein risico).

## 2. Groeit het agendaveld? (GEZIEN live 17 nov, DERDEN Palant-dataset 14 aug)

| Extensie | Aangemaakt | 14 aug 2026 | 17 nov 2026 | Sterren | In-app |
|---|---|---|---|---|---|
| Event Multiselect for Google Calendar | 30 jan 2025 | 2.000 | 3.000 | 2,7 (23) | nee |
| Google Calendar Bulk Edit | 27 dec 2025 | 644 | 1.000 | 3,0 (6) | nee |
| SUPER: Move Many Events (Tryotrix, Zwitserse bijlesschool; in aug heette hij "Bulk Edit, Move Events & Desktop - Pro Extension for Google Calendar") | 22 jan 2026 | 125 | 923 | 4,7 (26) | ja, $29 p/m |
| Calendar Bulk Delete (Columbia University) | 30 sep 2025 | 80 | 229 | 3,8 (16) | nee |
| Calendar Bulk Delete (tree.fm) | 13 apr 2025 | 36 | 37 | geen | nee |
| Calendar Bulk (verwijderen, verplaatsen, dubbele) | na aug 2026 | niet in dataset | 28 | geen | ja |
| Calendar Bulk Select / Calendar Select | sep, okt 2026 | niet in dataset | 3 en 5 | geen | nee |

- Samen (eerste vijf): ±2.885 op 14 aug, ±5.189 op 17 nov. Alle bulktools zijn jonger dan 2 jaar en gemaakt door kleine makers of een universiteit. Nergens een sterke nummer één (harde regel: niet overslaan).
- Let op: de winkel rondt af (1.000, 2.000, 3.000), dus de groei van de grote twee is grof. SUPER en de Columbia-tool tonen exacte getallen.
- Dat SUPER in 3 maanden 7 keer groeide met een betaalde laag en 4,7 sterren, is het beste teken in het veld. Waarom hij groeide (betrouwbaarder, nieuwe naam, advertenties, plek in de zoekresultaten) weten we niet (GOK).
- Vraag op Reddit is mager: r/GoogleCalendar heeft sinds 2024 maar twee posts met "delete multiple events" in de titel (feb 2025, 1 punt, 2 en 6 reacties; DERDEN, Arctic Shift). De vraag komt dus vooral via de zoekbalk en Google zelf, niet via een community.

## 3. Wordt er betaald? (GEZIEN)
- TrustMRR, de enige Calendar-extensie in de dump van 8 nov plus live profiel 17 nov: Add More Colors to Calendar, 6.000 gebruikers (opgave eigenaar), $7,98 (30 dagen), $23,94 (3 maanden), $921 (12 maanden), $9.592 alles samen. Per maand: dec 2025 $459, jan 2026 $148, daarna $7,98. Dus nu ±$96 per jaar. De pagina meldt ook "Current MRR $40.87" met 13 abonnementen, niet consequent. Eigenaar: "0 marketing, organic webstore traffic", nr. 2 op de zoekterm.
- SUPER: prijs gezien ($29 p/m, $228 p/j, bij Kai), aantal betalers onbekend.
- GOK, verwachting voor ons: bij ±1.000 gebruikers na 3 maanden (dan zijn we met SUPER en Event Multiselect de grootste drie) en 1 tot 2% die $39 per jaar betaalt: $400 tot $800 per jaar. Dat is optimistisch naast de ±$8 per maand hierboven; het hangt aan een teamprijs die werkt. Eerste euro's ja, €100 per maand pas met meer gebruikers of een hogere prijs voor teams.

## 4. Kandidaat 2: zoeken de 80.000 Revolver-gebruikers een opvolger? (GEZIEN live 17 nov, DERDEN Palant 14 aug)
Revolver ging op 31 aug weg met nog 80.000 gebruikers. Groei van de opvolgers sinds 14 aug:
- Revolver Tab Rotator (jan 2026): 1.000 naar 3.000. TabCycle (jan 2025): 1.000 naar 2.000. Tab Rotator (dec 2025): 442 naar 805. Tab Rotation: 182 naar 209.
- Ongewijzigd: Auto Tab Switcher 30.000, Tab Rotate 20.000, goRotate, TabTurner, 3-2-1 Revolver, Auto Refresh & Switch Tabs (alle 10.000), TabRotator en Tabs Rotator (3.000), FreeTabSwitcher 2.000. Twee kleintjes gingen omlaag.
- Samen zichtbaar: ±+3.400 gebruikers erbij, tegenover 80.000 die verdwenen. Binnen de afgeronde emmers (10.000, 20.000) kan groei verstopt zitten, maar ook dan is het geen stroom. Waarschijnlijk staan veel schermen nog op een oude browser of beheerde Chrome-versie, of zijn ze overgestapt op signage-software (GOK).
- Gevolg: de MV2-stop heeft voor tabbladen rouleren geen golf zoekers in de winkel gezet. Kandidaat 2 blijft "snelst live", maar is als markt zwakker dan het verlies van 200.000 doet denken.

## Advies voor Kai en de keuze van 10:45
1. Kandidaat 1 (Agenda in bulk) bovenaan houden. Nieuw bewijs: niets aangekondigd door Google, klein veld +80% in 3 maanden (grof), betaalde nieuwkomer groeit 7x.
2. Neem in het plan op dat GCalPlus (60.000, Featured) bulk kan toevoegen; tegenzet is snel zijn en op de dingen gaan zitten die GCalPlus niet doet (dubbele afspraken opruimen, zoeken en vervangen in titels).
3. Reken niet op snel geld: de enige agenda-extensie met gemeten omzet haalt nu ±$8 per maand ($921 in 12 maanden, vooral eind 2025). De teamprijs (meer agenda's, gedeelde agenda's opruimen) is de plek voor hogere bedragen.
4. Kandidaat 2 alleen als snelle tweede: bouwen kost weinig, maar verwacht geen opvolgersgolf.

Nagekeken door een controleur (17 nov ±07:10 UTC): winkelcijfers, Palant-cijfers en sommen klopten; aantal blogberichten, TrustMRR-bedrag en drie te stellige zinnen zijn hierboven verbeterd.

## Wat ik niet kon meten
- Reviews per extensie (de winkel laadt ze met een script, niet via curl): klachten over Event Multiselect alleen uit Chris' meting.
- Zoekvolume in de winkel: Google geeft het niet. Hoe het wel kan: na de lancering de vertoningen in het ontwikkelaarsdashboard (staat bij Thijs).
- Aantal betalers van SUPER.

---

# Deel 2: kandidaten 3, 4 en 5 (Vera, run 08:31 NL, 07:35 tot ±08:05 UTC)

Zelfde vragen als hierboven: doet Google (of een groot gratis product) het al, groeit het veld sinds 14 aug 2026, verdient iemand aantoonbaar. Werkwijze: zoekbalk van de winkel met drie zoektermen per kandidaat (eerste 10, GEZIEN 17 nov ±07:35 tot 07:45 UTC), en per gevonden extensie de stand op 14 aug 2026 uit de dataset van Palant (DERDEN, per ID opgehaald). Alles: `data/chrome-kandidaten-3-5-veld-2026-11-17.tsv`, scripts `data/chrome-zoek-ids-script.py` en `data/chrome-palant-aug-script.py`.

## Kort
- **Kandidaat 3 (Keep naar Markdown of Obsidian) valt eigenlijk af.** Obsidian doet het zelf, gratis: de officiële Importer-plugin heeft een knop "Google Keep (.zip)" voor de Takeout-zip (GEZIEN, obsidian.md/help/import/google-keep) en de Importer (alle bronnen samen, niet alleen Keep) is 1.926.030 keer gedownload (GEZIEN, community-plugin-stats.json van obsidianmd, 17 nov). Wie Keep naar Obsidian wil, krijgt dat in Obsidian zelf. De enige echte Keep-exporteur in de winkel groeide van 123 naar 175 gebruikers in 3 maanden. Geen geldbewijs.
- **Kandidaat 4 (autoplay) wordt zwakker.** Chrome zelf geeft gebruikers geen knop om video's te blokkeren en op chromestatus.com vond ik geen open voorstel (GEZIEN), dus het gat is echt. Maar de verdwenen gebruikers kwamen niet: de algemene stoppers gingen samen van ±25.000 naar ±16.000 (zonder Video Blocker, 10.000 naar 20.000, die de winkel alleen als "Block videos from playing" beschrijft; hoort hij erbij, dan staat het veld stil, ±35.000 naar ±36.000) (AutoplayStopper (MV3) van 20.000 naar 10.000). En ons idee (gratis met 3 sites, Pro voor onbeperkt) bestaat al: **Video Autoplay Stopper** (jan 2026, Pro via Lemon Squeezy) staat al 3 maanden stil op 2.000.
- **Kandidaat 5 (Google Foto's in bulk) is het enige van de drie dat groeit, en waar al betaald kan worden, maar is vol.** 18 Foto-tools in de zoekresultaten: samen 52.621 op 14 aug, 79.776 nu (+52%, grof door afgeronde emmers). 7 van de 18 hebben in-app aankopen. Duplicate Remover (met in-app) ging van 10.000 naar 20.000, Google Photos Downloader (in-app) van 10.000 naar 20.000. De enige Foto-tool op TrustMRR (SyncGP, back-up) haalde $1.420 alles samen en $0 de laatste 30 dagen (GEZIEN, dump 8 nov). Technisch blijft het zwak voor ons: werkt via de pagina, niet te testen zonder inloggen (Kai).
- **Advies:** de volgorde van Kai klopt. 3 kan van de lijst, 4 blijft een bereikproduct zonder geld, 5 is de enige met groei en betalende concurrentie, maar hoort niet bovenaan omdat wij het niet kunnen testen en het breekt bij elke wijziging van Google.

## 3. Keep naar Markdown of Obsidian (GEZIEN)
| Extensie | 14 aug 2026 | 17 nov 2026 | In-app |
|---|---|---|---|
| Keep to Markdown Export (feb 2026) | 123 | 175 | nee |
| KeepDown (jan 2025) | 0 | 160 | nee |
| Keep Web Clipper (feb 2026) | 570 | 542 | nee |
| markKeep, Markdown in Keep (2024) | 219 | 219 | nee |

- Doet een groot gratis product het: ja. Obsidian Importer, gemaakt door Obsidian zelf; de hulp-pagina beschrijft Takeout, "Deselect all", Keep kiezen, zip in de Importer. Beperkingen volgens Obsidian zelf: lijstjes worden plat (Keep exporteert geen inspringing) en herinneringen gaan niet mee. De inspringing zit niet in de Takeout-data, dus die kunnen wij ook niet terughalen. Herinneringen laat Obsidian weg omdat Obsidian ze niet kent; een eigen tool zou ze als tekst kunnen meenemen (GOK dat ze in de Takeout staan, niet nagekeken).
- Google zelf: 19 berichten met label Google Keep op Workspace Updates, geen enkel over export naar Markdown (GEZIEN, feed). Takeout blijft gratis.
- Wat wel betaald groeit, is AI-chats naar Obsidian (Claude to Obsidian 3.000 naar 4.000, Save ChatGPT to Obsidian 4.000 naar 5.000, beide met in-app). Dat is een andere markt en vol.
- Gevolg: geen gat. Iemand met Obsidian heeft het al gratis; iemand zonder Obsidian heeft waarschijnlijk weinig reden om Markdown te willen (GOK).

## 4. Autoplay stoppen (GEZIEN)
| Extensie (algemeen, niet alleen YouTube) | Gemaakt | 14 aug 2026 | 17 nov 2026 | Sterren aug, nu | In-app |
|---|---|---|---|---|---|
| AutoplayStopper (MV3) | aug 2025 | 20.000 | 10.000 | 3,76 naar 3,4 | nee |
| Disable HTML5 Autoplay (M3) | okt 2024 | 3.000 | 4.000 | 1,84 naar 1,8 | nee |
| Video Autoplay Stopper | jan 2026 | 2.000 | 2.000 | 4,58 naar 4,3 | ja, Pro |
| Autoplay Blocker | onbekend (laatste update 21 jul 2026) | niet in dataset | 79 | geen | nee |

- De YouTube-tools (alleen "volgende video" uitzetten) staan ook stil: Disable Autoplay for YouTube 20.000 naar 20.000, No Playlist Autoplay 8.000 naar 8.000. YouTube heeft daar zelf een schakelaar voor, dus dat deel telt niet als gat.
- Video Autoplay Stopper doet precies het freemium-plan: gratis overal blokkeren met 3 sites per lijst, Pro voor onbeperkt, jokertekens, per site kiezen en synchroniseren, abonnement via Lemon Squeezy (GEZIEN, winkelpagina). Hij staat stil op 2.000. Geen omzet bekend (niet op TrustMRR).
- Gevolg: zelfde patroon als Revolver. 200.000+ gebruikers verdwenen bij de MV2-stop (DERDEN, Palant-dataset, zie chrome-mv2-zonder-opvolger.md; niet opnieuw gemeten), maar ze zoeken niet in de winkel naar een opvolger (GOK: ze bleven op een oude browser, gingen naar uBlock Origin Lite met een filter, of naar Firefox, dat het zelf kan).

## 5. Google Foto's in bulk (GEZIEN)
| Extensie | Gemaakt | 14 aug 2026 | 17 nov 2026 | Sterren aug, nu | In-app |
|---|---|---|---|---|---|
| Google Photos Duplicate Remover | jun 2025 | 10.000 | 20.000 | 4,05 naar 4,0 | ja |
| Google Photos Downloader | feb 2026 | 10.000 | 20.000 | 5 naar geen | ja |
| Google Photos Delete Tool, Duplicate Finder | aug 2024 | 10.000 | 10.000 | 4,76 naar 4,6 | nee |
| Delete All Google Photos Extension | dec 2023 | 10.000 | 10.000 | 4,12 naar 3,7 | ja |
| Bulk Select Google Photos | nov 2024 | 4.000 | 5.000 | 4,30 naar 4,2 | nee |
| Delete Google Photos | apr 2025 | 2.000 | 3.000 | 5 naar 4,9 | nee |
| Bulk Edit Google Photos | mei 2026 | 611 | 1.000 | 4,85 naar 4,8 | ja |
| Google Photos Cleaner | nov 2025 | 0 | 1.000 | 3,66 naar 3,8 | ja |

- 18 Foto-tools in de resultaten, samen +52% in 3 maanden; drie die niet in de dataset van aug staan (11, 115 en 152 gebruikers), waarschijnlijk nieuw. Dit veld groeit wel, anders dan 3 en 4.
- Doet Google het zelf: de hulp-pagina over verwijderen noemt geen "alles selecteren" (GEZIEN, support.google.com/photos/answer/6128858). Op het web kun je wel een hele dag in één keer aanvinken (GOK, eigen kennis, niet nagekeken). Niets gezocht naar aankondigingen; Google Foto's valt niet onder Workspace Updates.
- Waarschuwing in de cijfers: Delete All Google Photos Extension zakte van 4,12 naar 3,7 sterren. Tools die de pagina bedienen gaan stuk als Google de pagina verandert (GOK, past bij Kai's punt over breekbaarheid).
- Geldbewijs: prijzen bestaan (Chris: ±$7 eenmalig tot $199 per jaar). Correctie na de controle: de maker van Bulk Edit Google Photos meldde zelf $500 per maand na 3 maanden, met de winkel als grootste bron (DERDEN, r/chrome_extensions via Arctic Shift, staat al in voorstellen/chrome-web-store.md en in besluiten 17 nov 06:50). Die groeide hier van 611 naar 1.000. Dat is het sterkste geldsignaal van alle vijf kandidaten, maar een eigen melding, niet nagemeten. SyncGP (Foto's back-up) op TrustMRR: $1.420 alles samen, $69 in 12 maanden, $0 in 30 dagen.

## Advies voor de keuze van 10:45 (aanvulling op deel 1)
1. Volgorde 1 en 2 blijft zoals in deel 1.
2. Kandidaat 3 schrappen: Obsidian doet het al gratis, met de officiële Importer (1,9 miljoen downloads voor alle bronnen samen, niet alleen Keep).
3. Kandidaat 4 alleen als gratis bereikproduct, niet voor de eerste euro's: de freemium-versie bestaat al en staat stil.
4. Kandidaat 5 is de enige van 3 tot 5 met groei, en met concurrenten met in-app aankopen die groeien; één maker meldt zelf $500 per maand (Bulk Edit Google Photos, DERDEN). Als 1 om een reden afvalt (bijvoorbeeld de keuring van Google voor de Calendar-scopes), is 5 inhoudelijk een betere tweede dan 2, maar alleen als we een manier vinden om te testen zonder in te loggen (een nagemaakte testpagina met de echte opbouw van photos.google.com), en met het risico dat het breekt.

## Wat ik niet kon meten (deel 2)
- Reviews per extensie (laden met een script). Waarom de Foto-tools sterren verliezen is dus een gok.
- Of er nieuwe autoplay- of Foto-tools zijn die niet in de eerste 10 van de zoektermen staan.
- Aankondigingen van Google Foto's (geen vaste feed gevonden in deze run).

Nagekeken door een controleur (17 nov ±07:50 UTC): alle getallen en sommen klopten met de TSV, steekproef live en in de Palant-dataset klopte; tien zinnen verbeterd (Importer-downloads gelden voor alle bronnen, Video Blocker apart benoemd, minder stellig waar het een gok is).
