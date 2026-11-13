# Het Hol: planning tot het Desktop Companion Fest (hoofdchat, 13 nov 2026)

Besluit Thijs 13 nov 11:51: **beelden blijven eigen werk (route C)**: geen tekenaar, geen AI-beeldtool. Alles uit code, zoals nu. Thijs is het oog voor smaak; herkennen toetst een frisse kijker.

## Vaste data (GEZIEN in de Steamworks-docs, zie `ontwerp/steam/winkelpagina/fest.md`)
- **14 tot 18 jan 2027:** Desktop Companion Fest. Wij doen mee als "binnenkort" met een gratis demo.
- **10 jan 2027:** uiterste aanmelddatum Next Fest februari (zelfde demo mag mee).
- **8 jan 2027:** Valve brengt de fest-trailer; vanaf dan mogen we zelf melden dat we meedoen.
- Valve wil de winkelpagina minstens 2 weken openbaar vóór uitbrengen en keurt een pagina in 1 tot 5 werkdagen (DERDEN).

## Mijlpalen, terug gerekend
| Datum | Wat | Wie keurt |
|---|---|---|
| **vr 20 nov** | **Gloop af**: één figuur helemaal goed op ware grootte (120 px strook). Thijs zegt ja op een blad met hoogstens 3 versies. Een frisse kijker herkent "een slijm met één oog die hoeden draagt" zonder uitleg. | Thijs, frisse kijker |
| **wo 25 nov** | **Helden en winkelbeelden**: 3 heldensoorten in dezelfde stijl als de goedgekeurde Gloop; capsule (header 920x430, klein 462x174, hoofd 1232x706, bibliotheek 600x900) en 5 schermafbeeldingen. | Thijs |
| **ma 30 nov** | **Winkelpagina klaar**: tekst, tags (Desktop Companion, Idler eerst), beelden, prijs. Thijs zegt ja. | Thijs |
| **di 1 dec** | Thijs dient de winkelpagina in bij Steam (hij klikt zelf). | |
| **±8 dec** | Pagina live als "binnenkort", verlanglijsten beginnen. | |
| **vr 18 dec** | **Demo af** volgens de vaste lijst hieronder. Thijs speelt hem zelf 15 minuten en zegt ja. | Thijs |
| **ma 21 dec** | Thijs dient de demo in (3 weken vóór het fest, met de feestdagen ertussen). | |
| **8 jan** | Eigen bericht met de asset kit van Valve. | |
| **10 jan** | Aanmelden Next Fest februari. | |

## Wanneer is de demo klaar? (vaste lijst, zoals bij Ebb: niet "als een keurder een 8 geeft")
1. Volle toetsrun groen op Windows (Actions), geen crash in 60 minuten draaien.
2. Zuinig: gemiddeld onder 1 CPU-seconde per 10 seconden op 120 px; stilstaand beeld bijna 0.
3. De eerste tien minuten zoals in `platformen/steam/features.md`: binnen 30 seconden gebeurt er iets leuks, binnen 10 minuten heb je één keer gekocht.
4. Nooit straffen als je weg bent: terugkomen na 8 uur geeft alleen winst.
5. Strook 96, 120 en 160 px werkt; klikken gaan door de lucht heen.
6. Demo-einde na ongeveer 2 uur speeltijd: een vriendelijke regel, het spel blijft draaien, save gaat mee naar het volle spel.
7. Ja van Thijs op het uiterlijk (Gloop, helden, winkelbeelden) op de vaste momenten hierboven.
Niets nieuws erbij na 18 dec. Wat niet op deze lijst staat, gaat naar na het fest.

## Werkwijze (lessen uit Ebb)
- **Eerst één figuur helemaal goed, dan pas breed.** Geen 22 dingen tegelijk ontwerpen.
- **Thijs keurt smaak, op vaste momenten**, met hoogstens 3 versies per blad, op ware grootte én vergroot.
- **Herkennen toetst iemand die niet weet wat het moet zijn** (een frisse agent die alleen het plaatje krijgt).
- **Geen open keuringsrondes.** Na een ja van Thijs ligt een onderdeel vast.
- **Kleine ploeg:** één bouwer elk uur, één ontwerper, de hoofdchat stuurt en laat Thijs zien. Geen vijf agents tegelijk.
- Webpagina's lees je met `curl` in Bash, nooit met WebFetch.

## Grootste risico (eerlijk)
De winkelafbeelding. Onze huidige header is een uitvergrote spelstrook naast getekende illustraties van de toppers (`ontwerp/steam/winkelpagina/vergelijk-v5-header.png`). Bij Ebb lukte "mooi uit code" niet bij kleine figuren; pixelart op 16 px gaat code beter af, maar een capsule op 920x430 is een ander soort beeld. Halen we op 25 nov geen ja van Thijs op de capsule, dan leggen we de keuze tekenaar of niet opnieuw voor: een tekenaar heeft 1 tot 3 weken nodig, dus later dan 25 nov schuift de winkelpagina op.
