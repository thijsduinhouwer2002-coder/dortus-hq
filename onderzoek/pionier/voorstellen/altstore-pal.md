# Voorstel: AltStore PAL (alternatieve iPhone-winkel)

Noor, 9 nov 2026, run 12:40 UTC. Cijfer **3**, advies **nee**.

## Wat het is
AltStore PAL is een officiële alternatieve app-winkel voor de iPhone, mogelijk gemaakt door wetten die Apple dwingen andere winkels toe te laten: EU (DMA, sinds april 2024), Japan (MSCA, sinds 18 dec 2025) en Brazilië (sinds juni 2026). Makers zetten hun apps in een eigen "bron" (een JSON-bestand) en gebruikers voegen die bron toe. Apps moeten wel door Apple's notarisatie.

## De vijf vragen

1. **Groeit het platform hard en zichtbaar?** Nauwelijks te zien.
   - Het enige gebruikerscijfer is "meer dan 100.000 installaties" uit 2024 (DERDEN, https://alloforfait.fr/actualites/131224-altstore-pal-deja-plus-de-100-000-installations.html). Een recenter cijfer vonden ik en de controleur niet.
   - Wel een motor: nieuwe landen door wetgeving (Japan dec 2025, Brazilië juni 2026, VK gepland), $6 mln financiering in okt 2025 (DERDEN, https://daringfireball.net/linked/2025/10/07/altstore-state-of-the-union) en eerder een Epic MegaGrant.
   - De Patreon van de makers van AltStore zelf (Riley + Shane, ook voor de oude AltStore Classic en de emulator Delta) heeft 8.710 betalende leden en 90.591 volgers (GEZIEN, Patreon-API, vanity rileyshane). Dat is het grootste betalende publiek dat bij AltStore te zien is.
   - Het sociale deel (explore.alt.store, sinds maart 2026 in de app) is klein: 110 accounts, het hoofdaccount heeft 388 volgers (GEZIEN, API van explore.alt.store, door de controleur bevestigd).

2. **Is de winkel jong?** Ja en nee. In de EU 2,5 jaar open, in Japan 11 maanden, in Brazilië 5 maanden. Bronnen die zich vindbaar maakten op explore.alt.store, per maand (GEZIEN, `data/altstore-explore-meet.py`): aug 2025 5, okt 15, dec 11, jan tot sept 2026 2 tot 9 per maand, okt 2026 17, nov tot nu 5. Samen 102. Klein en licht stijgend, geen golf.

3. **Kan er betaald worden?** Ja, nu al. AltStore rekent 0%, Apple 5% Core Technology Commission (GEZIEN, https://faq.altstore.io/developers/fees.md). Betalen gaat via de ingebouwde Patreon-koppeling: een app alleen voor patrons, met de minimale pledge als maandprijs; stopt de pledge, dan werkt de app na 7 dagen niet meer (GEZIEN, https://faq.altstore.io/developers/patreon-integration.md). Makers hoeven niet in de EU, Japan of Brazilië te zitten (GEZIEN). Kosten vooraf: Apple Developer Program €99 per jaar, en Thijs moet de alternatieve voorwaarden van Apple accepteren en als handelaar (met openbaar adres) geregistreerd staan.

4. **Is er vraag?** De vraag is naar wat Apple in de App Store weigert: emulators (Delta), torrent (iTorrent), Stremio, klembordbeheer (Clip). Dat zijn apps waar de winkel om bestaat. Voor gewone hulpprogramma's is er geen reden om AltStore te gebruiken, want die staan ook in de App Store, waar elke iPhone-gebruiker al zit.

5. **Is de eerste plek te pakken?** In de sterke categorieën niet: emulators heeft AltStore zelf (Delta), torrent heeft iTorrent. Open hoeken zijn er vooral in grijs gebied (downloaders, systeemhacks), en daar wil Dortus niet zitten.

## Past het bij een 8 (herweger)?
- Nieuwe kleine makers verdienen: niet te meten; de Patreon-campagnes van nieuwe bronnen die ik probeerde (itorrent, cizzuk, fantinel) bestaan niet onder die naam (GEZIEN). Geen bewijs.
- Bereik voor nieuwkomers: ja binnen AltStore (weinig apps, collecties "Indie Gems"), maar het publiek is klein en moet eerst een omweg nemen om AltStore te installeren.
- Bouwen en testen: kan, met macOS-machines op GitHub Actions en de iOS-simulator, maar het is Swift en Xcode, niet ons gebruikelijke JavaScript.
- Thijs verkoopt binnen een week: waarschijnlijk wel (Apple-account, Patreon), met €99 per jaar.

## Risico
Het platform hangt aan wetgeving en aan Apple's regels voor alternatieve winkels; elke wijziging van Apple (kosten, notarisatie) raakt het meteen. Het teken dat het stokt: geen nieuwe landen in 2027 en het aantal bronnen blijft onder de 10 per maand.

## Advies
Nee. Betalen werkt en de winkel is in Japan en Brazilië jong, maar het publiek is klein en groeit niet zichtbaar, en de categorieën die er werken zijn juist de apps die Apple weigert: daar is de eerste plek bezet of grijs. Een gewone Dortus-app hoort dan in de App Store zelf, niet hier.

Opnieuw kijken als: AltStore een gebruikerscijfer boven de miljoen meldt, het VK of de VS opengaan, of Apple de notarisatie zo versoepelt dat er een eigen soort app ontstaat die alleen buiten de App Store kan. Herhaalmeting hooguit 9 feb 2027: `python3 -I data/altstore-explore-meet.py`.

Controle: een controleur (agent) bevestigde punten 1 tot 5 van de feiten (kosten, landen, Patreon, explore-tellers, 8.710 betalende leden) en vond geen recenter gebruikerscijfer.
