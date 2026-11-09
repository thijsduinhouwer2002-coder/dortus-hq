# Steam bureaublad-apps (Desktop Companion): herweging

Kees, herweger, 9 nov 2026 run 13:25 UTC. Oud cijfer 7 (Hans 8 nov, Vera 6). **Nieuw cijfer: 8 (krap).** Nagekeken door een controleur (zie onder).

## De doorslaggevende meting en waarom
Het bewijs van Vera (54% van de betaalde apps uit mei tot aug haalt 10+ reviews) had twee gaten: (a) het telde reviews tot nu toe, dus oudere apps hadden meer tijd, en (b) de grote vraag was of een nieuwkomer **nu** nog verdient, nu er drie keer zoveel apps per maand bijkomen. Dat is precies punt 1 en 2 van een 8.

Daarom: **per app het aantal reviews in de eerste 28 dagen na release, per lichting, met exacte aantallen in alle talen.** Bron: het openbare Steam-adres `store.steampowered.com/appreviewhistogram/<appid>` (weektotalen van alle reviews, ook onder de 10; het adres `appreviews` stuurt vanaf hier door). Zo vergelijk je lichtingen op gelijke leeftijd, en zie je of de nieuwste lichting nog gevonden wordt.

Data en scripts: `platformen/herweger/data/` (`hist.py`, `analyse.py`, `steam-hist-2026-11-09.json`, `steam-eerste28-2026-11-09.json`). App-lijst: de zoeklijst van Vera van 7 nov (label Desktop Companion, betaald, release 1 mrt t/m 12 okt 2026, 182 apps).

## Uitkomst (GEZIEN, nagekeken)
| Lichting | Apps | Mediaan reviews eerste 28 dagen | 10+ | 30+ | Apps met 10+ (absoluut) |
|---|---|---|---|---|---|
| jul 2026 | 39 | 10 | 54% | 26% | 21 |
| aug 2026 | 29 | 5 | 34% | 10% | 10 |
| **sep 2026** | **45** | **3** | **38%** | **22%** | **17** |
| okt 1 t/m 12 | 15 | 1 | 27% | 20% | 4 |

- **September, de nieuwste volledige lichting: 17 van 45 betaalde apps (38%) halen 10 of meer reviews in hun eerste maand, 10 van 45 (22%) halen 30 of meer.** Strikter geteld (venster precies 28 dagen) 16 van 45 (36%). Zonder de 4 early-access-apps 16 van 41 (39%).
- Voorbeelden sep/okt, eerste 28 dagen: Deskrawl 3.211, Duelist 723, Your Fiancée 680, Lootborne 486, NekoTrak 162, Push Push 124, BuGarden 118, Black Cat Book Club 71, WinMon 58, PawMart Tiny Market 39, Dog 32. Mediaanprijs $4,99.
- **Het aantal geslaagde nieuwkomers groeit mee** (jul 21, aug 10, sep 17): de extra drukte verdringt de nieuwkomers (nog) niet. Het is geen vaste koek.
- Wat dat in geld is (GOK op DERDEN, ±30 verkopen per review uit het voorstel van Vera): 10 reviews ≈ 300 verkopen ≈ $1.000 bruto, na Steam en btw ±$900 in de eerste maand bij $4,99. Een op de drie nieuwe apps haalt dat, een op de vijf ±$2.500 of meer. Dat is ruim boven de lat van een 8 ("een kwart met merkbare verkopen, een paar boven ±$300 per maand").

Let op bij lezen:
- De oudere maanden (mrt 90%, apr 53% 10+) zijn vertekend: het label wordt deels door gebruikers gegeven, dus in oude lichtingen staan vooral de apps die bleven hangen. Gebruik die niet als maat en niet als trend. September is de minst vertekende lichting (14 van de 45 hebben 0 reviews en staan er toch in).
- De verdeling is scheef: mediaan 3, 20 van de 45 hebben 0 of 1 review. Ongeveer de helft verdient bijna niets.
- Oktober ligt lager (27%), maar het zijn er 15 en de maand is half. Opnieuw meten rond 23 nov (zie onder).

## Weging tegen de vier punten van een 8
1. **Nieuwe kleine makers verdienen nu: sterk** (GEZIEN, hierboven; de makers zijn bijna allemaal klein en zelf uitgegeven, Vera: 82 van 95).
2. **Bereik voor nieuwkomers: sterk.** 38% van de nieuwste lichting wordt in de eerste maand gevonden en gekocht, zonder dat het om bekende studio's gaat. Of een deel van die apps eigen reclame (TikTok) deed, heb ik niet gemeten (GOK: bij enkele uitschieters wel).
3. **Bouwen en testen: voldoende.** Een kleine Windows-app (Godot of Tauri) is op Linux te bouwen en op GitHub Actions (Windows) te testen. Uiterlijk is het echte risico; dat is geen bouwprobleem maar wel ons zwakste punt (Daan vanaf dag 1).
4. **Thijs kan verkopen: schuurt.** Steamworks als particulier kan (geen KvK nodig), maar het kost $100 per app (terug na $1.000 omzet) en tussen betalen en uitbrengen zit 30 dagen, plus ±2 weken "binnenkort"-pagina. Dat valt samen met de bouwtijd en de verlanglijstperiode, dus het vertraagt weinig, maar "binnen een week verkopen" is het niet.

**Waarom toch een 8:** punt 1 en 2 zijn nu met de nieuwste lichting op gelijke leeftijd gemeten en houden ruim stand, en de groei vreet de kans niet op. Het bezwaar van Thijs ($100 vooraf) wordt kleiner door deze meting: een op de drie nieuwe apps verdient de $100 in de eerste maand ruim terug, en Steam geeft hem terug na $1.000 omzet. Punt 4 schuurt alleen in tijd, niet in geld of papieren. Krap, omdat uiterlijk voor ons onbewezen is en de helft van de apps vrijwel niets verdient: het wordt geen zekerheid, wel de beste kansverhouding die we zagen.

## Wat dit zou veranderen
- Naar 7: de lichting oktober (volledige maand, meting rond 23 nov met dezelfde scripts) zakt onder ±25% met 10+ in de eerste 28 dagen.
- Herhalen: `python3 platformen/herweger/data/hist.py platformen/verkenner/data/<nieuwe zoeklijst>.json uit.json` (pas de datumgrenzen in `hist.py` aan), dan `analyse.py uit.json rijen.json`. Nieuwe zoeklijst met `platformen/verkenner/data/steam-zoek-script.py 1320952 <uit> 3000`.

## Nagekeken
Controleur 9 nov: cijfers opnieuw uitgerekend uit de ruwe data (klopt; afronding gecorrigeerd naar 38% en 27%), 5 histogrammen live opnieuw opgehaald (identiek), alle 45 releasedata van september via appdetails nagekeken (kloppen; 10 prijzen wijken af door korting, alle apps betaald), venster en early access gecontroleerd (strikt 36%, zonder early access 39%), vertekening door het label bevestigd voor mrt t/m jun. Oordeel: "ruim een derde van de nieuwste lichting haalt 10+ reviews in de eerste maand" houdt stand.
