# Audio-plugins (VST3, AU, CLAP) via Plugin Boutique, Gumroad en eigen site (14 nov 2026, run 10:31)

**Advies: nee voor nu. Cijfer 3.** Er wordt betaald, maar vooral aan makers die al jaren bezig zijn; een nieuwe plugin verkoopt meestal tientallen stuks, er is een vloed aan AI-plugins en Google laat producers sinds okt 2026 zelf plugins maken. Bouwen kan wel goed vanaf Linux. Nagekeken door een controleur: akkoord, alle cijfers herrekend en 3 productpagina's live gelijk; 5 correcties verwerkt.

## Wat ik zelf mat (GEZIEN, 14 nov)
- **Plugin Boutique** (robots.txt staat lezen toe): sitemap met 9.534 producten van 395 merken. Productpagina's tonen geen verkopen, ratings of datum. Bereik en geld per plugin dus niet te meten. KVR geeft 403, niet omzeild.
- **Gumroad Discover**, open zoek-API, vijf zoektermen (vst plugin, vst3, audio plugin, clap plugin, au plugin): 2.385 producten, daarvan 512 echte plugins (presets, samples, NAM-captures en dergelijke eruit gefilterd op naam), 310 betaald van 120 makers. Let op: Discover toont alleen makers die al $100 omzet hebben, dus dit is de betere helft.
  - Betaalde plugins: mediaan 1 rating, 148 van 310 (48%) nul, 46 (15%) 5+, 17 (5%) 10+, geen enkele 50+. Prijs mediaan $15.
  - Filter precies: naam bevat vst, plug-in, plugin, clap, au of aax (clap en au met woordgrens) en niet preset(s), sample(s), kit, capture, nam, bank, loop, ir, impulse, tutorial, course, patch, skin, template, ebook, guide, sound pack, drum, wav, soundbank, serum, vital, omnisphere, kontakt (nam en ir met woordgrens).
  - Vervuiling (controleur): ±24 van de 310 zijn geen audio-plugin (13 Resolume, 3 Premiere, 2 DaVinci Resolve, Stream Deck, Roblox, SketchUp, cursussen, waaronder de hoogste met 47 ratings: PFM::SimpleEQ Videos & Plugin, een videocursus van $1), plus 42 modelpakketten voor Proteus van één maker. **Opgeschoond: 244 betaalde plugins van 107 makers, mediaan 1 rating, 121 nul (50%), 40 5+ (16%), 14 10+ (6%), prijs mediaan $16.** Conclusie gelijk.
  - Beste echte betaalde: UChord VST 37 ratings ($25), Bloomer 27 ($19), StompTones amp-sims 13 tot 21 ($5).
  - Met de eerder gemeten verhouding op Gumroad (±1 rating per 19 verkopen, zie voorstellen/gumroad-discover.md, GOK dat die hier ook geldt): mediaan ±20 verkopen ooit, de top ±700 verkopen ooit (±$17.000 bij $25). Geen datums in de API, dus dit is de hele voorraad, niet alleen nieuwe plugins.
- Data: `data/audio-plugins-gumroad-2026-11-14.json`, script `data/audio-plugins-gumroad-haal-script.py`.

## Van derden (onderzoeker, met bronnen)
- Enquête Moonbase 2025 onder 95 zelfgekozen onafhankelijke pluginbedrijven: 53% werkt alleen, 49% haalt minder dan $20.000 per jaar, 30% meer dan $100.000; 71% van de groten ziet prijzen dalen. moonbase.sh/reports/state-of-audio-plugin-companies-2025 (DERDEN, door onderzoeker gelezen).
- Wederverkopers (Plugin Boutique, ADSR): maker houdt ±60 tot 70%, meeste eerste aanmeldingen afgewezen, eisen genotariseerde Mac-versie, AU, demo en video's. DERDEN, forum.hise.audio/topic/12392 (apr 2025) en audiotechhub.com (mei 2026, reclame voor een cursus).
- Een maker met maanden werk: site, sociale media en KVR leverden "vrijwel niets" op (DERDEN, hise-forum, apr 2025).
- AI: Attack Magazine (15 okt 2026) noemt vibe-coded plugins "plugin slop", kopers wantrouwen ze. Google Flow Music laat sinds 7 okt 2026 producers met gewone taal instrumenten en effecten als VST3/AU maken (DERDEN, synthtopia.com). Simpele effecten verliezen daardoor snel waarde.
- Vindbaarheid: YouTube-reviewers (de goede doen het niet voor een gratis exemplaar), deals-nieuwsbrieven van winkels, e-maillijsten. Tarieven niet gevonden.

## Past het bij ons
- Bouwen: ja. JUCE (gratis tot $20.000 omzet, daarna $40 per maand of $800 eenmalig tot $300.000), VST3-SDK nu MIT, nih-plug (Rust) voor VST3 en CLAP vanaf Linux. Pamplejuce bouwt, test (pluginval) en ondertekent via GitHub Actions. clap-validator voor CLAP.
- Maar: Mac-notarisatie vraagt een Apple Developer-account ($99 per jaar, Thijs), Windows-ondertekening via Azure $9,99 per maand. Luisteren of het goed klinkt kan geen Claude; dat is de kern van het product.

## Waarom nee
1. Geld per nieuwe plugin klein: ook in de betere helft van Gumroad mediaan ±20 verkopen ooit.
2. Bereik hangt aan YouTubers en winkelnieuwsbrieven, niet aan een winkel met een "nieuw"-lijst; niet te meten en niet te kopen met kleine bedragen.
3. Openlijk AI-gemaakt is hier een nadeel, en Google maakt simpele plugins gratis.
4. Kosten vooraf (Apple, Azure) en we kunnen het product niet zelf beluisteren.

## Wat het zou veranderen
Een winkel met openbare verkopen of ratings per plugin en een lijst voor nieuwe plugins (bijvoorbeeld als KVR leesbaar wordt), of een soort plugin die niet om klank draait (MIDI-gereedschap zoals UChord en GridFather doet het relatief goed: kan Dortus beoordelen zonder te luisteren). MIDI-plugins zijn een mogelijk vervolg als productkans. Geen herhaalmeting gepland.
