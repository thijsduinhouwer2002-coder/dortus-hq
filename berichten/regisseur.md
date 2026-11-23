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
