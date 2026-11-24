# Keuring Split to fit, naam Click Cuts, snedeplek en vrije snede, 24 nov 2026, keurder klik
Wat ik keurde: commit c651793 (en 27951bb voor de vrije snede) in `producten/blender-splitser/`, opdrachten van de hoofdchat van 23 nov 23:35 en 24 nov 01:25 onderaan `berichten/productbouwer.md`, ontwerp.md deel 12.
Akkoord: nee (twee moet-punten, beide klein)

Hoe gemeten: zip gemaakt met `e2e/maak_zip.sh`, in Blender 5.3.0 lokaal `e2e/toetsen_klik.py` en `e2e/toetsen_vrij.py` gedraaid (beide `KLAAR 0 FOUT []`, GEZIEN), plus een eigen meetscript buiten de repo dat de add-on aanroept en de meshes meet (cilinder met Array-modifier, tweede model in dezelfde scene, andere printer en speling, vrije sneden op andere plekken). CI-run 45305657263 op c651793: 4.2.23 groen (GEZIEN), 5.3.0 liep nog bij het afsluiten van deze keuring. Paneelbeeld `blender-4.2.23-paneel-x.png` uit release `splitser-kern-1` (01:33 UTC) zelf bekeken.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Vrije snede werkt: 2 stukken, waterdicht en groen, gaten 6,30 mm diep langs de schuine normaal, nummers 1-2 en 2-1, 1 pen (log toetsen_vrij in 5.3.0). Na elkaar snijden werkt ook: een tweede vrije snede op stuk 2 bij x=70 en op stuk 1 bij x=30 gaf 3 en 4 stukken. | feit | hoog | eigen meetscript |
| A2 | **De toets "snede door een pengat geweigerd" bewijst het niet.** Stuk 2 staat na de snede in het uit-elkaar-beeld op wereld-x 56,35 tot 88,48 (gemeten); het vlak op x=52 mist het stuk dus helemaal en wordt geweigerd met "does not go through Piece 02". De toets kijkt alleen naar CANCELLED, niet naar de reden. | feit | hoog | log toetsen_vrij en eigen meting van de hoekpunten |
| A3 | De pengat-weigering zelf werkt wel: stuk 2 bij x=60 en stuk 1 bij x=46 en x=40 geweigerd met "goes through a pin hole of Piece 0x (to piece y). Move it at least 1.2 mm away"; daarbuiten (x=70, x=30) snijdt hij. | feit | hoog | eigen meetscript |
| A4 | Naam Click Cuts: manifest id `click_cuts` en name, tabblad en paneel "Click Cuts", collecties "Click Cuts cut planes", "Click Cuts pieces", "Click Cuts fit test", materialen "Click Cuts piece 01..", "Click Cuts pins", "Click Cuts green", 3MF-metadata "Click Cuts", exportmap `//click_cuts/`. Geen zichtbare "Split Joints" meer over (grep), alleen interne klassenamen. | feit | hoog | grep, lijst van collecties en materialen na een klik, paneelbeeld |
| A5 | Split to fit geeft dezelfde stukken als Plan cuts plus Split, ook op een eigen model dat anders is dan de testmodellen: cilinder 180 x 420 mm met Array-modifier (2x) en 20 graden gedraaid, speling 0,30: 18 stukken, 138 pennen, zelfde maten, gaten per stuk en status, beide wegen `GELIJK True`. Gat-straal 2,80 mm volgt de speling. | feit | hoog | eigen meetscript |
| A6 | Andere printer en speling volgen: na K1 en 0,15 mm gaf een nieuwe klik 8 stukken (180 x 127 x 210 mm), uitslag "8 parts, all fit the bed / 30 pins, 0.15 mm clearance". | feit | hoog | eigen meetscript |
| A7 | **Split to fit op een tweede model snijdt het oude model opnieuw.** Na een klik op de cilinder een bol gemaakt, alleen de bol geselecteerd en actief, Split to fit: `bron` bleef "Cyl", de cilinder werd opnieuw in 18 stukken gesneden, de bol bleef heel. De knop zegt "Cut the selected model". Oorzaak: `snedes.model()` neemt eerst `scene.split_joints.bron`. Een koper die een tweede model in hetzelfde bestand laadt, ziet zijn eerste model weer gesneden en niets aan zijn nieuwe. | feit | hoog | eigen meetscript, regel 100 van `snedes.py` |
| A8 | Eén uitslagregel klopt met de stukken ("3 parts, all fit the bed", "8 pins, 0.20 mm clearance"), meters weigeren direct met "Wrong unit? Open More settings and use Convert to mm", open Suzanne krijgt eerst een dichte kopie. Vier stappen staan onder een inklapbaar "More settings" (paneelbeeld). | feit | hoog | log toetsen_klik, paneelbeeld 4.2 |
| A9 | Snedeplek: `Object.sj_plek_mm` heeft precisie 1 (0,1 mm), stap 0,1 mm, en leest en zet goed in een mm- en een meter-scene (12,3 mm wordt 0,0123 m). In het paneelbeeld staat More settings dicht, dus de afgeronde weergave heb ik niet met eigen ogen gezien. | feit (beeld: vermoeden) | hoog / midden | RNA-precisie en toets; beeld met More settings open |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Bestaande tests niet verzwakt: alleen namen aangepast, de kleurtoets is strenger geworden (exacte materiaalnamen). | feit | hoog | tests niet aangepast om te slagen |
| B2 | Alle bestanden onder 400 regels (grootste `vrije_snede.py` 364). | feit | hoog | ±400 regels |
| B3 | `architectuur.md` bijgewerkt met `in_een_klik.py`, `sj_plek_mm`, paneel en beide toetsen. `ontwerp.md` heeft nog geen deel voor Split to fit. | feit | hoog | architectuur bijgewerkt |
| B4 | Geen persoonsgegevens in de diff gevonden. | feit | midden | openbare repo |
| B5 | Toets A2 claimt in de docstring en in ontwerp deel 12 "geweigerd: vlak door een pengat" als bewezen, terwijl het om een andere reden weigert. | feit | hoog | eerlijk, werk pas af als de tests het bewijzen |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Het paneel is nu kort en duidelijk: printer, Split to fit, één vak met vinkje, Export. Dat is de 60-secondenbelofte. | (goed zo) | |
| C2 | De knop Split to fit is grijs, net als Export; in de schets is hij goud en springt hij eruit. | knop met `depress` of een opvallender icoon, of Export kleiner zodat Split to fit de enige grote knop is | klein |
| C3 | De rij Connectors (Pins, Click, None) uit de schets ontbreekt. | later toevoegen als Click-verbinders er zijn; nu niet nodig | midden |
| C4 | De printerkeuze staat twee keer (bovenaan en in stap 1). | in stap 1 alleen marge en eigen maten | klein |
| C5 | Na een geweigerde klik blijft de rode regel "Wrong unit?" staan, ook na Convert to mm, tot de volgende klik. | Convert to mm wist de regel | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
- M1 (A7): Split to fit moet het geselecteerde model snijden. Is het actieve object een ander mesh dan `bron` (en geen stuk, pen, snede of proefblok), dan wordt dat het nieuwe model en worden de oude sneden en stukken niet hergebruikt. Toets erbij in `toetsen_klik.py`: tweede model in dezelfde scene, klik, de stukken komen van het tweede model.
- M2 (A2, B5): de toets "snede door een pengat geweigerd" moet het pengat raken en op de reden toetsen (melding bevat "pin hole"), bijvoorbeeld vlak op het echte gat van stuk 2 in het uit-elkaar-beeld of uit-elkaar eerst uit. Plus een toets dat een vlak net buiten het gat wel snijdt.

**Kan**
- K1 (A9): schermafbeelding met More settings open, zodat "Cut X (mm) 101.5" met eigen ogen te zien is.
- K2: CI 5.3.0 op c651793 groen zien voor de kandidaat van do 27 nov.
- K3: deel in `ontwerp.md` voor Split to fit.
- K4: C2, C4, C5 hierboven.
