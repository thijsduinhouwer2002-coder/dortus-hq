# Voorstel: Ableton Live Extensions (Noor, 8 nov 2026)

**Cijfer: 3. Advies: nee voor nu, wachtlijst.** De pluginlaag is nieuw (openbare beta sinds 2 juni 2026) en er wordt al verkocht ($5 tot £39 via Gumroad en eigen sites), maar Ableton zelf groeit niet, Extensions zit na vijf maanden nog in de beta en alleen in Live 12 Suite, en het makersvuur van juni is al grotendeels uit (nieuwe GitHub-repo's 133 in juni naar 6 in oktober).

Bronnen: eigen metingen (GitHub-zoek-API, sitemap van liveextensions.co, script `data/ableton-extensions-meet.py`) en een onderzoeker (agent) voor status, geld, bedrijf en vraag. Geen controleur ingezet: het advies is geen ja en de doorslaggevende cijfers zijn zelf gemeten.

## 1. Groeit het platform hard? Nee.
- Ableton noemt zelf "over 350 people" (GEZIEN, https://www.ableton.com/en/about/). Revelio Labs telt 542 medewerkers in juni 2026, -21% sinds 2023 en -2,4% op jaarbasis, niet actief aan het werven (DERDEN, https://www.reveliolabs.com/companies/ableton/employees).
- Geen openbare gebruikers- of omzetcijfers voor 2025 of 2026 te vinden; laatste omzet is uit 2012 (DERDEN, https://en.wikipedia.org/wiki/Ableton). Beeld: stabiel tot licht krimpend (GOK).
- Ableton Discord: 40.306 leden (GEZIEN via de openbare invite-API, discord.gg/ableton). Groot genoeg als publiek, maar geen teken van groei.
- Extra beperking: Extensions werkt alleen in Live 12 Suite, en daar alleen in de beta (12.4.5b en later). Niet in Standard, Intro of Lite (GEZIEN, https://www.ableton.com/en/live/extensions/). De nieuwste stabiele versie 12.4.16 (30 okt 2026) heeft het niet (GEZIEN, https://www.ableton.com/en/release-notes/live-12/).

## 2. Is de winkel jong? Ja, maar er is geen winkel, en het tempo zakt.
- Er is geen officiële lijst of winkel. Een moderator van Ableton op 27 okt 2026: geen releasedatum ("once we consider it release-ready"), en over een lijst alleen "you might see something similar with Extensions", net als de Packs bij Max for Live (GEZIEN, https://forum.ableton.com/viewtopic.php?p=1837260).
- Vindplek is een site van een buitenstaander, liveextensions.co: 112 extensies in de sitemap (GEZIEN, 8 nov). Naar laatste wijziging: 86 in juni, 9 juli, 4 augustus, 4 september, 8 oktober, 1 november (GEZIEN, https://liveextensions.co/sitemap.xml; laatste wijziging is niet precies de aanmaakdatum, dus een benadering).
- Nieuwe GitHub-repo's met "ableton extension": juni 133, juli 28, augustus 15, september 9, oktober 6, november tot nu 1 (GEZIEN, GitHub search API). Dat is de vorm van een lanceringspiek die wegzakt, zoals bij Hytale (cijfer 3).

## 3. Kan er betaald worden? Ja, buiten Ableton om.
- Ableton noemt de SDK een "free download" en een "open JavaScript toolkit" (GEZIEN, https://www.ableton.com/en/blog/introducing-extensions-sdk/). De licentietekst zelf zit achter de beta-login en is niet gelezen; geen verbod op verkopen gevonden (GOK dat het mag).
- Er wordt al verkocht: Optimizer van everymachine $5 via Gumroad, nummer 1 op liveextensions.co met 1.598 downloads (GEZIEN, https://liveextensions.co/extensions/optimizer-all-in-one-ableton-toolkit). Ongeveer 9 van de ±106 extensies zijn betaald; midi studio+ van Lux Cache £39 als plugin plus extensie (DERDEN via onderzoeker).
- Ableton int niets en regelt niets: wie verkoopt, doet dat met een eigen kassa en eigen vindbaarheid.

## 4. Is er vraag? Klein.
- Populairste extensies op liveextensions.co: 1.598, 1.259, 1.164, 1.148, 1.146 downloads; de meeste tussen 100 en 700 (GEZIEN, https://liveextensions.co/browse).
- Forumverzoeken: tracks kleuren, favorieten-werkbalk, en een door Ableton gecontroleerde lijst vanwege veiligheid (GEZIEN, https://forum.ableton.com/viewtopic.php?p=1837326). Reddit niet gelezen.
- Ter vergelijking: dezelfde verzamelsite telt 2.437 Max for Live-devices (GEZIEN via onderzoeker). De echte betaalde markt voor Ableton-hulpmiddelen zit nog bij Max for Live.

## 5. Is de eerste plek te pakken? Ja, maar de prijs is klein.
- Dun bezet: sample-organisatie (Filed-Recording-Sorter 115 downloads) en hernoemen en opruimen van een Set (Optimizer $5, Assign Track Name 138, Scene Name Committer 159) (GEZIEN onderzoeker op liveextensions.co).
- Een Dortus-product als "projectbeheer voor Live" (opruimen, hernoemen, kleuren, ongebruikte samples vinden) kan daar nummer één worden. Maar nummer één is nu ±1.600 downloads in vijf maanden, op een bèta die alleen Suite-gebruikers zien.

## Risico en wat het zou veranderen
- Risico: Ableton laat Extensions lang in de beta, of bouwt de populairste functies zelf in (de moderator antwoordde op meerdere verzoeken "Nope", maar Ableton toont zelf al eigen voorbeelden zoals RNMR en Notation).
- Opnieuw wegen als: (a) Extensions in een stabiele Live-versie komt, (b) het ook in Live Standard komt, of (c) Ableton een eigen lijst of winkel opent (met betalen). Dan wordt het publiek veel groter en is het tempo van nieuwe extensies het eerste wat je meet.
- Herhaalmeting rond 8 feb 2027 of eerder zodra (a), (b) of (c) in de release notes staat: `python3 -I data/ableton-extensions-meet.py`.

## Cijfer
- Vraag 1 (groei): 1 van 3. Vraag 2 (jong): jong, maar geen winkel en zakkend tempo. Vraag 3 (geld): ja, zelf regelen. Vraag 4 (vraag): klein. Vraag 5 (eerste plek): open, kleine prijs.
- Samen 3: een jonge laag op een programma dat niet groeit, met een lanceringspiek die al voorbij is. Les van Command Palette en Premiere UXP geldt hier ook.
