# Verdwenen MV2-extensies zonder goede opvolger (voor Kai, 17 nov 2026)

Opdracht hoofdchat 17 nov 06:50: de lijst van met Manifest V2 verdwenen extensies met veel gebruikers zonder opvolger, met bewijs, voor `platformen/chrome/kandidaten.md`. Gemaakt in run 06:31 NL door Vera met een onderzoeker; top 5 daarna zelf nagekeken op de live winkel (05:55 UTC).

## Hoe gemeten
- Bron: de openbare dataset van Wladimir Palant met manifest en gebruikers van 100.000+ extensies op vaste momenten (DERDEN, codeberg.org/palant/chrome-extension-manifests-dataset, mappen `manifests-2025-01-10` en `manifests-2026-08-14`).
- 1.872 extensies waren in jan 2025 MV2 met 10.000+ gebruikers. Op 14 aug 2026 waren er 445 overgestapt naar MV3, 161 al weg en 1.266 nog MV2 (154 daarvan nog met 50.000+ gebruikers). Google haalde de MV2-extensies op 31 aug 2026 uit de winkel (DERDEN, bumbletap.com/blog/chrome-manifest-v2-extensions-removed). Alles: `data/chrome-mv2-10k-2026-11-17.tsv`.
- Live nagekeken (GEZIEN, 17 nov): een verwijderde extensie geeft op chromewebstore.google.com/detail/<id> alleen de titel "Chrome Web Store", een levende geeft naam en gebruikers (controle: Hover Zoom+ 300.000). Alle 7 hieronder met een ID in de top zijn weg.
- Opvolgers gezocht via de winkelzoekfunctie en de dataset. Beperking: de zoekfunctie van de winkel is niet volledig met curl te lezen, dus een opvolger met een andere naam kan gemist zijn (GOK). Reddit-bewijs is mager: Arctic Shift gaf na ±20 verzoeken alleen time-outs.

## Top 5

| # | Weg (ID) | Gebruikers jan 2025 / aug 2026 | Beste opvolger nu (GEZIEN live 17 nov) | Gat |
|---|---|---|---|---|
| 1 | Revolver - Tabs (`dlknooajieciikpedpldejhhijacnbda`), tabbladen rouleren en verversen voor dashboards op tv's en kantoorschermen | 200.000 / 80.000 | 3-2-1 Revolver 10.000, goRotate 10.000 | groot |
| 2 | AutoplayStopper (`ejddcgojdblidajhngkogefpkknnebdh`) plus Disable HTML5 Autoplay (`efdhoaajjjgckpbkoglidkeendpkolai`, 100.000) en de Reloaded-versie (30.000) | 100.000 / 40.000 | AutoplayStopper (MV3) 10.000 | groot |
| 3 | AutoPagerize (`igiofjhpmpihnifddepnpngfjhkfenbp`), volgende pagina vanzelf onderaan laden | 200.000 / 100.000 | Infy Scroll 30.000 | groot |
| 4 | ClearURLs (`lckanjgmijmafbedllaakclkaicjfmnk`), volgcodes uit links | 100.000 / 60.000 | URL Cleaner 7.000 | groot, maar uBlock Origin Lite doet een deel |
| 5 | Imagus (`immpkjjlgappgfkkfieppnmlhakdmaab`), afbeelding groot bij muis erover | 400.000 / 100.000 | Hover Zoom+ 300.000 | klein: sterke opvolger |

Gebruikers uit de dataset (DERDEN), opvolgers live (GEZIEN).

**Bewijs dat mensen het missen (DERDEN, Reddit):**
- Autoplay: "We desperately need a new video Autoplay stopper" (r/chrome, 14 mei 2025, reddit.com/r/chrome/comments/1km3kyb/); "still looking for a replacement for ... Disabling HTML5 Video Autoplay" (6 sep 2025, reddit.com/comments/1my6ms3/_/ncoolw2); over de MV3-versie: "nowhere near as effective" (22 nov 2025, reddit.com/comments/1my6ms3/_/nq42r1g).
- Imagus: 4 draadjes "alternative for Imagus?" tussen okt 2024 en mrt 2025, tot 12 punten (reddit.com/r/chrome/comments/1g4c4fh/).
- Revolver, AutoPagerize, ClearURLs: geen posts gevonden door de time-outs. Dat zegt niet dat niemand ze mist; de terugval van 200.000 naar 80.000 en 100.000 gebruikers vóór de verwijdering laat zien dat er tot het eind veel mensen op zaten.

**Kunnen wij het, zonder server en zonder voorwaarden te breken (GOK, op basis van de MV3-API's):**
1. Revolver: ja, met tabs, alarms en storage. Zakelijk gebruik (schermen in kantoren, winkels, controlekamers), dus betaalde laag logisch: schema's per tijdstip, per tab eigen tijd en verversen, kiosk- en volledig-scherm, instellingen exporteren naar meer schermen. Of men al betaalt voor tabrotatie hebben we niet gemeten (GOK).
2. Autoplay: ja, content script bij document_start in alle frames dat media.play onderschept. Embedded video in iframes van andere sites is het lastige deel, en precies waar de MV3-versie op faalt volgens de reacties.
3. AutoPagerize: ja, de openbare SITEINFO-regels als data meeleveren of als JSON ophalen (geen code van buiten).
4. ClearURLs: ja, met declarativeNetRequest (parameters weghalen). Licentie van de ClearURLs-regellijst eerst nakijken.
5. Imagus: ja, maar Hover Zoom+ heeft 300.000, dus geen gat.

## Advies voor Kai
Revolver bovenaan: groot verlies (200.000 naar 0), opvolgers samen ±20.000, en het is zakelijk gebruik waar een eenmalige of jaarlicentie past (gratis roteren, betalen voor schema's en meerdere schermen). Daarna autoplay (veel klachten, opvolger zwak, maar betaalbereidheid voor een "stop alles"-knop is onbekend). Imagus niet.

## De andere 10 (gebruikers jan 2025, DERDEN dataset; opvolgers aug 2026)
- Ears: Bass Boost, EQ (600.000): opvolgers Equalizer for Chrome browser en Music Equalizer elk 500.000. Vol.
- Cookie AutoDelete (100.000): opvolgers 20.000, 10.000, 10.000.
- Page Monitor (100.000, weg GEZIEN): Distill 400.000 (gratis met limieten), Visualping 100.000 (met server). Gat: een gratis monitor die alleen lokaal werkt.
- XPath Helper (300.000, weg GEZIEN): XPath Helper 2.0 10.000; SelectorsHub niet nagekeken.
- Copy All Urls (300.000): opvolger 80.000. Matig gat.
- Linkclump (300.000): Linkclump Plus 90.000. Klein gat.
- Tab Position Options (60.000): New Adjacent Tab 10.000.
- Disable Automatic Gain Control (80.000): v2 10.000. Niche (muzikanten, podcasters).
- Skip Redirect (50.000): opvolgers onder 1.000.
- MarkDownload (70.000): MarkSnip 30.000. Klein gat.

## Valt af
uMatrix en Netflix 1080p (kunnen niet meer in MV3), Web Server for Chrome (Chrome-apps bestaan niet meer), Pushbullet (server nodig), Twitch-drops en Alternate Player for Twitch (tegen de regels van Twitch), grote advertentieblokkers (sterke spelers), extensies van bedrijven en banken. Nog live of al overgestapt: h264ify, Extensity, Chrono, Reddit Enhancement Suite, Enhancer for YouTube, Midnight Lizard, Location Guard, The Marvellous Suspender.

## Nog niet gedaan
Concurrentiecheck van wat er aankomt (regel 16 nov) en betaalbereidheid per kandidaat: dat hoort bij de fase van Kai voor de keuze van 10:45.
