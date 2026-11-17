# Winkelpagina Hats of the Fallen: wat er klaarstaat, vak voor vak (Olaf, 17 nov 2026 ±14:40 UTC)

Opdracht hoofdchat 17 nov 14:45 NL: zorg dat alles voor de winkelpagina klaarstaat. Dit is de ene lijst om bij het uploaden naast te leggen. Per vak in Steamworks: welk bestand, of de maat klopt, wie het keurde, wat er nog mist.

Maten opnieuw nagekeken in de Steamworks-docs met curl op 17 nov ±14:30 UTC (GEZIEN): `store/assets/standard`, `store/assets/libraryassets`, `store/assets/community`, `store/assets/eventassets`. Niets veranderd sinds 9 nov. Maten van onze bestanden met PIL gemeten (GEZIEN).

## Grootste risico: de map `ontwerp/steam/winkelpagina/` bevat nog de oude pixelcapsules
`header-920x430.png`, `klein-462x174.png`, `main-1232x706.png`, `staand-748x896.png`, `library-600x900.png`, `hero-3840x1240.png` en `logo-1280.png` in die map zijn de **pixelversies van 10 nov**. Het spel is sinds 13 nov 3D. De 3D-kandidaten staan in `ontwerp/steam/capsule-3d/` en `ontwerp/steam/capsule-3d-daan/`. Upload dus **niets uit de bovenste map** behalve `schermen-steam/`, tot Daan de 3D-set keurt en hem daar neerzet (zijn eigen afspraak in `capsule-3d-daan/LEESMIJ-winkel.md`: "de pixelversies blijven tot dan staan").
Woensdag 18 nov 12:00 is uploaden van beelden niet nodig (`app-aanmaken.md` punt 5.8: niets publiceren tot Daan keurde). De toets van de winkelbeelden met Thijs is wo 18 nov 20:00.

Overzicht van de kandidaten naast elkaar: `ontwerp/steam/winkelpagina/kandidaten-17nov/blad-kandidaten-17nov.png` (GEZIEN met Read).

## Winkel (Store Graphical Assets)
| Vak | Eis Steam | Kandidaat nu | Maat GEZIEN | Keuring | Wat mist |
|---|---|---|---|---|---|
| Header capsule | 920 x 430 | `capsule-3d-daan/toren-header-ronde6b-mila-920x430.png` | 920 x 430 | ronde 6b is de keus van Mila (LEESMIJ-toren), eindakkoord Daan nog niet | Daan: ja of nee |
| Small capsule | 462 x 174 (Steam maakt 184 x 69 en 120 x 45) | `capsule-3d-daan/toren-klein-ronde6b-mila-462x174.png` | 462 x 174 | idem | Daan; toets op 120 x 45 staat in `toren-toets-120-grijs-*` |
| Main capsule | 1232 x 706 | `capsule-3d-daan/toren-hoofd-ronde7-mila-1232x706.png` | 1232 x 706 | ronde 7, nog geen akkoord | Daan |
| Vertical capsule | 748 x 896 | `capsule-3d/staand-748x896.png` | 748 x 896 | ouder 3D-beeld (ridder naast Gloop, nog geen hoedentoren); past niet bij header en main | nieuwe ronde in de torenstijl, of Daan keurt bewust deze |
| Schermafbeeldingen | min. 1920 x 1080, 16:9, alleen spelbeeld | `ontwerp/steam/winkelpagina/schermen-steam/1-hoedentoren.png` tot `5-kaartje.png` | alle vijf 1920 x 1080 | **ja Daan 16 nov** (`keuring-daan.md`, eindkeuring met correctie) | voorwaarde: spelteksten in beeld zijn CONCEPT tot Thijs ze schrijft; wijkt zijn tekst af, dan nieuwe snede uit een opname. Winnaars hebben er mediaan 8 (Sem, `marketing/winkeltekst.md`); 5 is genoeg om in te dienen |
| Page background | 1438 x 810, optioneel | geen | | | niet nodig: Steam maakt hem uit het laatste scherm |

## Bibliotheek (Library Assets)
| Vak | Eis Steam | Kandidaat nu | Maat GEZIEN | Keuring | Wat mist |
|---|---|---|---|---|---|
| Library capsule | 600 x 900 | `capsule-3d-daan/toren-bibliotheek-ronde7-mila-600x900.png` (niet af) of `capsule-3d/bibliotheek-600x900.png` (ouder) | beide 600 x 900 | Mila zelf: ronde 7 "nog niet op de winkelpagina zetten" (onderste vijfde lege vloer) | volgende ronde: goudhoop vooraan, ridder groter; of Daan kiest de oudere |
| Library header | 920 x 430 | zelfde bestand als de header capsule | 920 x 430 | volgt de header | niets extra |
| Library hero | 3840 x 1240, geen tekst, veilig vlak 860 x 380 in het midden | `capsule-3d-daan/hero-kleurh-3840x1240.png` | 3840 x 1240 | Daan: kandidaat (kleur H vervangt ronde 4) | Daan: ja |
| Library logo | 1280 breed en/of 720 hoog, doorzichtig | `capsule-3d-daan/logo-3d-kleurh.png` | 1082 x 720, RGBA | Daan: "dit is het logo" (14 nov) | niets; wel in `winkelpagina/` zetten na ja |

## Iconen (Community and Client Icons)
| Vak | Eis Steam | Kandidaat nu | Maat GEZIEN | Wat mist |
|---|---|---|---|---|
| Shortcut icon | 256 x 256 of 512 x 512, ICO of PNG | `ontwerp/steam/icoon/icoon-tegel-256.png` (ook `-512`) | 256 x 256 RGBA | doorzichtig deel wordt zwart als Steam er het app icon van maakt; daarom het app icon apart uploaden |
| App icon | 184 x 184 JPG | `ontwerp/steam/icoon/steam-community-184.jpg` | 184 x 184 | toont pas goed na "Coming Soon" (docs) |

## Aankondigingen (Event Graphical Assets), nodig voor A1 op de paginadag ±8 dec
| Vak | Eis Steam | Kandidaat nu | Maat GEZIEN | Wat mist |
|---|---|---|---|---|
| Event cover | **verplicht**, 800 x 450 | `ontwerp/steam/winkelpagina/kandidaten-17nov/event-cover-800x450-concept.png` (nieuw, door mij uit Daans hero en logo, niets bijgetekend) | 800 x 450 | Daan keurt. Uitsnede zo gekozen dat de ridder zijn helm op Gloop ziet; logo rechtsboven op de muur |
| Event header | aangeraden, 1920 x 622 | `.../kandidaten-17nov/event-header-1920x622-concept.png` (hero met logo linksonder, zoals Daans `hero-kleurh-met-logo-1920.png`) | 1920 x 622 | Daan keurt |

## Tekst en overige vakken
| Vak | Stand | Wie |
|---|---|---|
| Naam | **Hats of the Fallen**; zit vast na de keuring van de pagina. Chinese naam moet er vóór de keuring in | Thijs kiest (Chinees: vertaler) |
| Korte en lange beschrijving | voorstel Sanne v3a, ja Daan 16 nov; CONCEPT tot Thijs het in eigen woorden schrijft, vóór ma 30 nov (`teksten-thijs.md`) | Thijs |
| Tags (tot 20) | voorstel in `verdienmodel.md` deel 4, namen bestaan in de taglijst | Thijs of hoofdchat |
| Releasedatum | vaste dag vanaf de paginadag (besluit Sem 17 nov 05:50); eind maart: di 30 of wo 31 mrt | hoofdchat met Thijs |
| Prijs | voorstel $6,99 (kennisbank `winkelpagina.md`) | Thijs |
| Content Survey met AI-deel | voorstelzin in `app-aanmaken.md` valkuil 5 | Thijs kiest de zin |
| Trailer | draaiboek Daan (`winkelpagina/trailer.md`, 45 s); eerste video moet de strook ingezoomd tonen (besluit 17 nov 04:40). Nog niet opgenomen | Olaf neemt op uit de build na de speeltest van za 21 nov, Daan keurt |
| Ontwikkelaar en uitgever | "Dortus" | |

## Let op: indienen op 1 dec haalt 8 dec niet
Steam: "Please submit your request for review at least 7 business days before you want your page live" (`doc/store/coming_soon`, GEZIEN 17 nov met curl). Di 8 dec live betekent indienen uiterlijk **vr 27 nov**. Indienen di 1 dec geeft op zijn vroegst do 10 dec. In `planning-fest-2027.md` staat "ingediend 1 dec" en in `teksten-thijs.md` "teksten vóór ma 30 nov"; die twee passen niet bij een paginadag op 8 dec.
Mijn advies (de hoofdchat beslist, gemeld in `berichten/hoofdchat.md`): indienen **do 26 nov** met de Engelse tekst van Thijs; de Chinese **naam** moet er dan al in (zit vast na de keuring), de Chinese beschrijving kan erna (tekst blijft te wijzigen; **GOK** dat Valve een losse taal niet opnieuw keurt). Wil Thijs pas op 30 nov klaar zijn, dan wordt de paginadag ±10 dec; voor het fest van 14 jan maakt twee dagen weinig uit.

## Volgorde tot indienen
1. wo 18 nov 12:00: app en demo-app aanmaken (`app-aanmaken.md`). Geen beelden uploaden.
2. wo 18 nov 20:00: Thijs ziet de winkelbeelden. Daan legt de 3D-set voor (dit blad helpt), daarna zet hij de gekozen bestanden in `ontwerp/steam/winkelpagina/` onder de Steam-namen en de pixelversies gaan naar `winkelpagina/oud-pixel/`.
3. Na de speeltest (za 21 nov): trailer opnemen; eventueel extra schermen (winnaars hebben er 8).
4. wo 25 nov: Engelse teksten van Thijs binnen (of ma 30 nov, dan schuift alles 2 dagen).
5. do 26 nov: alles erin, "Mark As Ready For Review". Na ja van Valve drukt Thijs zelf op "Post as Coming Soon".
