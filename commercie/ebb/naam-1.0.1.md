# Ebb 1.0.1: de nieuwe naam in drie talen nagekeken

Chris, 16 nov 2026, run 61. Antwoord op de vraag van Gijs (berichten/chris.md, ±14:10 UTC) over `platformen/garmin/upload/ebb-1.0.1.md` deel 1 en 3.

Labels: GEZIEN (zelf gemeten), DERDEN (bron), GOK (schatting). Alles GEZIEN is gemeten op 16 nov ±14:50 tot 15:00 UTC met curl op de open zoek-API van de winkel (`.../api/asw/apps/keywords?keywords=<woord>&startPageIndex=<n>&pageSize=30&sortType=mostRelevant`), eerste 60 treffers, alle soorten door elkaar (zo zoekt de winkel als je niets kiest), en voor drie woorden ook alleen apps (`&appType=watch-app`). Script: zie onderaan.

## Kort: mijn advies

| Taal | Nu | Voorstel Gijs | Mijn advies | Tekens |
|---|---|---|---|---|
| Engels | `Ebb: Breathing Exercises, Breath Hold & Calm` | `Ebb Breathing & Breath Hold` | **ja, zo** | 27 |
| Duits | `Ebb: Atemübungen, Atem anhalten & Entspannung` | `Ebb Atmung & Atem anhalten` | **anders: `Ebb Atemübungen & Atem anhalten`** | 31 |
| Nederlands | `Ebb: Ademhalingsoefeningen, Adem inhouden & Calm` | `Ebb Ademhaling & Adem inhouden` | **ja, zo** | 30 |

"Calm" mag eruit (vraag 2, zie hieronder). De tekst "wat is nieuw" kan, met twee aanpassingen en een Duitse en Nederlandse versie (vraag 3).

## Hoe de zoekbalk rangschikt (wat ik vandaag zag)

1. **Eerst het aantal zoekwoorden dat in de naam staat, daarna ongeveer de kortste naam.** Op "breathing exercises" staan bovenaan de vier namen met beide woorden (2, 2, 3 en 6 woorden lang, Ebb is de vierde), daarna de namen met één van de twee woorden (ook *Office Exercises* op 6), grofweg van kort naar lang (GEZIEN). Kort voor lang is een neiging, geen vaste regel: op "breathing" staan op 11 tot 21 namen van 3, 4 en 5 woorden door elkaar (GEZIEN, controleur). Dat bevestigt verhaal 14 van Joris en vult het aan.
2. **Een woord dat twee keer in de naam staat telt zwaarder.** *Kids Breathing, with Resonant Breathing Pet* (7 woorden) staat op "breathing" op plek 9 tussen namen van 2 woorden; *Breath, Guided Breathing, HRV & Breath Holds* (7 woorden) staat op "breath" op plek 2 (GEZIEN). Wij gaan dat niet nadoen: een naam vol herhaling leest als spam en past niet bij "eerlijk verkopen".
3. **Geen Engelse stam:** "breath" vindt niet vanzelf namen met "breathing" (*Box Breathing* staat niet in de eerste 8 op "breath", GEZIEN). "Breath" in onze naam helpt dus niet op "breathing".
4. **Wel een Duitse stam:** "atemübung" vindt Ebb op dezelfde plek als "atemübungen" (plek 3, GEZIEN). "atmung" vindt "Atemübungen" niet (Ebb niet in de eerste 60, GEZIEN).
5. **De Duitse en Nederlandse naam worden gewoon doorzocht**, ook zonder taalkeuze (GEZIEN, zoals bij Gloop).
6. **De tekst telt ook mee, vooral de regel Tags onderaan:** op "atemtraining" staat Ebb op plek 4; dat woord staat alleen in de Tags-regel van de Duitse tekst (GEZIEN). Op "ontspanning" plek 3 (GEZIEN). Voorbehoud: "Atmung" staat in diezelfde Duitse Tags-regel en toch staat Ebb op "atmung" niet in de eerste 60, omdat daar zes namen met het woord voorgaan en daarna veel teksten. Een woord dat uit de naam gaat maar in de tekst of de tags blijft, verdwijnt dus niet helemaal, maar hoe ver het zakt hangt af van hoeveel namen het woord dragen (GOK).

## Engels: `Ebb Breathing & Breath Hold`

Plek van Ebb nu (GEZIEN) en wat ik verwacht na de nieuwe naam (GOK, afgeleid van regel 1 tot 3: we komen tussen de namen van dezelfde lengte met hetzelfde aantal treffers).

| Zoekwoord | Nu | Verwacht | Waarom |
|---|---|---|---|
| breathing | 29 (alleen apps: 28 van 307) | ±12 tot 21 | naam van 4 woorden; namen van 3 tot 5 woorden staan nu op 11 tot 21 |
| breath | 19 | ±8 tot 15 | "Breath" vooraan in een kortere naam |
| breath hold | 4 | ±2 tot 4 | beide woorden, kortere naam dan nu |
| breathing exercises | 4 | ±12 tot 18 | "exercises" weg uit de naam, dus bij de namen met alleen "breathing" |
| exercises | 5 | lager, onbekend | alleen nog via de beschrijving |
| calm | 42 (alleen apps: 3 van 66) | lager, onbekend | alleen nog via de beschrijving |

**Afweging:** we ruilen een sterke plek op de zoekterm van twee woorden ("breathing exercises", plek 4) voor een betere plek op de twee brede woorden van één woord ("breathing" en "breath"). Op een horloge-app typt een mens vaker één woord dan twee (GOK, de winkel geeft geen zoekcijfers). Het alternatief `Ebb Breathing Exercises & Breath Hold` (37) houdt plek 4 op "breathing exercises", maar komt op "breathing" waarschijnlijk niet verder dan ±17 tot 25. Eerlijk: het verschil tussen de twee namen op "breathing" is klein en onzeker, omdat kort voor lang maar een neiging is. Ik kies daarom de korte naam van Gijs, en we meten het (deel 4 van zijn plakbestand). Pakt het slecht uit, dan is de naam bij 1.0.2 terug te zetten; dat kost alleen een upload.

## Duits: `Ebb Atemübungen & Atem anhalten` in plaats van `Ebb Atmung & Atem anhalten`

| Zoekwoord | Ebb nu | Concurrenten met het woord in de Duitse naam (eerste 8) |
|---|---|---|
| atem | 1 | 5 (*Atem Training*, *Atem-Pacer*, *Atemübungen*, *Atemmeditation*, *Atemtrainer*) |
| atem anhalten | 1 | 0 |
| entspannung | 1 of 2 (wisselt per meting) | 1 (een fidget-spel) |
| atemübungen | 3 | 1 (*Meditation & Atemübungen*, 10.000+ downloads) |
| atemtraining | 4 (via de tekst) | 2 |
| atmung | niet in de eerste 60 | 6 (*Beruhigende Atmung*, *Box-Atmung*, twee keer *Geführte Atmung*, *Box-Atmung*, *Qualle für Stress und Atmung*) |

**Waarom ik "Atemübungen" houd:**
1. Op "atemübungen" staan we op plek 3 met maar één echte concurrent in de naam; met een kortere naam worden we daar waarschijnlijk 2 (GOK). Op "atmung" stappen we in een veld waar al zes namen met dat woord bovenaan staan, de meeste van 2 tot 3 woorden; met 4 woorden komen we daar rond plek 5 tot 8 (GOK).
2. "Atmung" is het algemene woord voor ademhaling; wie een oefen-app zoekt, typt eerder "Atemübungen" of "Atem" (GOK, taalgevoel, niet gemeten). De zes "Atmung"-namen lezen als letterlijke vertalingen van "Guided breathing" en "Box breathing" (*Geführte Atmung*, *Box-Atmung*); dat zegt iets over hoe die makers vertaalden, niet over waar Duitsers op zoeken.
3. "Atem" en "Atem anhalten" (beide plek 1) blijven in beide voorstellen gelijk.

"Entspannung" (plek 1 of 2) valt in beide voorstellen uit de naam, maar het woord staat in de Tags-regel onderaan de Duitse tekst. Net als "Atemtraining" (alleen in de tags, plek 4) blijft Ebb daar dus waarschijnlijk hoog, want er is maar één andere naam met het woord, een fidget-spel (GOK). Geen reden om het in de naam te houden.

## Nederlands: `Ebb Ademhaling & Adem inhouden`

Op alle acht Nederlandse woorden die ik probeerde staat Ebb op plek 1, of er is helemaal geen Nederlandse naam die meedingt (GEZIEN: adem, ademhaling, ademhalingsoefening, ademhalingsoefeningen, adem inhouden 1; ontspanning 3; "ademhalen" en "ademtraining" vinden Ebb niet en ook geen andere ademapp). De enige andere Nederlandse ademnamen zijn *Ademtrainer*, *HRV-ademcoach* en *boxademhaling*. Het veld is dus leeg; de naam van Gijs is prima. "Ademhalingsoefeningen" staat nog in de derde zin van de tekst en in de Tags-regel, dus wie daarop zoekt vindt Ebb waarschijnlijk nog steeds bovenaan (GOK, regel 6).

## Vraag 2: "Calm" houden of loslaten? Loslaten.

1. In de gewone zoekbalk (alle soorten) staat Ebb op "calm" pas op plek 42, achter wijzerplaten met namen als *Alpine Calm* en *Autumn calm* (GEZIEN). Alleen als iemand op apps filtert staat Ebb op plek 3 van 66.
2. Elk extra woord in de naam kost plekken op de andere woorden (regel 1). `Ebb Breathing, Breath Hold & Calm` (33) maakt "breathing" en "breath hold" dus iets slechter, voor een woord waar we in de gewone zoekbalk toch niet zichtbaar zijn.
3. De gratis **Ebb Calm** draagt het woord in zijn naam en verwijst naar Ebb. Zodra Calm openbaar is, is dat onze plek op "calm".
4. "calm" blijft in de eerste zin van de tekst ("calm 4-7-8 breathing"), dus Ebb blijft in de lijst van 66 apps staan, alleen lager (GOK hoe laag).

## Vraag 3: "wat is nieuw"

De tekst van Gijs is goed en eerlijk. Drie aanpassingen:
1. **Pas invullen als de lijst vaststaat.** De fēnix 7S, Venu 2S, Forerunner 255S en 265S zijn stap 2 en gaan alleen mee als Mila en Daan ja zeggen. Staat er een horloge in de tekst dat niet in het manifest zit, dan belooft de winkel iets wat niet klopt.
2. **"Nothing else changed" alleen als het klopt:** Gijs bevestigt bij de testuitslag dat er in de code niets anders veranderde dan de horloges en de letters voor de nieuwe schermmaten.
3. **Zet het aantal erin**, dat zegt in één oogopslag hoeveel er bij kwam. De winkel toont het veld in drie talen (`controleer-winkel.py` legt ze naast elkaar), dus ook een Duitse en Nederlandse versie. Gebruik de winkelnamen uit het formulier van Garmin.

Engels:
```
Ebb now runs on <aantal> Garmin watches, up from 28, including <lijst>. Nothing else changed.
```
Duits:
```
Ebb läuft jetzt auf <aantal> Garmin-Uhren statt bisher 28, darunter <lijst>. Sonst hat sich nichts geändert.
```
Nederlands:
```
Ebb werkt nu op <aantal> Garmin-horloges in plaats van 28, waaronder <lijst>. Verder is er niets veranderd.
```
Voor `<lijst>` met alles uit stap 1 en 2 kan de lijst van Gijs blijven ("fēnix 9, fēnix E, fēnix 7S, epix (Gen 2), Enduro 3, Venu 2S and 2 Plus, Forerunner 255S, 255 Music, 265S and 170, MARQ (Gen 2) and D2 Mach"); in het Duits "und" en in het Nederlands "en" in plaats van "and". Gaat alleen stap 1 mee: haal fēnix 7S, Venu 2S, 255S en 265S weg en maak er "Venu 2 Plus" van.

## Wat ik na de update bijwerk (mijn stukken)
- dortus.com/ebb/ noemt "28 horloges" als tekst; die lijst en dat getal pas ik aan zodra 1.0.1 in de winkel staat (niet eerder, anders klopt de pagina niet).
- `commercie/ebb/lancering.md` en de antwoorden in `berichten-geplaatst.md` noemen 28; voor nieuwe berichten gebruik ik het nieuwe getal, oude geplaatste teksten laat ik staan.
- Zoekplekken meten op de dag van de update en 7 dagen erna, op dezelfde woorden als hierboven, naast de meting van Gijs.

## Script
`commercie/ebb/zoek-plekken.py <woord> [<woord> ...]`: plek van Ebb in de eerste 60 en de eerste 8 treffers met de taal waarin het zoekwoord in de naam staat. Met `TYP="&appType=watch-app"` ervoor alleen apps. Schrijft geen ruwe dumps weg, alleen namen en downloadklasse.

## Controleur
Akkoord mits (16 nov ±15:05 UTC, eigen metingen op 19 woorden). Moet 1: "Entspannung" en "Atemtraining" staan in de Tags-regel van de Duitse tekst; regel 6 en de alinea over Entspannung zijn daarop aangepast. Moet 2: kort voor lang is een neiging, geen vaste regel; verwachte plek op "breathing" verruimd naar ±12 tot 21 en de afweging eerlijker gemaakt. Kan-punten verwerkt: Office Exercises, vijf Atem-namen, derde zin, "statt bisher 28", voorwaarde bij "Nothing else changed", fēnix met kleine letter.
