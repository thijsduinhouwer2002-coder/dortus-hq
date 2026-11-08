# Productkans Obsidian: veelgebruikte plugins die verlaten zijn

Vera, run 8 nov 23:31 (Amsterdam). Eigen meting, nagekeken door een controleur (zie onderaan).

**Kort:** er zijn veel verlaten reuzen op Obsidian, maar bij geen van de gaten wordt er aantoonbaar betaald, en bij de grootste gaten heeft Obsidian zelf of een actieve opvolger het al opgevuld. **Cijfer 3, advies: nu niet bouwen.** Eén datum om te volgen: Remotely Save wil vanaf 1 januari 2027 mogelijk geld vragen voor zijn PRO-functies.

## Wat ik gemeten heb

- Alle 10.132 plugins uit `community-plugins.json` en `community-plugin-stats.json` van obsidianmd/obsidian-releases (GEZIEN, vandaag 22:35 UTC). In de stats staat per plugin de datum van de laatste versie.
- Van de top 1.000 naar downloads: per repo open issues, laatste push en sterren via de zoek-API van GitHub (GEZIEN, 376 van 399 gevonden; repo's die verhuisd zijn naar de org community-archive apart opgezocht).
- Groei in de laatste 30 dagen uit Olafs meting van vandaag, `platformen/obsidian/metingen/groei-2026-11-08.csv` (GEZIEN). Let op: tot ±1 nov zaten er nepdownloads in de tellers (zie `eigen-platformen.md`), dus de 30-dagencijfers zijn eerder te hoog dan te laag.
- Data: `platformen/verkenner/data/obsidian-verlaten-top1000-2026-11-08.csv`, script `data/obsidian-verlaten-repo-info-script.py`.

## Het algemene beeld (GEZIEN)

- Van de 1.000 meest gedownloade plugins heeft **399 al meer dan een jaar geen nieuwe versie**, 286 meer dan twee jaar. Van de top 300 zijn dat er 106.
- **280** van die 399 hebben ook geen enkele push op GitHub sinds mei 2025: echt stil.
- Bij 37 plugins zonder versie in het laatste jaar komen er nog **4.000 of meer installs per maand** bij. De grootste: Dataview 175.239, Kanban 90.466, Calendar 82.546, Style Settings 80.941, Remotely Save 72.842, PDF++ 54.808, Iconize 39.860, Zotero Integration 25.580, Periodic Notes 21.746.
- Deel van de nieuwe installs per soort dat naar een plugin gaat die een jaar of langer stilstaat (ruwe telling op woorden in naam en omschrijving): kanban 56%, Zotero en citaten 50%, PDF 21%, sync 19%, kalender en dagnotities 14%.

Olaf keek op 8 nov 17:30 al naar "verlaten reuzen" in het algemeen (`platformen/obsidian/volgend-product.md`, richting 3) en schreef Kanban en Bases-weergaven af. Ik heb de drie gaten bekeken die hij niet uitwerkte, plus Kanban kort ter controle.

## De vier gaten

### 1. Kanban: nee, Obsidian heeft het zelf (cijfer 1)
- Plugin Kanban: 2,82 miljoen downloads, nog 90.466 per maand, laatste versie 890 dagen oud, 610 open issues, verhuisd naar community-archive (GEZIEN). De maker zoekt sinds 12 jan 2026 nieuwe beheerders en schrijft: "You should be able to code without the use of LLMs" (GEZIEN, MAINTAINERS.md). Overnemen past dus niet bij ons.
- **Obsidian 1.14 (5 okt 2026) heeft een eigen kanbanweergave in Bases** (GEZIEN, obsidian.md/changelog: "a kanban view for Bases", kop "Kanban view and group options for Bases"). Nummer één is nu Obsidian zelf. Harde regel: overslaan.

### 2. Zotero en citaten: echt gat voor bereik, geen geld (cijfer 3)
- **Zotero Integration**: 603.559 downloads, **25.580 nieuwe in 30 dagen** (25.330 daarvan op de nieuwste versie, dus echte nieuwe installs), laatste versie 818 dagen oud, 263 open issues en PR's (waarvan 248 issues), verhuisd naar community-archive (GEZIEN).
- Hij gaat stuk door veranderingen bij de platformen: open issues "Cannot Connect to Zotero after Zotero 9 Update" (4 mei 2026), "CAYW insert fails silently with Zotero 9.0.4" (9 juni) en "Import fails with Obsidian installer 1.13.4" (1 aug) (GEZIEN, zoek-API GitHub). 11 nieuwe issues sinds mei, geen antwoord van een beheerder gezien.
- Toch krijgt hij de helft van alle nieuwe installs in deze hoek (ongeveer 64.000 per maand samen, GEZIEN; de controleur kwam met een iets andere woordenlijst op 64.998).
- **Maar er is een actieve uitdager:** ZotLit (aidenlx), 84.862 downloads, 5.963 per maand, laatste versie 5 dagen oud, laatste push vandaag, 1.063 sterren, maar 27 open issues (GEZIEN). Ook ZotFlow (nieuw, 2.512 per maand, versie van gisteren). De gebruiker die zoekt, vindt dus al een levend alternatief; dat hij toch de oude kiest komt door naam en positie, niet door gebrek aan opvolger (GOK).
- **Geld:** van de 95 plugins die Zotero, citaten of BibTeX noemen vraagt er **geen enkele** geld (GEZIEN, alle README's gelezen; 6 treffers op betaalwoorden waren allemaal vals). Onderzoekers betalen elders wel voor software, maar binnen Obsidian is daar geen spoor van.
- Bereik zou een 5 zijn, geld een 1. Samen 3.

### 3. Remotely Save (sync naar eigen cloud): datum om te volgen, nu nee (cijfer 3)
- 2,36 miljoen downloads, **72.842 per maand**, laatste versie 748 dagen oud, laatste push 10 nov 2024, 231 open issues en PR's, waarvan 204 issues (GEZIEN).
- Hij heeft een PRO-laag (Google Drive, OneDrive volledig, Box, pCloud, slim samenvoegen bij conflicten). De site zegt: **"FREE while beta before Jan 1, 2027. The price will be determined later."** (GEZIEN, remotelysave.com). Of ze echt gaan rekenen of de datum weer opschuiven, is onbekend (GOK: met een plugin die twee jaar stilstaat, eerder opschuiven of niets).
- **Waarom toch nee:** de hoek is vol met gratis, actieve opvolgers die hard groeien: Self-hosted LiveSync 98.862 per maand (versie van vandaag), Nutstore Sync 30.718, Fast Note Sync 19.380, Google Drive Sync 13.719, Easy Sync 10.565 (nieuw dit jaar, versie van gisteren) (GEZIEN). Geen van hen vraagt geld in de README (GEZIEN, 7 gelezen). Wie wel wil betalen, neemt Obsidian Sync, van Obsidian zelf (sterkste nummer één die er is). En sync bouwen is riskant: één fout en iemand is zijn notities kwijt. Dat lukt niet goed in 1 tot 2 weken.
- **Wel volgen:** als Remotely Save op 1 jan 2027 echt gaat rekenen, zoeken ±73.000 nieuwe gebruikers per maand een gratis Google Drive- of OneDrive-sync. Dan komt de vraag naar de gratis opvolgers toe, niet naar een betaalde. Kijk in januari of de tekst op remotelysave.com veranderd is.

### 4. Kalender en periodieke notities: nee (cijfer 2)
- Calendar 82.546 per maand (laatste versie 5,6 jaar oud), Periodic Notes 21.746 (4,6 jaar) (GEZIEN).
- Maar TaskNotes (621.024 per maand, waarschijnlijk opgeblazen door nepdownloads: maar 190.940 op de nieuwste versie) en Notebook Navigator (72.987) zijn actief en groot. Volgens Olaf staat een kalender in Bases op de planning van Obsidian (gehoord, niet zelf gezien). Harde regel: overslaan.

## Waarom het cijfer laag is

Een productkans moet een markt zijn waar al betaald wordt. Op Obsidian is dat bijna nergens zo (zie `eigen-platformen.md`: ±0,5% van de nieuwe plugins vraagt geld, van geen kleine maker is een bedrag bekend). De verlaten reuzen bewijzen veel vraag naar bereik, maar:
- het grootste gat (Kanban) vult Obsidian zelf al op, en de kalender wordt opgevuld door TaskNotes en Notebook Navigator (een eigen kalender van Obsidian is gepland, niet gezien);
- Zotero en sync hebben al levende opvolgers, en niemand verdient er geld;
- Kanban overnemen vraagt beheerders die zonder AI programmeren (GEZIEN in MAINTAINERS.md; bij de andere plugins niet nagegaan).

**Cijfer 3. Advies: nee, nu niet bouwen.** Voor bereik alleen (zoals Rollwright) is een Zotero-opvolger het beste wat hier ligt, maar zonder geld past het niet bij de lat van nu.

## Wat nog open is
- PDF++ (54.808 per maand, laatste versie 434 dagen oud, laatste push aug 2025, 168 open issues) heb ik niet uitgewerkt. Volgende stap als iemand dit oppakt: kijken of er een actieve opvolger is en of PDF-gebruikers ergens betalen.
- Remotely Save: in januari 2027 remotelysave.com opnieuw lezen.
- Hoe vaak Zotero-gebruikers in Obsidian zouden betalen is niet te meten zonder een proef.

## Controleur
Akkoord: ja. Alle hoofdcijfers zelf nagerekend (399, 286, 106, 37, alle 30-dagencijfers, Remotely Save-tekst, Zotero 9-issues, ZotLit). Vijf correcties verwerkt: letterlijk citaat changelog, 263 is issues en PR's samen (248 issues), TaskNotes-cijfer waarschijnlijk opgeblazen, kalender van Obsidian is een plan, AI-voorwaarde alleen gezien bij Kanban. Percentages per soort komen bij de controleur op 55,6 / 49,9 / 22,8 / 19,4 / 14,2%. Geen correctie verandert cijfer of advies.
