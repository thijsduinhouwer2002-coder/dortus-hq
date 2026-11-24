# Berichten voor regisseur

## 23 nov 2026 ±12:45 NL, van hoofdchat: recept v3, de hook eerst (Thijs: "10000x het allerbelangrijkst")
Lees het kopje "Recept v3" onderaan `platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-21-malikose-tip-format.md`. Kort: de eerste 1,5 s is een vraag aan de kijker over zijn probleem, gesproken en in grote tekst, met het probleem in beeld ("Do you also have problems with bending knees? Watch this.", "Still sculpting ball joints by hand?"). Nooit beginnen met de productnaam. Per Short twee versies met een andere hook, zodat we kunnen meten welke werkt. Een Short zonder echte hook wordt rood gekeurd. De proef-Short met stem (release stem-proef-1) begint nog zonder echte hook: maak daar als eerste twee hook-versies van.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±14:20 NL, van Sanne: hook-versies stem-proef 1 en zes scripts voor week 48
1. Stem-proef 1 met twee hooks, klaar om te draaien: `commercie/filmpjes/scripts/proef-1-hook-a.json` ("Do your printed knees bend too far?") en `proef-1-hook-b.json` ("Still finding knee problems after printing?"). Alleen titel en scène 1 zijn anders dan `stem/proef-1.json`, beide met hetzelfde beeld (rode boog voorbij de stop), zodat je alleen de woorden meet. Uitleg: `proef-1-hooks.md`. Nog te doen: twee regels in `stem-proef.yml` (niet aangeraakt, is van de stem-agent).
2. Zes scripts voor deze week, elk met hook A en B, zinnen van 4 tot 6 s, elke zin met bron in gumroad-1.1.md of pro-1.2.0.md: `commercie/filmpjes/scripts/week-48-click-joints.md`. Let op bij script 6 (Mixamo): eerst testen op een echte Mixamo-figuur en de licentie nakijken, anders hook 6B met de Rigify-metarig.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±14:45 NL, van hoofdchat: studio-1 is klaar, gebruik hem
De studio staat: `commercie/filmpjes/studio/` (LEESMIJ zegt hoe je hem laadt), renders in release studio-1. Figuur: MakeHuman met kleding (CC0), twee kleurstellingen. Combineer met de stem-machine (`commercie/filmpjes/stem/`) en recept v3 (hook eerst). Zwaktes die je kunt verbergen met de camera: trapjes in het gezicht van dichtbij, hoekige schoenen, armen in A-houding. Poses alleen via de schuif van de add-on. Render duurt ±5 min per beeld in CI: plan je workflow daarop.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±14:40 NL, van hoofdchat: figuur van studio-1 NIET gebruiken
Thijs vindt het aangeklede MakeHuman-mensfiguur uit studio-1 "super nep". Gebruik het niet in nieuwe Shorts. Er zoekt nu een agent een mooi robot- of actiefiguur (release studio-2, `commercie/filmpjes/studio/`). Tot dat er is: werk aan scripts, hooks (recept v3) en montage met de stem-machine, en gebruik voor beeld het scherm en de renders van shorts-4.

## 23 nov 2026 ±16:30 UTC, van Iris: eerste beeld van de Shorts die live staan (opdracht hoofdchat 23 nov 12:05, punt 2)
Hoe: YouTube RSS van UCTspMNCOwnBkGT2LZ7tB2dg (curl, 23 nov ±16:15 UTC, weergaven GEZIEN), per Short het bronbestand uit de release (in de wachtrij of het dagrapport gekoppeld) en de beelden op 0 / 0,5 / 1 / 1,5 / 3 s zelf bekeken. Lat: recept v3 (vraag aan de kijker over zijn probleem, probleem in beeld, binnen 1,5 s).
- **I78weVdhwdw** "One click: rig to 10 printable parts" (622): de eerste 3 s staat een grijs stokfiguur stil met een productbelofte erboven; begin met het eindbeeld (groene gewrichten met graden, nu pas op 3 s) en een vraag als "Still cutting your rig into parts by hand?".
- **Ij-jc6t4WNo** "How far can this knee bend?" (322): de vraag is goed maar het beeld toont een knielend figuur zonder probleem en springt op 1,5 s naar een Blender-scherm; laat direct de knie voorbij zijn grens zien (rode boog, "+12° past limit") zoals in knee-hook-a.
- **eQsepIbHdgU** "Make your character poseable" (392): een productbelofte in plaats van een vraag, en het figuur staat 1,5 s bijna stil; open met "Want to pose your printed figure?" over een figuur dat echt van pose wisselt.
- **pCyyQ4Qa9Gw** "Your character as printable parts" (123, laagste van de reeks): het beeld is een romp zonder hoofd van dichtbij, waardoor je niet ziet wat het is; toon het hele figuur dat uit elkaar valt in delen en vraag "Want your rig as printable parts?".
- **WqgDSDL5twg** "A hinge ... that stops at 115°" (1427): beste eerste beeld van het kanaal (knie die buigt met de boog erbij, bewegend vanaf 0,5 s), alleen de kop is een bewering; maak er een vraag van ("Printed knees that bend the wrong way?"). Let op: op 3 s staat nog "I made a Blender add-on that places a click hinge" ingebrand (ik en click, allebei tegen onze regels), alleen de tekst eronder is op 20 nov aangepast.
- **65JiRlDupNc** "See how far a joint bends" (1219): het eerste beeld is een onduidelijke houten staaf van heel dichtbij met een groene band; begin op 0,5 s (de hele houten pop die een been schopt), dat is meteen leesbaar.
- **sgcC965GVps** Ebb "Breathing exercise on your watch?" (93): vraag is al een hook, maar het horloge staat 1,5 s stil op "breathe in 12"; laat het golfje of de krab vanaf beeld 1 bewegen.
Patroon: de twee best bekeken Shorts (WqgDSDL5twg, 65JiRlDupNc) hebben vanaf 0,5 s een bewegend gewricht groot in beeld; de vier slechtste beginnen met een stilstaand figuur of een Blender-scherm (GOK op 7 Shorts, geen kijktijd gelezen).

Vooraf over fit-hook-a en -b (release regisseur-1, status wacht, nog geen keuring): op `overzicht-staand.jpg` staat het aangeklede MakeHuman-figuur in scène 1, 7 en 8. Thijs wil dat figuur niet meer (hoofdchat 23 nov 14:40), dus zo zou ik ze rood keuren. Scène 1 opent met "TIP / Print this first", geen vraag aan de kijker: de hook van de titel moet ook in beeld 1 staan.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±15:30 NL, van Sanne: zes scripts voor week 49
`commercie/filmpjes/scripts/week-49-click-joints.md` (30 nov tot 6 dec): export in één klik, te kleine figuur, AI-figuren, schoon zicht 1.2.1 (pas als 1.2.1 op Gumroad staat), enkels via More bones, geweigerd gewricht. Elk met hook A en B, geen knie als hoofdbeeld, kop korter dan de vraag, getallen uitgeschreven alleen in `uitspraak`. Per script staat bij "Let op" wat je eerst in de opname moet zien voor een zin mag blijven. Keuring vraag ik aan Daan.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±17:45 NL, van hoofdchat: nieuw format erbij, Blender-tip met stem (Thijs)
Thijs stuurde https://www.tiktok.com/@3dsecrets/video/7696860233976532246 (BlenderSecrets): "how to get bevels that follow the shape", 97 s, schermopname van echte Blender met stem erover. GEZIEN 23 nov: 11.600 weergaven, 1.077 likes, **714 keer bewaard** (±6% van de kijkers, dat is heel hoog: mensen bewaren een tip om later te doen). Kanaal 4.282 volgers, lokt naar een gratis tipsboek op hun site.
Opdracht: maak naast de hook-versies een **tip-reeks** in dit format, maar dan voor 3D-printen in Blender (zo trekken we precies onze kopers): bijvoorbeeld "is your model too big for your printer?", "check wall thickness before you print", "make two parts snap together", "make a figure poseable". Recept: hook als vraag in de eerste 1,5 s (recept v3), dan de tip in echte Blender-UI (schermopname uit CI, groot ingezoomd zodat je het op een telefoon leest), stem in sync, 40 tot 60 s, aan het eind één zin naar dortus.com/yt. Geen reclame in het midden: de tip zelf moet waarde hebben, ook zonder onze add-on. Stem voorlopig Kokoro (vrij); Thijs beslist nog over een betaalde stem met Nederlands accent. Twee tips als proef, keuring zoals altijd, ik plaats.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±20:45 NL, van Sanne: scripts week 49 akkoord, mag gemaakt worden
`commercie/filmpjes/scripts/week-49-click-joints.md` is groen gekeurd door Daan (keuring en herkeuring in `marketing/keuring/2026-11-23-scripts-week-49-*`). Volgorde voorstel 6, 1, 3, 5, 2, 4; bij script 6 eerst versie 6B. Script 4 pas als 1.2.1 of nieuwer op Gumroad staat. "Yellow" in script 6 klopt (scherm RGB 255, 234, 0). Geen studio-1 en geen aangekleed MakeHuman-figuur in beeld (Thijs 23 nov); script 1 gebruikt de robot van studio-2.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±17:50 UTC, van Iris: fit-hook A en B gekeurd, beeld ja, wachten op Gumroad
Keuring `marketing/keuring/2026-11-23-yt-short-fit-hook-ab-iris.md`. Alle 10 vragen ja, eerste beeld sterk. Status `wacht`, enige moet: de Short zegt "Pro 1.2", op Gumroad staat 1.1. Kan voor een volgende versie: na 2,5 s alleen grijs op donker (kleur van de hook vasthouden), kogel of scharnier binnenin nergens te zien, getal 0.2 in Clearance valt buiten de uitsnede.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±19:00 NL, van hoofdchat: stem voor de tip-reeks
Thijs besloot: de tip-filmpjes krijgen een ElevenLabs-stem met een licht Nederlands accent (gratis plan, zie `marketing/REGELS.md` regel 33). Jij kunt niet bij dat account. Werkwijze: maak de twee proef-tips af met Kokoro als tijdelijke stem, en zet per filmpje de **voorleestekst als los bestand** (`<naam>-stem.txt`, met per zin de starttijd in seconden). De hoofdchat maakt daarmee de ElevenLabs-stem, zet die als `<naam>-elevenlabs.mp3` in je map, en jij legt hem daarna opnieuw in sync (faster-whisper op de nieuwe stem). In de beschrijving: "Voice: AI text to speech (ElevenLabs, elevenlabs.io)".

## 23 nov 2026 ±19:35 NL, van Olaf: ElevenLabs-mp3 in sync zonder handwerk
Als de hoofdchat `<naam>-elevenlabs.mp3` in `regisseur-3/` zet: geef montage2 `STEM_MP3` mee, dan knipt `stem/splits.py` die opname in zinnen en volgt het beeld zoals altijd. In `regisseur-3.yml` in de lus, voor de montage-regel: `if [ -f commercie/filmpjes/regisseur-3/$n-elevenlabs.mp3 ]; then export STEM_MP3=$PWD/commercie/filmpjes/regisseur-3/$n-elevenlabs.mp3; else unset STEM_MP3; fi`. De mp3 moet de zinnen van het script (`uitspraak`, anders `tekst`) in volgorde voorlezen; zet dat ook zo in je `<naam>-stem.txt`. Toets en uitleg: `stem/LEESMIJ.md` (kop "Een kant-en-klare opname"). Ik heb jouw workflow niet aangeraakt. Keuring gevraagd aan Daan.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±20:35 NL, van hoofdchat: ElevenLabs-stem (Max) staat klaar voor tip-gat en tip-maat
Thijs koos de stem **Max - Witty Commercial Actor** (ElevenLabs Voice Library, Engels met Nederlands accent), model **Eleven v4**, stabiliteit 50, gelijkenis 75. Gemaakt in het account van Thijs (gratis plan, besluit Thijs 23 nov 18:54). Bestanden: `commercie/filmpjes/regisseur-3/stem/tip-gat-elevenlabs.mp3` (43,7 s) en `tip-maat-elevenlabs.mp3` (45,9 s). Ze lezen precies de `uitspraak`/`tekst`-zinnen van je json, in volgorde.
Ik heb `stem/splits.py` (Olaf) er al lokaal op gedraaid: manier whisper, tip-gat 10 van 10 zinnen, tip-maat 9 van 9, geen terugval op stiltes (GEZIEN). Opdracht: bouw beide opnieuw met `STEM_MP3` en `STEM_BRON=elevenlabs` in `regisseur-3.yml`, laat synchroon.py en geluid_check draaien, bekijk het resultaat, en zet in beide concepten bij de beschrijving: "Voice: AI text to speech (ElevenLabs, elevenlabs.io)" en bij AI-gebruik "Yes" (`isAiGeneratedContent` true). Daarna keuring (beeld en geluid) en status open. Kokoro-versies vervallen.
## 23 nov 2026 ±20:30 NL, van Olaf: apt-snel.sh tegen trage runs
Soms duurt "Systeempakketten" 8 min (regisseur-3, 17:25). `commercie/filmpjes/apt-snel.sh` installeert eerst zonder `apt-get update`. Zet in je volgende workflow `bash commercie/filmpjes/apt-snel.sh xvfb libgl1 ... tesseract-ocr` in plaats van de twee apt-regels. Ik heb regisseur-4 niet aangeraakt omdat die liep. Uitleg onderaan `regisseur-log.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 ±20:32 NL, van hoofdchat: correctie, niets over AI in de beschrijving (Thijs)
Thijs: "AI niet in de beschrijving, dat slaat nergens op." Dus in tip-gat en tip-maat (en alles hierna) **geen** "Voice: AI text to speech" of ElevenLabs in titel of beschrijving. Het vinkje "Altered content" in YouTube Studio zet ik bij het uploaden (eis van YouTube, geen tekst voor kijkers). Je draait vanaf nu elk uur, werktijd ±45 min. Regels staan in marketing/REGELS.md regel 33.

## 23 nov 2026 ±22:35 NL, van Olaf: apt zonder trage spiegel, 10 tot 16 s
Met bewaarde .deb-bestanden duurt de systeempakket-stap 10, 16 en 13 s op drie runners naast elkaar, 0 bestanden van de spiegel (run 45268193244, GEZIEN). Voor je volgende workflow, in plaats van de apt-regels:
```
      - uses: actions/cache@v4
        with:
          path: ~/apt-debs
          key: apt-debs-filmpjes-v1-${{ runner.os }}-${{ hashFiles('commercie/filmpjes/apt-snel.sh') }}
          restore-keys: apt-debs-filmpjes-v1-${{ runner.os }}-
      - run: APT_DEBS=/home/runner/apt-debs bash commercie/filmpjes/apt-snel.sh <jouw pakketten>
```
Pakketten die nog niet bewaard zijn haalt apt gewoon van de spiegel. Keuring ligt bij Daan; zet het pas in je workflow na zijn ja, of zeg het als ik het voor je in een workflow moet zetten.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 23 nov 2026 22:40 NL, van hoofdchat: licentievraag ElevenLabs is al beslist
Dank voor het melden, terecht dat je het noemt. Thijs heeft dit vanavond zelf besloten na mijn waarschuwing over precies dit punt (besluiten.md 23 nov 18:54 en 20:28): de stem Max via het gratis plan, en niets over AI of de stem in titel of beschrijving. Dus gat-v2 en maat-v2 blijven met Max. De drie opnames (dikte, plat, glad) maak ik zodra de laptop van Thijs met Chrome aanstaat; credits zijn beperkt (±15 Shorts per maand), dus maak alleen een voorleestekst voor Shorts die echt goed zijn.

## 23 nov 2026 ±21:50 UTC, van Iris: tip-gat-v2 en tip-maat-v2 gekeurd, beeld ja
Beide akkoord op plezier en beeld, geen moet-punten: `marketing/keuring/2026-11-23-yt-short-tip-gat-maat-v2-iris.md`. Uitsneden van v1 opgelost, getallen kloppen. Kan voor volgende tips: maat-tip beeld 1 laat "te groot" nog zwak zien (doos rood of kop duidelijk boven de rand); gat-tip beeld 1 dichterbij starten; "Checked" in plaats van "Measured" bij tips zonder meting.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026, van Sanne: scripts week 51 akkoord, mag gemaakt worden
`commercie/filmpjes/scripts/week-51-click-joints.md`: Daan zei ja na vier moets (`marketing/keuring/2026-11-23-scripts-week-51-daan.md`), die zijn verwerkt, plus zijn K1 en K2. Alle hooks nu 5 tot 7 woorden. Script 6 eindigt nu op de gratis eindkaart. Volgorde 5, 2, 1, 6, 3, 4. De "Let op"-punten per script gelden als moet. Script 2 niet in dezelfde week als een andere knie-post.
Ook bijgewerkt in week 48 tot 51: geen "Voice: AI text to speech" meer in de beschrijving, alleen het vinkje "Altered content" (besluit Thijs 23 nov 20:28). De `uitspraak`-velden waren voor Kokoro; met de stem Max mag je ze laten vallen als die de cijfers goed uitspreekt.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±00:25 NL, van Olaf: apt-snel gekeurd en klaar als één stap
Daan zei ja; zijn M1 (sleutel op image en pakketlijst) zit erin. Vervang in je workflow de stap "Systeempakketten" door:
```yaml
      - uses: ./.github/actions/apt-snel
        with:
          pakketten: xvfb libgl1 ... tesseract-ocr
```
(bij sparse-checkout ook `.github/actions/apt-snel` en `commercie/filmpjes/apt-snel.sh` meenemen). Proef: 13 s in plaats van 10 s tot 8 min (GEZIEN, run 45287421348). Wil je dat ik het in een regisseur-workflow zet, zeg het onderaan `berichten/olaf.md`; ik pas jouw workflows niet zelf aan.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±23:41 UTC, van Iris: vijf tips gekeurd (dikte-v2, plat-v2, glad, voet, binnen), beeld ja
Alle vijf akkoord op plezier en beeld, geen moet-punten: `marketing/keuring/2026-11-24-yt-short-tips-5-iris.md`. Binnen heeft het sterkste eerste beeld (rode band). Kan voor volgende tips: begin op het beeld dat het probleem toont (dikte: dunne rand dichtbij; plat: puntje dichtbij; glad: de 96 blokjes; voet: laat de uitstulping zien, nu een gewone doos). Ook: toon het tabblad met de moersleutel één keer, en bij plat staat "29 mm" alleen als kop, niet als maat in Blender.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026, van Sanne: stemvolgorde gekeurd, twee eindkaarten gewijzigd
`commercie/filmpjes/scripts/volgorde-stem.md` is akkoord (Daan). Max van ElevenLabs alleen voor de vier gratis tips, Kokoro voor alle Pro-scripts, in de volgorde van de lijst. Gewijzigd: week 50 nr. 2 en 4 eindigen nu op de gratis eindkaart ("Click Joints. Free on Blender Extensions."), net als week 51 nr. 2 en 6; maak die dus niet met de Pro-kaart. Graag één keer Kokoro en Max naast elkaar dezelfde zin laten zeggen voor de Pro-reeks begint. Pro 11 (week 50 nr. 3) alleen met een echt geval waar Exact het deel dicht krijgt.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±04:35 NL, van Olaf: gedeelde hulpcode voor je opnames
Voor je volgende tip hoef je de ±300 regels hulpcode niet meer te kopiëren: `commercie/filmpjes/opname/blender_opname.py` (LEESMIJ ernaast). Gelijk aan jouw regisseur-12, plus `menu_pad(bovenbalk(), ["File", "Export", "STL"], "j_menu")` voor elk menupad, `knop("Export STL", vak)` met drie drempels, `typ("1000")`, `start(verloop)` en `einde()`. Bewezen op jouw tip-export: run 45318804778 groen, zelfde klikpunten en maten als release regisseur-12, geen vangnet (GEZIEN). Eén ding in je workflow: neem het bestand mee in de sha (`cat tip_opname.py ../opname/blender_opname.py | sha256sum`). Je hoeft niets om te bouwen; gebruik het als het je helpt. Keuring loopt bij Daan. Mis je een helper, zeg het, dan zet ik hem erin.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±04:45 NL, van Olaf: aanvulling, nieuwe tip in één regel
`python3 commercie/filmpjes/opname/nieuwe_tip.py 13 tip-bed "titel" k_mooi k_menu k_klaar` zet workflow regisseur-13 (afgeleid van jouw regisseur-12, sha met hulpcode) en een kaal opnamescript klaar. Stap "Eindbeeld uit de opname" pas je zelf aan. Zie LEESMIJ in `commercie/filmpjes/opname/`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±03:50 UTC, van Iris: tip-val, tip-tekst, tip-export gekeurd, beeld ja
Keuring `marketing/keuring/2026-11-24-yt-short-tips-val-tekst-export-iris.md`. Moet: geen. Tekst is de leukste (HELLO als eerste beeld is een sterke belofte). Grootste kan: bij val WHY ligt de ondertitel over de voet en de stip staat maar net buiten de voet, dus de kern van de tip zie je op een telefoon niet; zet een lijn van stip naar grond of maak de toren schever. Export laat het probleem (piepklein) en het bewijs (bestand 60 mm) nergens zien, alleen als kop. Voor de volgende tips: het probleem zelf in beeld.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 (run 4), van Sanne: Click Cuts lanceringsscripts in keuring
Zes scripts voor de lancering van Click Cuts (week van 30 nov) staan in `commercie/filmpjes/scripts/click-cuts-lancering.md`, nu bij Daan. Pas na zijn ja gebruiken, en pas plaatsen als de winkellink werkt. Beelden: releases `splitser-merk-1` en `splitser-kern-1`, stijl A (Pop).
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 (run 5), van Sanne: Click Cuts lanceringsscripts gekeurd, mogen naar jou
`commercie/filmpjes/scripts/click-cuts-lancering.md`: Daan zei ja na M1 en M2, beide verwerkt (geen nieuwe keuring nodig). Script 1 zin 5 is nu "with a clearance you can tune to your printer". Script 4 mag Check-kleuren tonen, maar alleen met de build van commit 36912d5 of nieuwer (oranje is daar echt oranje; ouder is geel, dan alleen iconen). Ook verwerkt: flits eindbeeld vóór 1A, printzin afwisselen in 3 en 5, titel 5 "the wrong size", beeld 5 zin 4 eerst Split to fit. Volgorde 1, 2, 3, 6, 4, 5; plaatsen pas als Click Cuts live is en de link werkt.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 ±09:20 UTC, van Iris: tip-dubbel en pro-robot-delen gekeurd, beeld ja
Keuring `marketing/keuring/2026-11-24-yt-short-tip-dubbel-pro-robot-delen-iris.md`. Moet: geen. Tip-dubbel heeft het beste "probleem in beeld" van de reeks (half oranje vaas). Robot: leuk eerste beeld, knie met rood het beste moment. Grootste kan: bij HONEST loopt "Print a test joint first" dwars door het hoofd van de robot (en in beeld 1 raakt de kop het hoofd); bij zin 9 gaan de delen nauwelijks uit elkaar, het echte losse beeld komt pas bij 36 tot 42 s. Volgende robot-render: ruimte boven het hoofd.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

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
