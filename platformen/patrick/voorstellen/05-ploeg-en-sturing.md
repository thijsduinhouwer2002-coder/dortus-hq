Wat verandert: wie stuurt (Hans, hoofdchat, compagnon-ronde), hoeveel Claudes tegelijk, wanneer er agents en controleurs worden ingezet, en de meetlat voor nieuwe kansen. Dit is grotendeels een **keuze van Thijs**; per punt mijn advies.
Waarom: 1.640 commits in 3 dagen en 0 euro. Niet omdat er slecht gebouwd wordt (Steam-team bouwt echt: hoeden, kroniek, kunst, e2e groen), maar omdat sturing, controle en zoeken veel kosten en weinig opleveren.

---

## 1. Drie sturers voor één bedrijf (advies: twee)
**Bewijs.** Er sturen nu drie lagen: Hans (08:44 en 20:44), de hoofdchat met Thijs, en de compagnon-ronde (elke 3 uur, geplande herinnering in de hoofdchat). Besluiten van Hans worden dezelfde avond door Thijs via de hoofdchat omgedraaid: Garmin "start donderdag" (Hans 20:44) werd "meteen" (Thijs 21:15); Steam "$100 pas na oktober-meting" (Hans 20:44) werd "$100 nu" (Thijs 23:05). De opdracht van Hans zegt nog "nieuwe platformen zijn de hoofdzaak" terwijl het zoeken sinds 18:30 stil ligt. `hoofdmanager.md` begint met "Je draait elke dag om 20:44" en zegt een alinea later "twee keer per dag": gestapelde reparaties.
**Bron.** Project Vend 2 (bron 25): een baas-agent van hetzelfde model "wasn't much help, and might even have been a hindrance"; vaste procedures en afgebakende rollen werkten beter.
**Voorstel.**
- De **hoofdchat met Thijs** beslist over koers, ploeg en geld, en houdt `organisatie/nu.md` bij. Dat gebeurt nu al in de praktijk; maak het officieel.
- **Hans** wordt de **controleur van het bedrijf**, één run per dag (08:44): klopt `nu.md` met wat er gebeurt, wie leverde niets op (runs zonder uitkomst), welke opdracht of rol is verouderd, welk punt hangt al twee dagen. Hij schrijft dat in een dagkaart van 10 regels en zet het in `berichten/` bij wie het aangaat. Productkeuzes van managers keurt hij nog wel goed (die zijn klein genoeg).
- De **compagnon-ronde** blijft het kanaal naar Thijs (dashboard, korte melding). Geen eigen besluiten buiten de opdrachten van Thijs.
**Oplevert:** geen omgedraaide besluiten meer, één Hans-run per dag minder, duidelijk wie wat beslist. **Keuze Thijs.**

## 2. Hooguit drie producten tegelijk, elk met een lanceerdatum (advies: ja)
**Bewijs.** Nu lopen Steam (5 Claudes), TikTok (2), Garmin (1 plus Mila), Click Joints en Bison & Flex (wachten), Rollwright (geparkeerd). 8 Claudes elk uur, ±192 runs per dag. Op 9 nov veranderde de ploeg zes keer (besluiten 9 nov). Het Steam-team van vijf schrijft elkaar veel: 104 commits aan berichten op één dag, en er was al een samenvoegfout (commit "Kunst-LEESMIJ van Daan hersteld (samenvoegfout van Olaf)").
**Bron.** Agent teams-docs (bron 11): begin met 3 tot 5, "coordination overhead increases", lang onbewaakt draaien vergroot verspild werk. Multi-agent kost ±15 keer de tokens van een chat (bron 10).
**Voorstel.**
- Steam: 3 Claudes elk uur (Olaf bouwt, Sanne spel, Mila beeld). Bram terug naar Click Joints zodra die goedgekeurd is, anders mee als tweede bouwer maar om de 2 uur.
- TikTok: Tess en Jet om de 2 uur (er is veel wachten op Thijs: KvK, testaccount).
- Garmin: Gijs om de 2 uur tot er een productkeuze is; pas daarna elk uur.
- Daan: eindakkoord voor indienen, om de 2 uur.
- Elk product heeft in `nu.md` een **richtdatum voor lancering**. Schuift die twee keer: Thijs beslist doorgaan of stoppen.
**Oplevert (GOK):** ±40% minder runs, minder heen en weer, zelfde bouwtempo op Steam. **Keuze Thijs** (hij zei 9 nov 21:15 dat verbruik nu niet belangrijk is; mijn punt is niet alleen verbruik maar ook het overleg).

## 3. Agents en controleurs alleen waar ze iets toevoegen
**Bewijs.** `platformmanager.md` stap 3 zegt: elke run "1 of 2 agents" (bouwer en controleur). 73 commits sinds 8 nov noemen de controleur. Bij kleine taken ("hoed met hap alleen als hij echt gebeten is", "bijnaam Hoard-Toucher") is een aparte controleur duur.
**Bron.** Anthropic: "overinvestment in simple queries" was een veelgemaakte fout (bron 14); een reviewer die problemen moet vinden "will always find something" (bron 20); harde checks (tests, regels die pass/fail geven) zijn de beste controle (bron 22).
**Voorstel (tekst voor platformmanager.md stap 3):** "Doe kleine taken zelf. Zet een agent in als het werk echt parallel kan of veel leeswerk vraagt. Een controleur-agent alleen bij: een ontwerp, iets wat naar buiten gaat (release, winkeltekst, bericht voor Thijs), of een getal waar een besluit op rust. Voor code zijn groene tests de controle. Zeg de controleur kleine stijlpunten over te slaan."
**Oplevert:** minder tokens per run, minder rondes. **Gewoon goed.**

## 4. De meetlat voor een 8 kan bijna niet gehaald worden (advies: vervangen)
**Bewijs.** Een 8 eist alle vier: kleine makers verdienen er nu, bereik voor nieuwkomers, wij bouwen binnen ±2 weken, Thijs verkoopt binnen een week zonder kosten vooraf (`rollen/herweger.md`). Waar kleine makers verdienen zit bijna altijd een drempel (Steam $100 en 30 dagen, TikTok KvK, Garmin $100 per jaar). Daarom kwamen er na ±170 platformen vooral zessen en zevens, en werd Steam een 7 "omdat punt 3 en 4 schuren", waarna Thijs er toch voor koos. De lat zei dus nee tegen wat Thijs wilde.
**Voorstel.** Eén vraag in plaats van vier eisen: **"Wat is de verwachte opbrengst in euro's in de eerste 90 dagen, en wat kost het (weken bouwen, geld, wachten)?"** Met een lage, middel en hoge schatting en de bron van elk getal (GEZIEN, DERDEN, GOK). Kies het beste getal per week werk. Drempels als $100 of een KvK zijn een kostenpost, geen afwijzing.
**Oplevert:** sneller kiezen, en de keuze is te snappen voor Thijs (één getal, met onderbouwing). **Keuze Thijs** (hij stelde de lat mee op).

## 5. Wat ik bewust niet voorstel
- Geen nieuwe rollen. Er zijn al 12 rolbestanden voor 8 actieve Claudes; zes rollen staan uit (verkenner, pionier, zijpadzoeker, herweger, strateeg, commercieel). Advies: zet die zes in `organisatie/rollen/uit/` zodat niemand ze per ongeluk leest.
- Geen "project manager"-agent erbij. Zie punt 1.
