# Berichten aan de Productbouwer

Nieuwe berichten onderaan, met datum en van wie.

- 23 nov 2026, van Productbouwer (aan mezelf): run 1 klaar, keuze Flexi-maker in `producten/blender-product-2/keuze.md`. Geen bezwaar van de hoofdchat na 1 run: verder met ontwerp en proef.

## 23 nov 2026 ±13:50 NL, van de hoofdchat: Flexi-maker
Geen bezwaar: bouw door. Let op de hoofdzaak: eerst een kleine versie die binnen weken op Gumroad kan, met bundel naast Click Joints Pro. Meld het in `berichten/hoofdchat.md` als er iets te keuren is.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±15:45 NL, van hoofdchat: testprint gaat niet naar Thijs
Goed werk met run 2. De testprint zet ik niet op de lijst van Thijs: die is vol met dingen die nu geld opleveren (Pro 1.2.1 op Gumroad en Superhive vóór de Cyber Sale). Bouw de add-on met e2e in CI door; laat de proef-STL in de repo staan, dan vraag ik het zodra Flexi Joints bijna uit kan. Beelden in de repo is prima zolang ze klein blijven (onder ±500 kB).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±16:25 NL, van hoofdchat: KOERSWIJZIGING, Thijs kiest de splitser, Flexi stopt
Thijs koos (chat, 16:20): het tweede product wordt **een splitser met verbinders**: een model dat te groot is voor de printer in stukken snijden, met pennen of klikverbinders die precies passen. Bewezen vraag: CatPin 400+ verkopen in 3 maanden, Cleave 300+ in 2 maanden (je eigen keuze.md). Doel: beter dan die twee, en een uiterlijk en winkelpagina waar mensen het echt willen hebben. Flexi stopt (laat je werk staan in `producten/blender-product-2/`, schrijf onderaan LOG.md waarom het stopt).
Jij bent vanaf nu de **bouwer van de splitser**, in `producten/blender-splitser/`. Er werken tegelijk drie agents mee (vandaag gestart): (1) een concurrentie-analist die CatPin, Cleave, Split 3D Print en anderen uitpluist en een lijst "zo worden we beter" maakt (`producten/blender-splitser/concurrentie.md`), (2) een merk- en uiterlijk-agent (naam, icoon, winkelbeelden, paneel in Blender; `producten/blender-splitser/merk/`), (3) een eerste bouwer die vandaag de kern neerzet (snijden plus verbinders, met e2e in CI, hergebruik van `producten/blender-gewrichten/`). Lees hun werk elke run en bouw daarop verder volgens de skill bouwen-in-stappen. Doel: binnen ±2 weken op Gumroad en Superhive, en een bundel met Click Joints Pro.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±18:00 NL, van hoofdchat: concurrentie goedgekeurd, bouw hierop
`producten/blender-splitser/concurrentie.md` is na herkeuring akkoord. Volgorde van wat we beter doen: (1) passingproef met je eigen verbinder op 4 spelingen, onthouden per printer en materiaal, (2) niet vastlopen op lelijke meshes (AI-modellen, sculpts), (3) wandcheck per verbinder in mm, (4) delen plat en verbinders zonder steun, (5) eerste snede binnen 60 seconden zonder video, (6) gegraveerde nummers, (7) de lat: pen die maar op één manier past, printerkeuze met groen/rood. Niet doen in versie 1: veel snijmodi, uithollen, AI-download. Lees de lijst "must have" in dat bestand en plan je stappen daarop.
