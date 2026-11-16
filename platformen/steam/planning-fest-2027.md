# Het Hol: planning tot het Desktop Companion Fest (hoofdchat, 13 nov 2026)

Besluit Thijs 13 nov 11:51: **beelden blijven eigen werk (route C)**: geen tekenaar, geen AI-beeldtool. **Aanvulling 13 nov 13:35: de hele app wordt 3D, met code in Blender gemaakt en gerenderd** (zie `ontwerp/steam/3d-stijl.md`). Thijs is het oog voor smaak; herkennen toetst een frisse kijker.

## Vaste data (GEZIEN in de Steamworks-docs, zie `ontwerp/steam/winkelpagina/fest.md`)
- **14 tot 18 jan 2027:** Desktop Companion Fest. Wij doen mee als "binnenkort" met een gratis demo.
- **10 jan 2027:** uiterste aanmelddatum Next Fest februari (zelfde demo mag mee).
- **8 jan 2027:** Valve brengt de fest-trailer; vanaf dan mogen we zelf melden dat we meedoen.
- Valve wil de winkelpagina minstens 2 weken openbaar vóór uitbrengen en keurt een pagina in 1 tot 5 werkdagen (DERDEN).

## Mijlpalen, terug gerekend
| Datum | Wat | Wie keurt |
|---|---|---|
| **ma 16 nov** | **Gloop in 3D**: blad met hoogstens 3 versies voor Thijs (Daan). Zelfde dag: één stukje hol in 3D (Mila) en de eerste render in Godot via de pijplijn (Bram). | Thijs |
| **vr 20 nov** | **Gloop af**: één figuur helemaal goed op ware grootte (120 px strook), in 3D, met animaties in het spel. Thijs zegt ja op een blad met hoogstens 3 versies. Een frisse kijker herkent "een slijm met één oog die hoeden draagt" zonder uitleg. | Thijs, frisse kijker |
| **wo 25 nov** | **Helden, hol en winkelbeelden**: 3 heldensoorten en het hele hol in dezelfde 3D-stijl; capsule (header 920x430, klein 462x174, hoofd 1232x706, bibliotheek 600x900) en 5 schermafbeeldingen. | Thijs |
| **ma 30 nov** | **Winkelpagina klaar**: tekst, tags (Desktop Companion, Idler eerst), beelden, prijs. Thijs zegt ja. | Thijs |
| **di 1 dec** | Thijs dient de winkelpagina in bij Steam (hij klikt zelf). | |
| **±8 dec** | Pagina live als "binnenkort", verlanglijsten beginnen. | |
| **vr 4 dec** | **Speeltest door Thijs**: een speelbare Windows-build die hij zelf 15 minuten speelt. Hij zegt wat saai, onduidelijk of kapot is; dat gaat vóór alles. Les uit TikTok-reacties (15 nov): echte spelers vinden in 10 minuten tientallen punten die agents missen. | Thijs |
| **vr 18 dec** | **Demo af** volgens de vaste lijst hieronder. Thijs speelt hem zelf 15 minuten en zegt ja. | Thijs |
| **ma 21 dec** | Thijs dient de demo in (3 weken vóór het fest, met de feestdagen ertussen). | |
| **8 jan** | Eigen bericht met de asset kit van Valve. | |
| **10 jan** | Aanmelden Next Fest februari. | |
| **vr 15 jan** | **Meetpunt fest** (voorstel Fenna 16 nov 11:15, besluit Olaf): nieuwe verlanglijsten in de festweek tellen (Steamworks, Thijs leest af of geeft het cijfer). | |
| **ma 18 jan** | **Uitslag fest, regel vooraf vastgezet:** minder dan 1.000 nieuwe verlanglijsten in de festweek (GOK als grens, geen eigen cijfers) betekent: de verbeterweek gaat naar de haak (capsule, eerste 30 seconden, korte tekst) en niet naar de demo zelf, en de hoofdchat bekijkt de lanceerdatum van maart opnieuw. Waarom: van 16 kerkerspellen voor de schermhoek met demo haalden er 3 de 100 reviews, mediaan 8 (`platformen/succes/verhalen-spellen.md`, verhaal 8). | hoofdchat |
| **ma 18 jan tot ma 1 feb** | **Verbeterweek demo** (voorstel Fenna 16 nov, besluit Olaf): één verandering in de demo uit wat fest-spelers zeiden (reviews, discussies, streams), geen nieuwe inhoud; daarna de demo opnieuw indienen vóór Next Fest. Waarom: van de 11 bureaubladspellen uit Next Fest juni 2026 deden de spellen die na het fest iets veranderden het beter (`platformen/succes/verhalen-spellen.md`, verhaal 7). | Thijs (indienen) |
| **22 feb tot 1 mrt** | Next Fest februari (demo doet mee). | |
| **di 2 tot do 4 mrt** | **Voorstel uitbrengen** (advies Vera 16 nov, Aanvulling 4 in `platformen/verkenner/steam-desktop-2026-11.md`; Olaf eens). Korting eerste week klaar vóór 18 mrt; niet uitbrengen van 11 tot 25 mrt (Spring Sale). Schuift het: eind maart tot half april. **Besluit ligt bij de hoofdchat.** | hoofdchat |

## Wanneer is de demo klaar? (vaste lijst, zoals bij Ebb: niet "als een keurder een 8 geeft")
1. Volle toetsrun groen op Windows (Actions), geen crash in 60 minuten draaien.
2. Zuinig: gemiddeld onder 1 CPU-seconde per 10 seconden op 120 px; stilstaand beeld bijna 0.
3. De eerste tien minuten zoals in `platformen/steam/features.md`: binnen 30 seconden gebeurt er iets leuks, binnen 10 minuten heb je één keer gekocht.
4. Nooit straffen als je weg bent: terugkomen na 8 uur geeft alleen winst.
5. Strook 96, 120 en 160 px werkt; klikken gaan door de lucht heen.
6. Demo-einde na ongeveer 2 uur speeltijd: een vriendelijke regel, het spel blijft draaien, save gaat mee naar het volle spel. **Nooit de save wissen** tijdens of tussen de fests, ook niet bij een update van de demo (Fenna 16 nov 11:15; Minimon wiste midden in het fest alle voortgang).
7. Ja van Thijs op het uiterlijk (Gloop, helden, winkelbeelden) op de vaste momenten hierboven.
Niets nieuws erbij na 18 dec. Wat niet op deze lijst staat, gaat naar na het fest.

## Werkwijze (lessen uit Ebb)
- **Eerst één figuur helemaal goed, dan pas breed.** Geen 22 dingen tegelijk ontwerpen.
- **Thijs keurt smaak, op vaste momenten**, met hoogstens 3 versies per blad, op ware grootte én vergroot.
- **Herkennen toetst iemand die niet weet wat het moet zijn** (een frisse agent die alleen het plaatje krijgt).
- **Geen open keuringsrondes.** Na een ja van Thijs ligt een onderdeel vast.
- **Ploeg (13 nov 13:35, Thijs wil meer agents):** Olaf (spel), Bram (3D-pijplijn), Daan (Gloop, helden), Mila (hol, winkelbeelden), elk uur, elk op een eigen stuk. De hoofdchat stuurt en laat Thijs zien.
- Webpagina's lees je met `curl` in Bash, nooit met WebFetch.

## Grootste risico (eerlijk)
De winkelafbeelding. Onze huidige header is een uitvergrote spelstrook naast getekende illustraties van de toppers (`ontwerp/steam/winkelpagina/vergelijk-v5-header.png`). Bij Ebb lukte "mooi uit code" niet bij kleine figuren; pixelart op 16 px gaat code beter af, maar een capsule op 920x430 is een ander soort beeld. Halen we op 25 nov geen ja van Thijs op de capsule, dan leggen we de keuze tekenaar of niet opnieuw voor: een tekenaar heeft 1 tot 3 weken nodig, dus later dan 25 nov schuift de winkelpagina op.

## Afgewezen of geparkeerd (met reden)
- **Gezamenlijk doel voor alle spelers** ("samen 10.000 helden opgegeten, dan komt hoed X in de demo", voorstel Fenna 16 nov 11:15): **nu niet** (besluit Olaf 16 nov). Zonder eigen server kunnen wij het aantal niet eerlijk tellen, en een teller die we zelf invullen is niet eerlijk. Het is ook een nieuwe feature buiten de demolijst. Na het fest opnieuw bekijken, bijvoorbeeld met de Steam-statistieken (stats/achievements) die Steamworks zelf telt.
