# Onderzoek distributie en marketing, en wat we kunnen automatiseren (Thijs, 18 nov 20:22)

Thijs: "distributie en marketing? daar moet je even goed onderzoek naar doen, misschien met 5 agents, en ook kijken hoe we dat kunnen automatiseren."

## Waarom
Het afkijk-onderzoek van vandaag (`platformen/ideeen/afkijken-2026-11-18/UITKOMST.md`) liet zien: winnaars zijn niet beter in bouwen maar in alles daarna. Wij hebben ±280 downloads verspreid over 7 live producten en 0 verkopen; TikTok heeft 1 volger. Plan tot 9 dec: Hats (hoofdzaak), Click Joints Free en Pro, Bison & Flex investeren; Garmin licht bijhouden.

## Eerst lezen (niet overdoen wat er al ligt)
`platformen/succes/lessen.md` (groot: zoek met grep), `platformen/succes/verhalen-groei.md`, `commercie/lanceerposts.md`, `commercie/filmpjes/`, `platformen/steam/marketing/` (festplan, makers, pers, curatoren, festivals), `platformen/succes/tools-producthunt.md`, en de geldende besluiten bovenaan `organisatie/besluiten.md`. Noem wat al bekend is in één regel en ga verder waar het ophoudt.

## Vaste grenzen (gelden voor elk advies)
- Niets plaatsen onder de naam van Thijs zonder zijn ja op tekst en beeld. Agents plaatsen nooit zelf. Automatiseren mag dus tot "klaar voor goedkeuring" (bijvoorbeeld Metricool `createScheduledPostForReview`), niet tot "zelf geplaatst", tenzij het om onze eigen winkelpagina, changelog of README gaat.
- Reddit kan de hoofdchat niet openen; daar plaatst Thijs zelf.
- Geen nep: geen nepreviews, geen AI-gezicht of nep-persoon, geen spam, geen regels van een community of winkel breken. Echte beelden uit het product.
- Geld uitgeven (advertenties, betaalde tools) alleen als voorstel met bedrag en verwachte opbrengst; Thijs beslist.

## Wat elke agent oplevert
Bestand `<LETTER>-<onderwerp>.md` in deze map:
1. **Wat werkt aantoonbaar** (met bron en getal, GEZIEN of GOK), voor kleine makers zoals wij.
2. **Per product van ons** (Hats, Click Joints, Bison & Flex, en kort Garmin): de 3 acties met de meeste kans, met waarom.
3. **Wat te automatiseren is**, hoe (tool, API, workflow), wat het kost, en wat Thijs één keer moet doen.
4. **Wat niet werkt of te duur is**, zodat we het niet proberen.
Antwoord aan de hoofdchat: max 15 regels.

## Regels
- **Webpagina's lees je met `curl` in Bash, nooit met WebFetch.** WebFetch vraagt Thijs om toestemming en dan staat alles stil. WebSearch mag om bronnen te vinden.
- Verzin niets. Geen persoonsgegevens. Niet committen; alleen je eigen bestand in deze map schrijven. Nederlands, gewone woorden, geen gedachtestreepjes.
