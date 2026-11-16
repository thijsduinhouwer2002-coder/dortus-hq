# Succesverhalen (Lars)

bezig: niets (laatste: BashSupport Pro, klaar 16 nov 2026 ±05:50 NL-tijd). Volgende: een Gumroad-verkoper van Blender-add-ons met openbare cijfers, of een tweede JetBrains-maker met een kleine betaalde taalplugin (zoals BatchCraft of de Flexible-reeks) om te zien wat een nieuwe betaalde plugin zonder eigen publiek haalt. Spoor voor later: TrustMRR toont meer makers met omzet uit Stripe (bijvoorbeeld "3D-AGENT AI for Blender", $7,3k in 30 dagen, nog niet nagekeken).

Nieuwste bovenaan.

---

## 5. BashSupport Pro (Joachim Ansorg, solo, Duitsland, betaalde taalplugin voor Bash en Zsh in JetBrains-IDE's)

Onderzocht 16 nov 2026, run 4. Waarom dit verhaal: JetBrains is ons eerste betaalde doel (6 dec), en Bison & Flex is net als dit een betaalde taalplugin naast een gratis alternatief. BashSupport Pro is de bekendste betaalde taalplugin van een solomaker, en de maker schrijft zelf openlijk over elke stap. Geen cursusverkoper: hij verkoopt de plugin en plugin-werk voor klanten, geen cursus.

### Bronnen
- Marketplace-API, met curl gelezen 16 nov 2026: https://plugins.jetbrains.com/api/plugins/13841 (Pro), `/api/plugins/4230` (oude gratis BashSupport), `/updates`, `/comments` en `/rating` van beide.
- Zijn eigen nieuwsberichten, met curl gelezen 16 nov: https://www.bashsupport.com/news/ , vooral "BashSupport's future" (18 jul 2019), "Current status of BashSupport Pro" (20 nov 2019), "BashSupport Pro released" (26 feb 2020), "1.3 and future of open-source BashSupport" (2 jun 2020), "1.4, now standalone" (18 jul 2020), "Pricing Update" (8 apr 2024), "Celebrating six years" (24 mrt 2026).
- Prijspagina en vergelijkingspagina, 16 nov: https://www.bashsupport.com/pricing/ en https://www.bashsupport.com/features/
- Interview uit 2018 (vóór Pro, over hoe hij begon): https://tomassetti.me/jetbrains-plugins/
- Zijn bedrijfssite: https://www.j-a.dev/
- Niet gevonden: omzet of aantal kopers. Hij noemt ze nergens, ook niet in interviews (zoektocht 16 nov). Alles over geld hieronder is dus GOK of afgeleid.

### Cijfers
- **Pro: 624.199 downloads, 63 reviews, cijfer 5 (59 keer 5 sterren, 1 keer 4)** (GEZIEN, API 16 nov). Downloads tellen updates mee.
- **Oude gratis BashSupport: 14.499.371 downloads, 118 beoordelingen** (GEZIEN). Pro staat dus op 4,3% van de downloads van de gratis voorganger (rekensom). In onze eigen marktmeting (`platformen/jetbrains/marktmeting-2026-11-06.md`) staat Nginx op dezelfde orde: betaald ±10% van gratis.
- **Eén review per ±10.000 downloads**, en 22 van de 63 reviews kwamen in 2020, het jaar van de overstap (GEZIEN, telling per jaar: 2020 22, 2021 15, 2022 3, 2023 11, 2024 5, 2025 3, 2026 4).
- **Werk: "close to 4,500 hours" in zes jaar**, dus ±750 uur per jaar (EIGEN OPGAVE, bericht 24 mrt 2026). **94 builds op de Marketplace tussen 19 nov 2024 en 6 nov 2026** (GEZIEN), vaak in paren voor twee IDE-lijnen, dus ±47 echte versies in twee jaar: ongeveer elke twee weken een update. 236 meldingen in zijn openbare issue-tracker op GitHub (GEZIEN via zoek-API).
- **Gebruikers nu (GOK):** de laatste versie (5.0.13, 6 nov) haalde in 10 dagen ±3.000 downloads over twee builds (GEZIEN); alle builds van 2025 samen 90.854. Dat wijst op enkele duizenden actieve installaties, inclusief proefgebruikers. Hoeveel er betalen weet niemand buiten JetBrains.
- **Prijs (GEZIEN 16 nov):** persoonlijk $39 per jaar of $3,90 per maand, zakelijk $99 per jaar of $9,90 per maand. Tweede jaar ±20% goedkoper, derde jaar ±40%. Na 12 maanden een blijvende licentie (fallback). Proef 30 dagen zonder registratie. Gratis voor open bron en onderwijs via JetBrains. Volumekorting voor bedrijven vanaf 10 licenties.
- **Prijs bij de start (feb 2020 tot jun 2024): $23 persoonlijk, $68 zakelijk per jaar** (GEZIEN, bericht 8 apr 2024). In nov 2019 noemde hij nog "$10 to $20 per year" voor persoonlijk. Na ruim vier jaar ging de prijs 70% omhoog.

### Wat hij deed, in volgorde
1. **2009: een gratis plugin voor een wedstrijd.** BashSupport won de eerste prijs van een plugin-wedstrijd van JetBrains (±$8.000, zegt hij in het interview). Daarna tien jaar gratis en open source, in zijn vrije tijd. Hij werd "the most widely used community plugin": de laatste versie alleen al meer dan 1 miljoen downloads (EIGEN OPGAVE, jul 2019).
2. **Jul 2019: JetBrains stopt een gratis Shell-plugin in elke IDE.** Dat botste met zijn plugin. Hij schreef meteen en eerlijk wat hij ging doen: "I'm not planning to compete with JetBrains's offering", de gratis plugin gaat in onderhoud, en een betaalde Pro komt bovenop die van JetBrains. Hij gaf ook toe dat een miljoen gebruikers als hobby niet meer ging.
3. **Nov 2019: vooraf vertellen wat Pro doet en ongeveer kost.** De eerste versie draait om één ding dat JetBrains niet had: een debugger. Prijs "most likely in the range of $10 to $20 per year", zakelijk duurder. Testers konden zich melden. Een nieuwsbrief op elke pagina.
4. **26 feb 2020: Pro 1.0 op de Marketplace**, acht maanden na de start van betaalde plugins daar (JetBrains begon op 26 jun 2019 met 10 betaalde plugins, in jul 2020 waren het er 46: DERDEN, JetBrains-blog). Hij zat er dus vroeg bij.
5. **De gratis plugin als wegwijzer.** In de beschrijving van de oude BashSupport (14,5 miljoen downloads) staat nog steeds: gestopt, gebruik BashSupport Pro, "attractively priced starting at 2.30 USD per month", met drie zoete redenen: 30 dagen proef, **25% korting tot 1 okt 2020 met de code BASHSUPPORT_THANKS**, en je oude instellingen werken gewoon (GEZIEN). Wie vroeger iets bijdroeg kreeg een gratis licentie. JetBrains staat zo'n verwijzing in een beschrijving dus toe (anders dan extensions.blender.org, zie besluit Bram 15 nov).
6. **Jun 2020: de gratis plugin stopt echt** (geen versie meer voor 2020.2). Tegelijk maakte hij Pro beter dan de oude ("superior to the old BashSupport plugin"), zodat overstappen geen stap terug was. In 2020 kwamen 22 van zijn 63 reviews.
7. **Jul 2020: los van JetBrains' plugin.** Bovenop de gratis Shell-plugin bouwen werkte niet: elke reparatie moest via JetBrains en duurde tot 4 maanden. Pro werd een eigen, complete plugin, met de oude instellingen van beide plugins nog bruikbaar.
8. **2021 tot 2025: steeds verder van wat gratis is.** Testrunner (bats-core), scripts op een andere machine draaien en debuggen, hernoemen, Zsh (versie 5.0, aug 2025), eigen opmaker. Een vergelijkingspagina met vinkjes tegen de gratis Shell van JetBrains én tegen VS Code (GEZIEN). Bijna alles waar je voor betaalt is iets wat de gratis plugin bewust niet doet.
9. **Apr 2024: prijs omhoog, netjes.** Twee maanden vooraf aangekondigd, wie wilde kon tot drie jaar vooruit betalen tegen de oude prijs, de korting voor trouwe klanten bleef, en "I don't like this" had een eigen kopje met een mailadres. Nieuw: volumekorting voor bedrijven.
10. **Mrt 2026: zes jaar, actie met de prijs van 2020** voor een maand. Hij verkoopt ook plugin-werk voor klanten (j-a.dev), en zegt daar dat AI-agents nu een deel van het werk aan zijn plugins doen.

### Drie lessen
1. **De betaalde plugin verkoopt precies wat de gratis plugin van de grote speler niet doet, en laat dat zien in een tabel.** Een debugger, een testrunner, op afstand draaien: werk dat JetBrains voor een gratis plugin niet gaat doen. Gewoon kleuren en aanvullen gaf hij bewust op ("I'm not planning to compete"). Dit is de tweede keer na Copilot dat het betaalde deel iets is wat de gebruiker niet zelf of gratis heeft.
2. **Het publiek kwam eerst, gratis, en jaren lang.** Tien jaar en 14,5 miljoen downloads gratis, daarna een betaalde opvolger die nu op 4,3% van die downloads staat. Bij de overstap gebruikte hij zijn gratis plugin als bord naar Pro, met korting en proef. Wij hebben bij Bison & Flex geen eigen gratis publiek; het gratis alternatief (Bison Language Support, 13.020 downloads, GEZIEN 8 nov in `commercie/jetbrains-bison-flex/indienen.md`) is van iemand anders. Met dezelfde verhouding is dat ±560 downloads voor een betaalde Bison-plugin in totaal, over jaren (GOK, en downloads zijn geen kopers).
3. **Rustig en lang volhouden, met eerlijke prijsstappen.** Laag begonnen ($23), na ruim vier jaar omhoog naar $39, met vooruitbetalen tegen de oude prijs, korting in jaar 2 en 3, en een blijvende licentie na een jaar. Elke twee weken een update, zes jaar lang, 4.500 uur. Zakelijk kost 2,5 keer persoonlijk (past in hoofdles 1).

### Eerlijk: wat niet zomaar voor ons geldt
- Hij had tien jaar naam en een miljoen gebruikers vóór hij iets vroeg. Dat valt niet te kopiëren; wij starten bij 0.
- Bash wordt door bijna elke ontwikkelaar gebruikt. Bison en Flex door een klein deel (compilervakken, oudere C-projecten). De markt is vele malen kleiner (GOK, niet gemeten).
- Of hij ervan kan leven weten we niet. Dat hij ook klantwerk verkoopt en in 2024 de prijs verhoogde "to let us keep working on BashSupport Pro" wijst erop dat de plugin alleen misschien niet genoeg is (GOK).
- Hij beantwoordt maar 9 van de 63 reviews op de Marketplace (GEZIEN). Hulp loopt via zijn forum en issue-tracker. Dat gaat tegen hoofdles 2 in; zijn cijfer is toch 5.

### Voorstel voor Dortus deze week
**Wie:** Chris (winkeltekst, `commercie/jetbrains-bison-flex/`), met Jet voor de feiten; zodra Bison & Flex zichtbaar is.
**Wat:** een vergelijkingstabel zoals die van BashSupport Pro, met vinkjes in drie kolommen: Bison & Flex Pro, Bison & Flex gratis, en Bison Language Support (het gratis alternatief, 13.020 downloads). Alleen rijen die waar zijn en die een koper merkt (bijvoorbeeld het werk tussen scanner en grammatica en de meldingen, als Jet bevestigt dat de ander dat niet heeft). Zet hem op dortus.com bij Bison & Flex en een korte versie in de Marketplace-beschrijving, met de link. Zet onder de prijs dezelfde zin als Ansorg: wie een gratis licentie voor onderwijs of open bron gebruikt, wordt gevraagd om een review. Reviews zijn schaars (bij hem 1 op de 10.000 downloads), en studenten zijn bij Bison en Flex waarschijnlijk een grote groep (GOK, staat ook al in `indienen.md`). Kost een uur, geen geld, geen nieuwe code.
**Voor Jet, ter info:** reken op dag 30 niet met de 2 tot 5% uit `doelen.md`. Een betaalde taalplugin naast een gratis plugin haalt in de twee gevallen die we kennen 4 tot 10% van de downloads van de gratis plugin (BashSupport, Nginx), en dat over jaren.

---

## 4. Copilot for Obsidian (Logan Yang, Brevilabs, twee vaste bouwers, AI-plugin met abonnement en levenslange licentie)

Onderzocht 16 nov 2026, run 3, opdracht van de hoofdchat ("een Obsidian-plugin met betaalde extra's die echt verkoopt, zodat we zien wat Rollwright mist"). Waarom dit verhaal: de enige betaalde Obsidian-plugin waarvan de omzet openbaar en gecontroleerd is, maand voor maand. Geen cursusverkoper: de cijfers komen rechtstreeks uit Stripe.

### Bronnen
- TrustMRR, profiel Brevilabs, met curl gelezen 16 nov 2026 (03:20 NL-tijd), ook de machineleesbare versie: https://trustmrr.com/startup/brevilabs en https://trustmrr.com/startup/brevilabs.md. TrustMRR haalt de omzet zelf op met een Stripe-sleutel van de maker ("Revenue is verified with Stripe API key", laatst bijgewerkt 15 nov 2026 20:51 UTC). De tekst over het bedrijf op die pagina is wel door de maker of TrustMRR zelf geschreven en niet gecontroleerd.
- Prijspagina, 16 nov: https://www.obsidiancopilot.com/en/pricing
- Bedrijfssite, 16 nov: https://brevilabs.com/
- De openbare code en de hele geschiedenis (git clone zonder bestanden, 16 nov): https://github.com/logancyang/obsidian-copilot. Daaruit de data van commits, tags en wie wat schreef.
- Downloads: `community-plugin-stats.json`, eerder gemeten door Olaf in `platformen/obsidian/volgend-product.md` (Copilot 3.340.702 in totaal).
- Tegenvoorbeeld: een maker met een eenmalige, offline Pro-licentie zoals Rollwright, DEV 19 jun 2026 (0 reacties): https://dev.to/ibrh96prog/im-not-a-software-engineer-but-i-shipped-an-obsidian-plugin-with-zero-servers-and-offline-4i14. Op Indie Hackers staat een bericht met de titel "Shipped my 7th one-time-purchase Obsidian plugin. Real numbers: ~7 views/day, 2 sales total" (https://www.indiehackers.com/post/shipped-my-7th-one-time-purchase-obsidian-plugin-real-numbers-7-views-day-2-sales-total-distribution-is-the-whole-problem-9a46ab4295). Alleen de titel gezien (Cloudflare blokkeert curl), dus wie het schreef en wat erin staat weet ik niet.
- Niet gevonden: een interview of blog van Logan Yang over hoe hij de eerste betalers kreeg (zoektocht 16 nov). FirstMRR heeft een stuk over Brevilabs, maar die site lag eruit (503).

### Cijfers
**Omzet, GEZIEN via TrustMRR (Stripe), alle bedragen bruto in dollars:**

| Periode | Omzet |
|---|---|
| Alles sinds de start | $926.038 |
| Laatste 12 maanden | $468.348 |
| Laatste 6 maanden | $177.538 |
| Laatste 3 maanden | $78.331 |
| Laatste 30 dagen | $19.286 (-17,3%) |

Per maand: dec 2025 $53.160, jan 2026 $55.789, **feb 2026 $66.646 (top)**, mrt $35.096, apr $34.309, mei $38.223, jun $36.054, jul $29.259, aug $33.873, sep $32.590, **okt $18.994**, nov tot en met de 15e $10.084.
- MRR (vaste maandomzet uit abonnementen) $17.600, **1.336 actieve abonnementen**, winstmarge 95% (GEZIEN, TrustMRR).
- Vóór december 2025 (jan tot nov 2025): $926.038 min $468.348 is **±$458.000 in ±11 maanden**, gemiddeld ±$42.000 per maand (rekensom op GEZIEN).
- **Let op:** het is de hele Stripe van Brevilabs, niet alleen Copilot. Brevilabs verkoopt ook advieswerk ("a four-week, $45k AI product sprint", GEZIEN op brevilabs.com) en twee nieuwere producten (Miyo en OpenArtifacts). Hoeveel daarvan in de omzet zit, is niet te zien. Copilot is wel het oudste en grootste product (GOK dat het meeste van Copilot komt).

**Prijzen nu (GEZIEN 16 nov):** Free $0 (eigen API-sleutel, lokale modellen, je eigen Claude- of ChatGPT-abonnement, zonder account). Plus $14,99 per maand of $139,99 per jaar (gehoste modellen, betere webzoeker, meerdere agents tegelijk). **Supporter $349,99 eenmalig**, doorgestreept van $499,96: twee jaar Plus, levenslang Miyo en OpenArtifacts, levenslang zelf hosten, vroege toegang, 15% extra tegoed. Terugbetalen binnen 14 dagen.

**Downloads:** 3.340.702 in totaal (Olaf, community-plugin-stats). De prijspagina zegt zelf "2.5M". Downloads tellen ook updates mee, dus het aantal echte gebruikers is veel lager (GOK, hoeveel weet niemand buiten Obsidian).

**Rekensom die ertoe doet (GOK op GEZIEN):** 1.336 abonnementen op 3,34 miljoen downloads is **0,04% per download**. ±$20.000 per maand op 3,34 miljoen downloads is ±$0,006 per download per maand. Neem je aan dat 1 op de 10 downloads een echte, actieve gebruiker is (GOK), dan betaalt 0,4% van de gebruikers een abonnement. Dat is 5 tot 12 keer minder dan de 2 tot 5% in het rekenvoorbeeld van `organisatie/doelen.md`. En dit is de meest gedownloade AI-plugin van Obsidian, met een betaalde laag die echt iets levert.

### Wat ze deden, in volgorde (uit de code en de pagina's)
1. **Maart 2023: gratis en open source, met je eigen OpenAI-sleutel.** Eerste commit 30 maart 2023, vier maanden na ChatGPT. 119 commits in april 2023. Hij zat vanaf dag één op de golf.
2. **Twintig maanden alleen gratis.** Van maart 2023 tot november 2024 geen betaalde laag. In die tijd werd het de grootste AI-plugin van Obsidian.
3. **Oktober 2024: een tweede vaste bouwer** (Zero Liu, eerste commit 26 okt 2024). Sinds half april 2026 schrijft die het meeste: 568 commits tegen 93 van Logan Yang (GEZIEN in de git-geschiedenis). Dit is dus geen solomaker meer.
4. **21 nov 2024: Copilot Plus als alfa voor testers. 15 jan 2025: bèta voor iedereen.** Brevilabs is opgericht in januari 2025 (TrustMRR). De betaalde laag verkoopt wat de gebruiker niet zelf heeft: gehoste modellen en eigen zoek- en embeddingmodellen ("copilot-plus-small", "copilot-plus-large", "copilot-plus-flash"), webzoeken, plaatjes in de chat. Gratis blijft alles wat met je eigen sleutel kan.
5. **5 feb 2025: een "believer"-klasse** met een eigen model alleen voor hen (commit "Add believer exclusive model"). Dat is de voorloper van de huidige Supporter van $349,99 eenmalig. De ±$42.000 per maand in 2025 met nu maar $17.600 MRR wijst erop dat een groot deel van het geld uit eenmalige levenslange licenties kwam (GOK, de verdeling toont TrustMRR alleen na inloggen).
6. **Aug 2025: Plus uit de bèta, met een agent.** Daarna versie 3 (aug 2025) en elke maand tientallen commits.
7. **Feb 2026: de top, daarna gehalveerd.** Van $66.646 in februari naar $35.096 in maart. Waarom zegt niemand. Mijn GOK: jaarabonnementen van de bèta-kopers van jan en feb 2025 verlengden in jan en feb 2026, en een deel stopte daarna.
8. **2026: de golf keert.** Gratis plugins die Claude Code en Codex in de kluis zetten groeien het hardst (Claudian 300.668 downloads in 30 dagen, Agent Client 34.048, gemeten door Olaf, `volgend-product.md`). Copilot volgt: **versie 4.0 op 11 aug 2026 met OpenCode, Claude Code en Codex**, en op de prijspagina staat nu bij Free "Use your Claude or ChatGPT subscription". Dat haalt een reden weg om Plus te kopen. Twee maanden later, in oktober, zakt de omzet van $32.590 naar $18.994. Of dat oorzaak en gevolg is, weet ik niet (GOK).
9. **Nu: breder dan één plugin.** Brevilabs zet Miyo (lokale contextdienst) en OpenArtifacts naast Copilot, stopt die in de Supporter-licentie, en verkoopt advieswerk. In de README vraagt Copilot alle gratis gebruikers om een gratis account en de Discord ("Sign up free and join our Discord"): een lijst van gebruikers die ze later iets kunnen aanbieden.

### Drie lessen
1. **Eerst groot gratis, pas daarna betalen, en dan alleen voor wat de gebruiker zelf niet heeft.** Twintig maanden gratis tot het de grootste AI-plugin was, daarna een betaalde laag met gehoste modellen. Zelfs dan betaalt maar 0,04% per download een abonnement. Bij Rollwright (40 downloads, skins van $6) is de verwachte verkoop met die verhouding nul. Dat ligt dus niet aan de skins of de betaalweg, maar aan het bereik.
2. **Eén dure eenmalige klasse brengt veel geld.** Supporter $349,99 (eerst "believer") naast $14,99 per maand. Dit past in hoofdles 1 (meer dan één prijs). Het verschil met Cleave en CatPin: hier is de duurste klasse 23 keer de maandprijs, niet $5 tot $13 extra. De top van $66.646 in één maand haal je niet met abonnementen van $14,99 alleen (GOK: dat zijn ±4.400 maandabonnementen, terwijl er nu 1.336 zijn).
3. **Een betaalde laag die AI doorverkoopt kan snel leeglopen.** Toen gebruikers hun eigen Claude- of ChatGPT-abonnement konden gebruiken (gratis plugins, en daarna Copilot zelf), viel de omzet van ±$42.000 per maand in 2025 naar ±$20.000 nu. Ook de grootste maker moest volgen en zijn gratis deel ruimer maken. Wat je verkoopt moet iets zijn wat een abonnement elders niet ook al geeft.

### Eerlijk: wat niet zomaar voor ons geldt
- Copilot is een AI-product in de drukste hoek. Mensen betalen voor AI meer en vaker dan voor dobbelstenen (GOK). De verhouding 0,04% is voor Rollwright eerder te gunstig dan te streng.
- De omzet is van heel Brevilabs, inclusief advieswerk dat $45.000 per opdracht vraagt. Eén opdracht zou al een maand vertekenen. Ik zie geen pieken van die grootte per dag (hoogste dag in de laatste 30: $1.562), maar voor eerdere maanden kan ik het niet uitsluiten.
- Downloads zijn geen gebruikers. De 0,4% per gebruiker is een GOK op een GOK.
- Twee vaste bouwers sinds eind 2024, ex-Google en ex-Uber (zegt de eigen site). Dat is meer menskracht dan een solomaker.

### Wat Rollwright mist (de vraag van de hoofdchat)
Niet de betaalweg en niet de skins zelf: die zijn er en werken (Polar, $6, offline na de controle). Wat mist, in volgorde:
1. **Bereik.** Copilot had miljoenen downloads voor het iets vroeg. Rollwright heeft er 40 (Olaf, 15 nov). Met de verhouding van Copilot zijn voor €350 per maand ±60.000 tot 70.000 downloads nodig (GOK: $400 / $0,006). Met eenmalige skins van $6 eerder meer.
2. **Een betaalde kant die iets doet wat gratis niet kan.** Copilot verkoopt rekenkracht en modellen. Skins zijn uiterlijk; dat werkt in spellen (Rusty's Supporter Pack, 11% bij Fenna), maar daar is het spel zelf al gekocht of gespeeld door tienduizenden.
3. **Een lijst van gratis gebruikers.** Copilot vraagt elke gebruiker om een gratis account en Discord. Rollwright heeft niets waarmee we gebruikers later kunnen bereiken, behalve de forumdraad (19 keer bekeken).
4. **Een dure eenmalige klasse.** Kan erbij, maar heeft pas zin met bereik.

### Voorstel voor Dortus deze week
**Wie:** Olaf (Obsidian-manager), in `platformen/obsidian/volgend-product.md`; Hans kijkt het na bij de volgende weekkeuze.
**Wat:** een vaste verdientoets voor elk kandidaat-product op Obsidian, vóór er gebouwd wordt, met de enige gecontroleerde verhouding die we hebben: **±$0,006 omzet per download per maand, 0,04% abonnees per download** (Copilot, Stripe via TrustMRR, 16 nov 2026). Per kandidaat drie regels: (a) hoeveel downloads haalt de beste plugin in die hoek per maand (GEZIEN in de stats), (b) wat levert dat op met die verhouding, (c) wat zit in de betaalde laag dat de gebruiker niet al gratis of via een eigen abonnement heeft. Komt (b) voor de hele hoek onder €350 per maand, dan geen betaald product in die hoek. Kost Olaf een halfuur, en voorkomt een tweede Rollwright. Voor Rollwright zelf: geen werk meer aan betaalde skins tot er minstens een paar duizend downloads zijn; die tijd naar bereik of naar een ander product.
**Voor de hoofdchat, ter info:** het rekenvoorbeeld in `organisatie/doelen.md` gaat uit van 2 tot 5% betalende gebruikers. De grootste betaalde Obsidian-plugin zit op ±0,4% (GOK op GEZIEN). Dat is een vraag voor Thijs, niet voor mij, want doelen.md is van hem.

---

## 3. CatPin (Alex Sokol, solo, één product, splitsen voor 3D-printen, Superhive en Gumroad)

Onderzocht 16 nov 2026, run 2, opdracht van de hoofdchat. Waarom dit verhaal: de sterkste nummer één in onze hoek (figuren printen), van een maker zonder eerder product, en hij verkoopt in drie prijsklassen, waaronder een Business-licentie.

### Bronnen
- Superhive, met curl gelezen 16 nov 2026 (00:50 NL-tijd): productpagina, FAQ, documentatie, reviews en versiepagina: https://superhivemarket.com/products/catpin, https://superhivemarket.com/products/catpin/faq, https://superhivemarket.com/products/catpin/docs, https://superhivemarket.com/products/catpin/ratings
- Gumroad, productpagina (schema.org-gegevens in de pagina) en de openbare zoek-API, 16 nov: https://alexsokol.gumroad.com/l/catpin en https://gumroad.com/products/search?query=catpin
- 80 Level, Emma Collins, 5 okt 2026: https://80.lv/articles/prepare-your-3d-models-for-printing-with-this-blender-add-on
- Digital Production, Bela Beier, 9 okt 2026, met prijzen gecontroleerd op 7 okt: https://digitalproduction.com/2026/10/09/catpin-blender-cuts-3d-printing/
- Zijn tutorial (titel via de oEmbed van YouTube; kijkcijfers en datum niet te lezen, YouTube blokkeert curl): https://youtu.be/KVPY63W0ovg, kanaal https://youtube.com/@alex_sokol_art
- Eerdere metingen van onze ploeg: Olaf (blender-2), 8 nov 2026, `platformen/blender-2/status.md` en `platformen/blender-2/data/superhive-print-2026-11-08.jsonl`.
- Niet gelukt: Reddit (blokkeert curl), Instagram, Telegram, ArtStation. Geen interview of devlog van de maker gevonden (zoektocht 16 nov). Hoe hij zijn eerste kopers kreeg, zegt hij nergens.

### Cijfers
- **Superhive:** 400+ verkopen, 4 reviews (alle vier 5 sterren), "Published 3 months ago", dus ±half augustus 2026 (GEZIEN 16 nov). Al 400+ op 8 nov (GEZIEN Olaf), dus in de laatste week geen nieuw blok; het volgende blok is waarschijnlijk 500+ (GOK over hoe Superhive telt).
- **Gumroad:** 84 reviews, gemiddeld 4,8 (GEZIEN 16 nov). Op 8 nov waren het er 81 (GEZIEN Olaf). Dus ±3 nieuwe reviews per week op Gumroad, tegen 4 in 3 maanden op Superhive. Hij heeft maar 1 product op Gumroad.
- Wat 84 reviews op Gumroad betekent in verkopen weet ik niet. Gumroad toont geen verkoopteller. Gumroad vraagt kopers in hun bibliotheek om sterren, dus daar schrijven waarschijnlijk veel meer kopers een review dan op Superhive (GOK). Bij Kambari zagen we op Superhive 1 review op 50 tot 140 verkopen; dezelfde verhouding op Gumroad toepassen kan niet.
- **Drie prijsklassen op Superhive** (GEZIEN 16 nov, nu 20% korting): Basic $27 ($21,60), Supporter Edition $40 ($32), Business / Studio $90 ($72) voor tot vijf mensen. Op Gumroad $30, nu $21.
- **De prijs veranderde, met bijna altijd korting:** 7 okt: Basic $30 met korting $24, Supporter $45 naar $36, Business $100 naar $80, extra jaar support 25% (DERDEN, Digital Production). 8 nov: $24 (GEZIEN Olaf). 16 nov: lijstprijs omlaag naar $27, $40 en $90, korting naar $21,60, en een extra jaar support nu 50% van de prijs (GEZIEN). Op alle drie de meetmomenten stond er een korting. Zoekresultaten tonen de pagina met `src=on_sale` en `src=popular`, dus hij stond in de lijsten "on sale" en "popular" van Superhive (GEZIEN in de links van de zoekmachine; hoe vaak en hoe lang weet ik niet).
- **Business-licentie:** 3,3 keer Basic voor vijf plaatsen. Ter vergelijking Click Joints Pro: Studio $45 is 3,75 keer Personal $12 (besluiten 15 nov 19:36).
- **Supporter Edition:** $13 meer dan Basic voor dezelfde add-on plus "an exclusive, personal thank-you letter from the add-on's creator" en "your name featured in the creator's Instagram Highlights". Hoeveel kopers die kiezen toont Superhive niet.
- Omzet, GOK: alleen Superhive, 400 tot 500 verkopen x ±$22 (meestal met korting) is $8.800 tot $11.000 bruto in 3 maanden, voor afdracht. Gumroad komt daar bovenop, maar hoeveel is niet te zeggen.
- Versies: 1.0.7 vóór 5 okt (80 Level), 1.0.8 in de oktober-update (Digital Production). De versiepagina op Superhive is leeg ("No versions found"), dus anders dan Cleave toont hij zijn versies daar niet.

### Wat hij deed, in volgorde (uit de pagina's afgeleid)
1. **Half augustus: één add-on, één klus.** Splitsen met pin en gat, rechte en gebogen snede, origineel blijft heel, alles in één keer exporteren naar STL. Op twee winkels tegelijk: Superhive en zijn eigen Gumroad. Of Gumroad eerder kwam weet ik niet.
2. **Antwoord op elke review, met een belofte met datum.** Een koper vraagt een losse deuvel (twee gaten en een los pinnetje). Zijn antwoord: "Yes, I can! It'll be available in the next Update on September 9". Alle vier de reviews op Superhive kregen een antwoord.
3. **Snel nieuwe functies:** handmatige snede, veelhoek-snede (ogen, monden, autoruiten los printen), tot vijf verbinders per snede, dubbelzijdige verbinder, controle op open randen (80 Level, 5 okt). Versie 1.0.8 in oktober.
4. **Begin oktober: twee vakbladen schrijven erover**, 80 Level (5 okt) en Digital Production (9 okt). Of hij die zelf tipte of dat ze het zelf vonden, weet ik niet (GOK). 80 Level heeft een betaalde rubriek "Promote", maar dit stuk staat onder Nieuws en Marketplace; of het betaald was, is niet te zien.
5. **Prijs en korting:** duurdere lijstprijs met een vaste korting, drie klassen, en in november een lagere lijstprijs met weer korting.
6. **De pagina vangt slechte reviews af:** "If something does not behave as expected, please contact support before leaving a review", met een lijstje van de vijf meest voorkomende oorzaken (schaal, eenheden, dicht model). Ook een eerlijk blok "Know what CatPin can handle" met wat niet werkt.

### Drie lessen
1. **Verkoop zakelijke kopers apart.** Een Business-licentie voor vijf plaatsen ($90) naast Basic ($27), met als doelgroep "3D-printing studios" en "STL model creators" op de pagina. Wie modellen verkoopt (en dat zijn er in de printwereld veel, zie McGybeer bij Joris), betaalt graag meer voor een licentie die bij zijn bedrijf past. Wij hebben die klasse al (Studio $45), dus dit bevestigt de keuze.
2. **Twee winkels, en de kleinere kan de grotere zijn.** Op Gumroad 84 reviews, op Superhive 4. Ook als Gumroad veel meer reviews per koper oplevert, is Gumroad bij hem geen bijzaak (GOK op GEZIEN). Wij staan voor Click Joints Pro alleen op Superhive.
3. **Vakbladen schrijven over kleine add-ons, juist als ze iets laten zien.** Na Kambari (CG Channel na 6 dagen) de tweede maker zonder publiek die binnen een paar weken in een vakblad stond, nu twee keer. Beide stukken zijn feitelijk en volgen de productpagina bijna letterlijk: een goede pagina met filmpjes is wat een redacteur nodig heeft.

### Eerlijk: wat niet zomaar voor ons geldt
- Zijn add-on doet precies wat Click Joints bewust niet doet (splitsen). Hij zegt zelf: "Articulated, rotating and movable joints are not currently supported." Dat is onze hoek. Maar Cleave heeft sinds 28 okt kogelgewrichten, dus "beweegbaar" is niet meer van ons alleen.
- Of de vaste korting werkt of alleen goedkoop oogt, kan ik niet meten. Ik zie wel dat hij hem steeds aan heeft en dat hij in de lijst "on sale" van Superhive staat.
- Waar zijn eerste kopers vandaan kwamen weet ik niet. Hij heeft YouTube, Instagram en Telegram, maar die kon ik niet lezen.

### Voorstel voor Dortus deze week
**Wie:** Chris (schrijft de tip), Thijs (verstuurt hem, want het gaat onder zijn naam), na de goedkeuring van Click Joints Pro (verwacht 18 tot 20 nov).
**Wat:** zodra Click Joints Pro live staat, een korte nieuwstip naar drie vakbladen die aantoonbaar over kleine Blender-add-ons voor printen schrijven: CG Channel (schreef over Smart Remesh), 80 Level en Digital Production (allebei over CatPin). Chris zet in `commercie/` per blad een mail van 5 zinnen klaar: wat het doet (gewrichten die bewegen, iets wat CatPin niet doet), voor wie, prijs, link naar de pagina en het demofilmpje, en één GIF. Daarna een regel op `organisatie/lijst-thijs.md` met de drie contactadressen van de redacties en wat hij moet doen. Kost niets en is in een uur klaar. Of het werkt is een GOK, maar het is twee keer gezien bij makers zonder publiek.
**Erbij, voor later (niet deze week):** Click Joints Pro ook op Gumroad, zoals CatPin. Dat vraagt een Gumroad-account van Thijs en Gumroad houdt 10% in (besluiten 6 nov). Pas zinvol als Pro op Superhive verkoopt.

---

## 2. Cleave (V4SS3UR, solo, één product, 3D-printen op Superhive)

Onderzocht 15 nov 2026, run 1, opdracht van de hoofdchat. Waarom dit verhaal: een nieuwkomer zonder publiek, in precies onze hoek (figuren printen, gewrichten), in een drukke categorie. Onze ploeg kent Cleave al als concurrent van Click Joints (`producten/blender-gewrichten/ontwerp.md`); hier gaat het om hoe hij het aanpakte.

### Bronnen
- Productpagina, versiegeschiedenis en reviews, met curl gelezen 15 nov 2026: https://superhivemarket.com/products/cleave, https://superhivemarket.com/products/cleave/versions, https://superhivemarket.com/products/cleave/ratings
- Zijn YouTube-filmpjes (titels via de openbare oEmbed van YouTube; kijkcijfers niet te lezen, YouTube gaf 429): kanaal https://www.youtube.com/@V4SS3UR
- Concurrenten in dezelfde categorie, productpagina's Superhive 15 nov: catpin, split-3dprint, printsplitter, easy-print, split-it, cutandkey, print-forge, dovetail-key.
- Geen interview, devlog of Reddit-post van de maker gevonden (zoektocht 15 nov).

### Cijfers (GEZIEN 15 nov 2026, tenzij anders vermeld)
- 100+ verkopen, 3 reviews (alle drie 5 sterren), "about 2 months ago" gepubliceerd. Versie 1.0.0 op 23 sep 2026, dus ±7,5 weken.
- Prijs $23, plus een tweede keuze "Support the developer" van $28: dezelfde download, $5 extra "to help fund future updates". Nu een coupon van 10% voor een week.
- De maker heeft maar 1 product in de winkel: geen eerder publiek op Superhive.
- **12 versies in 6 weken:** 1.0.0 (23 sep), 1.1.0 (24 sep), 1.2.0 (4 okt), 1.2.1 (6 okt), 1.3.0 (10 okt), 1.4.0 (11 okt), 1.5.0 (20 okt), 1.5.1 (21 okt), 1.6.0 (28 okt, kogelgewrichten), 1.6.1 (2 nov).
- Omzet, GOK: 100 tot 200 verkopen x $23 is $2.300 tot $4.600 bruto in 7,5 weken, voor afdracht en coupons.
- De categorie "model splitsen voor printen" is druk: Dovetail Key (Kambari, met publiek) 800+, CatPin 400+, Split 3D Print 400+ (teller telt ook gratis downloads), Cleave 100+, Split It 10+, Easy Print 10, Printsplitter, Cut and Key en PrintForge geen blok (onder 10). Cleave is de enige nieuwkomer van de laatste 2 maanden boven de 10+.

### Wat hij deed, in volgorde
1. **Versie 1.0 met één heldere belofte:** "Too big to print? Split it." Splitsen waar het model buigt (nek, schouders, knieën), verbinders in echte millimeters, controle tegen je printer.
2. **Daarna bijna elke week een versie**, steeds iets wat kopers vragen of nodig hebben: Make Manifold, printerlijst (120+ modellen) en 3MF-export, dowels en staafkanalen, een "Simple mode" omdat het paneel te vol werd, en op 28 okt kogelgewrichten voor beweegbare figuren. Elke versie staat met datum op de pagina, dus een koper ziet dat het product leeft.
3. **Hij beantwoordt elke review zelf, binnen een paar dagen**, bedankt, en vraagt om Blender-versie, besturingssysteem en een voorbeeldbestand bij een crash. Op de klacht "te veel menu's" antwoordt hij dat hij eraan werkt; in 1.5.0 kwam de "Simple mode".
4. **Uitleg op de plek waar mensen zoeken:** vier YouTube-filmpjes met titels die mensen intypen ("Cleave 01 (Beginner): Split a Model for 3D Printing in Blender", "Ball Joints for 3D Printed Figures (Blender)"). Op de pagina: "Your first split, step by step, in under four minutes."
5. **De pagina beantwoordt de gratis vervanger:** een blok "Why not just bisect it by hand?" ("You can. ... find out the fit was wrong after a six hour print"), en een eerlijk blok wat het niet doet ("Slicing, hollowing and supports stay in your slicer").
6. **Een eigen blok voor AI-modellen:** "Made for Meshy, Tripo and the like. Generators fuse arms, armour and props into one shell." Met een controle vooraf of het model dicht is en Make Manifold.

### Drie lessen
1. **Zichtbaar en snel bijwerken verkoopt, juist zonder publiek.** 12 versies in 6 weken, elk met datum op de pagina, en reviews die zeggen "in its early stages ... it can only get better" en "Didn't expect it to be so good yet". Een koper vergeeft ruwe randjes als hij ziet dat er elke week iets bijkomt. Dit is de tweede keer na Kambari (versie 2 na 6 dagen).
2. **AI-modellen zijn een eigen doelgroep, en ook hier staat het op de pagina.** Na Kambari ("Tame the mess AI leaves behind") de tweede maker die er een apart blok aan wijdt. Mensen die met Meshy of Tripo een figuur maken en het willen printen, hebben precies het probleem dat splitsen en gewrichten oplost.
3. **Elke review beantwoorden en een duurdere steunkeuze met dezelfde download.** Kost niets, maakt de pagina warmer, en de $28-keuze vangt kopers die meer willen geven. Hoeveel mensen die kiezen weet ik niet (geen cijfer, Superhive toont het niet).

### Eerlijk: wat niet zomaar voor ons geldt
- 100+ in 7,5 weken is een nette start, geen grote treffer. CatPin haalde 400+ in 3 maanden.
- Of hij buiten Superhive iets deed (Reddit, Discord, forums) heb ik niet gevonden. De verkoop kan ook uit de nieuwlijst en zoekfunctie van Superhive komen (GOK).
- Zijn productpagina is lang en heel goed, met filmpjes en voor-en-na-beelden; dat is werk dat wij voor Click Joints Pro deels al deden (demofilm, `platformen/blender/superhive-pagina.md`).

### Voorstel voor Dortus deze week
**Wie:** Bram (bouwer Blender) en Chris (winkeltekst), na de goedkeuring van Click Joints Pro door Superhive.
**Wat, drie kleine dingen die samen de les van Cleave en Kambari overnemen:**
1. **Een vast ritme: de eerste 6 weken elke week een kleine versie** (fout weg, of één wens van een koper), met datum in de versiegeschiedenis van Superhive. Past binnen de regel van hooguit één versie per week via Thijs (besluit Hans, 9 nov 20:44).
2. **Een blok "Made for AI-generated figures (Meshy, Tripo)"** op de Superhive-pagina, maar pas als Bram een AI-model door Click Joints Pro heeft gehaald en het werkt (eerst testen, niets beloven wat we niet zagen).
3. **Een tweede prijskeuze "Support the developer"**, $5 boven de gewone prijs, zelfde download. Chris zet het in `commercie/`; Thijs of de hoofdchat zet het in de winkel.
Plus: elke review binnen 2 dagen beantwoorden. Dat moet Thijs doen (bericht onder zijn naam), dus Chris zet per review een antwoord klaar op de lijst.

---

## 1. Milad Kambari (3DRedBox, Smart Remesh en Image to 3D op Superhive)

Onderzocht 15 nov 2026, run 1, opdracht van de hoofdchat. Een 3D-artiest die een klein bedrijf voor game-uitbesteding leidt (3DRedBox) en sinds 2024 op Superhive verkoopt. Hij is geen cursusverkoper met een trucje: zijn cijfers staan openbaar in de winkel.

### Bronnen
- Winkel van de maker, alle 85 producten (5 pagina's) en alle 85 productpagina's met curl gelezen op 15 nov 2026: https://superhivemarket.com/creators/miladkambari
- Smart Remesh, productpagina en reviews: https://superhivemarket.com/products/smart-remesh en https://superhivemarket.com/products/smart-remesh/ratings
- Image to 3D, productpagina en reviews (data van alle 22 reviews): https://superhivemarket.com/products/imageto3d
- CG Channel, Jim Thacker, 25 aug 2026, "Check out promising new Blender retopology tool Smart Remesh": https://www.cgchannel.com/2026/08/check-out-promising-new-blender-retopology-tool-smart-remesh/
- Nieuwkomers met hetzelfde onderwerp, ter vergelijking (productpagina's Superhive, 15 nov): image-to-3d-local, genmesh, depthforge.
- Niet gelukt: zijn ArtStation-cv (blokkeert curl) en het webarchief (geen verbinding vanuit onze omgeving). Geen interview of devlog van hem gevonden; alles hieronder komt uit de winkel, zijn productpagina's en CG Channel.

### Cijfers
Superhive toont verkopen in blokken ("2600+"). Alles GEZIEN op 15 nov 2026 tenzij anders vermeld.

| Product | Verkopen | Reviews | Prijs nu | Online sinds |
|---|---|---|---|---|
| Smart Remesh (retopologie) | 2600+ | 19 (gem. 4) | $17 | ±19 aug 2026 |
| Image to 3D (AI, lokaal op eigen GPU) | 1200+ | 22 (gem. 4) | $18 | ±30 okt 2026 (eerste review 16 dagen geleden) |
| Auto Unwrap (UV) | 1200+ | 9 | $18 | ±2 maanden |
| Dovetail Key | 800+ | 13 | $18 | ±5 maanden |
| Smart Segmentation | 300+ | 2 | $12 | ±3 maanden |
| Blender to Unreal Live Link | 300+ | 6 | $18 | ±9 maanden |
| Blender to Substance Painter Live Link | 200+ | 7 | $18 | ±9 maanden |
| Modeling Toolkit | 200+ | 1 | $18 | 20 dagen |
| 21 andere producten | 10+ tot 100+ | | $0 tot $28 | |
| 56 producten (vooral modellen, base meshes, 13 "lighting studios") | geen blok, dus onder 10 | 0 | $8,90 tot $25 | 1 tot 2+ jaar |

- Startprijs Smart Remesh was $15 (CG Channel, 25 aug, DERDEN); nu $17. Hij verhoogde dus na de eerste goede reviews.
- Versie 2 kwam 6 dagen na de release (CG Channel, DERDEN). Nu staat versie 3 online.
- Reviews tegen verkopen: Smart Remesh 19 op 2600 (0,7%), Image to 3D 22 op 1200 (1,8%), Auto Unwrap 9 op 1200 (0,75%), Dovetail Key 13 op 800 (1,6%). Op Superhive schrijft dus maar 1 op de 50 tot 1 op de 140 kopers een review (rekensom met GEZIEN-cijfers; de blokken zijn ondergrenzen).
- Omzet, GOK: de vier toppers samen ±5.800 verkopen x ±$17 is ±$100.000 bruto in ruim een half jaar, het meeste in de laatste 3 maanden. Kortingen (nu 25% coupon), studiolicenties en de afdracht van Superhive niet meegerekend; het echte bedrag voor hem ligt dus lager.
- Vergelijking: drie andere makers zetten in dezelfde weken een AI-naar-3D-add-on op Superhive (6, 21 en 24 dagen geleden). Geen van drieën heeft een verkoopblok, dus onder 10 verkopen (GEZIEN). Hetzelfde onderwerp, hetzelfde moment, 100 keer minder verkoop.

### Wat hij deed, in volgorde (uit de winkel afgeleid)
1. **2024 tot 2025: modellen.** Base meshes (helmen, zwaarden, kisten), ornamenten en 13 "lighting studios". Bijna niets verkocht (56 producten onder 10).
2. **Begin 2026: koppelingen (live links)** van Blender naar Unreal, Substance Painter en RizomUV. Eerste echte verkoop: 200+ tot 300+.
3. **Voorjaar 2026: kleine hulpjes** ($6 tot $18), een paar gratis ($0 tot $2, "betaal wat je wilt"). Dovetail Key haalt 800+.
4. **Aug 2026: Smart Remesh.** Lost een bekende pijn op (rommelige meshes uit CAD, scans, gekochte modellen en vooral AI-generatoren). De organische stand draait op het open-source Instant Meshes (BSD-licentie, op de pagina genoemd); zijn eigen werk is de harde-oppervlak-stand en alles eromheen: één knop, UV's en materialen blijven, terugzetten kan altijd. CG Channel schrijft er na 6 dagen over. Versie 2 na 6 dagen, daarna Mac en Linux, daarna versie 3.
5. **Sept tot nov 2026: de volgende producten haken in op dezelfde kopers.** Auto Unwrap (UV, 1200+), en eind oktober Image to 3D: open-source AI-modellen (TRELLIS, Hunyuan, FLUX.2 Klein en meer) die lokaal op je eigen NVIDIA-kaart draaien, "No cloud. No credits." De pagina laat voorbeelden zien met "Image to 3D + Smart Remesh, 1.5M to 5K faces": het ene product verkoopt het andere.

### Drie lessen
1. **Veel schoten, en de treffer zit in gereedschap voor een grote pijn, niet in spullen.** Van 85 producten verkochten er 56 onder de 10. Vier add-ons maken bijna alle omzet. Hij bleef uitbrengen tot hij de goede soort vond (werkstroom-hulpmiddelen voor game-artiesten) en ging daarna vol op die soort door. GEZIEN in zijn eigen winkel.
2. **Een bewezen open-source motor plus perfecte bediening in Blender is een product, als je op een golf zit.** Smart Remesh is voor de helft Instant Meshes, Image to 3D is TRELLIS en Hunyuan. Wat hij verkoopt is: één knop, niets kwijt (UV's, materialen, naam), alles terug te draaien, filmpje per onderdeel ín de add-on, en het antwoord op de golf van AI-modellen ("Tame the mess AI leaves behind"). Een review: AI-generatoren "spit out chaotic triangle soup with 2 to 3 million faces", dit lost het "in seconds" op.
3. **Na de lancering is snelheid het product.** Versie 2 na 6 dagen, Linux-versie op verzoek, wensen van kopers in de volgende versie. Drie van de tien nieuwste reviews noemen dat de maker snel reageerde of hun idee inbouwde. En een nieuw product verkoopt aan wie het vorige al had: Image to 3D haalde 1200+ in 16 dagen, terwijl drie nieuwkomers met hetzelfde idee onder 10 bleven.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij is zelf 3D-artiest met een game-bedrijf en kent de pijn van binnen. Wij kennen 3D-printen niet uit eigen werk.
- Hoe hij aan zijn eerste kopers kwam, weet ik niet: geen interview gevonden. Dat CG Channel hem na 6 dagen noemde kan toeval zijn of een persbericht (GOK). Hij heeft een Discord en post voorbeelden op X.
- De verkoopblokken zijn ondergrenzen en kunnen ook gratis "betaal wat je wilt"-downloads tellen bij producten van $0 tot $2. Bij zijn toppers ($17 en $18, geen gratis optie) is dat niet zo.

### Voorstel voor Dortus deze week
**Wie:** Bram (bouwer Blender), met een ja van Hans; Chris voor de lanceertekst.
**Wat:** Click Joints is één schot. Maak er een reeks van voor dezelfde kopers (3D-printers die figuren maken), en kies het tweede product op de golf van AI-modellen: een add-on die een AI-model (uit Meshy, TRELLIS, Hunyuan of Image to 3D) in één klik printbaar maakt (dicht maken, wanddikte, opdelen in delen die met Click Joints scharnieren), gebouwd op een bewezen open-source motor met een vrije licentie. Bram kijkt deze week eerst 1 uur in Superhive en op extensions.blender.org of zoiets al bestaat en hoe het verkoopt (zoeken op "printable", "3D print", "AI mesh"). Of de vraag er is, is nog een GOK; de golf zelf is GEZIEN (Image to 3D 1200+ in 16 dagen, reviews die AI-modellen noemen).
**Klein en meteen, na de goedkeuring van Click Joints Pro:** binnen een week na de lancering een versie 1.1 met de eerste wensen van kopers, en dat in de changelog zeggen. Lanceerprijs laag laten (de $9 van Chris klopt met dit verhaal) en na de eerste goede reviews verhogen, zoals Kambari van $15 naar $17.

**Aanvulling na verhaal 2 (Cleave, zelfde run):** het idee "AI-model in één klik printbaar maken en opdelen" is voor een deel al bezet. Cleave heeft een blok voor Meshy en Tripo, een controle of het model dicht is en Make Manifold, en splitst in delen met verbinders en kogelgewrichten (GEZIEN). Bram zoekt dus niet of het bestaat, maar wat Cleave en de rest niet doen. Het voorstel blijft staan als richting (reeks voor dezelfde kopers), het precieze product is nog open.
