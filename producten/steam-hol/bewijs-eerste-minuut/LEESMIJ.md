# De eerste minuut: altijd één doel met een pijl (Sanne, 25 nov 2026, issue #19 punt 4, bouwblad C)

Thijs 24 nov: "het is niet duidelijk wat je moet doen". Nu leert het spel het je zelf, zonder uitlegscherm.

**Wat de speler ziet (nieuw spel):**
1. 0 tot 4 s: één regel boven het hol, "Hats of the Fallen. Your taskbar has a basement." Daarna nooit meer.
2. Geen tekst: de eerste held valt in de put die er al staat (klap op 7,2 s, van Olaf), de muntjes vliegen naar de schat.
3. 1,6 s na de eerste muntjes: "Click the dirt to dig." met een pijltje dat zacht wipt en een gouden rand die rustig ademt om het vak grond. Klaar bij het eerste gegraven vak, waar ook.
4. "Click the tunnel to set a trap." met pijl en rand om het gangvak onder het nieuwe kamertje. Klaar bij de eerste nieuwe put, waar ook.
5. Klaar: het doel op het bord ("Next: Big Gloop, 19 gold to go") neemt het over. Tijdens de les staat dat doel niet op het bord, zodat er precies één doel in beeld is.
- Doet de speler 20 s niets bij stap 3 of 4: de pijl wipt één keer groter. Nooit een tweede regel.
- Letters 15 px op 120 (12 op 96, 20 op 160), goud op een donker plaatje met gouden rand, in de doorklikbare lucht boven het gras.
- De stap staat in de save: wie halverwege stopt, gaat verder waar hij was. Een oude save zonder die stap krijgt geen les. De demo-film (demo=1) slaat de les over; de Steam-demo krijgt hem wel.
- Spelerstekst is concept tot Thijs hem schrijft.

**Bewijs (GEZIEN, Godot 4.3 Linux onder xvfb, scherm 1024 breed, strook 120, `vers=1 zaad=2 uitleg_klik=6`, 20 beelden per s):**
- `eerste-minuut-60s-ware-grootte.mp4`: 60 s op ware grootte met geluid. Een proefspeler doet na 6 s wat de regel zegt. In de log: welkom 0,0 s, kijken 4,0 s, eerste klap 7,2 s, "dig" 8,9 s, "trap" 14,9 s, klaar 21,0 s.
- `eerste-minuut-strip-2x.png`: welkom (2 s), muntjes na de klap (8 s), dig (11 s), trap (17 s), klaar met twee putten (22 s).
- `bord-zonder-doel-tijdens-les-en-erna-2x.png`: bord tijdens de les zonder doel, erna met doel.
- Save getoetst: nieuw spel begint bij het welkom; na stoppen bij "dig" gaat het spel verder bij "dig"; een save zonder het veld `uitleg` geeft geen les.
- Toetsen 7 x 0 FOUT op Linux (systemen, namen, held, vleermuis, berg_wand, klap, aanloop).

**Code:** `godot/kern/eerste_minuut.gd` (nieuw), `kern/strook.gd` (aanmaken, doel op het bord leeg tijdens de les), `kern/opslag.gd` (veld `uitleg`), `kern/proef.gd` (`uitleg_klik=<s>` voor film en toets).
