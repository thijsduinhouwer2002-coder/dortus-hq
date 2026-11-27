# Click Cuts vindbaar maken: kruisverwijzingen (issue #284)

**Gekeurd: Daan ja 8 (#289), 27 nov.**

Productbouwer, 27 nov 2026 ±16:50 NL. Eén zin per pagina, met waar hij komt. Alles in het Engels, zoals de pagina's zelf. Geen nieuwe beloftes: elke bewering staat al in de gekeurde winkeltekst (`lancering.md`, Daan #12, #188) of in de gekeurde FAQ (`faq.md`, Daan #176).

## A. dortus.com (repo dortus, tak `claude/click-cuts-tegel`, samenvoegen doet de hoofdchat)
Al gedaan op de tak, niets te plakken:
1. **Voorpagina** (`index.html`, 455e45d): tegel Click Cuts naast Click Joints (Blender-rij), knoppen "Get it on Gumroad" naar https://duinhouwer8.gumroad.com/l/click-cuts en "Guide" naar /click-cuts/. De drie andere tegels (Ebb, Rollwright, Bison & Flex) staan nu met z'n drieën op de tweede rij. Ook bijgewerkt: meta-beschrijving, productlijst voor zoekmachines, FAQ "What is free and what is paid?" noemt Click Cuts ($19). Bekeken op 390 en 1366 px, geen zijwaartse scroll (GEZIEN).
2. **dortus.com/click-joints/** (eb7c49f): onder de knop "Get Click Joints Pro on Gumroad":
   > Model too big for your printer bed? Click Cuts splits it into parts that fit, with pins or magnet holes and a number on every part, $19 once. It works side by side with Click Joints.

   "Click Cuts" linkt naar /click-cuts/ (de gids, met Get-knop naar Gumroad). Bekeken op 390 en 1366 px (GEZIEN).
   Boven de zin een dunne lijn en het kopje "Also from Dortus" (Daan kan-punt #289, 75dc498), zodat het leest als ander product en niet als uitleg bij Pro. Opnieuw bekeken op 390 en 1366 px, scrollWidth gelijk aan de breedte (GEZIEN).

## B. Gumroad (alleen de hoofdchat plakt; Edit product, veld Description)

**B1. Click Cuts** (https://duinhouwer8.gumroad.com/l/click-cuts). Nieuwe alinea direct onder de regel "Made for busts, cosplay props, terrain and statues that are too big for one print.", vóór de lijst die begint met "Split to fit:":
> **Step-by-step guide:** [dortus.com/click-cuts](https://dortus.com/click-cuts/) shows how to install it, your first split, the fit test, magnets and every button in the panel.

Waarom: Gumroad heeft geen Docs-tab; de gids is wat Superhive-kopers als Docs-tab krijgen. Linkt de knop van de gids al terug naar Gumroad (GEZIEN 27 nov 15:35).

**B2. Click Joints Pro** (https://duinhouwer8.gumroad.com/l/click-joints-pro). Nieuwe alinea helemaal onderaan de beschrijving:
> **Model too big for your printer bed?** [Click Cuts](https://duinhouwer8.gumroad.com/l/click-cuts) splits it into parts that fit, with pins or magnet holes and a number on every part, $19 once. Splitting makes it fit on the bed. Click Joints Pro makes it move.

De laatste twee zinnen staan al letterlijk in de FAQ van Click Cuts op Gumroad (GEZIEN met curl 27 nov), dus de twee pagina's zeggen hetzelfde.

**B3. Click Joints (gratis)** (https://duinhouwer8.gumroad.com/l/click-joints-free; /l/click-joints geeft 404, verbeterd 27 nov ±20:35, #300). Zelfde alinea als B2, helemaal onderaan de beschrijving.

## C. Superhive: nog niet
Click Joints Pro op Superhive krijgt dezelfde zin pas als Click Cuts daar goedgekeurd is (nu Pending, GEZIEN 27 nov 15:10). Nu zou de link naar een pagina wijzen die bezoekers nog niet zien, en een link van Superhive naar Gumroad leidt kopers weg van de winkel die ons daar vindt. Na goedkeuring: zin B2 met de link https://superhivemarket.com/products/click-cuts.

## Gecontroleerd
- Gumroad Click Cuts linkt nu nergens naar dortus.com/click-cuts (curl 27 nov ±16:40, GEZIEN).
- Gumroad Click Joints Pro en gratis noemen Click Cuts alleen in Gumroads eigen blok "more from this creator", niet in de beschrijving (curl 27 nov ±16:40, GEZIEN).
- $19: prijs Standard op Gumroad, price_cents 1900 (GEZIEN, kaart 27 nov).
