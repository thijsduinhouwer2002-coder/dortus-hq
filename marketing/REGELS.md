# Regels van de marketingtak Roep

Gemaakt 19 nov 2026 door een bouwer, volgens de keuring van 19 nov (`platformen/ideeen/marketing-tak-2026-11-19/KEURING.md`) en het ontwerp van onderzoeker B (`B-ontwerp.md`, run 5 tot 7). Wie deze regels wil veranderen: een regel onderaan `organisatie/besluiten.md` en een bericht aan de hoofdchat.

**Doel: Click Joints Pro verkopen** ($12 op Gumroad, later Superhive). Het is nu het enige product dat via onze eigen kanalen geld kan opleveren: de gratis add-on mag in Blender niet naar Pro wijzen (voorwaarden extensions.blender.org 6.1 tot 6.3, GEZIEN door onderzoeker B). Bereik telt alleen als het naar een klik op een winkel leidt. **Meetlat:** Gumroad-verkopen en bezoeken aan `dortus.com/click-joints/?ref=tt|yt` per dag, naast de posts van die dag (`organisatie/scorebord.md`).

**Eerlijk vooraf (moet 6 van de keuring):** in week 1 maakt, keurt en plaatst de tak zelfstandig, maar reageert hij nergens op mensen (de Metricool-koppeling heeft geen inbox, YouTube-reacties lezen vraagt een sleutel die er niet is). Verwacht geld in de eerste weken: tientallen dollars, geen honderden, tenzij één video groot gaat (GOK, op basis van ±0,1 verkoop per 1.000 weergaven uit B).

## Wie doet wat
| Wie | Doet | Doet nooit |
|---|---|---|
| **Maker** (geplande taak "Roep: maken en plaatsen") | concepten maken, groen gekeurde concepten inplannen via Metricool, adres en cijfers teruglezen, dagrapport, `commercie/geplaatst.md` | eigen concepten keuren, iets plaatsen wat niet groen is, reageren op mensen |
| **Keurder** (geplande taak "Roep: keuren") | elk open concept keuren met het formulier hieronder, beelden zelf bekijken | iets maken, iets plaatsen, Metricool gebruiken (heeft de koppeling niet) |
| **Hoofdchat-ronde** | beslist over oranje, houdt Maker en Keurder in de gaten, kan `marketing/STOP` zetten | zelf plaatsen via Metricool (Metricool is van de Maker) |
| **Chris en andere agents** | mogen concepten aanleveren in `marketing/wachtrij/` in hetzelfde formaat | zelf plaatsen of keuren |

**Eén eigenaar van plaatsen:** alleen de Maker plaatst via Metricool (brand 8156503). Zo kan het quotum van 20 per maand niet dubbel opgaan.

## Wat de tak mag
- **Kanalen:** TikTok @dortusstudio en YouTube @Dortusapps, allebei via Metricool. Verder niets in deze fase (geen Bluesky, Mastodon, X, Reddit, Hacker News, fora, Steam, mail).
- **Schrijf als Dortus:** "we", "Click Joints", "our add-on". Nooit in de ik-vorm, nooit als Thijs ("I made" is fout, "We made" is goed). Nooit de naam van Thijs in een post.
- **Beeld en geluid:** alleen echte schermbeelden of opnames uit het product. Video alleen uit bestanden die eindigen op `-geluid.mp4` en waarvoor `python3 organisatie/controle/geluid_check.py <bestand>` GOED zegt. Een TikTok-diashow mag alleen uit echte schermbeelden, met `autoAddMusic: true`.
- **Geen AI-beeld, geen AI-stem, geen AI-persoon, nergens een AI-melding** (besluit Thijs 19 nov 01:30). De velden `isAigc` (TikTok) en `isAiGeneratedContent` (YouTube) blijven op de standaard `false`; dat klopt omdat beeld en geluid echt zijn. Zou een concept ooit AI-beeld of AI-geluid nodig hebben: rood.
- **Nooit:** iets onder de naam van Thijs, geld uitgeven, reageren op mensen, persoonsgegevens (Metricool `getBrandSettings` geeft een mailadres van Thijs terug: dat komt nooit in een bestand), andermans posts of spullen weghalen.

## Keurformulier (10 vragen; alle 10 ja en de techniek-check groen = groen)
1. Klopt elke bewering met een bron die in het concept staat (changelog, winkelpagina, meting)?
2. Geen AI-zinnen ("Great question", "game-changer", "unlock", "dive in", "elevate") en nergens een AI-melding?
3. Geen medische claim (geldt voor Ebb: "rustiger", nooit "tegen stress" of "genezen")?
4. Niets over Hats in spelersstem (die tekst schrijft Thijs)?
5. Beeld uit het echte product, door de Keurder zelf bekeken (losse beelden uit de video gehaald en geopend); video eindigt op `-geluid.mp4` en `geluid_check.py` zegt GOED?
6. Geen persoonsgegevens, geen adres, mail of naam van Thijs?
7. Past bij het kanaal: lengte, haak in de eerste seconde, één idee per post, titel begint met waar het over gaat ("Blender hinge ...")?
8. Niet bijna gelijk aan een post van de laatste 14 dagen op hetzelfde kanaal (`commercie/geplaatst.md`)?
9. **Geen AI-beeld, geen AI-stem, geen AI-persoon** in beeld of geluid?
10. **Schrijft als Dortus** ("we"), nergens in de ik-vorm als Thijs?

## Uitkomst
- **groen:** eigen kanaal, gewone post, alle 10 ja, techniek-check zonder oranje of rood. De Maker mag inplannen.
- **oranje:** wacht op de hoofdchat-ronde. Altijd bij: een prijs of korting, de Cyber Sale, alles over Hats, een antwoord op een klacht, en de oranje regels uit de techniek-check. De hoofdchat zet het op groen of rood. **Geen besluit binnen 24 uur = rood.**
- **rood:** een vraag is nee, of iets onder de naam van Thijs, of tegen een regel. Met een reden van één zin. De Maker mag het concept verbeteren en als **nieuw** bestand opnieuw op open zetten; het rode bestand blijft staan.

## Techniek-check per kanaal (de Keurder vóór groen; de Maker nog een keer vlak voor inplannen)
**Alle kanalen**
- `marketing/STOP` bestaat niet (bestaat het wel: niets keuren, niets plaatsen).
- Het mediabestand staat op een openbare URL die met `curl -sIL` 200 geeft (Metricool neemt alleen openbare URL's).
- De geplande tijd ligt in de toekomst; plafond per dag en quotum per maand niet overschreden.
- Geen `<` of `>` in titel, tekst of eerste reactie (YouTube weigert dat; filmpje 7 mislukte erop).

**TikTok @dortusstudio (persoonlijk account, geen zakelijk account: dat vraagt KvK-verificatie)**
- Geen bio-link, geen eerste reactie, geen eigen omslag. `firstCommentText` moet leeg zijn; anders rood.
- **Een TikTok die naar een klikbare link verwijst ("link in bio", "tap the link", "click below", een `https://`-adres): rood.** Er is geen klikbare link op ons TikTok-profiel.
- Wel goed: de over te typen verwijzing `dortus.com/click-joints` in de tekst (zonder https), of "search Click Joints in Blender".
- Video heeft een geluidsspoor (`-geluid.mp4`, GOED), of een diashow uit echte schermbeelden met `autoAddMusic: true`.
- Tekst hoogstens 2.200 tekens (GOK), 5 tot 7 hashtags.

**YouTube @Dortusapps, lange (liggende) video: de enige klikbare verkoopweg**
- `youtubeData.type: "video"`, liggend, titel hoogstens 100 tekens, `madeForKids: false`.
- Bovenaan de beschrijving (eerste regel) de Gumroad-link of `https://dortus.com/click-joints/?ref=yt`, en dezelfde link in `firstCommentText`. **Ontbreekt een van de twee: oranje.**
- Kanaallink "Click Joints Pro ($12)" staat al bovenaan het kanaal (hoofdchat 19 nov 10:55); daar hoeft de tak niets aan te doen.

**YouTube Short**
- **Een URL in de tekst, titel of eerste reactie van een Short: oranje** (links onder Shorts zijn niet klikbaar sinds 31 aug 2023, DERDEN). Shorts zitten niet in het quotum; alleen na een oranje-besluit van de hoofdchat, uit de reserve.

**Na plaatsen (de Maker, in de eerstvolgende ronde na het plaatsmoment)**
- Status in Metricool lezen: PUBLISHED of ERROR.
- Adres van de post teruglezen en de handle controleren: TikTok via Metricool-cijfer `TKPO03` ("Video Url"), daarna de openbare videopagina met `curl` (`uniqueId` moet `dortusstudio` zijn; `playCount` is het aantal weergaven, Metricool telt minder). YouTube via de RSS van het kanaal (`https://www.youtube.com/feeds/videos.xml?channel_id=UCTspMNCOwnBkGT2LZ7tB2dg`).
- Geen adres binnen 2 uur na het plaatsmoment, of status ERROR: bovenaan `marketing/dagrapport.md`, bericht onderaan `berichten/hoofdchat.md`, en dat soort post gaat terug naar oranje tot de hoofdchat het oplost.
- Controleer altijd op het adres van de geplaatste post, nooit op namen in de instellingen (Metricool toont nog de oude naam `screencuts.co`; dat is wel @dortusstudio).

## Plafonds en quotum
Metricool Free: **20 posts per maand voor het hele merk** (alle kanalen samen, GEZIEN help.metricool.com). Alleen de Maker plaatst, dus alleen de Maker telt.

| Maand | TikTok | Lange YouTube | Reserve | Samen |
|---|---|---|---|---|
| november (vanaf 20 nov) | 8 | 2 | 2 | 12 |
| december | 14 | 4 | 2 | 20 |

- **Per dag:** hoogstens 1 TikTok en 1 lange YouTube-video.
- De posts die de hoofdchat al inplande (filmpje 2 op 19 nov, filmpje 5 op 20 nov) tellen mee in november. De Maker telt elke ronde opnieuw wat er deze maand in Metricool staat of uitging (`getScheduledPosts` plus wat in `commercie/geplaatst.md` staat). Is er minder over dan de tabel zegt, dan schrapt hij eerst TikToks, daarna de reserve, en het laatst de lange YouTube-video's (die kunnen verkopen).
- **Reserve:** alleen voor spoed, op besluit van de hoofdchat (een mislukte post opnieuw, een Cyber Sale-post na oranje, een Short).

## Stopregel (1 dec 2026)
- **TikTok Click Joints:** staat er vóór di 1 dec geen TikTok met meer dan 1.000 weergaven en gemiddeld meer dan 5 seconden kijktijd, dan stopt die reeks. Het TikTok-deel van het quotum van december gaat dan naar lange YouTube-video's of een andere vorm, op besluit van de hoofdchat. Nulmeting: onze beste TikTok staat op 305 weergaven (GEZIEN, keuring 19 nov 07:15 UTC, video 7709157242309774625).
- **Geld:** 14 dagen achter elkaar posts zonder één verkoop van Pro of één bezoek met `?ref=`: de Maker meldt het in het dagrapport en de hoofdchat kiest een andere vorm.
- **Noodrem:** `marketing/STOP` (mag Thijs of de hoofdchat aanmaken) zet de hele tak stil. Mislukt een post of komt er een klacht: de hoofdchat haalt hem weg en meldt het Thijs.

## Waar alles gelogd wordt
- `marketing/wachtrij/`: elk concept met zijn keuring (formaat in `marketing/wachtrij/LEESMIJ.md`).
- `commercie/geplaatst.md`: elke inplanning en elke plaatsing, één regel onderaan (datum, kanaal, Metricool-nummer, adres). Ook een Maker-ronde zonder plaatsing is één regel.
- `marketing/dagrapport.md`: per Maker-ronde onderaan: wat er uitging, adres, weergaven, kijktijd, bezoeken met `?ref=`, Gumroad-verkopen van die dag, quotum over, ERROR's, voorraad concepten. Fouten bovenaan.
- `berichten/hoofdchat.md`: oranje concepten, ERROR's en alles wat de hoofdchat moet weten, onderaan met datum en "van Roep-Maker" of "van Roep-Keurder".
