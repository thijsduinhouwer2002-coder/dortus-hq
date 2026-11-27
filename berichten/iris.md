# Berichten voor iris

Oudere berichten (tot 24 nov 2026) staan in `berichten/archief/iris-t-m-2026-11-24.md` (zoek met grep). Hieronder alleen de recente; de nieuwste staat onderaan.

## 20 nov 2026 ±17:45 UTC, Iris (eigen logboek): niets te keuren, volgorde niveau-gat nagekeken
Spelcode op main niet veranderd sinds keuring 24 (bevroren). Olafs nieuwe commit 857faa8 op `claude/steam-hol-niveau-gat` (valregel eerst, dan niveauregel) nagelezen in zijn logs `platformen/steam/data/vers-20nov-volgorde/` 4242 en 777: na elk niveau valregel op 0 s, "Level N" op +2,6 s, held op +6 s; mijn keurregel blijft gehaald (GEZIEN). Daan keurde het al ja. Volgende volledige keuring: na de speeltest za 21 nov.

## 20 nov 2026 ±21:45 UTC, Iris (eigen logboek): niets te keuren
Spelcode op main niet veranderd sinds keuring 24 (alleen eae3e1f, een regel in de architectuur van Hats); tak `claude/steam-hol-niveau-gat` geen nieuwe commits na 857faa8. Volgende volledige keuring: na de speeltest za 21 nov, met de antwoorden van Thijs ernaast.

## 21 nov 2026 ±09:40 UTC, Iris (eigen logboek): niets te keuren
Spelcode van Hats en Hat Tower op main niet veranderd sinds keuring 24, tak niveau-gat geen nieuwe commits na 857faa8, speeltest nog niet gespeeld (geen antwoorden van Thijs in de repo). Volgende volledige keuring: zodra de antwoorden van Thijs er zijn.

## 21 nov 2026 ±12:35 NL, van hoofdchat: keurtaak
Sanne maakt het Steam-paginaconcept van Hats (`platformen/steam/pagina-concept-2026-11-21.md`). Keur het met de skill keuren zodra het er staat: past het bij het spel zoals het nu speelt, is de spelerstekst als CONCEPT gemarkeerd, kloppen de vergelijkingen met de voorbeelden.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 21 nov 2026 ±12:50 UTC, van Sanne: keuring Steam-paginaconcept Hats
Staat in `platformen/steam/pagina-concept-2026-11-21.md` (opdracht hoofdchat 21 nov 12:35). Drie nieuwe voorbeelden (Rusty's Retirement, Tiny Pasture, Cornerpond: korte tekst, eerste 5 schermen, trailerlengte, tags, aankondigingen), daaruit: nieuwe korte tekst (soort en plek voorop), lange tekst ingekort tot ±215 woorden, schermvolgorde met bureaublad plus pijl op plek 1 en een nieuw scherm "naast echt werk". Graag keuren met de skill `keuren`, vooral: klopt elke zin met de build, en kloppen mijn tellingen. Tekst blijft CONCEPT tot Thijs. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 21 nov 2026 ±14:55 UTC, Iris (eigen logboek): Steam-paginaconcept gekeurd
Concept van Sanne (23454d4) gekeurd: akkoord nee om één zin ("got away with your gold" klopt niet met de build). Alle tellingen en de drie voorbeelden zelf nagerekend met curl en schermen bekeken: kloppen. Berichten Sanne en hoofdchat. Volgende: haar fix nakijken (alleen die zin), scherm 1 met pijl en scherm 5 keuren als ze er zijn, speeltest na de antwoorden van Thijs. Let op: `git pull` hangt nog steeds; `timeout 60 git fetch` plus rebase werkt.

## 21 nov 2026 ±17:40 UTC, Iris (eigen logboek): paginaconcept akkoord ja
Fix van Sanne 2b1a321 nagekeken: goud-zin weg, A5 en A6 verwerkt, akkoord ja. Spelcode op main niet veranderd, geen speeltestantwoorden van Thijs, scherm 1 en 5 nog niet gemaakt. Berichten Sanne en hoofdchat. Volgende: scherm 1 en 5, speeltest na de antwoorden van Thijs.

## 21 nov 2026 ±18:55 UTC, van Sanne: scherm 1 met pijl staat klaar om te keuren
`ontwerp/steam/winkelpagina/concept-21nov/1-bureaublad-pijl.png` (en `-600.png`), LEESMIJ ernaast. Het gekeurde bureaubladbeeld ongewijzigd, plus witte gebogen pijl naar de strook en "Lives above your taskbar" (CONCEPT). Scherm 5 heb ik bij Olaf gevraagd. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 21 nov 2026 ±20:50 UTC, van Sanne: scherm 5 klaar voor keuring
`ontwerp/steam/winkelpagina/concept-21nov/5-naast-werk.png` (en `-600.png`), uitleg onderaan `concept-21nov/LEESMIJ.md`. Beeld komt ongewijzigd uit de bevroren build (run 44934704337, held-2-b), geen eigen tekst erop. Open punt: "Recycle Bin" half bedekt; nieuwe opname met venster op x ±90 gevraagd aan Olaf, dan wissel ik hetzelfde moment. Scherm 1 met pijl ligt ook nog bij je.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 21 nov 2026 ±22:50 UTC, Iris (eigen logboek): scherm 1 en 5 gekeurd
Beide akkoord nee, één moet elk: tekst op scherm 1 botst met Valve-regel "geen marketing copy op schermen" (DERDEN), scherm 5 is 1280 x 720 en Valve vraagt 1920 x 1080. Nieuwe opname Olaf (Recycle Bin vrij) bekeken, mooier, maar zelfde maat. Berichten Sanne, Olaf, hoofdchat. Spelcode op main niet veranderd. Volgende: fixes nakijken, speeltest na de antwoorden van Thijs. `git fetch` van tak schermen hangt; raw.githubusercontent met curl werkt.

## 21 nov 2026 ±21:45 UTC, van Sanne: scherm 1 na je keuring, graag nakeuren
Moet 1 gedaan: "Lives above your taskbar" is van scherm 1 af, alleen de pijl; pijlpunt naar links, wijst nu op Gloop met zijn hoed (kan C2). GEZIEN op 600 breed. Bestanden: `ontwerp/steam/winkelpagina/concept-21nov/1-bureaublad-pijl.png` (+ `-600`), script en LEESMIJ. Concept regel 90 heeft nu de Valve-zin (DERDEN) in plaats van de GOK; punt 3 bij "Open voor Thijs" vervallen. Moet 2: LEESMIJ verbeterd (minimaal 1920 x 1080, DERDEN); de nieuwe opname op 1920 x 1080 heb ik bij Olaf gevraagd, scherm 5 stuur ik je als die er is.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 21 nov 2026 ±22:45 UTC, van Olaf: scherm 5 opnieuw op 1920 x 1080
Run 44955974789 (zaad 1795340417, Kladblok vanaf x 135, strook 160 omdat het spel niet hoger kan), echte 1920 x 1080, niet opgeschaald. Map op tak schermen: `steam-hol/winkel-1920-week-160-zaad1795340417-run44955974789-werkvenster-run44955974789-scherm1920/bureaublad/`. Sanne kiest het beeld en stuurt het naar jou.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 22 nov 2026 ±13:45 UTC, van Sanne: scherm 5 op 1920 x 1080, graag nakeuren (samen met scherm 1)
Moet 2 opgelost: `ontwerp/steam/winkelpagina/concept-21nov/5-naast-werk.png` is nu held-2-b uit run 44975368948 (kladblok=laag, zonder schuifbalk), echte 1920 x 1080, niet opgeschaald, ongewijzigd uit de opname. Recycle Bin vrij. Daan keurde de opname al groen (`platformen/steam/keuring/2026-11-22-kladblok-laag-nakeuring.md`). Uitleg onderaan `concept-21nov/LEESMIJ.md`. Scherm 1 (alleen pijl) ligt ook nog bij je voor nakeuring. Bron ophalen met curl via raw.githubusercontent (git fetch van tak schermen hangt).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 22 nov 2026 ±10:50 UTC, Iris (eigen logboek): scherm 1 en 5 nagekeurd, beide akkoord ja
Keuring `platformen/steam/keuring/2026-11-22-scherm1-en-5-nakeuring.md`. Scherm 5 hash gelijk aan bron run 44975368948. Berichten Sanne en hoofdchat. Volgende: speeltest na de antwoorden van Thijs.

## 22 nov 2026 ±13:40 UTC, Iris (eigen logboek): niets te doen
Spelcode Hats op main niet veranderd, geen speeltestantwoorden van Thijs, geen nieuwe keurtaak. Volgende: speeltest na de antwoorden van Thijs.

## 22 nov 2026 ±17:40 UTC, Iris (eigen logboek): niets te doen
Spelcode Hats op main niet veranderd sinds 13:40, geen speeltestantwoorden van Thijs, geen nieuwe keurtaak. Volgende: speeltest na de antwoorden van Thijs.

## 22 nov 2026 ±21:45 UTC, Iris (eigen logboek): niets te doen
Spelcode Hats op main niet veranderd sinds 17:40 (laatste 01076b3), geen speeltestantwoorden van Thijs, geen nieuwe keurtaak. Volgende: speeltest na de antwoorden van Thijs.

## 23 nov 2026 ±11:45 UTC, Iris (eigen logboek): niets te doen
Spelcode Hats niet veranderd (main kreeg vannacht een nieuwe geschiedenis vanaf c69b121, geen commit sindsdien raakt `producten/steam-hol`, geen bericht over Hats-werk), geen speeltestantwoorden van Thijs, geen nieuwe keurtaak. Volgende: speeltest na de antwoorden van Thijs.

## 23 nov 2026 ±12:05 NL, van hoofdchat: nooit meer een lege run (Thijs 23 nov)
Thijs wil een team dat veel doet in elke run. Heb je niets te keuren of te doen, pak dan dit, in volgorde:
1. Keur de nieuwe filmpjes op plezier en beeld (zelfde lat als de Hats-schermen): concepten in `marketing/wachtrij/` met kanaal youtube-short en status open, en de renders in release studio-1. Oordeel in `marketing/keuring/` met de skill keuren.
2. Kijk de Shorts die al live staan (YouTube RSS van UCTspMNCOwnBkGT2LZ7tB2dg) en schrijf per Short in één zin wat het eerste beeld beter kan, naar `berichten/regisseur.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±16:30 UTC, Iris (eigen logboek): eerste beelden live Shorts bekeken
Geen wachtrij-concept met status open (fit-hook-a en -b staan op wacht, knee-hook A en B al groen door Daan), dus punt 2 van de hoofdchat gedaan: 7 live Shorts (RSS) op hun eerste 3 s bekeken, per Short één zin naar `berichten/regisseur.md`, plus waarschuwing dat fit-hook A en B het afgekeurde MakeHuman-figuur tonen. Spelcode Hats niet veranderd, geen speeltestantwoorden. Volgende: fit-hooks keuren zodra ze open staan.

## 23 nov 2026 ±17:50 UTC, Iris (eigen logboek): fit-hooks gekeurd
Fit-hook A en B (regisseur-2) bekeken: beeld ja, status wacht tot Pro 1.2.x op Gumroad. Berichten Regisseur en hoofdchat. Spelcode Hats niet veranderd (alleen een actions-log-commit), geen speeltestantwoorden. Volgende: tip-gat en tip-maat keuren zodra ze open staan.

## 23 nov 2026 ±21:50 UTC, Iris (eigen logboek): tip-gat-v2 en tip-maat-v2 gekeurd
Beide beeld ja, alleen kan-punten (eerste beeld sterker). Berichten Regisseur en hoofdchat. Spelcode Hats niet veranderd, geen speeltestantwoorden. Volgende: nieuwe tips (dikte, plat, glad) keuren zodra ze open staan.

## 24 nov 2026 ±23:41 UTC, Iris (eigen logboek): vijf tips gekeurd
Dikte-v2, plat-v2, glad, voet, binnen: alle vijf beeld ja, alleen kan-punten (eerste beeld toont het probleem niet, behalve bij binnen). Berichten Regisseur en hoofdchat. Spelcode Hats niet veranderd (alleen volgorde-stem van Sanne), geen speeltestantwoorden. Volgende: nieuwe tips keuren zodra ze open staan.

## 24 nov 2026 ±03:50 UTC, Iris (eigen logboek): tip-val, tip-tekst, tip-export gekeurd
Alle drie beeld ja, Moet geen; grootste kan bij val (stip buiten de voet niet te zien) en export (probleem en bewijs niet in beeld). Berichten Regisseur en hoofdchat. Spelcode Hats niet veranderd, geen speeltestantwoorden. Rechtzetting: mijn vorige regel hoort bij 23 nov ±23:41 UTC, niet 24 nov. Volgende: nieuwe tips keuren zodra ze open staan.

## 24 nov 2026 ±09:20 UTC, Iris (eigen logboek): tip-dubbel en pro-robot-delen gekeurd
Beide beeld ja, Moet geen; grootste kan bij de robot (kop door het hoofd bij HONEST, zin 9 delen niet zichtbaar uit elkaar). Berichten Regisseur en hoofdchat. Spelcode Hats niet veranderd, geen speeltestantwoorden. Volgende: pro-botnamen en pro-enkels keuren zodra ze open staan.

## 24 nov 2026 ±11:50 NL, van hoofdchat-ronde: cc-fit en cc-pas keuren
Graag beeldkeuring van de twee Click Cuts-Shorts in `marketing/wachtrij/`: `2026-11-30-yt-short-cc-fit.md` en `2026-12-01-yt-short-cc-pas.md` (release `regisseur-20`, `cc-pas-geluid.mp4`). Geen haast tot de zip van do 27 nov, wel vóór vr 27 nov, zodat ze klaarstaan als Click Cuts live gaat. Uitslag in het wachtrijbestand en een regel in `berichten/regisseur.md`.
Webpagina's lees je met curl in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±12:00 UTC, Iris (eigen logboek): cc-fit, cc-pas, cc-nummers gekeurd
cc-pas en cc-nummers beeld ja; cc-fit nee om M1 (belofte pennen in elke snede tegen lijmmelding). Berichten Regisseur en hoofdchat. Spelcode Hats niet veranderd, geen speeltestantwoorden. Volgende: cc-fit nakeuren op M1, en de volgende Click Cuts-Shorts.

## 24 nov 2026 ±16:50 UTC, Iris (eigen logboek): cc-fit nagekeurd, vier Shorts gekeurd
cc-fit M1 opgelost; pro-botnamen, pro-enkels, tip-speling, tip-es-kogel beeld ja, Moet geen; grootste kan bij enkels (knie buigt, niet de enkel). Berichten Regisseur en hoofdchat. Spelcode Hats niet veranderd, geen speeltestantwoorden. Volgende: nieuwe Shorts keuren zodra ze open staan.

## 24 nov 2026 ±17:40 NL, van hoofdchat: keuren tot een 8 (besluit Thijs 17:34)
Thijs wil dat Hats doorgaat tot een 8 of 9. Keur elke ronde waarin main voor Hats veranderde, met dezelfde vier cijfers als op 19 nov en per cijfer wat er nog mist om een 8 te halen. Je keurt pas "klaar voor Thijs" als Leuk en Aandacht allebei ≥ 8 zijn. Wees streng: een 8 betekent dat je zelf na 5 minuten nog wilt kijken.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±19:30 NL, van Sanne: keur het plan inhoud-100 op plezier
`producten/steam-hol/inhoud-100.md`: 100 dingen (vallen, drankjes, kamers, helpers, hoeden, gebeurtenissen) en 21 voor de demo, elke 2 tot 3 min iets nieuws in de eerste 30 min, gericht op jouw top 3 (stil gat na hol 2, eerste koop na 141 tot 206 s, gat min 20,7 tot 27,7). Vraag: is elk demo-ding in een blik van 30 s grappig, en welke 5 zou jij eerst bouwen? Uitslag onderaan `berichten/sanne.md`. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±21:05 NL, van hoofdchat: ALLEEN UITERLIJK tot het product plek 1 haalt (Thijs 20:50 en 20:59)
Thijs: eerst moet alles er spectaculair uitzien en opvallen, dan pas marketing, dan doorbouwen. Geen geld voor gekochte plaatjes: we maken het zelf. **Nieuwe harde regel 9 in CLAUDE.md:** een hoofdbeeld, omslag, thumbnail of eerste beeld gaat pas live als het GESLAAGD is in de blinde test door Gemini en ChatGPT (`organisatie/blindtest/LEESMIJ.md`). Eerste uitslag staat in `organisatie/blindtest/uitslag/`: onze cover plek 2 achter Cleave; held-3 voor-na plek 4 (geen tekst, niemand snapt wat het doet); beide rechters willen een gedetailleerd personage in plaats van de tekenpop en een echte print. Lees ook `organisatie/lat/wat-thijs-wil.md`. Geen marketing, geen nieuwe functies: alleen uiterlijk en gevoel.
**Hats:** eerst het kernmoment (bericht van 20:25 in berichten/sanne.md en olaf.md): de val krijgt een klap, een reeks wordt beloond, graven en kopen voelen goed, een keuze met spanning. Daarna de graphics: zelf maken, geen gekochte pakketten, wel feller, scherper en meer kleurverschil (etalage-audit punt 10). Daan en Sanne maken een blinde-testset van ons beste scherm tegen Rusty's Retirement, Spirit City en Desktop Defender. Iris keurt het spelgevoel op ware maat, minstens een 8.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±22:05 NL, van hoofdchat: nieuw team, werk komt nu uit GitHub-issues
Vanaf nu staat je werk in een GitHub-issue met jouw label en een blok "Klaar als" (zie je nieuwe vaste opdracht en `organisatie/team-plan-2026-11-24.md`). Dat issue gaat voor oudere berichten hieronder of hierboven. De beelden van Click Joints Pro en Click Cuts maakt voortaan de Beeldmaker; de kunst van Hats Mila. Kaart van je product: `producten/<naam>/KAART.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±01:00 NL, Iris (eigen logboek): build 52aa730 gekeurd
Leuk 7, aandacht 7, mooi 6 (GOK); klachten Thijs: lopen 6, tekst 4, controle 5. Blinde test met echt beeld uit de build gestart (`hats-speelscherm-build`). Uitslag in issue #7.

## 25 nov 2026 ±05:00 NL, Iris (eigen logboek): build f6aa9b6 gekeurd
Leuk 7, aandacht 7, mooi 7 (GOK); lopen 7, tekst 5, controle 6. App-balk GEZIEN goed. Grootste gat: 24 s stilte aan het begin, tekst ±8 px, geen geluid. Uitslag in issue #7.

## 25 nov 2026 ±09:00 NL, Iris (eigen logboek): build 46cdec1 gekeurd
Leuk 7, aandacht 6, mooi 7 (GOK); lopen 7, tekst 6, controle 6. Krijtbord en val-flits GEZIEN goed; eerste klap pas op 37 s en 55 s zonder goud. Uitslag in issue #7, cijfer lopen in #25.

## 25 nov 09:30, van hoofdchat (namens Thijs)
Hats wordt **rustig**: zacht leven (figuren doen vanzelf kleine dingen), zeldzame momenten die nooit dringend zijn, geen timers of oppassen. Mijn eerdere idee "elke 10 tot 15 s iets" is ingetrokken. Het gat van 55 s zonder goud is dus geen fout op zich; wel moet er na 2 min wegkijken iets veranderd zijn en een keuze klaarstaan. Lees `organisatie/lat/wat-thijs-wil.md`, kop "Hats: rustig, niet druk".

## 25 nov 2026 ±12:50 NL, Iris (eigen logboek): build e39939e gekeurd
Leuk 7, aandacht 7, mooi 7, duidelijk 7 (GOK); lopen 8, tekst 6. Klap op 44,7 s GEZIEN mooi, echte eerste minuut stil na 24 s. Blinde test `hats-speelscherm-e39939e` gestart. Uitslag in issue #7.

## 25 nov 2026 ±17:00 NL, Iris (eigen logboek): build 77d657f gekeurd
Leuk 7, aandacht 7, mooi 7, duidelijk 8, tekst 8 (GOK). Bordregels grappig maar weg na 6 s en ver van de held; hol verandert niet na minuut 4 zonder kopen. Blinde test `hats-speelscherm-77d657f` gestart. Uitslag in issue #7.

## 25 nov 2026 ±17:20 NL, van Mila: de film die je vroeg (10 min, speler koopt, met geluid)
`producten/steam-hol/bewijs-koper/koper-10min-1920-ware-grootte.mp4` (605 s, 1920 x 120, main 2da580e). De speler doet wat de les zegt en koopt elk ding als het al 8 s kan. Ring en les in echt spel: ring aan op 188,4 s, les "Click Gloop to grow him." tegelijk, klik op 194,5 s, gekocht op 197,3 s, Gloop groter (GEZIEN). Let op voor regel 4: in 10 min maar 2 aankopen (197 en 510 s), daartussen ruim 5 min niets te kopen. Uitleg: `bewijs-koper/LEESMIJ.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±20:55 NL, Iris (eigen logboek): build d27cfc3 gekeurd
Leuk 7, aandacht 7, mooi 7 (GOK). Hoedentoren en geen stilte GEZIEN goed; na de eerste koop 6 min alleen vluchten en 6 tot 8 min tussen koop 1 en 2 bij 4 zaden. Blinde test `hats-speelscherm-d27cfc3` gestart. Uitslag in issue #7.

## 25 nov 2026 ±22:55 NL, Iris (eigen logboek): build 369bfca gekeurd
Leuk 8, aandacht 7, mooi 7, duidelijk 8 (GOK). Koopgeluk en 4 aankopen in 15 min GEZIEN bij 4 zaden; na de vierde koop 5 tot 7 min geen keuze (Royal Gloop 160 niet gehaald). Big Gloop leest als koop (#76 ja). Blinde test `hats-speelscherm-369bfca` gestart. Uitslag in issue #7.

## 26 nov 2026 ±00:55 NL, Iris (eigen logboek): build c32f7a4 gekeurd
Leuk 8, aandacht 7, mooi 7, duidelijk 8 (GOK). Aankopen zichtbaar zonder tekst (#76 ja), lichtplas GEZIEN goed; na de vierde koop nog steeds 5,5 tot 7,5 min geen keuze bij 4 zaden (Royal Gloop 160 niet gehaald, eind 127 tot 157). Uitslag in issue #7.

## 26 nov 2026 ±02:50 NL, Iris (eigen logboek): build 45b234e gekeurd
Leuk 8, aandacht 7 (dichtbij), mooi 7, duidelijk 8 (GOK). Royal Gloop op de troon en veren GEZIEN mooi; langste gat zonder koop 215 tot 304 s bij 5 zaden (was 336 tot 454). Uitslag in issue #7.

## 26 nov 2026 ±04:50 NL, Iris (eigen logboek): build 8e50c87 gekeurd
Leuk 8, aandacht 7, mooi 7, duidelijk 8 (GOK). Grond in lagen GEZIEN goed maar weg na het graven; langste gat zonder koop 207 tot 395 s bij 4 zaden (pech: reeks vluchten). Blinde test `hats-speelscherm-troon-8e50c87` gestart. Uitslag in issue #7.

## 26 nov 2026 ±07:00 NL, Iris (eigen logboek): build 9b2c518 gekeurd
Leuk 8, aandacht 7, mooi 7, duidelijk 8 (GOK). Minuut 4 tot 12 nu goed (gat tussen koop 2 en 6 hooguit 146 s, 6 zaden GEZIEN); na de zesde koop 193 tot 333 s niets te kopen (#145). Spullen in de gang GEZIEN beter. Blinde test `hats-speelscherm-troon-9b2c518` gestart. Uitslag in issue #7.

## 26 nov 2026 ±09:00 NL, Iris (eigen logboek): build 499fd9f gekeurd, #7 dicht
Leuk 8, aandacht 8, mooi 7, duidelijk 8 (GOK). Na minuut 4 hooguit 150 s zonder keuze tot minuut 20 bij 6 zaden (GEZIEN). Open: stap 4 tot 6 zonder beeld, gangwand nog roze buis. Blinde test `hats-speelscherm-20min-499fd9f` gestart.

## 26 nov 2026 ±13:00 NL, Iris (eigen logboek): build 3fddb22 gekeurd (#163)
Leuk 8, aandacht 7, mooi 7, duidelijk 8 (GOK). Gouden stenen stap 4 tot 6 GEZIEN goed; gang nog één kleur, dingen te klein op 1x, bord leest als los venster. Gat na minuut 4 tot 246 s. Blinde test `hats-speelscherm-20min-3fddb22` gestart.

## 26 nov 2026 ±15:00 NL, Iris (eigen logboek): build 26b42a6 gekeurd (#163)
Leuk 8, aandacht 8, mooi 7, duidelijk 8 (GOK). Gang niet meer roze maar doffer; stekelput leest als lichte plak zonder stekels (eens met Daan #183). Na minuut 4 hooguit 193 s zonder keuze, 5 van 6 zaden onder 160 s. Blinde test `hats-speelscherm-20min-26b42a6` gestart.

## 26 nov 2026 ±17:00 NL, Iris (eigen logboek): build bb298d3 gekeurd (#163)
Leuk 8, aandacht 8, mooi 7 dichtbij 8, duidelijk 8 (GOK). Plak weg, steen met voegen, grotere kamerstukken en worm GEZIEN goed; een dichte put is nu onzichtbaar (alleen ruit), bord nog los venster. Blinde test `hats-speelscherm-20min-bb298d3` gestart.

## 26 nov 2026 ±21:00 NL, Iris (eigen logboek): build 5ecaf64 gekeurd, #163 dicht
Leuk 8, aandacht 8, mooi 8, duidelijk 8 (GOK). Luik op elke dichte put GEZIEN op 1x; wand leest als metselwerk maar zacht. Na minuut 4 hooguit 172 s zonder keuze bij 6 zaden. Blinde test klaargezet, geen tegoed (Gemini 402, ChatGPT 429).

## 27 nov 2026 ±01:05 NL, Iris (eigen logboek): build 74f03c9 gekeurd (#223)
Leuk 8, aandacht 8, mooi 8, duidelijk 8 (GOK). Wand nu scherp steen in tint, luik blijft hout onder kleine ruiten, rood blokje weg (GEZIEN). Voor een 9: bovenste gang zacht en leeg, bruine steensoort valt weg. Twee zaden met gat boven 180 s, waarschijnlijk last (10 fps), opnieuw meten. Blinde test klaargezet, geen tegoed.

## 27 nov 2026 ±03:30 NL, Iris (eigen logboek): build aef9f5f gekeurd (#239, dicht)
Leuk 8, aandacht 8, mooi 8, duidelijk 8, helden vallen op 7 (GOK). Tekens en klap GEZIEN op 1x; lijf van de held niet (geen rand, verdwijnt in het fakkellicht), issue #242 voor Sanne. Tempo één voor één: 1 van 6 zaden boven 180 s (189 s), dus vooral last in #223.

## 27 nov 2026 ±06:55 NL, Iris (eigen logboek): build deea47d gekeurd (#245, dicht)
Leuk 8, aandacht 8, mooi 8, duidelijk 8, helden vallen op 8 (GOK). Rand om de held GEZIEN op 1x: links in het fakkellicht los van de gele stenen. Voor een 9: donker geklede held in het midden valt weg tegen de donkere stenen, schaduwvlek bijna onzichtbaar. 11 aankopen, langste gat na minuut 4 178 s.

## 27 nov 2026 ±09:00 NL, Iris (eigen logboek): build 1b0e933 gekeurd (#255, dicht)
Leuk 8, aandacht 8, mooi 8 dicht bij 9, duidelijk 8, helden vallen op 8 (GOK). Bovenste gang en rode baksteen GEZIEN goed op 1x. Voor een 9: lege onderste helft van het bord, donker pak in het midden, bovenste gang één tint. Langste gat na minuut 4 183 s.

## 27 nov 2026 ±11:00 NL, Iris (eigen logboek): build f0c2a6a gekeurd (#263)
Leuk 8, aandacht 8, mooi 8 dicht bij 9, duidelijk 8, helden vallen op 8 (GOK). Bord klapt in GEZIEN goed; als er iets te koop is staat alleen het goud op een lege plank. Langste gat na minuut 4 178 s. Blinde test `hats-speelscherm-20min-f0c2a6a` GESLAAGD (Gemini plek 2 en 2, eerste keus Rusty; "muddy, laat helden meer opvallen").

## 27 nov 2026 ±13:15 NL, Iris (eigen logboek): build 3240a1b gekeurd (#271)
Leuk 8, aandacht 8, mooi 8 dicht bij 9, duidelijk 8, helden vallen op 9 (GOK). Donker pak op blauwgrijze steen staat nu los (GEZIEN naast licht=0); randje is zacht en niet op spelpixels, leest op 2x als sticker. Langste gat na minuut 4 133 en 180 s in twee runs. Blinde test `hats-speelscherm-20min-3240a1b` gestart.

## 27 nov 2026 ±15:00 NL, Iris (eigen logboek): build 4329a3a, minuut 0 tot 60 gekeurd (#279)
Minuut 0 tot 20: leuk 8, aandacht 8, mooi 8. Minuut 20 tot 60: leuk 6, aandacht 6, mooi 8 (GOK). Laatste koop op 1498 s, daarna 35 min niets te kopen en goud tot 1517; 84 hoeden maar toren en berg zien er op min 60 uit als op min 25 (GEZIEN). Issue #280 bij Sanne.

## 27 nov 2026 ±17:00 NL, Iris (eigen logboek): build 43879de, minuut 20 tot 60 gekeurd (#286)
Leuk 7, aandacht 7, mooi 8 (GOK; was 6, 6, 8). Berg groeit zichtbaar, koop elke 318 tot 457 s (GEZIEN); robijnkoop is op 1x een ruitje van 5 px en na minuut 25 gebeurt niets nieuws. Issue #291 bij Sanne, blinde test `hats-speelscherm-60min-43879de` gestart.

## 27 nov 2026 ±21:00 NL, Iris (eigen logboek): main b4d960c, minuut 20 tot 60 gekeurd (#301, dicht)
Leuk 8, aandacht 8, mooi 8 (GOK; was 7, 7, 8). Robijnen groot op 1x, reuzen op 1458, 1970, 2522, 3263 s, langste gat zonder koop of reus 386 s (GEZIEN). Voor een 9: reus is vooral een kroon, lijf ±1,3 keer; linker deel van het hol verandert niet. Blinde test `hats-speelscherm-60min-b4d960c` gestart.

## 27 nov 2026 ±23:00 NL, Iris (eigen logboek): main 8a2c2ff (spel e0ed18c), minuut 0 tot 20 als nieuwe speler (#316, dicht)
Leuk 8, aandacht 8, mooi 8 (GOK). 12 kopen, eerste op 79 s, langste gat 141 s (GEZIEN, zaad 11). Voor een 9: 43 s op "2 gold to go" voor de eerste koop, linker helft leeg in minuut 0 tot 2, bovenkamer vaag op 2x. Blinde test `hats-speelscherm-minuut0-e0ed18c` gestart.
