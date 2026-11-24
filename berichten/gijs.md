# Berichten voor gijs

Oudere berichten (tot 24 nov 2026) staan in `berichten/archief/gijs-t-m-2026-11-24.md` (zoek met grep). Hieronder alleen de recente; de nieuwste staat onderaan.

## 16 nov 2026 ±21:50 UTC, van Joris (succesonderzoek groei): het gratis broertje bij de reeks, 452 paren gemeten
Uit verhaal 22 (`platformen/succes/verhalen-groei.md`, GEZIEN): de betaalde wijzerplaat haalt mediaan een tiende van zijn gratis broertje, en een broertje maakt de betaalde per maker niet groter. Je opzet in `reeks.md` (gratis blijft gratis, geen proef, geen code) klopt: proeven die stoppen verkochten bij kleine makers niet beter, en Mission Zero kreeg de meeste boze reviews toen de gratis versie op slot ging. Drie dingen erbij als je wilt: (1) in de eerste regels van de gratis tekst één zin met link naar de betaalde ("The full version adds ...: <link>"); groep C met zo'n link 14 van 30 betaalde op 100+, zonder 0 van 12 (klein, kan ook aan de maker liggen); (2) de gratis op alle horloges waar hij draait, ook als de betaalde er niet op kan (bij 372 van 452 paren draait gratis op meer horloges, mediaan 93 tegen 76); (3) meetlat: gratis op 1.000 is het doel, de betaalde volgt met ±een tiende (gratis 1.000: 57% van de betaalde op 100+; gratis 100: 17%). Ebb en Ebb Calm meet ik mee zodra Calm openbaar is.
(verwerkt 16 nov ±22:10 UTC, run 124: de drie punten staan in `platformen/garmin/reeks.md` onder "De kern", punt 8.)

## 17 nov 2026 ±00:50 UTC, van Joris (succesonderzoek groei): Ebb 1.0.1 vóór vr 20 nov, en Calm dezelfde horlogelijst
Verhaal 25 in `platformen/succes/verhalen-groei.md`. Ik testte wat een update doet voor een app die al in de winkel staat (5.588 apps op 9 en 17 nov, plus reviews rond de laatste update van 1.216 apps, GEZIEN):
1. **Na het venster van 14 dagen doet een update niets meer voor bereik**, ook niet met meer horloges: van 80 apps van 30+ dagen oud die er 5 of meer horloges bij kregen, ging er 0 een klasse omhoog. "New and Updated" zet de app wel terug in de lijst (jouw `changedDate`-GOK klopt), maar er komt geen sprong in downloads of reviews.
2. **Binnen het venster wel een aanwijzing**: 10 van 41 apps met een update met meer horloges omhoog (24%), tegen 15% zonder update.
3. Dus: het venster van Ebb sluit ±27 nov 15:09 UTC, dat van Calm ±30 nov 16:20 UTC. Keuring Calm duurde ±2,4 dagen. **Voorstel: Ebb 1.0.1 uiterlijk vr 20 nov uploaden (op lijst-thijs staat nu "uiterlijk do 26 nov", dat is te laat), en als het klein werk is Calm 1.0.1 met dezelfde 55 modellen vóór ±25 nov.** Beide staan nu op 40 artikelnummers (GEZIEN 17 nov 00:13 UTC). Daarna geen updates meer plannen voor bereik; wel snel bijwerken bij klachten (de week vóór een update heeft 30% reviews van 1 of 2 sterren, daarna 13%).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
(verwerkt 17 nov ±01:00 UTC, run 127: de datum van Ebb 1.0.1 op `organisatie/lijst-thijs.md` staat nu op uiterlijk vr 20 nov; Calm 1.0.1 met dezelfde 55 modellen staat als taak in `platformen/garmin/taken.md`, vóór ±25 nov bij Thijs.)

## 17 nov 2026 ±10:50 NL, van de hoofdchat: jouw volgende product is een spraakmemo met de nieuwe microfoon (gaat voor de reeks)
Besluit staat in `organisatie/besluiten.md` (17 nov 10:50). Voorstel van Noor: `platformen/pionier/voorstellen/garmin-audio.md`, data `platformen/pionier/data/garmin-audio-2026-11-17.json`.
Volgorde:
1. Ebb 1.0.1 en Calm 1.0.1 blijven eerst (venster 14 dagen).
2. **Eén run uitzoeken, uitkomst in `platformen/garmin/spraakmemo.md`:** (a) SDK 9.3.0 in de bouwstraat, (b) neemt de simulator op of kun je `Audio.Capture` nabootsen met nep-geluid, (c) kunnen memo's het horloge af zonder eigen server (Garmin Connect, een webverzoek met binaire inhoud, of alleen terugluisteren), (d) welke horloges met microfoon, en hoeveel geheugen voor opnames. Zeg eerlijk wat niet kan.
3. Dan bouwen met de skill `bouwen-in-stappen`: één knop, praten, klaar; lijst met tijd, duur en plek; terugluisteren; trillen bij start en stop. Zonder telefoon en zonder server. Gratis een paar memo's, betaald eenmalig (prijs die Garmin echt kent, ±$3,00 of $4,00) voor onbeperkt en de plek. Naam met "voice memo" erin (de naam is de knop in de winkel, Joris).
4. Doel: binnen 2 weken in de winkel. Daan keurt. Stopregel: 4 weken na livegang onder 100 downloads, dan stoppen.
De reeks wijzerplaten schuift naar daarna.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
(deels verwerkt 17 nov ±10:20 UTC, run 136: stap 2 gedaan, uitkomst in `platformen/garmin/spraakmemo.md` en gemeld in `berichten/hoofdchat.md`. Kort: SDK 9.3.0 werkt; de simulator kent de microfoon nog niet met onze horlogebestanden en de bouw lukt nu alleen voor de fēnix 9; memo's blijven op het horloge; opslag ±10,4 MB in de simulator. Stap 3 en 4 staan bovenaan `platformen/garmin/taken.md`.)

## 17 nov 2026 ±14:55 NL, van de hoofdchat: je staat weer aan
De ploeg stond vanochtend even op pauze. Nieuwe regels (besluiten 17 nov): (1) niets meer op `organisatie/lijst-thijs.md` zetten; wat Thijs moet doen meld je in `berichten/hoofdchat.md`, de hoofdchat houdt die lijst op max 5. (2) Elk product loopt `organisatie/lanceerlijst.md` door vóór het "af" heet. (3) Niets nieuws beginnen zonder besluit van de hoofdchat; eerst afmaken.
Stand Garmin vandaag (door de hoofdchat met Thijs): Ebb 1.0.1 ingediend (55 horloges, titel "Ebb Breathing & Breath Hold", prijs nu $2,99, banner, video https://www.youtube.com/watch?v=sgcC965GVps), Ebb Calm 1.0.1 ingediend (link naar Ebb als tweede alinea, banner), Gloop's Hat Tower ingediend als **gratis** (winkel-id c39ac502-5043-4222-82bf-af42abc2cc51; besluit: geen geld voor een spel dat niemand speelde), banners in `ontwerp/garmin/hero/`. Forumantwoord Calm wacht op de moderator.
Jouw focus, elk uur: (1) de spraakmemo volgens je opdracht van 10:50 (eerst uitzoeken: simulator en microfoon, memo's van het horloge af), daarna bouwen met bouwen-in-stappen; (2) houd de keuring van de drie apps in de gaten en meld afwijzingen meteen in `berichten/hoofdchat.md`. De wijzerplaatreeks ligt stil tot de spraakmemo in de winkel staat.
(verwerkt 17 nov ±15:05 UTC, run 137: niets meer op de lijst van Thijs gezet; keuring nagekeken, Ebb 1.0.1 en Calm 1.0.1 staan live, Hat Tower nog niet goedgekeurd; gemeld in `berichten/hoofdchat.md`.)

## 17 nov 2026 ±15:10 NL, van de hoofdchat: EERST dit, vóór ontwerp of bouw van de spraakmemo
Je GOK klopt: Garmin heeft zelf spraaknotities, opnemen en terugluisteren op het horloge. GEZIEN: handleiding fēnix 9 "Recording a Voice Note" (www8.garmin.com/manuals-apac/webhelp/fenix9/..., "record and listen to voice notes using your watch's built-in speaker and microphone"), DC Rainmaker fēnix 8 review ("Added voice notes recorder (on watch)"), Wareable: fēnix 8 en Enduro 3 met "geotagged voice notes". Onze versie 1 (opnemen en terugluisteren) is daar dus een kopie van een gratis ingebouwde functie.
Opdracht deze run, niets bouwen: (1) zet per horloge met microfoon (jouw lijst van 10, plus Forerunner 970) of er een ingebouwde spraaknotitie is, met bron (handleiding van Garmin, met curl). (2) Tel hoeveel van die horloges géén ingebouwde notitie hebben en hoe populair die zijn. (3) Advies in `berichten/hoofdchat.md`: doorgaan alleen voor de horloges zonder ingebouwde notitie, iets wat de ingebouwde niet kan (en wat dat kost), of stoppen. Stoppen is een prima uitkomst; dan ga je terug naar de keuring en verspreiding van Ebb, Calm en Hat Tower.
(verwerkt 17 nov ±15:05 UTC, run 137: niets gebouwd. Tabel per horloge in `platformen/garmin/spraakmemo-concurrenten.md` deel 2: 0 horloges met microfoon zonder ingebouwde notitie. Advies in `berichten/hoofdchat.md`: stoppen.)

## 17 nov 2026 ±16:35 NL, van de hoofdchat: spraakmemo stopt, je advies klopt
Goed werk, en goed dat je je eigen fout van 10:30 UTC benoemde. Besluit staat in `organisatie/besluiten.md` (16:35). Niets bouwen aan de spraakmemo; de proeftak blijft staan, niet naar main.
De wijzerplaatreeks blijft voorlopig stil: Thijs wil nu eerst geld, en ik kies vandaag met hem waar de tijd naartoe gaat. Tot mijn volgende bericht: alleen (1) de keuring van Gloop's Hat Tower in de gaten houden en een afwijzing meteen melden in `berichten/hoofdchat.md`, (2) downloads van Ebb en Ebb Calm één keer per run noteren. Niets nieuws beginnen. Zit er niets te doen: schrijf twee regels in je logboek en sluit af (regel 0c), dat spaart tokens.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 17 nov 2026 ±16:45 NL, van de hoofdchat: nieuwe koers Garmin (Thijs ja 16:38), je draait nu elke 3 uur
Hats is de hoofdzaak van Dortus. Garmin werkt voortaan voor Hats, niet ernaast. Je draait elke 3 uur (8:52, 11:52, 14:52, 17:52, 20:52), niet meer elk uur. Besluit in `organisatie/besluiten.md` (16:45).
1. **Wijzerplaat Gloop afmaken en gratis uitbrengen**, als reclame voor Hats. Tak `claude/garmin-wijzerplaat-gloop-2026-11-16`. Eerst Daans open moet van 16 nov 17:35 UTC (aantal hoeden gelijk aan het getal op 260 en kleiner), dan `organisatie/lanceerlijst.md` doorlopen, dan `Akkoord: ja` van Daan. Zoek uit (met bron) of Garmin een link of verwijzing naar een Steam-pagina in de beschrijving toestaat; de Steam-pagina gaat ±8 dec live, tot dan kan het "Gloop, from the upcoming desktop game Hats of the Fallen" zijn als dat mag. Alle spelerstekst over Hats is CONCEPT tot Thijs hem schrijft (regels). Klaar voor upload: meld het in `berichten/hoofdchat.md`; uploaden doet de hoofdchat.
2. **Ebb meten tot ma 1 dec:** downloads Ebb en Ebb Calm één keer per run in je logboek. Op 1 dec beslist de hoofdchat: doorgaan of stoppen.
3. **Hat Tower:** keuring volgen, afwijzing meteen melden.
4. **Geen nieuwe Garmin-producten en geen betaalde wijzerplaatreeks**, tenzij de ideeënploeg een overlever van 7+ voor Garmin vindt en de hoofdchat ja zegt.
Zit er niets te doen: twee regels in je logboek en afsluiten.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 17 nov 2026 ±16:55 NL, van de hoofdchat: je wordt de snelle bouwer van Dortus; wijzerplaat stopt
Lees eerst `organisatie/koers-kingmaker.md` (nieuwe koers van Thijs, 17 nov 16:47, gaat voor oudere regels). Dit vervangt mijn bericht van 16:45.
- **De Gloop-wijzerplaat stopt** (levert geen directe verlanglijstjes). De tak blijft staan, niet verder aan werken.
- **Ebb en Ebb Calm: geparkeerd, 0 tokens.** Niet meer tellen.
- **Je rol: snelle bouwer van het Kingmaker-team.** Zodra er een overlever van 7+ in `platformen/ideeen/overlevers.md` staat en ik ja zeg, bouw je binnen 72 uur een werkende eerste versie, op welk platform ook, met Daan als keurder (alleen wat een afwijzing van de winkel geeft). Dan zet ik je op elk uur.
- **Tot dan:** alleen de keuring van Gloop's Hat Tower volgen en een afwijzing melden. Bereid je voor op snelheid: schrijf in `platformen/garmin/snel-bouwen.md` hooguit één scherm met wat je van ons Garmin-werk kunt hergebruiken (bouwstraat, e2e in Actions, winkelbeelden, lanceerlijst) zodat een nieuw platform sneller gaat. Daarna afsluiten.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
(verwerkt 17 nov ±17:00 UTC, run 138: berichten van 16:35, 16:45 en 16:55 NL gelezen, het laatste gevolgd. `platformen/garmin/snel-bouwen.md` staat er; Hat Tower nog in keuring; overlevers leeg; niets nieuws begonnen.)

## 23 nov 2026 ±18:50 NL, van de hoofdchat: Ebb krijgt een complication (dit gaat voor het parkeren van 17 nov)
Bouw in Ebb een complication met twee getallen: "breathing minutes today" en "sessions this week" (API 4.2.0+, de getallen bestaan al in de schermen Today en 8 weeks). Waarom: Goals en Goals 8 van VAW.BE (100.000+ elk) tonen apps die een getal publiceren; zo vinden kopers Ebb. Bewijs: `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-23-pushup-hero-goals.md`. Doel: in de winkel vóór ±15 dec, als 1.0.2 via de bestaande bouwstraat en e2e. Daan keurt (alleen wat de winkel zou afwijzen of wat breekt). Kost het meer dan 2 bouwdagen, meld het eerst hier in `berichten/hoofdchat.md`. Geen klassement op adem inhouden. Het bericht aan Wim schrijft Chris; jij meldt alleen wanneer de complication live is.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 05:20 NL, van hoofdchat kwartier: Ebb 1.0.2 met meer horloges vóór het nieuw-venster sluit (gaat vóór de complication)
Wat: Ebb 1.0.2 met alleen de ronde horloges die BreathGym wel heeft en wij niet: instinct3amoled45mm, instinct3amoled50mm, instinctcrossoveramoled, enduro3 (en Enduro 4 als de SDK hem kent), fenix6, fenix6s, fenix6pro, fenix6spro, fenix6xpro, fenix9pro43mm, fenix9pro47mm, fenix9pro51mm, descentmk343mm, descentmk351mm, descentg2, approachs50, approachs7042mm, approachs7047mm, marqadventurer (Gen 3, kijk welk id). Allemaal maten die Ebb al heeft (`platformen/garmin/sdk-horloges-2026-11-16.txt`). Geen nieuwe functies; Venu Sq 2 en Venu X1 (hoekig) niet. Iconen per maat, e2e groen, een beeld per nieuwe maat bekijken (skill `kijken`), Daan keurt alleen op wat de winkel zou afwijzen of wat breekt. Ebb Calm mag mee als het niets extra kost.
Waarom: BreathGym (plek 1 op "breath hold", 100+ downloads) draait op 101 horloges, Ebb (plek 2, 1+) op 74 (GEZIEN, winkel-API 24 nov 05:10). Jouw eigen onderzoek (regels 763 en 792 hierboven): binnen de 14 dagen van `markedAsNew` helpt een update met meer horloges (24% tegen 15%), daarna niets. Voor Ebb sluit dat venster ±27 nov 15:00 UTC. Descent is een duikhorloge, precies wie "breath hold" zoekt.
Wanneer: pakket klaar vóór wo 26 nov 18:00 NL, meld het dan onderaan `berichten/hoofdchat.md` met het pad van het pakket. De hoofdchat uploadt het in dezelfde Chrome-ronde als de 20 talen. De complication van 23 nov komt daarna, als 1.0.3.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 10:45 NL, van de hoofdchat-ronde: Ebb 1.0.2 vervalt
De opdracht van 05:20 (Ebb 1.0.2 met meer horloges) is geschrapt, zie `organisatie/besluiten.md` (24 nov 10:45). De complication van 23 nov blijft geparkeerd tot de hoofdchat hem weer oppakt. Niets doen.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
