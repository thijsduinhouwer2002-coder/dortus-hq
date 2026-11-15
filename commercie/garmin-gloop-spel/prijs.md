# Prijsvoorstel: Garmin-spelletje met Gloop

Chris, 15 nov 2026, run 43. Voor de platformmanager (Gijs, nu uit tot Ebb Calm is goedgekeurd) en Hans. Prijs is een besluit van de platformmanager na dit voorstel (rol Chris). Achtergrond van het product: `platformen/verkenner/iets-erbij-2026-11.md` (Vera, kandidaat 1) en het besluit van Thijs van 15 nov 15:30 (bouwen, pas rond 20 nov beginnen).

Labels: GEZIEN (zelf gemeten), DERDEN (bron), GOK (schatting).

## Voorstel in drie zinnen
1. **Start op $1,99 eenmalig, gewoon betaald in de Garmin-winkel, zonder proef.** Twee derde van de betaalde spellen kost $1,99, en de enige groep met een duidelijk verschil wijst naar $1,99; het bewijs is dun.
2. **Kijk op dag 30 opnieuw:** haalt het spel in de eerste maand de 100+ in de winkel, probeer dan $2,49 bij een volgende versie en meet of de verkoop per week gelijk blijft.
3. Dit wijkt bewust af van "durf hoger te prijzen" (doelen.md, punt 4) en van Ebb ($4,99). Doelen.md punt 1 zegt ook dat een eenmalige prijs niet te laag mag zijn, tenzij er veel gebruikers zijn. Eerlijk: in geld maakt de keuze in de eerste maand bijna niets uit (Vera verwacht rond 10 kopers, GOK; dan scheelt $1,99 of $2,49 ongeveer $4). De keuze gaat dus om zichtbaarheid (zo snel mogelijk 100+ in de winkel), niet om omzet.

## Wat ik gemeten heb (GEZIEN)
Bron: de detailgegevens van alle 605 Garmin-spellen (categorie 206) die Vera op 13 nov uit de open winkel-API haalde, `platformen/verkenner/data/garmin-spellen-details-2026-11-13.jsonl`. Script: `commercie/garmin-gloop-spel/meet-prijs.py` (draai met `python3 -I meet-prijs.py <dat bestand>`).

Weggelaten, net als bij Vera: ThijsGer en QuadroGames (vreemd koopgedrag), de 8 spellen met klachten "it was free" of die volgens Vera zeker eerst gratis waren, en de 2 die dat waarschijnlijk waren (ZigZag van garminland, Snake van li2niu). Over blijven 162 betaalde spellen, waarvan 140 met een datum van eerste goedkeuring (de 22 zonder datum staan niet in de tabel). Downloads zijn de emmers van de winkel (1+, 10+, 100+, 1.000+, 10.000+), dus ondergrenzen.

**Hoe vaak welke prijs (alle 172 betaalde spellen zonder ThijsGer en QuadroGames):** $1,99: 116 (67%); $2,25: 7; $2,49: 15; $2,99: 17; $3,49 tot $4,99: 17. Geen enkel betaald spel onder $1,99.

**Prijs tegen downloads, per leeftijd (sinds de eerste goedkeuring, op 13 nov):**

| Leeftijd | Prijs | Spellen | Mediaan | 100+ | 1.000+ |
|---|---|---|---|---|---|
| 3 tot 10 maanden | $1,99 | 21 | 100+ | 15 (71%) | 5 (24%) |
| 3 tot 10 maanden | $2,00 tot $2,99 | 6 | 1+ | 1 (17%) | 0 |
| 3 tot 10 maanden | $3,00 en meer | 2 | 1+ | 0 | 0 |
| 10 maanden en ouder | $1,99 | 21 | 10+ | 6 (29%) | 3 (14%) |
| 10 maanden en ouder | $2,00 tot $2,99 | 9 | 10+ | 3 (33%) | 2 (22%) |
| 10 maanden en ouder | $3,00 en meer | 1 | 1.000+ | 1 | 1 |
| jonger dan 3 maanden | $1,99 | 52 | 1+ | 8 (15%) | 0 |
| jonger dan 3 maanden | $2,00 tot $2,99 | 19 | 1+ | 4 (21%) | 0 |
| jonger dan 3 maanden | $3,00 en meer | 9 | 1+ | 1 (11%) | 0 |

Voorbeelden:
- $1,99 en 1.000+ of meer: AstroBlast (10.000+, sinds apr 2024), Fruit Spider (10.000+), Chess Pro, Blackjack, Circle Pong Game, Snake Game (KBialy).
- Hoger en toch 1.000+: Step Farmer ($2,49, 10.000+, maar eerst gratis volgens een review uit jun 2025, zie Vera; niet weggelaten omdat het geen klacht in haar telling was), Simon (garminland, $2,49), Chess! (Strafe, $3,99, goedgekeurd 4 nov 2024). Allemaal ouder dan 10 maanden, toen er veel minder aanbod was.
- Hoger en jong: Brick Breaker ($2,49, 100+), Voidrunner Arcade ($2,99, 100+ in 3 weken), Klotski ($3,99, 1+), Word Spinner ($3,49, 1+).

## Wat dit zegt, en wat niet
- **De duidelijkste groep is 3 tot 10 maanden oud** (lang genoeg om te groeien, en uit de tijd van nu): op $1,99 haalt 71% de 100+, op $2,00 tot $2,99 1 van de 6. Dat verschil is groot, maar de groep met de hogere prijs is klein (6 spellen), dus het is een aanwijzing, geen bewijs. **Let op: het grote verschil komt deels door het weglaten van de spellen die eerst gratis waren.** In deze groep vallen 4 spellen van $1,99 weg (alle 1.000+), 5 van $2,00 tot $2,99 (3 op 1.000+, 2 op 100+) en 1 van $3,49 (100+). Zonder dat filter is het 76% (19 van 25) tegen 55% (6 van 11) op 100+. Het weglaten is terecht (die spellen hadden al gratis spelers), maar het laat ook zien dat wie van gratis naar betaald ging, vaak een hogere prijs koos en daar toch verkocht.
- **Bij spellen van 10 maanden en ouder doet $2,00 tot $2,99 het even goed** (33% tegen 29% op 100+). Laat je ook Step Farmer weg (volgens een review eerst gratis, maar niet in Vera's telling), dan is het daar 2 van 8 op 100+ en 1 van 8 op 1.000+.
- **Bij de jongste lichting (aug tot nov) zie ik geen straf voor een hogere prijs** (21% tegen 15% op 100+). Die spellen zijn nog te jong om iets te zeggen, en bijna alles staat daar op 1+ of 10+, wat de prijs ook is.
- **Hogere prijzen werkten vooral vroeger en voor bekende makers** (Strafe, garminland). Wij beginnen zonder achterban.
- Andersom: niets bewijst dat $2,49 echt minder kopers geeft dan $1,99. De makers die op $1,99 slagen, hebben vaak veel gratis spellen die kopers aanvoeren (Vera, voorbehoud bij kandidaat 1), en dat telt in deze tabel mee.

## Waarom toch $1,99 (de afweging)
- Per verkoop scheelt het weinig: $1,99 geeft ±$1,69 na Garmins deel, $2,49 ±$2,12 (GOK: 85% voor de maker, `platformen/herweger/garmin-connect-iq.md`). Met $2,49 heb je 80% van de kopers van $1,99 nodig om quitte te spelen.
- Het getal in de winkel (1+, 10+, 100+) is wat een nieuwe koper als eerste ziet naast de prijs. Een spel op 100+ oogt als iets wat anderen al kochten; dat lijkt mij in de eerste maand meer waard dan $0,43 extra per verkoop (GOK, niet te meten in de winkel).
- Twee derde van de betaalde spellen kost $1,99; een koper die spellen vergelijkt, ziet die prijs als normaal (GOK op GEZIEN).
- Het spel is voor Dortus ook een reclamebord voor Hats of the Fallen en Ebb (Vera). Meer spelers is daarvoor beter dan meer per speler.

## Wat ik bewust niet voorstel
- **Gratis met ontgrendelen buiten de winkel (KPay of eigen code):** AstroBlast heeft naast de betaalde versie een versie "with trial and kpay"; die haalt 1.000+ tegen 10.000+ (Vera, GEZIEN). Ook vraagt het een extra betaaldienst en een account; bij ons zou dat via Thijs moeten.
- **Een proefstand in de winkel:** van de 605 spellen staat de proefstand bij 603 uit en bij 2 is hij onbekend; geen enkel spel heeft hem aan (Vera, GEZIEN; controleur zag `hasTrialMode` live uit bij AstroBlast, Step Farmer en Voidrunner Arcade). Onbekend of het betalen dan nog via de winkel gaat; niet de eerste keer uitproberen.
- **$0,99:** komt bij betaalde spellen niet voor (laagste prijs $1,99, GEZIEN); of de winkel het toestaat, heb ik niet gezien. Elke prijs heeft in de API een eigen artikelnummer ($1,99 eindigt op -04, $2,49 op -06, $2,99 op -08), dus Garmin werkt waarschijnlijk met vaste prijsstappen (GOK). Gijs kan de stappen en de prijs in euro voor Europese kopers in het portaal zien; alle prijzen hier zijn in dollars.

## Controleur (agent, 15 nov run 43)
Akkoord mits. Tabel, tellingen (172, 162, 140, 22), rekensom en Vera's feiten klopten; live steekproef van 3 spellen gelijk aan het bestand. Moet-punten verwerkt: (1) het filter "eerst gratis" maakt het verschil groter, nu met de cijfers zonder filter; (2) voorstelzin 1 zachter; (3) doelen.md punt 1 genoemd, keuze gaat om zichtbaarheid. Kan-punten verwerkt: Step Farmer, proefstand 603 en 2, prijsstappen, euro, datum Chess!.

## Wat dit voorstel omgooit
- Gijs of Thijs ziet in het makersportaal dat de prijs na de lancering niet te veranderen is: dan kies ik nog steeds $1,99, want terug naar beneden is dan ook niet mogelijk.
- Ebb ($4,99) haalt in zijn eerste 30 dagen (tot 13 dec) duidelijk meer kopers dan de betaalde spellen van zijn leeftijd (mediaan 1+): dan is de Garmin-koper minder op de prijs gericht dan ik denk, en is $2,49 de betere start.
- Een herhaalmeting rond de lancering laat zien dat jonge spellen op $2,49 tot $2,99 nu vaker 100+ halen dan die op $1,99.

## Volgende stap voor Chris
Vóór de lancering: het verspreidingsplan (`commercie/garmin-gloop-spel/verspreiding.md`), de winkeltekst en de herhaalmeting van deze tabel. Eerst moet het ontwerp er zijn (Gijs, na 20 nov).
