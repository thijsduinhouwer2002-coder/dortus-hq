# Keuring B. Afkijken bij het printpubliek, 21 nov 2026, keurder namens Daan
Wat ik keurde: `platformen/ideeen/afkijken-2-2026-11-21/B-print-publiek.md` (niet gecommit, stand 21 nov ±13:30 NL)
Akkoord: nee (één moet-punt, klein werk; daarna akkoord)

Alle cijfers hieronder zelf nagelopen met `curl -sL` en een gewone browser user-agent op 21 nov ±13:20 tot 13:35 NL.

## Deel A: doet het wat beloofd is?
(opdracht: waar zit het printpubliek, hoe verkopen anderen aan hen, wat kunnen wij nadoen, met wie en wat het kost)

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | **Dummy 13 klopt.** Printables-GraphQL print 981111: 332.183 downloads, 32.254 likes, 957.936 weergaven, 3.089 makes (rapport: 332.177 / 32.252 / 957.914 / 3.089; verschil is groei sinds het meten). Bouwfilmpje Rwu3UP0cHZw: 1.864.175 weergaven (rapport 1.864.176). | feit (GEZIEN) | hoog | |
| A2 | **Patreon klopt precies.** API `filter[vanity]`: Cinderwing3D 6.322 betalend / 48.120 / 442 modellen; Flexi Factory 7.340 / 45.661 / 334; NunnBreakable 7 / 306; EmGi3D 452 / 1.881 in EUR; Jopek 122 / 935. Lagen van Cinderwing3D: Free $0, COMMERCIAL LICENSE ACCESS $10, DISTRIBUTOR LICENSE ACCESS $100. De GOK "minstens $63.000 per maand" is goed als GOK gemerkt. | feit (GEZIEN) | hoog | |
| A3 | **CatPin klopt, maar de prijs is een actieprijs.** Gumroad: 84 beoordelingen, gemiddeld 4,8 en de koppen "Cut. Connect. Print." en "Is CatPin Right for You?" staan erin. De `.json` van het product geeft `price_cents 3000` met `display_price $21, original_price $30`: $21 is dus korting op $30. Het rapport noemt $21 als vaste prijs (doe-lijst punt 1 en tabel deel 2). Filmpjes: KVPY63W0ovg 23.595 (rapport 23.558), o5QbTiKnfAM 12.306 (rapport 12.305). | feit (GEZIEN) | hoog | |
| A4 | **TrailPrint3D op Reddit klopt.** Arctic Shift, auteur Cube004: r/BambuLab 1jo0uew 3.309 met flair "Self Designed Model", r/3Dprinting 1jnex49 2.210, 1ki9xmc 3.827, bolt sorter 1gh20do 9.813. | feit (GEZIEN, via Arctic Shift) | hoog | |
| A5 | **"Mediaan 1 punt" klopt.** Laatste 100 posts met "articulated" in de titel: r/3Dprinting mediaan 1, top 1.922; r/BambuLab mediaan 1, top 479. Kanttekening: Arctic Shift slaat scores vaak kort na plaatsen op, en 36 van de 100 staan op 0 (deels weggehaald). De echte mediaan ligt dus mogelijk iets hoger; de les (zonder print haal je daar niets) blijft staan. | feit plus vermoeden | midden | scores van 10 posts los op reddit.com naast Arctic Shift leggen |
| A6 | **Regel r/BambuLab klopt** (rules-API): flair "Paid model", "Self Designed Model" of "Purchasable", "no more than one post per user per week", affiliatelinks nooit. | feit (DERDEN, Arctic Shift) | hoog | |
| A7 | Het "nee" van Thijs op de testprint van ±€12 op 20 nov klopt met `organisatie/besluiten.md` regel 186. | feit | hoog | |
| A8 | Het rapport geeft een bruikbare doe-lijst met wie, kosten en GOK op verkopen, en toetst aan geld. Het eerlijke slot ("niemand verkoopt een printtool zonder echte print") volgt uit het bewijs. | feit | hoog | |
| A9 | Niet nagelopen (tijd): r/-ledenaantallen, Discord-aantallen, HueForge-prijzen, prijzen van PAM/Dragon/THOR. Steekproef van zes zware bronnen klopte overal, dus geen reden tot argwaan. | | | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | **Doe-lijst punt 3 noemt de verkeerde plaatser.** "Een Short ... (Roep, na keuring)". Een YouTube Short uploadt sinds 21 nov de hoofdchat zelf in YouTube Studio; Roep plaatst via Metricool alleen op TikTok en lange YouTube-filmpjes. Zoals het er staat, zou Roep een YouTube Short plaatsen. | feit | hoog | harde regel 4 (Thijs 21 nov) |
| B2 | Punt 1 (lang YouTube-filmpje via Roep en Metricool, na groene keuring), punt 2 en 4 (Gumroad door de hoofdchat, die heeft toegang via Chrome volgens `toegang.md`), punt 5 (geld, alleen Thijs), punt 6 (Thijs, zijn Reddit, ja op de tekst) en de regels in deel 4 (Printables-account en makers benaderen: ja van Thijs) zijn eerlijk over wie en wat het kost. | feit | hoog | harde regels 1, 4 |
| B3 | Cijfers zijn gemerkt: deel 1 "Alles GEZIEN", deel 2 kolom "(GEZIEN)", deel 3 leden en regels DERDEN, schattingen GOK, valuta van Printables-prijzen GOK. Klein gat: "site noemt MakerWorld 8.000+" (TrailPrint) en de HueForge-prijzen hebben een link maar geen woord; de cijfers in de doe-lijst zelf leunen op de gemerkte tabellen. | feit | hoog | harde regel 5 |
| B4 | Geen persoonsgegevens van Thijs; van makers alleen openbare namen en links. Niets geplaatst of benaderd. | feit | hoog | harde regel 2, 4 |
| B5 | Nederlands, gewone woorden, geen gedachtestreepjes gezien. Bestand onder 400 regels. | feit | hoog | harde regel 8 |
| B6 | Punt 2 belooft kopers "You can sell the figures you make. No royalties." Dat past bij de GPL-licentie van Pro (wat je ermee maakt is van jou), maar het rapport toetst het niet aan onze eigen licentie- of winkeltekst. | vermoeden | midden | harde regel 5 (eerlijk) |

## Deel C: kort
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Sterk en leesbaar: de doe-lijst bovenaan, bewijs eronder. | | |
| C2 | Punt 3 en de rij "Dummy 13-style" leunen op de naam van een ander. Dummy 13 is CC-BY, maar een titel met andermans naam kan als meeliften voelen. | in de Short "inspired by Dummy 13-style joints" en credit aan soozafone | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Doe-lijst punt 3: wie plaatst wordt "TikTok: Roep via Metricool na groene keuring; YouTube Short: de hoofdchat in YouTube Studio" (B1).

**Kan**
1. CatPin "$21" wordt "$21 in de aanbieding, normaal $30" (A3).
2. Bij punt 2 even toetsen of de zin klopt met onze licentie en winkeltekst (B6).
3. Woord GEZIEN of DERDEN bij "MakerWorld 8.000+" en de HueForge-prijzen (B3).
4. Bij "mediaan 1" de kanttekening over Arctic Shift-scores (A5).
