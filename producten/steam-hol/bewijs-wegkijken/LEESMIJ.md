# Wegkijken: het hol groeit ook als je niets koopt (Olaf, 25 nov 2026, issue #86)

Tempo-regel 5 (`organisatie/lat/hats-tempo.md`): na 2 min wegkijken is er iets te zien dat er eerst niet was. In mijn film van 10 min (#79) bleef het hol van minuut 3 tot 10 bijna gelijk voor een speler die niets koopt.

**Wat ik zag vóór de wijziging (GEZIEN, film van 30 min van main 0c04fb7, zelfde instellingen als hieronder):** Gloop had na 30 min nog steeds één hoed (de kroon), want alleen wie Gloop opat gaf een hoed. Bijna elke vangst gaat in een speler die niets koopt via de stekelput, en die hoed verdween met de held in de put. De toren, de hoedenberg en de hoedenwand waren er al (gekeurd), maar kregen niets.

**Wat er veranderde voor de speler:** de hoed van wie in de put valt, valt 1,2 s na de klap van boven op Gloops toren, met de landing van de hoeden van de nacht die er al was (Gloop even blij, hoed wiebelt uit, de onderste springt bij een volle toren op de berg). Geen tekst, geen geluid, geen klok. Pas vanaf Gloops eigen eerste hoed, dus de eerste minuut en de regel van de eerste hoed blijven gelijk; niet in de demo-film. Telt niet als opgegeten (Gloop spuugt geen laarzen van wie hij niet at). Keuze van mij, past bij de naam: Hats of the Fallen, de hoeden van wie viel.

**Bewijs (GEZIEN, Godot 4.3 Linux onder xvfb, `--write-movie --fixed-fps 5`, scherm 1024, `hoogte=120 vers=1 zaad=2 uitleg_klik=6 balk=0`; de proefspeler doet alleen de les en koopt niets):**
- `echt-spel-30min-zonder-kopen.mp4`: 1810 s, ware grootte 1024 x 120, 5 beelden per s, met geluid (piek -12,6 dB).
- Hoeden op Gloop: 1 aan het begin, 27 na 30 min (logregel `HOL put-hoed`, 26 keer). In 95 procent van alle vensters van 2 min (elke seconde een start, 60 tot 1680 s) komt er minstens één hoed bij. Het langste gat zonder nieuwe hoed was 171 s.
- `paar-1` tot `paar-5`: vijf plekken gekozen met een vaste dobbelsteen (Python `random.seed(86)`, 5 starttijden tussen 130 en 1660 s), boven het beeld op t, onder op t + 120 s, alleen het hol (bord rechts weggesneden), 2x. In elk paar is de toren of de berg anders: 154 naar 274 s (toren 2 naar 4 hoog), 193 naar 313 s (toren 3 naar 4), 780 naar 900 s (andere hoeden op de toren, berg groter), 1269 naar 1389 s (4 hoeden erbij), 1651 naar 1771 s (andere bovenste hoed).
- `na-30-min-voor-en-na.png`: boven main zonder deze wijziging na 30 min (één kroon), onder met (toren van 4 en een berg).
- Toetsen 7 x 0 FOUT op Linux; nieuw in `toets_klap.gd`: geen put-hoed vóór Gloops eerste hoed, daarna wel, telt niet als opgegeten, niet in de demo.
- CPU (GOK voor Windows): beelden per 10 s gelijk (51 in beide films); de vaste laag van het hol tekent 30 keer extra in 30 min (eens per nieuwe hoed, 84 tegen 54).

**Eerlijk:** zonder graven is de hoedenwand niet te zien (die hoort bij gegraven gang), dus de groei zit in de toren en de berg. De berg ligt bij 10 of meer hoeden deels voor de blauwe kristallen; dat lees ik als een berg die ervoor ligt, maar Daan kijkt ernaar.

**Code:** `kern/afloop.gd` (`put_hoed`, één regel na de stempel van de put). Bekeken: hoe de hoeden van de nacht al landen (`systemen/slijm.gd`, Bram) en Rusty's Retirement in de lat (de boerderij verandert zichtbaar terwijl je werkt).

## Na de keuring van Daan (#92, ja met twee kanpunten), Olaf 25 nov ±19:45 NL
- **Kristallen niet meer onder de berg (punt 3):** een vloerding dat onder de linkerrand van de hoedenberg zou liggen, schuift hooguit één kolom naar links als daar plek is (geen val, niet naast het vorige stuk); anders wordt het niet getekend, zoals het spinrag bij de berg al deed (`hol/hol_vast.gd`, `vloer_x`). `kristal-niet-onder-berg-voor-en-na-2x.png`: boven main, onder nieuw, zelfde hol (zaad 2, 1024 breed, 27 hoeden op Gloop), GEZIEN: boven half onder de kroon en de berg, onder heel en vrij.
- **Put-hoed achteraan de lopende rij (punt 4):** valt er al een rij hoeden (terugkomen, of een vorige put-hoed), dan gaat de nieuwe achteraan en start de klok van de nacht niet opnieuw (`kern/afloop.gd`). Nieuwe toets in `toets_klap.gd`. Toetsen 7 x 0 FOUT (Linux, GEZIEN).
