# r/3Dprinting: antwoord op "program to split 3d model and add connectors automatically" (Verspreider, run 55, vr 27 nov 2026, A)

**Status:** voorstel, keuring Daan. Daarna voor Thijs (zijn Reddit-account, dus zijn ja op de tekst). Niets geplaatst.

**Links:**
- Dit bestand op GitHub: https://github.com/thijsduinhouwer2002-coder/dortus-hq/blob/main/commercie/verspreiden/2026-11-27-reddit-3dprinting-click-cuts.md
- Het draadje: https://www.reddit.com/r/3Dprinting/comments/1xh96e1/program_to_split_3d_model_and_add_connectors/
- Waar de link in de reactie heen gaat: https://dortus.com/click-cuts/?van=reddit-3dprinting (curl 200, 27 nov ±18:40 NL, GEZIEN; met Get-knop naar Gumroad /l/click-cuts)

**Wanneer:** di 1 dec of later, op een tijd die Thijs uitkomt. Reddit van Thijs: hooguit één ding per dag, en vr 27 (r/blender), za 28 (r/NomadSculpting), zo 29 (Blender Artists) en ma 30 nov (r/customactionfigures) zijn al bezet. Click Cuts zit niet in de CYBER25-sale, dus de datum maakt voor de tekst niet uit. Duur: ±2 minuten.

## Waarom deze plek
- Click Cuts staat sinds vr 27 nov ±15:00 live op Gumroad en heeft nog geen enkele plek buiten onze eigen pagina's (commercie/geplaatst.md, GEZIEN). De twee sterkste plekken voor een nieuwe add-on vallen af: BlenderNation rekent voor een commercieel bericht EUR 25 en Thijs zei daar op 20 nov nee tegen (organisatie/archief/besluiten-t-m-2026-11-24.md); op Blender Artists telt één zelfpromotie per week en die gaat zo 29 nov naar het Pro-draadje.
- De vraag is letterlijk wat Click Cuts doet: "I am printing life size dinosaur skulls and I have always used orca to slice the model into parts that fit into the build volume and manually add connectors. This however takes a VERY long time and I was wondering if anyone has designed a program which automatically does this?" (DERDEN, link hierboven, 28 okt 2026, flair Question, niet op slot, niet gearchiveerd; Arctic Shift posts-API, 27 nov ±18:30 NL).
- De zes antwoorden (DERDEN, Arctic Shift comments-API) noemen de cut-knop in Bambu Studio en PrusaSlicer (de vrager antwoordt zelf: "yes thats exactly why I need a dedicated slicer tool. I am aware on ways to slice manually"), twee websites, Luban, en een andere maker die zijn eigen Blender-add-on op Gumroad noemt. Niemand legt uit wat hij precies vraagt: alle sneden in één keer plannen zodat elk deel op het bed past. Dat is het verschil dat ook in onze eigen FAQ staat ("A slicer cuts one plane at a time").
- Een antwoord blijft staan en komt boven bij wie later zoekt op "split 3d model add connectors automatically" (GOK). Een eigen post zakt weg en valt in r/3Dprinting sneller onder zelfpromotie.
- Publiek: r/3Dprinting is een van de grootste printfora op Reddit (GOK, geen cijfer gezien deze run). Het draadje zelf is klein (6 reacties, score 1), dus het effect zit vooral in later zoekverkeer.

## Regels (DERDEN, https://arctic-shift.photon-reddit.com/api/subreddits/rules?subreddits=3Dprinting, 27 nov ±18:35 NL)
1. "Less than 10% self-promotion": eigen werk mag als je ook anderen helpt en meedoet; "be prepared to engage with the community". Daarom: open zeggen dat we de makers zijn, eerst de vraag zelf beantwoorden, en de beperkingen noemen (betaald, Blender nodig).
2. "No Linking to Restricted Websites": de lijst (wiki) geeft curl 403, dus ik weet niet of Gumroad erop staat. Daarom wijst de link naar onze eigen hulppagina op dortus.com, met de Get-knop daar. Dat meet ook beter (`?van=` in Umami).
3. Geen linkverkorters (regel "Community Behavior"). Staat er niet in.

## Wat Thijs doet
1. Open het draadje (link bovenaan) en lees de regels rechts (±1 min). Staat er nu iets tegen links naar eigen werk of tools, of is het draadje op slot: niet plaatsen, één regel aan de hoofdchat.
2. Plak de tekst hieronder als reactie op de post zelf (niet onder een ander antwoord). Geen beeld nodig.
3. Reageert iemand met een vraag: de hoofdchat of ik zet een antwoord klaar; antwoorden mag Thijs ook zelf.

## Reactie (Engels, om te kopiëren)
```
Late reply, but for anyone who finds this later: the cut tool in Orca, Bambu Studio or PrusaSlicer works fine for one or two cuts, but you place every plane and every connector yourself. On something as big as a skull that is where the hours go.

Full disclosure, I'm one of the makers: we built a Blender add-on for exactly this, Click Cuts. You pick your printer (9 are built in, or type your own bed size), press Split to fit, and it plans all the cuts so every part fits your bed, with round pins, pin holes and an engraved part number on the cut faces. Each part turns green when it fits, is watertight and has enough wall around its holes, or orange or red with the reason. If you don't like where a cut lands, Free cut adds one at any angle through a single part. You export all parts and pins as STL or 3MF in mm.

Two honest limits: it's paid ($19), and it needs Blender (free, 4.2 or newer). Big scans show a time estimate before you split; a 1 million face scan took about 40 seconds in Blender 5.3 in our tests.

It also makes one small fit test block with the pin at four clearances, so you pick the one that fits before you print the big parts. Print that block first: every printer is different.

https://dortus.com/click-cuts/?van=reddit-3dprinting
```

## Waar elke zin vandaan komt (live Gumroad-pagina /l/click-cuts, curl 27 nov ±18:35 NL, GEZIEN)
| Zin | Gumroad zegt |
|---|---|
| slicer: one plane at a time, you set every cut and connector | FAQ "Why not just use my slicer's cut tool? A slicer cuts one plane at a time, and you set every cut and connector yourself." |
| 9 printers or own bed size | "Your printer: 9 printers with their usable bed size, or type your own size." |
| Split to fit plans all cuts, pins, pin holes, engraved part number on the cut faces | "Press Split to fit and Click Cuts plans every cut for you, so each part fits your bed, with pins, pin holes and an engraved part number on the cut faces." |
| green / orange / red with the reason | "Each part turns green when it fits, is watertight and has enough wall around its holes, or orange or red with the reason." |
| Free cut at any angle through one part | "Free cut: an extra cut at any angle through one part." |
| STL or 3MF in mm | "Export all parts and pins as STL or 3MF in millimeters." |
| $19 | price_cents 1900 (Standard; intro t/m zo 14 dec, KAART). Na 14 dec de prijs nakijken vóór plaatsen. |
| Blender 4.2 or newer | "Blender 4.2 and newer." |
| time estimate, 1 million faces about 40 s in 5.3 | "Big models show a time estimate under Split to fit." en "Tested on a 1 million face scan in Blender 5.3: about 40 seconds (2-core test machine)." |
| fit test block, four clearances | "print one small block with your own pin at four clearances, pick the one that fits" |

Niet erin: dat wij printten of dat het klikt, AI, "not print tested", dat het voor levensgrote schedels goed werkt (niet gezien; alleen de meting op 1 miljoen vlakken), magneten (de vrager wil pennen), CYBER25 (geldt alleen voor Pro), de gratis Click Joints (past niet bij deze vraag). "Free" staat er alleen bij Blender, dat echt gratis is.

## Meten
Bezoeken met `?van=reddit-3dprinting` op dortus.com (Umami), Gumroad-verkopen Click Cuts, reacties onder het antwoord. Verwacht: 0 tot 20 bezoeken en 0 tot 1 verkoop in twee weken (GOK). Levert het na 14 dagen niets op, dan geen tweede antwoord in r/3Dprinting over Click Cuts.
