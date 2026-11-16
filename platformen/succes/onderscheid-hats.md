# Onderscheid van Hats of the Fallen (Fenna, 16 nov 2026)

Opdracht: hoofdchat, groeironde 16 nov 07:10 (`berichten/fenna.md`). Vraag: waar lijkt Hats op de spellen die er al zijn of eraan komen, waar zijn we echt anders, zie je dat binnen 2 seconden op de capsule en binnen 30 seconden in het spel, en wat is de haak die geen ander kan claimen.

**Kort antwoord, hard:** op het niveau van het idee lijkt Hats bijna volledig op **Don't Rob My Dungeon**. Hun eerste zin en de onze zeggen hetzelfde, hun capsule heeft dezelfde onderdelen (kerker, goudberg, ridder met helm, groen slijm, fakkels, paars), en de lus "helden komen je goud stelen, ze vallen in je vallen" is dezelfde. Wat ons echt onderscheidt zit in twee dingen die zij niet hebben: **de hoeden op Gloop** en **helden die terugkomen met een wrok**. Op dit moment zie je die twee niet binnen 2 seconden op de kleine capsule en niet binnen 30 seconden in een nieuw spel. Daar zit het werk.

## Bronnen en hoe ik keek (16 nov, 06:40 tot 07:20 UTC)
- Winkeltekst, prijs, datum, talen en AI-melding: `store.steampowered.com/api/appdetails?appids=<id>` en de winkelpagina zelf (`store.steampowered.com/app/<id>/`), met curl.
- Capsules: de header-plaatjes uit appdetails, naast elkaar op 460 x 215 en verkleind tot 120 px breed (de "2 seconden"-toets: wat blijft er over als het klein en vluchtig is). Hats: `ontwerp/steam/capsule-3d-daan/header-pluim-460.png` (stand 16 nov) en het blad dat Thijs goedkeurde (`ontwerp/steam/blad-3d/hol-3d-blad-voor-thijs-concept13.png`, besluit 15 nov 13:24).
- Trailers: de eerste 10 seconden van de officiële Steam-trailer, 1 beeld per 2 seconden (ffmpeg op de openbare HLS-stroom).
- Reviews: de 10 "meest behulpzame" positieve en negatieve Engelse reviews per uitgebracht spel, `steamcommunity.com/app/<id>/positivereviews/?browsefilter=toprated` en `.../negativereviews/...`. (De oude route `store.steampowered.com/appreviews` stuurt door naar de voorpagina; dat zag Vera ook.)
- Volgers: `steamcommunity.com/games/<id>/memberslistxml/?xml=1`; de rest van de volgers en reviewcijfers komt uit Vera's kaart `platformen/verkenner/steam-desktop-2026-11.md`.
- Hats: `ontwerp/steam/winkelpagina/teksten.md` (korte en lange beschrijving), `ontwerp/steam/winkelpagina/trailer.md`, `producten/steam-hol/ontwerp.md` en de toets in `producten/steam-hol/godot/systemen/toetsen/toets_systemen.gd` (eerste hoed in het echte spel).

## 1. Per spel: haak, wat spelers prijzen, waar ze over klagen

### Don't Rob My Dungeon (appid 5376930, Highlander Interactive, nog niet uit, demo 5378080)
- **Haak in één zin (winkeltekst, GEZIEN):** "A tiny dungeon lives at the bottom of your screen while you work. Heroes walk in to steal your gold: set traps, raise monsters, smash them with the Dark Hand and grow infamous. Even your Twitch chat can try to rob you."
- **Wat ze verder beloven (GEZIEN):** je bent Mordo, "a greedy little imp sitting on a mountain of gold"; vallen (spikes, pijlmuren, rollende keien, olie, valluiken), monsters (skeletten, geesten, vleermuizen, een mimic), kamers graven en upgraden, "infamous" worden zodat rijkere helden komen, de Dark Hand (klik een held en een klauw komt uit het plafond), streamermodus waarin kijkers met `!join` als held binnenlopen met hun eigen naam, voortgang als het spel dicht is, klikken gaan erdoorheen, onder 1% CPU, boven of onder op het scherm, lo-fi chiptune "quiet by default". 11 talen.
- **Capsule (GEZIEN):** pixelart, grote titel links, paarse imp met kroon op een goudberg in het midden, ridder met helm en blauw tabbaard, dief, skelet, **groen slijm** rechtsonder, fakkels, paarse kerkermuur. Druk en vol.
- **Trailer:** geen; alleen 8 schermen. Scherm 1 toont de strook op een bureaublad met wazige vensters erboven.
- **AI (GEZIEN, winkelpagina):** "The pixel art was created with the help of AI image tools, then cleaned up, animated and assembled by hand. Sound effects and music were made with AI audio tools".
- **Publiek:** 8 volgers (GEZIEN 16 nov, zelfde als Vera), demo-reviews: geen zichtbaar. Geen datum ("Coming soon").
- **Prijzen en klachten van spelers:** nog geen reviews, dus niet te zeggen.

### There is no HERO: Desktop Quest (5091650, Broad Street Indie Games, 2027)
- **Haak (GEZIEN):** "In this comedic desktop companion RPG, let the villagers worship your woolly savior, gather resources, build and defend your town". Het grapje: de helden zijn weg en het dorp denkt dat een schaap de redder is.
- **Capsule:** pixelart, donkere kerker, gouden schaapje in een lichtbundel, dorpelingen met hartjes en een "YES"-ballon, een taakbalk met klokje onderin. **Trailer 0 tot 10 s:** zwart, een schaapje dat oplicht, dan een zwevend eiland op een Windows-bureaublad.
- **Geen AI-melding.** 7 volgers (Vera). Geen reviews.
- Lijkt op Hats in: humor, verdedigen. Anders: je bent de redder van een dorp, het is een stadsbouwer, en het staat in een hoek, niet in een strook.

### Work From Dungeon (5478110, horisi, uit op 19 nov 2026)
- **Haak (GEZIEN):** "A tiny adventure moves into the corner of your desktop. Click the mage and her monsters fight and grow stronger while you work. Collect and breed 99 monsters".
- **Capsule:** pixelart, donkerpaars, titel, vijf monstertjes op een rij, heks met cursor. **Trailer 0 tot 10 s:** een saai werkvenster ("Weekly report") met het spelletje in de hoek en de onderschrift "A tiny adventure in the corner of your desk", dan "Your monsters fight on their own". Dat is de beste opening van de zes: in 2 seconden snap je "spel naast je werk".
- **AI (GEZIEN):** "Much of the pixel art, music, sound effects, code and in-game text was produced by programs written by the AI assistant". 4 volgers (Vera).
- Lijkt op Hats in: kerkernaam, monsters, idle naast werk. Anders: verzamelen en fokken, jij bent de held (de heks), geen strook.

### Deskrawl: Idle ARPG (4623570, First Day Games, 28 sep 2026, nu $4,89 in de aanbieding, 3.631 reviews, 68%)
- **Haak (GEZIEN):** "Grind mobs, farm loot and capture enemies to serve you. Deskrawl is an epic idle ARPG that plays at the bottom of your desktop." Reviewers zeggen het korter: "Diablo 2 for busy people" en "A very fun Diablo 2-style side-scrolling idle ARPG".
- **Capsule:** een rode demon met vuur, titel in Diablo-letters. Zegt "duister en episch", niet "taakbalk". **Trailer 0 tot 10 s:** buitlijst in een stadje, logo met datum, "A Horde of Monsters Is Closing in", wereldkaart. Het bureaublad zie je in de eerste 10 s niet.
- **Prijzen (10 positieve):** loot en builds als in Diablo, makkelijk te snappen, "fun to leave it running and come back to see your progress", single player.
- **Klachten (10 negatieve):** dropkansen in het eindspel bijna nul (5 van de 10), handel op de Steam-markt en betalen om te winnen (4), "feels cheap and poorly put together", "obviously made with AI" (1, het spel heeft geen AI-melding, dus dit is een verdenking van een speler, niet bewezen), builds te beperkt.
- Lijkt op Hats in: kerker in een strook onderaan. Anders: jij bent de held, buit en handel, toon is grimmig.

### Desktop Defender (3772810, Conradical Games, 4 nov 2025, $4,99, 1.788 reviews, 92%)
- **Haak (GEZIEN):** "An idle auto-battler that sits in the corner of your screen while you do other things."
- **Capsule:** alleen de titel in pixelletters op een donker schaakbord met vlekjes. Je ziet geen spel. **Trailer 0 tot 10 s:** een echt Windows-bureaublad met het spelletje klein in de hoek, dan in- en uitzoomen, dan het spelletje naast Steam en YouTube. Ook hier: in 2 seconden zie je "speelt naast je andere dingen".
- **Prijzen:** loopt mooi op de achtergrond, vaak updates, de grote getallen ("me play game for 278 hours me see very big number me happy"). Een speler noemt zichzelf verzamelaar: "I have the whole bottom of screen collection and I hope that steam makes a filter".
- **Klachten:** "not NEARLY idle enough", te veel micromanagen (2), herhaling en geen keuzes (3), na ±40 uur uit terwijl er een prestatie voor 100 uur is (2), te veel CPU (1), UI.
- Lijkt op Hats in: golven tegenhouden. Anders: geen kerker, geen figuren met een karakter, abstract.

### Desktop Survivors 98 (3339780, Brandon Hesslau, solo, 20 mei 2025, $4,99, 1.352 reviews, 94%)
- **Haak (GEZIEN):** "Your cursor becomes the hero" in een bullet-heaven over je bureaublad, in Windows 98-stijl.
- **Capsule:** een Windows 98-venster met de titel, een cursor, en een zwaard met googly eyes op de bekende groene heuvel. In 2 seconden snap je de grap. **Trailer 0 tot 10 s:** dezelfde heuvel, een geel briefje "Are you ready to survive?", dan "SURVIVE" en vijanden.
- **Prijzen:** de stijl en de grap ("Come for roguelike, stay for emotional support sword friend"), nostalgie, veel inhoud voor de prijs.
- **Klachten:** balans (4), flitsend licht ondanks de instelling (1), tekst te klein (1), crashes zonder opslaan (1).
- Lijkt op Hats in: humor met één grappig figuur. Anders: actief spel, geen idle, geen kerker.

## 2. Hats ernaast

**Hats in één alinea (uit `teksten.md` en het blad):** een kerker in 3D in een strook boven de taakbalk. Helden klimmen erin om goud te stelen, vallen in je vallen en worden opgegeten door Gloop, een groen slijm met één oog, die hun hoeden opzet; de hoedentoren groeit en de rest komt op een berg. Wie vlucht komt terug met een verband, een bijnaam en een wrok ("Bram is back for the Spike Pit"); een bard die ontsnapt zingt over je kerker. Kroniek, heldenboek, upgrades die je terug kunt draaien, stil, nooit straf als je weg bent, één prijs.

| | Don't Rob My Dungeon | Deskrawl | Desktop Defender | Survivors 98 | No HERO | Work From Dungeon | **Hats** |
|---|---|---|---|---|---|---|---|
| Jij bent | de kerker (imp op goud) | de held | een toren | de cursor | een schaap met dorp | een heks met monsters | **de kerker (Gloop op goud)** |
| Waar | strook onder of boven | strook onder | hoek | heel scherm | hoek | hoek | strook boven taakbalk |
| Lus | helden stelen, vallen, monsters | buit en builds | golven, upgrades | rondes overleven | bouwen en verdedigen | verzamelen en fokken | helden stelen, vallen, Gloop eet |
| Figuren met eigen verhaal | alleen Twitch-kijkers met hun naam | nee | nee | nee | dorpelingen | monsters | **elke held: naam, eigenaardigheid, wrok, bijnaam** |
| Verzamelen | nee | buit | buit | wapens | spullen | 99 monsters | **hoeden op een toren** |
| Stijl | pixel, AI-beeld | pixel/2D, grimmig | abstract | Win 98 | pixel | pixel, AI | **3D, zacht speelgoed, geen AI** |
| Geluid | lo-fi, stil bij start | ja | ja | ja | ? | ja (AI) | **helemaal stil** |
| Iets eigens | Dark Hand, Twitch | Steam-markt | | cursor als held | schaap | fokken | **hoeden, wrok, kroniek, bard** |

**Waar we op lijken (eerlijk):**
1. **Don't Rob My Dungeon, bijna alles van het idee.** Leg de eerste zinnen naast elkaar: zij "A tiny dungeon lives at the bottom of your screen while you work. Heroes walk in to steal your gold", wij "A tiny dungeon lives on top of your taskbar. Heroes climb in". Dat is bijna woord voor woord dezelfde zin. Beide: jij bent de kerker, een klein monsterachtig baasje op een goudberg, vallen kopen, kamers graven, upgraden, nooit focus stelen, zuinig. Ook hun capsule bevat een ridder met helm en een **groen slijm**. Wie beide pagina's kort na elkaar ziet, denkt "hetzelfde spel, andere tekenaar". Dat is de harde waarheid.
2. Deskrawl: kerker in een strook onderaan. Maar daar ben je de held, dus dat verschil is duidelijk.
3. Desktop Defender en No HERO: golven tegenhouden. Klein, want de vorm is anders.

**Waar we echt anders zijn:**
1. **Gloop draagt de hoeden van wie hij opat.** Niemand van de zes heeft iets wat erop lijkt (in de winkelteksten van de drie aangekondigde spellen komt "hat" of "hats" niet voor, GEZIEN). Het is een beeld dat je zonder uitleg snapt en dat in de tijd groeit.
2. **Helden die terugkomen met een wrok, een bijnaam en een verband**, plus de kroniek en de bard. Bij Don't Rob My Dungeon hebben alleen Twitch-kijkers een naam; gewone helden zijn "warriors, thieves, wizards and very brave peasants". Terugkeren met een wrok noemen ze nergens.
3. **3D, zonder AI.** Alle zes zijn 2D of abstract; twee van de drie die eraan komen melden AI-beeld (Don't Rob My Dungeon, Work From Dungeon). Of kopers "geen AI" belangrijk vinden is een GOK; wel staat bij Deskrawl een behulpzame negatieve review met "obviously made with AI" als klacht, en Duelist kreeg dezelfde klacht (`platformen/steam/idee.md`).
4. **Helemaal stil en nooit straf.** Kleiner verschil: Don't Rob My Dungeon is ook "quiet by default" en telt door als het spel dicht is.

**Zie je het anders-zijn binnen 2 seconden op de capsule? Deels.**
- Wat wel: de stijl. Naast vijf pixel- of abstracte capsules valt de zachte 3D-Gloop meteen op, en de toon is vrolijk in plaats van grimmig.
- Wat niet: de hoeden. Op 460 breed zie je de toren met helm en heksenhoed, maar verkleind tot 120 px breed is de toren een paars vlekje boven een groen vlekje (eigen toets, GEZIEN). Wat dan overblijft is "kerker, goud, ridder, groen slijm, fakkels": precies wat Don't Rob My Dungeon ook laat zien. De grap van de capsule (ridder schrikt omdat zijn helm op Gloop staat) vraagt een paar seconden kijken.
- Daan kwam vanochtend (±06:35 UTC, `ontwerp/steam/winkelpagina/vergelijk-kerkerspellen-klein.png`, `keuring-daan.md`) tot "onze herken je in 2 s: enige in 3D en warm oranje". Dat klopt voor de stijl, en ik ben het met hem eens dat ze niet verward worden. Mijn punt is een ander: je ziet in 2 s dat het een ander plaatje is, maar niet dat het een ander spel is. Het eigen stuk (de hoeden) leest klein nog niet.
- Desktop Survivors 98 en Work From Dungeon laten zien dat het kan: één beeld dat de grap in een oogopslag vertelt (zwaard met ogen op de Windows-heuvel; werkvenster met een spelletje erin).

**Zie je het binnen 30 seconden in het spel? Nee, nog niet.**
- In een nieuw spel valt de eerste held altijd en komt er goud binnen (ontwerp.md), maar de **eerste hoed op Gloop komt pas na 59 tot 62 seconden** (gemeten in het echte spel, 5 zaden, 15 nov, toelichting bij de toets in `toets_systemen.gd`). De eerste wrok vraagt een held die vlucht en later terugkomt; helden komen gemiddeld elke ±50 s, dus dat duurt minuten.
- Wat je in de eerste 30 seconden wel ziet (held loopt binnen, valt in de stekels, goud) is wat Don't Rob My Dungeon ook laat zien.
- De vaste demofilm op tak `schermen` heeft wrok en lied wel in de eerste minuut (`spelgevoel.md`), maar dat is een vaste opname voor de trailer, niet wat een koper in zijn eerste spel ziet.

## 3. Advies

**De haak van Hats in één zin (Engels, voor winkel en trailer):**
> **Every hero who falls into your dungeon leaves a hat on Gloop's head, and the ones who get away come back with a grudge.**

Geen van de zes kan dit claimen: de hoeden niet, en de terugkerende helden met wrok ook niet. Korte vorm voor de trailer en de capsule: **"He wears their hats."**

**Drie dingen om aan te scherpen:**

1. **Tekst: begin met de hoeden, niet met "a tiny dungeon".** Onze eerste zin is nu bijna die van Don't Rob My Dungeon. Voorstel korte beschrijving (±280 tekens, nalopen door Mila en Daan):
   > Gloop the slime lives in a tiny dungeon on top of your taskbar. Every hero who falls in gets eaten, and Gloop keeps their hat. The ones who flee come back with scars, nicknames and a grudge. Dig, upgrade and laugh between tasks. You're never punished for looking away.
   En de eerste kop van de lange beschrijving "Gloop wears the hats" bovenaan houden (staat er al). In de trailer: de tekst bij 3 tot 6 s ("A tiny dungeon on your taskbar.") is precies de zin van de concurrent; maak er "He wears their hats." of "Every hero leaves a hat." van, en zet "on your taskbar" in het beeld (de uitzoom naar het bureaublad doet dat al).
   Wie: Mila (eigenaar wow) met Sanne's tekst, Daan keurt. Klein werk.

2. **Beeld: de hoedentoren moet het grootste ding op de capsule zijn, ook op 120 px.** Nu deelt de toren de ruimte met de ridder, het goud, de muur en de titel. Voorstel: Gloop met een hoge, felle toren van 5 tot 6 hoeden die duidelijk verschillen van kleur en vorm (koksmuts wit, kroon goud, heksenhoed paars, emmer, pan), groter in beeld, minder goud en muur, en de ridder kleiner met een duidelijke reactie. Toets op 120 px breed en grijs: zie je "slijm met een stapel hoeden"? Dan hebben we het. Vermijd wat Don't Rob My Dungeon al heeft: paarse kerkermuur, goudberg als hoofdzaak, ridder vooraan. De warmere kleur H gaat al de goede kant op. Kijk ook naar de trailer-opening: Work From Dungeon en Desktop Defender beginnen met een echt werkvenster; onze trailer begint ingezoomd op de put, wat goed is voor de hoed, en zoomt daarna uit, wat goed is. Dat blijven.
   Wie: Mila (capsule, haar opstelling) en Daan (hero en logo), Olaf voor de trailer.

3. **Spel: de eerste hoed binnen 30 seconden, de eerste wrok binnen 5 minuten.** In een nieuw spel moet de eerste held niet alleen vallen maar ook door Gloop opgegeten worden, met de hoed op de toren, binnen ±30 s (nu 59 tot 62 s). En de tweede of derde held vlucht gegarandeerd en komt binnen de eerste 5 minuten terug met verband en bijnaam (alleen in het eerste spel zo vast, daarna gewoon de balans). Zo ziet elke koper, elke streamer en elke speler in de demo op Next Fest binnen een halve minuut wat alleen wij hebben. Dit raakt de balans en de toets ("hap onder 75 s"), dus het is een keuze voor Olaf en Bram; de richting (eerste minuut = het eigen stuk) zie ik als belangrijkste van de drie.
   Wie: Olaf (ritme in `kern/ritme.gd`), Bram (sim en toets).

**Wat we niet moeten doen:** de Dark Hand of een Twitch-modus nadoen. Dat is hun eigen stuk, en de streamermodus is bij hen nog niet bewezen (8 volgers). Wel nuttig om te onthouden: als streamers ons later oppakken, is "helden met een naam die terugkomen" juist iets waar kijkers op aanhaken; een Twitch-koppeling waarbij kijkers als held met wrok terugkomen zou dan van ons zijn. Dat is een GOK en iets voor na versie 1.

**Hoe erg is Don't Rob My Dungeon?** Voor het publiek niet (8 volgers, ±100 verlanglijsten volgens Vera, geen datum, geen trailer, AI-beeld). Voor het idee wel: de belofte "jij bent de kerker aan de rand van je scherm" is niet meer van ons alleen, en wie hen eerst ziet, ziet ons als tweede. Daarom moeten we niet verkopen wat we delen ("a tiny dungeon") maar wat alleen wij hebben (de hoeden en de wrok). Volgen: elke week hun volgers en of er een datum of trailer komt (staat al bij Vera, vanaf 1 dec).
