# Hats of the Fallen: teksten voor de winkelpagina (Sanne)

**Versie 2, 10 nov 2026** (keuring 1 van Daan verwerkt: naam overal Hats of the Fallen, één verhaal over de hoogte, "No microtransactions" weg, punt 11; prijs volgt `platformen/steam/verdienmodel.md`). Eerste versie 9 nov 2026, 23:05 UTC. Opdracht Thijs 9 nov 23:45 NL: Sanne schrijft de teksten mee, Mila is eigenaar van de wow, Daan keurt, Olaf levert de beelden. De winkel is Engelstalig; de uitleg eromheen is Nederlands.

**Eerlijk-regel voor deze pagina:** elke zin beschrijft iets dat bij het uitbrengen in het spel zit. Zinnen met **[v1]** gaan over features uit versie 1 (`platformen/steam/features.md`) die nog niet gebouwd zijn. Zit zo'n feature er bij het indienen van de binnenkort-pagina (±1 december) nog niet in, dan blijft de zin staan alleen als Olaf bevestigt dat het bij het uitbrengen erin zit; anders gaat hij eruit. Niets over skins of DLC op de pagina tot ze bestaan.

## 1. Naam
**Definitief: Hats of the Fallen** (Daan en Mila, 9 nov 23:45 UTC, `taken.md`). Vaste ondertitel *a tiny dungeon on your taskbar*, alleen in tekst en trailer, niet op de capsules. Hieronder mijn eerdere afweging, ter archief.

### Eerdere afweging (9 nov)
"Het Hol" is een werknaam en zegt een Engelse koper niets. Gezocht in de winkel van Steam (GEZIEN, `store.steampowered.com/api/storesearch`, 9 nov):
| Naam | Op Steam | Waarom wel | Waarom niet |
|---|---|---|---|
| **Hat Hoard** (eerste keus) | geen treffer | kort, rijmt bijna, past op de kleinste capsule, en het noemt de haak: Gloop draagt de hoeden van wie hij opat, en de schat is je hoard | zegt niet meteen "taakbalk"; dat doet de ondertitel of het eerste schermbeeld |
| **Grudgehole** | geen treffer ("Grudge" heeft wel 6 spellen) | uniek, noemt ons eigen stuk (de wrok) | lastiger uit te spreken, klinkt grimmiger dan het spel is |
| Gloop's ... | "Gloop" is al minstens twee spellen (2096210 en 3279240), plus andere treffers (GEZIEN) | | verwarring |
| Hole Sweet Hole | lijkt op "SWEET HOLES" (4023170) | | verkeerde associatie |

Mijn advies was Hat Hoard; Daan koos Hats of the Fallen omdat Hat Hoard als verzamelspel klinkt en de grap mist. Akkoord.

## 2. Korte beschrijving (Steam-veld ±300 tekens, DERDEN/GOK: Valve noemt "a few hundred characters"; deze heeft 270)
> A tiny dungeon lives on top of your taskbar. Heroes climb in, fall into your traps and get eaten by Gloop, who wears their hats. The ones who flee come back with scars, nicknames and a grudge. Dig, upgrade and laugh between tasks. You're never punished for looking away.

Waarom zo: zin 1 zegt wat en waar (Desktop Companion, voor de fest-keuring), zin 2 is de haak die op de capsule en in de trailer staat (hoeden op Gloop), zin 3 is wat geen ander taakbalkspel heeft (de wrok), zin 4 belooft het eerlijke ritme. Valen, opgegeten worden, hoed op Gloop en terugkomen met wrok zitten in de film van main (toets 5); graven en "nooit straffen" zitten in de bouw. "Upgrade" is sinds 10 nov waar in de build (kaartje met Buy en Undo, drie stappen voor Gloop en voor de put, toets 8 en 9 in `spelgevoel.md`), dus geen **[v1]** meer. Sinds toets 10 (10 nov 05:00 UTC) wel in de lange beschrijving: het lied van de bard (luit in beeld, "Mara knows all the words. Sadly.") en "he grows" (Gloop wipt en wordt groter bij kopen). De namen van stap 2 en 3 nog niet, want die zag ik nog niet in een film. (Na controleur: "into" in plaats van "in", "upgrade" in plaats van "decorate".)

## 3. Lange beschrijving (Steam-opmaak: koppen als [h2], lijstjes als [list])

> [b]Your taskbar has a basement now.[/b]
>
> Hats of the Fallen is a tiny pixel dungeon that sits in a strip right above your taskbar while you work, study or watch something. Heroes keep climbing in to steal your gold. Most of them don't make it out.
>
> [h2]Gloop wears the hats[/h2]
> Gloop the Slime eats heroes and keeps their hats. A crown, a chef's hat, a bucket, a frying pan: they stack on his head, and when the stack gets too tall, the hats pile up next to him in a hoard of hats that keeps growing for weeks. Spend your gold on him and he grows.
>
> [h2]Heroes hold grudges[/h2]
> Every hero has a name and a quirk. The ones who flee come back with a bandage, a nickname and a grudge against whatever hurt them. "Bram is back for the Spike Pit." Bards are worse: one who escapes sings about your dungeon, and new heroes show up knowing all the words. Flee three times and he becomes your Archenemy. **[v1]** One day his son shows up and wants his father's hat back.
>
> [h2]Glance, smile, get back to work[/h2]
> [list]
> [*]Something happens about every minute: a fall, a burp, a hero who tries to lift your whole hoard and gives up.
> [*]A visit of 30 seconds is enough: read the chronicle, spend your gold on a new tunnel, go back to what you were doing.
> [*]Coming back after a night away? You get gold and three lines about who came by. Nothing broke, none of your monsters died, nothing was stolen.
> [/list]
>
> [h2]Small, quiet and fair[/h2]
> [list]
> [*]Sits right above the taskbar, 120 pixels tall (right-click to switch to 96 or 160). Clicks pass straight through the sky and the grass.
> [*]Light on your PC: it only draws when something moves, with an FPS setting.
> [*]Sound is off by default.
> [*]No daily rewards, no energy, no timers calling you back. Anything you build can be moved or removed for all its gold back.
> [*]The whole game for one price. No shop inside the game, no marketplace, nothing that makes you faster.
> [/list]

Te controleren voor het indienen (Olaf, Bram):
- Hoogte en klikken (10 nov 00:55 UTC): rechtsklik wisselt 96, 120, 160 en bewaart het (`HOOGTES` en `MOUSE_BUTTON_RIGHT` in `kern/strook.gd`), klikken gaan door lucht en gras (`window_set_mouse_passthrough`), op main volgens Olaf, controleur akkoord. Zin aangepast naar wat de build doet. Klopt.
- "about every minute": held elke 40 tot 60 s (strook.gd), klopt nu.
- "three lines about who came by": `kern/strook.gd` roept `VOORTGANG.verhaal` al aan (controleur, GEZIEN). Klopt.
- "FPS setting", "Sound is off by default", "full refund": eisen in `features.md`; de fps-instelling en al het goud terug bij verplaatsen of weghalen moeten in de bouw (nu nog niet GEZIEN).
- "A crown, a chef's hat, a bucket, a frying pan": zitten in Mila's 10 hoeden en in de code (Bram 22:40). Klopt.
- "hats pile up next to him ... for weeks": hoedenberg in zes maten, 3000 hoeden na ±110 u open tijd (Bram, sim). Klopt.
- Archenemy na drie keer vluchten: `kroniek.gd`. De zoon **[v1]**.

## 4. Tags (Valve raadt tot 20 aan, alleen de bovenste 20 zijn te zien en filters kijken naar de eerste 15, DERDEN: partner.steamgames.com/doc/store/tags)
Alle namen bestaan in de taglijst van Steam (GEZIEN, `store.steampowered.com/tagdata/populartags/english`, 429 tags):
1. **Desktop Companion** (verplicht voor het fest, zie `fest.md`)
2. Idler
3. Pixel Graphics
4. Funny
5. Casual
6. Management
7. Cute
8. Relaxing
9. Villain Protagonist (jij bent de kerker)
10. Comedy
11. Building
12. Incremental
13. Fantasy
14. 2D
15. Singleplayer
16. Cozy
17. Simulation
18. Base Building (je graaft en breidt je hol uit)
19. Indie
20. Cartoony (bestaat, GEZIEN; Mila mag hem schrappen als hij niet bij de stijl past)

Niet Side Scroller: het beeld schuift niet.

Bewust niet: Tower Defense (helden lopen door vallen, maar je bouwt geen torens en stuurt niets tijdens het lopen; dat zou kopers misleiden), Dungeon Crawler (jij crawlt niet), Strategy (te licht), Dark Humor (het is eerder slapstick dan grimmig).

## 5. Prijs (voorstel, versie 2)
**$4,99 / € 4,99**, eerste week 10% korting, plus een permanente gratis demo. Uitgewerkt in `platformen/steam/verdienmodel.md` (controleur akkoord): betaald levert in alle drie de schattingen 3,5 tot 11 keer meer op dan gratis zonder drops; $4,99 is de mediaan van de betaalde Desktop Companion-apps (GEZIEN door Kees) en een kleine stap na de demo. Thijs neigt naar gratis en beslist; kiest hij gratis, dan geldt hoofdstuk 4 van `verdienmodel.md` en verandert alleen deze regel en de zin "The whole game for one price" (wordt "Free. The whole game, no shop inside it, nothing that makes you faster."). Versie 1 van dit voorstel was $5,99.

## 6. Plan voor skins en DLC (alleen uiterlijk en inhoud, nooit sneller of sterker)
Basisregel: wie niets extra koopt, kan het heldenboek, de wand en de hoedenberg 100% vol krijgen. DLC krijgt eigen bladzijden.
| Wat | Soort | Prijs (GOK) | Wanneer (GOK) | Waarom |
|---|---|---|---|---|
| **Supporter Pack**: Gloop in goud, een eigen hoed voor Gloop, achtergrond-wallpapers | uiterlijk | $2,99 | bij het uitbrengen (verkocht in de Steam-winkel, niet in het spel; daarom klopt "No shop inside the game") | alle toppers hebben er een; laat fans iets geven zonder iets te verkopen wat het spel nodig heeft |
| **Holthema's**: ijsgrot, vulkaan, spookslot, snoepgrot | skin (hol, gras, fakkels, schat) | $2,99 per stuk of $7,99 alle vier | eerste 6 tot 8 weken na uitbrengen, daarna elke 2 maanden | grootste skin; zelfde spel, ander hol. Tiny Pasture verkoopt al een thema-DLC voor $2,39 (Olaf, `idee.md`, GEZIEN) |
| **Heldengilden**: piraten, ridders van de ronde tafel, toeristen met camera's | inhoud (nieuwe helden, trekken, hoeden, regels voor de kroniek) | $3,99 per gilde | vanaf ±4 maanden na uitbrengen | meer verhalen en hoeden voor de toren; niet sterker |
| **Seizoenshelden**: kerstman, Halloween | inhoud | gratis update | in het seizoen | goede reden voor een update-bericht op Steam; komen vaker in hun seizoen maar zijn het hele jaar te halen |
| Hoedjes en kleuren voor bewoners | skin | in Supporter Pack of thema's | | |

Bewust niet: geen ruilmarkt of Steam-ruilitems (Deskrawl: 26 van 78 negatieve reviews, GEZIEN, `features.md`), geen tijdelijke dingen die nooit terugkomen, geen loot boxes, geen betaalde versnelling.

## 7. Wat nog moet (wie)
- Naam definitief (Hats of the Fallen); logo: Mila, Daan keurt.
- Capsules, schermen en trailer: Mila en Olaf. Voor de trailer van 30 tot 60 s stel ik voor (haak in de eerste 3 s): 0 tot 3 s Gloop met een hoedentoren van drie hoeden en de tekst *He keeps the hats.*; 3 tot 10 s de strook boven een gewone taakbalk met een open document erboven (dit is een bureaubladspel); 10 tot 35 s één held met een wrok in drie bezoeken (vlucht, pleister, terug, opgegeten, hoed op Gloop); 35 tot 45 s de hoedenberg in zijn maten; 45 tot 55 s "Never punished for looking away" boven de kroniek na een nacht weg; einde naam Hats of the Fallen en "Wishlist now". Overal: de strook ligt boven (above/on) de taakbalk, nooit "under". Alles uit het echte spel (Olaf).
- Teksten keuren: Daan (en Chris als hij aan staat). Engels nalezen op natuurlijk Engels: controleur.

## Nagekeken
Controleur 9 nov ±23:10 UTC: akkoord na verbeteren. Verwerkt: tags tot 20 met de regel van Valve, tekenlimiet als DERDEN/GOK, "fall into", "upgrade" in plaats van "decorate", "all its gold back" in plaats van "refund", Steam-opmaak [b] en [list], labels bij alle cijfers, Gloop-treffers bijgewerkt, controlepunt kroniek na een nacht weg afgevinkt.
