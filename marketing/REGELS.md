# Regels van de marketingtak Roep

> **TikTok staat stil (Thijs 24 nov 17:50: "kut tiktoks die niemand kijkt").** Plan geen TikTok in en maak geen TikTok-concepten tot de hoofdchat deze regel weghaalt. De 3 geplande TikToks (24, 25, 27 nov) zijn door de hoofdchat op concept (draft) gezet in Metricool. TikTok komt pas terug met filmpjes die op YouTube al bewezen goed lopen (Regisseur, stem Max), en alleen na keuring. Lange YouTube-video's gaan gewoon door.


Gemaakt 19 nov 2026 door een bouwer, volgens de keuring van 19 nov (`platformen/ideeen/marketing-tak-2026-11-19/KEURING.md`), het ontwerp van onderzoeker B (`B-ontwerp.md`, run 5 tot 7) en de keuring van deze opzet (`marketing/KEURING.md`). Wie deze regels wil veranderen: een regel onderaan `organisatie/besluiten.md` en een bericht aan de hoofdchat.

**Doel: Click Joints Pro verkopen** ($19 op Gumroad, ook op Superhive; prijs bijgewerkt 20 nov). Het is nu het enige product dat via onze eigen kanalen geld kan opleveren: de gratis add-on mag in Blender niet naar Pro wijzen (voorwaarden extensions.blender.org 6.1 tot 6.3, GEZIEN door onderzoeker B). Bereik telt alleen als het naar een klik op een winkel leidt.

## Meetadressen (in posts alleen deze)
| Kanaal | Adres in de post | Wat het is |
|---|---|---|
| TikTok | `dortus.com/tt` (over te typen, zonder https) | korte Pro-pagina met de knop naar Gumroad |
| Lange YouTube-video | `https://dortus.com/yt/` (klikbaar) | dezelfde korte Pro-pagina, eigen adres |

- De pagina's staan in de site-repo (`tt/index.html`, `yt/index.html`), met het Amami-script, `noindex` en niet in de sitemap. Zo is elk bezoek aan een van de twee aan één kanaal te koppelen.
- **Geen Gumroad-link in een post**, ook niet in de eerste reactie: die gaat langs de meting heen en het winkeladres bevat een deel van de accountnaam van Thijs. Ook geen `dortus.com/click-joints` meer in nieuwe posts (dat telt mee met alle andere bezoekers van die pagina).
- **Meting:** het scorebord telt nu per pad alleen de voorpagina, de vier productpagina's en "overig" (GEZIEN, `organisatie/controle/scorebord_amami.py`, `PAGINAS` en `pagina_van`). `/tt` en `/yt` vallen dus nog samen onder "overig". De hoofdchat laat ze als eigen kolom toevoegen (`marketing/VOORSTEL-hoofdchat.md`). **Tot er in `organisatie/scorebord.md` een eigen getal voor tt en yt staat, schrijft de Maker "niet gemeten"** en leunt de geld-stopregel alleen op Gumroad-verkopen.

**Eerlijk vooraf:** in week 1 maakt, keurt en plaatst de tak zelfstandig, maar reageert hij nergens op mensen (de Metricool-koppeling heeft geen inbox, YouTube-reacties lezen vraagt een sleutel die er niet is). Verwacht geld in de eerste weken: tientallen dollars, geen honderden, tenzij één video groot gaat (GOK, op basis van ±0,1 verkoop per 1.000 weergaven uit B).

## Wie doet wat
| Wie | Doet | Doet nooit |
|---|---|---|
| **Maker** (geplande taak "Dortus Roep: maken en plaatsen") | concepten maken, groen gekeurde concepten inplannen via Metricool, adres en cijfers teruglezen, dagrapport, `commercie/geplaatst.md` | eigen concepten keuren, iets plaatsen wat niet groen is, reageren op mensen |
| **Keurder** (geplande taak "Dortus Roep: keuren") | elk open concept keuren met het formulier hieronder, beelden zelf bekijken | iets maken, iets plaatsen, Metricool gebruiken (heeft de koppeling niet) |
| **Hoofdchat-ronde** | beslist over oranje (zet dan zelf groen of rood), houdt Maker en Keurder in de gaten, kan `marketing/STOP` zetten | zelf plaatsen via Metricool zodra de Maker draait |
| **Chris en andere agents** | mogen concepten aanleveren in `marketing/wachtrij/` in hetzelfde formaat | zelf plaatsen of keuren |

**Eén eigenaar van plaatsen:** alleen de Maker plaatst via Metricool (brand 8156503). Zo kan het quotum van 20 per maand niet dubbel opgaan. Overgang: zolang er op main geen commit met kop `Roep-Maker:` staat (na te gaan met git log), plaatst de hoofdchat-ronde nog zoals vroeger (één teken, besluit 19 nov opruimen fase 1).

## Wat de tak mag
- **Kanalen:** TikTok @dortusstudio en YouTube @Dortusapps, allebei via Metricool. Verder niets in deze fase (geen Bluesky, Mastodon, X, Reddit, Hacker News, fora, Steam, mail).
- **Schrijf als Dortus:** "we", "Click Joints", "our add-on". Nooit in de ik-vorm, nooit als Thijs ("I made" is fout, "We made" is goed). Nooit de naam van Thijs in een post.
- **Beeld en geluid:** alleen echte schermbeelden of opnames uit het product. Video alleen uit bestanden die eindigen op `-geluid.mp4` en waarvoor `python3 organisatie/controle/geluid_check.py <bestand>` GOED zegt. Een TikTok-diashow mag alleen uit echte schermbeelden, met `autoAddMusic: true`.
- **Geen AI-beeld en geen AI-persoon** (besluit Thijs 19 nov 01:30). **Uitzondering sinds 23 nov (wens Thijs): een voice-over met een AI-stem mag**: een open stem met commerciële licentie (Kokoro, Apache 2.0) of ElevenLabs (stem Max, ook het gratis plan, besluit Thijs 23 nov 18:54; de opname maakt alleen de hoofdchat via het account van Thijs), nooit een stemkloon van iemand zonder toestemming. **Geen vermelding van AI of van de stem in titel of beschrijving** (Thijs 23 nov 20:28: "AI niet in de beschrijving, dat slaat nergens op"). Wel zet de hoofdchat bij het uploaden in YouTube Studio "Altered content" op Yes (`isAiGeneratedContent` true, TikTok `isAigc` true): YouTube eist dat bij een gesynthetiseerde stem die echt klinkt, en zet anders zelf een label (DERDEN: https://support.google.com/youtube/answer/14328491). Dat vinkje is geen tekst in de beschrijving. Zonder AI-stem blijven die velden `false`. De velden `isAigc` (TikTok) en `isAiGeneratedContent` (YouTube) blijven op de standaard `false`; dat klopt omdat beeld en geluid echt zijn (het geluid van de filmpjes is met code gemaakt, GEZIEN in `marketing/KEURING.md`). Zou een concept ooit AI-beeld of AI-geluid nodig hebben: rood.
- **Nooit:** iets onder de naam van Thijs, geld uitgeven, reageren op mensen, persoonsgegevens (Metricool `getBrandSettings` geeft een mailadres van Thijs terug: dat komt nooit in een bestand), andermans posts of spullen weghalen.

## Materiaal (waar de Maker echte beelden vindt)
- Filmpjes met geluid: de releases van de Click Joints-filmpjes in deze repo (`filmpjes-week-1` en latere releases met `-geluid.mp4`; lijst via `https://api.github.com/repos/thijsduinhouwer2002-coder/dortus-hq/releases`). Die in de laatste 14 dagen al uitgingen, tellen niet als nieuw (vraag 8).
- Schermbeelden voor een diashow: `commercie/blender-click-joints/`, `ontwerp/click-joints/` en de beelden op `dortus.com/click-joints/`. Openbare URL via `https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/<pad>` (de repo is openbaar).
- Een nieuwe lange YouTube-video kan de Maker niet zelf opnemen: die vraagt hij aan Chris (zie de rem hieronder).

## Rem op maken
- Hoogstens **2 nieuwe concepten per dag**, elk met bronnen.
- Na **2 keer rood achter elkaar**, of als er geen bruikbaar materiaal is: één bericht onderaan `berichten/hoofdchat.md` en niets meer maken tot de hoofdchat antwoordt of er nieuw materiaal is.
- Chris alleen vragen (onderaan `berichten/chris.md`) als daar in de laatste 48 uur geen open vraag van Roep staat.

## Keurformulier (10 vragen; alle 10 ja en de techniek-check groen = groen)
1. Klopt elke bewering met een bron die in het concept staat (changelog, winkelpagina, meting)?
2. Geen AI-zinnen ("Great question", "game-changer", "unlock", "dive in", "elevate"), en alleen een AI-melding als er een AI-stem in zit (dan verplicht)?
3. Geen medische claim (geldt voor Ebb: "rustiger", nooit "tegen stress" of "genezen")?
4. Niets over Hats in spelersstem (die tekst schrijft Thijs)?
5. Beeld uit het echte product, door de Keurder zelf bekeken (losse beelden uit de video gehaald en geopend); video eindigt op `-geluid.mp4` en `geluid_check.py` zegt GOED?
6. Geen persoonsgegevens, geen adres, mail of naam van Thijs, geen Gumroad-link (alleen de meetadressen)?
7. Past bij het kanaal: lengte, haak in de eerste seconde, één idee per post, titel begint met waar het over gaat ("Blender hinge ...")?
8. Niet bijna gelijk aan een post van de laatste 14 dagen op hetzelfde kanaal (`commercie/geplaatst.md`)?
9. **Geen AI-beeld en geen AI-persoon**, en een eventuele AI-stem alleen volgens de uitzondering van 23 nov (open stem met commerciële licentie, of ElevenLabs zoals in de regel hierboven; niets over AI in titel of beschrijving, wel het vinkje Altered content)? Heeft de Short een echte hook in de eerste 1,5 s (recept v3)?
10. **Schrijft als Dortus** ("we"), nergens in de ik-vorm als Thijs?

## Uitkomst
- **groen:** eigen kanaal, gewone post, alle 10 ja, techniek-check zonder oranje of rood. De Maker mag inplannen.
- **oranje:** wacht op de hoofdchat-ronde. Altijd bij: een prijs of korting, de Cyber Sale, alles over Hats, een antwoord op een klacht, en de oranje regels uit de techniek-check. De hoofdchat zet het op groen of rood. **Geen besluit binnen 24 uur = rood** (de Maker zet het).
- **rood:** een vraag is nee, of iets onder de naam van Thijs, of tegen een regel. Met een reden van één zin. De Maker mag het concept verbeteren en als **nieuw** bestand opnieuw op open zetten; het rode bestand blijft staan.

## Techniek-check per kanaal (de Keurder vóór groen; de Maker nog een keer vlak voor inplannen)
**Alle kanalen**
- `marketing/STOP` bestaat niet (bestaat het wel: niets keuren, niets plaatsen).
- Het mediabestand staat op een openbare URL die met `curl -sIL` 200 geeft (Metricool neemt alleen openbare URL's).
- De geplande tijd ligt in de toekomst; plafond per dag en quotum per maand niet overschreden.
- Geen `<` of `>` in titel, tekst of eerste reactie (YouTube weigert dat; filmpje 7 mislukte erop).
- Een Gumroad-adres (`gumroad.com`) in titel, tekst of eerste reactie: rood.

**TikTok @dortusstudio (persoonlijk account, geen zakelijk account: dat vraagt KvK-verificatie)**
- Geen bio-link, geen eerste reactie, geen eigen omslag. `firstCommentText` moet leeg zijn; anders rood.
- **Een TikTok die naar een klikbare link verwijst ("link in bio", "tap the link", "click below", een `https://`-adres): rood.** Er is geen klikbare link op ons TikTok-profiel.
- Wel goed: het over te typen meetadres `dortus.com/tt` in de tekst (zonder https).
- Video heeft een geluidsspoor (`-geluid.mp4`, GOED), of een diashow uit echte schermbeelden met `autoAddMusic: true`.
- Tekst hoogstens 2.200 tekens (GOK), 5 tot 7 hashtags.

**YouTube @Dortusapps, lange (liggende) video: de enige klikbare verkoopweg**
- `youtubeData.type: "video"`, liggend, titel hoogstens 100 tekens, `madeForKids: false`.
- Eerste regel van de beschrijving `https://dortus.com/yt/`, en hetzelfde adres in `firstCommentText`. **Ontbreekt een van de twee: oranje.**
- Kanaallink "Click Joints Pro" naar https://dortus.com/yt/ staat bovenaan het kanaal (hoofdchat, 20 nov 14:38; was "($12)" naar Gumroad); daar hoeft de tak niets aan te doen. Een bestaande post of kanaallink aanpassen (geen nieuwe post, geen quotum) doet de hoofdchat na keuring door een ander (besluit 20 nov 14:40). Let op: /yt telt ook bezoek uit de kanaallink en de Short 65JiRlDupNc.

**YouTube Short (sinds 21 nov ±12:40: de Shorts-motor)**
- Afgekeken: CatPin (400+ verkopen in 3 maanden) en Cleave (200+ in 2 maanden, 3 Shorts per dag, 700 tot 1.600 weergaven per stuk, 157 abonnees) verkopen hun Blender-add-ons voor 3D-print met dagelijkse Shorts op hun eigen kanaal (GEZIEN 21 nov, `platformen/ideeen/afkijken-2-2026-11-21/A-blender-kopers.md`). De oude regel "een Short verkoopt niets" vervalt.
- **Wie plaatst:** de hoofdchat, zelf in YouTube Studio in Chrome op de HP van Thijs (staat 24/7 aan, Thijs 21 nov 13:18), elke avond om 21:17 na de keurronde van 20:43 (herinnering in de hoofdchat, die zichzelf elke dag opnieuw zet), buiten Metricool om (keuze Thijs 21 nov ±12:40: "Gratis: ik upload zelf"; Metricool blijft voor TikTok en lange video's). De hoofdchat plant gekeurde Shorts in een sessie in voor de komende dagen (YouTube Studio: inplannen), **2 tot 3 per dag**, op vaste tijden (bijvoorbeeld 12:00, 17:00, 20:00 NL).
- **Keuring:** een Short gaat alleen uit als hij **groen** is: groen gekeurd door de Keurder van Roep of door Daan (skill keuren, de 10 vragen hierboven en de techniek-check). Een Short is niet meer vanzelf oranje; wel oranje bij een prijs, korting of Hats. Let op: de vaste opdracht van de Keurder van Roep zegt nog "elke Short is oranje" (die opdracht kan de hoofdchat niet aanpassen). Is een Short alleen daarom oranje en zijn alle 10 vragen ja en de techniek-check goed, dan schrijft de hoofdchat in de ronde van 21:17 een ## Oranje-besluit (groen, reden: REGELS 21 nov) en plant hem in.
- **Vorm (afgekeken van Cleave en CatPin):** één figuur, één belofte in de titel (bijvoorbeeld "Make a goblin poseable: 8 joints in Blender"), haak in de eerste seconde, echte beelden uit Blender, 40 tot 60 seconden als les (recept v2, afgekeken van Malikose, 22 nov; eerste beeld = een mooi eindresultaat, geen scherm vol getallen), beschrijving met het over te typen dortus.com/yt. Bij elke Short als "Gerelateerde video" de nieuwste lange Pro-video (de enige klikbare link). Eerlijk: zeg of toon nooit dat wij geprint hebben of dat het klikt, maar schrijf ook nergens "not print tested" of "not printed yet" (besluit Thijs 24 nov 15:32); waar het over printen gaat: "Print the Fit test strip first: every printer is different." Slot van elke Short: "Click Joints Pro, on Gumroad" (saleweek: "25% off this week").
- **Wie maakt:** Chris en de Maker van Roep, als concept in `marketing/wachtrij/` met kanaal `youtube-short`. Voorraad: minstens 7 groene Shorts klaar.
- Na plaatsen: de hoofdchat zet per Short een regel onderaan `commercie/geplaatst.md` (datum, adres, titel).

**Na plaatsen (de Maker, in de eerstvolgende ronde na het plaatsmoment)**
- Status in Metricool lezen: PUBLISHED of ERROR.
- Adres van de post teruglezen en de handle controleren. TikTok: Metricool-cijfer `TKPO03` ("Video Url"); is dat nog leeg (de statistiek loopt soms achter), lees dan het openbare profiel `https://www.tiktok.com/@dortusstudio` met curl en zoek de nieuwe video. Daarna de videopagina met curl: `uniqueId` moet `dortusstudio` zijn, `playCount` is het aantal weergaven (Metricool telt minder). YouTube: de RSS van het kanaal (`https://www.youtube.com/feeds/videos.xml?channel_id=UCTspMNCOwnBkGT2LZ7tB2dg`).
- **Mislukt** alleen bij status ERROR, of als er 24 uur na het plaatsmoment nog geen adres is (niet in Metricool, niet op het profiel, niet in de RSS). Dan: bovenaan `marketing/dagrapport.md` onder "Open fouten", bericht onderaan `berichten/hoofdchat.md`, en nieuwe concepten van dat kanaal gaan naar oranje tot de hoofdchat het oplost.
- Controleer altijd op het adres van de geplaatste post, nooit op namen in de instellingen (Metricool toont nog de oude naam `screencuts.co`; dat is wel @dortusstudio).

## Plafonds en quotum
Metricool Free: **20 posts per maand voor het hele merk** (alle kanalen samen, GEZIEN help.metricool.com). Alleen de Maker plaatst, dus alleen de Maker telt.

| Maand | TikTok | Lange YouTube | Reserve | Samen |
|---|---|---|---|---|
| november (vanaf 20 nov) | 8 | 2 | 2 | 12 |
| december | 14 | 4 | 2 | 20 |

- **Per dag:** hoogstens 1 TikTok en 1 lange YouTube-video.
- **Lange YouTube-video's gaan voor:** zodra er een groene is, krijgt die de eerste vrije plek, ook vóór TikToks die al groen klaarstaan.
- De posts die de hoofdchat al inplande (filmpje 2 op 19 nov, filmpje 5 op 20 nov) tellen mee in november. Filmpje 5 is twee keer opnieuw aangemaakt; of Metricool dat dubbel telt is niet bekend (GOK). De Maker telt elke ronde opnieuw (`getScheduledPosts` plus `commercie/geplaatst.md`). Is er minder over dan de tabel zegt, dan schrapt hij eerst TikToks, daarna de reserve, het laatst de lange YouTube-video's.
- Weigert Metricool een post om het quotum: niet opnieuw proberen, melden aan de hoofdchat.
- **Reserve:** alleen voor spoed, op besluit van de hoofdchat (een mislukte post opnieuw, een Cyber Sale-post na oranje, een Short).

## Stopregel (staat ook als stap in de Maker-opdracht)
- **TikTok Click Joints, vanaf di 1 dec 2026:** staat er geen TikTok met meer dan 1.000 weergaven en gemiddeld meer dan 5 seconden kijktijd, dan plant de Maker geen TikTok meer in en meldt hij het de hoofdchat. Het TikTok-deel van het quotum van december gaat dan naar lange YouTube-video's of een andere vorm, op besluit van de hoofdchat. Nulmeting: onze beste TikTok staat op 305 weergaven (GEZIEN, keuring 19 nov 07:15 UTC, video 7709157242309774625).
- **Geld:** 14 dagen achter elkaar posts zonder één verkoop van Pro (Gumroad, uit `organisatie/scorebord.md`): melden in het dagrapport en aan de hoofdchat; de hoofdchat kiest een andere vorm.
- **Noodrem:** `marketing/STOP` (mag Thijs of de hoofdchat aanmaken) zet de hele tak stil. Mislukt een post of komt er een klacht: de hoofdchat haalt hem weg en meldt het Thijs.

## Waar alles gelogd wordt
- **Geen lege rondes:** is er sinds de vorige ronde niets teruggelezen, ingepland, gemaakt of gekeurd, dan schrijft niemand iets en wordt er niets vastgelegd; alleen het eindantwoord van de taak.
- `marketing/wachtrij/`: elk concept met zijn keuring (formaat in `marketing/wachtrij/LEESMIJ.md`).
- `commercie/geplaatst.md`: elke inplanning en elke plaatsing, één regel onderaan (datum, kanaal, Metricool-nummer, adres). Geen regels voor rondes zonder plaatsing.
- `marketing/dagrapport.md`: **één blok per dag**, in de ronde van 20:13 (wat uitging, adres, weergaven, kijktijd, meetadressen of "niet gemeten", Gumroad-verkopen, quotum over, voorraad). Daarnaast alleen een korte regel als er iets uitging of misging. Fouten bovenaan onder "Open fouten".
- `berichten/hoofdchat.md`: oranje concepten, fouten en alles wat de hoofdchat moet weten, onderaan met datum en "van Roep-Maker" of "van Roep-Keurder".
