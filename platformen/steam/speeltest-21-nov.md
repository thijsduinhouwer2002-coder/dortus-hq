# Speeltest Hats of the Fallen, zaterdag 21 nov 2026 (ruwe versie)

Voor Thijs. Opgezet door Olaf, 15 nov 2026. Doel (besluit Thijs 15 nov 19:35): zien of het **leuk** is voordat het mooi wordt. Lelijke of ontbrekende beelden horen erbij.

**Stand:** de build staat klaar (do 19 nov, een dag vroeg, op de bevroren stand). Link hieronder bij "Build".

## De build ophalen (±2 min)
1. Ga naar de run die hieronder bij "Build" staat (je moet ingelogd zijn op GitHub).
2. Onderaan de pagina bij "Artifacts": klik **speeltest-hats-of-the-fallen-windows**. Je krijgt een zip.
3. Pak de zip uit en lees `LEES-MIJ-EERST.txt` (starten, klikken, stoppen). Kort: dubbelklik `HetHol.exe`; zegt Windows "Windows heeft uw pc beschermd", dan "Meer informatie" en "Toch uitvoeren" (de .exe is nog niet ondertekend).

Build: https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/44597872156 , zip `speeltest-hats-of-the-fallen-windows` (33 MB, te halen tot 3 dec). Main 1cb8219, spelcode gelijk aan de bevroren stand 1f63c27. Groen: bouwen, toetsen op de echte .exe en sluiten via de taakbalk (GEZIEN, Olaf 19 nov 20:40 NL). Eigen proef van 5 zaden volgt vr 20 nov.

Proefrun op de stand van 17 nov (werkt, nog niet de build voor jou): https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/44137119222 , main 816eb97 (spelcode gelijk aan fb00619), groen, exe-toetsen 0 FOUT, sluiten 0 FOUT, zip `speeltest-hats-of-the-fallen-windows` 33 MB, beeld `strook-120-volledig.png` GEZIEN (Olaf 17 nov 17:40 UTC). CPU in deze korte meting 1,77 per 10 s, in lijn met eerdere exe-runs (2,14 / 2,77 / 2,81; deze meting telt het opstarten en kopen mee, niet de duurtest-grens).

Oudere proefrun: https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/43752055212 , main 04d6fad, groen, exe-toetsen 0 FOUT, zip 31 MB met `HetHol.exe` (82,5 MB uitgepakt), GEZIEN 15 nov 19:25 UTC via de API.

## Eigen proef vooraf, opnieuw op main fb00619 (Olaf, 17 nov 17:30 UTC)
Main na terugslag, Dame, naamfamilies en vaste plekjes. Vers spel (geen save), Godot 4.3 Linux onder Xvfb, `vers=1 hoogte=120`, 5 zaden (4242, 777, 2026, 1, 99), 200 tot 240 s. Uit de logs (GEZIEN):
- 4,1 s: eerste held binnen, bij alle vijf.
- 12,8 s: eerste held valt in de stekelput (+6), 15,4 s eerste bladzijde in het heldenboek. **Binnen 30 s gebeurt er iets** (demolijst 3).
- 26,4 tot 27,3 s: **Gloop eet de tweede held, de kroon gaat op de toren** (alle vijf).
- 42 tot 45 s: derde held vlucht met een wrok; 56 tot 69 s komt hij terug, 65 tot 78 s **wint de put ronde twee** (+9, hol-niveau 2).
- 103 tot 119 s: Gloop gaat plat ("Gloop is flat. Back soon."), ±30 s later weer op.
- Eerste koop mogelijk: 132, 137, 144, 180 s, en bij zaad 1 rond 200 s (goud 50 bij het einde). Ruim onder de grens van 600 s.
- Stilste stukken in de kroniek: één keer 22 tot 28 s zonder nieuwe regel, steeds net na de terugkomst (rond 65 tot 78 s). Geen SCRIPT ERROR, alleen de bekende geluidsfout (geen geluidskaart).

Eerlijk: dit is Linux, niet de Windows-build van Thijs; de tijden komen uit de spelklok en zijn op Windows gelijk. De oude proef van 15 nov staat hieronder.

## Eigen proef vooraf (Olaf, 15 nov 21:30 UTC, oudere stand)
Een vers spel (geen save) 150 s laten lopen, Godot 4.3 Linux onder Xvfb, `vers=1 hoogte=120`, twee keer met een ander zaad. Uit de log:
- 4 s: eerste held komt binnen ("Wout brought a torch. And hope.").
- ±10 s: tweede held.
- 16 s: de eerste held valt in de stekelput, +6 goud, eerste bladzijde in het heldenboek. **Dus binnen 30 s gebeurt er iets** (demolijst 3).
- **±27 s: Gloop eet de tweede held en zijn hoed (de kroon) gaat op de toren** (op main sinds 16 nov 07:31 UTC, tak `claude/steam-hol-hoed30` van Bram; zaden 4242, 777, 1, 2026, 99, 2 en 3: hap 26,3 tot 27,8 s; daarvoor 59 tot 62 s, en vóór 16 nov 00:35 UTC 96 tot 102 s).
- ±31 s: derde held, die ontsnapt mank. **±63 tot 75 s: hij komt terug met zijn wrok** (bijnaam, "is back for ...").
- Eerste koop mogelijk na 157 tot 227 s, gemiddeld 196 s (zelfde 5 zaden; met de stand van 16 nov 00:35 UTC gemiddeld 245 s, daarvoor 291 s); eerder op Windows gemeten: 211 s. Ruim onder de grens van 600 s (demolijst 3).
Eerlijk: dit is Linux, niet de Windows-build van Thijs; de tijden komen uit het spel zelf en zijn op Windows gelijk (zelfde code, zelfde klok). Het echte hoedengrapje (Gloop eet, hoed op de toren) komt nu rond 27 s, binnen de eerste halve minuut, en de eerste wrok binnen anderhalve minuut.

## Wat je doet (15 tot 30 min)
- Start het spel en **werk gewoon door** op je pc (mail, browser). Het hol ligt onderaan, boven de taakbalk.
- Klik als je zin hebt: graven, een put zetten, op Gloop klikken om iets te kopen. Lees geen uitleg verder dan het briefje; wat je niet snapt, is precies wat we willen weten.
- Na een kwartier mag je stoppen (rechtsklik op Gloop in de taakbalk, "Venster sluiten"; liever geen Alt+F4, want het hol pakt nooit de focus en dan sluit Alt+F4 misschien je browser). Wil je het later nog eens aanzetten: het spel gaat verder waar het was.

## Waar je op let
1. **De eerste 30 seconden:** gebeurt er iets leuks, of zit je naar een leeg hol te kijken?
2. **De eerste 10 minuten:** kon je iets kopen, en wilde je dat ook?
3. **Stoort het?** Zit het hol in de weg bij je werk, klikt er iets mis, wordt je pc traag of lawaaiig? Kijk na ±10 minuten één keer in Taakbeheer (Ctrl+Shift+Esc, tabblad Processen) welk percentage CPU er bij HetHol staat, en zet dat getal in je antwoord, met je processor (staat onder Prestaties, CPU, bijvoorbeeld "Intel i5-1135G7"). Wij rekenen het om; onze testmachines zijn te wisselend om dat zelf te weten. (Sanne 17 nov 03:55, regel 3 en 4 in `balans.md`.)
4. **Kun je het lezen** op je eigen scherm: zie je Gloop, de helden en de hoeden, of zijn het een paar pixels? Te groot of te klein? Rechtsklik op de strook wisselt de maat (96, 120, 160, dan weer 96). (Staat je scherm op 125% of meer, dan begint het spel al op 160.) Zet in je antwoord ook je schermmaat en schaal (Instellingen, Systeem, Beeldscherm, bijvoorbeeld "1920 x 1080, 125%"): het spel rekent in echte schermpixels, dus op een laptop of 4K-scherm met hoge schaal is alles kleiner dan bij ons.

5. **Na de eerste nacht** (alleen als je hem aan laat staan of de volgende dag weer start): bovenaan komt één regel over wat er gebeurde terwijl je weg was. Schrijf die regel over of maak er een schermafbeelding van, en zeg of je snapte wat er bedoeld werd. (Iris keuring 16, punt 3. Wat onze testmachine na 8 uur gaf staat in `keuring/2026-11-17-04.md`; niet vooraf lezen, dan weten we of het zonder uitleg te snappen is.)

## Vijf vragen na afloop (zeg ze in de projectchat, een zin per vraag is genoeg)
1. **Afhaken:** op welke minuut keek je voor het laatst uit jezelf naar het hol, en waarom keek je daarna niet meer?
2. **Glimlach:** wanneer moest je voor het eerst glimlachen (ongeveer welke minuut), en waarom?
3. **Meer:** waar wilde je meer van (helden, hoeden, graven, kopen, de regels bovenaan)? En wat mag eruit?
4. **Vast:** wat snapte je niet, of wilde je doen maar lukte niet?
5. **Terug:** zou je hem morgen weer aanzetten terwijl je werkt, en zou je hem op je verlanglijst zetten als je hem als demo op Steam vond? Waarom wel of niet?

(Sanne 18 nov. Vraag 1 en 5 wegen het zwaarst: een demospeler beslist vroeg of hij op het verlanglijstje zet.)

## Wat wij ermee doen
Je punten gaan vóór alles (ook vóór de winkelbeelden). Olaf zet ze bovenaan `platformen/steam/taken.md` en bouwt ze in volgorde.

Waar wij zelf op letten (niet aan Thijs vragen, alleen kijken of het hem opvalt):
- Sanne 18 nov: in de duurtest op main (run 44127812882, één zaad) is het stilste stuk zonder iets nieuws **minuut 20,7 tot 27,7**. Noemt hij bij vraag 1 een minuut rond de 20 tot 28, dan is dat dit gat.
- Sanne 16 nov 22:50: wie veel graaft, heeft zondag goud zonder iets om te kopen (30 min spelen plus een nacht weg geeft ±963 goud, de winkel is 1048). Dat is de demo die ophoudt, geen fout.

## Eerlijk vooraf
- De naam in het bestand is nog Het Hol; het spel heet Hats of the Fallen.
- Geluid kan uit staan of kaal zijn; de beelden zijn deels nog oud of paars.
- Bekend en niet nodig om te melden (keuring Iris 16 nov): de winkel is klein (zes stappen, samen 1048 goud). Speel je eerst een half uur en laat je het spel dan een nacht aan, dan kun je de volgende ochtend de rest van de winkel kopen (vanaf een vers hol geeft een nacht ongeveer de helft, Windows-toets Olaf 22:40: +511). De diepe voortgang van ±100 uur (Sanne, `voortgang.md`) zit er nog niet in.
- Na een half uur spelen plus een nacht ben je dicht bij het eind van wat er nu in zit (hol 12 en de zes dingen in de winkel, ongeveer wat de demo wordt). Zondag zie je dus hoe de eerste dag voelt, niet hoe week 3 voelt; die diepte komt in versie 3. Vraag 3 gaat daarom over de eerste dag. (Sanne 16 nov 23:55, na keuring Iris 23:00.)
- Niets hiervan is gepubliceerd: de zip staat alleen als bijlage bij een testrun.
