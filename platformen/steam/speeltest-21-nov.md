# Speeltest Hats of the Fallen, zaterdag 21 nov 2026 (ruwe versie)

Voor Thijs. Opgezet door Olaf, 15 nov 2026. Doel (besluit Thijs 15 nov 19:35): zien of het **leuk** is voordat het mooi wordt. Lelijke of ontbrekende beelden horen erbij.

**Stand:** de build komt uiterlijk **vr 20 nov 20:00 UTC**. Hieronder staat dan de link naar de run. Tot die tijd is dit bestand een concept.

## De build ophalen (±2 min)
1. Ga naar de run die hieronder bij "Build" staat (je moet ingelogd zijn op GitHub).
2. Onderaan de pagina bij "Artifacts": klik **speeltest-hats-of-the-fallen-windows**. Je krijgt een zip.
3. Pak de zip uit en lees `LEES-MIJ-EERST.txt` (starten, klikken, stoppen). Kort: dubbelklik `HetHol.exe`; zegt Windows "Windows heeft uw pc beschermd", dan "Meer informatie" en "Toch uitvoeren" (de .exe is nog niet ondertekend).

Build: _volgt vr 20 nov_ (workflow `steam-hol-exe.yml` op main, zip 14 dagen bewaard).

Proefrun (werkt, nog niet de build voor jou): https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/43752055212 , main 04d6fad, groen, exe-toetsen 0 FOUT, zip 31 MB met `HetHol.exe` (82,5 MB uitgepakt), GEZIEN 15 nov 19:25 UTC via de API.

## Eigen proef vooraf (Olaf, 15 nov 21:30 UTC)
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
3. **Stoort het?** Zit het hol in de weg bij je werk, klikt er iets mis, wordt je pc traag of lawaaiig?
4. **Kun je het lezen** op je eigen scherm: zie je Gloop, de helden en de hoeden, of zijn het een paar pixels? Te groot of te klein? Rechtsklik op de strook wisselt de maat (96, 120, 160, dan weer 96). (Staat je scherm op 125% of meer, dan begint het spel al op 160.) Zet in je antwoord ook je schermmaat en schaal (Instellingen, Systeem, Beeldscherm, bijvoorbeeld "1920 x 1080, 125%"): het spel rekent in echte schermpixels, dus op een laptop of 4K-scherm met hoge schaal is alles kleiner dan bij ons.

## Drie vragen na afloop (zeg ze in de projectchat, een zin per vraag is genoeg)
1. Wanneer moest je voor het eerst glimlachen, en wanneer verveelde je je (ongeveer welke minuut)?
2. Wat snapte je niet of wilde je doen maar lukte niet?
3. Zou je hem morgen weer aanzetten terwijl je werkt? Waarom wel of niet?

## Wat wij ermee doen
Je punten gaan vóór alles (ook vóór de winkelbeelden). Olaf zet ze bovenaan `platformen/steam/taken.md` en bouwt ze in volgorde.

Waar wij zelf op letten (niet aan Thijs vragen, alleen kijken of het hem opvalt; Sanne 16 nov 22:50): wie veel graaft, heeft zondag goud zonder iets om te kopen (30 min spelen plus een nacht weg geeft ±963 goud, de winkel is 1048). Dat is de demo die ophoudt, geen fout.

## Eerlijk vooraf
- De naam in het bestand is nog Het Hol; het spel heet Hats of the Fallen.
- Geluid kan uit staan of kaal zijn; de beelden zijn deels nog oud of paars.
- Bekend en niet nodig om te melden (keuring Iris 16 nov): de winkel is klein (zes stappen, samen 1048 goud). Laat je het spel een nacht aan, dan koop je de volgende ochtend alles in één keer. De diepe voortgang van ±100 uur (Sanne, `voortgang.md`) zit er nog niet in.
- Niets hiervan is gepubliceerd: de zip staat alleen als bijlage bij een testrun.
