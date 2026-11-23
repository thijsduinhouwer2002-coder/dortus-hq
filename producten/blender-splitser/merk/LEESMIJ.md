# Merk van de splitser (merk-agent, ma 23 nov 2026)

Opdracht hoofdchat ±16:30 NL: naam, icoon, kleuren, coverbeeld en winkelbeelden voor het tweede product (een model dat te groot is voor de printer in stukken snijden, met pennen of klikverbinders). Thijs: "zorg dat het uiterlijk en alles eromheen mensen trekt". De lat: niet grijs, niet vol getallen, niet nep.

**Thijs kiest uit 2 stijlen en 3 namen.** Alle beelden staan in release [`splitser-merk-1`](https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/tag/splitser-merk-1).

GEZIEN = zelf gezien of gemeten op 23 nov 2026. DERDEN = cijfer van een ander, met link. GOK = eigen schatting.

## 1. Afgekeken: wat verkoopt (coverbeelden met curl gehaald en bekeken)

| Add-on | Verkopen op Superhive (GEZIEN) | Wat het coverbeeld doet |
|---|---|---|
| [CatPin](https://superhivemarket.com/products/catpin) | 400+ | Bruine anime-buste uit elkaar met pennen, plus grote stickers (versie, -20%), mascotte-kat. Op Gumroad is het vierkante beeld alleen de kat met de naam (85 beoordelingen, DERDEN: Gumroad-zoek-API) |
| [Cleave](https://superhivemarket.com/products/cleave) | 300+ | Figuur met vleugels in 5 felle kleuren uit elkaar, op een snijmat met echte prints; grote witte naam, drie korte regels. Hun eerste zin is "Too big to print? Split it." (die nemen we dus niet) |
| [Split 3D Print](https://superhivemarket.com/products/split-3dprint) | 400+ | Voor en na: grijs figuur, pijl, hetzelfde figuur in 10 kleuren uit elkaar; drie woorden van de naam reusachtig groot |
| [SnapSplit](https://superhivemarket.com/products/snapsplit) | 30+ | Grijs Blender-scherm met een muur van instellingen. Het enige grijze beeld, en het minst verkocht |
| [Hard Ops](https://superhivemarket.com/products/hardopsofficial) | 9300+ | Geen tekst, twee strakke modellen op zwart met één felle kleur (groen, blauw) |
| [Flip Fluids](https://superhivemarket.com/products/flipfluids) | 19000+ | Eén spectaculair resultaat (golf) schermvullend, logo klein linksboven |
| [BagaPack](https://superhivemarket.com/products/bagapack-addon-bundle) | 200+ | Alleen het logo groot op een vage foto |
| [Texel Density Checker](https://superhivemarket.com/products/texel-density-checker) | 300+ | Donker vlak, grote witte naam, groot oranje icoon |

Wat opvalt (mijn lezing, GOK dat het de reden van verkopen is):
1. **Eén groot resultaat, geen scherm.** De bestverkopers tonen wat je krijgt, niet hoe de knoppen eruitzien. Het enige beeld met een paneel (SnapSplit) verkoopt het minst.
2. **Felle kleur per deel** maakt "in stukken" in één tel duidelijk (Cleave, Split 3D Print). Grijs leest als "nog niet af".
3. **Naam groot, hooguit drie korte regels.** Geen getallen in het beeld, behalve de stickers van CatPin (en die zien er goedkoop uit).
4. **Voor en na** (Split 3D Print) is het snelste verhaal; wij doen dat met twee beelden (cover en winkelbeeld 1).
5. **Een eigen gezicht:** CatPin heeft een kat, Texel een oranje blokicoon. In een lijst herken je ze aan dat ene ding.
6. Alle drie de concurrenten gebruiken een anime-meisje. Wij vallen op met iets anders: een leeuwenkop, groot en herkenbaar, en zonder bekend personage.

## 2. Naam (top 3)

Gecontroleerd met curl op Superhive (zoeken en de productpagina), Gumroad (zoek-API), extensions.blender.org en GitHub, plus een zoekopdracht op het web: geen Blender-add-on en geen bekend merk met deze namen gevonden (GEZIEN 23 nov). Een merkregister heb ik niet doorzocht; voor de zekerheid laat de hoofdchat dat doen vóór de lancering.

| # | Naam | Waarom | Twijfel |
|---|---|---|---|
| 1 | **Click Cuts** | Past naast Click Joints: samen "de Click-set", een bundel verkoopt zichzelf. Zegt wat het doet (snijden, en de stukken klikken weer in elkaar). Kort, rijmt bijna, makkelijk te onthouden | "Click" kan doen denken dat het alleen klikverbinders zijn; de pennen dekt het minder |
| 2 | **PlateFit** | Zegt de uitkomst: past op je printplaat. Eén woord, goed als icoon-naam en in een zoekbalk | Past minder als bundelnaam naast Click Joints |
| 3 | **Print Big** | Zegt de wens van de koper ("ik wil dit groot printen"). Werkt in Shorts en titels | Twee gewone woorden; moeilijker te vinden in zoekresultaten, en als merk minder te beschermen |

Ook bekeken: **Partwise** (mooi, maar zegt niet meteen wat het doet), **Peg Cuts** (duidelijk, niet pakkend). Niet gekozen: "Split Joints" (werknaam in `split_joints/`: botst met het woord "joints", dat bij ons gewrichten betekent), "Bed Fit" en "Click Split" (bestaan al op Superhive: `bed-fit-splitter`, `one-click-splitting`), alles met "Split" of "Snap" vooraan (SnapSplit, Split It, Split 3D Print, PrintSplitter, PrintSplit Easy zitten er al).

De beelden in de release dragen de naam **Click Cuts**. Kiest Thijs een andere naam: start de workflow `splitser-merk.yml` met invoer `naam` (handmatig), of vervang de standaardnaam in de workflow; alle tekst komt opnieuw uit `bron/maak_beelden.py`.

## 3. Icoon en kleuren

`icoon.svg` (en `icoon-512.png`): een blok in twee stukken, schuin doorgesneden, met twee gouden pennen dwars over de spleet. Koraal en kobalt op het donkere vlak van Dortus. Leest op 32 px nog als "doorgesneden met pennen" (GEZIEN in een proef op 512, 64 en 32 px). Zelfde vorm als het Click Joints-icoon (donker afgerond vlak), dus familie in een bundel.

| Naam | Hex | Waar |
|---|---|---|
| Nacht | `#1D1426` | ondergrond van het icoon (Dortus) |
| Koraal | `#FF5B3A` | stuk 1 van het icoon, warme kleur van de familie |
| Kobalt | `#3D5BFF` | stuk 2 van het icoon, achtergrond van stijl A |
| Goud | `#FFD25C` | pennen, de grote knop in het paneel (Dortus) |
| Lila | `#A58CFF` | stukken in stijl B (Dortus) |
| Crème | `#FFF4E0` | tekst op donker |

Waarom dit opvalt: in een lijst vol grijze en zwarte beelden is de combinatie van een warm en een koud vlak met goud het eerste wat je ziet; het goud en de nacht houden het bij Dortus.

Letters: **Bricolage Grotesque ExtraBold** voor de naam en koppen (eigenwijs, met karakter, OFL-licentie), **Inter** voor kleine tekst (zelfde als Dortus).

## 4. Coverbeeld en winkelbeelden (release `splitser-merk-1`)

Alles gemaakt in Blender 5.3.0 (Cycles) in de workflow `.github/workflows/splitser-merk.yml`, geen AI-beeld. Model: **Lion Head van Poly Haven**, [polyhaven.com/a/lion_head](https://polyhaven.com/a/lion_head), licentie CC0 (zelf gelezen op [polyhaven.com/license](https://polyhaven.com/license): "Our assets are all licensed as CC0"). Geen naamsvermelding nodig; we zetten "Lion Head by Poly Haven (CC0)" er toch bij in de winkeltekst. De achterwand komt uit `commercie/filmpjes/studio/studio.py` (`achterwand`), in eigen kleuren.

Het model is 436 mm hoog (zoals het geleverd wordt) en wordt in 7 stukken gesneden die elk op een bed van 256 mm passen (gemeten in het script, GEZIEN in het log: grootste stuk 188 x 179 x 228 mm), met 19 pennen van 10 mm dik en 28 mm lang, gat 0,2 mm ruimer. Het gezicht blijft heel.

| Bestand | Wat |
|---|---|
| `cover-a.png`, `cover-b.png` (2400 x 1200) en `-1200x600` | De cover in twee stijlen |
| `winkel-*-1-heel.png` | De hele leeuw steekt ver buiten het bouwvolume (gouden kader van 256 mm): het probleem |
| `winkel-*-2-bed.png` | Alle stukken op drie printplaten, pennen ervoor: het past |
| `winkel-*-3-pen.png` | Dichtbij: pennen en gaten tussen gezicht en manen |
| `winkel-*-4-paneel.png` | Het paneel naast de uiteengevallen leeuw |
| `winkel-*-5-samen.png` | Weer in elkaar, de kleuren per stuk zichtbaar |
| `gumroad-*-1200.png` | Vierkant voor Gumroad |
| `paneel-schets.png` | Schets van het paneel (ook in deze map) |
| `vergelijk.png` | Onze covers naast CatPin en Cleave, groot en klein (hun beelden van Superhive, alleen ter vergelijking, niet om te gebruiken) |
| `render-*.png` | De kale renders zonder tekst |

**Stijl A, Pop:** kobaltblauwe studio, stukken in zon, koraal, roze, munt, oranje, wit en paars, witte pennen. Vrolijk en fel, valt op tussen donkere beelden.
**Stijl B, Nacht:** pruimkleurige studio van Dortus met goud licht, stukken in goud, lila, koraal, oranje, crème en munt, gouden metalen pennen. Duurder en rustiger, past het best bij Dortus.

Mijn voorkeur: **B voor de cover** (ziet er het duurst uit, goud en pruim zijn van Dortus, het donker laat de kleuren gloeien), A voor Shorts en TikTok (fel werkt daar beter). Thijs beslist.

Tekst op de cover (Engels, concept): naam, "Print bigger than your printer.", "Parts that fit your bed, with pins that line up." Bewust niet "Too big to print? Split it.": dat is de eerste zin van Cleave.

## 5. Paneel in Blender (`paneel-schets.png`)

Een schets, geen echt scherm. Van boven naar onder: printer kiezen (één keuzelijst), verbinder kiezen (drie grote knoppen met icoon: Pins, Click, None), één grote gouden knop **Split to fit**, daaronder de uitkomst in gewone woorden ("7 parts, all fit the bed"), export, en alles wat meer is achter "More settings". Geen muur van instellingen. Past bij punt 6 uit `../concurrentie.md` ("in 60 seconden je eerste snede, zonder video").

## Eerlijk oordeel

- Zou ik dit kopen op basis van het beeld? **Stijl B: ja**, het ziet eruit als een product dat af is, en de leeuw in kleuren met gouden pennen zegt in één tel "in stukken, en het past weer". Stijl A: bijna; de blauwe vloer is wat vlak.
- **De beelden zijn gemaakt met Blender-booleans, niet met de add-on** (die bestaat nog niet). Ze laten zien wat de add-on moet doen: vlakke sneden, pennen, elk stuk past op 256 mm. Zodra de add-on werkt: dezelfde scène opnieuw renderen met de echte uitkomst, zodat beeld en product gelijk zijn. Het paneel in winkelbeeld 4 is een schets en moet dan een echte schermafbeelding worden. Tot dan niets hiervan plaatsen als bewijs van wat het doet.
- Nog beter (volgende ronde): een echte print van de leeuw in kleuren naast een printer (de concurrentie-analist zag dat niemand dat toont); de naad tussen de stukken iets duidelijker in "samen"; de vloer van stijl A meer diepte geven.

## Bron
- `bron/splits_scene.py`: model laden, snijplan, pennen zoeken en boren, kleuren, studio, camera die het beeld vult. Lokaal: `blender -b --factory-startup --python bron/splits_scene.py -- <modelmap> <uitmap> a|b cover|heel|delen|bed|pen|samen [samples] [schaal%]` met `STUDIO_DIR` naar `commercie/filmpjes/studio`.
- `bron/maak_beelden.py`: tekst erop, paneelschets, vergelijkingsblad.
- `bron/icoon.svg`: kopie van het icoon voor de beelden.
