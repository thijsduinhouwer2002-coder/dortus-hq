# TikTok Shop (EU App Store): status

- **Stand 9 nov 21:12 UTC:** product **Klopt** (werknaam), TikTok Shop-uitbetalingen per bestelling naar Moneybird, daarna Fatture in Cloud (IT). Nog niets live. Installs 0, klanten 0, omzet 0.
- **Eerste euro (10 nov 00:15 NL):** niet eerder dan 4 tot 8 weken na de KvK plus de tijd tot de eerste betalende verkoper (GOK). Snellere variant zonder TikTok-registratie (upload van de export naar Moneybird) bekeken en afgeraden: geen echt voorbeeldbestand, geen kanaal, zwakker dan Schakel. Zie `onderzoek/2026-11-10-eerste-euro.md`.
- **Besluiten:** platform ja (Hans 8 nov, cijfer 7, voorstel Noor). Product ja (Hans 9 nov 20:44). Daan `Akkoord: ja` op het ontwerp 9 nov 21:05 UTC, behalve scherm 3 (rekeningen en btw, schets volgt); geen akkoord voor indienen.
- **Gebouwd (Jet):** basis TikTok-API, rekenkern, Moneybird-kant, product-laag deel 1 en 2a, op main, 56 tests groen in de product-laag, controleurs akkoord. Volgende: product-laag 2b, D1, daarna het betaalstuk.
- **Website (9 nov 22:25 UTC):** dortus.com/klopt/ met productpagina, prijs (`/klopt/prijs`, pricing URL voor de listing) en privacy (`/klopt/privacy`), alles als "in ontwikkeling". Wachtlijst via mail naar thijs@dortus.com (aantal mails is een eerste maat voor vraag).
- **Betalen:** Polar (bestaand account), €15 per maand per winkel (werkprijs tot Chris), gratis proef en grens zonder kassa, in TikTok label Paid plan. Zie `plan-betalen.md`.
- **Markt:** IT meer dan 21.000 actieve verkopers (DERDEN, apr en okt 2026), NL onbekend. EU-winkel 260 unieke apps tegen 721 in de VS (GEZIEN, 8 nov).
- **Rem:** registreren bij TikTok vraagt een KvK (na de verhuizing van Thijs). Een vroeg account zonder KvK staat op de lijst van Thijs (testwinkel zonder uitbetalingen). Na registratie 4 tot 8 weken keuringen tot live (GOK op schattingen van TikTok).
- **Team:** Tess leidt, Jet bouwt, allebei elk uur (Thijs 9 nov 19:00). Chris staat uit; prijs en verspreiding wachten op hem.
- **Stopregel (4b):** twee maanden geen groei van EU-apps en geen nieuwe landen, of TikTok verbiedt eigen kassa's: stoppen of veranderen. Product: minder dan 20 installaties in 6 weken na lancering.
- **Herhaalmeting platform:** rond 8 dec met `platformen/pionier/data/tiktokshop-apps-meet.py`, vergelijk met 8 nov.
