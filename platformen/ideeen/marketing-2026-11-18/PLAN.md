# Plan distributie en marketing (hoofdchat, 18 nov 2026)

Bron: verslagen A tot en met J in deze map, gekeurd in `KEURING.md` (12 zware beweringen bij de bron nagekeken: 9 klopt, 3 klopt deels, 0 fout). Geldt tot de meting van wo 9 dec; dan bijstellen.

## Wat aantoonbaar werkt (en wat niet)
1. **De eerste 1.000 komen niet van eigen posts** (F: in alle 10 reizen). Recept: iets openbaars plus een verzamelplek, dan één moment op een plek met kijkers (fest, showcase, zoekbalk van de winkel), binnen 72 uur een tweede golf via één passende middelgrote maker, daarna maanden een post per versie en uitlegpagina's.
2. **Mail is veel sterker dan social:** Tiny Glade 28% doorklik uit mail tegen 1% uit social (D), één mail van Failbetter ±1.200 verlanglijsten (J). Maillijst wordt **Kit** (gratis tot 10.000); Gumroad mailt pas na $100 omzet (J, KLOPT).
3. **Zoekbalk en uitleg zijn de lange staart:** gevonden worden in de winkel (A) en tutorials (H: "Flex en Bison op Windows" 190.000 weergaven op Stack Overflow, geen video voor CLion).
4. **Een nieuwe versie geeft zelden een betere plek** (A, KEURING): bij JetBrains ±45 minuten bovenaan, bij Blender en Garmin niets. Wat een versie oplevert is de **post erbij** en de bestaande gebruikers.
5. **Advertenties verdienen zich bij onze prijzen niet terug** (I). Niet doen: Product Hunt, Show HN (verboden voor gegenereerde tekst), podcasts, Keymailer, persberichten in bulk, TikTok- en Meta-advertenties.

## Per product
**Hats of the Fallen** (de pagina hangt aan Valve, mogelijk eind januari; geen vaste paginadag)
1. **Vangnet nu:** pagina op dortus.com voor Hats met Kit-aanmelding (belofte: als eerste de demo, plus een Gloop-achtergrond) en een Discord. Hat Tower op Garmin verwijst ernaar.
2. **Het moment:** demo plus Desktop Companion Fest. Binnen 72 uur na de demo de makers: lijst van Sem plus Alpha Beta Gamer, ImCade en Indie Game Joe (F, C). Sem komt ±1 dec terug.
3. **Steam-eisen:** 6 tot 8 echte spelschermen (Valve wil er minstens 5 als gameplay; wij hebben er 5 en één is een menu), en de demo-app op dezelfde dag indienen als de hoofdapp (D).

**Click Joints Free en Pro**
1. **Zoekwoorden:** tagline met "3D printing" (voorstel A: `Poseable figures for 3D printing: ball joints with bend range`), titel en 12 tags op Superhive vol zoekwoorden.
2. **Eén echte print** (testprint ligt klaar). Zonder print geen posts in r/BambuLab, r/customactionfigures of bij 80 Level, en geen belofte dat het klikt.
3. **Uitleg en lijsten:** een rustige uitlegvideo van 8 tot 12 minuten, aanmelden bij blender-addons.org en de maandlijsten van InspirationTuts en BlenderHub, een post per versie op BlenderArtists. Let op: Pose to Print ($24) doet bijna wat Pro 1.1 "Rig to Figure" gaat doen.

**Bison & Flex** (groeit in jaren, niet in weken: verwachting voor 9 dec omlaag)
1. **In de aanraadlijst van JetBrains komen:** bij `.y` raadt JetBrains nu twee andere plugins aan, bij `.l` niemand. Vr 20 nov opnieuw meten; staan we er niet in, dan een mail aan JetBrains (tekst eerst langs Thijs), met één alinea over hun marketinghulp (hun pagina zegt "can", geen recht).
2. **Tutorial voor studenten:** een rekenmachine van nul (pagina plus video) en een installatiepagina voor Windows.
3. **Eén post** "I built a JetBrains plugin that ..." op r/Jetbrains en een post op r/Compilers, per versie.

**Garmin:** alleen Hat Tower, zolang hij "nieuw" is (tot ±1 dec): om reviews vragen, horloges erbij, verwijzing naar Hats. Verder niets.

## Snelle fixes (hoofdchat, deze week)
- dortus.com/ebb/ zegt $4,99, de winkel $2,99: gelijkzetten.
- `commercie/blender-click-joints/geplaatst.md`: BlenderNation (18 nov) en awesome-blender (17 nov) staan nog op "wacht".
- Filmpje 7 opnieuw op YouTube (mislukte op `>` in de tekst; de short van do 19 nov is al gerepareerd).
- Eigen sitemap per productmap op dortus.com.

## Automatiseren (alles € 0), in deze volgorde
1. **Weekpakket:** elke week alle conceptposts en video's in één wachtrij (`organisatie/goedkeuren.md`), één ja van Thijs, daarna inplannen in Metricool (Free: 20 posts per maand) of via de YouTube-API. (Chris)
2. **Blender-upload met token** in `click-joints-uitgave.yml`. (Bram)
3. **Scorebord elke dag:** winkelcijfers, onze plek in de zoekbalk van JetBrains, Blender en Steam, Metricool-cijfers, bezoekers per bron. (Chris)
4. **Vermeldingen volgen:** RSS van BlenderNation, CG Channel en 80 Level plus Google Alerts, naar `berichten/hoofdchat.md`. (Chris)
5. **Uitgavepakket:** per versie vanzelf een GIF en clip met vaste namen. (Bram, Olaf)
6. **Maillijst bij Kit** met formulier op dortus.com (de beveiligingsregel van de site moet Kit toelaten). (hoofdchat)
7. **Steam-aankondiging als concept** uit de changelog (er is geen gedocumenteerde API om te plaatsen; Thijs plakt), vanaf de paginadag. (Olaf)

## Wat alleen Thijs kan (eenmalig, samen ±30 minuten)
Blender-token (3 min), Kit-account met een postadres dat geen woonadres is, Discord-server, Search Console (10 min), 4 Google Alerts (5 min), een openbare meldingenrepo voor Bison & Flex (1 klik).

## Keuzes voor Thijs
1. **AI-melding waar die verplicht is** (itch, r/incremental_games, mogelijk 80 Level): eerlijk melden of die plekken overslaan. Het besluit "geen AI-melding" ging alleen over Steam.
2. **Posts op de Dortus-kanalen:** jouw ja per weekpakket (±5 minuten per week), of de hoofdchat na een keuring. Tot je kiest: jouw ja.
3. **Geld:** nu € 0. In januari eventueel $75 Reddit-advertenties voor Hats als leerproef, alleen als pagina en demo live zijn.
