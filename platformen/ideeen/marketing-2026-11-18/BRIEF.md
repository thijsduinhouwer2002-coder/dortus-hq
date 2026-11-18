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

## Aanvulling 18 nov 20:45: tweede ronde (Thijs: "Meer onderzoek")
Vijf extra hoeken, letters F tot en met J. Zelfde regels en uitvoer als hierboven. Lees ook wat A tot en met E al opleverden in deze map, en doe dat niet over.
- **F. Hele reizen van 0 naar de eerste 1.000 gebruikers of $1.000:** 8 tot 10 kleine makers van tools (Blender, JetBrains, VS Code, Chrome, Obsidian) en kleine spellen die het van begin tot eind beschreven. Tijdlijn per week: wat deden ze, wat werkte, wat niet. Gemeenschappelijk recept.
- **G. Lanceerplekken en pers:** Product Hunt, Show HN, BlenderNation, 80.lv, nieuwsbrieven, podcasts, gamepers. Wat leverde het kleine makers echt op (bezoekers, downloads, verkopen), wanneer werkt het, hoe dien je in.
- **H. Zoeken en uitleg:** eigen pagina's op dortus.com, lange YouTube-uitleg en tutorials, SEO voor "how to ..." vragen. Bewijs dat uitlegcontent installs geeft (bijvoorbeeld Flex en Bison-tutorials met 68.000 tot 120.000 weergaven), en wat wij per product kunnen maken. Wat kan automatisch.
- **I. Betaalde advertenties met een klein budget:** Reddit, Google, YouTube, Meta, TikTok Spark, advertenties in nieuwsbrieven, Steam-advertenties. Echte proeven van kleine makers met kosten per installatie of verlanglijst. Alleen als voorstel met bedrag en verwachte opbrengst; Thijs beslist.
- **J. Eigen publiek en doorverwijzen:** maillijst en Discord laten groeien, en van het ene product naar het andere sturen (Hat Tower naar Hats, Click Joints Free naar Pro, Bison & Flex naar volgende plugins). Conversiecijfers van makers, wat werkt binnen de regels van elke winkel (bijvoorbeeld geen koopknop in Blender), wat automatisch kan.
