# J: eigen publiek (maillijst, Discord) en doorverwijzen tussen onze producten

Agent J, 18 nov 2026, opdracht `BRIEF.md` (aanvulling 20:45). Alle webpagina's gelezen met curl op 18 nov ±21:00 tot 22:00 UTC. **GEZIEN** = zelf gelezen in officiële documentatie, de API of onze repo. **DERDEN** = iemand anders zegt het, met link. **GOK** = niet nagekeken of eigen rekensom.

**Al bekend (niet overgedaan):**
- Tiny Glade: 28% doorklik uit de maillijst tegen 1% of minder uit sociale media (D, `D-steam.md`).
- D actie 1: `dortus.com/hats` met aanmeldvak en Discordlink vóór de Steampagina; D A3: Steam-RSS naar Discord; D A6: Kit gratis tot 10.000.
- E stap 6: maillijst via Gumroad-volgers en `/v2/emails`; Buttondown gratis tot 100.
- A: Superhive "Upgrade Variant" (Free als Lite, Pro als upgrade); Hat Tower staat op 10 downloads.
- Verhaal 19 en lessen 6 en 14: gratis in Blender naar betaald mediaan 0,18% (±1 op 550); BashSupport Pro 4,3%; AutoCam hernoemd naar "Free" en Pro bovenaan de oude gratis video.
- Verhaal 22 (Garmin): betaalde broertje ±een tiende van de gratis; gratis met link naar betaald 14 van 30 op 100+, zonder link 0 van 12.
- Besluiten: geen knop of koopregel naar Pro in Blender, alleen het veld Website; geen beloning voor verlanglijst of volgen; Fest Hat alleen in de festdagen en voor kopers.

Hieronder gaat het verder waar dat ophoudt: wat er per winkel echt mag, twee blokkades die nog niemand zag, en de cijfers van mail en Discord.

---

## 0. Twee blokkades die de plannen van D en E raken (GEZIEN)

1. **Gumroad laat ons nog geen mail sturen.** In de hulp bij Emails en bij Workflows staat: "You cannot send emails until you've earned $100 after fees and received a payout." (https://gumroad.com/help/article/169-how-to-send-an-update , https://gumroad.com/help/article/131-using-workflows-to-send-automated-updates). Wij hebben 0 verkopen. E stap 6 (Gumroad-mail) werkt dus pas na ±10 verkopen van Pro Personal ($12 min kosten, GOK op de kosten). Gumroad verzamelt wel adressen: de lijst staat onder Emails > Subscribers.
2. **dortus.com blokkeert een ingebouwd aanmeldformulier.** De pagina heeft in de kop `form-action 'self'` en `connect-src 'self' https://analytics.amami.dev` (GEZIEN, curl op dortus.com). Een formulier dat naar Kit post, wordt door de browser tegengehouden. Oplossing: Kit-domein toevoegen aan `form-action` in de repo `dortus`, of linken naar een Kit-landingspagina (gratis, onbeperkt). Het precieze Kit-domein voor formulieren heb ik niet kunnen lezen (kit.com weigert curl; GOK: `app.kit.com`).

En een derde punt dat Thijs moet beslissen:
3. **Elke mail moet een postadres hebben.** Kit: "The CAN-SPAM Act requires a valid physical postal address in every email you send, even if you work from home." (GEZIEN, https://intercom.help/convertkit/en/articles/2502494-alternatives-for-your-physical-address , 17 jul 2026). Dat adres ziet iedereen op de lijst. Het woonadres van Thijs mag daar niet staan zonder zijn keus, en nooit in de repo. Thijs kiest één keer welk adres (zakelijk adres of postbus; de prijs van een postbus heb ik niet nagekeken). Discord heeft dit probleem niet.

---

## 1. Wat werkt aantoonbaar

### Mail
| Wat | Getal | Label en bron |
|---|---|---|
| Eén mail van Failbetter (Fallen London) aan een lijst van "hundreds of thousands" | **±1.200 verlanglijsten**, open 26%, klik 2%, afmelden 0,6% | DERDEN, https://howtomarketagame.com/2022/06/28/using-mailing-lists-to-gain-thousands-of-wishlists/ |
| Normaal voor een goede lijst (Zukowski) | open 15 tot 30%, klik 1 tot 15%; spamvlag bij ±3% afmelden | DERDEN, zelfde bron |
| Mail tegen tweet | "people are 10-times more likely to click on a link from a trusted email than from a Tweet" | DERDEN, https://howtomarketagame.com/2017/11/29/email-marketing-101-how-to-actually-use-your-mailing-list/ |
| Aanmelden voor "news and updates" | "Very very few people"; een klein cadeautje erbij geeft "greatly increase signups"; één mail = één knop | DERDEN, zelfde bron |
| Gratis product op Gumroad als lijst | 1.000 "customers" waren 528 unieke geldige adressen; fooien 3,5 cent per gratis download | DERDEN, https://dev.to/themes_dev/i-have-1000-customers-on-gumroad-this-is-what-i-learned-2095 |
| Steam volgen van de maker (Creator Homepage) | volgers krijgen een mail als de maker een nieuw spel uitbrengt | GEZIEN, https://partner.steamgames.com/doc/store/creator_homepage |
| Volgknop in de winkelwagen (sinds mei 2025) | wie koopt, kan de maker volgen en krijgt mail bij nieuwe spellen | DERDEN, https://wnhub.io/news/stores-and-publishing/item-47906 |

### Discord
| Wat | Getal | Label en bron |
|---|---|---|
| Doorklik bij een bericht met @everyone | "about as half as good as the click-through rate on email" (eigen server en lijst van Zukowski) | DERDEN, https://howtomarketagame.com/2021/03/29/dont-worry-because-microsoft-might-buy-discord/ |
| Gevonden worden in Discord zelf (Server Discovery) | pas vanaf **1.000 leden** en **8 weken** oud, plus activiteitseisen | GEZIEN, Discord-hulp "Enabling Server Discovery" (17 nov 2026) |
| Core Defense (solo, $20.186 in week 1) | Discord gestart door de community van zijn vorige spel en gamesites te waarschuwen; spijt: vertalers niet via Discord, "I have no way of reaching most of them" | DERDEN, https://newsletter.gamediscover.co/p/case-study-making-core-defense-a |
| White Knuckle | Discord-onboarding vraagt "tell us how you found the game": gratis meting van de bron | DERDEN, https://www.pushtotalk.gg/p/how-to-get-your-first-1000-players |
| Sabito (Instagram 50.000) | paginadag aangekondigd via Instagram, Discord (3.000) en wat Reddit | DERDEN, https://howtomarketagame.com/2023/09/11/three-inspiring-marketing-success-stories/ |

**Wat ik eruit haal:** Discord brengt geen nieuwe mensen (Discovery pas bij 1.000 leden) en klikt half zo goed als mail. Het is een plek om mensen vast te houden en te horen, niet om ze te vinden. Mail is het sterkere kanaal, maar alleen met een concrete reden om je aan te melden.

### Doorverwijzen van het ene product naar het andere
| Wat | Getal | Label en bron |
|---|---|---|
| Gamblers Table | grote verlanglijstknop in het spel naar de Steampagina; werkte zelfs in gestolen kopieën op andere sites; 10.000 verlanglijsten in 18 dagen (vooral itch en YouTubers) | DERDEN, https://greenpixels.itch.io/gamblers-table/devlog/945763/wishlists-0-to-10000-in-just-three-weeks- |
| Mega Jump naar Mega Run (mobiel, 2012) | 45,1% klik, 9,9% installatie | DERDEN, https://gamedeveloper.com/business/gdc-china-how-cross-promotion-for-mobile-titles-can-hit-big |
| Garmin: gratis broertje met link naar betaald | 47% tegen 0% op 100+ | GEZIEN, verhaal 22 |
| Blender gratis naar betaald | ±1 op 550 | GEZIEN, verhaal 19 |

**Eerlijk over Mega Jump:** zelfde reeks, zelfde toestel, 10 miljoen spelers. Hat Tower naar Hats is een ander toestel (horloge naar pc) en Hat Tower heeft 10 downloads. Reken daar niet mee.

### Onze stand (GEZIEN 18 nov)
- dortus.com: geen aanmeldvak, geen Discordlink; de Click Joints-pagina linkt naar Gumroad Pro, de Bison & Flex-pagina naar de Marketplace.
- Geen maillijst, geen Discord, TikTok 1 volger (bord), Hat Tower 10 downloads (A), Bison & Flex 6 downloads (nulmeting).
- Bison & Flex heeft al een Pro-melding in de IDE (`ProMelding.kt`) en meldt de bestandstypen `.y .yy .l .ll` aan (`plugin.xml`).

---

## 2. Wat mag per winkel (GEZIEN, met de regel erbij)

| Plek | In het product | Op de winkelpagina | Bron |
|---|---|---|---|
| **Steam** | Knop die de Steampagina in de overlay opent: `ActivateGameOverlayToStore(appid, ...)`. Vragen om te wishlisten mag, belonen niet (besluit, Bongo Cat). | **Geen links naar websites** in tekst of beelden, ook geen "implied URLs". **Geen andere producten** in de beschrijving, "including text, images, links, or widgets"; wel in de secties DLC en "More From", en via de vaste linkvelden voor site en sociale media. Volgers van de Creator Homepage krijgen mail bij een nieuw spel. | https://partner.steamgames.com/doc/store/page/description ; https://partner.steamgames.com/doc/api/ISteamFriends ; creator_homepage |
| **extensions.blender.org** (Click Joints Free) | (6.1) geen links naar winkels of donaties, geen knoppen of tekst om iets te kopen in de Blender-UI. (6.3) geen UI om updates, betaalde versies of andere extensies te promoten. | (6.1) link naar "external funding platforms" mag in de beschrijving. (6.2) tekst en beelden alleen over wat de gratis versie kan; Pro-functies tonen telt als reclame. Laatst bijgewerkt 10 aug 2026. Ons besluit (alleen het veld Website) blijft dus goed. | https://extensions.blender.org/terms-of-service/ |
| **Click Joints Pro** (Gumroad, Superhive) | De regels 6.x gelden voor wat op extensions.blender.org staat; Pro staat daar niet. Een knop "Get updates" of "Discord" in het Pro-paneel valt er dus niet onder (GOK: regels van Superhive voor knoppen niet nagelezen). | Gumroad: **upsell bij het afrekenen**: een extra product, een vervanging, of een betere versie, eventueel met korting; verschijnt na "Pay". Mail en workflows: pas na $100 (zie 0). | https://gumroad.com/help/article/331-creating-upsells |
| **JetBrains Marketplace** (Bison & Flex) | Persoonsgegevens of statistiek alleen met uitdrukkelijke toestemming (2.2d) en dan een privacybeleid (3.4): dus **geen mailveld in de IDE**. Geen inhoud "for additional promotion that would give it an unfair advantage" (2.2f). | Externe links moeten over de plugin **of de maker** gaan (1.7b): links naar dortus.com en onze andere producten mogen. Geen reclame op schermafbeeldingen (1.6d). JetBrains toont plugins zelf in de IDE op grond van bestandstypen die de plugin aanmeldt. | https://plugins.jetbrains.com/docs/marketplace/jetbrains-marketplace-approval-guidelines.html |
| **Garmin Connect IQ** (Hat Tower) | `Communications.openWebPage(url, ...)`: het horloge stuurt een melding naar de telefoon, die de gebruiker moet accepteren; dan opent de pagina in de browser. Alleen met Bluetooth-verbinding, en de app heeft de permissie **Communications** nodig (nieuwe permissie = update en keuring). | Link in de winkeltekst komt voor (verhaal 22). De officiële keuringsregels laden met JavaScript en kon ik niet lezen: GOK of een link naar een Steamspel daar mag. | https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications.html |
| **Kit** (de maillijst) | | Gratis tot 10.000 abonnees: onbeperkt formulieren, landingspagina's en verzendingen, **1 automatisering met 1 reeks**, A/B-test. "Recommendations" (andere makers aanbevelen) staat aan, kan uit. Betaald vanaf $39 per maand. API v4: `POST /v4/broadcasts` met `send_at: null` maakt een **concept**. | https://intercom.help/convertkit/en/articles/9053602-the-kit-newsletter-plan ; https://developers.kit.com/api-reference/broadcasts/create-a-broadcast |

---

## 3. Per product: de 3 acties met de meeste kans

### Hats of the Fallen (hoofdzaak)
1. **Eén lijst bij Kit, met een reden om je aan te melden, vóór de paginadag.** D actie 1 blijft staan (`dortus.com/hats`, aanmeldvak plus Discord). Mijn aanvulling: de lijst bij Kit, niet bij Gumroad (zie 0.1); de CSP van dortus.com aanpassen of naar een Kit-landingspagina linken (0.2); de tekst niet "news and updates" maar één belofte: "One email when the free demo is playable. Plus a Gloop desktop wallpaper." (wallpaper uit de Blender-renders: echt beeld, geen hoed, zodat het besluit over de Fest Hat heel blijft). Elke latere mail één knop. **Waarom:** mail klikt 10 keer beter dan een tweet en ±2 keer beter dan Discord; een cadeautje geeft meer aanmeldingen (DERDEN, Zukowski). **Verwachting (GOK):** 100 tot 300 aanmeldingen voor 4 jan bij 2 tot 28% klik geeft 2 tot 80 verlanglijsten per mail. Klein, maar het enige kanaal waar wij zelf de knop hebben.
2. **In de demo (4 jan): een verlanglijstknop en een Discordknop op het titelscherm en na elke ronde.** Knop roept `ActivateGameOverlayToStore(<appid Hats>, k_EOverlayToStoreFlag_None)` aan; tekst "Wishlist Hats of the Fallen", geen beloning. De Discord-onboarding stelt als eerste vraag "How did you find Hats?" (White Knuckle). **Waarom:** Gamblers Table kreeg zo zelfs verlanglijsten uit gestolen kopieën; Core Defense had spijt dat hij spelers niet via Discord liep. Olaf bouwt het; Thijs hoeft niets. Daarnaast op de paginadag de **Creator Homepage "Dortus"** koppelen (een paar klikken in Steamworks): volgers krijgen vanzelf mail bij ons volgende spel.
3. **Hat Tower wijst naar `dortus.com/hats`, niet naar Steam.** Eén regel in de Garmin-winkeltekst ("Gloop's big adventure: Hats of the Fallen, coming to Steam: dortus.com/hats") en op het eindscherm een keuze "Hats on Steam" die `openWebPage("https://dortus.com/hats", {"utm_source"=>"hattower"}, null)` aanroept. Omdat de bestemming `dortus.com/hats` is, verwijst het niet naar niets (de zorg in `gloop-winkel-voorstel.md`) en kan het mee in de update met extra horloges die A vóór ±1 dec aanraadt. **Waarom:** kost één keer code en dan niets; het broertje met link doet het beter dan zonder (verhaal 22). **Verwachting eerlijk (GOK):** bij 10 tot 100 downloads een handvol bezoekers. Doe het omdat het goedkoop is, niet omdat het groot wordt.

### Click Joints Free en Pro
1. **Free-gebruikers een reden geven om zich aan te melden, buiten Blender.** Het veld Website wijst al naar `dortus.com/click-joints/`. Zet daar één Kit-formulier met tag `click-joints`: "Email me when Pro 1.1 Rig to Figure is out" (één concrete belofte). De Gumroad-versie $0+ (taak van Chris) vraagt ook om een adres; die lijst kan pas mailen na $100 (0.1), dus ook daar een link naar het Kit-formulier in de downloadtekst. **Waarom:** in Blender mag niets (6.1 tot 6.3); de site is de enige plek waar Free-gebruikers ons nog zien.
2. **Upsell bij het afrekenen op Gumroad.** Bij Pro Personal ($12) de Studio-versie ($45) aanbieden; bij Free $0+ Pro Personal met een kleine korting. **Waarom:** Gumroad biedt het aan na "Pay" (GEZIEN), kost niets, en hoofdles 1 zegt dat meer prijzen helpt. GOK: of de upsell ook verschijnt bij een bestelling van $0; eerst testen met een kortingscode van 100% (zo test Gumroad zelf workflows). Samen met A's Superhive "Upgrade Variant".
3. **In Pro zelf een knop "What's new / Get updates" naar het Kit-formulier, en Pro 1.1 aankondigen aan kopers.** Pro staat niet op extensions.blender.org, dus 6.x geldt niet (GOK voor Superhive). Zodra de $100 binnen is, gaat de aankondiging van 1.1 ook als Gumroad-mail naar alle Pro-kopers, met één vraag om een review. **Waarom:** les 14: het tweede product (of de grote update) verkoopt aan de kopers van het eerste.

### Bison & Flex
1. **Controleren dat JetBrains hem zelf aanbiedt bij `.y` en `.l`.** De bestandstypen staan in `plugin.xml`; JetBrains toont plugins in de IDE op grond van zulke kenmerken (GEZIEN, richtlijnen). Eén keer testen in een schone IDE: een `.y`-bestand openen en kijken of de suggestie komt. Dat is de enige doorverwijzing die vanzelf mensen brengt.
2. **Op `dortus.com/bison-flex/` hetzelfde Kit-formulier (tag `jetbrains`), niet in de IDE.** Een mailveld in de IDE vraagt toestemming en een privacybeleid (2.2d, 3.4). De bestaande Pro-melding niet uitbreiden met reclame.
3. **Geen doorverwijzing naar "volgende plugins" bouwen.** Er is geen tweede JetBrains-plugin en de koers is "geen nieuw product". Met 6 downloads is een eigen lijst hier ±0 (GOK). Komt er ooit een tweede plugin, dan één regel "More from Dortus" in de beschrijving (mag volgens 1.7b).

### Garmin (kort)
Hat Tower: zie Hats actie 3. Ebb en Ebb Calm zijn geparkeerd; alleen als iemand de tekst toch aanraakt, één regel in Ebb Calm naar Ebb (verhaal 22).

---

## 4. Wat te automatiseren is

| Wat | Hoe | Kosten | Wat Thijs één keer doet |
|---|---|---|---|
| Aanmelden en welkom | Kit-formulier of -landingspagina; dubbele bevestiging; 1 automatisering (gratis plan) stuurt de welkomstmail met de wallpaper | € 0 tot 10.000 abonnees | Kit-account maken, postadres kiezen (0.3), welkomsttekst één keer goedkeuren, API-sleutel als GitHub-secret |
| Mail klaarzetten | Workflow op elke uitgavetag (E stap 1) maakt via `POST /v4/broadcasts` met `send_at: null` een **concept** in Kit met de tekst uit `update-tekst` | € 0 | per mail: lezen en op verzenden drukken (of ja zeggen tegen de hoofdchat). Agents versturen nooit zelf. |
| Tellen | dagelijkse workflow: aantal abonnees uit de Kit-API (GOK op de precieze route) en Discordleden via `discord.com/api/v9/invites/<code>?with_counts=true` (werkt zonder sleutel, gebruikt in verhalen-groei) naar het scorebord | € 0 | niets |
| Bron meten | elke link met `utm_source` (hattower, blender, gumroad, demo, discord); dortus.com heeft al analytics via amami.dev (GEZIEN in de CSP; GOK of die UTM toont) | € 0 | niets |
| Discord | één server "Dortus" met een kanaal per product; Onboarding-vraag "hoe vond je ons"; webhook zet changelogs die al openbaar zijn in #updates (D A3 voor Steam). Nieuwe tekst onder onze naam blijft concept. | € 0 | server maken met zijn account, webhook-URL als GitHub-secret |
| Knoppen in producten | Steam-overlay (Hats), `openWebPage` (Hat Tower), link in Pro-paneel: gewone code, gaat mee met de keuring | € 0 | niets |
| Gumroad-mail en workflows | trigger "New subscriber" of "Purchase", filter "Has bought" / "Has not yet bought" | € 0 | pas na $100 en een uitbetaling; dan teksten één keer goedkeuren |

**Volgorde:** eerst Kit plus het formulier op `dortus.com/hats` (hangt aan 0.3), dan dezelfde lijst met tags op de Click Joints- en Bison & Flex-pagina, dan de knoppen in de producten. Discord pas openen als er iets te spelen of te zien is (demo of paginadag), niet eerder: een lege server ziet er dood uit.

---

## 5. Wat niet werkt of te duur is

- **Gumroad als maillijst nu:** geblokkeerd tot $100 plus uitbetaling (GEZIEN).
- **Discord als groeikanaal:** Discovery pas bij 1.000 leden en 8 weken; @everyone klikt half zo goed als mail. Geen aparte servers voor Click Joints of Bison & Flex.
- **Een formulier "news and updates" zonder belofte:** "very very few" melden zich aan (Zukowski).
- **Hat Tower, Click Joints of een link noemen op de Steampagina van Hats:** verboden (geen links, geen andere producten); alleen "More From" en de Creator Homepage.
- **Pro noemen of tonen op extensions.blender.org of in de gratis add-on:** regels 6.1 tot 6.3; kan Click Joints Free uit de winkel laten halen.
- **Een mailveld in de JetBrains-plugin of de horloge-app:** toestemming en privacybeleid nodig, voor een publiek van 6 en 10.
- **Rekenen met Mega Jump-cijfers voor Hat Tower naar Hats:** ander toestel, 10 downloads.
- **Beloning voor verlanglijst, volgen of review** (Valve, besluit) en een hoed als cadeau voor aanmelden (botst met het besluit over de Fest Hat).
- **Betaalde mailtools:** Kit betaald vanaf $39 per maand, Buttondown automatiseringen +$29 per maand (E). Niet nodig onder 10.000 adressen.
- **Het woonadres van Thijs onderaan elke mail:** niet doen zonder zijn keus; dat is de eerste vraag aan hem.

---

## Bronnen (alle met curl gelezen op 18 nov 2026, tenzij anders vermeld)
- Gumroad Emails: https://gumroad.com/help/article/169-how-to-send-an-update ; Workflows: https://gumroad.com/help/article/131-using-workflows-to-send-automated-updates ; Upsells: https://gumroad.com/help/article/331-creating-upsells
- Kit Newsletter-plan: https://intercom.help/convertkit/en/articles/9053602-the-kit-newsletter-plan ; postadres: https://intercom.help/convertkit/en/articles/2502494-alternatives-for-your-physical-address ; API: https://developers.kit.com/api-reference/broadcasts/create-a-broadcast
- Steam beschrijvingsregels: https://partner.steamgames.com/doc/store/page/description ; Creator Homepage: https://partner.steamgames.com/doc/store/creator_homepage ; overlay: https://partner.steamgames.com/doc/api/ISteamFriends ; volgknop in winkelwagen: https://wnhub.io/news/stores-and-publishing/item-47906
- Blender: https://extensions.blender.org/terms-of-service/
- JetBrains: https://plugins.jetbrains.com/docs/marketplace/jetbrains-marketplace-approval-guidelines.html
- Garmin: https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications.html
- Discord Discovery: support.discord.com, artikel 360030843331 (via de openbare hulp-API)
- Zukowski: https://howtomarketagame.com/2022/06/28/using-mailing-lists-to-gain-thousands-of-wishlists/ ; https://howtomarketagame.com/2017/11/29/email-marketing-101-how-to-actually-use-your-mailing-list/ ; https://howtomarketagame.com/2021/03/29/dont-worry-because-microsoft-might-buy-discord/ ; https://howtomarketagame.com/2023/09/11/three-inspiring-marketing-success-stories/
- Core Defense: https://newsletter.gamediscover.co/p/case-study-making-core-defense-a ; White Knuckle: https://www.pushtotalk.gg/p/how-to-get-your-first-1000-players ; Gamblers Table: https://greenpixels.itch.io/gamblers-table/devlog/945763/wishlists-0-to-10000-in-just-three-weeks- ; Mega Jump: https://gamedeveloper.com/business/gdc-china-how-cross-promotion-for-mobile-titles-can-hit-big ; Gumroad gratis producten: https://dev.to/themes_dev/i-have-1000-customers-on-gumroad-this-is-what-i-learned-2095
- Onze repo: `producten/jetbrains-bison-flex/src/main/resources/META-INF/plugin.xml`, `producten/blender-gewrichten/click_joints/blender_manifest.toml`, `platformen/garmin/gloop-winkel-voorstel.md`, dortus.com (CSP, curl).

Niet gelezen: de keuringsregels van Garmin (laden met JavaScript), de regels van Superhive voor knoppen in een betaalde add-on, de exacte formulierroute van Kit (kit.com weigert curl), en Mike Rose over Discord (mcvuk.com gaf alleen de omlijsting).
