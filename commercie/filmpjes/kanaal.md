# YouTube-kanaal Dortus (@dortusstudio): profiel om in te vullen

Door Chris, 16 nov 2026, run 58. Opdracht: hoofdchat 16 nov 09:25 (`berichten/chris.md`). Daan keurt de beelden; daarna zet de hoofdchat alles erop in YouTube Studio. Niets hiervan vraagt een login van mij.

**Stand (GEZIEN 16 nov ±11:50 UTC, curl op https://www.youtube.com/@dortusstudio):** kanaal heet "Dortus", beschrijving leeg, geen video's.

## Wat het kanaal is (keuze, met reden)
Het kanaal is vooral **Blender-tips voor 3D-printen**: de dagelijkse korte filmpjes uit `reeks.md` en de langere video uit `youtube-1.md`. Daar ligt het bewijs van Joris: mensen volgen tips, geen reclame (Blender Secrets, VAW.BE), en kleine kanalen die groeiden hielden één vaste kopvorm aan ("Blender Tip: ..."). Het spel heeft een eigen TikTok (@hatsofthefallen); de trailer van Hats of the Fallen kan later ook hier, maar het spel staat nog niet in de beschrijving, want de Steam-pagina is er nog niet (regel uniform: een product pas noemen als het te vinden is).

## 1. Beschrijving (Studio > Customization > Profile > Description)
Engels, 588 tekens (GEZIEN, geteld met Python; grens 1.000 tekens is GOK uit het hoofd, YouTube Help noemt geen getal):

```
Short Blender tips for 3D printing. One problem, one fix: ball joints that click in and still turn, clearances that fit your printer, walls thick enough to hold a joint, exports at the right scale.

Every tip is checked in Blender itself before it goes up.

Dortus is a one-person studio from the Netherlands. I'm Thijs. I make focused tools, like Click Joints, a free add-on on Blender Extensions that cuts printable joints into your model. Small games are on the way. AI agents write the code, I direct and test.

Questions, or a tip you want to see: thijs@dortus.com
https://dortus.com
```

Waarom zo:
- **Eerste zin is de belofte** (wat je hier krijgt, voor wie). Geen "innovatief", geen cijfers zonder bron (toon uit `platformen/abel/merk/teksten.md`).
- **Alleen wat klopt:** "click in and still turn" en "clearances" volgen Brams nakijk van dag 1 (speling bepaalt of de kogel draait, niet het inklikken); "walls thick enough" is dag 2 met dag 4 als aanvulling (1,5 mm wand); "exports at the right scale" is dag 7. Geen "small games" als belofte van nu: er is nog geen spel uit (Daan, kan 5 bij Abel), dus "Small games are on the way", zoals de goedgekeurde regel "Focused tools today, small games on the way" (`platformen/abel/merk/LEESMIJ-upload.md`). Geen "print-in-place": Click Joints print de delen los (`youtube-1.md`).
- **"Checked in Blender itself":** klopt voor de reeks, Bram keek elke tip na in de echte Blender (`platformen/blender/tips-nagekeken.md`). Komt er een tip die niet zo is nagekeken, dan niet plaatsen of deze zin aanpassen.
- **AI-zin:** `AI agents write the code, I direct and test.`, dezelfde zin als in de onderschriften (`reeks.md`), niet "with the help of AI", want dat maakt de rol van AI kleiner dan hij is. Eerlijk zijn is een harde eis (hoofdchat 9 nov), en op r/blender is "snel met AI gemaakt" nu een rode vlag (Joris, 16 nov). Wie het vooraf leest, kan kiezen; wie het later ontdekt, voelt zich bedrogen. Kort en rustig.
- **"I'm Thijs":** het kanaal is van Thijs en hij plaatst; "we" zou een team suggereren.

## 2. Links (Studio > Customization > Profile > Links)
De eerste link staat groot naast de abonneerknop (DERDEN: https://support.google.com/youtube/answer/2972003, "Your first link will be prominently displayed"). Tot 14 links.

| Volgorde | Titel | URL | Waarom |
|---|---|---|---|
| 1 | Click Joints (free Blender add-on) | https://extensions.blender.org/add-ons/click-joints/ | Wie een tip ziet, kan in één klik de add-on halen; de pagina geeft 200 (GEZIEN 16 nov). Niet dortus.com/click-joints/: daar staat op main nog "On its way to Blender Extensions" (oud, wacht op het ja van Thijs). |
| 2 | Dortus | https://dortus.com | Alles van de studio. |
| 3 | Source and issues | https://github.com/thijsduinhouwer2002-coder/click-joints | Bewijs dat het blijft (open broncode, meldingen). |

Later toevoegen: dortus.com/click-joints/tips/ (nu 404, staat op een tak van Abel, GEZIEN 16 nov) en de Steam-pagina van Hats of the Fallen als die live is.

## 3. Contact (Studio > Customization > Profile > Contact info)
`thijs@dortus.com` (vast supportadres, `organisatie/doelen.md`).

## 4. Beelden (Studio > Customization > Profile)
Alle bestanden in `commercie/filmpjes/kanaal/`, gemaakt met `maak_kanaal.py` op het uniform van Mila (zelfde deur-D, kleuren, licht en spullen; alleen een geprinte arm met kogelgewricht erbij, want Click Joints is het product van dit kanaal en het uniform zegt: komt er een product bij, dan rolt dat er ook uit).

| Bestand | Maat | Eis van YouTube (DERDEN: https://support.google.com/youtube/answer/10456525) | Uitkomst (GEZIEN) |
|---|---|---|---|
| `profielfoto-800.png` | 800 x 800 | JPG/GIF/BMP/PNG, max 15 MB, wordt getoond op 98 x 98 | 61 KB. De avatar v2 die Daan op 10 nov goedkeurde (`ontwerp/keuring-abel.md`), niet veranderd, alleen op 800 gezet. Rond op 176, 98, 48 en 24 px op wit en op zwart: `proef-profielfoto-rond.png`. |
| `banner-2560x1440.png` | 2560 x 1440 | aanbevolen 2560 x 1440, min 2048 x 1152, 16:9, max 6 MB, geen rand of schaduw om het beeld; veilige zone 1235 x 338 op 2048, dus ±1544 x 423 op 2560 (gangbaar sjabloongetal 1546 x 423) | 0,4 MB (378 KB). Woordmerk, regels en spullen allemaal binnen 1546 x 423. Op computer, tablet, telefoon en tv: `proef-banner-overal.png` (groen = veilige zone/telefoon, blauw = tablet, rood = computer). |
| `watermerk-300.png` | 300 x 300 | vierkant, min 150 x 150, onder 1 MB | 13 KB. De kleine D (`merkteken-klein.svg`), die leest beter op klein formaat. Instelling: "End of video" (laatste 15 s), zodat hij niet door de tips heen staat. |

**De banner in woorden:** links het woordmerk Dortus; uit de deur-D valt warm licht naar rechts over de vloer, en daarin liggen accolades, een kroontje, een dobbelsteen en een geprinte arm met een kogelgewricht die omhoog buigt. Onder het woordmerk: **Blender tips for 3D printing**, met kleiner eronder *Focused tools today, small games on the way* (de goedgekeurde regel van het uniform; geen "we", geen spel als belofte van nu). Beide regels in Inter Medium (uniform). Geen tweede grote D naast het woordmerk (les uit Daans keuring 6 van de Steam-kop: twee keer dezelfde D).

## 5. Overige instellingen (Studio > Settings > Channel)
- **Land:** Nederland.
- **Trefwoorden van het kanaal:** `blender "3d printing" "blender tips" "3d print" "ball joint" "articulated" "blender add-on" "click joints" dortus` (de woorden die mensen intypen, GEZIEN in de YouTube-suggesties in `youtube-1.md`).
- **Standaard voor uploads (Upload defaults):** taal Engels; beschrijving eindigt met `Click Joints (free): https://extensions.blender.org/add-ons/click-joints/` alleen bij filmpjes waarin Click Joints in beeld is.
- **Niet "made for kids"** (dan vervalt het watermerk, DERDEN: helppagina 10456525; ook reacties gaan dan uit, GOK uit het hoofd).

## 6. TikTok @dortusstudio (zelfde gezicht)
Profielfoto: dezelfde `profielfoto-800.png`. Bio (max 80 tekens, GOK uit het hoofd), 73 tekens:
```
Blender tips for 3D printing. Free add-on Click Joints. Made by Thijs, NL
```
De AI-zin past niet in 80 tekens; daarom staat `AI agents write the code, I direct and test.` in elk onderschrift (`reeks.md`). Link in bio (als TikTok die toestaat; vaak pas vanaf 1.000 volgers, GOK): https://extensions.blender.org/add-ons/click-joints/

## Nog open vóór het live zetten
- Brams klopt op "Try" bij tip dag 1 (`reeks.md`): pas daarna klopt "Every tip is checked in Blender itself" helemaal.
- Watermerk: donker vierkant achter de D (mag volgens het uniform) of doorzichtig; Daan kiest.

## Voor de hoofdchat
Na Daans ja: profielfoto, banner, beschrijving, links en contact uit dit bestand in YouTube Studio zetten, en profielfoto en bio op TikTok @dortusstudio. Daan geeft zijn oordeel in `berichten/chris.md`.
