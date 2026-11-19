# Click Joints Pro op Superhive: pakket voor de Cyber Sale (Bram, 19 nov 2026)

Opdracht hoofdchat 19 nov 09:20 NL. Alles hier is klaar om te plakken of te uploaden. Wat alleen een mens kan staat in `mens-lijst.md`. Wat op de Pro-map leunt staat in `inventaris-pro.md`. Keuring: Daan (gevraagd 19 nov).

## Eerst lezen: de stand is anders dan de opdracht dacht
- **Pro staat al op Superhive, in de keuring.** Product 269495, ingediend 15 nov 19:45 NL met ja van Thijs, status Pending (zie `../superhive-pagina.md`). Superhive zegt "Reviews typically take 3 to 5 days" (DERDEN, support-artikel 195). De productpagina geeft vanaf hier 403 (GEZIEN 19 nov 09:30 UTC), dus nog niet openbaar.
- **Tijdens Pending kan niets veranderen** ("Editing is paused while your product waits for review", DERDEN, artikel 195). Alles hieronder gaat er pas op na goedkeuring, of bij "Changes requested".
- **Een nieuwe maker mag maar één product tegelijk in behandeling hebben** tot het eerste is goedgekeurd (DERDEN, artikel 388). Dus geen tweede pagina beginnen; deze bijwerken.
- **De zwarte schermbeelden zijn opgelost.** De Pro-beelden uit run 44438033323 (19 nov 01:52 UTC, commit 362e9ff, Blender 5.3.0) zijn gewoon in kleur; ik heb ze zelf bekeken (GEZIEN). De 6 beelden hieronder komen daaruit.

## Prijs (opdracht: $19, met korting in de sale)
- Nu ingediend: Personal $12, Studio (tot 5 personen) $45. Gumroad: $12 (GEZIEN, reddit.md).
- Voorstel na goedkeuring: **Personal $19, Studio $59**. Gumroad gelijk trekken naar $19, anders koopt men daar goedkoper (beslissing hoofdchat of Chris).
- **Cyber Sale:** Superhive geeft in sitebrede sales meestal 25% korting (DERDEN, artikel 300). $19 min 25% = **$14,25**; Studio $44,25. Netto voor ons op het gratis plan bij $14,25: 70% min $0,49 = ±$9,49 (GOK, rekensom; de 5,5% merchant fee komt er mogelijk nog af).
- Let op: een eigen "Shop Sale Campaign" werkt niet tijdens een sitebrede sale (DERDEN, artikel 315). Dus alleen het vinkje "Opt-in to all sitewide sales".
- De $9-lanceerprijs uit `../superhive-pagina.md` vervalt: niet vlak voor de sale omlaag en dan weer omhoog.

## Gratis variant ($0): kost geld, dus nu niet
- **$0 kan alleen met een betaald makersabonnement** (Pro $49 per maand of Ultimate $199). "This feature is not available to Creators at the free level", en de laagste prijs is anders $1 (DERDEN, artikelen 281 en 302, prijspagina). Dat is geld uitgeven: alleen met ja van Thijs.
- Mijn advies: **niet doen**. $49 per maand vraagt ±5 verkopen per maand alleen om quitte te spelen (GOK, rekensom), en de gratis versie staat al op extensions.blender.org (234 downloads, GEZIEN 18 nov). Wil Thijs het toch: zip `producten/blender-gewrichten/uitgave/click_joints-0.1.1.zip` (gelijk aan Extensions) als variant "Free (ball joints only)" $0.

## Tags (max die het formulier toelaat; de 9 van 15 nov aanvullen met de woorden van de koper)
`3d printing`, `3d print`, `joints`, `ball joint`, `hinge`, `articulated`, `poseable`, `action figure`, `figure`, `rig to print`, `posable`, `stl`, `3mf`, `cosplay`, `miniature`

## Producttekst (Engels, na goedkeuring plakken in plaats van de tekst van 15 nov)

**Excerpt:** Turn a rigged character into a poseable 3D print: hinges with an end stop and ball joints with the bend range shown in degrees before you print.

**Title:** Click Joints Pro: poseable 3D print figures from your rig

**Description:**

**Make your figure poseable before you print it.**

Click Joints Pro cuts a character into printable parts with real joints: hinges for knees and elbows that stop at their limit, and ball joints for shoulders, hips and neck. You see the bend range of every joint in degrees in the viewport, so you know how far the printed figure will move before you spend hours printing.

What you get:
- **Figure from rig.** Select a rigged mesh and press one button. Click Joints places joints on shoulders, elbows, hips, knees and neck. Where your rig has a rotation limit, the hinge uses it ("from rig"); otherwise it takes 90°, 115° or 135°.
- **Hinge with an end stop** for knees and elbows. Measured in Blender: our test knee bends 0° to 115° and stops there, shown as a degree arc around the axis.
- **Red past the limit.** Bend further than the stop and the spots that collide turn red, with the number of degrees past the limit.
- **Green fit band.** A joint is only placed when the fit is good; the seam turns green.
- **Everything from the free Click Joints:** ball joints with a fit colour and ±degrees, split into watertight parts, export to STL or 3MF in millimetres.

**Split with anything. Make it move.** Already split your model into printable parts with another tool? Keep those parts. Open one, put the 3D cursor on the knee or elbow, and Click Joints Pro cuts a hinge or a ball joint right there, with the clearance you set and the range in degrees.

**Why not a ball joint by hand?** You can. What you only find out after the print is that the knee bends backwards, the wall next to the socket is too thin, or the ball is stuck. Click Joints shows all three before you print: an end stop on every hinge, the wall and clearance as a number, and the range in degrees.

Good to know:
- Clearance 0.2 mm by default. Print a test joint first; every printer is different.
- Works on Blender 4.2 LTS, 5.2 LTS and 5.3. We test every version on all three before release.
- The free Click Joints (on Blender Extensions) and Pro can not be enabled at the same time. Disable the free one first; your settings stay in the .blend file.
- Pure Python, no other add-ons needed.
- Support: the Superhive inbox, or https://github.com/thijsduinhouwer2002-coder/click-joints/issues

Nagekeken tegen de code en de beelden: knoppen Shoulder, Elbow, Hip, Knee, Ankle, Neck en "Place hinge, bends up to: 90° 115° 135°" staan in het paneel (beeld 1 en 6); 0 tot 115 en "+3° past limit" in beeld 2 en 3; 0,2 mm in het paneel (Clearance 0.20). Geen woord over AI, geen "I". 19 nov (Bram): "click hinge" werd "hinge" (geen klik beloven zonder print, opdracht hoofdchat) en de blokken "Split with anything" en "Why not by hand" erbij, zelfde als `platformen/blender-2/winkeltekst-1.1.md`.

## Beelden (map `beelden/`, allemaal 2:1, echte schermen uit Blender 5.3.0)
Superhive eist minstens 5 beelden in 2:1, aanbevolen 1200 x 600 (DERDEN, artikel 41), en geen Blender-logo als ontwerpelement (artikel 253). De menubalk met het logo is er overal af gesneden.

| # | Bestand | Wat | Bron |
|---|---|---|---|
| 1 (uitgelicht) | `1-figuur-van-rig.png` | MakeHuman-figuur (CC0) na Figure from rig, knieën 120°, ellebogen 140°, paneel rechts | `19-mens-x.png` |
| 2 | `2-knie-boog-0-115.png` | knie met gradenboog 0° tot 115° | `13-pro-knie-x.png` |
| 3 | `3-rood-voorbij-de-stop.png` | rood, "+3° past limit" | `14-pro-knie-rood-x.png` |
| 4 | `4-groene-passing.png` | groene passingband dichtbij | `13d-pro-knie-dicht-x.png` |
| 5 | `5-kogel-rood-gratis-deel.png` | kogel met rood voorbij 20° (zit ook in gratis) | `9-winkel-rood-x.png` |
| 6 | `6-figuur-rig-scharnieren.png` | hele figuur, 4 scharnieren en kogels na één knop (achteraan, kan-punt Daan) | `17-figuur-heel-x.png` |

Bron: tak `schermen`, `referentie/blender-gewrichten/main/5.3.0/`, run 44438033323. Beeld 1 (19 nov 10:20 UTC, kan-punt Daan): figuur en paneel uitgesneden, links één regel tekst "From rig to poseable print in one click." in Inter, dan 1920 x 960. Beeld 6 is het hele scherm met een donkere rand tot 2:1; de rest is bijgesneden 1920 x 960. Label 115° in beeld 3 vrijmaken vraagt een nieuwe opname: bij een volgende run. Demofilm v3 blijft de eerste preview (release `click-joints-pro-film-v1`), al toont die nog de knie zonder Figure from rig.

## Zip
Na goedkeuring 1.1.0 uploaden (de pagina heeft nu 1.0.1). Workflow `click-joints-pro-uitgave.yml` met een groene e2e-run op main maakt artefact `click-joints-pro-zip-1.1.0`. Het artefact van 1.0.2 is verlopen op 19 nov 04:41 UTC; 1.1.0 is nieuwer en vervangt het.
