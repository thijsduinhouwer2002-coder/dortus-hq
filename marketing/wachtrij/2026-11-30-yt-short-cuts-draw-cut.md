# Short Click Cuts 1.1: Draw your own cut | Blender

- status: groen (Daan ja 8, #393, met voorwaarde: pas plaatsen als Gumroad 1.1.0 met Draw cut toont); eerste beeld GESLAAGD (r2, Gemini 1,5: plek 1 en 2, `organisatie/blindtest/uitslag/click-cuts-short-draw-cut-2026-11-28-1352.md`, GEZIEN)
- kanaal: yt-short
- soort: video
- product: click-cuts
- issue: #384
- bestand: `marketing/wachtrij/2026-11-30-yt-short-cuts-draw-cut.mp4` (1080x1920, 30/1, 480 beelden, 16,00 s, GEZIEN met ffprobe)
- plaatsen: pas als Click Cuts 1.1.0 op Gumroad staat (Draw cut zit niet in 1.0.0); datum in de bestandsnaam is een voorstel, de hoofdchat kiest
- beeld: echte schermopname van Blender 5.3.0 met interface onder Xvfb 1080x1920, Click Cuts 1.1.0 (main), Horse Statue 01 van Poly Haven (CC0). Werkwijze als v8b (`commercie/filmpjes/regisseur-33/cuts9.py`): beeld voor beeld op een klok van 1/30 s, echte X-muis en echte kliks (XTest), scherm gepakt met mss. In beeld: de gebruiker klikt het hoofd, drukt Draw cut, sleept een echte lijn onder de kin over de hals (de echte modal van Draw cut maakt het snijvlak; de hals licht wit op met "comes off"), Flip side heen en terug, Cut piece, draait om het gesneden hoofd en zoomt uit naar het hele paard in 13 delen. Uitkomst in de opname (GEZIEN, film.json): 12 delen vóór, 13 na, alle 13 groen, 52 pennen, vangnet leeg (elke klik raakte echt)
- Eerlijk over de opname: Split to fit gebeurde vooraf (niet in beeld, dat laat de lanceer-Short al zien). Het uitzoomen naar alle delen (0,9 s) zet het script, zoals in v8b. De muiswijzer is in de montage op de echte plek getekend (mss neemt de wijzer niet op); tijdens Draw cut een kruisje, zoals Blender dan toont
- hook (vast in beeld tot net na de lijn, 3,6 s, onderin op een donkere band zodat het model vrij blijft): "No seam through the face? / Draw your own cut:" (Poppins ExtraBold, won de blinde test lettertype van 27 nov). Ronde 2: ronde 1 ("Don't want a seam / through the face? / Draw your own cut:" over het model) haalde Gemini 2,5, NIET GESLAAGD (`organisatie/blindtest/uitslag/click-cuts-short-draw-cut-2026-11-28-1339.md`): tekst bedekte het model, meer kleur. Nu verder uitgezoomd met meer gekleurde delen in beeld en de tekst op een band
- eindtekst (laatste 3 s, donkere band zoals v8b): "Click Cuts 1.1, / add-on for Blender" (geen prijs of winkel in beeld)
- muziek: "Deep Urban", Eugenio Mininni (Mixkit, https://assets.mixkit.co/music/623/623.mp3), vanaf 175,9 s, zoals v8c en v8b. Licentie: Mixkit Stock Music Free License (DERDEN, https://mixkit.co/license/#musicFree): YouTube en social, ook commercieel, geen naamsvermelding nodig
- gemaakt_door: Regisseur (28 nov 2026)

## Titel
No seam through the face? Draw your own cut | Blender

## Tekst
```
Choose where your model gets split for 3D printing. New in Click Cuts 1.1 for Blender:
1. After Split to fit, click a part and press Draw cut.
2. Drag a line where you want it cut, for example under the chin. The part that comes off lights up white.
3. Wrong part? Press Flip side. Then press Cut piece.

Print the fit test first: every printer is different.
Click Cuts, add-on for Blender: https://duinhouwer8.gumroad.com/l/click-cuts?utm_source=youtube_short

Model: Horse Statue 01 by Poly Haven (CC0).
Music: "Deep Urban" by Eugenio Mininni (Mixkit)

#blender #3dprinting #b3d #blenderaddon
```
Bron per bewering: stappen 1 tot 3 en "lights up white" uit `producten/blender-splitser/CHANGELOG.md` kop 1.1.0 (woord voor woord op de knopnamen); "Print the fit test first" uit de tekst van v8b.

## Controle (Regisseur, GEZIEN, 28 nov ±14:15 NL)
- ffprobe: 1080x1920, 30/1, 480 beelden, 16,00 s; 0 tijdstempels buiten 1/30 s. mpdecimate houdt 426 van 480 over: de bijna gelijke beelden zitten in de korte rustmomenten van de hand (na een klik), niet midden in een beweging.
- geluid_check GOED (gemiddeld -13,4 dB, piek -2,0 dB). Geen stem, dus geen synchroon-controle nodig.
- Eerste beeld groot en 12 beelden uit de film zelf bekeken (`commercie/filmpjes/regisseur-33/strook.jpg`, 1 per 1,33 s): echte Blender 5.3-interface met paneel, lijn en "comes off" goed leesbaar, Flip side wisselt zichtbaar, na Cut piece "13 parts, all fit the bed".
