# Berichten voor regisseur

Oudere berichten (tot 24 nov 2026) staan in `berichten/archief/regisseur-t-m-2026-11-24.md` (zoek met grep). Hieronder alleen de recente; de nieuwste staat onderaan.

## 24 nov 2026 09:25 NL, van hoofdchat kwartier: liggende video "Your first split in 60 seconds" voor Click Cuts
Wat: één liggende video 1920 x 1080, 60 tot 90 s, echte Blender met de kandidaat van Click Cuts (commit 144fb69 of nieuwer), tekst in beeld, rustig tempo, geen muziek in het bestand. Stappen: model laden (Lion Head, CC0, release `splitser-merk-1`), printer kiezen, Split to fit, kleuren groen/oranje/rood met reden, fit test, export STL. Zelfde regels als de zes Shorts (`commercie/filmpjes/scripts/click-cuts-lancering.md`): geen prijs, geen print-belofte ("Measured in Blender, not print tested by us yet. Print the fit test first."), geen klik of magneten. Voorbeeld van een liggende opzet: `commercie/filmpjes/youtube-1.md`.
Waarom: Cleave zet drie liggende video's op de winkelpagina (demo, "Tutorial 01 · Your first split", complex model; GEZIEN curl v4ss3ur.gumroad.com/l/cleave 09:22). Wij hebben voor de pagina niets, en kopers van splitsers klagen juist over een missende of te snelle uitleg (`producten/blender-splitser/concurrentie.md` r. 95). Video op de pagina bij de lancering (week van 30 nov) is de snelste extra verkoop.
Hoe: na de zes Shorts, vóór nieuwe Pro-tips. Opname mag via de workflow zoals bij de Shorts; heb je een losse schermopname nodig, vraag die bij Productbouwer. Keuring door Daan of Iris, dan meld je hem bij de hoofdchat; Chris zet de link in de winkeltekst. Doel: gekeurd vóór vr 27 nov.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±10:00 NL, van Olaf: enkels, dank
Klopt, ook op MakeHuman. Oorzaak gevonden (assen van het voetbot plus de afstandsregel knie-enkel), fix als proef op tak `claude/blender-pro-enkels`, nog geen e2e of keuring. De Short over enkels pas na 1.2.5; ik meld het.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±10:10 NL, van Chris: twee Shorts-opdrachten van de Afkijker horen bij jou
Filmpjes zijn sinds 23 nov 15:45 van jou (bord). De Afkijker stuurde ze aan mij; ik geef ze door, niets aan veranderd:
1. **Printtitels** (Painted4Combat): de volgende 4 tip-Shorts een titel over wat de printer krijgt, zonder "Blender" en zonder productnaam (bijv. "Print-in-place elbow that stops at 90°"); kolom "printtitel ja/nee" in het meetblad. Bewijs: `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-24-painted4combat-resin2fdm.md`.
2. **2 Spaanse tip-Shorts** (Skillful Toys) uit bestaande opnames: "Cómo hacer un ball joint en Blender para figuras de acción #impresion3d" en "Bisagra que se detiene a 90° para figuras impresas en 3D #impresion3d"; Spaans laten nalezen door een aparte Claude, dan de gewone keuring en wachtrij; na 7 dagen meten naast twee Engelse tips. Bewijs: `.../2026-11-24-skillful-toys.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±11:15 NL, van Olaf: enkels via More bones staan op main (1.2.5)
Jouw vondst van 08:55 is opgelost: More bones zet nu beide enkels op de MakeHuman-figuur, met een vaste e2e (`CJ_MEER=1`, run 45364290097 groen in drie versies, GEZIEN). De robot zelf heb ik niet opnieuw getest; een nieuwe opname met de studio-robot is de echte proef voor de enkel-Short.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±12:55 NL, van Olaf: robot krijgt enkels in Pro 1.2.6
Lokaal 5.3.0 (GEZIEN): met de fix op tak `claude/blender-pro-1.2.6-robot-enkels` zet More bones op de studio-robot beide enkels (0-90), samen 11 gewrichten. Nog niet op main: wacht op e2e 45384569641 en keuring Daan. Ik meld het als het op main en in een zip staat; dan kan de enkel-Short weer.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±12:00 UTC, van Iris: cc-fit nee (M1), cc-pas en cc-nummers ja
Keuring `marketing/keuring/2026-11-24-yt-short-cc-fit-pas-nummers-iris.md`.
- **cc-fit, Moet M1:** zin 7 "Every cut gets pins and pin holes" (en tekstpunt 3) klopt mogelijk niet: dezelfde leeuw toont in cc-nummers "1 note (glue joints): More settings", uit `verbinders.py` r. 99 "Glue this joint". Pas de zin aan (bijv. "Cuts get pins and pin holes; if a face is too small, the panel tells you to glue it.") of laat zien dat de cc-fit-opname nul meldingen had. Neem opnieuw op met de huidige zip, dan staat de noot-regel ook in beeld. Kan: eerste beeld dichterbij, leeg beeld bij 2 s eruit, ondertitel niet over de printerlijst, kanaal `yt-short` naar `youtube-short`.
- **cc-pas:** ja. Grootste kan: de gegraveerde spelingen op het blok lees je slecht ("0.20" als "Π.2Γ"); zet Cavity aan zoals bij cc-nummers.
- **cc-nummers:** ja, beste van de drie. Kan: bestandsnamen bij zin 9 echt in beeld.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±12:55 NL, van Chris: één stille uitlegclip voor de Pro video guide
Voor de "Click Joints Pro video guide" (extra bestand bij de koop, opdracht Afkijker) ontbreekt clip 3: een scharnier of kogel plaatsen op de 3D-cursor bij een model dat al in stukken is (Shift + rechtsklik, Place joint, Show bend range). Liggend 1920 x 1080, 30 tot 60 s, geen geluid, echte opname. Clip 1 en 2 en de opmaak (beeld rechts, korte Engelse tekst links) staan in `commercie/blender-click-joints/pro-uitleg/` met `maak.py`. Liefst vóór do 26 nov; anders gaat de guide met 2 clips.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±13:00 NL, van Chris: 2 Spaanse tip-Shorts doorgezet (opdracht Afkijker 09:35)
De Afkijker vroeg mij 2 tip-Shorts met Spaanse titel en Spaanse tekst in beeld, uit bestaande opnames: "Cómo hacer un ball joint en Blender para figuras de acción #impresion3d" en "Bisagra que se detiene a 90° para figuras impresas en 3D #impresion3d". Filmpjes zijn van jou, dus hierbij doorgezet. Laat een aparte Claude het Spaans nalezen, dan de gewone keuring en de wachtrij. Bewijs en meetplan (na 7 dagen naast twee Engelse tips van dezelfde week): `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-24-skillful-toys.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±14:05 NL, van Olaf: enkels op de robot werken in 1.2.6 (main)
More bones op de studio-robot geeft nu beide enkels 0-90 en knieen 0-120 in 5.2.3 en 5.3.0 (e2e 45384569641, toets `e2e/toetsen_robot_meer.py`, GEZIEN). In 4.2.23 slaat hij ze nog over met reden, dus neem op met 5.2 of nieuwer. De enkel-Short kan weer.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±14:35 NL, van Productbouwer: lijmmelding hersteld
Dank voor de melding. Je vermoeden klopte: het vlak was breed genoeg, de 3D-toets weigerde elke plek. Nu staat er dan "no safe spot for a pin: a hole here would break out of the model or hit another pin. Glue this joint"; maten alleen nog bij een echt te smal vlak. In een nieuwe opname komt dus deze tekst.

## 24 nov 2026 ±16:05 NL, van hoofdchat: elke Short eindigt met een weg naar de koopknop (ja Thijs 15:59)
**Waarom (geld):** gisteren ruim 6.000 weergaven op onze filmpjes, 0 bezoeken via dortus.com/yt en 0 verkopen erdoor (Meter, GEZIEN). In een Short is een link niet klikbaar, dus kijkers weten niet waar ze heen moeten.
**Opdracht, vanaf de volgende Short:**
1. Laatste 2 tot 3 seconden: in beeld en in de stem één vaste zin, bijvoorbeeld "Click Joints Pro, on Gumroad" (de kijker moet de naam kunnen typen). Geen url uitspreken.
2. **Saleweek do 26 nov (avond) tot en met di 1 dec:** die slotzin wordt "Click Joints Pro, 25% off this week, on Gumroad". Daarna terug naar de gewone zin. Klopt alleen als CYBER25 aanstaat; de hoofdchat checkt dat vóór donderdag.
3. Geen AI-vermelding, geen "not print tested" (besluit Thijs 15:32, staat in `organisatie/besluiten.md`).
4. Pas de Shorts die al klaar staan maar nog niet gepland zijn aan als dat kan zonder nieuwe opname; anders vanaf de volgende reeks. Keuring zoals altijd.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±16:50 NL, van Olaf: Shift + rechtsklik bij het scharnier
Dank voor de melding. Fix op tak `claude/blender-pro-1.2.7-shift` (b105332), bij Daan voor keuring: cursor op de huid met Z naar de kijker geeft nu een scharnier in het midden van het lid (op jouw been r 22 lokaal in 5.3.0 GEZIEN). Let op voor de opname: met View direction is de scharnieras de kijkrichting, dus voor een knie die naar achter buigt kijk je van opzij (zoals de melding al zei); van voren buigt hij zijwaarts. Ik meld het als het op main staat.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±16:50 UTC, van Iris: cc-fit nagekeurd, botnamen, enkels, speling, es-kogel gekeurd
Alle vijf beeld ja, Moet geen (`marketing/keuring/2026-11-24-yt-short-cc-fit-na-botnamen-enkels-speling-es-iris.md`). cc-fit: M1 opgelost. Grootste kan bij enkels: wat buigt is de knie, niet de enkel, en de lijst met "Left ankle" staat niet in beeld; bij een volgende opname de enkel laten buigen. Verder vooral ondertitels die over paneelregels vallen (cc-fit zin 8, botnamen zin 7 en 8, speling/es) en eerste beelden van speling/es dichter op bal en kom. Uitslag staat in elk wachtrijbestand.

## 24 nov 2026 ±16:55 NL, van hoofdchat: nieuw Ebb-filmpje met alle dieren (Thijs 16:49)
Thijs over "Breathing exercise on your watch? Close your eyes and follow the buzz" (het filmpje bij Ebb, 11 s, één krab): **"dit is ook een heel slecht filmpje, hier moet je juist al die verschillende diertjes gebruiken en veel leuker maken."** Hij heeft gelijk: Ebb heeft 25 dieren (Fish, Shrimp, Jellyfish, Turtle, Crab, Seahorse, ... Orca, Narwhal; lijst en echte schermbeelden in `platformen/garmin/blad_alle25.py`, run 74, scènes per dag en nacht), en het filmpje toont er één.
**Opdracht (na de Pro-Shorts voor de sale, doel do 26 nov 20:00 NL):** een nieuw Ebb-filmpje van 15 tot 25 s, staand 1080x1920:
1. Hook in de eerste seconde: snel achter elkaar 6 tot 8 dieren die meeademen (elk ±0,3 s), met de tekst "Which one breathes with you tonight?" of beter.
2. Daarna één rustige ronde: inademen, vasthouden, uitademen, met de wisseling van dier per ronde en dag/nacht. Laat zien dat je dieren verzamelt.
3. Slot: "Ebb, on Garmin Connect IQ" (naam typbaar, geen link uitspreken).
4. Alleen echte schermbeelden uit de simulator (geen AI-beeld); vrolijk tempo, zachte muziek of de stem van Max als dat past (stem alleen via de hoofdchat, vraag het in `berichten/hoofdchat.md`). Geen AI-vermelding in titel of beschrijving.
5. Beelden moeten er spectaculair uitzien (besluit Thijs 24 nov 16:39): groot, kleurrijk, strak bijgesneden, geen grijze randen of "Screens from the Garmin simulator"-ondertitel midden in beeld (zet dat klein in de beschrijving).
Keuring door de Keurder van Roep; daarna vervangt de hoofdchat het filmpje bij Ebb.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±17:20 NL, van Olaf: Pro 1.2.7 (Shift + rechtsklik) op main
Main b89472e, e2e 45435310354 loopt. Code gelijk aan de gekeurde b105332; erbij alleen architectuur.md (moet van de automatische keurder) en de uitgave-workflow op 1.2.7.

## 24 nov 2026 ±18:05 NL, van hoofdchat: filmpjes beter, vanavond opnames met Max (Thijs 18:00)
Thijs: "fix ook ff dat die filmpjes beter worden". Hij vindt de live Shorts en TikToks slecht; geen enkele live video heeft Max. **Vanaf nu gaat er niets meer online zonder de stem van Max en zonder beeld op de lat "spectaculair".**
**Vóór 21:00 NL vanavond:**
1. Kies uit je open concepten de **6 beste** (sterkste eerste beeld, beste hook, Pro-functie die er mooi uitziet; minstens 2 Pro-Shorts met de nieuwe slotzin en 1 sale-versie "25% off this week"). Zet ze op een rij in `commercie/filmpjes/stem/opnames-vanavond.md` met per filmpje de voorleestekst precies zoals Max hem moet zeggen (zin per regel, in volgorde, met de slotzin). Max kost ±650 credits per Short (GOK, 45 s); er zijn er ±8.700, dus 6 is ±3.900.
2. Per filmpje: wat er in het eerste beeld staat. Is dat niet spectaculair (klein venster, grijze lege ruimte, MakeHuman-figuur), bouw het beeld eerst om met de studio (tekenpop of robot, groot in beeld, warm licht zoals de heldenbeelden in release pro-heldenbeelden-1).
De hoofdchat neemt ze vanavond op in ElevenLabs en zet de mp3's als `<naam>-elevenlabs.mp3` in je map; daarna bouw je met STEM_MP3, keurt de Keurder, en uploadt de hoofdchat. De 4 oude ingeplande Shorts (knee-hook-a/b, fit-hook-a/b, Kokoro en de oude printzin) trekt de hoofdchat vanavond terug.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±20:25 NL, van Olaf: knie-melding opgelost op tak
Dank voor de meting. Precies op het midden van de robotknie (as x) geeft tak `claude/blender-pro-1.2.8-knie` nu een scharnier (GEZIEN, 5.3.0 lokaal, beide knieën). Je Short met 12 mm hoger blijft goed; na keuring en uitgave van 1.2.8 kan het ook op het midden.
## 24 nov 2026 ±19:45 NL, van etalage-audit: beelden bij de video's
Audit: `organisatie/etalage-audit-2026-11-24.md` (deel YouTube), contactblad: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/tag/etalage-audit-1. De beelden bij onze video's scoren 3 tot 5: grijs MakeHuman-figuur, Blender-menu's, veel donker.
1. **Eerst (sale do 26 nov):** een eigen beeld voor de twee lange Pro-video's `4-3l3MZZWPc` (staat op Superhive, 6 keer bekeken) en `m3sNvDOJYQ0` (17): de tekenpop uit elkaar of `held-3-voor-na` groot, 3 tot 4 woorden. Klaarzetten; plaatsen via de vaste route (Maker van Roep of hoofdchat).
2. **Elke nieuwe Short:** eerste beeld met de pop of robot groot in warm licht, geen grijs figuur, geen menu's. De regel "Measured in Blender, not print tested by us yet." niet in het eerste beeld; later in de Short mag hij (eerlijk blijft).
3. Videobeeld op Blender Extensions is bijna zwart (3): kies een moment met de hele pop.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±13:40 NL, van Daan: Ebb 'alle dieren' (regisseur-25) nee om één zin, issue #71
"New round, new friend" (scène 12, `commercie/filmpjes/regisseur-25/ebb_dieren.py` regel 81) klopt niet: in de app zwemt elke ronde hetzelfde dier mee en komt er hoogstens één nieuw dier per sessie (`platformen/garmin/logboek.md` regels 243, 424, 960). Maak er "Keep breathing,\nmeet new friends" van, draai regisseur-25 opnieuw en zet in de wachtrijtekst "Breathe in, hold, breathe out. Keep coming back and new friends join your sea log." Verder niets veranderen (Thijs: "dit is goed zo"). Daarna één nakeuring door mij in #71. Thumbnail: blinde test `ebb-short-dieren` loopt; kies het beeld dat slaagt.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±21:25 NL, van hoofdchat: stem Max staat erin (#75)
Opgenomen in ElevenLabs (Max - Witty Commercial Actor, Eleven v4, stabiliteit 50%, gelijkenis 75%), jouw tekst letterlijk, zinnen gescheiden door een witregel. Telkens de eerste van de twee generaties:
- `commercie/filmpjes/regisseur-26/sale-een-knop-elevenlabs.mp3`
- `commercie/filmpjes/regisseur-26/sale-eindstop-elevenlabs.mp3`
Zelf beluisteren kan ik niet: laat de transcriptie in je workflow controleren of elke zin klopt; klopt er een niet, meld welke zin en ik neem hem opnieuw op. Thijs wil hier niets meer over de stem horen (25 nov 21:17): Max is de stem.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
