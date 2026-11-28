
## 23 nov 2026 ±13:50 NL, van de hoofdchat: Gumroad-mail 27 nov
Besluit: de mail gaat via het account van Thijs, dus Thijs zegt ja op de tekst (regel 4). Bram schrijft, Daan keurt, de hoofdchat zet de gekeurde tekst op de lijst van Thijs. Het aantal gratis kopers zet de hoofdchat erbij zodra de tekst er is.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±12:45 NL, van hoofdchat-ronde: sale-vinkje staat aan
Dank voor Surface Lab. Je vraag: ja, "Sitewide Sales" staat aan op Superhive sinds 19 nov 13:45 (besluit, GEZIEN toen in het creator-dashboard), Cyber Sale 35% van vr 27 nov t/m wo 2 dec. Clips (Chris) en Docs-tab (Bram) gaan mee in de plak van 1.2.5.

## 24 nov 2026 ±20:15 NL, van hoofdchat: per product een lat met voorbeelden van de top (besluit Thijs 20:08)
Thijs wil blijven spreiden, maar de agents moeten "beter opgeleid" worden. Jouw volgende runs: maak voor elk product een lat in `organisatie/lat/<product>.md` (click-joints, click-cuts, hats, ebb, bison-flex, rollwright): de 3 beste concurrenten in die winkel (naam, link, verkopen of reviews), hun hoofdbeeld, beste schermbeeld, video en eerste alinea van de winkeltekst (beelden met curl opslaan in `organisatie/lat/beelden/<product>/`, bekeken met Read), en in 5 tot 8 regels wat ze beter doen dan wij en waar ons werk aan moet voldoen. Begin met Click Joints en Hats. Elke agent leest die lat voor hij iets maakt (CLAUDE.md startstap 3).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±21:05 NL, van hoofdchat: ALLEEN UITERLIJK tot het product plek 1 haalt (Thijs 20:50 en 20:59)
Thijs: eerst moet alles er spectaculair uitzien en opvallen, dan pas marketing, dan doorbouwen. Geen geld voor gekochte plaatjes: we maken het zelf. **Nieuwe harde regel 9 in CLAUDE.md:** een hoofdbeeld, omslag, thumbnail of eerste beeld gaat pas live als het GESLAAGD is in de blinde test door Gemini en ChatGPT (`organisatie/blindtest/LEESMIJ.md`). Eerste uitslag staat in `organisatie/blindtest/uitslag/`: onze cover plek 2 achter Cleave; held-3 voor-na plek 4 (geen tekst, niemand snapt wat het doet); beide rechters willen een gedetailleerd personage in plaats van de tekenpop en een echte print. Lees ook `organisatie/lat/wat-thijs-wil.md`. Geen marketing, geen nieuwe functies: alleen uiterlijk en gevoel.
**Jouw taak (vervangt de lat-opdracht van 20:15 deels):** maak voor elk product een blinde-testset met de 3 sterkste concurrenten in die winkel (hoofdbeeld, openbare url met curl gevonden, naam), in `organisatie/blindtest/sets/<product>-<winkel>.json`, met ons huidige hoofdbeeld als kandidaat. Volgorde: Click Joints Pro Gumroad, Click Cuts, Ebb (Garmin), Bison & Flex (JetBrains), Rollwright (Obsidian), Hats (Steam, schermen). Push: de test draait vanzelf. Schrijf in `organisatie/lat/<product>.md` wat de winnaars beter doen, met de zinnen van de rechters.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±21:30 NL, van hoofdchat: lat per product is nu verplicht voor alles (CLAUDE.md regel 10)
Thijs: bouwen, functies, uiterlijk en marketing moeten bij alles bijna gelijk zijn aan de beste concurrenten. Vul per product `organisatie/lat/<product>.md` volgens `organisatie/lat/SJABLOON.md`: functies, prijs, etalage, marketingkanalen van de 3 sterksten, onze gaten op volgorde van geld, en ons voordeel. Volgorde: click-joints-pro, click-cuts, hats, ebb, bison-flex, rollwright. Daarbij de blinde-testsets uit je vorige opdracht. Eén product per run, maar dan helemaal en met bronnen.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±22:05 NL, van hoofdchat: nieuw team, werk komt nu uit GitHub-issues
Vanaf nu staat je werk in een GitHub-issue met jouw label en een blok "Klaar als" (zie je nieuwe vaste opdracht en `organisatie/team-plan-2026-11-24.md`). Dat issue gaat voor oudere berichten hieronder of hierboven. De beelden van Click Joints Pro en Click Cuts maakt voortaan de Beeldmaker; de kunst van Hats Mila. Kaart van je product: `producten/<naam>/KAART.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 26 nov 2026 00:20, van hoofdchat: drie namen nagaan
Google AI raadt kopers in plaats van Click Joints Pro aan: SlicerJoint Pro (±$20), NB Figure Joints (Patreon), JointLab (±$65). Gemini noemde NB Figure Joints en SlicerJoint Pro ook. Ga na of ze echt bestaan (curl, link), wat ze doen en kosten, en zet wat klopt in `organisatie/lat/click-joints-pro.md`. Bestaan ze niet: zet dat erbij, dan weten we dat de AI verzint.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 27 nov 2026 00:45, van hoofdmanager: ja, push de README van click-joints
Antwoord op je vraag van 26 nov 21:35: zet `producten/blender-gewrichten/repo-click-joints/README.md` (Daan ja #160) in je volgende run in repo click-joints. De openbare README zegt om 00:40 nog "print tested" (curl, GEZIEN). Alleen die README, niets anders in die repo. Meld het daarna in één regel in `commercie/geplaatst.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
- 28 nov ±06:45 #323: grotere-markt-2026-12.md (derde controle, ranglijst, advies geen nieuwe markt, prijsvoorstel), keuring Daan #355.
