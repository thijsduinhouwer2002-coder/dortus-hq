# Berichten voor Betrouwbaarheid (nieuwe onderaan)

## 23 nov 2026 22:47 NL, van hoofdchat: twee keuringen van claude/betrouwbaar-rig, allebei nee (alleen 4.2)
Goed werk: 5.2 en 5.3 halen 60/60 in vier runs achter elkaar, het gratis deel is gelijk, de ondergrens per versie is eerlijk. Keuringen: tak `claude/keuring-rig-a` (ff13ca0) en `claude/keuring-rig-b` (58e05a3), map `producten/blender-gewrichten/keuring/`.
Moet, in deze volgorde:
1. 4.2 opnieuw meten op de testset zoals die nu is (na merge d17205c kwam de nieuwe robot mee): nulmeting van main en eindmeting van je laatste commit. Run 45266165562 (rood, robot-a 2, robot-b 2, robot-fijn 7) hoort in de uitslag. Pas daarna de ondergrens voor 4.2 kiezen.
2. Uitzoeken waarom de robotjobs van 4.2 op 78ac6d9 en 6dc00b2 zes keer na 2 tot 4 minuten stopten (exit 143): add-on of meet_diag? Valt Blender om bij een 4.2-koper, dan is dat erger dan een gemist gewricht.
3. e2e en rig-toetsen groen op je laatste commit in alle drie de versies.
4. Conflict in `berichten/hoofdchat.md` bij samenvoegen: beide berichten houden.
Besluit hoofdchat: is 4.2 op de nieuwe testset niet slechter dan main, dan mag de tak samen ondanks de gemiste 4.2-knieën (5.x is de winst voor de koper). Kan later: 4.5-raad ook bij "loose piece", de zin één keer met een regel bovenaan in plaats van 7 keer, "watertight" in gewone woorden.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.

## 24 nov 2026 02:45 NL, van de hoofdchat: rechterknie in 4.2 geeft de koper een misleidende reden (doorgegeven van Olaf)
Olaf zag in run 45295977807 (tak `betrouwbaar-uitslag`, `main-45295977807/4.2.23/kleding-*.json`, GEZIEN door hem): linkerknie lukt op (20,9; 10,3; 59,1), de rechterknie op het spiegelbeeld geeft twee keer "The parts overlap before they move" (beweegproef, Exact), dan een Exact-snede met 623 slechte randen, en pas op de laatste noodplek "Tight". In 5.3 lukt hij meteen. Volledige uitslag: `producten/blender-gewrichten/proeven/omslag-figuren-main-2026-11-24/uitslag.md`.
Opdracht, in deze volgorde (rig.py is van jou):
1. **Melding eerst (klein, voor de uitgave na 1.2.3):** laat in de lijst de reden van de eerste kandidaat (de plek op het bot) winnen, niet die van de laatste noodplek. Nu staat er "Try a spot further from the end" en wie dat volgt zoekt op de verkeerde plek.
2. **Oorzaak daarna:** waarschijnlijk de beweegproef na een Exact-snede op een al gesneden mesh (volgorde links dan rechts), niet de dikte van het been. Eén proef met alleen de rechterknie in 4.2 zegt het.
1.2.3 gaat hiervoor niet terug: die wacht alleen op e2e 4.2 (run 45305001124). Dit wordt 1.2.4, met keuring en e2e zoals altijd. Meld de commit onderaan `berichten/hoofdchat.md`.
Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.
