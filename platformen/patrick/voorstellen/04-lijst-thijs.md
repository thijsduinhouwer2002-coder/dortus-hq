Wat verandert: `organisatie/lijst-thijs.md` past op één scherm: alleen wat Thijs moet doen, in een vaste vorm. Afgehandelde en ter-info-punten gaan naar `organisatie/archief/lijst-thijs-2026-11.md` (het huidige bestand in zijn geheel, niets weg).
Waarom: het bestand is 82 KB met 61 doorgestreepte punten; van de ±15 open punten zijn er 2 echt voor nu. Bron: LangChain "Agent Inbox" (melden, vragen, nakijken in één inbox, bron 26); Hans' eigen besluit 9 nov 20:44 ("hooguit 15 minuten"). Eerste vulling op basis van de stand van 9 nov 23:05; de hoofdchat controleert.

---

# Lijst voor Thijs

Alleen wat jij moet doen. Hooguit 5 punten. Wat af is, gaat dezelfde dag naar `archief/lijst-thijs-<maand>.md`. Ter info staat op het dashboard, niet hier.

Vorm per punt (verplicht, hooguit 6 regels):
`- **<wat>** | <minuten> | <dringend: nu / deze week / pas na X> | van <naam>, <datum>`
`Waarom:` één zin, met wat het oplevert in geld of tijd.
`Stappen:` genummerd, met link.
`Klaar? Zeg in de projectchat:` "<zin>".

## Nu
- **Steamworks-account en Steam Direct ($100) starten** | 30 min | nu | van hoofdchat, 9 nov 23:05
Waarom: Valve doet 15 tot 30 dagen over bank, belasting en ID; hoe eerder je start, hoe eerder Het Hol kan verkopen. De $100 wordt verrekend na $1.000 omzet (GEZIEN, partner.steamgames.com/steamdirect).
Stappen: (1) https://partner.steamgames.com/steamdirect, "Sign up" met je Steam-account; (2) voorwaarden zelf lezen en accepteren; (3) $100 betalen; (4) bank, belasting en ID invullen.
Klaar? Zeg in de projectchat: "Steamworks gestart".

## Deze week
- **TikTok Partner Center-testaccount, zonder KvK** | 20 min | deze week | van Tess, 9 nov
Waarom: zo testen we de TikTok-koppeling van Klopt één keer echt voordat de KvK er is.
Stappen: zie `platformen/tiktok-shop/registratie.md` stap 1 tot 3; bij het bedrijfsformulier "Save for later"; app "Dortus Boekhouding test" (custom), redirect `https://dortus.com/tiktok-boekhouding/koppel`; testwinkel NL; App Key en Secret als repository secrets `TIKTOK_APP_KEY` en `TIKTOK_APP_SECRET`. Vraagt een stap om KvK: stop en zet de melding hier.
Klaar? Zeg in de projectchat: "TikTok testaccount staat".

## Pas na een mail (niets doen tot dan)
- **Bison & Flex zichtbaar maken** | 2 min | pas na goedkeuringsmail JetBrains | van Jet, 8 nov
Stappen: https://plugins.jetbrains.com/plugin/35901-bison--flex, Edit, "Hidden" uit.
Klaar? Zeg: "Bison & Flex zichtbaar".

- **Mail van extensions.blender.org over Click Joints** | 1 min | pas na de mail | van Bram, 8 nov
Stuur de mail door naar de projectchat; de ploeg doet de rest.

---
Let op voor de hoofdchat: `dashboard/bouw.py` (regel 113 tot 121) leest punten die beginnen met `- **` en raadt "ter info" met een lange zoekzin. Met deze vorm kan dat eenvoudiger en zekerder: `ter_info = "pas na" in r`. Het getal "wacht op Thijs" klopt dan altijd. Twee regels werk.
