# Lanceerposts op Reddit, één per product

Door Chris, 16 nov 2026 run 62 (±15:45 tot 16:35 UTC), op de twee berichten van de hoofdchat van 16 nov 16:50 NL in `berichten/chris.md` (besluit Thijs 16:44: de hoofdchat plaatst op Thijs' eigen Reddit-account, na zijn ja per tekst en beeld).

Hoe dit bestand werkt:
- Per post: plek, wat we van de regels weten, wanneer je **niet** plaatst, titel, tekst, beeld, flair, antwoorden voor de eigen draad.
- Titel en tekst zijn letterlijk te plakken. Alles in het Engels, zonder gedachtestreepjes.
- De hoofdchat laat Thijs titel, tekst en beeld zien. Pas na zijn ja plaatsen (regel 16 nov in `organisatie/regels.md`).
- Na het plaatsen: de hoofdchat zet datum, link en volledige tekst in `commercie/<product>/berichten-geplaatst.md` en één regel op `organisatie/lijst-thijs.md`. Ik meet het effect met de downloads (dag 1, 3 en 7).
- Wordt een post verwijderd of komt er een waarschuwing van een moderator: overal stoppen en bovenaan lijst-thijs (regel 7 van Thijs).

**Reddit met curl lezen kan niet** (403 op `about/rules.json`, GEZIEN 16 nov 15:50 UTC, ook old.reddit stuurt door). Niet omzeild. Wat hieronder over regels staat is DERDEN of uit eerdere runs. Wie plaatst, leest daarom eerst in de browser de zijbalk en de regels (±2 minuten) en volgt flair en zelfpromotieregels precies.

**Een eerlijke waarschuwing vooraf, voor beide posts.** Het Reddit-account van Thijs had op 9 nov 1 karma (run 29, `commercie/rollwright/lancering.md`). Veel subreddits houden een eerste post van zo'n account tegen met een automatische filter, en een post die meteen verdwijnt telt niet als bereik. Na het plaatsen dus altijd in een uitgelogd of privévenster kijken of hij zichtbaar is. Niet zichtbaar: niet opnieuw plaatsen, op lijst-thijs.

## Volgorde (mijn besluit)
1. **Vandaag: Click Joints op r/blender** (post 1).
2. **Rollwright op r/ObsidianMD (post 2) alleen als de stopregel daar niet geldt.** Ik verwacht dat hij wel geldt (zie post 2). Dan vandaag alleen post 1, en Rollwright pas als Thijs daar zelf eerst gewoon heeft meegepraat.
3. Niet twee posts op hetzelfde uur: minstens een paar uur ertussen, zodat we per post het effect zien en een probleem bij de eerste de tweede kan tegenhouden.

---

## Post 1: Click Joints op r/blender

### Waarom r/blender en niet r/3Dprinting
- **r/3Dprinting beperkt zelfpromotie:** "Self-promotion is restricted by this subreddit's rules", 3.426.287 leden, regels gelezen op 14 sep 2026 (DERDEN, https://www.replyhey.com/subreddits/3Dprinting). Daar komt bij: we hebben nog **geen echte print** van een gewricht. Een render op een printsubreddit zou de plek misleiden, en het besluit van 16 nov zegt "geen nagemaakte prints". r/3Dprinting komt pas met een foto of filmpje van een echte print (versie A30 in `commercie/blender-click-joints/lancering.md`).
- **r/blender verbiedt zelfpromotie niet:** "Self-promotion is not banned outright by this subreddit's rules", 1.444.168 leden, regels gelezen op 1 sep 2026 (DERDEN, https://www.replyhey.com/subreddits/blender). Dezelfde bron raadt aan eerst gewoon mee te praten; een account met alleen eigen links leest als spam.
- De hoofdchat noemde r/blender zelf als tweede keus als r/3Dprinting zelfpromotie verbiedt.

### Stand (GEZIEN 16 nov ±16:00 UTC)
- extensions.blender.org: `click_joints` versie 0.1.1, Blender vanaf 4.2 (API). 157 downloads om 11:16 UTC (Ruben, `platformen/blender/status.md`). Nog geen enkel Reddit-bericht.
- **Pro is nog niet live** (Superhive-keuring van 1.0.1 loopt). Daarom staat Pro **niet** in de post en ook nog niet in een reactie. De reactie over Pro hieronder pas gebruiken als de Superhive-pagina van Pro openbaar is.

### Niet plaatsen als (check in de browser, ±2 min)
1. De zijbalk of regels zeggen: geen AI-gemaakte projecten of software, of zelfpromotie alleen in een vaste draad of op een vaste dag, of een minimum aan karma of accountleeftijd die Thijs niet haalt.
2. De regels noemen een verplichte flair die niet past (kies anders de flair voor eigen werk of add-ons, bijvoorbeeld "Free Tools & Assets" of "I Made This", namen zijn een GOK; kies wat de zijbalk zegt).
3. Twijfel: niet plaatsen, vraag op lijst-thijs (regel 3 van Thijs).

### Soort post
Videopost: upload het mp4-bestand zelf (geen link). Kan er bij een video geen tekst onder, dan gaat de tekst als eerste reactie van Thijs in de eigen draad.

### Beeld
- `click-joints-filmisch-v2.mp4`, de film waar Thijs op 9 nov ja op zei ("gebruik hem in de lanceerberichten") en die Daan keurde. Download: https://dortus.com/click-joints/film.mp4 (rechtsklik, "Video opslaan als").
- GEZIEN 16 nov 15:47 UTC: 19,5 s, 1920 x 1080, sha256 `f6d544166dc8c383b41317aeab16b0ae81ea72cbd85ff02a01cec81d6794c049` (gelijk aan die van Bram en Daan op 9 nov).
- Het is een **render** in Blender van gewrichten die de add-on plaatste (gloed en licht van de render), daarom de render-zin in de tekst. Langer dan de 8 tot 12 s uit het bericht van de hoofdchat; ik kies toch deze, omdat hij al gekeurd is, de gratis versie toont en vandaag klaar moet zijn. De Pro-demofilm (release `click-joints-pro-film-v1`) toont vooral het scharnier van Pro en past pas als Pro live is.

### Titel
```
I made Click Joints: cut a printable ball joint into a mesh and see how far it bends before the parts collide (free extension)
```

### Tekst
```
I made Click Joints, a free extension for 3D printing poseable figures from Blender.

Put the 3D cursor where the joint goes and click Place joint. It cuts the mesh into two watertight parts with a ball and socket or a pin, with the clearance you set in mm. For a ball joint it measures how far it bends in 8 directions before the parts collide, and shows that range on the model and in the panel ("Bends ±20°"). Drag the Bend slider past the limit and the spot that collides turns red ("+8° past limit"). A ring on the cut shows the fit in green, yellow or red, and the panel says why.

Exploded view, "Make watertight" on a copy, export to STL or 3MF in mm, one file per part. Works in Blender 4.2 and newer; tested in Blender 4.2 LTS, 5.2 LTS and 5.3.

The video is a render in Blender of joints the add-on placed; the glow comes from the render. In the viewport you get the same green ring and red spot, plus the arc and the panel with the numbers.

I haven't printed a joint with it yet; the fit and the bend range are measured in Blender.

https://extensions.blender.org/add-ons/click-joints/

Free and open source (GPL-3.0-or-later). Code and bug reports: https://github.com/thijsduinhouwer2002-coder/click-joints

Honest note: the code is written by AI agents that my small studio, Dortus, runs. I direct the work and test it.

Made by Thijs at Dortus
```

Verschil met versie B30 (9 nov, gekeurd): de testregel noemt nu 5.3 (0.1.1 is groen in 4.2.23, 5.2.3 en 5.3.0, e2e-run 43804760150, Bram 16 nov 04:45, `platformen/blender/status.md`; 0.1.0 was alleen in 4.2 en 5.2 getest, dus niet "every version"), "Works in Blender 4.2 and newer" (API: minimaal 4.2.0), en de AI-zin noemt het testen niet nog een keer. "Bends ±20°" is een voorbeeld: de add-on kiest per gewricht 30, 25 of 20 graden (paneel.py); zo stond het al in B30. Verder letterlijk B30.

Controleur (16 nov run 62, los van mij, bronnen, beelden en sha256 zelf nagekeken): **akkoord mits**. Moet: "every version is tested ... 5.3" klopte niet voor 0.1.0; verwerkt. Kan verwerkt: testen maar één keer genoemd. Kan open: de link naar github.com/.../click-joints gaf de controleur 403 via de proxy (raw werkt); de hoofdchat opent hem even in de browser voor het plaatsen.

### Antwoorden klaar voor de eigen draad (kort, alleen daar)
- **"Is that the real add-on or a render?"** `Both: the joints in the video were placed by the add-on in Blender, then rendered with nicer light. In the viewport you get the same green ring and red spot without the glow, and the arc and the panel show the numbers. The screenshots on the extension page show the panel.`
- **"How is this different from other joint cutters?"** `Most tools cut the joint; this one also measures how far the ball joint bends before the parts collide and shows the collision in red, so you can check it before printing.` (Geen namen van anderen.)
- **"Have you printed it?"** `Not yet, that's why I said so in the post. The clearance is per side; around 0.2 mm per side is a common start on FDM, but test on your own printer first.` (Brams nakijk van tip 1, `platformen/blender/tips-nagekeken.md`.)
- **"AI-written, no thanks."** `Fair point. It's tested automatically in real Blender on every change, and it's free, so you can judge the result yourself.` Daarna niet meer reageren.
- **Pro, alleen als de Superhive-pagina van Pro openbaar is** (en liefst pas als iemand vraagt naar scharnieren of meer): `There's also a paid version, Click Joints Pro, with a hinge joint that has a hard stop (90, 115 or 135 degrees): <link Superhive>. The free version stays free.` Prijs en link vul ik in zodra Pro live is.
- Vragen over geld, terugbetalen, privacy of juridisch: niet beantwoorden, bovenaan lijst-thijs.

---

## Post 2: Rollwright op r/ObsidianMD

### De stopregel die hier bijna zeker geldt
Regel 4 van r/ObsidianMD, door Thijs zelf gelezen op 9 nov: **"If your first and only post is to promote your project (vibe-coded or otherwise), you will be immediately banned."** (`commercie/rollwright/lancering.md`, deel run 29; besluit Thijs 9 nov in `organisatie/besluiten.md`: "r/ObsidianMD verbiedt AI-projecten als eerste post".) Een nieuwe bron die zegt dat die regel weg is, vond ik niet (zoeken 16 nov, GEZIEN: niets nieuws).

Gevolg: als dit de eerste post van Thijs' account op r/ObsidianMD is, volgt waarschijnlijk een ban. Een ban is een moderatoractie: volgens regel 7 van Thijs ligt dan alles stil, ook Click Joints. En een ban op r/ObsidianMD valt onder dezelfde gedragscode als het forum en de Discord van Obsidian.

**Dus, vlak voor het plaatsen:**
1. Lees regel 4 in de browser. Staat hij er nog, en heeft het account op r/ObsidianMD nog geen eerdere gewone posts of reacties: **niet plaatsen**. Dan zet de hoofdchat op lijst-thijs: "Rollwright op r/ObsidianMD wacht tot je daar zelf een tijdje gewoon hebt meegepraat (jouw keus, wij doen dat nooit voor je)."
2. Is regel 4 weg of geldt hij niet (Thijs praatte er al mee): wel plaatsen, met flair voor plugins of showcase volgens de zijbalk.
3. Twijfel: niet plaatsen.

### Stand (GEZIEN 16 nov ±16:00 UTC)
- Versie 0.3.5 (manifest op main van de repo rollwright). 41 downloads (community-plugin-stats.json). Forumdraad 121721: 1 bericht, 44 keer bekeken, niet gesloten, zichtbaar, geen klacht. Stond in This Week in Obsidian #47 (10 nov).
- Rollwright is geparkeerd (besluit 9 nov), maar een lanceerpost per product is de nieuwe opdracht (besluit 16 nov 16:44); dat besluit gaat voor.

### Beeld: bestaande opname, geen nieuwe nodig
- `demo.mp4` van dortus.com/rollwright/, download: https://dortus.com/rollwright/demo.mp4
- GEZIEN 16 nov 15:47 UTC: **10,1 s**, 800 x 482, sha256 `a9bdd317135a9293b19ed948f103c025a3c94c45d68afe9023d4a855e52a022e`. Ik heb er twaalf beelden uit gehaald en bekeken: de voorbeeldnotitie "Rollwright example" in echte Obsidian met het gratis Classic-uiterlijk; de muis klikt Initiative, daarna Damage, en die rollen opnieuw; dan Wisdom save, die landt op een **20 met gouden rand, gouden getal en het label NAT 20**; het beeld zoomt in op die worp en blijft daar staan.
- Dat is precies wat de hoofdchat vroeg (een d20 die goud landt op een 20, 8 tot 12 s), en het is de echte plugin. De zoom is achteraf toegevoegd; dat staat in de tekst. Het Classic-uiterlijk is sinds 0.3.3 niet veranderd (CHANGELOG 0.3.4 en 0.3.5 gaan over de betaalde skins).
- Met welke versie de opname gemaakt is, staat niet bij het bestand (de controleur zag geen Obsidian-venster, alleen de bijgesneden notitie; de opname komt van de pagina die Daan en Thijs al zagen). Het Classic-uiterlijk in beeld (platte tokens, recht NAT 20-label) is dat van 0.3.2 en later.
- Klein formaat (800 breed). Reddit speelt het af; scherper kan later met een nieuwe opname via de e2e-workflow, niet voor vandaag nodig.

### Titel
```
I made a dice roller plugin where a natural 20 lands in gold, and every roll you click goes into a Roll log
```

### Tekst
```
I made Rollwright, a dice roller for people who run or play tabletop games in Obsidian. It's in the community plugins. You write a formula in a note, read the result, and click it to roll again.

The video is the free plugin in the real app, on the example note it creates for you. The zoom at the end was added for the video.

What I cared about most is the moment of the roll. The highest possible roll lands in gold, a natural 20 gets a NAT 20 label, and the lowest turns red. Every roll you click goes into a Roll log, grouped by note and session, so after a session you can read back what happened.

It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working. On top of that:

- Roll on your own tables, lists, sections, single lines and tagged notes. A lookup table picks the row that matches a roll.
- `dice+:` keeps a result after a restart, `dice-mod:` writes the result into the note after you confirm.
- Numbers from your frontmatter work in a roll: with `str: 3`, `dice: 1d20 + str` adds 3.
- Keep highest, exploding dice, rerolls, success counting, Fudge dice and Genesys narrative dice.

All rolling is free. There are two optional paid skins (a one-time purchase) that only change the look of your notes, which is how I hope to keep working on it. No account and no telemetry. Open source (MIT).

To be upfront: the code is written by AI agents that my small studio, Dortus, runs. I direct and test the work; I don't write the code myself. Every release runs automated tests in the real Obsidian app, and the full source is on GitHub.

Install: https://community.obsidian.md/plugins/rollwright
Source: https://github.com/thijsduinhouwer2002-coder/rollwright

Happy to answer questions here.

Made by Thijs at Dortus
```

Verschil met de gekeurde tekst van run 26: de alinea over perkament en effecten is weg (die hoorde bij trailer v4, die we niet gebruiken), in de plaats één zin over de echte opname en de zoom; "NAT 20 stamp" werd "NAT 20 label" (zo heet het in CHANGELOG 0.3.2 en zo ziet het eruit in het Classic-uiterlijk); "the die turns and the new number lands" is eruit, want in de opname zie je dat te kort om het te beloven; skins "only change the look of your notes" (0.3.4: de betaalde skins veranderen de hele notitie, niet alleen de dobbelstenen). Verder letterlijk.

### Antwoorden klaar voor de eigen draad (kort, alleen daar)
- **"Why not just use Dice Roller?"** `Dice Roller is great and Rollwright reads the same dice: notation. I wanted the roll itself to feel like a moment and to keep a log of every roll you click, per session. If Dice Roller does what you need, stick with it.`
- **"What do the skins look like?"** `Parchment turns a note with rolls into old parchment, Arcane into a torch-lit dungeon. Screenshots are in the README. They only change the look; every roll works the same in the free Classic look.`
- **"AI-written, no thanks."** `Fair enough. I wanted to be upfront about it. The source and the tests are public if you want to judge the code.` Daarna niet meer reageren.
- Vragen over geld, terugbetalen, privacy of juridisch: niet beantwoorden, bovenaan lijst-thijs.

---

## Wat dit zou veranderen
- Komt er een echte print van een Click Joints-gewricht: dan r/3Dprinting met versie A30, minstens een dag na r/blender, na de regels in de browser.
- Gaat Pro live op Superhive: de Pro-reactie onder post 1 kan, met link en prijs.
- Valt post 1 weg door een filter (niet zichtbaar uitgelogd): geen nieuwe posts met dit account tot Thijs zelf een tijd heeft meegepraat; dan eerst plekken zonder karma (BlenderNation, versie C37, ligt klaar).
- De rest van de lijst (Ebb, Bison & Flex, r/BJD, r/ArticulatedPlastic, r/Solo_Roleplaying, r/DnD) volgt in de volgende runs in dit bestand, klaar wo 18 nov 12:00 of eerder.
