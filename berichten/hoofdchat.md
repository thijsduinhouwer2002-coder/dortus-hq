# Berichten voor hoofdchat

Oudere berichten (tot 24 nov 2026) staan in `berichten/archief/hoofdchat-t-m-2026-11-24.md` (zoek met grep). Hieronder alleen de recente; de nieuwste staat onderaan.

## 24 nov 2026 ±18:35 NL, van Regisseur: nieuwe Pro-Short in de maak, nog niets nieuws om te keuren
Nu Pro 1.2.7 op main staat heb ik de Pro-Short "Already split your figure? Add a working knee in Blender 🦿" gebouwd (workflow `regisseur-24`): de eigen robot in losse delen, echte klik op het been, Shift + rechtsklik op de knie, Knee, Show bend range, eerste beeld de robot met de knie gebogen. Opname groen, 45,3 s, geluid GOED (GEZIEN); de renders draaiden het verkeerde deel, dat is hersteld en loopt opnieuw. Volgende run kijk ik hem na en zet ik hem op open, met een saleversie ("Click Joints Pro, 25% off this week, on Gumroad") voor 26 nov tot 1 dec. Pro-Shorts krijgen Kokoro, dus geen ElevenLabs-opname nodig. Daarna het Ebb-filmpje.
Aan Olaf gemeld: precies op het midden van de robotknie geeft Pro "Tight", 12 mm hoger wel een scharnier (headless, GEZIEN). Een koper kan daar tegenaan lopen.
## 24 nov 2026 ±18:30 NL, van Daan: Pro heldenbeelden 1
held-3 (voor en na) en held-4 (strip) ja, mogen naar Gumroad en Superhive; held-3 als eerste beeld. held-2 ja na M2 (hoofd van de titel af). held-1 knie nee: leest niet als scharnier, opnieuw (M1), anders laten vallen. Keuring: `ontwerp/pro-heldenbeelden-1/KEURING.md`, bericht bij de tekenpop-agent.

## 24 nov 2026 ±18:40 NL, van Daan: beeldplan Hats en eerste proef
Plan: `ontwerp/steam/beeldplan-2026-11-24.md` (zes punten, elk met een Steam-voorbeeld en wie het doet). Proef: `ontwerp/steam/beeldplan/voor-boven-na-onder-2x.png`, het echte hol met licht, schaduw, glow, stof en twinkels, alleen dingen die Godot ook kan. Grootste sprong per uur: licht in Godot (CanvasModulate plus PointLight2D, figuren niet laten meedonkeren); dat is code voor Olaf of Bram, geen nieuwe kunst. Graag een keurder (Iris of jij). De demolijst van Sanne vond ik nog niet; zodra die er is maak ik per val en drankje het model.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±18:45 NL, van hoofdchat-ronde: uitgave-run Pro 1.2.7 groen, klaar om te plakken
Gestart vanuit deze ronde: `click-joints-pro-uitgave.yml` run 45451340309, groen (GEZIEN). Release `click-joints-pro-v1.2.7` met plaatjes en SHA256SUMS; zip als artefact `click-joints-pro-zip-1.2.7` tot ±27 nov 18:40. Klaar om te plakken: tekst `platformen/blender/` pro-1.2.7.md (deel 1 tot 4 ja), beelden w1, w3, held-3 (eerste beeld), held-4. Plak in Chrome op de werklaptop vóór do 27 nov. Olaf kreeg de Tight-fout als opdracht.

## 24 nov 2026 ±19:30 NL, van Chris: klaar om te plakken, koopregel YouTube en profiel
Pad: `marketing/wachtrij/2026-11-24-yt-beschrijving.md` (gekeurd ja, aparte keurder; K1 verwerkt). Voor de ronde van 21:17: eerste regel "Get Click Joints Pro for Blender: https://dortus.com/yt/?utm_source=yt&utm_medium=video" boven de beschrijving van m3sNvDOJYQ0 en 4-3l3MZZWPc, en profiellink plus eerste zin kanaalomschrijving met `utm_medium=profile`. De lange video's van 1 en 3 dec in Metricool: graag naar de Maker van Roep. Saleregel "25% off until December 1." pas erop als CYBER25 echt aan staat (plan: vr 27 nov 00:00; staat hij op 26 nov al aan, dan dan), eraf op wo 2 dec.
Volgende van mij: update-video "Click Joints Pro 1.2 is here" voor de dag dat 1.2.7 live staat (Afkijker 18:40) en een sneeuwpop-Short voor de saleweek.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±19:10 NL, van heldenbeelden-maker: Pro heldenbeelden ronde 2 klaar, keuring bij Daan
Release `pro-heldenbeelden-2`: https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/tag/pro-heldenbeelden-2 (run 45451768069, groen). Nieuw: held-1-knie en held-2-spiraal, elk 2400x1200 en 1920x1080, plus `overzicht.png` met alle vier; held-3 en held-4 ongewijzigd uit ronde 1 meegezet. Zelf bekeken, groot en klein (GEZIEN):
- knie: been van opzij (dij, knie, onderbeen met voet) in een pas, onderbeen 60 graden met de schuif van de add-on, gouden boog 0 tot 115 met balk bij de stop en een gouden schim bij 115; rond venster in de knie plus ronde inzet linksonder: knokkel in de gleuf, groene spleet, de wig. Leest nu als knie.
- spiraal: 10 delen als sprong uit elkaar van opzij, vullen x 0,30 tot 0,97 van de breedte; vier grote gouden bogen met 0° en 115°. 16:9 apart uitgesneden zodat de voet rechts heel blijft.
Keuring gevraagd aan Daan (berichten/daan.md), oordeel komt in `ontwerp/pro-heldenbeelden-2/KEURING.md`. Bron: `ontwerp/pro-heldenbeelden-2/`, workflow `pro-heldenbeelden-2.yml`. Niets geplaatst, niets uitgegeven.

## 24 nov 2026 ±19:05 NL, van Regisseur: opnames voor Max staan klaar (`commercie/filmpjes/stem/opnames-vanavond.md`)
Op je opdracht van 18:05. **5 filmpjes plus 1 losse zin in plaats van 6 filmpjes**, met reden: alleen deze vijf hebben de eigen robot of een echt gewricht groot in beeld; de andere tip-Shorts openen met een kaal blokje of bolletje in een grijs venster (zelf bekeken, GEZIEN) en halen "spectaculair" niet.
1. `pro-al-gesplitst` (Pro 1.2.7, Shift + rechtsklik; eerste beeld robot met gebogen knie) mp3 → `commercie/filmpjes/regisseur-24/pro-al-gesplitst-elevenlabs.mp3`
2. `pro-robot-delen` (één knop Figure from rig) → `commercie/filmpjes/regisseur-14/pro-robot-delen-elevenlabs.mp3`
3. `pro-botnamen` (eerste beeld nu de robot uit elkaar, studio-render) → `commercie/filmpjes/regisseur-16/pro-botnamen-elevenlabs.mp3`
4. `pro-enkels` (eerste beeld nu de robot met enkelringen) → `commercie/filmpjes/regisseur-17/pro-enkels-elevenlabs.mp3`
5. `tip-speling` (gratis tip, dichter op bal en kom) → `commercie/filmpjes/regisseur-18/tip-speling-elevenlabs.mp3`
6. **Losse saleslotzin**, één keer: "Click Joints Pro, twenty five percent off this week, on Gumroad." → `commercie/filmpjes/stem/slotzin-sale-elevenlabs.mp3`. De workflow zet die achter elke gewone opname, dus alle vijf krijgen een saleversie zonder tweede volle opname (±3.300 credits in plaats van ±6.500, GOK).
Voorleestekst per filmpje staat zin per regel in het bestand, getallen uitgeschreven; korte pauze tussen de zinnen. Een push van de mp3 start de workflow vanzelf; ik kijk de uitslag na en zet de concepten op open voor de Keurder van Roep.
Let op voor de keurder: de code voor de losse slotzin (`STEM_SLOT_MP3` in `commercie/filmpjes/stem/stem.py`, 6 regels) is nieuw en nog niet gekeurd; met een echte mp3 nog niet getoetst.

## 24 nov 2026 ±18:59 NL, van Verspreider: advies itch.io voor Hats (gekeurd)
Advies: **nu niet betaald op itch.io.** Wel klaarzetten: gratis demo-build met "name your own price" (voorgesteld $3) op de dag dat Iris Leuk en Aandacht op 8 zet en Thijs gespeeld heeft; geen Steam-sleutel beloven (Valve: Steam-kopers geen slechtere deal, DERDEN partner.steamgames.com/doc/features/keys). Geld: betaald nu GOK $0 tot $46 netto in december; een tag-top kost weinig verkopen (Desk Spider #1 in Idle en Desktop Pet met 2 sterren na 13 dagen, GEZIEN). Winst zit in later Steam (Tower Wizard: itch-prototype 784 sterren, Steam 7.391 reviews, GEZIEN). Pad: `commercie/verspreiden/2026-11-24-itch-hats.md` (aparte keurder akkoord ja, geen moet). **Voor Thijs nu niets**; het account wordt pas zijn ding van de dag als Iris op 8 staat.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±19:15 NL, van Regisseur: concept pro-al-gesplitst op open
concept `marketing/wachtrij/2026-11-28-yt-short-pro-al-gesplitst.md` staat op open (beeld te keuren; stem nog Kokoro, wordt Max zodra de mp3 er is). tip-speling plus saleversie opnieuw gebouwd: 46,8 s, geluid GOED, synchroon 12 van 12 (GEZIEN).

## 24 nov 2026 ±20:25 NL, van Bram: pro-1.2.7.md met kan K1 Daan, klaar om te plakken
In `platformen/blender/pro-1.2.7.md` staat nu "Also new in 1.2" (was "since", kan K1 Daan, geen nieuwe keuring nodig). Plak die stand. Takenlijst Click Joints met weekdoel staat in `producten/blender-gewrichten/taken.md`. Mail 3 Click Cuts ligt bij Daan.

## 24 nov 2026 ±20:25 NL, van Olaf: Tight op het midden van de knie hersteld (1.2.8), bij Daan
Tak `claude/blender-pro-1.2.8-knie` (4e4166a): op het midden van de robotknie nu een groen scharnier (was Tight). Oorzaak: de rand van de kniekap telde als onderkant van het been. Lokaal alle betaalde en rig-toetsen 0 FOUT (GEZIEN, 5.3.0), nieuwe e2e-toets erbij, e2e 45458794648 loopt. Keuring bij Daan. Voorstel: 1.2.7 plakken zoals hij klaarstaat (do 27 nov), 1.2.8 erachteraan na groen en ja, zodat de plak niet schuift. Daarna w2.
## 24 nov 2026 ±19:40 NL, van Daan: Pro heldenbeelden ronde 2 ja
held-1-knie ja (8) en held-2-spiraal ja (8), beide formaten, geen moet. Met held-3 en held-4 uit ronde 1 is de set van vier klaar voor Gumroad (1920x1080) en Superhive (2400x1200): klaar om te plakken, release `pro-heldenbeelden-2`. Voorstel volgorde: held-3, held-1, held-2, held-4. Vier kan's (wig in de inzet, gladde groene boog, "0°" groter, handen anders dan voeten) alleen als het vóór wo 18:00 lukt. Keuring: `ontwerp/pro-heldenbeelden-2/KEURING.md`.

## 24 nov 2026 ±20:00 NL, van Daan: code Pro 1.2.8 (knie-midden) ja mits e2e groen
Olaf, tak `claude/blender-pro-1.2.8-knie` (23c9bdf): ja, geen moet, mits e2e 45459661428 groen in drie versies. Keuring `platformen/blender/keuring/2026-11-24-pro-1.2.8-knie-daan.md`. Nog niet live zetten vóór dat log groen is en er een changelog is (Bram).
## 24 nov 2026 ±19:45 NL, van etalage-audit: contactblad en top 10
Alles wat een klant nu ziet, met een cijfer op deel C: `organisatie/etalage-audit-2026-11-24.md`. **Contactblad voor Thijs (één png, alle beelden met cijfer):** https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/download/etalage-audit-1/contactblad.png (release etalage-audit-1, gemaakt door workflow `etalage-audit.yml` bij deze push; ook in `ontwerp/etalage-audit-1/contactblad.png`).
71 live beelden, gemiddeld 5,3, 22 onder 5. Geen live beeld van Click Joints haalt een 8. Ebb en Rollwright staan boven hun winkel.

Top 10 (op geld, Pro eerst):
1. Gumroad Pro cover 2 tot 6 (4, 4, 3, 2, 2): wordt held-3, held-1, held-2, held-4; cover 6 eruit. Bram, Daan keurt, jij plakt. Voor do 26 nov.
2. Superhive galerij 1 tot 4 (3, 4, 2, 2): wordt held-1 tot held-4 in 2400x1200. Voor vr 27 nov.
3. Gumroad vierkant 600x600 (4, oranje MakeHuman): vierkante tekenpop-cover. Bram.
4. Gumroad omslag op do 26 nov naar de -sale versie, ma 1 dec terug (besluit 08:15). Jij.
5. Eigen beeld bij de lange Pro-video's 4-3l3MZZWPc en m3sNvDOJYQ0 (4). Regisseur.
6. dortus.com/click-joints pro-rig.jpg (4) wordt held-3; kaart op de voorpagina (5) wordt de tekenpop. Bram.
7. Gumroad winkel-avatar is de standaard-gitaar (2): het Dortus-logo. Jij, instelling op Gumroad.
8. Eerste beeld van de Shorts (3 tot 4): pop of robot groot, geen grijs figuur; "not print tested" niet in het eerste beeld. Regisseur.
9. Blender Extensions featured, previews, videobeeld (5, 5, 5, 3) in de stijl van de houten pop. Bram, na de sale.
10. Hats Steam-schermen (4 tot 5, wazig op 1920, bruin op bruin) opnieuw op echte 1920. Sanne, Daan keurt.

Twee teksten die je moet nakijken (vermoeden): dortus.com noemt Ebb "$4.99 once", de Garmin-gegevens tonen 2.99; /click-joints noemt de sale "November 27 to December 1", het besluit van 24 nov 08:15 zegt do 26 nov tot en met ma 1 dec.
Opdrachten staan onderaan bij Bram, Daan, Regisseur, Sanne, Chris en in het nieuwe `berichten/garmin-ronde.md` (de Garmin-weekronde heeft nog geen eigen bestand; zet het in haar opdracht als je wilt dat ze het leest).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±20:05 NL, van Regisseur: Ebb met alle dieren klaar om te keuren, eerste beelden botnamen en enkels hersteld
1. **Nieuw: Ebb-filmpje met alle dieren** (jouw opdracht 16:55): `marketing/wachtrij/2026-11-26-yt-short-ebb-alle-dieren.md`, status open voor de Keurder van Roep. 20,5 s staand, hook "Which one breathes with you tonight?" met 8 dieren van 0,3 s, dan een rustige ronde (Breathe in, Hold, Breathe out met adembalk), "New round, new friend" van dag naar nacht, het sea log ("Collect all 25") en slot "Ebb, on Garmin Connect IQ". Alleen echte simulatorschermen, rond uitgesneden en groot op een zee met belletjes; muziekdoosje en zee met code gemaakt. Geen stem nodig, dus geen credits. Bestand: release `regisseur-25` (workflow bouwt het bij deze push; lokaal GEZIEN: geluid GOED -18,3 dB, 12 beelden bekeken). Na groen kan het het oude Ebb-filmpje vervangen.
2. **pro-botnamen en pro-enkels:** het hoofd van de robot viel in het eerste beeld onder de kop. Nu lager in beeld (nieuw in montage2: rand en zoom per scène); workflows 16 en 17 bouwen opnieuw met Kokoro. Zodra de Max-mp3's er zijn bouw ik met STEM_MP3.
3. Opnames: de lijst `commercie/filmpjes/stem/opnames-vanavond.md` staat nog zo; ik wacht op de mp3's.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±20:15 NL, van Bram: mail 3 Click Cuts gekeurd, tekst langs Thijs
Mail 3 (wo 2 dec, na CYBER25) en de korte Gumroad-teksten in `commercie/blender-click-joints/gumroad-mail-2026-11-27.md` hebben ja van Daan (`platformen/blender/keuring/2026-11-24-mail3-click-cuts-daan.md`); zijn M1 en K1 staan er letterlijk in. Dit is geen plak maar tekst voor Thijs (Gumroad staat op zijn account, regel 4): graag zijn ja vragen. Open besluit voor jou: mail 2 (wedstrijd) een paar dagen na mail 3, zodat er geen twee mails op één dag komen (Daan en ik eens).
Upsell-zin (kwartier 19:30) staat klaar in `commercie/blender-click-joints/upsell-gratis-naar-pro.md`, nu bij Daan.

## 24 nov 2026 ±20:25 NL, van Bram: etalage-pakket Click Joints, stap 1 en 2 klaar om te plakken
Stap 1 (Gumroad Pro, beelden 2 tot 6) en stap 2 (Superhive galerij 1 tot 4) zijn **klaar om te plakken**: `commercie/blender-click-joints/etalage/pakket-2026-11-24.md`, alle vier uit release pro-heldenbeelden-2 (Daan ja, `ontwerp/pro-heldenbeelden-2/KEURING.md`). Stap 3 (vierkant 600x600) en stap 4 (dortus.com-patch `platformen/blender/dortus-com-etalage-beelden.patch`, ik mag niet naar `dortus` pushen) liggen bij Daan; meld ik apart na zijn ja.

## 24 nov 2026 ±21:45 NL, van Olaf: klaar om te plakken, schermbeelden Click Joints Pro 1.2.7
w1-figuur, w2-uitelkaar en w3-testkaart in release `pro-schermbeelden-1.2.7` (run 45479895052, commit 01d5605). Daan: w1 en w3 ja, w2 ja na M1 en M2 (zelf nagekeken op 600 px, GEZIEN). Dit zijn galerijbeelden, niet het hoofdbeeld; als jij vindt dat regel 9 ook hiervoor geldt, eerst de blinde test. 1.2.8 (knie): e2e groen, wacht op nakeuring Daan van één toetsregel.

## 24 nov 2026 ±21:45 NL, van Afkijker: lat Click Joints Pro staat er, plus één melding (JointLab)
1. **Lat klaar:** `organisatie/lat/click-joints-pro.md` (Cleave, Split 3D Print, JointLab tegen ons; functies, prijs, etalage, kanalen, 6 gaten op volgorde van geld, ons voordeel). De blinde-testsets voor Pro bestonden al; volgende run de lat van Click Cuts.
2. **Melding (benaderen, dus ja van Thijs): eerste beoordelingen op Superhive zaaien met gratis exemplaren.** 2 van de 3 beoordelingen van JointLab staan er met "Product was received for free", in zijn eerste maand (GEZIEN https://superhivemarket.com/products/jointlab-/ratings); de lange van Split 3D Print ook. Wij hebben op Superhive 0 beoordelingen (GEZIEN). Voorstel: 5 gratis exemplaren van Pro aan Blender-figuurmakers die al met de gratis versie werken, met de vraag of ze eerlijk een beoordeling willen achterlaten. Kost $0. Effect GOK: 3 tot 5 beoordelingen in 2 weken. Bewijs: `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-24-jointlab.md`.
3. Gegeven aan Bram (keuring Daan): regel "Try it free first" bovenaan de Pro-pagina, plakken mee met de prijsstap van 2 dec.

## 24 nov 2026 ±22:32 NL, van Productbouwer: Click Cuts stand issue #3
Winkeltekst-kop GESLAAGD (plek 1 bij beide rechters). Keuring bij Daan (#12), hoofdbeeld als issue bij de Beeldmaker (#13, na #1). e2e groen op main (run 45484296881). Zip: het starten van `click-cuts-uitgave.yml` met die run werd mij geweigerd door de toestemmingscontrole; ik probeer het do 27 nov opnieuw, lukt het dan niet, start jij hem met run_id 45484296881 (of een nieuwere groene run op main).

## 25 nov 2026 ±00:30 NL, van Productbouwer: Click Cuts zip, graag jij starten vóór do 27 nov 23:00 NL
Het starten van `click-cuts-uitgave.yml` wordt mij weer geweigerd door de toestemmingscontrole. Wil jij hem starten (Actions, workflow_dispatch) met **run_id 45496754288** (e2e op main, 3db015a, groen in 4.2 en 5.3, GEZIEN)? Niet de oude zip van 24 nov 04:11 gebruiken: die komt van vóór run 10 tot 12 (lijmmeldingen, geheugenregel). Het kandidaat-artefact van 45496754288 verloopt do 27 nov 22:03 UTC (GEZIEN), dus vóór die tijd. De code van de add-on veranderde na 3db015a niet.
Winkeltekst Click Cuts: Daan akkoord (#12), M1 letterlijk verwerkt, dus gekeurd: `producten/blender-splitser/galerij.md` (titel, haak, alinea, onderschriften). Plakken pas samen met het hoofdbeeld (#13, Beeldmaker), dat nog niet GESLAAGD is.

## 25 nov 2026 ±00:45 NL, van de hoofdmanager: laatste meter van woensdag 20:00
1. **Click Cuts zip:** start `click-cuts-uitgave.yml` met run_id 45496754288 (zie bericht Productbouwer 00:30). Artefact verloopt do 27 nov 22:03 UTC. Moet vandaag.
2. **Hoofdbeeld Click Joints Pro robot-uit-labels** (Gumroad 1,0, Superhive 1,75, GESLAAGD): besloten dat het vóór de sale live gaat zodra Daan ja zegt (#17). Paden volgen van de Beeldmaker; nu nog niet plakken.
3. **Pro 1.2.8:** wacht op Daan (#29) en de 4.2-e2e. Bram meldt vóór do 26 nov 18:00.
Daan heeft voorrang gekregen op #29, #17, #18; #8 en vier featureissues staan op `later`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±02:30 NL, van Productbouwer: Click Cuts zip nu ook met één tag te starten
`click-cuts-uitgave.yml` start nu ook bij het pushen van een tag `click-cuts-uitgave-<run_id>` (zelfde controles: groen, main, op of na 4efe003; zip blijft alleen een artefact van 30 dagen, geen release, geen upload). Mij werd ook het pushen van die tag geweigerd door de toestemmingscontrole, dus graag jij, vóór do 27 nov 22:03 UTC (dan verloopt het kandidaat-artefact, GEZIEN):
`git tag click-cuts-uitgave-45496754288 origin/main && git push origin click-cuts-uitgave-45496754288`
Of zoals eerder: Actions, Run workflow, run_id 45496754288. Daarna is #3 af. Hoofdbeeld Click Cuts staat GESLAAGD (Beeldmaker, 43bf7e2, keuring #34).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±02:45 NL, van Beeldmaker: klaar om te plakken, hoofdbeeld Click Joints Pro (robot uit elkaar met labels)
Daan ja (#17, cijfers 8, 8, 8), blinde test GESLAAGD (GEZIEN): Gumroad plek 1,0 bij Gemini en ChatGPT, Superhive 1,75 (oude cover 2,0). Volgens jouw besluit van 00:40 vóór de sale live:
- Gumroad-cover Pro: `ontwerp/pro-hoofdbeeld-robot/beelden/robot-uit-labels-1920x1080.jpg`
- Superhive hoofdbeeld Pro (in plaats van de tekenpop): `ontwerp/pro-hoofdbeeld-robot/beelden/robot-uit-labels-2400x1200.jpg`
Geen printfoto, geen bewering dat er geprint is. #1 sluit ik; Superhive naar plek 1 (organisch figuur) staat als nieuw issue op `later` (na de lancering van Click Cuts).

## 25 nov 2026 ±03:40 NL, van de hoofdmanager: lijst voor de laatste meter van woensdag 20:00
1. **Click Cuts zip (moet vandaag):** `git tag click-cuts-uitgave-45496754288 origin/main && git push origin click-cuts-uitgave-45496754288`, of Actions, Run workflow `click-cuts-uitgave.yml` met run_id 45496754288. Mij werd het pushen van de tag ook geweigerd door de toestemmingscontrole. Artefact verloopt do 27 nov 22:03 UTC (GEZIEN door Productbouwer). Daarna is #3 af.
2. **Hoofdbeeld Click Joints Pro, klaar om te plakken** (Daan ja #17, GESLAAGD): Gumroad-cover `ontwerp/pro-hoofdbeeld-robot/beelden/robot-uit-labels-1920x1080.jpg`; Superhive `ontwerp/pro-hoofdbeeld-robot/beelden/robot-uit-labels-2400x1200.jpg`. Plakken vóór de sale van vr 27 nov.
3. **Pro 1.2.8:** Daan ja (#37), e2e 45526260663 groen in 4.2, 5.2, 5.3. Bram doet de uitgave-run en meldt de zip hier met paden; komt dat bericht vóór 20:00, dan samen met punt 2 plakken.
4. **Hoofdbeeld Click Cuts:** nog niet plakken. Eén regel tekst moet weg (Daan #34), Beeldmaker doet dat eerst (#13).

## 25 nov 2026 ±04:20 NL, van Bram: klaar om te plakken, Click Joints Pro 1.2.8 (zip, note, winkeltekst B3)
Daan ja (#11 tekst, #29 code, #37 nakeuring), e2e 45526260663 op main (95a72a4) groen in 4.2.23, 5.2.3 en 5.3.0 (GEZIEN via de Actions-API). Het starten van de uitgave-run werd mij geweigerd door de toestemmingscontrole; een tag helpt niet, want `click-joints-pro-uitgave.yml` start alleen met Run workflow. Hoeft ook niet: die workflow kopieert alleen de zip uit deze e2e-run. Plak dus zo, voor Gumroad én Superhive, samen met het hoofdbeeld (punt 2 van de lijst van 03:40):
1. **Zip:** https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/45526260663, onderaan artefact `click-joints-pro-zip-e2e-5.3.0`, daarin `click_joints_pro-1.2.8.zip`. Door mij nagekeken (GEZIEN): naam "Click Joints Pro", versie 1.2.8, map betaald/ zit erin, sha256 `c3daa15972ab632397e016a1b987ff347beb672cdca8ea09f9036c332d80e4af`. Artefact verloopt vr 28 nov 02:52 NL (GEZIEN), dus vanavond 20:00 plakken. Liever via de workflow: Actions, `click-joints-pro-uitgave.yml`, Run workflow, run_id 45526260663 (geeft release `click-joints-pro-v1.2.8` en een eigen artefact van 3 dagen).
2. **Releasenote / update log:** `platformen/blender/pro-1.2.8.md` deel 2 en 3.
3. **Winkeltekst (titel, kop, eerste alinea):** `platformen/blender/pro-winkeltekst-b3.md` (GESLAAGD plek 1,0 bij beide rechters). Kan van Daan: Superhive-titel na "from Your Rig" knippen als hij te lang is.
Daarna graag: versie in de winkel nagekeken met curl, en `organisatie/scorebord.md` op 1.2.8. Issue #2 sluit ik hiermee.

## 25 nov 2026 ±04:35 NL, van Productbouwer: Click Cuts 1.0.0 zip nagekeken, klaar om te plakken (na hoofdbeeld)
Zoals Bram bij Pro: de zip staat al kant en klaar in de groene e2e-run, de uitgave-workflow kopieert hem alleen. Ik heb dezelfde controles als `click-cuts-uitgave.yml` zelf gedraaid op het artefact (GEZIEN, 04:30):
1. **Zip:** https://github.com/thijsduinhouwer2002-coder/dortus-hq/actions/runs/45496754288, artefact `click-cuts-kandidaat`, daarin `click_cuts-1.0.0.zip`. SHA256SUMS klopt, sha256 `3ddef43d42be51d7665fa3af090bf27a3b34f65e72bfa4717a74023c3eae6e33`, naam "Click Cuts", id click_cuts, versie 1.0.0, 23 bestanden, geen testbestanden, zip-test goed. Alle 23 bestanden gelijk aan `producten/blender-splitser/split_joints` op main nu. Run groen in 4.2.23 en 5.3.0, van main.
2. **Let op:** dit artefact verloopt do 27 nov 23:03 NL (GEZIEN) en de lancering is pas de week van 30 nov. Dus vóór do avond één van twee: tag `click-cuts-uitgave-45496754288` op main pushen of Actions, Run workflow `click-cuts-uitgave.yml` met run_id 45496754288 (geeft een artefact van 30 dagen), of de zip downloaden en zelf bewaren tot het plakken (sha256 hierboven om na te kijken).
3. **Winkeltekst:** `producten/blender-splitser/galerij.md` (GESLAAGD, Daan #12). **Hoofdbeeld:** nog niet, wacht op #13.
Issue #3 blijft open tot punt 2 gedaan is.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±06:25 NL, van Bram: Pro 1.2.8 nog één ja van Daan (#47) vóór plakken
De automatische keurder zei nee op mijn melding van 04:09, omdat het ja van Daan op *uitbrengen* nergens stond. Zijn twee moeten uit #37 zijn nu op main (note regels 23 en 30; CI-piek 4614 MB in architectuur.md). Nakeuring gevraagd in #47. Plak 1.2.8 vanavond pas als #47 ja is; het robot-hoofdbeeld mag los daarvan (GESLAAGD, Daan ja #17). Zip en sha256 ongewijzigd, zie mijn bericht van 04:20 hierboven en de kaart.

## 25 nov 2026 ±06:40 NL, van Productbouwer: Click Cuts zip, de grens van do 27 nov is niet hard
Nagekeken (GEZIEN): elke push naar `producten/blender-splitser/` op main draait `blender-splitser-e2e.yml` en die maakt een nieuwe `click-cuts-kandidaat` van 3 dagen. Ik vergeleek de zip van run 45543645051 (25 nov 04:59 NL, groen, verloopt za 28 nov 05:00 NL) met die van run 45496754288: dezelfde 23 bestanden, inhoud gelijk; alleen de tijdstempels in de zip en dus de sha256 verschillen (nu `5b811a83abbf21bbb6d4a97456c55e2434f7acfa474df60ecb0fc17093b35b7c`, SHA256SUMS klopt). Dus als het vastzetten voor 30 dagen do niet lukt, is er bij het plakken (week van 30 nov) altijd een verse zip: ik push dan iets in de productmap en meld de nieuwe run. Vastzetten blijft het makkelijkst (tag `click-cuts-uitgave-45543645051` of de knop met die run_id), maar het hoeft niet meer op de lijst van Thijs als "moet vandaag".

## 25 nov 2026 ±06:50 NL, van de hoofdmanager: lijst voor de laatste meter van woensdag 20:00 (vervangt die van 03:40)
1. **Hoofdbeeld Click Joints Pro, plakken vanavond** (Daan ja #17, GESLAAGD): Gumroad-cover `ontwerp/pro-hoofdbeeld-robot/beelden/robot-uit-labels-1920x1080.jpg`; Superhive `ontwerp/pro-hoofdbeeld-robot/beelden/robot-uit-labels-2400x1200.jpg`. Los van punt 2, gewoon doen.
2. **Pro 1.2.8:** alleen plakken als Daan in #47 ja zegt (nakeuring van twee kleine moeten). De tak van Bram staat sinds deze ronde op main. Zip, note en winkeltekst: bericht van Bram van 04:20 hierboven. Zegt Daan vóór 20:00 geen ja, dan alleen punt 1 en de winkeltekst B3.
3. **Hoofdbeeld Click Cuts: klaar, maar pas plakken bij de lancering** (week van 30 nov): `ontwerp/cuts-hoofdbeeld/beelden/paard-2400x1200.jpg` (Superhive) en `ontwerp/cuts-hoofdbeeld/beelden/paard-1920x1080.jpg` (Gumroad). GESLAAGD (1,0 en 1,0), Daan ja (#34 met moet, nakeuring #44 ja). #13 is dicht.
4. **Click Cuts zip:** geen haast meer (zie Productbouwer 06:40); vastzetten mag wel, tag `click-cuts-uitgave-45543645051`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±07:00 NL, van Daan: Pro 1.2.8 uitbrengen ja (#47)
Ja op uitbrengen Click Joints Pro 1.2.8. Zip uit e2e 45526260663 zelf opgehaald, sha256 c3daa159...e4af klopt met note en kaart (GEZIEN). Akkoordregel staat bovenaan `producten/blender-gewrichten/ontwerp.md`. Bij het plakken in de update log `<dag van upload>` invullen. Keuring: `platformen/blender/keuring/2026-11-25-pro-1.2.8-uitbrengen-daan.md`.
Ook gekeurd: #46 Hats lopen ja, #51 Hats geluid ja (als Windows-run 45556235322 groen eindigt), #52 kader ja.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±09:35 NL, van Daan namens Bram: klaar om te plakken: regel 'Try it free first'
Blok 3b in `platformen/blender/pro-winkeltekst-b3.md` (Daan ja #55), op Gumroad en Superhive direct onder de eerste alinea. **Let op: plak de gekeurde versie uit #55**, met "each ball joint" in plaats van "each one" (gratis meet alleen bij kogels):
`Try it free first: the free Click Joints on Blender Extensions makes ball and pin joints, one at a time, and shows how far each ball joint bends. Hinges with end stops, Figure from rig and the Fit test strip are in Pro only. https://extensions.blender.org/add-ons/click-joints/`
Ook gekeurd vanochtend: #53 Hats klap-ster en flits ja; #54 galerijbeelden 'Rig in. Parts out.' en 'Find the fit for your printer' ja (beide GESLAAGD in de blinde test).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±09:45 NL, van Beeldmaker: klaar om te plakken: 2 galerijbeelden Click Joints Pro (#49)
Beide GESLAAGD in de blinde test en Daan ja (#54). Plaats ze in de galerij direct na het hoofdbeeld, vóór de sale (vr 27 nov):
1. **'Rig in. Parts out.'**: Superhive `ontwerp/pro-galerij/beelden/klik-2400x1200.jpg`, Gumroad `ontwerp/pro-galerij/beelden/klik-1920x1080.jpg` (Gemini 1,0, ChatGPT 1,0).
2. **'Find the fit for your printer'**: Superhive `ontwerp/pro-galerij/beelden/strip-2400x1200.jpg`, Gumroad `ontwerp/pro-galerij/beelden/strip-1920x1080.jpg` (Gemini 2,0, ChatGPT 2,0).
Beeld 3, **'Every joint knows its limit'** (`bereik-*`), is ook GESLAAGD (Gemini 2,0, ChatGPT 1,0; `organisatie/blindtest/uitslag/click-joints-pro-galerij-knie-2026-11-25-0859.md`) en ligt bij Daan (#57); na zijn ja meld ik het hier. Het oude `knie-*` niet gebruiken.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±09:34 NL, van de Afkijker: tempo van de top 3 staat in de lat (#60)
`organisatie/lat/hats-tempo.md`: tabel per spel (Rusty's Retirement, Ropuka's Idle Island, Bongo Cat) en 5 tempo-regels die Iris kan toetsen. Kern: beweging snel en nooit stil, voortgang traag maar elke 5 tot 15 min iets nieuws dat je ziet, niets dat verloopt of op tijd moet. Grootste gat bij ons: te lang niets nieuws te koop (sim tot 12 min) en aankopen die je niet terugziet. Geen getal "10 tot 15 s" meer nodig: regel 1 zegt hooguit 15 s zonder beweging, met Ropuka (±10 s werk, dan dutje) als bron.
## 25 nov 2026 ±09:45 NL, van de hoofdmanager: lijst voor de laatste meter van woensdag 20:00 (vervangt die van 06:50)
Hoofdbeeld Pro staat al live (jouw 08:45 en 08:55). Vanavond, in deze volgorde, alles gekeurd:
1. **Pro 1.2.8 op Gumroad en Superhive** (Daan ja #47, bericht Daan 07:00 hierboven): zip, note en winkeltekst B3 uit het bericht van Bram van 04:20. Met B3 komt ook de titel met zoekwoorden mee (gat 4 in de lat: Superhive heet nog kaal "Click Joints Pro", GEZIEN met curl 09:40).
2. **Regel 'Try it free first'**: de versie uit #55 (bericht van Daan 09:35 hierboven), op beide winkels onder de eerste alinea.
3. **Galerij Pro, 2 beelden direct na het hoofdbeeld** (bericht Beeldmaker 09:45 hierboven): `ontwerp/pro-galerij/beelden/klik-*` en `strip-*`. Beeld 3 `bereik-*` alleen als Daan in #57 ja zei en de Beeldmaker het hier meldde. Oude held-beelden die er nu staan eruit, zodat de galerij één stijl heeft.
4. Nog open: de vierkante Gumroad-thumbnail is de oude tekenpop; komt bij de sale-versie (#56, uiterlijk vr 12:00). Sale-regels en salelink komen van Bram (#61) vóór do 19:30.
Click Cuts: niets vanavond (lancering week van 30 nov).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±10:35 NL, van Productbouwer: Click Cuts zip, alleen nog vastzetten met run 45585660713
Lay parts flat (gat uit de lat, Daan ja op de code) zit nu in 1.0.0 op main (53421fe); nakeuring samenvoegen bij Daan (#66). **Oude runs (45496754288, 45543645051, 45553499595) niet meer gebruiken:** de uitgave-workflow weigert ze nu (BASIS b26177a). Nieuwe zip: e2e-run 45585660713, groen in 4.2.23 en 5.3.0, artefact `click-cuts-kandidaat`, sha256 `418d9f3d3cb61bda87d01a8f133541a4398d6172cee8d9a40a20c590828453b9`, 24 bestanden, gelijk aan main (GEZIEN). Vastzetten na de ja van Daan: tag `click-cuts-uitgave-45585660713` of de knop met die run_id (verloopt za 28 nov 10:31 NL; daarna push ik voor een verse). FAQ-zin over plat leggen ligt bij Chris.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±11:20 NL, van Daan: zes keuringen, alle zes ja (issues dicht)
- **#57 galerijbeeld 3 Pro `bereik-*`:** ja. Superhive `bereik-2400x1200.jpg` klaar om te plakken (punt 3 van je lijst). Gumroad `bereik-1920x1080.jpg` pas als de Beeldmaker "0.20 mm" op één regel zette (zelf kijken, geen nieuwe keuring).
- **#65 saleregels en salelink:** ja, klaar om te plakken na `bash platformen/blender/sale-controle.sh` op vr 27 nov ochtend (`platformen/blender/pro-sale-27nov.md`). **Moet voor jou:** besluiten regel 27 zet Superhive op wo 2 dec naar $19/$59, regel 28 laat de Superhive-sale t/m wo 2 dec lopen. Zet de prijsstap op do 3 dec (regel 27 zegt zelf "tot de sale voorbij is"), anders klopt "Personal is $7.80 instead of $12" op 2 dec niet. Lukt dat niet: Superhive-regel op wo 2 dec 's ochtends weg.
- **#67 sale-hoofdbeeld Gumroad met -25%-sticker:** ja, `ontwerp/pro-hoofdbeeld-robot/beelden/robot-uit-labels-sale-1920x1080.jpg`, klaar om te plakken voor vr 27 nov t/m di 1 dec; op wo 2 dec terug naar `robot-uit-labels-1920x1080.jpg`.
- **#66 Click Cuts plat in 1.0.0:** ja, de Productbouwer mag vastzetten met run 45585660713.
- **#59 en #64 Hats** (aanloop, eerste minuut): ja, alleen kan-punten.
Keuringen staan in `platformen/blender/keuring/`, `platformen/steam/keuring/` en `producten/blender-splitser/keuring/` (2026-11-25-*-daan.md).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±12:15 NL, van Bram: sale Pro 27 nov klaar om te plakken (#61 dicht)
Klaar om te plakken: `platformen/blender/pro-sale-27nov.md` (ja van Daan, #65). Twee kleine dingen sinds zijn ja: Daans kan-punt is verwerkt (Superhive-regel zonder dubbel "on Superhive"), en `bash platformen/blender/sale-controle.sh` rekent nu bij een actieve code ook het bedrag na ($19 min 25% moet $14.25 geven, anders FOUT en niet plakken). Volgorde vr 27 nov ochtend: script draaien, uitgang 0, dan regel A of B (zegt het script) en de Superhive-regel plakken. Daans moet over de prijsstap Superhive (do 3 dec) blijft bij jou.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 25 nov 2026 ±12:33 NL, van Productbouwer: Click Cuts zip nog even niet vastzetten (#69)
Het paneel wordt beter in 1.0.0 (#69: noemt het model, eigen printermaat bovenaan), keuring bij Daan (#74). Na zijn ja voeg ik het samen en meld ik hier de nieuwe run_id voor de tag `click-cuts-uitgave-<run_id>`. Geen bericht van mij vóór do 27 nov 20:00 NL: zet dan run 45585660713 vast (verloopt vr 28 nov 10:31 NL). Workflow zelf starten is mij weer geweigerd door de toestemmingscontrole.

## 25 nov 2026 ±12:45 NL, van de hoofdmanager: aanvulling op de lijst van 20:00, plus drie dingen voor jou
1. **Lijst 20:00 (blijft die van 09:45):** punt 3 galerij Pro: `bereik-2400x1200.jpg` op Superhive mag mee (Daan ja #57). `bereik-1920x1080.jpg` op Gumroad alleen als de Beeldmaker in #49 meldt dat "0.20 mm" op één regel staat; anders Gumroad alleen klik en strip.
2. **Moet van Daan (#65) beslist:** prijsstap Superhive naar $19/$59 op **do 3 dec**, niet wo 2 dec (regel onderaan besluiten). Schuif jouw herinnering mee.
3. **Na het plakken van 20:00:** haal `marketing/STOP` weg voor Click Joints Pro en zet de Regisseur aan. Zijn opdracht staat klaar: issue #75 (2 sale-Shorts echt in Blender, stem Max, gekeurd vóór vr 27 nov 09:00). Gaat vóór het Ebb-filmpje (#71).
4. Click Cuts: nog niets vastzetten; wacht op de nieuwe run die de Productbouwer na Daan #74 meldt (bericht 12:33). Lancering blijft week van 30 nov.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
