# Nakijken live tekst Gumroad Click Joints Pro tegen 1.2.0, 23 nov 2026, Daan
Wat ik nakeek: https://duinhouwer8.gumroad.com/l/click-joints-pro (beschrijving, met curl gelezen 23 nov ±12:45 UTC, GEZIEN), tegen `platformen/blender/pro-1.2.0.md`.
Opdracht: lijst hoofdchat 23 nov 12:05, punt 1.

Nu staat 1.1.0 nog als bestand op Gumroad (lijst Thijs punt 3), dus de tekst klopt vandaag met de zip. Maar zodra Thijs de zip naar 1.2.0 wisselt, klopt de pagina niet meer, en in punt 3 van de lijst staat geen tekstwissel.

| # | Live zin | Probleem bij 1.2.0 | Voorstel (Engels) | Moet/kan |
|---|---|---|---|---|
| 1 | "Already bought Pro? 1.1 is a free update: download it again from your Gumroad library." | verouderd | "Already bought Pro? 1.2 is a free update: download it again from your Gumroad library." | moet |
| 2 | (ontbreekt in "What you get") | de nieuwe knop Fit test strip staat nergens op de pagina, terwijl dat de reden voor 1.2 is | nieuw punt: "Fit test strip. Print this first: five joints from 0.10 to 0.30 mm clearance, each with its number, so you know which gap fits your printer." (letterlijk uit de gekeurde releasenotes) | moet |
| 3 | "Not print tested by us yet: print a test joint first, every printer is different." | kan nu naar de knop wijzen | "Not print tested by us yet: print the Fit test strip first, every printer is different." | kan |
| 4 | "Best in Blender 4.5 and newer. In Blender 4.2 it works, but some joints may need to be placed by hand (the list tells you which)." | klopt met de elleboogfix (4.5+) | geen | ok |
| 5 | "A small degree arc at each joint with its number" | klopt met 1.2.0; pas aanpassen als de mooier overlay uitkomt ("Labels: Selected or All") | later | ok |

Superhive (blok "New in Pro 1.2") en extensions.blender.org (gratis 0.1.1, geen Pro-claims behalve de steunzin) zijn al gekeurd en apart geregeld.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
