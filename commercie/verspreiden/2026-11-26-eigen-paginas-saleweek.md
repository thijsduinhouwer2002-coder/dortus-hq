# Eigen pagina's vóór de saleweek: vier keer "not print tested" weg, en de sale op de gratis Gumroad-pagina (Verspreider, run 21, do 26 nov 2026, C)

**Status:** keuring Daan gevraagd. Na zijn ja: deel 1 en 2 doet Bram (repo's dortus en click-joints), deel 3 de hoofdchat (Gumroad, samen met de saleregel op Pro).

## Waarom (geld en eerlijkheid)
Wie in de saleweek van ons hoort, komt vaak eerst op onze eigen pagina's: dortus.com/click-joints (BlenderNation is onze grootste verwijzer, GEZIEN in `organisatie/meten/stand.md`), de gidsen en de GitHub-pagina van de add-on (25 bezoeken, 14 mensen in 14 dagen, waarvan 5 via dortus.com, GEZIEN, GitHub traffic-API 26 nov ±08:57 NL). Op vier van die plekken staat nog "not print tested by us yet". Thijs besliste op 24 nov 15:32 dat dat nergens meer mag ("komt super onprofessioneel over"; `organisatie/besluiten.md` regel 20). Op 24 nov ging het van Gumroad, Superhive en de hoofdpagina's af (`commercie/geplaatst.md` regel 41), maar deze vier bleven staan. Een koper die twijfelt, leest die zin op het slechtste moment.

Effect op verkoop: GOK, klein maar zeker niet negatief. Kost: ±10 minuten voor Bram, ±1 minuut voor de hoofdchat.

## Wat ik zag (GEZIEN, curl en git, 26 nov ±08:55 NL)
| Plek | Regel | Staat er nu |
|---|---|---|
| dortus.com/click-joints/ (`dortus/click-joints/index.html`) | 187, blok Fit test strip | `<em>Not print tested by us yet.</em> 140 &times; 52 &times; 45 mm, 10 parts, made with Click Joints Pro.` |
| dortus.com/click-joints/gids/articulated-figure-3d-print-blender/ | 141 | `These numbers are measured in Blender, not print tested by us yet. Print one test joint before the whole figure, every printer is different.` |
| dortus.com/click-joints/gids/hinge-joint-3d-print-blender/ | 123 | `These numbers are measured in Blender, not print tested by us yet. Print one test hinge before the whole figure, every printer is different.` |
| github.com/thijsduinhouwer2002-coder/click-joints, `README.md` | 30 | `Measured in Blender, not print tested by us yet: print a test joint first. Works best on figures of about 200 mm or taller with separate arms and legs, in Blender 4.5 or newer. ...` |

Nagekeken en schoon: dortus.com/, /yt, /tt, extensions.blender.org, Gumroad Pro, Gumroad gratis, Superhive Pro, CHANGELOG van click-joints. Printables kon ik niet lezen (Cloudflare); die tekst werd op 23 nov al aangepast (`2026-11-23-printables.md` regel 165).

## Deel 1: dortus.com (Bram, repo dortus)

**1a. `click-joints/index.html` regel 187**, vervang de hele regel door:
```html
          <p class="lede" style="margin-top: 0.8rem"><em>Every printer is different.</em> 140 &times; 52 &times; 45 mm, 10 parts, made with Click Joints Pro.</p>
```
(Het blok heet al "Print this first"; "Every printer is different" is de zin die Thijs op Printables koos.)

**1b. `click-joints/gids/articulated-figure-3d-print-blender/index.html` regel 141:**
```html
          <p>These numbers are measured in Blender. Print the <a href="/click-joints/#fit-test">Fit test strip</a> first: every printer is different.</p>
```

**1c. `click-joints/gids/hinge-joint-3d-print-blender/index.html` regel 123:**
```html
          <p>These numbers are measured in Blender. Print the <a href="/click-joints/#fit-test">Fit test strip</a> first: every printer is different.</p>
```
Het anker `#fit-test` bestaat (`<div class="head" id="fit-test">`, regel 175 van `click-joints/index.html`, GEZIEN).

## Deel 2: README van de add-on (Bram, repo click-joints)

**2a. `README.md` regel 30**, vervang de hele alinea door:
```markdown
Measured in Blender. Print the [Fit test strip](https://dortus.com/click-joints/#fit-test) first: every printer is different. Works best on figures with separate arms and legs, at about 200 mm tall or more. Best in Blender 4.5 and newer; in Blender 4.2 it works, but some joints may need to be placed by hand (the list tells you which). A joint that does not fit is skipped, and the list says why. The free Click Joints and Pro can not be enabled at the same time: disable the free one first.
```
Bron per zin: de live Gumroad-pagina van Pro, blok "Good to know" en "Honest when it can not" (GEZIEN, curl 26 nov ±08:56 NL): "about 200 mm tall or more", "Best in Blender 4.5 and newer. In Blender 4.2 it works, but some joints may need to be placed by hand (the list tells you which)", "Print the Fit test strip first: every printer is different." Zo spreekt de README regel 7 ("Blender 4.2 LTS, 5.2 LTS and 5.3") ook niet meer tegen. De laatste zin blijft tot 1.2.9 (ma 30 nov); daarna gaat hij eruit, net als op de Superhive Docs-tab (`producten/blender-gewrichten/KAART.md`, #114).

**2b. Alleen in de saleweek, README regel 9**, vervang `$19 once,` door:
```markdown
$19 once (25% off from November 27 to December 1),
```
Dezelfde woorden als op dortus.com/click-joints nu al staan (GEZIEN). **Weghalen op wo 2 dec** (terug naar `$19 once,`). Wie de datum mist, laat 2b weg: deel 2a is het belangrijke.

## Deel 3: gratis Gumroad-pagina (hoofdchat, vr 27 nov, in dezelfde Gumroad-sessie als de saleregel op Pro)
**Pas plakken als `bash platformen/blender/sale-controle.sh` bij stap 1 GOED zegt** (de salelink geeft `"valid":true`).

Op https://duinhouwer8.gumroad.com/l/click-joints-free staat nu als laatste alinea: "Want a whole figure that moves? Click Joints Pro reads your rig ... https://duinhouwer8.gumroad.com/l/click-joints-pro" (GEZIEN). Zet direct daaronder één regel:
```
Cyber Week: Click Joints Pro is 25% off until Tuesday December 1, 23:59 CET. This link applies the discount: https://duinhouwer8.gumroad.com/l/click-joints-pro/CYBER25?utm_source=gumroad&utm_medium=gratis
```
- Feiten: CYBER25, 25%, t/m di 1 dec 23:59 NL (`platformen/blender/pro-sale-27nov.md` deel 1 en 3; CET is de tijd in Nederland in december). De link met code en utm werkt (GEZIEN door Bram, 25 nov, met `utm_source=yt`). "applies the discount" klopt zodra stap 1 GOED is, of vanzelf toepassen nu aan staat of niet.
- **Weghalen op wo 2 dec**, samen met de saleregel op Pro.
- Eerlijk over het bereik: de gratis Gumroad-versie heeft 0 downloads in het scorebord (GEZIEN, `organisatie/scorebord.md`). Dit is dus vooral voor wie hem deze week vindt; het kost een minuut.

## Bewust niet
- Geen sale-zin op extensions.blender.org: reclame op de Blender-site riskeert regel 6 van hun voorwaarden (al eerder afgewogen, `2026-11-24-extensions-beoordelingen.md`).
- Geen sale op Printables: bewust zonder prijs, zodat de tekst na 1 dec klopt (`2026-11-23-printables.md` regel 66).
- dortus.com/yt noemt de sale niet, maar /yt krijgt ±0 tot 2 bezoeken per dag (GEZIEN, `organisatie/meten/stand.md`); dat laat ik aan Bram bij de utm-knoppen.

## Meten
- Vr 27 nov: met curl nakijken dat "print tested" op geen van de vier plekken meer staat.
- GitHub traffic van click-joints (nu 25 bezoeken, 14 mensen in 14 dagen) en Gumroad-verkopen met `utm_source=gumroad` in het scorebord, t/m 10 dec. Niets via `utm_source=gumroad` na 14 dagen: deel 3 voortaan niet meer doen bij een sale.
