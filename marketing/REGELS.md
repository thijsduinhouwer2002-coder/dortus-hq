# Regels van de marketingtak Roep

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
- **Geen AI-beeld, geen AI-stem, geen AI-persoon, nergens een AI-melding** (besluit Thijs 19 nov 01:30). De velden `isAigc` (TikTok) en `isAiGeneratedContent` (YouTube) blijven op de standaard `false`; dat klopt omdat beeld en geluid echt zijn (het geluid van de filmpjes is met code gemaakt, GEZIEN in `marketing/KEURING.md`). Zou een concept ooit AI-beeld of AI-geluid nodig hebben: rood.
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
2. Geen AI-zinnen ("Great question", "game-changer", "unlock", "dive in", "elevate") en nergens een AI-melding?
3. Geen medische claim (geldt voor Ebb: "rustiger", nooit "tegen stress" of "genezen")?
4. Niets over Hats in spelersstem (die tekst schrijft Thijs)?
5. Beeld uit het echte product, door de Keurder zelf bekeken (losse beelden uit de video gehaald en geopend); video eindigt op `-geluid.mp4` en `geluid_check.py` zegt GOED?
6. Geen persoonsgegevens, geen adres, mail of naam van Thijs, geen Gumroad-link (alleen de meetadressen)?
7. Past bij het kanaal: lengte, haak in de eerste seconde, één idee per post, titel begint met waar het over gaat ("Blender hinge ...")?
8. Niet bijna gelijk aan een post van de laatste 14 dagen op hetzelfde kanaal (`commercie/geplaatst.md`)?
9. **Geen AI-beeld, geen AI-stem, geen AI-persoon** in beeld of geluid?
10. **Schrijft als Dortus** ("we"), nergens in de ik-vorm als Thijs?

## Uitkomst
- **groen:** eigen kanaal, gewone post, alle 10 ja, techniek-check zonder oranje of rood. De Maker mag inplannen.
- **oranje:** wacht op de hoofdchat-ronde. Altijd bij: **elke YouTube Short**, een prijs of korting, de Cyber Sale, alles over Hats, een antwoord op een klacht, en de oranje regels uit de techniek-check. De hoofdchat zet het op groen of rood. **Geen besluit binnen 24 uur = rood** (de Maker zet het).
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
- Kanaallink "Click Joints Pro ($12)" staat al bovenaan het kanaal (hoofdchat 19 nov 10:55); daar hoeft de tak niets aan te doen.

**YouTube Short**
- **Elke Short is oranje**, met of zonder URL. Shorts gaan alleen uit de reserve, na een besluit van de hoofdchat (links onder Shorts zijn niet klikbaar sinds 31 aug 2023, DERDEN, dus een Short verkoopt niets).

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
