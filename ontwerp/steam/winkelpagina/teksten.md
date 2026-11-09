# Het Hol: teksten voor de winkelpagina (Sanne)

Eerste versie 9 nov 2026, 23:05 UTC. Opdracht Thijs 9 nov 23:45 NL: Sanne schrijft de teksten mee, Mila is eigenaar van de wow, Daan keurt, Olaf levert de beelden. De winkel is Engelstalig; de uitleg eromheen is Nederlands.

**Eerlijk-regel voor deze pagina:** elke zin beschrijft iets dat bij het uitbrengen in het spel zit. Zinnen met **[v1]** gaan over features uit versie 1 (`platformen/steam/features.md`) die nog niet gebouwd zijn. Zit zo'n feature er bij het indienen van de binnenkort-pagina (±1 december) nog niet in, dan blijft de zin staan alleen als Olaf bevestigt dat het bij het uitbrengen erin zit; anders gaat hij eruit. Niets over skins of DLC op de pagina tot ze bestaan.

## 1. Naam (voorstel, Mila en Daan beslissen samen met het logo)
"Het Hol" is een werknaam en zegt een Engelse koper niets. Gezocht in de winkel van Steam (GEZIEN, `store.steampowered.com/api/storesearch`, 9 nov):
| Naam | Op Steam | Waarom wel | Waarom niet |
|---|---|---|---|
| **Hat Hoard** (eerste keus) | geen treffer | kort, rijmt bijna, past op de kleinste capsule, en het noemt de haak: Gloop draagt de hoeden van wie hij opat, en de schat is je hoard | zegt niet meteen "taakbalk"; dat doet de ondertitel of het eerste schermbeeld |
| **Grudgehole** | geen treffer ("Grudge" heeft wel 6 spellen) | uniek, noemt ons eigen stuk (de wrok) | lastiger uit te spreken, klinkt grimmiger dan het spel is |
| Gloop's ... | "Gloop" is al een spel (2096210) en 4 anderen | | verwarring |
| Hole Sweet Hole | lijkt op "SWEET HOLES" (4023170) | | verkeerde associatie |

Advies: **Hat Hoard**, met als vaste regel eronder op de capsule en in de trailer: *a tiny dungeon on your taskbar*.

## 2. Korte beschrijving (max 300 tekens; deze heeft 262)
> A tiny dungeon lives on top of your taskbar. Heroes climb in, fall in your traps and get eaten by Gloop, who wears their hats. The ones who flee come back with scars, nicknames and a grudge. Dig, decorate and laugh between tasks. Never punished for looking away.

Waarom zo: zin 1 zegt wat en waar (Desktop Companion, voor de fest-keuring), zin 2 is de haak die op de capsule en in de trailer staat (hoeden op Gloop), zin 3 is wat geen ander taakbalkspel heeft (de wrok), zin 4 belooft het eerlijke ritme. Alle vier zitten nu al in de film van main (toets 5), behalve "decorate" **[v1]**: dat zijn de upgrades van feature 5. Gaat dat niet mee, dan wordt het "Dig, watch and laugh between tasks."

## 3. Lange beschrijving (Steam-opmaak: koppen als [h2], lijstjes als [list])

> **Your taskbar has a basement now.**
>
> Hat Hoard is a tiny pixel dungeon that sits in a 120-pixel strip above your taskbar while you work, study or watch something. Heroes keep climbing in to steal your gold. Most of them don't make it out.
>
> [h2]Gloop wears the hats[/h2]
> Gloop the Slime eats heroes and keeps their hats. A crown, a chef's hat, a bucket, a frying pan: they stack on his head, and when the stack gets too tall, the hats pile up next to him in a hoard of hats that keeps growing for weeks.
>
> [h2]Heroes hold grudges[/h2]
> Every hero has a name and a quirk. The ones who flee come back with a bandage, a nickname and a grudge against whatever hurt them. "Bram is back for the Spike Pit." Flee three times and he becomes your Archenemy. **[v1]** One day his son shows up and wants his father's hat back.
>
> [h2]Glance, smile, get back to work[/h2]
> - Something happens about every minute: a fall, a burp, a hero who tries to lift your whole hoard and gives up.
> - A visit of 30 seconds is enough: read the chronicle, spend your gold on a new tunnel, go back to what you were doing.
> - Coming back after a night away? You get gold and three lines about who came by. Nothing broke, nobody died, nothing was stolen.
>
> [h2]Small, quiet and fair[/h2]
> - Sits above the taskbar, 96 to 160 pixels tall. Clicks pass straight through the empty sky.
> - Light on your PC: it only draws when something moves, with an FPS setting.
> - Sound is off by default.
> - No daily rewards, no energy, no timers calling you back. Every choice can be undone for a full refund.
> - One price, the whole game. No microtransactions, no marketplace, nothing that makes you faster.

Te controleren voor het indienen (Olaf, Bram):
- "about every minute": held elke 40 tot 60 s (strook.gd), klopt nu.
- "three lines about who came by": `Voortgang.verhaal` van Bram, aangesloten in strook.gd? Nog nagaan.
- "FPS setting", "Sound is off by default", "full refund": eisen in `features.md`; de fps-instelling en het terugbetalen bij dichtgooien moeten in de bouw (nu nog niet GEZIEN).
- "A crown, a chef's hat, a bucket, a frying pan": zitten in Mila's 10 hoeden en in de code (Bram 22:40). Klopt.
- "hats pile up next to him ... for weeks": hoedenberg in zes maten, 3000 hoeden na ±110 u open tijd (Bram, sim). Klopt.
- Archenemy na drie keer vluchten: `kroniek.gd`. De zoon **[v1]**.

## 4. Tags (Steam laat er 20 toe; de eerste tellen het zwaarst)
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

Bewust niet: Tower Defense (helden lopen door vallen, maar je bouwt geen torens en stuurt niets tijdens het lopen; dat zou kopers misleiden), Dungeon Crawler (jij crawlt niet), Strategy (te licht), Dark Humor (het is eerder slapstick dan grimmig).

## 5. Prijs (voorstel)
**$5,99 / € 5,99**, eerste week 10% korting.
Waarom, met de prijzen van nu (GEZIEN, `store.steampowered.com/api/appdetails`, cc=us, 9 nov): Rusty's Retirement $6,99, Deskrawl $6,99, Tiny Pasture $5,99, Ropuka's Idle Island $3,99, Virtual Cottage 2 $7,99. Mediaan van de betaalde Desktop Companion-apps: $4,99 (GEZIEN door Kees, `platformen/steam/status.md`). Wij zitten in de bovenste helft omdat we meer verhaal hebben dan een tuintje, en de koers van 8 nov zegt hoger prijzen; niet boven Rusty's, want die heeft 97% positief van 6.625 reviews en wij nog nul. Gaat versie 1 met de ±40 uur inhoud uit `features.md` mee, dan kan $6,99; dat beslissen we bij het indienen van de prijs (Thijs, in Steamworks).

## 6. Plan voor skins en DLC (alleen uiterlijk en inhoud, nooit sneller of sterker)
Basisregel: wie niets extra koopt, kan het heldenboek, de wand en de hoedenberg 100% vol krijgen. DLC krijgt eigen bladzijden.
| Wat | Soort | Prijs (GOK) | Wanneer (GOK) | Waarom |
|---|---|---|---|---|
| **Supporter Pack**: Gloop in goud, een eigen hoed voor Gloop, achtergrond-wallpapers | uiterlijk | $2,99 | bij het uitbrengen | alle toppers hebben er een; laat fans iets geven zonder iets te verkopen wat het spel nodig heeft |
| **Holthema's**: ijsgrot, vulkaan, spookslot, snoepgrot | skin (hol, gras, fakkels, schat) | $2,99 per stuk of $7,99 alle vier | eerste 6 tot 8 weken na uitbrengen, daarna elke 2 maanden | grootste skin; zelfde spel, ander hol. Tiny Pasture verkoopt al een thema-DLC voor $2,39 (Olaf, `idee.md`, GEZIEN) |
| **Heldengilden**: piraten, ridders van de ronde tafel, toeristen met camera's | inhoud (nieuwe helden, trekken, hoeden, regels voor de kroniek) | $3,99 per gilde | vanaf ±4 maanden na uitbrengen | meer verhalen en hoeden voor de toren; niet sterker |
| **Seizoenshelden**: kerstman, Halloween | inhoud | gratis update | in het seizoen | goede reden voor een update-bericht op Steam; komen vaker in hun seizoen maar zijn het hele jaar te halen |
| Hoedjes en kleuren voor bewoners | skin | in Supporter Pack of thema's | | |

Bewust niet: geen ruilmarkt of Steam-ruilitems (Deskrawl: 26 van 78 negatieve reviews), geen tijdelijke dingen die nooit terugkomen, geen loot boxes, geen betaalde versnelling.

## 7. Wat nog moet (wie)
- Naam en logo definitief: Mila en Daan (voorstel hierboven).
- Capsules, schermen en trailer: Mila en Olaf. Voor de trailer van 30 tot 60 s stel ik voor (haak in de eerste 3 s): 0 tot 3 s Gloop met een hoedentoren van drie hoeden en de tekst *He keeps the hats.*; 3 tot 10 s de strook boven een gewone taakbalk met een open document erboven (dit is een bureaubladspel); 10 tot 35 s één held met een wrok in drie bezoeken (vlucht, pleister, terug, opgegeten, hoed op Gloop); 35 tot 45 s de hoedenberg in zijn maten; 45 tot 55 s "Never punished for looking away" boven de kroniek na een nacht weg; einde naam en "Wishlist now". Alles uit het echte spel (Olaf).
- Teksten keuren: Daan (en Chris als hij aan staat). Engels nalezen op natuurlijk Engels: controleur.
