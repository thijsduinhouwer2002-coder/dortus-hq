# YouTube: koopregel bovenaan de lange video's, kanaalprofiel en saleregel

- status: gekeurd ja (aparte keurder 24 nov), K1 verwerkt; klaar om te plakken
- kanaal: youtube (beschrijvingen en profiel, geen nieuwe post)
- product: click-joints-pro
- plakt: de hoofdchat in YouTube Studio (Shorts-ronde 21:17); de twee lange video's die al in Metricool klaarstaan (1 en 3 dec) past de Maker van Roep aan
- gemaakt_door: Chris, 24 nov 2026 ±19:10 NL, opdracht hoofdchat 16:05 (ja Thijs 15:59)

## Waarom
6.000 weergaven, 0 klikken naar de site (Meter, bericht hoofdchat 16:05). Een Short heeft geen klikbare link; een lange video en het kanaalprofiel wel. De link staat nu pas onderaan of als losse regel; YouTube toont boven "...meer" alleen de eerste regels (GOK: ±2 regels op een telefoon).

## De link
`https://dortus.com/yt/?utm_source=yt&utm_medium=video`

Waarom deze en niet /click-joints: volgens `organisatie/meten/korte-links.md` is /yt het pad voor YouTube. Amami telt bezoeken per pad, en de koopknop op /yt krijgt `utm_source=yt` zodra laag 1 op main staat. Zo blijft alles van YouTube op één spoor. /yt is de Pro-pagina "Click Joints Pro for Blender: rig to printable figure" en gaf code 200 (GEZIEN, curl 24 nov ±19:05 NL). Voor het profiel `utm_medium=profile`, zodat we die klikken apart zien.

## 1. Nieuwe eerste regel, lange video's
Bovenaan de beschrijving, boven alle bestaande tekst. De rest blijft zoals hij is.

```
Get Click Joints Pro for Blender: https://dortus.com/yt/?utm_source=yt&utm_medium=video
```

Geldt voor:
- https://www.youtube.com/watch?v=m3sNvDOJYQ0 (20 nov, scharnier met stop)
- https://www.youtube.com/watch?v=4-3l3MZZWPc (22 nov, rig to printable figure)
- de twee lange video's in Metricool: 437867666 (1 dec, `2026-12-01-yt-lang-zoek-articulated-3d-prints.md`) en 437867758 (3 dec, `2026-12-03-yt-lang-zoek-blender-hinge-3d-print.md`); die zet de Maker van Roep erin
- en vanaf nu elke nieuwe lange video (ook de update-video van 1.2.7)

## 2. Kanaalprofiel
Link in het profiel (Aanpassen, Basisinfo, Links), titel en adres:
```
Click Joints Pro
https://dortus.com/yt/?utm_source=yt&utm_medium=profile
```
Eerste zin van de kanaalomschrijving (de rest blijft):
```
Blender add-ons that turn your models into poseable 3D printable figures. Get Click Joints Pro: https://dortus.com/yt/?utm_source=yt&utm_medium=profile
```

## 3. Saleregel (alleen in de saleweek)
Komt boven regel 1, dus wordt de nieuwe eerste regel:
```
25% off until December 1.
```
- Erop: als de korting op Gumroad echt aan staat. Volgens het plan (`commercie/blender-click-joints/black-friday.md` stap 1) loopt CYBER25 van vr 27 nov 00:00 tot di 1 dec 23:59. Staat hij op do 26 nov nog niet aan, dan wacht de regel tot hij aan staat: een korting noemen die er niet is mag niet. De hoofdchat kijkt het na op de productpagina (doorgestreepte prijs).
- Eraf: wo 2 dec, op alle video's en in het profiel als hij daar ook staat.
- Op Superhive loopt de Cyber Sale 27 nov tot en met 2 dec (bord); de link gaat naar dortus.com en Gumroad, dus de regel noemt 1 december.

## Wat er niet in staat
Geen AI-vermelding, geen "not print tested" (besluit Thijs 15:32, bericht hoofdchat 16:05). Geen prijs, zodat de regel na de prijswijziging blijft kloppen.

## Keuring
24 nov 2026 ±19:20 NL, aparte keurder voor Chris (één keuring, kleine tekst). **Akkoord: ja.**

Getoetst:
- Opdracht (`berichten/chris.md`, 16:05): koplink met utm als eerste regel lange video's, zin voor de kanaalomschrijving, profiellink met dezelfde link, saleregel "25% off until December 1", geen AI-vermelding, geen "not print tested". Alles aanwezig.
- utm-patroon: /yt met `utm_source=yt&utm_medium=video` is precies de regel voor YouTube in `organisatie/meten/korte-links.md` (het voorbeeld in de opdracht met /click-joints en `youtube` was alleen een voorbeeld; de opdracht zegt het patroon uit korte-links te volgen). Goed gekozen.
- Links: beide (video en profiel) gaven code 200 zonder doorsturing, titel "Click Joints Pro for Blender: rig to printable figure" (GEZIEN, curl 24 nov ±19:20 NL).
- Saledatum: CYBER25 loopt vr 27 nov 00:00 tot di 1 dec 23:59 (`commercie/blender-click-joints/black-friday.md` stap 1); "until December 1" klopt daarmee. De opdracht zei de regel op do 26 nov erop te zetten; Chris koppelt het terecht aan de korting die echt aan staat. Dat is eerlijker dan de opdracht en mag zo. Superhive tot en met 2 dec (bord) is goed uitgelegd.
- Engels kort en correct. Geen persoonsgegevens, geen prijs in de tekst.

Moet: geen.

Kan:
- K1: `utm_medium=profiel` is Nederlands en zichtbaar voor kijkers in de link. `profile` past beter naast `video`. Kies het vóór het plakken, want na het plakken telt Amami de oude naam.
- K2: Let op dat de utm nu alleen in Amami (bezoek per pad) zichtbaar is: de koopknop op /yt gaat nog zonder utm naar Gumroad tot laag 1 op main staat (GEZIEN, curl). Staat al zo in "De link"; geen tekstpunt.
- K3: "until December 1" kan een koper lezen als "tot en met 30 nov". "through December 1" is scherper, maar de opdracht noemt deze zin letterlijk, dus laten staan mag.
- Verwerkt door Chris (24 nov ±19:30): K1, overal `profile`. K3 gelaten (letterlijk uit de opdracht).
