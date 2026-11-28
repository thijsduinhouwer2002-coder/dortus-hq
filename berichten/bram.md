# Berichten voor bram

Oudere berichten staan in `berichten/archief/bram-t-m-2026-11-24.md` en `berichten/archief/bram-25-t-m-26-nov-2026.md` (zoek met grep). Hieronder alleen de recente; de nieuwste staat onderaan.

- 27 nov ±05:00 NL (van Daan): #246 YouTube-beschrijvingen ja (8), klaar om te plakken. Kan (geen nakeuring): in de saleversie van de Shorts de tweede regel "Type dortus.com/yt" weg; in 65JiRlDupNc de saleregel direct na de eerste zin.

## 28 nov 2026 ±00:10 NL, van de automatische keurder: blender-gewrichten akkoord nee
Keuring van 7de51b8..086354d: `platformen/blender/keuring/2026-11-28-auto-blender-gewrichten-086354d.md`. Moet en kan: **Moet** 1. Laat een groene e2e-run zien met `toetsen_tenen.py` erin, op 4.2.23 en 5.x, plus de bestaande Pro-toetsen (army_man, Rigify, Meshy-knight). Zonder dat is niet bewezen dat de teenfout weg is en dat `buiten == 0` Pro niet raakt (A2, A3, B1). 2. Maak duidelijk welke workflow `toetsen_tenen.py` start en hoe het Human Base Meshes-bestand binnenkomt. Als dat niet gebeurt, draait de test nooit (B1). **Kan** 1. Zet in de test een logregel waaruit blijkt dat bij Exact het samensmelten van de ogen echt voorkomt, om de versoepeling te onderbouwen (B2). 2. `h_pogingen` heeft nu 5 in plaats van Los elk moet-punt op en push opnieuw; de keurder kijkt dan weer. Hij leest alleen tekst, dus beeld en speelplezier blijven bij Daan en Iris.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 28 nov 2026 ±00:15 NL, van de automatische keurder: blender-gewrichten akkoord ja
Keuring van 086354d..f893c68: `platformen/blender/keuring/2026-11-28-auto-blender-gewrichten-f893c68.md`. Moet en kan: **Moet:** geen. **Kan:** - Zet het gemeten verlies uit de eerste groene run in de commit of in `ontwerp.md`. Dan is de grens van 6% onderbouwd (A2). - Controleer in het log dat `lid` bestaat en dat `vol0` klopt. Laat de toets anders vooraf een waarschuwing geven als het figuur open randen heeft (A3, B5). Hij leest alleen tekst, dus beeld en speelplezier blijven bij Daan en Iris.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 28 nov 2026 ±00:42 NL, van de automatische keurder: blender-gewrichten akkoord ja
Keuring van af966bb..8003e4b: `platformen/blender/keuring/2026-11-28-auto-blender-gewrichten-8003e4b.md`. Moet en kan: **Moet:** geen. **Kan:** - Schrijf bij "Daan ja (8, #326)" de datum en het bestand van de keuring, en wat "8" is. - Schrijf bij "keurder liep opnieuw (moeten al gedekt door run 46072364194)" kort wat M1 precies was en welk bewijs het dekt. - Zet bij de aangepaste toets voor 4.2.23 in één zin dat hij niet slapper is geworden. Dat kan met het aantal controles of de grens van voor en na. - De code en toets van f893c68 zitten niet in deze diff. Ze moeten door de gewone keuring van de tak `claude/blender-306` voor ze samengevoegd worden. Hij leest alleen tekst, dus beeld en speelplezier blijven bij Daan en Iris.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 28 nov 2026 01:13 NL, van de beeldvergelijking (automatisch): blender-gewrichten
1 plaatje(s) sterk anders dan de vorige geslaagde run of leeg (4.2.23). Geen rode test: kijk of het zo bedoeld is.
Welke plaatjes: https://github.com/thijsduinhouwer2002-coder/dortus-hq/blob/schermen/referentie/blender-gewrichten/main/GEMELD.md

## 28 nov 2026 ±02:12 NL, van de automatische keurder: blender-gewrichten akkoord ja
Keuring van c5dd84e..4a4e2be: `platformen/blender/keuring/2026-11-28-auto-blender-gewrichten-4a4e2be.md`. Moet en kan: **Moet:** geen. **Kan:** 1. Plakkaart zegt "0.1.2 is nergens geplakt" en "nooit geplakt", maar dezelfde kaart noemt dat Printables direct-0.1.2 heeft (en `CHANGELOG.md` heeft 0.1.2 met datum). Herschrijf naar "in geen winkel behalve Printables". 2. Superhive Lite: de kaart zegt dat Lite "the same code as the free Click Joints 0.1.3 on extensions.blender.org" blijft, maar krijgt nu de direct-zip (met `direct.py`, drie sloten en "Upgrade to Pro") in plaats van de extensions-zip. Dat is een kleine onjuistheid op een winkelpagina (vermoeden: zo zou Daan of Thijs het zien). Pas de zin aan of laat d Hij leest alleen tekst, dus beeld en speelplezier blijven bij Daan en Iris.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

- 28 nov ±03:05 NL, van Daan: #340 (plakkaart gratis 0.1.3) nee (7), één moet: Superhive Lite krijgt `click_joints-0.1.3.zip` (extensions-zip), niet de direct-zip, want de Lite-zin belooft dezelfde code als extensions.blender.org; maak er een nieuwe Lite-versie 0.1.3 met de notes van. Details in #340. Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
