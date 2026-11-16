# Reeks "Printable joints in Blender, day N" (Click Joints) en de tips voor Ebb

Door Chris, 16 nov 2026, run 51. Opdracht: hoofdchat 16 nov 05:00 (filmpjes zijn vooral nuttige tips) en de verhalen 3 en 4 van Joris (VAW.BE, Blender Secrets) in `berichten/chris.md`.

**Niemand plaatst zonder Daans akkoord, Brams "klopt" op de tip en het ja van Thijs.**

## Waarom deze naam
- De hoofdchat stelde "Print-in-place in Blender, day 1" voor. Click Joints doet geen print-in-place: je print de delen los en klikt ze in elkaar (besluit Bram, `producten/blender-gewrichten/ontwerp.md` regel 76; zie ook run 50). Een reeks met die naam belooft iets wat het gereedschap niet doet. Daarom **"Printable joints in Blender, day N"**: dekt kogel, pen en scharnier, en klopt voor gratis en Pro.
- Elk filmpje: bovenaan klein de reeksnaam met dagnummer, daaronder één vraag of één handeling, onderaan klein "Tool: Click Joints, a free Blender add-on". Geen logo, geen inleiding (Blender Secrets, verhaal 4).
- De eerste 10 duren 10 tot 15 seconden (hoofdchat punt 1; de workflow eist 10 tot 20).

## Verhouding 4 op 5, en wat dat met week 1 doet
Vier tips op elke vijf filmpjes, één filmpje over het product. De zes filmpjes van week 1 zijn allemaal productfilmpjes en blijven zoals Daan ze keurde (hoofdchat: "de keuring van Daan blijft"). Ze worden de productplekken: dag 5 en dag 10 van de reeks, en voor Ebb hetzelfde. Zo hoeft er niets opnieuw gekeurd te worden en schuift alleen de volgorde.

Voorstel volgorde Click Joints (elke dag één, wisselend met Ebb zoals de opdracht van 15 nov zegt):

| dag | filmpje | soort | tip (de bewering) | beeld | Bram: klopt? |
|---|---|---|---|---|---|
| 1 | f7, **gemaakt** | tip | Zonder speling klemt de kogel of klikt hij niet in de kom. Begin rond 0,2 mm op FDM en test op je eigen printer. | staande opname 5 (kogel en kom uit elkaar), paneel met Clearance 0.20 en "Clearance: 0.20 mm (measured)", arm die buigt (film v2) | open |
| 2 | f8 | tip | Een dunne wand rond de kom breekt bij het inklikken. Mik op 1,5 mm of meer (dezelfde grens als de melding "Tight" in de add-on: `GRENS_ORANJE_MM = 1.5` in `click_joints/passing.py`, "aim for 1.5 mm or more"; de 1,2 mm in ontwerp.md regel 119 is een oud voorstel). | paneel met "Wall: 1.54 mm" en Good fit | open |
| 3 | f9 | tip | Een kogelgewricht dat wel klikt maar niet buigt: de platte snijvlakken raken elkaar. De naad moet om het kogelmidden heen lopen. | film v2, buigen met de groene ring | open |
| 4 | f10 | tip | Kies de grootste kogel die in het lid past: groter is sterker. | paneel, Diameter met Auto | open |
| 5 | f2 (week 1) | product | Zie hoe ver een gewricht buigt voordat je print. | gekeurd door Daan | n.v.t. |
| 6 | f11 | tip | Pen voor één richting (vinger, kaak), kogel voor alle richtingen (schouder, heup). | paneel Ball en Pin | open |
| 7 | f12 | tip | Werk in millimeters: een figuur van 0,2 eenheden wordt in de slicer een stofje. Kijk de schaal na voor je exporteert. | paneel Export, melding mm | open |
| 8 | f13 | tip | Een gewricht snijden lukt alleen in een gesloten mesh. Gaten eerst dicht. | paneel Check mesh | open |
| 9 | f14 | tip | Print eerst een klein proefje met een paar spelingen, voordat je de hele figuur print. | eigen opname nodig (vraag aan Bram) | open |
| 10 | f1 (week 1) | product | Gaat dit gewricht ver genoeg buigen? | gekeurd door Daan | n.v.t. |

Daarna f3 (week 1) als productplek op dag 15; f5 (Pro) zodra Pro live is, ongeacht het dagnummer.

Elke bewering in de tabel komt uit ons eigen ontwerp en de metingen in `producten/blender-gewrichten/ontwerp.md` (speling 0,20 als standaard, wand "aim for 1.5 mm or more" uit `passing.py`, de vondst van de platte snijvlakken, Auto kiest de grootste maat, schaalcheck in mm, Check mesh), behalve "rond 0,2 mm op FDM" als algemene start (GOK uit de standaard van de add-on, daarom "then test on your printer") en de tip van dag 9 (algemene werkwijze). Daarom kijkt Bram elke tip na voor hij uitgaat (Joris, verhaal 4: "een tip die niet klopt, kost meer dan hij oplevert").

## Dag 1: `click-joints-7-tip-day-1-clearance.mp4` (12,5 s), bron `week-1/f7.json`
| tijd | beeld | tekst in beeld |
|---|---|---|
| 0 tot 3,3 s | staande opname 5 van Bram: kogel en kom van de gratis versie uit elkaar, groene pasband, hele scherm | Ball joint too tight to **snap in**? |
| 3,3 tot 7,8 s | paneel van de gratis versie 0.1.0 (preview op extensions.blender.org), langzame zoom: Clearance (mm) 0.20 en "Clearance: 0.20 mm (measured)" | No gap, no movement. Leave **clearance** between ball and socket. |
| 7,8 tot 12,5 s | film v2: de arm buigt met de groene ring | Start around **0.2 mm** on FDM. Then test on your printer. |
| hele filmpje | | bovenaan klein: Printable joints in Blender, day 1; onderaan klein: Tool: Click Joints, a free Blender add-on |

- Eerste haak was "Why does my ball joint print as one solid lump?". De controleur zag terecht dat vastsmelten alleen bij print-in-place gebeurt; Click Joints maakt losse delen die je inklikt. Daarom nu "too tight to snap in".
- Geen rode close-up (moet M1 van Daan), geen ring en pop als begin (kan-punt van Daan: elk filmpje een ander begin). Alleen de gratis versie: staande opname 5 is de kogel, die ook gratis zit (LEESMIJ van Bram).
- 1080 x 1920, H.264, geen geluid, 12,5 s. Lokaal gebouwd met `maak.py` en beeld voor beeld bekeken (GEZIEN 16 nov ±04:55 UTC): de tekst staat onder de bovenbalk (y 240 en lager, zoals Daan voor filmpje 6 vroeg), het paneel valt in het vlak van y 640 tot 1540, beide regels met de speling blijven tijdens de zoom in beeld.

**Onderschrift:** `Printable joints in Blender, day 1: ball joint too tight to snap in? Without a gap between ball and socket, the parts jam or never click together. Start around 0.2 mm clearance on FDM, then test on your own printer. Tool in the video: Click Joints, a free Blender add-on (link in bio). AI agents write the code, I direct and test. Made something with Click Joints? Tag me, I'd love to see it. #blender #3dprinting #b3d #articulated`

De AI-zin is `AI agents write the code, I direct and test.` (zoals in het door Daan gekeurde onderschrift van filmpje 4) en niet "Built with help from AI" uit week 1, want die maakt de rol van AI kleiner dan in de winkeltekst (gezien in run 50). Voorstel: deze zin in alle nieuwe onderschriften.

**Tijd:** zoals week 1, rond 16:00 NL op werkdagen.

## Tipspagina op dortus.com/click-joints/tips/ (hoofdchat punt 2)
Per tip een korte tekst met één plaatje, zodat de verzameling blijft staan (Blender Secrets, verhaal 4 punt 4). Abel bouwt de pagina op een tak in de repo dortus (verzoek in `berichten/abel.md`). Tekst voor tip 1, Engels zoals de site:

> **Day 1: Ball joint too tight to snap in?**
> If the ball and the socket have the exact same size in the model, the printed parts jam or never click together, because every printer adds a little extra plastic. Leave a small gap, the clearance, between them. Around 0.2 mm is a common place to start on an FDM printer, but every printer is different: print a small test first and adjust. In Click Joints you set the clearance in mm before you place the joint, and after placing it the panel shows the clearance it measured on your mesh.
> *Plaatje:* het paneel met "Clearance: 0.20 mm (measured)" (uitsnede van `4-preview-paneel.png`).

Pas op de pagina zetten nadat Bram "klopt" zei.

## Ebb: dezelfde verhouding (hoofdchat punt 4)
Vier tips op vijf, één over Ebb. Tips over ademen en rust op je horloge **zonder gezondheidsclaims**, niet als freediving, altijd "zit of lig". Eerste ideeën, alle vier over het gebruik van een horloge en niet over wat ademen met je lichaam doet:
1. Zet "niet storen" aan voor je vijf minuten rust neemt, anders trilt elk bericht erdoorheen.
2. Een vast moment (na de lunch, voor het slapen) houd je langer vol dan "als ik eraan denk".
3. Kijk niet naar het scherm maar voel het trillen: zo kun je je ogen dicht houden.
4. Begin kort: twee minuten die je elke dag doet, zijn er meer dan tien die je overslaat.
De productplekken zijn f4 en f6 uit week 1. Ebb-tips maak ik in een volgende run uit de simulatorschermen, en Gijs kijkt of elke tip klopt met wat Ebb doet (trillen, niet storen).
