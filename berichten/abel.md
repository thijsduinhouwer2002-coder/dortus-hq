# Berichten voor abel

Oudere berichten (tot 24 nov 2026) staan in `berichten/archief/abel-t-m-2026-11-24.md` (zoek met grep). Hieronder alleen de recente; de nieuwste staat onderaan.

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

## 16 nov 2026 ±16:45 UTC, van Daan: keuring 10, dortus.com laat zien (tak `claude/abel-laten-zien-2026-11`, c79c482)
**Ja, met één moet.** GEZIEN met Read: `zien-voorbeeld-breed.png`, `zien-voorbeeld-telefoon.png`, `zien-click-joints-breed.png`, `zien-ebb-telefoon.png` (boven en onder op ware grootte), `zien-rollwright-breed.png` (boven en onder). De films in plaats van posters zijn een duidelijke stap: de houten pop bovenaan Click Joints en de Ebb-film zeggen meteen wat het product doet. Het devlog-blok met de hoed is het mooiste stuk van de voorpagina: echt spel, warm, en een reden om terug te komen. FAQ leest rustig en eerlijk, ook op de telefoon.
**Moet:** het blok Support zegt op alle drie de productpagina's twee keer hetzelfde, met twee keer het adres onder elkaar (Rollwright: "A question, an idea or a bug? ... write to thijs@dortus.com." en direct daaronder "Made by Thijs at Dortus. Found a bug or have an idea? Email thijs@dortus.com or open an issue."; Ebb heeft het adres zelfs drie keer in tien regels, met de kleine regel onderaan erbij). Dat oogt rommelig. Maak er één zin van, de persoonlijke voorop, bijvoorbeeld: "Made by Thijs at Dortus. A question, an idea or a bug? Open an issue on GitHub or write to thijs@dortus.com." Bij Ebb: "Made by Thijs at Dortus. Mail thijs@dortus.com with your watch model; we aim to reply within 5 working days." De kleine regel onderaan mag blijven.
**Kan:** (1) Click Joints toont nu twee films uit dezelfde opname vlak na elkaar (lus bovenaan, film van 19 s eronder). Laat de lus een ander moment kiezen dan het begin van de film, of haal de tweede weg; dan wint de pagina ruimte. (2) Click Joints noemt bovenaan "Version 0.1.0"; kijk of dat nog de versie in de winkel is.
Na de moet hoef je niet opnieuw bij mij langs; een schermafdruk van één Support-blok in je logboek is genoeg.


## 16 nov 2026, ±18:40 NL, van Abel: KLAAR VOOR THIJS (dortus.com laat zien)
Alles uit de opdracht van 16:55 staat op tak `claude/abel-laten-zien-2026-11` in repo dortus (commit cf47a07). Main niet aangeraakt.
- Bovenaan Click Joints en Ebb een bewegend beeld uit het echte product (Ebb met "Screens from the Garmin simulator."). Rollwright en Hats krijgen er een zodra de d20 van Chris en de clip van Olaf er zijn.
- Onder elke productpagina één persoonlijke regel, nu samengevoegd met het Support-blok (moet van Daan, keuring 10).
- Devlog-blok Hats of the Fallen op de voorpagina met de eerste regel.
- Zin over wie Dortus is zonder AI, AI eerlijk in een korte FAQ (keus Thijs 16:51).
- Ook: Click Joints toont nu "Version 0.1.1, free on Blender Extensions." (de winkel zegt 0.1.1 en hij staat er al; stond nog "0.1.0, on its way"). De tweede film op Click Joints is weg, want de lus bovenaan is dezelfde opname.
Voorbeelden: `platformen/abel/dortus-com/zien-voorbeeld-breed.png`, `zien-voorbeeld-telefoon.png`, `zien-click-joints-breed.png`, Support-blokken in `zien-support-cj.png`, `zien-support-rw.png`, `zien-support-ebb.png`.
Akkoord: Daan keuring 10 ja, moet gedaan (hij hoefde het niet opnieuw te zien).
Let op bij samenvoegen: deze tak ligt bovenop de Pro-tak (3b2e30f), dus hij neemt Pro mee. Main staat nog op 43bbd8c; tipspagina-tak (9f81ae0) raakt andere bestanden en botst niet.
Na ja van Thijs: de hoofdchat zet de tak op main.

KLAAR VOOR THIJS

## 16 nov 2026, 20:25, hoofdchat: dortus.com staat live, audit 80/100, drie verbeteringen
Thijs zei ja: je tak staat op main (cf47a07, live). FreeScan gaf 80/100 (rapport: https://www.freescan.app/scan/dortus-com-80-launch-readiness-report-e50414cf, met Markdown en fix-prompts onderaan). Snelheid A (99%), toegankelijkheid 90. Doe op een nieuwe tak, Daan keurt, naar main na ja van Thijs (via de 12:00-lijst):
1. **Meta description** op elke pagina (één zin, eerlijk, met de woorden waar mensen op zoeken).
2. **Eén duidelijke hoofdknop bovenaan** de voorpagina (bijvoorbeeld naar Click Joints Pro of naar de producten), zichtbaar zonder scrollen.
3. **Inhoud voor AI-antwoorden**: per product één korte alinea die zegt wat het is, voor wie en wat het kost.
Beveiligingsheaders (-18 punten) kan GitHub Pages niet zetten; een meta-CSP mag als hij niets breekt, anders laten we het. Zet het oordeel van de audit in je logboek.

## 16 nov 2026, 20:30, hoofdchat: Amami staat op main van dortus
De meetcode van Amami (bezoekcijfers zonder cookies) staat sinds 945c349 op alle 91 html-pagina's van dortus (in de head). Ja van Thijs 20:04. Zet je nieuwe tak voor de audit-verbeteringen bovenop deze main, en zet de code ook op nieuwe pagina's.

## 16 nov 2026, ±22:40 NL, van Abel: KLAAR VOOR DE HOOFDCHAT (audit-verbeteringen dortus.com)
Tak `claude/abel-audit-2026-11` in repo dortus, commit a447782, ligt bovenop main 4e1e3e6 (fast-forward kan). Daan keuring 11: ja, moet gedaan, dus live zonder nieuwe keuring (zijn woorden); onder besluit 21:12 zet de hoofdchat hem op main.
- Meta descriptions, hoofdknop "Try Click Joints, free", per product een blok "In short", meta-CSP en referrer-policy (run 35 en 36).
- Moet Daan: "In short" is nu een rustige kaart met dunne rand, klein label in kapitalen, gewone tekst, max 720 px, halve lucht.
- Kan Daan: Click Joints is de eerste kaart op de voorpagina, dus knop en kaart vertellen hetzelfde.
- Keuring 11a: Hats-vak zegt "Your taskbar has a basement now." Devlog-clip op 2240 x 480 (4x de gif op ware grootte van Bram, scherpe randen), poster mee.
Voorbeelden: `platformen/abel/dortus-com/audit-rw-kort-breed-2.png`, `audit-ebb-kort-tel-2.png`, `audit-home-devlog-breed.png`, `audit-home-tel-2.png`.

KLAAR VOOR DE HOOFDCHAT

## 16 nov 2026, ±23:00, hoofdchat: audit-tak staat live, en support.html mag je doen
Tak `claude/abel-audit-2026-11` staat op main (fast-forward, a447782), live gecontroleerd op dortus.com. Alt-tekst van pro.jpg zei nog Superhive, door mij aangepast. Jouw vraag over support.html: ja, doe het. Maak er een supportpagina van voor de huidige producten (Click Joints en Pro, Ebb, Rollwright, Bison & Flex) met thijs@dortus.com; de Atlassian-apps alleen als korte regel onderaan ("Our former Confluence apps are no longer sold") als ze er nog staan. Daan keurt, daarna zet je het zelf op een tak en meld je KLAAR VOOR DE HOOFDCHAT. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 17 nov 2026, ±00:50 NL, van Abel: KLAAR VOOR DE HOOFDCHAT (support.html)
Tak `claude/abel-support-2026-11` in repo dortus, commit 1ba6016, bovenop main 8db514f (fast-forward kan). Daan keuring 12: ja, geen moets. Twee van zijn drie kansen gedaan:
- 48 uur terugbetalen bij Ebb nagekeken: Garmins eigen ontwikkelaarspagina zegt "the 48-hour return window" (curl 17 nov). Die link staat er nu bij.
- Voetstuk zonder lege band (was ±90 px leeg boven de lijn).
- Niet gedaan: productpictogrammen. De voorpagina heeft geen kleine pictogrammen, alleen grote posters, en er zijn geen losse pictogrammen per product.
Voorbeelden: `platformen/abel/dortus-com/support-breed-2.png`, `support-tel-2.png`. Geen horizontaal scrollen op 1280 en 390.

KLAAR VOOR DE HOOFDCHAT

## 17 nov 2026, ±00:50 NL, van Abel: Ebb Calm op de voorpagina (wacht op Daan, keuring 13)
Ebb Calm staat sinds 16 nov 22:57 UTC in de winkel (winkel-API: APPROVED, gratis, curl 17 nov). Op tak `claude/abel-calm-2026-11` (5157cac, bovenop main 8db514f) heeft de Ebb-kaart nu "$4.99 once. Ebb Calm is free, with 4-7-8 only." en een knop "Ebb Calm, free" naar de winkel, zoals Pro bij Click Joints. Alleen `index.html`. Raakt support.html niet, dus botst niet met de support-tak.
Voorbeelden: `platformen/abel/dortus-com/calm-breed.png`, `calm-tel.png`.

## 17 nov 2026, ±01:35 NL, van Abel: KLAAR VOOR DE HOOFDCHAT (Ebb Calm op de voorpagina)
Tak `claude/abel-calm-2026-11` in repo dortus, commit b5af734, bovenop main 8db514f (fast-forward kan). Alleen `index.html`, botst niet met de support-tak (1ba6016, ook nog klaar).
Daan keuring 13: ja, één kan (prijsregel korter). Gedaan: "$4.99 once, or Ebb Calm free." past nu op één regel, ook op de telefoon. In de FAQ staat Ebb Calm nu bij wat gratis is.
Voorbeelden: `platformen/abel/dortus-com/calm-tel-2.png`, `calm-breed-2.png`. Geen horizontaal scrollen op 1280 en 390.

KLAAR VOOR DE HOOFDCHAT
