# Plakkaart Click Cuts: de laatste meter (issue #300)

Productbouwer, vr 27 nov 2026 ±20:35 NL. **Eén kaart voor alles wat nog geplakt moet worden voor Click Cuts**, op volgorde van geld. Plakken doet de hoofdchat (Chrome van Thijs, inloggen alleen Thijs). Na elk deel één controle met curl: `bash producten/blender-splitser/winkel/controle-laatste-meter.sh <deel>` moet eindigen op `ALLES GOED`. Geeft hij FOUT: dat blok opnieuw plakken en opnieuw draaien. Stopt bij de eerste fout.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## Wat al staat (niet opnieuw doen)
| Wat | Stand |
|---|---|
| Click Cuts 1.0.0 op Gumroad, $19 en Supporter $29 | live sinds 27 nov ±15:00 (GEZIEN, `commercie/geplaatst.md`) |
| Gumroad Click Cuts linkt naar de gids dortus.com/click-cuts (kruisverwijzing B1) | geplakt 27 nov ±20:15; curl ziet de link (GEZIEN, 27 nov ±20:25) |
| Upsells Pro naar Click Cuts en Click Cuts naar Pro (#295 deel 1) | live sinds 27 nov ±17:00 (GEZIEN, `commercie/geplaatst.md`) |
| Superhive Click Cuts 1.0.0 | ingediend 27 nov ±15:10, Pending, keuring 3 tot 5 dagen (DERDEN, #188) |

## Wat eruit is (dubbel)
**#295 deel 2 (Verspreider, regel onderaan de Content-tab van Pro en gratis) vervalt.** Kruisverwijzing B2 en B3 zetten dezelfde boodschap in de beschrijving, die ook bezoekers zien die nog niet kochten, en de zinnen "Splitting makes it fit on the bed. Click Joints Pro makes it move." staan al op de Click Cuts-pagina (Daan ja #289). Wel overgenomen uit deel 2: de utm in de link, zodat we zien welke pagina de koper bracht.

---

## Deel 1. Za 28 nov: Click Cuts 1.1.0 op Gumroad (het meeste geld)

**Waarom eerst:** 1.0.0 staat live zonder Draw cut, terwijl alle vier de rechters in de blinde test vroegen om zelf te kiezen waar het snijdt (`organisatie/lat/click-cuts.md` gat 3). De FAQ op Gumroad zegt nu "Partly"; na deel 1 "Yes", met het beeld erbij dat plek 1 haalde. Effect op verkoop: GOK. Kost niets, niet onder de naam van Thijs, geen promotie (besluit 27 nov 16:06 gaat over promoten, niet over het product zelf).

**Superhive niet nu:** daar ligt 1.0.0 in de keuring en kan niets veranderen (hoofdchat 27 nov 15:15, DERDEN artikel 195). Superhive krijgt 1.1.0 in deel 3, na goedkeuring.

### 1a. De zip
| | |
|---|---|
| Bestand | `click_cuts-1.1.0.zip` |
| Waar | e2e-run **46056960861** op main (commit a3d23511, 1.1 samengevoegd), artefact `click-cuts-kandidaat`; ingelogd te downloaden via https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/46056960861 . **Verloopt ma 30 nov 20:31 NL** (GitHub `expires_at` 19:31 UTC, GEZIEN): dus za 28 nov downloaden. Voor Superhive (deel 3, later) vastzetten met tag `click-cuts-uitgave-46056960861` (workflow `click-cuts-uitgave`, leest de versie uit de zip), of dezelfde gedownloade zip bewaren. |
| Groen in | Blender 4.2.23 en 5.3.0 (beide e2e-jobs `success`, GEZIEN via de API 27 nov ±20:36 NL) |
| sha256 | `bd591759e8c9aae943fad45ed871d8c8126447906b3c04955497e3b0640d3e7a` (GEZIEN: zelf gedownload en nagerekend, gelijk aan `SHA256SUMS.txt` in het artefact) |
| Nagekeken | 72.966 bytes, 26 bestanden; `blender_manifest.toml`: `version = "1.1.0"`, `name = "Click Cuts"`; `lijn.py` (Draw cut) en `hulp.py` (?-knop) zitten erin (GEZIEN) |

Niet uitpakken, niet hernoemen. Na het downloaden: `sha256sum click_cuts-1.1.0.zip` moet de waarde hierboven geven.

### 1b. Gumroad, product Click Cuts, tab Content
https://duinhouwer8.gumroad.com/l/click-cuts (Edit product, Content)
1. Bestand `click_cuts-1.0.0.zip` verwijderen, `click_cuts-1.1.0.zip` uploaden. Geldt voor Standard en Supporter (zelfde Content). Wie al kocht, downloadt de nieuwe zip van dezelfde pagina.
2. Bovenaan de tekst, boven "Getting started", dit blok als kopje met opsomming (de releasenote, gelijk aan `CHANGELOG.md` 1.1.0):
```
What's new in 1.1.0
- New: Draw cut. After Split to fit, click a part, press Draw cut and drag a line where you want it cut, for example under the chin or at the shoulder.
- New: before you cut, the part that comes off lights up white with an arrow that says "comes off". Wrong part? Press Flip side.
- New: the clearance starts at a value for your material until you save a fit test: Resin 0.10, PLA 0.20, PETG and ABS / ASA 0.25, TPU 0.30 mm. The fit test block covers that value.
- Better: after Split to fit, the result box names the clearance the parts were cut with, and tells you to split again when you change it.
- New: a ? in the panel header opens the guide on dortus.com/click-cuts/. Right click any Click Cuts button and choose Online Manual to jump to its part of the guide.
```
3. De rest van de tekst vervangen door het blok "Tekst voor de tab" uit `producten/blender-splitser/winkel/docs.md` (nu de 1.1-versie op main), met dezelfde aanpassing als op 27 nov: de zin "Got a folder instead of a zip? See the FAQ." wordt het antwoord uit de FAQ, want Gumroad heeft geen FAQ-tab. Wat er inhoudelijk verandert: zipnaam 1.1.0, fit test met startspeling per materiaal, en het stuk "Choose where it cuts: Draw cut" in plaats van "Free cut".

### 1c. Gumroad, product Click Cuts, beschrijving (Product, Description)
Drie plekken. De rest blijft woord voor woord.

Regel die begint met **Free cut:** wordt (met "Draw cut:" vet, zoals de andere regels):
```
- **Draw cut:** after Split to fit, click a part and drag a line where you want it cut, for example under the chin or at the shoulder. The part that comes off lights up white before you cut. Or add a free cut and set it with G, R and S.
```
Regel die begint met **Fit test:** wordt:
```
- **Fit test:** print one small block with your own pin at four clearances, pick the one that fits, and Click Cuts keeps it for that printer and material. Until then it starts at a clearance that suits your material, from 0.10 mm for resin to 0.30 mm for TPU.
```
Onder "Questions", bij de vraag "Can I choose where it cuts, so it does not go through a character's face?": het antwoord dat begint met "Partly." wordt:
```
Yes. Split to fit cuts along the X, Y and Z axes. After splitting, click a part, click Draw cut and drag a line where you want it cut, for example an arm at the shoulder or under the chin. The part that comes off lights up white before you cut, and it gets pins and numbers like the other cuts. Click Cuts does not find those places by itself.
```
Titel, haak, prijs, tags en de regel naar de gids blijven gelijk (titel en haak GESLAAGD; een nieuwe titel vraagt een nieuwe test).

### 1d. Gumroad, product Click Cuts, beelden (Cover)
Beeld toevoegen en naar **plek 2** slepen, direct na het hoofdbeeld (het beantwoordt de grootste twijfel van de koper):
- `ontwerp/cuts-galerij/beelden/tekenen-1920x1080.jpg` (16:9, zoals de vijf covers die er staan, alle 1920 x 1080, GEZIEN met curl 27 nov ±20:30).
- Blinde test GESLAAGD, Gemini 1,0 (`organisatie/blindtest/uitslag/click-cuts-galerij-tekenen-2026-11-27-1355.md`), Daan ja 8 (#278): "mag live, maar alleen samen met de 1.1-update". Daarom pas in dit deel.

Opslaan. Gumroad vraagt kopers te mailen over de wijziging: **niet doen** (gaat onder de naam van Thijs, en hij gaf geen ja op een tekst).

### 1e. dortus.com/click-cuts/ naar 1.1.0 (repo dortus)
Tak `claude/click-cuts-hulp-1.1` (1cb650f) samenvoegen in main, op hetzelfde moment als 1c. Wat er verandert: zipnaam 1.1.0, startspeling per materiaal bij de fit test, het stuk "Choose where it cuts: Draw cut" met het GESLAAGDE beeld `draw-cut.jpg` (1600 x 900, uit `tekenen-1920x1080.jpg`), FAQ "Yes", en één regel "New in 1.1.0. Bought 1.0.0? Download the new zip from the page where you bought it and install it the same way." Alle zinnen gelijk aan de gekeurde `docs.md` en `faq.md` (`python3 producten/blender-splitser/winkel/controleer_hulppagina.py <index.html van de tak>`: OK, GEZIEN). Bekeken op 390 en 1366 px, geen zijwaartse scroll (`keuring/beelden/2026-11-27-hulppagina-1.1-drawcut-*.jpg`, GEZIEN). Waarom nu: de ?-knop en Online Manual in 1.1 openen deze pagina; Draw cut springt naar `#free-cut`, en daar staat nu nog alleen Free cut.

### Controle deel 1
`bash producten/blender-splitser/winkel/controle-laatste-meter.sh 1`
Kijkt: Gumroad heeft "Draw cut", "Yes. Split to fit cuts", "from 0.10 mm for resin", 6 covers en geen "Partly." meer; dortus.com/click-cuts/ heeft "Choose where it cuts: Draw cut", "click_cuts-1.1.0.zip" en draw-cut.jpg geeft 200. Content (de zip en de Docs-tekst) ziet curl niet: kijk dat met eigen ogen in de bon van een testaankoop of via View content.

Na ALLES GOED: regel in `commercie/geplaatst.md` met het runnummer en de sha256, en een regel onderaan `berichten/productbouwer.md`.

---

## Deel 2. Zodra Superhive Click Cuts 1.0.0 goedkeurt: vindbaar maken
Besluit Thijs 27 nov 16:06: Click Cuts pas promoten na de goedkeuring van Superhive, dan alles tegelijk (`organisatie/besluiten.md`). Dit deel is het Click Cuts-stuk daarvan; Reddit en de bundel met Pro zijn van de hoofdchat en de Verspreider.

**2a. dortus.com:** tak `claude/click-cuts-tegel` (repo dortus, 75dc498) samenvoegen: tegel op de voorpagina naast Click Joints, en onder de Pro-knop op dortus.com/click-joints/ het kopje "Also from Dortus" met één zin naar Click Cuts. Gekeurd: Daan ja 8 (#289). Tekst: `winkel/kruisverwijzing.md` deel A.

**2b. Gumroad Click Joints Pro** (https://duinhouwer8.gumroad.com/l/click-joints-pro), nieuwe alinea helemaal onderaan de beschrijving. Tekst B2 uit `winkel/kruisverwijzing.md` (Daan ja 8, #289); alleen de link heeft nu de utm uit #295:
```
**Model too big for your printer bed?** [Click Cuts](https://duinhouwer8.gumroad.com/l/click-cuts?utm_source=gumroad&utm_medium=description&utm_campaign=pro) splits it into parts that fit, with pins or magnet holes and a number on every part, $19 once. Splitting makes it fit on the bed. Click Joints Pro makes it move.
```
**2c. Gumroad Click Joints (gratis)** (https://duinhouwer8.gumroad.com/l/click-joints-free; let op: `kruisverwijzing.md` B3 noemt /l/click-joints, die geeft 404, GEZIEN curl 27 nov ±20:35), zelfde alinea helemaal onderaan, met `utm_campaign=free` in de link.

Let op de prijs: "$19 once" klopt tot en met zo 14 dec (introprijs, besluit Thijs 25 nov 22:03). Daarna "$19" uit B2 en B3 halen of aanpassen.

**2d. Superhive Click Joints Pro:** zelfde alinea B2 onderaan de beschrijving, met de link https://superhivemarket.com/products/click-cuts (kruisverwijzing deel C: van Superhive naar Superhive, niet naar Gumroad).

### Controle deel 2
`bash producten/blender-splitser/winkel/controle-laatste-meter.sh 2`
Kijkt: Superhive Click Cuts geeft een productpagina (nu nog 403 "Access forbidden", GEZIEN 27 nov ±20:35); voorpagina dortus.com noemt Click Cuts; dortus.com/click-joints/ heeft "Also from Dortus"; Gumroad Pro en gratis hebben "Model too big for your printer bed?" en de link naar /l/click-cuts; Superhive Pro linkt naar /products/click-cuts.

---

## Deel 3. Na de goedkeuring van 1.0.0: Superhive naar 1.1.0
Pas als Superhive Click Cuts op Approved staat (anders blokkeert een wijziging de keuring). Alles staat al in `winkel/update-1.1.md` (Daan ja #249), met deze aanvullingen:
1. Nieuwe versie uploaden: dezelfde `click_cuts-1.1.0.zip` als in deel 1 (zelfde sha256), Blender 4.2 en nieuwer.
2. Update log bovenaan: blok 3 uit `update-1.1.md`.
3. Beschrijving: de twee regels Draw cut en Fit test uit 1c (gelijk aan `update-1.1.md` punt 4).
4. Docs-tab en FAQ-tab: het hele blok "Tekst voor de tab" uit `winkel/docs.md` en `winkel/faq.md` op main (1.1-versie). De FAQ-tab heeft daarmee ook "Yes" bij zelf kiezen waar het snijdt.
5. Product Images: `ontwerp/cuts-galerij/beelden/tekenen-2400x1200.jpg` (2:1, zoals Superhive vraagt) erbij, op plek 2 na het hoofdbeeld.

### Controle deel 3
`bash producten/blender-splitser/winkel/controle-laatste-meter.sh 3`
Kijkt: Superhive Click Cuts noemt "Draw cut" en "1.1.0"; Docs-tab heeft "click_cuts-1.1.0.zip"; FAQ-tab heeft "Yes. Split to fit cuts" en geen "Partly." meer.

---

## Waar elke tekst vandaan komt
| Blok | Bron | Keuring |
|---|---|---|
| Releasenote 1.1.0 | `CHANGELOG.md` kop 1.1.0 (`controleer_update.py` kijkt na dat ze gelijk zijn: OK) | Daan #249; regel over ? en Online Manual: Daan #272 |
| Draw cut en Fit test (beschrijving) | `update-1.1.md` punt 4 | Daan #249 |
| FAQ "Yes" | `faq.md` (1.1) | Daan #240 |
| Docs-tab 1.1 | `docs.md` (1.1) | Daan #240, installzin #254 |
| Beeld Draw your own cut | `ontwerp/cuts-galerij/beelden/tekenen-*` | GESLAAGD, Daan #278 |
| B2 en B3, tegel | `kruisverwijzing.md` | Daan #289 |
| Nieuw op deze kaart, nog niet gekeurd | de regel "New in 1.1.0. Bought 1.0.0? ..." op de hulppagina, het kopje "What's new in 1.1.0" in Content, de utm in B2 en B3, de keuze voor plek 2 | keuring op deze kaart (#300) |
