# Skins v3: elke skin een eigen wereld (Daan, 8 nov 2026)

Aanleiding: Thijs 8 nov 12:33 en 12:34. Skins v2 mag mee in 0.3.1, maar het verschil is nog te klein: de achtergrond is bij beide hetzelfde, Parchment en Arcane lijken op elkaar, en het blijft "hetzelfde token in een andere kleur". Hij wil een eigen vorm, een eigen beweging, een eigen letter, een eigen sfeer per skin. Geen haast: eerst de gebruikers voor het gratis deel.

**Waarom wij (één zin):** Andere dobbelsteen-skins leven op een speeltafel (Foundry, D&D Beyond); Rollwright is de enige waar je skin een eigen wereld in je notities zelf is, met een eigen vorm, letter, merkteken en beweging bij elke worp.

## Wat de beste voorbeelden doen (en wat ze missen)
- **Foundry VTT, Dice So Nice en betaalde dobbelsets.** Er worden echte betaalde sets verkocht met precies onze thema's: "Enchanted Parchment Dice" en "Arcane Trap" van The Rollsmith en Norse Foundry (DERDEN: https://foundryvtt.com/packages/trs-norse-dd-enchantedparchment, https://foundryvtt.com/packages/trs-norse-dd-arcanetrap). En een betaalde module Dice VFX voegt alleen sporen tijdens het rollen en een effect bij het landen toe (DERDEN: https://foundryvtt.com/packages/dice-vfx). Wat ik overneem: **een skin is materiaal plus beweging plus een landingsmoment**, niet alleen kleur. Mensen betalen daar al voor.
- **D&D Beyond digitale dobbelstenen.** Sets per thema (DERDEN: https://www.dndbeyond.com/tag/digital-dice). Zelfde les: elke set heeft een eigen materiaal en eigen effect.
- **Wat ze missen:** het gebeurt allemaal op een 3D-tafel, los van je aantekeningen. In een notitie is er niets. Daar doen wij de stap bovenop: de wereld van de skin zit in de regel tekst zelf, klein, snel en zonder 3D.

## Het ontwerp
| | Classic (gratis) | Parchment, "het scriptorium" | Arcane, "de sterrenkaart" |
|---|---|---|---|
| Vorm | afgerond speelstuk | gescheurde strook papier, licht scheef | kristal met punten aan beide kanten |
| Letter | die van het thema | IM Fell English Italic (17e eeuw, label en tabelzinnen), getal in Palatino vet | Cinzel Bold (Romeinse kapitalen) |
| Merkteken | d20 in de accentkleur | rood lakzegel met de d20 erin gedrukt | cyaan d20 met gloed |
| Rand | dun, accentkleur | verbrande papierrand en schaduw | rand van licht (cyaan en violet) die de vorm volgt |
| Rollen | d20 tuimelt, getal valt | zegel drukt neer, inkt schrijft het getal van links naar rechts, spatjes inkt | d20 draait twee keer in een cirkel van runen, getal verschijnt uit het licht, wolkje sterrenstof |
| NAT 20 | goud, vonk | bladgoud met rood lakzegel als sticker | gouden rand en gouden cijfers op paars |
| NAT 1 | rood, schudt | inktvlek, zwart zegel, schudt | rode vloekgloed, schudt |

Techniek (alleen CSS, op tak `ontwerp/rollwright-skins5`): het lichaam van het token is `::before` met een `clip-path` (de vorm); het token zelf is doorzichtig met `isolation: isolate`, zodat de vorm achter de tekst blijft en de sticker er bovenop. Rand en schaduw met `filter: drop-shadow`, die volgt de vorm. De twee letters zitten als kleine woff2 in `styles.css` (alleen gewone Latijnse tekens, samen ±66 kB; SIL Open Font License 1.1, die vraagt dat de licentietekst meegaat). Bestanden: `src/styles/07-skins-v3-letters.css`, `src/styles/08-skins-v3.css` (gemaakt met `e2e/ontwerp/maak-skins-v3.py`).

## Nog te doen voor het naar Thijs gaat
1. Roll log per skin: het paneel zelf wordt de wereld (een bladzijde perkament met inkt, of een sterrenkaart). Dat is de "eigen achtergrond" waar Thijs om vraagt, op een plek die van ons is, zonder de notitie van de gebruiker te verven.
2. Populaire thema's (Minimal, AnuPpuccin, Things, Border) zodra hun download weer werkt.
3. Nieuw skins-plaatje met de beweging (korte GIF per skin).
4. Voor Olaf (later, als klus): de twee CSS-delen overnemen, de licentietekst van de letters in de openbare repo, en `skin-tegels.e2e.mjs` aanpassen: die leest de achtergrond van het token, en die zit nu op `::before`. Dat is een bewuste ontwerpwijziging, met controleur.
