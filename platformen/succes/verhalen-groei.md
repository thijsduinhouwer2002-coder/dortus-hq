# Succesverhalen groei en marketing (Joris)

bezig: niets (laatste: VibeDesk, klaar 16 nov 2026 01:40 NL-tijd). Volgende: een kleine maker van een tool of Garmin-app die WEL groeide met korte filmpjes, met cijfers per filmpje, als tegenwicht voor VibeDesk.

Nieuwste bovenaan.

---

## 2. VibeDesk (Fred, solo, gratis Windows-app voor Claude Code): 20 Shorts zonder gezicht, met cijfers

Onderzocht 16 nov 2026, run 2. Open vraag uit run 1: wat deed een maker in zijn eerste 30 filmpjes, met kijkcijfers per filmpje? Waarom dit verhaal: een solo maker die precies doet wat Chris vanaf di 17 nov gaat doen (staande schermopnames, tekst in beeld, geen gezicht, geen stem) en zijn echte cijfers uit YouTube Studio en GitHub openbaar zet. Hij bouwt ook met Claude Code, net als wij. Het is geen succesverhaal maar een eerlijke mislukking, en daarom juist bruikbaar: zo ziet de start eruit als het niet vanzelf gaat.

### Bronnen
- Zijn eigen verslag op DEV, 3 nov 2026 (curl via de openbare API van DEV): https://dev.to/fxdgif/15-youtube-shorts-2674-views-1-subscriber-promoting-a-dev-tool-without-showing-my-face-2m8j
- Zijn eerste bericht over de app, 22 okt 2026, met 17 reacties (curl, API van DEV): https://dev.to/fxdgif/i-kept-missing-claude-codes-permission-prompts-so-i-built-a-desktop-around-it-8fc
- Zijn kanaal, tab Shorts en tab Video's (curl, de cijfers staan in de pagina zelf): https://www.youtube.com/@vibedesk-lounge/shorts
- De repo, sterren via de zoek-API van GitHub (gh api search): https://github.com/fxd-gif/vibedesk
- Ter vergelijking: de zoekpagina van YouTube voor "print in place joints blender" en "articulated print in place blender tutorial" (curl, 16 nov).
- Niet gelukt: de GitHub-pagina zelf (403 vanuit de cloud) en de afspeelpagina van YouTube (429). Kijkduur per filmpje en precieze plaatsingsdata heb ik dus alleen uit zijn eigen verslag.

### Cijfers
Uit zijn verslag (EIGEN OPGAVE, uit YouTube Studio, laatste 28 dagen tot 3 nov):
- 15 Shorts in twee weken: samen 2.674 views, 32 likes, **1 abonnee** uit Shorts.
- 70% veegde vrijwel meteen weg. Snelle, flitsende filmpjes: 19% tot 25% bleef kijken. Het beste filmpje (26 seconden, "sort my windows" typen en het zien gebeuren, geen effecten): 42% bleef.
- Elke Short kwam tussen 50 en 370 views. YouTube Studio zegt zelf: "usually get 140 to 220". 81% van de views kwam uit de Shorts-feed.
- GitHub: 21 unieke bezoekers in 14 dagen, waarvan 5 via YouTube. 0 sterren.
- Eén langer filmpje van 1:15 (gewone video, geen Short): 332 views, gemiddeld 51% bekeken, 80% van de views via de startpagina van YouTube, ook 1 abonnee.
- Eén eerlijk bericht op DEV ("I kept missing...") gaf 15 reacties en twee wensen die hij in de volgende versie bouwde.

Zelf nagekeken (GEZIEN 16 nov 2026):
- Kanaal: 20 Shorts en 2 gewone video's, 136 abonnees. Views per Short, nieuwste eerst: 97, 53, 39, 153, 84, 79, 55, 215, 151, 134, 363, 157, 196, 194, 284, 201, 245, 274, 72, 54. Samen 3.100. Hoogste 363 ("How much Claude Code did this project use today?"), laagste 39.
- De 7 Shorts van na zijn verslag halen samen 560 views (gemiddeld 80), lager dan de 13 oudere (gemiddeld ±195). Of dat komt door minder vaak plaatsen of door het onderwerp, weet ik niet.
- De gewone video's: "I vibecoded the Claude Code workspace I wished I had, in 12 days" 370 views; "VibeDesk in 5 minutes" 81 views.
- Repo: 0 sterren, 1 fork, aangemaakt 11 okt 2026.
- DEV: het eerste bericht heeft nu 17 reacties; zijn negen berichten daarna hebben 0 tot 2 reacties elk.
- Klopt niet helemaal: hij schrijft "+1 subscriber from Shorts", het kanaal heeft er nu 136. Waar de rest vandaan komt staat er niet; GOK: via zijn DEV-berichten en de link op zijn site, of later erbij gekomen.

Ter vergelijking, YouTube-zoekpagina (GEZIEN 16 nov): lange uitlegvideo's over beweegbare prints in Blender halen 38.000 tot 143.000 views ("Articulated Dragon 3d print // Blender tutorial" 142.783, "How To Design Articulating 3D Prints! Blender Tutorial!" 48.548, "How to Make Your Own Flexi STL Files (Free FlexiMaker Tutorial Using Blender)" 38.163). Maar twee nieuwe kleine kanalen met dezelfde soort uitleg halen 38 en 270 views. Lang is dus geen garantie, wel een kamer waar mensen met de vraag zitten.

### Wat hij deed, in volgorde
1. **Eerst een eerlijk bericht** op DEV met het probleem in één zin ("I kept missing Claude Code's permission prompts") en een filmpje erin. Reacties van mensen met hetzelfde probleem; hij antwoordde iedereen uitgebreid, opende issues voor hun wensen en bouwde ze in versie 2.0.
2. **Daarna 15 Shorts in twee weken**: eerst snel en flitsend, toen rustig met één idee per filmpje en een grote uitsnede van de app. Het aantal views veranderde niet.
3. **Opgeschreven en bijgestuurd**: hoogstens twee Shorts per week, langere rustige video's die iets beantwoorden waar mensen op zoeken, meer eerlijke berichten, en een kortere weg naar de download (de installer is niet ondertekend, dus Windows waarschuwt).
4. Daarna nog 5 Shorts; die deden het slechter.

### Drie lessen
1. **Bij een nichetool zonder gezicht bepaalt het filmpje de views nauwelijks.** Snel, traag, grappig of technisch: alles landde tussen 50 en 370. De feed laat een kleine testgroep kijken; vegen ze weg, dan stopt het. Wat wel verschil gaf in hoe lang mensen bleven: **één duidelijke handeling die je zelf zou willen** ("sort my windows", 42%), geen effecten. Dat sluit aan op McGybeer (verhaal 1): het product dat het werk doet in beeld, niet de knoppen.
2. **De Shorts-feed is een kamer vol mensen zonder jouw probleem.** Uit 3.000 views kwamen 5 bezoekers op de repo. In een Short kun je niet klikken. Een gewone, langere video kwam via de startpagina bij mensen die zulke video's kijken, en een eerlijk bericht kwam bij mensen met het probleem; die gaven allebei meer dan alle Shorts samen.
3. **Meet tot aan de download, niet tot aan de view.** Zijn eigen conclusie: uren in montage, bijna niets in de weg na de klik (releasepagina, .exe, waarschuwing van Windows). Views zonder downloads zeggen niets.

### Eerlijk: wat niet zomaar voor ons geldt
- Eén kanaal, één tool, vier weken, alleen YouTube. Geen TikTok en geen Reels. Op TikTok is het bereik voor nieuwe accounts mogelijk anders (GOK, niet gemeten).
- Zijn publiek (Windows-gebruikers van Claude Code) is kleiner en zijn drempel hoger (onondertekende .exe) dan bij Click Joints, dat je in Blender met één klik installeert van extensions.blender.org. Ons beeld (een figuur die buigt) is ook makkelijker te begrijpen dan een bureaublad met terminals. Onze Shorts kunnen dus beter doen (GOK).
- Hij schrijft zelf: "Maybe my hooks were just bad." Het kan aan zijn filmpjes liggen.
- Verwachting voor Chris, als GOK op basis van dit verhaal: de eerste Shorts halen 50 tot 400 views per stuk en leveren een handvol downloads. Dat is normaal en geen reden om na een week te stoppen; het besluit van 15 nov kijkt terecht pas na 20 tot 30 filmpjes.

### Voorstel voor Dortus deze week
**Naast de dagelijkse Shorts één gewone liggende YouTube-video (60 tot 120 seconden) die een zoekvraag beantwoordt**, titel in de vorm "How to make print-in-place joints in Blender (free add-on)": één figuur van begin tot geprint resultaat, rustig, tekst in beeld, geen gezicht, geen stem. Bij VibeDesk haalde zo'n video evenveel abonnees als alle Shorts samen en kwam hij via de startpagina bij het juiste publiek; in onze niche halen zulke uitlegvideo's bij gevestigde kanalen tienduizenden views. Kost weinig: Bram heeft de filmpijplijn al en de bestaande winkelplaatjes zijn liggend (1920 x 1080); of de film zelf liggend is, heb ik niet nagekeken. **Wie:** Chris maakt hem in week 1 of 2, Bram levert liggende opnames als die ontbreken, Thijs plaatst. **En meten:** Chris zet in zijn dagmeting per filmpje de views naast de downloads van Click Joints op extensions.blender.org (dagteller), zodat we na 20 tot 30 filmpjes zien of views downloads worden, niet alleen of de views stijgen.

---

## 1. McGybeer (Javier Rodríguez, solo, beweegbare 3D-print-figuren)

Onderzocht 15 nov 2026, run 1. Vraag van de hoofdchat: hoe groeiden kleine makers met korte filmpjes zonder gezicht? Waarom dit verhaal: dit is precies de hoek van Click Joints (beweegbare figuren die je in één keer print, ontworpen in Blender), en het is het bekendste voorbeeld van een 3D-ontwerp dat via TikTok groot werd.

### Bronnen
- Interview Snapmaker, 24 feb 2022 (curl): https://www.snapmaker.com/blog/3d-printed-articulated-dragon-model-designer-javier-rodriguez/
- Artikel 3DWithUs over beweegbare draken, 27 apr 2022, bijgewerkt 5 nov 2023 (curl): https://3dwithus.com/articulated-dragon-models-flexible-print-in-place-for-3d-printing
- Productpagina en profiel op Thangs (curl, cijfers uit de pagina zelf): https://thangs.com/designer/McGybeer/3d-model/Articulated%20Dragon-863344
- Zijn TikTok-profiel (curl, alleen de tellers bovenaan): https://www.tiktok.com/@mcgybeer
- Niet te lezen vanuit de cloud: Cults3D, Printables, Thingiverse, Patreon (403), 3dprint.com (Cloudflare), zijn eigen site mcgybeer.xyz (onbereikbaar). De lijst met zijn eigen TikTok-filmpjes heb ik niet kunnen ophalen: dat gaat alleen via een verborgen API of een browser die de pagina naspeelt, en dat doen we niet. Wat hij in zijn eerste 30 filmpjes deed, weet ik dus NIET.

### Cijfers
- Zijn eerste bekende ontwerp: Cute Mini Octopus (2019), gemaakt voor zijn roller-derbyteam (DERDEN, Snapmaker).
- De Articulated Dragon: "40K paid downloads" met "thousands of physical models sold across Etsy, eBay, Amazon" (DERDEN, 3DWithUs, stand ±2022 tot 2023, niet nagekeken).
- Eén filmpje van Snapmaker over de draak op Facebook (dec 2021): 15 miljoen views en 8.600 reacties, "the most popular case in the Snapmaker community ever" (DERDEN, Snapmaker).
- TikTok-account @mcgybeer aangemaakt op 17 dec 2020 (GEZIEN, tijdstip in de pagina). Nu: 43.263 volgers, 336.225 likes, 187 filmpjes (GEZIEN 15 nov 2026). Gemiddeld ±1.800 likes per filmpje (GOK, gewoon gedeeld).
- Thangs (GEZIEN 15 nov 2026): draak los $3,99, 396 downloads, 208.019 keer bekeken, 493 likes; profiel 70 modellen, 29.491 downloads, 3.536 volgers. Leden: $10 per maand (4 ontwerpen), $18 (8 ontwerpen), en drie **verkooplicenties**: $10, $18 en $60 per maand (de laatste met alles, onbeperkt).
- Omzet: niet openbaar. GOK: 40.000 x ±$4 tot $8 is $160k tot $320k bruto alleen voor de draak, maar de prijs per winkel en het aandeel dat via leden liep weet ik niet.

### Wat er gebeurde, in volgorde
1. **Eerst het mechaniek, dan het dier.** Hij wilde de draak al een jaar eerder maken, maar "my design skills were still not enough". Hij ontwierp eerst een nieuw soort gewricht, maakte "a bunch of prototypes", testte en paste aan, en pas daarna modelleerde hij de draak in Blender. Gewrichten eerst, "as they are the key and the rest of the model depends on them".
2. **Het ontwerp verspreidde zich via filmpjes van anderen.** "Its popularity grew mainly on TikTok and I didn't have an account back then." Printerbezitters en een printermerk (Snapmaker) filmden de draak die in de hand kronkelt; dat deed het werk. Zijn eigen account kwam pas daarna (dec 2020).
3. **Hij maakte er werk van verkopers.** Mensen die de draak printen en verkopen (Etsy, eBay, Amazon, markten) kopen een verkooplicentie. Elke verkoper die zijn print filmt om hem te verkopen, maakt zo reclame voor het ontwerp.
4. **Daarna een reeks in dezelfde vorm.** Cali-Dragon, hagedis, haai, ratelslang: steeds een beweegbaar dier dat je zonder steun print. Na de draak werd hij voltijds ontwerper, omdat hij "2-3 hours per day just responding to emails, messages, posts" kwijt was.

### Drie lessen
1. **Het filmpje dat werkt is het product dat beweegt in een hand, niet uitleg.** Het groeimoment kwam niet van zijn eigen filmpjes maar van anderen die het resultaat lieten kronkelen. Voor een product als Click Joints is het sterkste beeld dus de geprinte figuur die buigt, niet het Blender-paneel.
2. **Laat anderen filmen: geef ze een reden.** Een printermerk wil indrukwekkende prints laten zien, een verkoper wil zijn waar verkopen, een hobbyist wil laten zien wat hij maakte. McGybeer verdient aan die groep met een verkooplicentie. Voor ons: makers die met Click Joints iets printen, zijn het kanaal, niet ons eigen account alleen.
3. **Eerst een nieuw mechaniek dat je in één beeld ziet.** De draak was "the first highly detailed articulated design" (volgens hemzelf); het verschil was in twee seconden te zien. Een filmpje zonder gezicht werkt als het onderwerp zelf de haak is.

### Eerlijk: wat niet zomaar voor ons geldt
- Hij verkoopt **printbestanden** (iedereen kan het eindresultaat begrijpen). Wij verkopen een **Blender-add-on**: het publiek dat het eindresultaat leuk vindt is veel groter dan het publiek dat de add-on kan gebruiken. Een viraal filmpje van een kronkelende figuur levert ons dus minder kopers op dan hem (GOK).
- Het is één uitschieter uit 2020 tot 2021, toen beweegbare draken nieuw waren. Nu zijn er "lots of similar Dragon variations around"; het moment is voorbij.
- Over zijn eigen eerste 30 filmpjes heb ik niets kunnen vinden. Dat deel van de vraag blijft open.

### Voorstel voor Dortus deze week
**Een filmpje van een echt geprinte Click Joints-figuur die in een hand buigt** (8 tot 12 seconden, eerste seconde al bewegen, geen gezicht), als filmpje 6 in de reeks van Chris, en vanaf de lancering van Pro bij elke nieuwe figuur. Wie: Chris, met de print die al op de lijst van Thijs staat (echte print van een gewricht, alleen als hij of iemand die hij kent een printer heeft). Is er geen printer, dan vraagt Chris bij de lancering op r/3Dprinting of iemand een print wil laten zien, met credits (Thijs plaatst). Tot er een echte print is: Bram rendert een "hand"-beeld waarin de figuur buigt, eerlijk vermeld als render. En op de Pro-pagina een regel "Made something with Click Joints? Tag us, we share the best ones", zodat makers een reden hebben om zelf te filmen.

### Voor de ploeg: wat ik leerde over meten
Het openbare TikTok-profiel geeft met curl wel de tellers (volgers, likes, aantal filmpjes, aanmaakdatum) in het blok `__UNIVERSAL_DATA_FOR_REHYDRATION__`, maar niet de lijst met filmpjes. Handig om na de start van onze accounts elke dag volgers en likes te meten.
