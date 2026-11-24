# Keuring zes lanceringsscripts Click Cuts, 24 nov 2026, Daan
Wat ik keurde: `commercie/filmpjes/scripts/click-cuts-lancering.md` (Sanne, commit 7614c9a), elke claim nagelopen tegen `producten/blender-splitser/split_joints/` op main.
Akkoord: ja na M1 en M2

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Script 4: de kleur "oranje" is in de code RGB (1.0, 0.92, 0.0) (`controle.py` KLEUREN). Dat is geel. Wie bij zin 4 de stukken in Check-kleuren ziet, hoort "orange" en ziet geel. | feit (code) | hoog | opname in Check-kleuren bekijken |
| A2 | Script 1 zin 5 "with clearance for your printer": de speling is 0,20 mm standaard voor elke printer; pas na de fit test is hij echt van jouw printer (`eigenschappen.py` default 0.2, `passingproef.py`). | feit | hoog | |
| A3 | Script 5 zin 4 "sees it at once, and shows a red line": de rode regel bovenaan komt pas na Split to fit ("Wrong unit? Open More settings and use Convert to mm", `in_een_klik.py` r. 75, `paneel.py` r. 41 alert). Onder More settings stap 2 staat hij wel meteen, maar die is dicht. Klopt als het beeld eerst Split to fit drukt. | feit | hoog | |
| A4 | Script 5: de paneelregel zegt altijd "(mm model in a meter scene)"; zin 3 "or the other way round" is dus breder dan wat het paneel zegt. Niet fout, wel in beeld de mm-in-meters-kant tonen. | feit | midden | |
| A5 | Overige claims kloppen: 9 printers plus Custom size, fewest cells van het rooster (en Sanne zegt terecht niet "fewest possible"), STL/3MF in mm, fit test 4 gaten 0,15 tot 0,30 bij 0,2, opslaan per printer + materiaal en terugzetten bij wisselen, nummers "2-3"/"3-2" van onder naar boven (sorteren op z, y, x), rood onder 0,8 mm wand of te groot of niet dicht, vrije snede alleen binnen de rechthoek met "Move it at least 1.2 mm" (standaardwand 1,2). | feit (code) | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Printzin in alle zes, geen prijs, geen "snap/click together", geen AI of stem in titels. | feit | hoog | eerlijk, besluit 23 nov |
| B2 | "Alleen plaatsen als Click Cuts live is" staat erin. Goed. | feit | hoog | |
| B3 | 6B "slicer-achtig beeld": alleen eigen render, geen UI van een echte slicer. Staat er al. | feit | hoog | |

## Deel C: zou een kijker het leuk vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Alle zes eindigen met dezelfde twee zinnen (printzin en eindkaart); bij zes Shorts in een week ziet een vaste kijker dat. | Wissel de printzin tussen twee varianten met dezelfde inhoud, bv. "Not print tested by us yet. Print the fit test first." | klein |
| C2 | Script 1 laat het mooiste beeld (Lion Head in felle kleuren uit elkaar) pas bij zin 4 zien. | Flits van 0,5 s van het eindbeeld vóór 1A of als achtergrond onder de kop. | klein |
| C3 | 2B met de klok "10 h" werkt goed als angst van de kijker; leest niet als belofte. Mag blijven. | | |
| C4 | Script 2 zin 2: de stellige zin is goed, algemeen bekend in de printwereld; de zachtere reserve hoeft niet. | | |

## Moet
- **M1 (script 4, zin 4 en 7):** geen Check-kleuren in beeld zolang "oranje" geel is. Of de bouwer maakt oranje echt oranje vóór de uitgave (bv. 1.0, 0.55, 0.0; ook goed voor de koper, die "orange" leest in de tooltip en geel ziet), of de opname toont alleen de lijst met iconen (vinkje, driehoek, kruis) en de kop zegt "Orange: thin wall". Voorkeur: kleur aanpassen, ik meld het bij Chris.
- **M2 (script 1, zin 5):** "Every cut gets pins and pin holes, with a clearance you can tune to your printer." (13 woorden). Of laat het weg; script 2 vertelt het al.

## Kan
- K1: script 5 beeld zin 4: eerst Split to fit drukken, dan de rode regel, dan More settings openen naar Convert to mm (A3, A4).
- K2: C1 en C2.
- K3: titel 5 "is tiny" past alleen bij één kant; "Imported STL the wrong size in Blender? It is the unit" dekt beide.
