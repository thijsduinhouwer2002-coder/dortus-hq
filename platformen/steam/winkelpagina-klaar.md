# Winkelpagina Hats of the Fallen: wat er klaarstaat, vak voor vak (Olaf, 17 nov 2026 ±14:40 UTC, bijgewerkt ±15:25 UTC na de keuring van Daan)

Opdracht hoofdchat 17 nov 14:45 NL: zorg dat alles voor de winkelpagina klaarstaat. Dit is de ene lijst om bij het uploaden naast te leggen. Per vak in Steamworks: welk bestand, of de maat klopt, wie het keurde, wat er nog mist.

Maten opnieuw nagekeken in de Steamworks-docs met curl op 17 nov ±14:30 UTC (GEZIEN): `store/assets/standard`, `store/assets/libraryassets`, `store/assets/community`, `store/assets/eventassets`. Niets veranderd sinds 9 nov. Maten van onze bestanden met PIL gemeten (GEZIEN).

## Stand 17 nov ±15:25 UTC: de 3D-set is gekeurd en staat klaar
Daan keurde de hele set op 17 nov ±15:10 UTC en zette hem onder de Steam-namen in `ontwerp/steam/winkelpagina/` (overzicht met akkoord per vak: `winkelpagina/LEESMIJ-set.md`). De pixelversies van 10 nov staan nu in `winkelpagina/oud-pixel/`; daar niets uit uploaden. Het risico van eerder vandaag (oude pixelcapsules in de uploadmap) is daarmee weg.

**Blad voor de toets met Thijs (wo 18 nov 20:00):** `platformen/steam/winkelblad/blad-winkelset-17nov.png` (in mijn map, niet in de uploadmap van Daan, want daar horen alleen de uploadbestanden) (GEZIEN met Read, 2400 x 3688). Alles op ware grootte behalve de hero, met de kleine capsule ook op 184 x 69 en 120 x 45, het logo op ruitjes en de vijf schermen en twee iconen. Opnieuw maken: `python3 platformen/steam/winkelblad/maak_blad_set.py` vanuit de repo-root. Het oude blad `kandidaten-17nov/blad-kandidaten-17nov.png` is vervallen.

Maten van alle bestanden opnieuw gemeten met PIL op 17 nov ±15:20 UTC (GEZIEN): alles klopt met de eis van Steam.

## Winkel (Store Graphical Assets)
| Vak | Eis Steam | Bestand in `ontwerp/steam/winkelpagina/` | Maat GEZIEN | Keuring | Wat mist |
|---|---|---|---|---|---|
| Header capsule | 920 x 430 | `header-920x430.png` (ronde 9: 6b plus goudberg en grotere ridder die naar Gloop kijkt, Daan 17 nov 15:55) | 920 x 430 RGB | ja Daan 17 nov (ronde 9) | ja Thijs wo 20:00 |
| Small capsule | 462 x 174 (Steam maakt 184 x 69 en 120 x 45) | `klein-462x174.png` (toren ronde 6b) | 462 x 174 RGB | ja Daan 17 nov | ja Thijs; op 120 x 45 is de titel nog net leesbaar (blad) |
| Main capsule | 1232 x 706 | `main-1232x706.png` (toren ronde 8, goudberg onder Gloop) | 1232 x 706 RGB | ja Daan 17 nov | ja Thijs |
| Vertical capsule | 748 x 896 | `staand-748x896.png` (staand ronde 1, torenstijl) | 748 x 896 RGB | ja Daan 17 nov | ja Thijs |
| Schermafbeeldingen | min. 1920 x 1080, 16:9, alleen spelbeeld | zes uit `schermen-steam/`, volgorde in `schermen-steam/LEESMIJ.md` (22 nov: `bureaublad-pijl.png`, `1-hoedentoren.png`, `3-hap.png`, `4-val.png`, `naast-werk.png`, `5-kaartje.png`; `2-bureaublad.png` niet zelf) | alle zes 1920 x 1080 | ja Daan 16 nov (`keuring-daan.md`); plek 1 en 5 ja Iris 22 nov (`platformen/steam/keuring/2026-11-22-scherm1-en-5-nakeuring.md`) | spelteksten in beeld zijn CONCEPT tot Thijs ze schrijft; wijkt zijn tekst af, dan nieuwe snede uit een opname. Winnaars hebben er mediaan 8 (Sem, `marketing/winkeltekst.md`); 6 is genoeg om in te dienen |
| Page background | 1438 x 810, optioneel | geen | | | niet nodig: Steam maakt hem uit het laatste scherm |

## Bibliotheek (Library Assets)
| Vak | Eis Steam | Bestand | Maat GEZIEN | Keuring | Wat mist |
|---|---|---|---|---|---|
| Library capsule | 600 x 900 | `library-600x900.png` (bibliotheek ronde 8) | 600 x 900 RGB | ja Daan 17 nov | ja Thijs |
| Library header | 920 x 430 | zelfde bestand als de header capsule | 920 x 430 | volgt de header | niets extra |
| Library hero | 3840 x 1240, geen tekst, veilig vlak 860 x 380 in het midden | `hero-3840x1240.png` (kleur H) | 3840 x 1240 RGB | ja Daan 17 nov | ja Thijs |
| Library logo | 1280 breed en/of 720 hoog, doorzichtig | `logo-1082x720.png` | 1082 x 720 RGBA | ja Daan 17 nov | plaats in Steamworks: linksonder (Daan) |

## Iconen (Community and Client Icons)
| Vak | Eis Steam | Kandidaat nu | Maat GEZIEN | Wat mist |
|---|---|---|---|---|
| Shortcut icon | 256 x 256 of 512 x 512, ICO of PNG | `ontwerp/steam/icoon/icoon-tegel-256.png` (ook `-512`) | 256 x 256 RGBA | doorzichtig deel wordt zwart als Steam er het app icon van maakt; daarom het app icon apart uploaden |
| App icon | 184 x 184 JPG | `ontwerp/steam/icoon/steam-community-184.jpg` | 184 x 184 | toont pas goed na "Coming Soon" (docs) |

## Aankondigingen (Event Graphical Assets), nodig voor A1 op de paginadag ±8 dec
| Vak | Eis Steam | Kandidaat nu | Maat GEZIEN | Wat mist |
|---|---|---|---|---|
| Event cover | **verplicht**, 800 x 450 | `ontwerp/steam/winkelpagina/event-cover-800x450.png` (uitsnede hero en logo, Olaf) | 800 x 450 RGB | ja Daan 17 nov ("de grap leest ook op 400 breed") |
| Event header | aangeraden, 1920 x 622 | `ontwerp/steam/winkelpagina/event-header-1920x622.png` (hero met logo linksonder) | 1920 x 622 RGB | ja Daan 17 nov |

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
2. wo 18 nov 20:00: Thijs ziet de winkelbeelden op `platformen/steam/winkelblad/blad-winkelset-17nov.png`. De set staat al onder de Steam-namen (Daan 17 nov 15:10). Zegt Thijs nee op een beeld, dan gaat alleen dat beeld terug naar een ronde.
3. Na de speeltest (za 21 nov): trailer opnemen; eventueel extra schermen (winnaars hebben er 8).
4. wo 25 nov: Engelse teksten van Thijs binnen (of ma 30 nov, dan schuift alles 2 dagen).
5. do 26 nov: alles erin, "Mark As Ready For Review". Na ja van Valve drukt Thijs zelf op "Post as Coming Soon".
