# Keuring makers voor Click Joints Pro 1.1, 20 nov 2026, keurder (losse Claude, niet de maker)
Wat ik keurde: `commercie/blender-click-joints/makers-1.1-2026-11-20.md` (commit 4ed448e8)
Akkoord: nee

Alles nagekeken met curl op vr 20 nov ±15:00 tot 15:30 UTC: kanaalpagina's (`/about`), RSS-feeds per kanaal (kanaal-id uit de canonical link), de YouTube-zoekpagina voor elke genoemde video, de contactpagina's van de makers en vijf artikelen op gumroad.com/help. Mails geteld met een script (alles tussen "Hi" en de naam, zonder onderwerp). Ik schrijf hier geen adressen van makers op.

Kort: het meeste klopt goed. De mails zijn netjes, eerlijk en kort, alle Pro-beweringen staan in `gumroad-1.1.md`, het rekenvoorbeeld klopt. Maar twee GEZIEN-cijfers zijn fout (precies de twee twijfelgevallen), en de waarschuwing over CYBER25 berust op een verkeerd gelezen zin. Dat gaat naar Thijs als reden voor de verzenddag, dus eerst rechtzetten.

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | **InspirationTuts heeft 342K abonnees, niet 51,5K.** De kanaalpagina zelf zegt in de kop "342K subscribers" (veld `content` naast `@InspirationTuts` en "1.6K videos"). 51,5K is een ander kanaal dat onderaan dezelfde pagina staat (aanbevolen kanalen). SponsorRadar (342K) had dus gelijk. | feit | hoog | `curl` op youtube.com/@InspirationTuts/about, zoek `"content":"342K subscribers"` |
| 2 | **askNK heeft 290K abonnees, niet 3,63K.** Kop van de kanaalpagina: "290K subscribers". 3,63K hoort bij een ander kanaal op die pagina. Het "slecht passen bij 23.000 weergaven" verdwijnt dus: 290K met 23K tot 40K per video past gewoon. | feit | hoog | idem, @asknk/about |
| 3 | Gevolg van 1 en 2: de twee "twijfelgevallen" zijn geen twijfel meer. Het zijn na Grant Abbitt (643K) en CG Boost (415K) de grootste kanalen in de lijst, en ze zitten precies in de doelgroep (add-onoverzichten). Ook de kans dat ze geld vragen is daarmee groter. De volgorde en de tekst bij 6 en 7 moeten dat zeggen. | feit (cijfers) en vermoeden (geld vragen) | hoog / midden | antwoord van de makers |
| 4 | Overige abonnees kloppen (GEZIEN in de kop van elk kanaal): Stefan 214K, muwiart 41K, Pixel Artistry 55,4K, CG Boost 415K, Azrach Toys 11,3K, CG Dive 99,7K, Nikko 23,4K, Grant Abbitt 643K, Wickelle 5,99K. | feit | hoog | |
| 5 | Laatste uploads kloppen allemaal met de RSS-feed: Stefan 19 nov, muwiart 4 nov, Pixel Artistry 18 nov, CG Boost 19 nov, Azrach 17 nov, InspirationTuts 18 nov, askNK 19 nov, CG Dive 20 nov, Nikko 20 nov, Grant 14 nov, Wickelle 19 jun. | feit | hoog | |
| 6 | Alle genoemde video's bestaan met de genoemde weergaven (op een paar weergaven na, normaal): Stefan 80.318 en 179.311, muwiart 67.393, Pixel Artistry 67.137, CG Boost draak 280.945 (7 jaar oud, het stuk zegt "eerder", oké), Azrach Tripo 5.634 en Meshy Ninja 8.959, InspirationTuts 23.299 (8 dagen), askNK 25.541, Nikko 38.563, Grant 333.407 en deel 10 van de reeks (±3 weken), Wickelle frog girl (1 jaar oud). | feit | hoog | |
| 7 | Zakelijke adressen staan waar het stuk zegt: Stefan (site, blok Contact, "One inbox, read by me", gmail), muwiart (about, "Collaboration & Inquiries"), Pixel Artistry (Impressum, regel Kontakt; adres verborgen door Cloudflare, maar er staat er een), InspirationTuts (contactpagina, twee adressen), askNK (kanaalbeschrijving "For Enquires and Sponsorship - Email"), Nikko (voettekst, gmail). Formulier bij CG Boost, Azrach, CG Dive, Grant en Wickelle klopt. Namen in de aanhef kloppen (Bee, Philipp, Todor, Isabelle, Grant). | feit | hoog | |
| 8 | **De waarschuwing over CYBER25 klopt niet.** Het stuk zegt: of een eigen code in de link CYBER25 vervangt "staat er niet (GOK)". Het staat er wel. Discount codes, kopje Automatically apply: "If a customer arrives with a different discount from a discount link or URL parameter, Gumroad applies whichever discount is larger. Discounts never stack." De 100%-code in de link wint dus van de automatische 25%. De geciteerde zin dat de koper een automatische code "niet kan weghalen" komt uit het stuk over "Limit to new customers" en gaat daar over iets anders. Punt 5 van "Wat Thijs moet beslissen" geeft dus een reden die niet bestaat. Vroeg versturen blijft wel slim (een video moet vóór of in de saleweek af zijn), maar om die reden. | feit | hoog | gumroad.com/help/article/128-discount-codes; de test van één code door de hoofdchat blijft goed |
| 9 | Rekenvoorbeeld klopt. Met 10% + $0,50 plus kaart 2,9% + $0,30 (fees-pagina: kaart komt er los bij): kosten $2,638 op $14,25, wij zonder affiliate $11,61, maker bij 30% $4,275 min $0,79 = $3,48, wij $8,13. Bij $19: wij $11,02 (stuk zegt ±$11,03, afronding), maker $4,72. Bij 50%: $5,81 (stuk ±$5,80). Kosten naar rato staat letterlijk op beide pagina's ("if an affiliate's commission is 30%, they'll be responsible for 30% of the fees"). Rekent men alleen met 10% + $0,50 zonder kaartkosten, dan wordt het maker $3,70 en wij $8,63; het stuk kiest terecht de volledige kosten. | feit | hoog | |
| 10 | **De verwachting rekent met de verkeerde marge.** "Bij ±$11 netto per verkoop na de affiliate ... één goede video ±$50 tot $100; 2 tot 3 video's in de saleweek ±$100 tot $300." In de saleweek is het volgens het eigen voorbeeld $8,13, niet $11. Vijf verkopen per video (het enige DERDEN-cijfer) is dan ±$40 per video en ±$80 tot $120 voor 2 tot 3 video's. Dit gaat naar Thijs als geldverwachting, dus het moet kloppen met de eigen som. | feit (de som) | hoog | |
| 11 | Overige Gumroad-feiten kloppen met de hulp: twee soorten (eigen 1% tot 75%, Gumroad Affiliates vast 10%, uitzetten kan), toevoegen met het e-mailadres van hun Gumroad-account (bevestigd, anders fout), koekje 30 en 7 dagen, laatste klik telt, percentage over wat de koper betaalt na korting zonder btw, uitbetaling na 7 dagen op het weekschema, terugbetaling gaat van hun deel af, `?offer_code=` werkt niet bij een doel-URL, Posts "Affiliates only", aanmeldformulier, gift kan niet voor eigen product en Gumroad wijst zelf naar een 100%-code, code alleen letters en cijfers, Limit quantity telt het totaal, "Only one code can be used per product". | feit | hoog | gumroad.com/help artikelen 333, 249, 66, 128, 213 |
| 12 | **Het stuk zegt dat het melden van de affiliatelink "staat in onze mail". Dat staat er niet.** De mails vragen alleen "please say it was free". Of de zin in het stuk eruit, of de mails vragen ook om te zeggen dat het een affiliatelink is (let op: Stefan en Azrach zitten op 119 woorden). | feit | hoog | lees de 11 mails |
| 13 | Elke Pro-bewering in de mails staat in `platformen/blender-2/gumroad-1.1.md`: één knop, end-stop scharnier aan ellebogen en knieën, kogel aan schouders, heupen en nek, graden per gewricht, Limit Rotation 30° tot 150°, lijst met waar het bereik vandaan komt, botnamen (Rigify, Mixamo, Auto-Rig Pro, VRoid, Daz), AI-figuren met benen tegen elkaar slaan heupen over met reden, 200 mm, 3D-cursor op een al gesplitst deel, speling, STL of 3MF. Nergens "clicks", "holds a pose", testkaart of overdrijving. "Clicker" in de mail aan muwiart is haar eigen video. | feit | hoog | |
| 14 | "Honest note: not print tested by us yet." staat in alle 11 mails. "please say it was free" staat in alle 11. Geen AI-melding; "AI-made figures" gaat over wat de koper erin stopt, net als in de winkeltekst. | feit | hoog | |
| 15 | Woorden (geteld met script, zonder onderwerp, met aanhef en naam): 119, 111, 114, 113, 119, 114, 118, 113, 117, 110, 110. Alle 11 onder 120. | feit | hoog | |
| 16 | Klein: bij InspirationTuts en askNK staat "The end stop comes from Limit Rotation in your rig" en "taken from Limit Rotation in the rig". De winkeltekst zegt: alleen als een bot die beperking heeft, anders spiegel of een standaard. CG Dive doet het precies goed ("A bone's Limit Rotation becomes..."). | feit | midden | |
| 17 | Wickelle is niet echt actief: laatste upload 19 jun (5 maanden), die had 439 weergaven, Blender niet gezien. Het stuk zegt dat eerlijk ("minder actief", GOK), maar telt haar wel mee in "advies de 11". Azrach Toys: actief en past bij beweegbare figuren, maar Blender niet gezien (GOK staat er). | feit | hoog | |
| 18 | Stefan schrijft op zijn site: "If it's a brand partnership, say which product and which video slot". Hij is gewend aan betaalde plekken. Kans dat hij geld vraagt is reëel; het stuk zegt dat alleen bij 6 en 7. | vermoeden | midden | zijn antwoord |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen adressen van makers in het bestand: alleen "waar het staat". Gezocht op `@`: alleen thijs@dortus.com (bedrijfsadres, staat al in de winkeltekst) en YouTube-handles. Geen persoonsgegevens van Thijs. De winkel-URL met `duinhouwer8` staat al op meer plekken in de repo en is de openbare winkel. | feit | hoog | regel 2 |
| 2 | Twee cijfers met GEZIEN zijn fout (deel A 1 en 2). Dat is precies wat GEZIEN niet mag zijn. | feit | hoog | regel 5 |
| 3 | Overige cijfers hebben GEZIEN, DERDEN of GOK (kop van de tabel, GOK bij de verwachting, DERDEN met links bij Gumroad en Superhive). | feit | hoog | regel 5 |
| 4 | Nederlands in gewone woorden; geen gedachtestreepjes gevonden (gezocht op lange en halve streepjes en " - "; alleen een citaat van askNK). | feit | hoog | regel 8 |
| 5 | Niets verstuurd, niets aangemaakt; het stuk zegt duidelijk dat Thijs ja moet zeggen op de teksten en dat geld vragen nee is of naar Thijs gaat. | feit | hoog | regels 1 en 4 |

## Deel C: hoe leest een maker dit?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De mails openen elk met hun eigen video en zijn kort en eerlijk; dat leest als een echt mens. De laatste alinea is wel steeds dezelfde dichte zin met drie dingen tussen haakjes en puntkomma's. | Eén korte zin per ding: gratis code, 30% via eigen link, korting 27 nov. Binnen 120 woorden blijven. | klein |
| 2 | "It's 25% off Nov 27 to Dec 1" zegt niet waar. Pro staat ook op Superhive, waar geen korting is, en de 30% geldt alleen via Gumroad. | "on Gumroad" toevoegen als het past. | klein |
| 3 | Een maker met een groot kanaal (InspirationTuts, askNK, Grant) krijgt hetzelfde als een klein kanaal. | Prima zo; het stuk zegt al dat Thijs per persoon hoger kan. | klein |

## Moet (blokkeert akkoord)
1. Abonnees InspirationTuts naar 342K en askNK naar 290K (GEZIEN op de kanaalpagina), de twijfeltekst bij 6 en 7 weg, en de volgorde of het advies opnieuw bekijken nu dat de twee grootste overzichtskanalen in de lijst zijn.
2. De "Let op" over CYBER25 rechtzetten: de hulp zegt dat Gumroad de grootste korting toepast en dat kortingen nooit stapelen, dus de 100%-code wint. Punt 5 van "Wat Thijs moet beslissen" een echte reden geven (video af vóór of in de saleweek), niet de code.
3. De geldverwachting laten kloppen met het eigen rekenvoorbeeld: in de saleweek $8,13 per verkoop, dus ±$40 per video bij 5 verkopen (GOK).
4. De zin "en staat in onze mail" over het melden van de affiliatelink weghalen, of de mails echt laten vragen om te zeggen dat het een affiliatelink is (binnen 120 woorden).

## Kan (mag later)
1. Wickelle als reserve zetten, niet in "de 11": 5 maanden geen upload, Blender niet gezien.
2. Bij InspirationTuts en askNK "if your rig has one" of "where your rig sets a limit" toevoegen bij Limit Rotation.
3. Bij Stefan noemen dat hij betaalde plekken gewend is (zijn contacttekst), zoals bij 6 en 7.
4. "on Gumroad" bij de korting, en de laatste alinea in korte zinnen (deel C).

## Nakeuring 20 nov
Wat ik keurde: alleen de 4 moet-punten, zoals verwerkt in commit c8a3d726 (deel "Verwerkt na de keuring"). Losse keurder, niet de maker. Nagekeken met curl op vr 20 nov ±16:00 UTC.
Akkoord: ja

| # | Moet-punt | Opgelost? | Wat ik zag |
|---|---|---|---|
| 1 | Abonnees InspirationTuts en askNK | ja | Kanaalpagina's opnieuw met curl: `"content":"342K subscribers"` op @InspirationTuts/about en `"content":"290K subscribers"` op @asknk/about (GEZIEN). De tabel zegt nu 342K en 290K; de twijfeltekst over 3,63K en "slecht passen" is weg. De volgorde blijft 1 tot 5 eerst, met als reden dat zij zelf figuren printen en de overzichtskanalen mogelijk geld vragen. Dat is opnieuw bekeken en beargumenteerd, goed genoeg. |
| 2 | CYBER25 | ja | gumroad.com/help/article/128-discount-codes, kopje Automatically apply, staat letterlijk: "If a customer arrives with a different discount from a discount link or URL parameter, Gumroad applies whichever discount is larger. Discounts never stack." Het stuk citeert dat nu goed, en punt 5 van "Wat Thijs moet beslissen" geeft de echte reden (video af vóór of in de saleweek). De oude, verkeerd gelezen zin is weg. |
| 3 | Geldverwachting | ja | Nu $8,13 per verkoop in de saleweek, ±$40 per video bij 5 verkopen, ±$80 tot $120 bij 2 tot 3 video's (GOK). Klopt met het eigen rekenvoorbeeld (5 x 8,13 = 40,65). |
| 4 | Affiliatelink melden | ja | Alle 11 mails hebben nu dezelfde zin: "Mention it and get 30% of each sale via your own link (send us your Gumroad email); please disclose it was free and an affiliate link." Eerlijk: de maker wordt gevraagd zowel gratis als affiliate te melden. Natuurlijk Engels: kort en zakelijk, goed te begrijpen. De zin "en staat in onze mail" is vervangen door wat nu waar is. |
| 4b | Max 120 woorden | ja | Zelf geteld met een script, zonder onderwerp, met aanhef en groet (en met het mailadres bij de formulieren): 119, 113, 116, 115, 119, 116, 120, 115, 119, 112, 112. askNK zit precies op 120, de rest eronder. |

Kan (geen blokkade): "please disclose it was free and an affiliate link" leest strikt als "Pro was een affiliatelink". Netter is "disclose that it was free and that the link is an affiliate link", maar dat brengt askNK boven 120; dan elders twee woorden schrappen. De kan-punten uit de eerste keuring staan nog open, zoals het stuk zelf zegt.
