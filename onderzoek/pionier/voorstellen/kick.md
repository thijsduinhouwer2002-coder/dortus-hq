# Kick (streamingplatform), tools van derden via de openbare API

Onderzocht 8 nov 2026 door Noor (pionier). Onderzoeker: één agent (groei, API, geld, vraag, leiders). Zelf nagekeken: het Q3 2026-rapport van Streams Charts en de FAQ van de Kick-API over geverifieerde apps.

**Cijfer: 3. Advies: nee voor nu.** Kick groeit het hardst van alle grote streamingplatformen, maar er is geen winkel, geen extensies in het kanaal en geen betaalroute van Kick. Een tool voor Kick is een gewoon SaaS-product dat zelf klanten moet werven, en de brede categorie (chatbot, alerts) heeft al een sterke nummer één.

## De vijf vragen

**1. Groeit het platform hard? Ja.**
- Q3 2026: 2,04 miljard uur gekeken, +30,7% op Q2; Twitch +4% naar 4,51 miljard; Twitch nu ±2,2 keer Kick (was ±2,8 keer in Q2); aandeel Kick 6,4% (GEZIEN, https://streamscharts.com/news/q3-2026-global-livestreaming-landscape).
- Q1 2025: 863 miljoen uur; Q2 2025: 1,1 miljard (DERDEN, https://streamscharts.com/news/q1-2025-global-livestreaming en https://streamscharts.com/news/q2-2025-global-livestreaming-landscape). Dus ruwweg een verdubbeling in anderhalf jaar.
- Kanttekening: Streams Charts meldt "unusual audience patterns" bij de grootste streamer; een deel kan nepkijkers zijn (DERDEN via agent).

**2. Is de winkel jong? Er is geen winkel.**
- Openbare API sinds maart 2025, met chat, moderatie, kanaalpunten en inwisselingen (sinds jan 2026), KICKs (fooien), webhooks (DERDEN, https://www.tubefilter.com/2025/03/07/kick-launches-api-developer-fund-third-party-streamer-tools/ en https://docs.kick.com/llms.txt).
- Geen app-directory, geen extensies in het kanaal. Alleen "App Verification": een badge op het botaccount en hogere limieten (GEZIEN, https://docs.kick.com/apis/faqs.md).
- Laatste wijziging in de changelog 11 aug 2026; het tempo van het platform voor ontwikkelaars is laag (DERDEN via agent, https://docs.kick.com/changelog.md).

**3. Kan er betaald worden? Alleen buiten Kick om.**
- Het fonds van $100.000 was een eenmalige wedstrijd (maart tot mei 2025), geen aanwijzing dat het in 2026 nog loopt (DERDEN, Tubefilter; GOK voor 2026).
- Tools rekenen zelf af. KickBot vraagt $9,99 per maand voor premium (DERDEN via agent, https://kickbot.com/).
- Geen plan van Kick voor betaalde apps gevonden.

**4. Is er vraag? Weinig gemeten.**
- Sound Alerts ondersteunt Kick niet; het verzoek had in maart 2026 één stem (DERDEN, https://feedback.soundalerts.com/p/kick-support-2). Streamer.bot-gebruikers vragen om Kick-extensies (DERDEN, https://extensions.streamer.bot/t/when-will-extensions-get-updates-for-kick/3354).
- Reddit niet doorzocht (geen bruikbare treffers). Zwakste punt van dit onderzoek.

**5. Is de eerste plek te pakken? In de brede categorie niet.**
- Chatbot, alerts, TTS en clips: KickBot zegt 150.000+ Kick-streamers te hebben, met de grootste namen (DERDEN, eigen claim, https://kickbot.com/). Daarnaast BotRix, StreamElements en Streamlabs met Kick-ondersteuning (DERDEN via agent).
- Smalle hoeken zonder duidelijke leider: geluidsalerts in de stijl van Sound Alerts, interactieve beloningen op de nieuwe inwisselingen-API, statistieken voor kleine streamers (GOK). Maar zonder winkel is "nummer één" niet zichtbaar en niet meetbaar.

## Risico
Kick hangt aan een paar grote streamers en aan de eigenaren (gokbedrijf Stake); beleid kan snel draaien, en een deel van de groei kan nep zijn. Teken dat het voor ons interessant wordt: Kick opent extensies in het kanaal of een app-directory met installs, of een betaalroute voor apps.

## Eerste productidee (alleen als dat verandert)
Geluidsalerts voor Kick met kanaalpunten: kijkers wisselen punten of KICKs in voor een geluid of klein filmpje op de stream, via de inwisselingen-webhook en een OBS-browserbron.

## Wat ik niet kon meten
Aantal streamers en apps, verdiensten van kleine tool-makers, vraag op Reddit, echtheid van de kijkcijfers.

## Advies
Nee voor nu (3). Hoort niet bij de pionier zolang er geen winkel of extensies zijn. Opnieuw kijken als Kick extensies of een app-directory aankondigt; de groei is wel een reden om dat in de gaten te houden (Streams Charts kwartaalrapport, eens per kwartaal).
