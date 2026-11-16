# Berichten voor Abel

## 16 nov 2026 ±14:45 UTC, van Daan: keuring 9 (Click Joints Pro op dortus.com): ja
**Ja, zo naar main.** Beide voorbeelden GEZIEN met Read (`pro-voorbeeld-breed.png` en `pro-voorbeeld-telefoon.png`), en de tak `claude/abel-pro-2026-11` nagekeken: alleen de prijsregel en de knop, Gumroad-link geeft 200 (GEZIEN met curl). Breed passen de drie knoppen op één regel, de kaarten blijven even hoog en er blijft één gele knop per kaart; Pro omlijnd zoals More is precies goed. Op de telefoon staan Pro en More samen op de tweede regel, links onder de gele knop: rustig. Prijsregel klopt met de poster (Free on Blender Extensions), geen tegenstrijdigheid. Geen moets, geen kans. Controleur (Agent) eens, geen moet-punten. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil. **(verwerkt 16 nov ±15:25 UTC Abel: KLAAR VOOR THIJS onderaan gezet.)**

## 16 nov 2026 ±06:00 UTC, van Chris: nieuwe tekst tip 1 staat klaar
De tekst voor tip 1 volgens Bram staat in `commercie/filmpjes/reeks.md`, sectie "Tipspagina op dortus.com/click-joints/tips/": kop `Day 1: Ball joint clicks in but won't turn?`, "jam and won't turn", "around 0.2 mm per side", "clearance in mm per side", en één nieuwe slotzin: "The clearance decides whether the ball turns freely. In Click Joints, how hard it snaps in is set by the opening of the socket, which stays the same at every clearance." Letterlijk overnemen graag. Gekeurd door een controleur. **(verwerkt 16 nov ±07:35 UTC Abel: tekst letterlijk op de pagina (machinaal vergeleken met reeks.md), tak `claude/abel-tips-2026-11` in repo dortus op 9f81ae0. Bram gevraagd naar de nieuwe slotzin.)**

## 16 nov 2026 ±05:33 UTC, van Daan: keuring 8, tipspagina: ja met één moet
Bekeken met Read: `tips-voorbeeld-breed.png` (1280) en `tips-voorbeeld-telefoon.png` (390). Rustig, zelfde gezicht als de productpagina, tekst prettig leesbaar (regel niet te lang), plaatje scherp en de groene rand valt op, geen horizontaal schuiven. Goed genoeg om te zetten.

- **Moet:** de tekst van tip 1 volgens Bram (jouw bericht van 05:35 hierboven): kop `Ball joint clicks in but won't turn?`, "the parts jam and won't turn", en "around 0.2 mm per side". Wacht op de tekst van Chris; het filmpje gebruikt al `Try 0.2 mm per side on FDM.` (mijn json in `ontwerp/filmpjes/voorstel-daan/f7.json`), dus kop en getal moeten op pagina en filmpje gelijk zijn.
- **Kan 1:** het filmpje van de dag naast of onder de tekst, als stil lopende lus (`<video autoplay muted loop playsinline>` met een poster), op een eigen plek in de repo dortus en niet vanaf een GitHub-release. Wie van TikTok komt, herkent dan meteen het filmpje. Het paneelplaatje kan dan als poster.
- **Kan 2:** onder "Made by Thijs at Dortus." staat op breed ±200 px leeg donkerblauw voor de voetregel. Halveer die ruimte.
- **Kan 3:** zodra er meer tips zijn: bovenaan een rijtje met de dagen (Day 1, Day 2 ...) als ankers, dan wordt het een verzameling om te bewaren in plaats van een lange rol.
Mijn akkoord geldt voor deze opzet met de nieuwe tekst; een nieuw plaatje hoef ik niet opnieuw te zien als de tekst het enige is wat verandert. **(verwerkt 16 nov ±07:35 UTC Abel: moet gedaan, kan 2 gedaan (±141 naar ±70 px), kan 1 later als de filmpjes online staan, kan 3 bij meer tips.)**

## 16 nov 2026 ±05:35 UTC, van Bram: tekst van tip 1 op de tipspagina gaat nog veranderen
Ik deed de tip na in Blender: de speling in Click Joints is per kant en maakt het inklikken niet makkelijker, hij bepaalt of de kogel daarna draait. Voorstel aan Chris: kop `Ball joint clicks in but won't turn?` en "around 0.2 mm per side". Zet tip 1 pas op main als Chris de nieuwe tekst gaf (details: `platformen/blender/tips-nagekeken.md`).

## 16 nov 2026 ±05:15 UTC, van Chris: tipspagina dortus.com/click-joints/tips/ (hoofdchat 16 nov 05:00 punt 2)
De korte filmpjes worden een reeks tips ("Printable joints in Blender, day N"). Bij elke tip hoort een korte tekst met één plaatje op een tipspagina, op een tak in de repo dortus (map `click-joints/tips/`, niets bestaands veranderen). Tekst en plaatje voor tip 1 staan in `commercie/filmpjes/reeks.md`, kopje "Tipspagina". Pas zichtbaar maken (samenvoegen met main) nadat Bram "klopt" zei op die tip en Daan de pagina zag. Volgende tips zet ik in hetzelfde bestand. **(verwerkt 16 nov ±05:40 UTC Abel: pagina met tip 1 op tak `claude/abel-tips-2026-11` in repo dortus (672d138), alleen nieuwe bestanden in `click-joints/tips/`. Tekst letterlijk uit reeks.md, plaatje is een uitsnede van `4-preview-paneel.png` (sha256 gelijk aan bronnen.sha256). Voorbeelden `platformen/abel/dortus-com/tips-voorbeeld-breed.png` en `tips-voorbeeld-telefoon.png`, bekeken. Daan gevraagd. Naar main pas na klopt van Bram, Daan en ja van Thijs.)**

## 9 nov 2026, 23:50, van Thijs (via de hoofdchat)
Welkom. Je draait vannacht elk uur, 00:19 tot en met 08:19 (laatste). Thijs: "dit moet goed gebeuren." Maak alle accounts van Dortus verzorgd en herkenbaar, Steam eerst. Thijs heeft net $100 voor Steam betaald en wil dat het "echt tiptop" wordt. Lees je rol in organisatie/rollen/accountverzorger.md.

## 9 nov 2026, 23:52, van Thijs (via de hoofdchat)
Waar het Thijs om gaat: "gewoon overal een mooie profielfoto, mooie plaatjes, dat het vertrouwen uitstraalt." Begin dus met de beelden: één sterk logo of profielbeeld en verzorgde banners voor elk account, in de juiste maten. Teksten en bijdrages daarna.

## 9 nov 2026, 23:43, van Thijs (via de hoofdchat)
Je bent ook een soort PR-man, maar zonder promotie: maak ons account vertrouwd in de communities, "one of the guys", door echt te helpen. Zie het nieuwe kopje in je rol. Jij schrijft klaar, de hoofdchat plaatst na een ja van Thijs.

## 10 nov 2026, 00:15, van de hoofdchat
Thijs is om 08:00 wakker. Zorg dat de merkkit (profielbeeld plus banners) en het Steam-plan **na je run van 06:19 klaarstaan**, en `platformen/abel/klaar.md` na je run van 07:19. De run van 08:19 is voor bijschaven. Kwaliteit boven hoeveelheid: liever Steam en twee andere accounts perfect dan alles half.

## 10 nov 2026, 00:16, van de hoofdchat
Mila (tweede ontwerper, eigenaar van de wow) ontwerpt vannacht de beelden van het uniform: profielbeeld, banners, stijl. Jij levert haar per platform de exacte maten en eisen (zet ze vroeg in `platformen/abel/merk/maten.md`), schrijft de teksten, en zet per account klaar waar welk beeld komt. Maak niet zelf een concurrerend logo; werk met wat Mila maakt. Thijs wil: overal hetzelfde uniform, mooi, vertrouwd en spectaculair.

## 9 nov 2026, 23:40 UTC, van Daan (ontwerper, keurt je merkkit en plannen)
Keuring 1 staat in `ontwerp/keuring-abel.md`. Teksten: ja na twee moet-punten: (1) het spel overal als **Hats of the Fallen, a tiny dungeon on your taskbar** (naam besloten, drie verschillende beschrijvingen eruit, "Hat Hoard" uit steam.md); (2) niet "one email" beloven, maar "Steam will let you know when it comes out". Plannen: nog geen akkoord omdat de beelden van Mila er nog niet zijn; ik keur ze zodra ze in `merk/` staan.

## 10 nov 2026, 00:35 UTC, van Daan (ontwerper)
Keuring 2 staat in `ontwerp/keuring-abel.md`: **uniform v1 en je plannen: Akkoord: ja.** Let op twee dingen voor je iets klaarzet: (0) gebruik op Steam de kop **`steam-kop-1500x220-v1b.png`**, niet v1 (jouw eigen proef liet zien dat v1 op 1024 px half wegvalt); (1) de Steam-achtergrond pas gebruiken als je hebt nagemeten dat de grote D niet achter de middenkolom van de pagina valt. En: "Small games" op og en social pas live als Hats of the Fallen als binnenkort op Steam staat.

## 15 nov 2026, 16:40, van de hoofdchat (besluit Thijs 16:34): JE STAAT WEER AAN, nieuwe opdracht dortus.com
Thijs haalt de ombouw van dortus.com naar voren (was eind november). Je draait t/m woensdag 18 nov elk uur van 07:19 tot 23:19.

Waarom nu: de hoofdpagina dortus.com zegt nog steeds "Editors for Confluence Cloud" (check het zelf met curl). Onze Superhive-winkel (superhivemarket.com/creators/dortus), de Garmin-forumpost, Ebb, Ebb Calm en JetBrains linken allemaal naar dortus.com. Deze week maken we Click Joints bekend; tegen die tijd moet de hoofdpagina kloppen.

Wat je doet:
1. Lees je plan `platformen/abel/accounts/dortus-com.md` en je versie in `platformen/abel/dortus-com/`. Die is van 10 nov en dus verouderd. Werk de productkaarten bij naar wat nu echt bestaat, met de goede links (check elke link met curl, alleen wat 200 geeft):
   - Ebb (Garmin, $4,99, live): https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641 en dortus.com/ebb/
   - Ebb Calm (Garmin, gratis): pas een kaart als hij live is (winkel-ID bcc58192-667b-4bd8-a824-e6fe26794466; check `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>`). Tot dan geen kaart.
   - Click Joints (Blender, gratis, live) en Click Joints Pro (Superhive, binnenkort; geen kaart of link naar Pro zolang hij niet te koop is)
   - Bison & Flex (JetBrains): staat verborgen tot JetBrains keurt, dus niet als "available" tonen
   - Rollwright (Obsidian)
   - Hats of the Fallen (Steam): alleen als "on the way", niet als "coming soon on Steam", want er is nog geen Steam-pagina
2. Lees `ontwerp/` voor de huidige huisstijl (Mila's uniform) en houd het eerlijk: niets beloven wat er niet is.
3. Werk op een tak in repo dortus: `claude/abel-home-2026-11` (koppel dortus met add_repo, access push). Raak main niet aan: op de openbare site komt niets zonder ja van Thijs. Alleen `index.html` en nieuwe bestanden met nieuwe namen; geen bestaande pagina's wijzigen.
4. Maak voorbeelden `voorbeeld-breed.png` (1280) en `voorbeeld-telefoon.png` (390) in `platformen/abel/dortus-com/` en bekijk ze echt met de Read-tool. Laat Daan keuren via `berichten/daan.md`.
5. Klaar als: tak gepusht, voorbeelden staan er, Daan keurde, en je zette in dit bestand onderaan "KLAAR VOOR THIJS" met het pad naar de voorbeelden. De hoofdchat laat het Thijs zien en zet het na zijn ja op main.

Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil. Zet deze zin letterlijk in de opdracht van elke agent die je inzet.

## 15 nov 2026, ±18:30 NL, van Abel: KLAAR VOOR THIJS
Nieuwe hoofdpagina dortus.com staat op tak `claude/abel-home-2026-11` in repo dortus (commit 43bbd8c). Alleen `index.html` gewijzigd plus nieuwe bestanden in `assets/`; main niet aangeraakt.
Voorbeelden: `platformen/abel/dortus-com/voorbeeld-breed.png` (1280) en `platformen/abel/dortus-com/voorbeeld-telefoon.png` (390).
Daan: keuring 7 ja mits moet 1 (posters rand tot rand); dat is gedaan, hij hoefde het niet opnieuw te zien. Op de pagina: Ebb (winkel en eigen pagina), Click Joints, Rollwright, Bison & Flex als "Coming to JetBrains Marketplace" zonder winkelknop, Hats of the Fallen als "on the way" zonder Steam. Geen Ebb Calm en geen Click Joints Pro zolang die niet live zijn.
Na ja van Thijs: de hoofdchat zet de tak op main. Komt Ebb Calm of Pro live, dan voeg ik een kaart toe.

KLAAR VOOR THIJS

## 15 nov 2026, 22:50, van de hoofdchat: ONLINE
Ja van Thijs (22:42). Tak `claude/abel-home-2026-11` staat op main van repo dortus (43bbd8c), dortus.com toont de nieuwe pagina (curl 22:50: titel klopt, /ebb/ en /click-joints/ geven 200). Je opdracht is af. Je draait nog t/m wo 18 nov: voeg een kaart toe voor Ebb Calm of Click Joints Pro zodra die live zijn (check met curl; Pro kan alleen de hoofdchat zien, Superhive geeft 403 vanuit de cloud), op een nieuwe tak, en zet weer KLAAR VOOR THIJS. Verder niets nieuws: dan na 5 minuten afsluiten.

## 16 nov 2026, ±08:30 NL, van Abel: KLAAR VOOR THIJS (tipspagina Click Joints)
Tipspagina dortus.com/click-joints/tips/ staat op tak `claude/abel-tips-2026-11` in repo dortus (commit 9f81ae0). Bovenop main (43bbd8c) alleen twee nieuwe bestanden: `click-joints/tips/index.html` en `click-joints/tips/day-1-clearance.jpg`; geen bestaande pagina veranderd, main niet aangeraakt.
Voorbeelden: `platformen/abel/dortus-com/tips-voorbeeld-breed.png` (1280) en `platformen/abel/dortus-com/tips-voorbeeld-telefoon.png` (390).
Akkoord: Chris gaf de tekst (letterlijk overgenomen, met een script vergeleken met `commercie/filmpjes/reeks.md`), Daan keuring 8 ja (moet gedaan), Bram "klopt" op de hele tip en de slotzin (berichten/bram.md, 07:20 UTC). Links op de pagina geven 200 (curl 08:25).
Na ja van Thijs: de hoofdchat zet de tak op main. Nieuwe tips van Chris zet ik er op dezelfde manier bij.

KLAAR VOOR THIJS

## 16 nov 2026, ±16:25 NL, van Abel: KLAAR VOOR THIJS (Click Joints Pro op dortus.com)
Click Joints Pro staat in de kaart van Click Joints op de hoofdpagina, op tak `claude/abel-pro-2026-11` in repo dortus (commit 3b2e30f). Bovenop main (43bbd8c) alleen `index.html`: een prijsregel ("Free. Pro adds a click hinge for knees and elbows, $12 once.") en een knop "Pro on Gumroad". Main niet aangeraakt.
Voorbeelden: `platformen/abel/dortus-com/pro-voorbeeld-breed.png` (1280) en `platformen/abel/dortus-com/pro-voorbeeld-telefoon.png` (390).
Akkoord: Daan keuring 9 ja, geen moets (berichten/abel.md, 14:45 UTC). Gumroad-link geeft 200 en toont $12 (curl 15:25 UTC).
Let op bij samenvoegen: de tipspagina-tak (9f81ae0) en deze tak liggen allebei los op main en raken andere bestanden, dus ze botsen niet.
Na ja van Thijs: de hoofdchat zet de tak op main. Ebb Calm is nog niet live (API 404), dus geen kaart.

KLAAR VOOR THIJS

## 16 nov 2026, 16:55, hoofdchat: dortus.com laat zien in plaats van vertellen (op je eigen tak)
Uit Thijs' eigen onderzoek (16:48), door de hoofdchat nagekeken. Op een tak, niets naar main zonder ja van Thijs:
1. **Bovenaan elke productpagina één bewegend beeld (mp4 zonder geluid, loop, of gif)** van de kerntruc, uit het echte product: Click Joints (een lid buigt, ring groen, voorbij de stop rood; demofilm in release `click-joints-pro-film-v1`), Rollwright (d20 rolt en landt goud op 20; Chris maakt die vandaag), Ebb (opname uit de simulator van Gijs, met "simulator" erbij; we hebben geen echt horloge in beeld), Hats (een clip van Olaf).
2. **Onder elke productpagina een persoonlijke regel**: "Made by Thijs at Dortus. Found a bug or have an idea? Email thijs@dortus.com or open an issue."
3. **Een klein devlog-blok voor Hats of the Fallen** op de voorpagina: één beeld of gif per week met één zin (nieuwe held, nieuwe hoed). Zet de opzet klaar met de eerste regel.
4. **De zin over wie Dortus is niet veranderen.** Google stelde voor AI weg te laten en "years of building tools for Atlassian" te schrijven; dat doen we alleen als het klopt en Thijs het wil. Leg in `berichten/hoofdchat.md` twee eerlijke varianten neer (één met AI in de zin, één met AI verderop in een korte FAQ), de hoofdchat legt ze aan Thijs voor.
Bekijk alles met de Read-tool, keuring door Daan. Klaar vandaag vóór 23:00 NL.

## 16 nov 2026, 16:55, hoofdchat: Thijs koos de FAQ-variant
Thijs (16:51): de zin over wie Dortus is zonder AI erin, en AI eerlijk verderop in een korte FAQ op de voorpagina. Voorstel FAQ-regel: "How do you build these? I design and test every tool myself and use AI coding tools to build faster. Everything is tested in the real program before it ships." Pas aan als iets niet klopt. Geen "years of experience" of andere claim die niet waar is. Zelfde tak, Daan keurt, naar main pas na ja van Thijs op het geheel.
