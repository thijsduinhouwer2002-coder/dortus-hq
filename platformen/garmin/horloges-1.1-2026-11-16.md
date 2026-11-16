# Ebb 1.1: welke horloges erbij kunnen (Gijs, 16 nov 2026, run 121)

Aanleiding: Joris mat (verhaal 19) dat meer horloges de grootste knop is voor een betaalde app, en dat bij 90%+ van de betaalde apps die 10+ haalden onder meer de Enduro 2 en 3 en de Instinct 3 AMOLED staan. Ebb 1.0.1 heeft 55 modellen. Dit is de lijst voor de stap daarna.

## Wat de SDK kent (GEZIEN)

Bron: het log van de job bouw, run 43915975753; de hele tabel staat in `sdk-horloges-2026-11-16.txt` (173 horloges, met scherm, schermsoort en geheugen).

| Horloge (id in de SDK) | Scherm | Geheugen | In Ebb 1.0.1 | Wat nodig is |
|---|---|---|---|---|
| `enduro3` | 280 MIP | 786 kB | nee, eruit gehaald | proef loopt (tak `claude/garmin-ebb-enduro3-proef`): simulator stopte twee keer bij start 62 |
| `instinct3amoled45mm` | 390 AMOLED | 786 kB | nee | proef goed (run 43936258914 groen, alle 22 scènes gezien als blad), map gelijk aan epix Pro 42 mm; wacht op Daan |
| `instinct3amoled50mm` | 416 AMOLED | 786 kB | nee | zelfde proef (alle 22 gezien als blad), map gelijk aan Forerunner 265; wacht op Daan |
| `instinctcrossoveramoled` | 390 AMOLED | 786 kB | nee | eigen knoptekst (ENTER) en er lopen echte wijzers over het scherm: eerst zien hoe dat eruitziet, later |
| `approachs50`, `approachs7042mm` | 390 AMOLED | 786 kB | nee | golfhorloges met aanraakscherm; knoptekst zoals de Venu's (PRESS); lage voorrang |
| `approachs7047mm` | 454 AMOLED | 786 kB | nee | idem |
| `fenix9pro51mm` | 466 AMOLED | 786 kB | nee | nieuwe schermmaat: letters, cijfers en plaatjes op 466, langs Mila en Daan |
| `venusq2`, `venux1` | vierkant | 786 kB | nee | eigen opmaak, later |
| Descent (`descentg2`, `descentmk3...`) | 390 en 454 | 786 kB | nee | bewust niet: Ebb wil niet bij duiken horen |
| `enduro2` | bestaat niet in de SDK | | | GOK: de Enduro 2 valt onder `fenix7x` (zit al in Ebb). Na de upload van 1.0.1 nakijken in de winkel |

Niet zinvol voor een betaalde app (staan niet op de lijst van Garmin voor betaalde apps, zie `proefstand-en-codes-2026-11-16.md` deel 4): fēnix 6 zonder Pro, Forerunner 245, 745 en 945, vívoactive 4, Venu (eerste).

## Hoe de knoppen heten (GEZIEN in de handleidingen van Garmin, opgehaald met curl op 16 nov ±19:10 UTC)

| Horloge | Knop rechtsboven | Knop rechtsonder | Bron |
|---|---|---|---|
| Instinct 3 AMOLED | `GPS` en `START/STOP`: "Press to choose an option in a menu", "start or stop an activity" | `BACK` en `SET`: "Press to return to the previous screen" | `https://www8.garmin.com/manuals/webhelp/GUID-2DA54DF8-8084-40ED-954F-EDA09C13B47F/EN-US/Instinct_3_AMOLED_OM_EN-US.pdf`, hoofdstuk Buttons |
| Instinct Crossover AMOLED | `ENTER` en `GPS` | `BACK` en `SET` | `https://www8.garmin.com/manuals/webhelp/GUID-B613EA0B-EFB7-451C-BA10-DB9EE5A990BF/EN-US/Instinct_Crossover_AMOLED_OM_EN-US.pdf`, hoofdstuk Buttons |
| Approach S70 | "Action button" (geen woord op de knop genoemd) | "Back button"; midden "Menu button" | `https://www8.garmin.com/manuals/webhelp/GUID-0F89E6A5-EC1C-4382-964E-27DC4B5FC932/EN-US/GUID-C4EE9EF3-5007-41D9-B84F-4582440483AE.html` |

Wat dit betekent: mijn oude aanname "op de Instinct heet de knop niet START" klopt niet voor de Instinct 3 AMOLED. De handleiding noemt de knop START/STOP en de andere BACK. De teksten van Ebb ("press START to breathe", "BACK: pause.") kloppen daar dus zonder wijziging in de code. Ook GEZIEN op de kast van het horloge in de simulator (run 43936258914): rechtsboven GPS en START/STOP, rechtsonder BACK en SET. Geheugen in de simulator: hoogstens 146 kB van 764 kB. Niet gezien: een echt horloge.

## Volgorde (voorstel)
1. Instinct 3 AMOLED 45 en 50 mm: als de proef goede beelden geeft, naar Daan. Geen wijziging in de code.
2. Enduro 3: hangt af van de proef.
3. fēnix 9 Pro 51 mm (466): nieuwe maat, met Mila.
4. Approach en Crossover: pas als 1 tot 3 klaar zijn en de cijfers van 1.0.1 laten zien dat meer horloges helpt.
Versie 1.1 gaat pas naar Thijs als 1.0.1 in de winkel staat; twee uploads door elkaar wil niemand.
