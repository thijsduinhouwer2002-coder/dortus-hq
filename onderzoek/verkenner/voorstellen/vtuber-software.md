# Voorstel: VTuber-software (plugins en tools voor VTube Studio, Warudo, VNyan, PNGtuber)

Vera, 9 nov 2026 (voorwerk run 07:31, meting run 08:31). Controleur akkoord, 6 correcties verwerkt. Advies: **nee voor nu, cijfer 2.**

## Wat het is
VTubers streamen met een geanimeerd figuur. De software eromheen: VTube Studio (gratis, Steam), Warudo (gratis, Steam), VNyan (itch), PNGtuber-programma's, en daar omheen plugins en losse tools (lipsync, tekst naar spraak, Twitch-koppelingen, overlays). Makers verkopen via itch.io, BOOTH, Ko-fi en Steam (DLC). Geen eigen winkel met tellers.

## Cijfers
**Markt (GEZIEN, Steam, 9 nov ±07:40 UTC):** VTube Studio 9.443 spelers tegelijk, 3.498 Engelstalige reviews; Warudo 828 tegelijk, 699 reviews; PNGTuber Plus 150; VBridger ($9,99) 905 tegelijk, 208 reviews. Warudo Steam Workshop 1.707 items, allemaal gratis; beste software-plugin 5.443 abonnees.

**Bereik op itch (GEZIEN, eigen meting, alle 329 tools met tag vtuber, data/vtuber-itch-pagina-2026-11-09.jsonl en vtuber-itch-rss-2026-11-09/):**
- Ouder dan 3 maanden (208): mediaan 0 ratings, 174 met 0, 34 met 3+, 17 met 10+. Bijna alle 3+ zijn oude gratis of "kies zelf"-programma's (veadotube mini 957, PNGTuber Plus 234). Let op: oude tools hadden jaren om ratings te verzamelen, dit is geen eerlijke vergelijking met de lichting hieronder.
- Lichting jan 2025 t/m 8 aug 2026 (95, dus 3 tot 22 maanden oud): **2 met 3+ ratings, beide betaald** (VTS Y.A.P £7 en een Xsens-plugin $100, elk 4 ratings). De andere 93 hebben 0. De lichting bestaat uit 34 overlays en maar ±12 echte plugins voor VTube Studio, Warudo of VNyan; juist 2 van die plugins zijn de uitschieters, dus het signaal voor ons soort product is zwak maar niet nul.
- Betaalde oudere tools: 49, waarvan 6 met 3+. Best betaald, naast een algemene 3D-tool uit 2016 (Mannequin, $29,99, 148): HONK lipsync $12 (70 ratings, sinds 2021), VTS P.O.G. $15 (25, sinds 2022), Inochi Creator $40 (21).

**Drukte (GEZIEN, RSS-datum; die is gelijk aan de aanmaakdatum van de pagina, de controleur zag bij alle 329 pubDate = createDate, een update verandert hem niet):** mei 7, jun 16, jul 14, aug 29, sep 63, okt 31 nieuwe tools per maand. De sprong komt van AI: 109 van de 121 tools van de laatste 3 maanden melden AI, één maker (tsuru1125) zette er 57 OBS-overlays van $3 tot $5 neer. Alle 97 jonge overlays hebben 0 ratings.

**BOOTH (GEZIEN, run 07:31):** 156 echte VTuber-tools, nov 2025 t/m aug 2026 56 nieuwe (±5 tot 14 per maand), betaald 34 met mediaan 23 likes. Likes zijn geen verkopen.

**Geld (DERDEN, graphtreon en TrustMRR):** PngTuberMaker (web-abonnement, sinds feb 2026) $663 in 30 dagen, 51 abonnees; Mix It Up (streambot met VTube Studio-koppeling) ±$1.158 per maand op Patreon; SAMMI ±$213; Inochi2D ±$158; veadotube $546 (laatste openbare stand mei 2022). Algemene streamtool Streamer.bot ±$4.406. Ko-fi en Reddit verbieden ons in robots.txt, Patreon zit achter Cloudflare, SteamDB gaf 403: VSeeFace, VNyan, Warudo Pro en PNGTuber Plus konden we niet meten.

## Voordelen
- Echte, trouwe markt: VTube Studio heeft ±9.400 gebruikers tegelijk en DenchiSoft laat plugins verkopen zonder afdracht.
- Betaalde tools van $7 tot $20 bestaan en een paar oude houden het jaren vol.
- Software past bij ons (kleine tools, API van VTube Studio is open en goed beschreven).

## Nadelen
- Geen winkel die bereik geeft: itch toont nieuwe tools een paar dagen, daarna niets. Van de lichting 2025 tot aug 2026 haalt 2 van 95 meer dan 2 ratings.
- De markt loopt nu vol met AI-tools van $3 (63 nieuwe in september), dus wij zouden in die vloed staan.
- Openbare bedragen per maker blijven onder ±$1.200 per maand, en de hoogste zitten bij oude namen of algemene streamtools.
- De gratis basis is sterk: veadotube, PNGTuber Plus, VTube Studio en de Warudo Workshop zijn gratis.
- Het enige nieuwe succes (PngTuberMaker) is een webdienst die zijn eigen klanten zoekt, geen plugin in een winkel.

## Wat we zouden bouwen (als het ooit verandert)
Een betaalde VTube Studio-plugin voor één klus waar nu gratis rommel zit (bijvoorbeeld chat-reacties op het model of ondertitels), $7 tot $15. Maar zonder winkel met bereik moeten we zelf klanten zoeken via Twitch en Discord, en dat is precies wat we niet kunnen.

## Cijfer en advies
**2 van 10, nee voor nu.** Bereik voor nieuwe makers bijna nul (2 van 95 met 3+ ratings), geld wel echt maar klein en bij oude namen. Lager dan itch-tools in het algemeen (4) omdat dit een kleiner, nu volstromend stukje daarvan is.

Opnieuw kijken als: veadotube op 4 dec 2026 op Steam komt met Workshop of betaalde plugins, of als VTube Studio of Warudo een eigen betaalde pluginwinkel opent.

## Wat ik niet kon meten
Let op bij de data: het veld `pub` in vtuber-itch-pagina-2026-11-09.jsonl is meestal de Updated-datum (itch toont vaak geen rij Published), dus niet gebruiken; de RSS-datum telt.

Verkopen op itch (alleen ratings; bij itch-tools is ±1 rating per 10 kopers een ruwe gok uit de meting van 8 nov), Ko-fi-winkels (robots.txt), en BOOTH-verkopen (alleen likes).
