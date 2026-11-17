# Hats of the Fallen: alle tekst in het spel, voor Thijs (Sanne)

Status van alles hieronder: **CONCEPT** (regel Thijs 16 nov 21:05). Thijs schrijft het in eigen woorden; wat hij goed vindt zet hij op DEFINITIEF in `teksten-thijs.md`. Max 42 tekens per kroniekregel ná invullen, inclusief ` +12` bij goud, dus houd een regel liefst onder 34 tekens.

**Hoe te lezen:** `{naam}` is de voornaam van de held (Odo, Mara), `{held}` naam met bijnaam, `{bewoner}` is Gloop, `{val}` is "the Spike Pit". Volgorde: wat een speler het vaakst ziet bovenaan. De telling komt uit een echte duurtest van 75 minuten (run 44040279373, `platformen/steam/data/teksten/lijst_spel.py`).

**Waar Thijs het meest mee wint (Sanne):** de bovenste vier rijen zijn samen 176 van de 324 regels die een speler in 75 minuten leest. Een regel uit `val` of `vlucht` zie je om de 7 tot 8 minuten opnieuw; "stays forever" zelfs 20 keer, omdat hij in twee lijsten staat. Wie maar tien regels herschrijft: neem die tien.

## 1. Kroniek, nu in het spel (17 nov, demo-inhoudtak)

| soort | keer in 75 min | regels (CONCEPT), tussen haakjes hoe vaak gezien |
|---|---|---|
| val | 57 | `{naam} fell to {val}.` (9) / `{naam} found {val}. Hard.` (9) / `{naam} stays forever.` (20) / `{naam} left gold and one boot.` (9) / `{naam} will not be leaving.` (10) |
| vlucht | 50 | `{naam} fled. Grudge: {bewoner}.` (10) / `{naam} ran. Swore revenge.` (10) / `{naam} escaped with a limp.` (10) / `{naam} left. Took nothing. Angry.` (10) / `{naam} fled, crying a little.` (10) |
| binnen | 48 | `{naam} climbs into your hole.` (7) / `{naam} is here for your gold.` (7) / `{naam} brought a torch. And hope.` (7) / `{naam} read about you in a tavern.` (6) / `{naam} has a map. It is wrong.` (7) / `{naam} knocks first. Polite.` (7) / `{naam} says this is a quick one.` (7) |
| terug_bewoner | 21 | `{naam} is back for {bewoner}.` (11) / `{held} is back. Grudge: {bewoner}` (3) / `{naam} wrote a song about {bewoner}.` (7) |
| val_bewoner | 20 | `{bewoner} ate {naam}. Burp.` (10) / `{bewoner} says thanks for the snack.` (10) / `{naam} stays forever.` |
| binnen_dief | 19 | `{naam} the Thief tiptoes in.` (6) / `{naam} sneaks in. Nobody saw. You saw.` (7) / `{naam} picks the lock. It was open.` (6) |
| naamgenoot | 12 | `{naam} climbs in. Family business.` (4) / `{naam}. {oud} fell here once.` (4) / `{naam} wants dad's boot back.` (4) |
| binnen_magier | 10 | `{naam} the Wizard sniffs for traps.` (3) / `{naam} casts Light. It is a candle.` (4) / `{naam} knows every trap. Almost.` (3) |
| binnen_ridder | 10 | `Sir {naam} clanks in.` (4) / `Sir {naam} polished his armor for this.` (3) / `Sir {naam} is very slow. Very sure.` (3) |
| terug_val | 8 | `{naam} remembers {val}.` (4) / `{naam} is back for {val}.` / `{naam} limps back to {val}.` (4) |
| binnen_wraakzuchtig | 7 | `{naam} holds grudges. Hard.` (2) / `{naam} the Spiteful is here.` (2) / `{naam} keeps a list of names.` (3) |
| afgerekend | 5 | `Grudge settled. {naam} rests.` (2) / `{naam} came back once too often.` (3) |
| afgerekend_val | 5 | `{naam} came back. {Val} won.` (2) / `{Val} won. Grudge settled.` (2) / `{Val} wins round two.` (1) |
| binnen_bard | 5 | `{naam} the Bard tunes his lute.` (2) / `{naam} hums on the way in.` (2) / `{naam} is here for a story.` (1) |
| hap_hoed | 5 | `{bewoner} ate {naam}. Kept the {hoed}.` / `{bewoner} ate {naam}. The {hoed} fits.` (2) / `{bewoner} ate {naam}. Wears the {hoed} now.` (1) / `{naam} is gone. The {hoed} stays.` (1) / `{bewoner} ate {naam}, saved the {hoed}.` (1) |
| binnen_slaapkop | 3 | `{naam} yawns. Long walk.` (1) / `{naam} brought a pillow.` (1) / `{naam} the Sleepy shuffles in.` (1) |
| dutje | 3 | `{naam} took a nap in your hole.` (1) / `{naam} snored. Gloop watched.` (1) / `{naam} slept. Rude.` (1) |
| hoed | 3 | `{bewoner} tries on {naam}'s hat. Fits.` (1) / `{bewoner} adds {naam}'s hat to the pile.` (1) / `{bewoner}'s hat pile is taller than him.` (1) |
| binnen_opschepper | 2 | `{naam} tells everyone he slew a dragon.` (1) / `{naam} the Boastful struts in.` (1) / `{naam} signs autographs. Nobody asked.` |
| hap_hoed_eerste | 2 | `{bewoner} ate {naam}. Kept the {hoed}.` (2) |
| op | 2 | `{bewoner} is up again. Wobbly.` (2) |
| plat | 2 | `{bewoner} is flat. Back soon.` (2) |
| schat | 2 | `{naam} touched your hoard!` (1) / `{naam} tried to lift it. Too heavy.` / `{naam} licked a coin and ran.` (1) / `{naam} is now the Hoard-Toucher.` |
| schat_weg | 2 | `{naam} the Hoard-Toucher ran.` / `{naam} ran. Hands smell of gold.` (1) / `{naam} ran off, giggling.` (1) |
| aartsvijand | 1 | `Your nemesis {naam} has arrived.` (1) / `{naam} again. Of course.` / `{naam} trained all week for this.` |
| afgerekend_aarts | 1 | `Nemesis {naam}: finally stays.` (1) / `Grudge settled. {naam} rests.` |
| hoed_bijnaam | 1 | `{bewoner} is now known as the {bijnaam}.` (1) |
| afgerekend_bewoner | 0 | `{naam} came back. {bewoner} won.` / `Rematch. {bewoner} won. Burp.` / `{naam} had a plan. {bewoner} ate it.` |
| binnen_hebzuchtig | 0 | `{naam} the Greedy smells gold.` |
| binnen_lied | 0 | `{naam} heard the song. Came to see.` / `{naam} hums the song. Off-key.` / `{naam} knows all the words. Sadly.` / `{naam} came for the gold in the song.` / `{naam} asks if this is the song hole.` |
| binnen_schijterig | 0 | `{naam} the Timid peeks in.` |
| hoed_eerste | 0 | `{bewoner} wears {naam}'s hat now.` |
| hoed_klein | 0 | `{bewoner} tries on {naam}'s hat. Fits.` / `{bewoner} adds {naam}'s hat to the pile.` |
| lied | 0 | `{naam} sang about your hole. More came.` / `{naam}'s song got popular. Uh oh.` / `A song about you! Heroes on the way.` |
| naamgenoot_hoed | 0 | `{naam} wants dad's hat back.` / `{naam} glares at the hat pile.` / `{naam} can't find it. Too many hats.` |
| pensioen | 0 | `{naam} retired. Opened a bakery.` / `{naam} retired. Tells tall tales now.` / `{naam} quit heroing. Sells maps.` / `{naam} won't be back. Too scared.` |
| terug | 0 | `{held} is back.` / `{naam} came back. Bigger sword.` / `{naam} is back. Still limping.` |
| valt | 0 | `{naam} fell to {val}.` / `{naam} stays forever.` / `{naam} found {val}. Hard.` / `{bewoner} ate {naam}. Burp.` / `{naam} left gold and one boot.` / `{naam} will not be leaving.` / `{bewoner} says thanks for the snack.` |
| vlucht_zonder | 0 | `{naam} left. Took nothing. Angry.` / `{naam} ran. Swore revenge.` / `{naam} fled, crying a little.` |

324 kroniekregels gezien, 306 herkend, 39 soorten, 118 regels in de voorraad.

## 2. Nieuw voorstel: de vangst die terugslaat op de binnenkomst (CONCEPT, ontwerp in `features.md`)
Een held met een soort of trek krijgt bij zijn binnenkomst al een eigen regel ("Sir Odo is very slow. Very sure."). Nu hoort daar bij de vangst niets bij; dan komt weer "stays forever". Voorstel: bij de vangst een regel die terugslaat op wat hij bij binnenkomst zei. Dat is de grap die mensen doorvertellen (Iris keuring 19 en 20: nog geen lachregel).

| soort | binnenkomst nu | vangst, nieuw (CONCEPT) |
|---|---|---|
| val_ridder | `Sir {naam} is very slow. Very sure.` | `Sir {naam} was very sure. Was.` / `Sir {naam} clanked all the way down.` / `Sir {naam}'s armor stays. So does he.` |
| val_dief | `{naam} sneaks in. Nobody saw. You saw.` | `Nobody saw {naam} fall. You saw.` / `{naam} picked the wrong floor.` / `{naam} stole nothing. Got kept.` |
| val_magier | `{naam} knows every trap. Almost.` | `{naam} knew every trap but one.` / `Candle out. {naam} out.` / `{naam} sniffed the pit. Too late.` |
| val_bard | `{naam} the Bard tunes his lute.` | `{naam}'s last song was short.` / `{naam} hit a low note. Very low.` / `The ballad of {naam}: one verse.` |
| val_slaapkop | `{naam} brought a pillow.` | `{naam} gets a long nap now.` / `{naam} dozed off. Then fell off.` / `{naam} used the pillow. For good.` |
| val_wraakzuchtig | `{naam} keeps a list of names.` | `{naam}'s list got one name shorter.` / `Spite did not help {naam}.` / `{naam} holds a grudge. Down there.` |
| val_opschepper | `{naam} tells everyone he slew a dragon.` | `{naam} slew a dragon. Not this hole.` / `{naam}'s autograph: in the pit now.` / `{naam} will tell no one about this.` |

En `val` van 5 naar 8 regels, zonder dubbele met `val_bewoner` (CONCEPT, erbij): `{naam} took the short way down.` / `{naam} checked the floor. Too late.` / `{naam} is part of the hole now.`

## 3. Winkel: de zes dingen die je koopt (kaartje en kroniek)
Elke speler koopt ze; de naam en de uitleg staan op het kaartje, de kroniekregel komt bij de koop. Houd de naam op 12 tekens en de uitleg op 34 (het kaartje is smal). `{b}` is Gloop.

| ding | naam | uitleg op het kaartje | kroniek bij koop (één van drie) |
|---|---|---|---|
| slijm 1 | `Big Gloop` | `Bigger mouth. More heroes fall.` | `{b} is now Big {b}. Bigger mouth.` / `{b} grew. The hats fit better.` / `More {b}. Same appetite. Worse.` |
| slijm 2 | `Bouncy Gloop` | `Back up in 40 s instead of 60.` | `{b} bounces now. Back up in 40 s.` / `{b} learned to bounce. Smug.` / `Boing. {b} is Bouncy {b}.` |
| slijm 3 | `Royal Gloop` | `A royal cape. Heroes gulp.` | `{b} wears a royal cape now.` / `All hail Royal {b}. Burp.` / `{b} is royalty now. Insufferable.` |
| put 1 | `Rusty Spikes` | `Rust hurts. More heroes fall.` | `The Spike Pit got rusty. Ouch.` / `Rust on the spikes. On purpose.` / `The spikes are rusty now. Tetanus.` |
| put 2 | `Deep Pit` | `Timid heroes forget to turn back.` | `The pit got deeper. Echo, echo.` / `Deeper pit. Nobody turns back now.` / `The pit is very deep now. Hello?` |
| put 3 | `Trick Lid` | `Looks like floor until it isn't.` | `The pit has a lid. Looks like floor.` / `New floor. Not floor.` / `The Spike Pit hides now. Shh.` |

Kaartje en knoppen: `Buy  45` / `Undo` / `Remove` / `Bought.` / `All three bought.` / `Next: Big Gloop, 12 gold to go` / `The Spike Pit is filled in.`

## 4. Hol-niveaus: de naam van je hol (bordje en kroniek)
Bij elk nieuw niveau: `Hole level 4: a bad idea.` op het bordje, en `Level 4: a bad idea.` in de kroniek. Onder het bordje: `7 heroes to go.` en `Next: level 5, in 6 min`. Na weg zijn: `Grew 2 levels while you were away.`
Namen van niveau 1 tot 12 (de demo eindigt bij 12, dus deze ziet elke demospeler): `a damp hole` / `a local rumor` / `a known hazard` / `a bad idea` / `a tavern tale` / `a hat museum` / `a hero shortage` / `a no-go zone` / `a dare` / `a local legend` / `a royal problem` / `Gloop's Empire`. Sanne: dit is het rijtje met de meeste kans op een glimlach per woord; het mag gekker.

## 5. Start, weg geweest, demo-einde
| waar | concept |
|---|---|
| eerste regel van een nieuw spel | `Your hole is open. Heroes will come.` |
| terug na weg zijn (bovenaan het kaartje en in de kroniek) | `240 came, 179 fell, 107 hats. +1314 gold.` / daarna `7 more to come as you play.` / hover op het bordje `7 more to come. Next: a hat museum, in 2 min.` / niets gebeurd: `All quiet while you were away.` / aartsvijand kwam: `Nemesis Odo came by. Still free.` |
| demo voorbij (één keer) | `That's the demo. Your hole keeps going.` |
| elke start daarna | `Demo over. The full game keeps it all.` |
| kaartje na het demo-einde | `Full game: keep this hole.` |
| hoedenberg bij hover | ` 212 more in the pile.` |

## 6. Heldensoorten (Heldenboek, uitleg per soort)
`Knight`: `Heavy armor. Too big for Gloop. Pits love him.` / `Thief`: `Quick. Pits rarely catch him. Hates slime.` / `Wizard`: `Sees traps. No spell works on Gloop.` / `Bard`: `Weak. If he escapes, he sings about you.` Bijnamen die helden krijgen: `Thrice-Fled`, `Hatted`, `Milliner`.

## 7. Heldenboek (een bladzijde per soort, stempels, hoeden, aartsvijanden)
- **Titels van bladzijden:** soorten `the Hero` / `the Knight` / `the Thief` / `the Wizard` / `the Bard`; trekken `the Greedy` / `the Timid` / `the Sleepy` / `the Vengeful` / `the Braggart` / `the Lost`; aparte bladzijde `The Hat Pile`.
- **Stempels (wat een held kan doen):** `touched the hoard` / `turned back at a trap` / `was caught napping` / `fell to his own grudge` / `bragged, then ran` / `got lost`; en `The pit got him.` / `Spikes: one.` / `He got away.` / `Ran off. Counts.`
- **Op een bladzijde:** `Weak to: Spike Pit` / `First worn by Odo.` / `Grudge: Gloop.` / `Came 3 times.` / `Settled on day 4 by Gloop.`
- **Kroniek als het boek iets nieuws krijgt (één van):** `New page: the Knight. The pit got him.` / `Page for the Thief. He got away.` / `Booked: ...` / `New stamp: touched the hoard.` / `New stamp for the Bard. ...` / `New hat: Crown. Thanks, Odo.` / `Book: Odo's Crown. Kept.` / `New hat in the book: Crown.` / `The hat pile reached 25. Stamped.` / `New nemesis in the book: Odo.` / `Book: Odo, settled on day 4.` / `Day 4: Odo's grudge is filed.`
- **Hoeden (10):** `Helmet` / `Pointy hat` / `Hood` / `Cap` / `Crown` / `Chef's hat` / `Bucket` / `Top hat` / `Pan` / `Feather cap`.

## 8. Heldennamen en bijnamen
- **Voornamen (12):** Bram, Odo, Wout, Gerda, Pim, Rik, Mara, Joost, Fenna, Tibbe, Lotte, Kees. Sanne: een paar zijn namen uit onze eigen ploeg (Bram, Fenna, Kees, Joost). Leuk als knipoog, maar Thijs beslist of dat zo blijft. Wie terugkomt heet Tibbe II, Tibbe III.
- **Bijnamen na vluchten:** `the Once-Fled` / `the Twice-Fled` / `the Thrice-Fled` / `the 4-Times-Fled`; andere bijnamen: `Hatted`, `Milliner`, `Hoard-Toucher`, `Spooked`, `Lucky`.
- **Waarom een held wegging (in het boek en de log):** `touched your hoard, took nothing and ran` / `grabbed one coin, saw the hoard wake up and ran` / `saw the Spike Pit again and turned back` / `got hurt by the Spike Pit and ran`.

## 9. Nog te doen (Sanne)
Het rechtsklikmenu (tak `claude/steam-hol-menu`, nog niet op main): lees ik als het op main staat. Let op: `tel_tekst.py` slaat teksten over die met een getal beginnen (`%d came, ...`), dus de echte telling is iets hoger dan 404 teksten en 1647 woorden. Wat hier staat is alles wat een speler in de demo ziet, behalve het menu.
