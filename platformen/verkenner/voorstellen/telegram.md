# Telegram (bots en Mini Apps, betalen met Stars)

Vera, 7 nov 2026, run 17:32 (tweede helft). Zelf toegevoegd.

## Advies: nee voor nu, cijfer 4

Telegram is groot en het betalen is goed geregeld, maar ik kon het bereik van nieuwe bots niet zelf meten (geen lijst met nieuwe bots, cijfers pas boven 10.000), en ik vond geen enkele kleine maker van een hulpmiddel-bot die een controleerbaar maandbedrag in Stars noemt. Daarbij komt een nadeel dat de andere platforms niet hebben: een bot moet dag en nacht op een eigen server draaien, dus er zijn vaste kosten en onderhoud.

## Waarom gekozen
- Meer dan 1 miljard gebruikers per maand (DERDEN, https://www.theblock.co/post/348630/telegram-surpasses-1-billion-monthly-active-users, 2025).
- Betalen zit in de app: digitale goederen mogen alleen met Telegram Stars (DERDEN, https://telegram.org/tos/bot-developers artikel 6.2, gelezen 7 nov 2026).
- Op 6 nov leek Discord (cijfer 5) het beste geldsignaal; Telegram is het grotere broertje.

## Cijfers

### Geld
- De maker krijgt 0,013 dollar per Star (GEZIEN in de voorwaarden, artikel 6.2.4). Stars zijn pas na maximaal 21 dagen op te nemen, uitbetaling via Fragment in TON (GEZIEN, artikel 6.2.4 en 6.2.4.1).
- De koper betaalt ±0,02 dollar per Star, dus de maker houdt ±65% (DERDEN, https://dev.to/__747bb5a1521/i-built-a-paid-telegram-bot-heres-what-telegram-stars-actually-pay-3fo, mei 2026; percentage GOK op die prijs).
- Opnemen vanaf 1.000 Stars (±$13), Fragment eist identiteitscontrole sinds nov 2024 (DERDEN, dev.to hierboven en https://thearabianpost.com/fragment-now-mandates-kyc-for-blockchain-transactions/). TON moet zelf via een beurs naar euro's: extra stap en koersrisico.
- Abonnementen per 30 dagen in Stars kunnen (DERDEN, https://core.telegram.org/bots/api).
- Kleine makers met bedragen: **geen controleerbaar geval gevonden**. Het enige succesverhaal, GPT4Telegrambot (familie van drie, gestart jan 2023), zegt 5 tot 6 miljoen roebel per maand uit abonnementen te halen bij 8 miljoen maandgebruikers, maar heeft nu personeel en gaf $400.000 uit aan marketing; eigen woorden in een interview (DERDEN, https://incrussia.ru/understand/ii-na-million/, 13 apr 2026). Andere dev.to-verhalen (PolySignal, WhisprMe) noemen alleen prijzen, geen omzet.

### Bereik
- Telegram toont het aantal maandgebruikers van een bot pas boven de 10.000 (DERDEN, https://okhlopkov.com/en/articles/telegram-bot-trends-august-2026/).
- Op de openbare t.me-pagina staat dat cijfer wel, in het tweede blok `tgme_page_extra` (het eerste bevat alleen de @naam). Eerst las ik alleen het eerste blok en dacht ik dat het ontbrak; de controleur zag de fout. Hertest: BotFather 8.045.824, userinfobot 631.929; jsondumpbot, remindmebot en wallet tonen niets, dus die zitten onder 10.000 of tellen anders (GEZIEN). De controleur vond bij 11 van 12 bekende bots een cijfer (GEZIEN door controleur).
- Er is geen openbare lijst van nieuwe bots met startdatum. tapps.center (staat lezen toe) toont geen datum en geen gebruikers; findmini.app verbiedt ClaudeBot in robots.txt, dus niet gebruikt. Het kanaal t.me/trendingapps tipt vooral spelletjes (GEZIEN).
- Conclusie: mediaan en percentage 100+ voor nieuwe bots zijn **nu niet te meten**, omdat de lijst met nieuwe bots ontbreekt en alles onder 10.000 onzichtbaar is. Wel te volgen: elke bot boven 10.000, en later een eigen proefbot. Wat bekend is: ±15.000 bots hebben 10.000+ maandgebruikers; algemene AI-bots zakten 61% sinds hun piek in dec 2025; videodownloaders (27,9 miljoen over 66 bots) groeiden in augustus maar 3%, en maar 30 van de 66 groeiden (DERDEN, okhlopkov aug 2026). Tegenvoorbeeld van een kleine maker: SpeedTap had na twee weken 79 gebruikers en $0 aan Stars (DERDEN, https://www.printmoneylab.com/2026/04/mini-app-builder-episode-4-honest-numbers.html).
- Meer bron: okhlopkov meet elke maand de maandgebruikers van bots aan begin en eind van de maand (Russisch juli-rapport: https://habr.com/ru/articles/1066040/).

### Drukte
- In 2025 kwamen er 50 tot 100 nieuwe AI-concurrenten per dag bij (DERDEN, Inc-interview hierboven). BotFather groeide in 6 weken van 3,5 naar 5 miljoen maandgebruikers en staat nu op 8.045.824 (GEZIEN 7 nov): veel mensen maken nu bots, vaak met AI (DERDEN, https://okhlopkov.com/en-botfather-mau-43-percent-growth-telegram-ai/). Zeer druk.

### Vindbaarheid
- Vooral via zoeken in Telegram op de naam van de bot, en via doorsturen in chats (DERDEN, Inc). Dat zoeken wordt uitgebuit: 104 "doorway-bots" met samen 20,3 miljoen maandgebruikers sturen zoekverkeer door (DERDEN, okhlopkov aug 2026). Telegram Ads leverde weinig op, ingekochte video's beter (DERDEN, Inc).
- De Mini App Store in de app bestaat sinds juli 2024; geen cijfers over hoeveel verkeer die geeft.

### Past het bij ons
- Bouwen is makkelijk (Bot API, 1 tot 2 weken haalbaar).
- Maar: een bot draait op een eigen server die altijd aan moet staan (geld, dus Thijs, en storingen zonder iemand die opstaat), en de ploeg kan het niet in "de echte app" testen zoals bij Obsidian zonder een Telegram-account van Thijs.
- Betaald krijgen in TON via Fragment met identiteitscontrole; dat moet Thijs zelf doen.

## Voor en tegen
- Voor: enorm publiek, betalen ingebouwd, makers houden ±65%, smalle taakbots houden beter stand dan algemene AI-bots.
- Tegen: bereik nieuwe bots niet te meten, geen bewezen kleine maker met bedrag, zeer druk, zoeken wordt gespamd, servers en uitbetaling in crypto.

## Eerste idee (als het ooit ja wordt)
Een smalle taakbot die mensen opzoeken op naam, met een gratis deel en een abonnement in Stars. Geen algemene AI-chatbot (krimpt en is vol).

## Wat dit zou veranderen
- Twee kleine makers, gestart in 2025 of 2026, met een controleerbaar bedrag boven $300 per maand in Stars.
- Een bron met nieuwe bots en hun maandgebruikers over tijd (de maandrapporten van okhlopkov.com, robots.txt staat ClaudeBot toe), zodat te zien is hoeveel nieuwe bots de 10.000 halen.
- Of een proefbot van Dortus zelf, maar dat kost een server en dus een besluit van Thijs.

## Nagekeken
Controleur 7 nov: akkoord met nee voor nu en cijfer 4, 8 punten. Verwerkt: t.me toont het cijfer wel (tweede blok), BotFather nu ±8 miljoen, "groeien nog" afgezwakt, tegenvoorbeeld SpeedTap en de maandrapporten van okhlopkov als bron toegevoegd.
