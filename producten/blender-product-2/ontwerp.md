# Flexi Joints: ontwerp v0.1 (Productbouwer, 23 nov 2026, run 2)

Werknaam product: **Flexi Joints** (Engels in de winkel). Stappen 1 tot 4 van `bouwen-in-stappen`. De keurder kijkt hier mee vóór stap 5.

## 1. Begrijpen
Een Blender-add-on die een model langs een lijn in segmenten snijdt en tussen elk paar een print-in-place scharnier zet, zodat het hele model in één print van het bed komt en meteen buigt. Voor wie figuren en dieren ontwerpt om te printen en te verkopen (dezelfde kopers als Click Joints Pro).

"Af" voor v0.1 (toetsbaar, elk punt een regel in de e2e):
1. Op een staaf en een ronde buis met 4 scharnieren: elk segment gesloten (0 foute randen, volume > 0, 1 eiland).
2. In rust raken de segmenten elkaar nergens en is de kleinste afstand ten minste 0,9 x de speling.
3. Elk scharnier draait vrij tot (bereik - 3) graden naar beide kanten en raakt bij (bereik + 3) graden: de eindstop klopt.
4. Eén STL en één 3MF met alle segmenten, op het bed (z = 0).
5. In de add-on: kies object, kies of teken een lijn, aantal segmenten, knop "Make flexi". Paneel toont per scharnier het bereik in graden.
6. Groen op Blender 4.2, 5.2 en 5.3 in CI, met schermafbeeldingen in een release.

## 2. Wat er al is (Click Joints, `producten/blender-gewrichten/`)
- `click_joints/gewricht.py` r. 25 tot 80: keuze Manifold (4.5+) of Exact, booleans op kopieën, `bak`. Hergebruiken.
- `click_joints/vormen.py`: bol, cilinder, doos, kegel in een frame met Z als as. Flexi heeft daarnaast een omwentelingslichaam nodig (nieuw, `draai_profiel` in de proef).
- `click_joints/gesloten.py` r. 9 tot 50: `foute_randen`, `volume`, `is_gesloten`. Hergebruiken.
- `click_joints/betaald/scharnier_beweeg.py` r. 70 tot 115: botsproef met BVH tijdens draaien. Zelfde idee als `toets_paar` in de proef.
- `click_joints/drie_mf.py`: eigen 3MF-schrijver. Hergebruiken voor de export.
- CI: `.github/workflows/blender-gewrichten-e2e.yml` (Blender ophalen, xvfb, matrix 4.2.23, 5.2.3, 5.3.0). Zelfde opzet voor `blender-flexi-e2e.yml`.

## 3. Open vragen, zelf beantwoord
- **Welke kant buigt het?** v0.1: zijwaarts, as loodrecht op het bed (zoals de meeste flexi-vissen, slangen en draken die je op tafel laat kronkelen). Reden: dan liggen alle spleten verticaal of als kegel van 45 graden, dus print het zonder steun. Op en neer buigen (as evenwijdig aan het bed) komt later als het gevraagd wordt.
- **Hoe houdt de knokkel zich vast?** Hij zit opgesloten tussen twee armen van de vork. Bovenop een kegel van 45 graden, zodat het plafond van de holte zonder steun print. Geen losse pen nodig.
- **Wat als het model te dun is voor het scharnier?** De add-on meet de dikte op elk scharnierpunt; te dun = rood in het paneel met de kleinste maat die past (zoals `maat.py` in Click Joints). Geen stil falen.
- **Gebogen lijn?** Elk scharnierpunt krijgt een eigen frame (punt op de curve, richting van de curve, Z = bed). De proef doet een rechte lijn; de curve is stap 5b.
- **Speling?** Standaard 0,4 mm (GOK, gangbaar voor print-in-place op FDM; Click Joints gebruikt 0,2 voor klikken, dat is te krap voor los printen). Instelbaar 0,2 tot 0,8.
- **Exact op 4.2 is gevoelig.** Gemeten in de proef: zie de lessen hieronder.
- **Gratis of betaald?** Alleen betaald ($19, Gumroad en Superhive), bundel met Click Joints Pro. Geen gratis kern: de hoofdzaak is geld (besluit van Thijs 19 nov).

## 4. Aanpakken
| | Aanpak | Voor | Tegen |
|---|---|---|---|
| A | Knokkel en vork met wiggen (deze proef) | Eindstop en bereik volgen uit één getal (de wighoek); alles verticaal of 45 graden, print zonder steun; 4 booleans per scharnier | Model moet ten minste ±9 mm dik zijn op het scharnier |
| B | Kogel in kom per segment (zoals Flexi Rex) | Buigt alle kanten op | Kom moet open naar boven of steun nodig; bereik moeilijk te meten; meer werk |
| C | Ketting van vaste schakels, model eromheen hol | Werkt op elke vorm | Ziet er niet uit als het model; kopers willen hun eigen dier, niet een ketting |

**Keuze: A.** Snelst naar een werkend en verkoopbaar v0.1, en het bereik in graden is ons verschil (zelfde verhaal als Click Joints Pro). B kan later als tweede soort.

### Vorm (gebouwd en gemeten in `proef/proef_flexi.py`)
Per scharnier punt J, ketting langs +X, Z omhoog. Maten standaard: speling s 0,4, knokkel Rk 3,0, plat op de kegel 1,0, middenband z 2,0 tot 5,0, bereik 30 graden per kant.
- K (knokkel, deel A): cilinder Rk in de middenband met een kegel van 45 graden erop.
- Ks: K met s eromheen (cilinder Rk + s, kegel s·√2 hoger, s eronder).
- WA, WB: wiggen achter en voor J, spleet van "bereik" graden aan beide kanten. Punt op J.
- A = lichaam ∩ ((WA - Cks onder z1 - Cks boven z2) ∪ K)
- B = (lichaam ∩ (WB ∪ Ck)) - Ks
- Ketting: snij het lichaam bij J1 in A1 en rest, snij de rest bij J2, enzovoort.

### Lessen uit de proef (Blender 4.2.23, Exact, gemeten 23 nov)
1. "WA ∪ hals" met dezelfde wangen gaf T-naden (8 foute randen). Oplossing: Cks in twee stukken eraf, de hals blijft vanzelf staan.
2. Ks eerst van het gereedschap halen en dan snijden gaf bij de ronde buis een kapot deel B (volume groter dan het model). Oplossing: Ks direct van het deel af.
3. Wigpunt precies op J; anders sluit de spleet nooit en is er geen eindstop (proef 1 gaf "raakt 0" bij 33 graden).
4. Na elke snede punten samenvoegen (0,1 micron): de Exact-solver laat dubbele punten achter.

## Nog open voor stap 5
- Dikte meten per scharnier en rood melden; middenband automatisch midden in de dikte.
- Lijn als curve-object; scharnieren op gelijke afstand langs de curve.
- Operator, paneel, export STL en 3MF, e2e-workflow en manifest (eigen id `flexi_joints`).
- Testprint: ik kan niet printen. Bewijs dat het print is nu GOK; de proef bewijst alleen de vorm. Een gratis testprint van de proefketting (`flexi_ketting.stl`) door iemand met een printer zou het sterkste bewijs zijn; hoofdchat beslist of dat Thijs gevraagd wordt.
