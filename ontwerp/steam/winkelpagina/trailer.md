# Trailer Hats of the Fallen: draaiboek (Daan, 15 nov 2026)

Voor de winkelpagina van ma 30 nov (niet nodig voor wo 18 nov). Dit is het eerste wat mensen op de pagina zien: Steam zet de trailer vóór de schermen. Thijs (8 nov): stop meer tijd in films dan in plaatjes.

## Wat de beste doen (GEZIEN)
Rusty's Retirement, release trailer, 60 s, bekeken op 1 beeld per seconde (`rusty-trailer-1fps-blad.jpg`, uit de openbare Steam-API):
- **Begint ingezoomd**, het figuurtje groot (2 s), niet het hele bureaublad.
- Daarna 3 s het echte bureaublad met de strook onderaan: "zo zit het".
- Het grootste deel (±35 s) is **ingezoomd spel**: elke 2 tot 3 s een nieuwe handeling (zaaien, oogsten, bouwen, groeien).
- Eén tekstkaart: "SITS AT THE BOTTOM OF YOUR SCREEN!" over een **echt werkvenster** (een script, Trello, YouTube) met het spel eronder. De grap: je werkt, het spel leeft.
- Slot 6 s: logo groot, "OUT NOW", Steam-logo.
- Geen voice-over, vrolijke muziek, snelle maar rustige knippen.

Wat zij missen en wij hebben: **een verhaal per held**. Bij Rusty groeit er iets; bij ons komt iemand binnen, valt, en zijn hoed belandt op Gloop. Dat is een grap met een begin en een eind in 3 s, en die herhalen we met steeds een gekkere hoed. Daar bovenop: de wrok (wie vlucht, komt terug).

**In één zin:** waar Rusty laat zien dat er iets groeit, laten wij elke 3 s een kleine grap zien die eindigt met een hoed op het slijm.

## Draaiboek, 45 s, 1920x1080, 60 fps (opname uit het echte spel, niets bijgetekend)
| Tijd | Beeld | Tekst |
|---|---|---|
| 0 tot 3 s | **Haak.** Ingezoomd (4x) op de put: een ridder met pluimhelm loopt binnen, ziet de munt, stapt, valt (stof), de helm wipt op en draait door de lucht en landt op Gloops toren. Gloop knippert blij. | geen |
| 3 tot 6 s | Uitzoomen in één beweging naar het echte bureaublad (donkere achtergrond, Kladblok open): het hol is een dunne strook boven de taakbalk. | "A tiny dungeon on your taskbar." |
| 6 tot 18 s | Ingezoomd, vier grapjes van 3 s: heks valt (heksenhoed op de toren), kok (koksmuts), dief met masker die "picks the lock. It was open.", bard. Elke hoed komt bovenop; de toren groeit. | kaartjes uit het spel zelf |
| 18 tot 24 s | **Wrok.** Een held vlucht met een litteken, komt later terug met een bijnaam ("Fenna the Limp") en valt in dezelfde put. | "They come back. With a grudge." |
| 24 tot 30 s | Bouwen: graven, een nieuwe put kopen (kaartje Big Gloop, Buy), munten. | "Dig. Upgrade. Get fat." |
| 30 tot 36 s | Werkvenster groot (een echte saaie spreadsheet of mail), strook eronder; er valt iemand terwijl de cursor typt. Daarna de hoedentoren in Royal, groot. | "Work. Gloop does the rest." |
| 36 tot 39 s | Snelle montage van 6 hoeden die op de toren vallen (elk 0,5 s). | geen |
| 39 tot 45 s | Logo (onze `logo-3d-kleurh.png`) op de warme grot, Gloop knippert eronder. | "Wishlist now" |

Regels: eerlijk (alles uit een echte opname, `moment=` mag om een beeld stil te zetten, zoals in het spel), warm (kleur H, geen paars), elke knip op een handeling, nooit langer dan 3 s hetzelfde beeld. Tekst in de letter van de capsule (Lilita One), geel met donkere rand, linksboven, korter dan 6 woorden.

## Wat er nodig is
- **Olaf:** een opname met camera ingezoomd op een kolom (een `zoom=` of `kijk=<kolom>` in de demo-modus) op 60 fps; donkere bureaubladachtergrond (zie mijn wens van 15 nov in `platformen/steam/taken.md`).
- **Bram:** de montage met ffmpeg in Actions, zoals de film van Click Joints.
- **Daan:** ruwe animatic uit bestaande beelden (volgende stap), daarna keuren per versie; laat de projectchat hem zien vóór Thijs.
- Muziek: alleen vrij te gebruiken muziek met licentie, of geen; nooit iets zonder licentie.
