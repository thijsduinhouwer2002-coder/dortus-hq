# B. Afkijken bij het printpubliek: waar zitten ze en hoe verkopen anderen aan hen (21 nov 2026)

Opdracht hoofdchat 21 nov ±12:30 NL. Alles met `curl` gelezen op 21 nov tussen 12:30 en 13:45 NL: openbare API's van Printables (GraphQL), MakerWorld, Patreon (`/api/campaigns?filter[vanity]=...`), Gumroad (zoeken), Arctic Shift (Reddit), Discord (uitnodigingen) en de zoekpagina van YouTube. Niets geplaatst, niemand benaderd, geen account gemaakt. Van makers alleen hun openbare naam en links.

## Doe-lijst (wat, wie, kosten, verwacht effect)
1. **YouTube-filmpje bij elke Pro-versie, zoals CatPin** (Roep via Metricool, alleen na groene keuring; €0; deze week 1.1). CatPin, een Blender-add-on van $21 om modellen te splitsen voor print, maakt bij elke kleine versie een filmpje ("New CatPin 1.0.8 is available NOW!", 12.305 weergaven) en uitlegfilmpjes met zoekwoorden in de titel (23.558 weergaven). Titel voor ons: "Hinge joints with an end stop for 3D printing in Blender". GOK: 200 tot 2.000 weergaven, 0 tot 2 verkopen per filmpje, omdat CatPin met een klein kanaal duizenden haalt, maar wel echte prints laat zien.
2. **Op de Gumroad-pagina van Pro de zin "You can sell the figures you make. No royalties."** (hoofdchat; €0; vandaag). TrailPrint3D zet "Commercial Use" als blok op de site; het grote geld in deze groep komt van mensen die prints verkopen (Cinderwing3D: 6.322 betalende leden voor een commerciële licentie). GOK: 0 tot 1 verkoop extra, haalt een twijfel weg bij verkopers op Etsy.
3. **Een Short met de hoek "Dummy 13-style joints on your own character"** (Roep, na keuring; €0; volgende week). Dummy 13 is het grootste figuur-onderwerp: 332.177 downloads, bouwfilmpje 1,86 mln weergaven. Eerlijk: "rendered in Blender, not printed yet". GOK: meer weergaven dan een gewone Pro-Short, verkopen 0 tot 2.
4. **Gumroad-titel en tags met "3D printing", "articulated", "action figure"** (hoofdchat; €0). CatPin staat bovenaan bij Gumroad-zoeken op "articulated stl". GOK: pas iets na de eerste verkoop en reviews (Gumroad sorteert daarop en Discover komt pas na de eerste verkoop), dus klein.
5. **Echte print: €12 (Thijs, geld; eerder nee op 20 nov).** Dit stuk laat zien waarom die zo zwaar weegt: r/PrintedMinis verbiedt renders, r/BambuLab wil "a picture of the product", en TrailPrint3D haalt 2.210 tot 3.827 punten op r/3Dprinting met geprinte kaarten. Zonder print is de mediaan van "articulated"-posts daar 1 punt. Ook mogelijk: een gratis testmodel op Printables (nieuw account, ja van Thijs). Alleen ter informatie: de keus blijft bij Thijs.
6. **Na een print: r/BambuLab, flair "Paid model" of "Purchasable"** (Thijs, zijn Reddit, ja op de tekst; €0). Mag één keer per week (regel van de sub). GOK: 0 tot 3 verkopen; TrailPrint3D haalde er 3.309 punten met een geprinte kaart.
7. **Niet doen:** r/functionalprint (verbiedt speelgoed), r/3Dmodeling (verbiedt betaalde reclame), r/ActionFigures (verbiedt zelfpromotie), en de TrailPrint-route "eerst karma met prints". Die laatste kan pas als er een printer is.

---

## 1. Makers van beweegbare figuren die geld verdienen

Bronnen: Printables-API (`api.printables.com/graphql/`, velden downloadCount, likesCount, displayCount = weergaven, makesCount), Patreon-API (paid_member_count = betalende leden, patron_count = alle leden, ook gratis), MakerWorld-API. Alles GEZIEN op 21 nov.

| # | Maker | Grootte | Waar het publiek zit | Wat liep (GEZIEN) | Hoe naar betaald |
|---|---|---|---|---|---|
| 1 | **soozafone / Lucky 13 Toys** ([Printables](https://www.printables.com/@soozafone), [site](https://www.lucky13toys.com/)) | 24.875 volgers en 1.102.608 downloads op Printables | Printables en YouTube (eigen bouwfilmpje) | [Dummy 13 v1.0](https://www.printables.com/model/981111): 332.177 downloads, 32.252 likes, 957.914 weergaven, 3.089 makes, 5.482 reacties. [Bouwfilmpje](https://youtu.be/Rwu3UP0cHZw): 1.864.176 weergaven. Anderen maakten er filmpjes over: Uncle Jessy 592.486, Brandon Tucker 1.191.531 | Skelet gratis (CC-BY, "Yes, you can sell it"), donatieknoppen (PayPal, Stripe, Buy Me a Coffee), daarna **betaalde modellen in de Printables-winkel**: [PAM](https://www.printables.com/model/1189615) prijs 6,3, [Dragon](https://www.printables.com/model/1335739) 4,9, [M13 THOR](https://www.printables.com/model/1484179) 8,4 (valuta staat niet in de API, GOK dollar); 85, 120 en 80 makes. Plus een club op Printables (link op zijn licentiepagina). Grote uitgave ongeveer elke 4 tot 5 maanden (feb, jun, nov 2025) |
| 2 | **Cinderwing3D** ([Patreon](https://www.patreon.com/cinderwing3d)) | Patreon **6.322 betalend**, 48.120 leden, 442 modellen; Discord 9.284 leden (2.074 online) | MakerWorld (officiële samenwerking met Bambu Lab), Patreon, Discord | [Bamboo Dragon, Cinderwing3D x BambuLab](https://makerworld.com/en/models/154224): 27.553 downloads, 11.152 likes | Gratis voorproefje op MakerWorld, dan Patreon met lagen Free, **Commercial License $10** en Distributor $100 per maand. Ze verkopen vooral het recht om prints te verkopen. GOK: minstens $63.000 per maand bruto (6.322 x $10, ondergrens) |
| 3 | **Flexi Factory** ([Patreon](https://www.patreon.com/flexifactory)) | Patreon **7.340 betalend**, 45.661 leden, 334 modellen | Patreon; anderen maken op Printables accessoires voor hun figuren ([Beanie](https://www.printables.com/model/608458) 222, [Stand](https://www.printables.com/model/738145) 168 downloads) | eigen modellen staan niet gratis op Printables (zoeken gaf alleen accessoires van anderen) | Alles achter Patreon; prijzen van de lagen geeft de API niet |
| 4 | **Jopek Design (JD3D)** ([Printables](https://www.printables.com/@JD3D), [Patreon](https://www.patreon.com/jopekdesign)) | 3.121 volgers, 386.448 downloads; Patreon 122 betalend, 935 leden | Printables | [Articulated Whale Shark](https://www.printables.com/model/507275): 120.300 downloads, 19.037 likes, 251.127 weergaven, 1.489 makes | Bio en elke beschrijving: "Check out my Patreon for more awesome models and benefits!" Gratis toppers trekken, Patreon verkoopt. Verhouding: 386.448 downloads tot 122 betalers |
| 5 | **McGybeer** ([Printables](https://www.printables.com/@McGybeer)) | 5.968 volgers, 470.309 downloads | Printables, YouTube | [Articulated Shark](https://www.printables.com/model/178032): 112.498 downloads, 15.762 likes, 247.777 weergaven, 1.736 makes | Eigen site (geeft 403 op curl) en Patreon sinds nov 2022, 117 modellen; aantal betalers verborgen. Filmpjes op YouTube gelinkt onder elk model |

**Ook gezien, kleiner of zonder geld:** [Spennolio](https://makerworld.com/en/models/1949985) op MakerWorld (8.609 fans, "Blank Man" 19.713 downloads, exclusief voor MakerWorld; verdient daar met punten), [Make-A-Print](https://www.printables.com/model/484193) (ETP-Robot 6.079 downloads, geen betaalde link), [Direct Designs, MODULYR V2](https://www.printables.com/model/1482745) (3.073 downloads, geen betaalde link), Biocraftlab (Patreon 4 betalend van 265, "Join for a commercial license"), Cupio Pax Studios (3 betalend van 31), 3dzipguy op Gumroad ([ZIPGUY](https://3dzipguy.gumroad.com/l/3dzipguy), $20, 55 beoordelingen), cgproasmr op Gumroad ([articulated figure](https://cgproasmr.gumroad.com/l/XEVKqk), $5, 24 beoordelingen).

**Wat opvalt (bij elkaar):**
- Het geld zit bij **commerciële licenties**: mensen die prints op markten of Etsy verkopen betalen per maand (Cinderwing3D $10, Biocraftlab, HueForge hieronder). Dat is les 1 uit de vorige afkijkronde ("wie aan het product verdient, betaalt") opnieuw.
- **Gratis eerst, veel en groot**: alle vijf hebben een gratis topper met 100.000+ downloads voordat er iets betaald wordt.
- In de beschrijving van de populairste figuurmodellen staat zelden een verkooplink: bij tot 60 modellen uit de zoeklijsten "action figure", "dummy 13", "articulated figure" en "poseable" vond ik geen enkele link naar Patreon, Cults3D, MyMiniFactory, Etsy, Gumroad, Ko-fi of Discord (GEZIEN). De verkoop loopt via het profiel, de bio of een losse winkelpagina.
- **Makes** (foto's van mensen die het printten) zijn de echte maat van vertrouwen: Dummy 13 heeft er 3.089.

## 2. Verkopers van tools voor 3D-printers

| Tool | Prijs | Kopers en bereik (GEZIEN) | Kanalen | Winkelpagina |
|---|---|---|---|---|
| **CatPin** (Blender-add-on, splitsen met pennen, door AlexSokol) | $21 op [Gumroad](https://alexsokol.gumroad.com/l/catpin) | 84 beoordelingen, gemiddeld 4,8 (GEZIEN in de pagina) | **YouTube is de motor**: in ±3 maanden minstens 6 filmpjes: [uitleg](https://youtu.be/KVPY63W0ovg) 23.558, [eerste](https://youtu.be/OttC5yJYlT4) 21.031, [1.0.8](https://youtu.be/o5QbTiKnfAM) 12.305, [snelste manier](https://youtu.be/D8PWAxgpC78) 6.315, [1.0.9](https://youtu.be/0rmT2gD9Kpg) 2.227 weergaven (13 dagen oud). Op Reddit bijna niets: 2 hulpvragen van gebruikers op r/blender, 0 posts op r/3Dprinting en r/resinprinting (GEZIEN, Arctic Shift). Abonnees van het kanaal niet zeker te lezen (de pagina gaf 76, dat past niet bij de weergaven) | Opbouw: belofte "Cut. Connect. Print.", dan per functie een kop met uitleg, dan "Is CatPin Right for You?" met een lijst kopers: "STL model creators, Character sculptors, Figure, bust, and statue artists ... 3D-printing studios". Geen gratis versie gezien |
| **TrailPrint3D** (Blender-add-on, wandelroute naar printbare kaart, door EmGi) | gratis add-on, Premium via [Patreon](https://www.patreon.com/c/EmGi3D) | Patreon **452 betalend** (EUR), 1.881 leden; [Printables-model](https://www.printables.com/model/1242540) 3.883 downloads, 1.198 likes, 25.878 weergaven; Discord 1.222 leden; YouTube [@EmGi_](https://www.youtube.com/@EmGi_) 14,9K abonnees; site noemt MakerWorld 8.000+ downloads | **Reddit met prints**, zie het rijtje hieronder. De add-on staat zelf als "model" op Printables en MakerWorld, met links naar Patreon, site, Discord, Buy Me a Coffee en Amazon (affiliate) | [Site](https://trailprint3d.com/): "Free Addon ... No Accounts No Tracking", blok "Commercial Use: The add-on itself can be used commercially, sell prints", aparte lijst "Premium Features" (meer sporen, tegels, puzzels), versie en datum bovenaan ("07.11.2026 - Version 4.0.0 released") |
| **HueForge** (eigen programma, foto's printen in laagjes filament) | Personal $24 eenmalig, Limited Commercial $60 per jaar, Professional Commercial $120 per jaar, Professional $350 eenmalig; plug-ins $15 tot $20 ([winkel](https://shop.thehueforge.com/products.json)) | 6.473 modellen op Printables en 4.840 op MakerWorld met "HueForge" in de zoekresultaten; YouTube [@hueforging](https://youtube.com/@hueforging) 16,6K abonnees | **De gemeenschap maakt de reclame**: elk model dat iemand met HueForge maakt en op Printables of MakerWorld zet, draagt de naam. Daarnaast affiliatelinks voor filament en een kortingscode met Polymaker | Shopify-winkel; "All Full Release versions have the same features. There are no Commercial Only features": de duurdere lagen zijn alleen het recht om te verkopen, plus vroege beta's |

**TrailPrint3D op Reddit (maker Cube004, GEZIEN via Arctic Shift, alle 64 posts):**
- Eerst ±9 maanden geprinte handige dingen zonder tool: [M3 bolt sorter](https://reddit.com/r/3Dprinting/comments/1gh20do/) 9.813 punten op r/3Dprinting (nov 2024), [magneethulpje](https://reddit.com/r/3Dprinting/comments/1flapy8/) 4.002, [schroevensorteerder](https://reddit.com/r/functionalprint/comments/1hzr31x/) 1.589 op r/functionalprint.
- Toen de add-on (mrt 2025): [r/3Dprinting](https://reddit.com/r/3Dprinting/comments/1jnex49/) 2.210, [r/BambuLab](https://reddit.com/r/BambuLab/comments/1jo0uew/) 3.309 met flair "Self Designed Model", r/komoot (de fietsers en wandelaars zelf) [1.704](https://reddit.com/r/komoot/comments/1j9jgrd/) (geprinte tocht, twee weken vóór de add-on) en [121](https://reddit.com/r/komoot/comments/1juxrpj/) (de add-on), r/MapPorn 215.
- Daarna elke 1 tot 3 maanden een nieuwe print met de add-on: [3.827](https://reddit.com/r/3Dprinting/comments/1ki9xmc/) (mei 2025), [2.376](https://reddit.com/r/3Dprinting/comments/1qqc6wz/) (jan 2026), [2.469](https://reddit.com/r/3Dprinting/comments/1ubseh1/) (jun 2026), 545 en 524 (sep en okt 2026). Op r/blender maar 2 posts (57 punten): de kopers zitten in de printsubs, niet in r/blender.
- Elke post toont een **geprinte** kaart. De titel noemt wat je krijgt, niet de prijs.

**Direct concurrent, als waarschuwing:** NB Figure Joints van [NunnBreakable](https://www.patreon.com/NunnBreakable) (gewrichten in elk model, alleen via Patreon): 7 betalend van 306 leden, [filmpje](https://youtu.be/IBObASfadOo) 648 weergaven, YouTube 3,96K abonnees. Een tool die alleen achter Patreon zit, zonder gratis versie in een winkel, komt nauwelijks van de grond.

**Drukte in splitsen:** naast CatPin kwamen in de laatste 4 maanden ook SnapSplit ($14 op Gumroad, 0 beoordelingen), Cleave (filmpjes 3.606 en 1.244), SPLIT IT (1.507), CutMode (gratis, 11.472) en Dovetail Key ([30.027](https://youtu.be/kb-Y-SAWDKg)) uit (GEZIEN op YouTube en Gumroad). Gewrichten met eindstop doet daar niemand. Dat is ons verschil, maar de kopers vinden deze tools via YouTube-zoeken op "split for 3D printing in Blender", dus daar moeten wij ook staan.

## 3. Waar de groep samenkomt

Leden: Arctic Shift (DERDEN, hun kopie van Reddit). Regels: Arctic Shift rules-API (DERDEN). Scores: Arctic Shift posts-API met zoekwoord "articulated", de laatste 100 posts (GEZIEN via die API).

| Plek | Grootte | Mag een tool? | Wat moet je laten zien | Wat liep |
|---|---|---|---|---|
| r/3Dprinting | 2.940.796 leden (DERDEN) | "Less than 10% self-promotion ... you must engage with the community"; er is een lijst met verboden sites | een print | top "articulated": [weerwolfmasker](https://reddit.com/r/3Dprinting/comments/1x0rvue/) 1.922, [action figure voor neefje](https://reddit.com/r/3Dprinting/comments/1x5u4id/) 888; mediaan van de 100 posts: 1 punt |
| r/BambuLab | 217.767 (DERDEN) | **ja**: "Members can post links for their paid models, 3D printing products ... Tag it with 'Paid model', 'Self Designed Model' or 'Purchasable' ... no more than one post per user per week ... You must show a picture of the product or model." Geen affiliate-links | foto van het product (GOK: een render van een add-on is daar zwak) | [gratis rupsgenerator](https://reddit.com/r/BambuLab/comments/1tx1qx5/) 479; TrailPrint 3.309; mediaan 1 |
| r/PrintedMinis | 135.926 (DERDEN) | alleen op vrijdag: "Patreon, Kickstarter and any Advertising posts are limited to Fridays only" | "Renders are not allowed" | geprinte meetlat 1.340 en 1.006; mediaan 10 |
| r/functionalprint | 493.482 (DERDEN) | nee: "No Toys/Games" en "No self-promotion, advertising, or selling" | | |
| r/customactionfigures | 13.170 (DERDEN) | geen regel tegen promo (enige regel: "don't be evil") | eigen figuren | [Toph Beifong](https://reddit.com/r/customactionfigures/comments/1wupg6z/) 348, Star Fox 259; mediaan 8 |
| r/ActionFigures | 171.041 (DERDEN) | nee, verboden (zie `commercie/blender-click-joints/plekken-boost-2026-11-20.md` rij 17) | | |
| r/BJD | 28.915 (DERDEN) | zie `reddit.md`, argwaan tegen 3D-print | | |
| r/Dummy13 | 280 (DERDEN) | geen regels gelezen | | te klein |
| r/3dprintedfigures | 3 (DERDEN) | | | bestaat bijna niet |
| r/3Dmodeling | 1.393.798 (DERDEN) | nee: "Do not advertise paid assets, content, or services" | | |
| r/resinprinting | 94.325 (DERDEN) | niet gelezen | | |
| Discord Cinderwing3D | 9.284 leden, 2.074 online (GEZIEN) | van een maker zelf, GOK nee | | |
| Discord r/ActionFigures | 6.872, 915 online (GEZIEN) | GOK nee (de sub verbiedt het) | | |
| Discord Bambu Lab, 3DMeltdown, Blender Community | 42.249 / 12.855 / 223.742 (GEZIEN) | zie plekken-boost rij 6, 23, 24 | print | |
| Discord TrailPrint3D | 1.222 (GEZIEN) | eigen server van een toolmaker: zo bouw je een eigen plek | | |
| Facebook-groepen (Dummy 13, action figures) | onbekend | niet te lezen met curl; alleen met het privé-account van Thijs | | niet gemeten |
| YouTube: tools | | | | Slant 3D [verbindingen](https://youtu.be/vsHpiHhB3RU) 199.279; ZeroDotCMD [articulating prints in Blender](https://youtu.be/y05kcJ8v_Y4) 48.958; Nikko Industries [FlexiMaker](https://youtu.be/Sml8ecHkhPg) 38.630; Skillful Toys [Blender for action figures](https://youtu.be/XtfSeCm7cbo) 10.911 |
| YouTube: figuren | | | | Dummy 13: Lucky 13 Toys 1.864.176, Brandon Tucker 1.191.531, Uncle Jessy 592.486, Guide Blocks 538.005 (1 maand oud), My CG Tutor 120.456 |

**Wat je moet laten zien:** op elke grote printplek een echte print. De enige plekken waar een tool zonder print kan, zijn Blender-plekken (r/blender, BlenderArtists, BlenderNation; al in plekken-boost) en ons eigen YouTube- en TikTok-kanaal.

## 4. Wat we letterlijk kunnen nadoen

| Wat (bron) | Wie | Kosten | Kan zonder print? |
|---|---|---|---|
| Filmpje per versie plus uitlegfilmpjes met zoekwoorden (CatPin) | Dortus, Roep via Metricool na keuring | €0 | ja, render met "not printed yet" |
| Blok "Commercial use: sell your prints" op de pagina (TrailPrint3D, HueForge, Cinderwing3D) | Dortus, hoofdchat | €0 | ja |
| Versie en datum bovenaan de pagina (TrailPrint3D) | Dortus, hoofdchat | €0 | ja |
| Hoek "Dummy 13-style joints for your own character" (grootste figuuronderwerp) | Dortus, Roep | €0 | ja, als render |
| Eigen Discord voor kopers (TrailPrint3D, 1.222) | Dortus, hoofdchat | €0 | ja, maar GOK leeg bij 0 kopers: later |
| Duurdere commerciële laag (HueForge $60 tot $350) | Dortus | €0 | ja, maar GOK te vroeg bij 0 verkopen |
| Tool als gratis "model" op Printables en MakerWorld met links (TrailPrint3D) | nieuw account, ja van Thijs | €0 | **nee**: geprinte foto's nodig, anders openbare mislukkingen onder ons model |
| Posts op r/3Dprinting, r/BambuLab, r/PrintedMinis (TrailPrint3D) | Thijs, zijn Reddit | €0 | **nee**: renders verboden of zwak |
| Eerst karma met handige prints, dan de tool (TrailPrint3D) | Thijs | printer nodig | **nee** |
| Maker laat jouw tool zien (Dummy 13-filmpjes van anderen) | Thijs (benaderen) | €0 of een gratis licentie | kan, lijst staat al in `commercie/blender-click-joints/makers.md` |
| Echte testprint | Thijs | ±€12 (`echte-print-2026-11-20.md`) | opent de rijen hierboven |

**Eerlijk:** niemand in dit onderzoek verkoopt een printtool zonder echte prints te laten zien. CatPin toont geprinte figuren, TrailPrint3D geprinte kaarten, HueForge leeft van geprinte voorbeelden van anderen. Zonder print blijft onze verspreiding beperkt tot Blender-plekken en ons eigen kanaal.
