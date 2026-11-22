# Productkans BOOTH: Unity-editortools en avatarsystemen voor VRChat

Onderzocht: 9 nov 2026, run 07:31 (Amsterdam), door Vera. Controleur akkoord met cijfer en advies, 10 correcties verwerkt (zie onderaan).

## Advies: nee voor nu. Cijfer 3.

Er wordt in deze markt echt betaald en nieuwe tools krijgen snel aandacht, maar ik vond geen soort tool met een zwakke, oude of afwezige nummer één. De top bestaat uit kleine makers die zelf nog actief zijn, en in elke niche met veel vraag komen er elke maand nieuwe makers bij. Daarbij halen AI-tools voor VRChat ongeveer de helft van de likes, en de VRChat-gemeenschap is op dit moment fel over AI. Wel een echte kans om in de gaten te houden: de overstap van VRChat naar **Unity 6** (SDK binnenkort in open beta) en later naar **URP**. Dan breken oude tools en shaders, en dat is precies het soort gat dat we zoeken.

## Platform en soort product
BOOTH (booth.pm, pixiv), categorie 3Dツール・システム: Unity-editortools, avatargimmicks en shaders voor VRChat, meestal ¥300 tot ¥1.500. BOOTH rekent af, kosten ±6% (zie voorstellen/booth.md, cijfer 6 als platform).

## Hoe gemeten
- GEZIEN: de 1.500 populairste tools van de categorie (lijst gesorteerd op likes, pagina 1 t/m 25), per item de open JSON (publicatiedatum, prijzen, likes, winkel, tags). Data: `data/booth-top1500-likes-2026-11-09.jsonl`.
- GEZIEN: de nieuwe lichting van 7 nov (alle 1.920 tools van 11 mei t/m 30 sep 2026, `data/booth-tools-2026-05tot09-2026-11-07.jsonl`), ingedeeld in 28 thema's op trefwoorden in naam en tags. Script: `data/booth-thema-script.py`. Een tool kan in meer thema's vallen; de indeling op trefwoorden is grof.
- GEZIEN: de Developer Updates van VRChat (ask.vrchat.com, 25 jun, 27 aug en 5 nov 2026) en de post "Regarding AI Usage on VRChat" (6 okt 2026).
- Niet te meten: verkoopaantallen (BOOTH toont ze niet; likes als maat, zie voorstellen/booth.md voor de schatting van ±36% likes naar aankopen) en het laatste bijwerken van een tool (de JSON heeft geen updatedatum, en GitHub van de makers was vanaf hier niet leesbaar).

## Bewijs van vraag en betalen (GEZIEN)
- Top 1.500: nummer 1 heeft 53.962 likes, nummer 100 6.066, nummer 500 1.527, nummer 1.500 342. Van de 1.500 zijn er 768 echt betaald (laagste prijs boven 0) en 461 gratis met een betaalde steunvariant.
- De top is jong: 1.068 van de 1.500 zijn in 2025 of 2026 uitgebracht. Nieuwe tools komen dus snel bovenin.
- In de top 300 staan 190 verschillende winkels; de 160 betaalde tools daarin komen van 112 winkels. 27 van die 160 zijn van voor 2024.

## Waar de vraag het hoogst is (nieuwe betaalde tools mei t/m aug 2026, mediaan likes)
| Thema | Nieuwe betaalde tools | Winkels | Mediaan likes | 500+ | Nummer één in de top 1.500 |
|---|---|---|---|---|---|
| Aai-gimmicks (撫で, なでなで) | 9 | 9 | 514 | 5 | 赤夜式 撫で音ギミック, 26.042 likes, okt 2024, ¥900 |
| Poses | 14 | 14 | 166 | 3 | AvatarPoseSystem, 30.647, aug 2024, ¥1.200 |
| Staart, oren | 21 | 10 | 108 | 2 | |
| Modular Avatar en niet-destructief | 83 | 65 | 97 | 13 | Light Limit Changer, 28.604, gratis met steun |
| Shaders | 80 | 63 | 77 | 12 | lilToon, 51.783, gratis |
| Haar | 16 | 15 | 93 | 3 | Kami-Pita, 15.713, jan 2026, gratis met steun |
| Geluid | 26 | 22 | 71 | 5 | 赤夜式 撫で音ギミック |
| Gezicht en expressies | 111 | 52 | 52 | 8 | FaceEmo, 32.168, gratis |
| Lichter maken (optimalisatie) | 18 | 15 | 11 | 1 | AAO, 32.002, gratis |
| Quest, Android, iOS | 14 | 12 | 11,5 | 1 | |
Alle nieuwe betaalde tools samen: mediaan 40 likes (meting 7 nov). De tabel is een selectie van de 28 thema's.

Let op de grove indeling (controleur): bij aaien gaat het om 7 à 9 echte tools ('pat' ving ook "Spatial", en Nade Pose Editor is een gebarentool); zonder die twee blijft de mediaan 514, en precies de twijfeltool ガチ恋シェーダー (514) bepaalt die. Slapen viel uit de tabel: '寝' ving ook 添い寝 (twee NPC-tools voor werelden); er blijven 4 echte V睡-tools over met mediaan ±22. Poses is een mengzak van vooral editortools voor foto's en poses; zonder vier valse treffers ±222. Bij staart en oren ving '耳' ook 耳かき (oorschoonmaken).

## Top 3 en hoe sterk ze zijn, in de beste niches
- **Aai-gimmicks:** 赤夜式 (26.042), リアルなでシェーダー van osakanaheaven (14.923, en in apr 2026 een nieuwe met 6.066), Shadowdepth Shader van wataame89 (13.936; maker bracht nog in aug 2025 iets uit). Daarnaast 2026 al nieuwe toppers: てとら式すりすり (3.837, gratis), お顔もちもち (2.137, ¥300), なでビジョン (1.303, ¥500, sep 2026). Sterk en druk.
- **Slapen (bleek na controle klein, 4 nieuwe betaalde tools, mediaan ±22):** GoGo Loco (gratis, de standaard), VRC睡眠システム van goho-cheat-vrc (15.379, ¥300, uit 2021; de maker maakt nu avatars, Komane jul 2026 met 7.881 likes, dus niet verdwenen), RBS SuiminSystem 2 (9.490, gratis). Gratis is hier sterk.
- **Poses:** AvatarPoseSystem (30.647), AvaPo! (21.556, aug 2025), AvatarBasicTool van childwitch (18.031, gratis; deze maker heeft 9 tools in de top 300 en bracht er in 2025 nog meer uit). In mei t/m sep 2026 kwamen er 35 treffers op pose bij (met een paar valse).

## Gezocht naar een zwakke of oude nummer één
- Van de 160 betaalde tools in de top 300 zijn er 27 van voor 2024. Bij 8 daarvan vond ik in mijn data niets nieuwers van na 2023 van dezelfde winkel. Die telling zegt weinig: mijn data dekt alleen de top 1.500 en mei t/m sep 2026. Bij de grootste (goho-cheat-vrc, 16 items in de top 300) bleek de maker gewoon actief met avatars in 2026.
- Oudste grote betaalde tool: VirtualLens2 (39.949 likes, 2020, ¥1.300). De winkel bracht sinds 2021 niets nieuws uit op BOOTH, maar de tool wordt bijgewerkt via een eigen pakketbron; of dat nog gebeurt kon ik niet lezen (GitHub geeft 403 vanaf hier). Er staan 94 camera-tools in de top 1.500, dus vervangers zijn er al.
- Oude top met een stille maker (gevonden door de controleur): フェイドアウトシステム Ver.2.0 van fleur7tec7oha7 (19.951 likes, jan 2023, ¥200; winkel sinds jul 2023 stil). Nummer twee One Fade Out (4.500, ¥1.000) komt ook van een stille winkel. Maar er zijn gratis lilToon-fadetools (1.533 en 1.527 likes) en de prijs is laag; de tool hangt aan shaders, dus URP kan hem raken. Kandidaat voor de herhaalmeting, geen reden voor ja nu.
- Nagekeken en niet zwak: PoLKA (verlichting, 2021, stil) heeft actieve concurrenten (UMHL 4.020, MA Light Controller 3.957), PPPen (2021, stil) heeft sterke gratis tegenhangers (QvPen, Pen-Ta).
- Conclusie: geen niche gevonden waar betaald wordt en de top zwak is. Waar de vraag hoog is, is het druk en zijn de makers actief.

## AI: een rem voor ons (GEZIEN)
- 24 nieuwe tools (mei t/m aug) noemen AI, ChatGPT, Claude of LLM in naam of tags: mediaan 11,5 likes tegen 41. Daar zitten valse treffers en niet-VRChat-spullen in (InnerRise zegt juist "zonder AI", promptbundels, Minecraft-kits). Alleen de 15 AI-tools voor VRChat of Unity: mediaan **±24 tegen 41**, dus ongeveer de helft. Kleine groep, maar een duidelijk verschil.
- VRChat schreef op 6 okt 2026 "Regarding AI Usage on VRChat": AI-thumbnails die misleiden zijn verboden, er liep een enquête, en op 5 nov is er nog geen nieuw beleid. De gemeenschap is verdeeld en vaak tegen.
- Dortus maakt alles met AI en verstopt dat niet. Op BOOTH en in VRChat kost dat ons dus aandacht.

## Het gat dat er wel aankomt: Unity 6 en daarna URP (GEZIEN, VRChat Developer Updates)
- 25 jun 2026: VRChat zelf draait in een open beta op Unity 6 (6000.0.60f1). Makers mogen nog niet overstappen. VRChat schreef daar ook dat de render-pipeline niet verandert, dat bestaande content blijft werken en dat Udon shims krijgt.
- 5 nov 2026: "Unity 6 SDK is coming to Open Beta Soon!", met een Upgrade Wizard die waar het kan automatisch repareert. Unity-versie 6000.0.67f1, de Creator Companion zet hem zelf klaar.
- Daarna noemt VRChat "the upcoming URP work", een overstap van de oude render-pipeline naar URP. Dat raakt alle eigen shaders (lilToon, Poiyomi en de aai-, schaduw- en effectshaders in de top), maar er is geen datum.
- GOK (gesteund door die uitspraak van 25 jun): bij Unity 6 breekt vooral een deel van de editortools (verouderde Unity-API's, UI-code), niet de gimmicks die alleen uit animaties en prefabs bestaan. Hoeveel er breken is pas te meten als de SDK uit is.
- Wat het voor ons kan betekenen: betaalde tools van makers die niet meer bijwerken, die het onder Unity 6 niet meer doen, en waar mensen in de eerste weken om vragen. Dat is te meten.

## Wie betaalt, hoeveel en hoe vaak
Eén persoon voor zichzelf (een VRChat-speler die zijn avatar aanpast), eenmalig ¥300 tot ¥1.500 (mediaan ¥500, ±$3,30). Met de schatting uit voorstellen/booth.md verkoopt een betaalde tool met 500 likes ±180 keer. Geen abonnementen.

## Eerste productidee (alleen als de herhaalmeting een gat laat zien)
Een vervanger voor een veelgebruikte betaalde editortool die onder Unity 6 kapot is en niet wordt bijgewerkt, in het Japans en Engels, niet-destructief met Modular Avatar of NDMF, ¥500 tot ¥1.000. Eerlijk vermelden dat het met AI is gemaakt.

## Cijfer en advies
Cijfer 3, nee voor nu.
- Vraag en betalen: goed (gemeten via likes, verkoop geschat).
- Zwakke top: niet gevonden; in de beste niches juist veel actieve makers en snelle nieuwkomers.
- Past bij ons: code kan Claude schrijven, maar de best lopende soorten (aaien, slapen, poses) draaien om gevoel, geluid en beweging en vragen testen in VR. Japanse taal en de AI-weerstand maken het zwaarder.

**Herhaalmeting:** 4 tot 8 weken nadat de Unity 6 SDK voor makers live gaat (niet de open beta), uiterlijk 1 feb 2027. Meet dan: welke betaalde tools uit de top 300 (data/booth-top1500-likes-2026-11-09.jsonl) melden Unity 6 in hun beschrijving, welke niet (begin bij フェイドアウトシステム, One Fade Out en VirtualLens2), en waar in de VRChat-gemeenschap om een werkende vervanger wordt gevraagd. Zelfde vraag opnieuw als VRChat een datum voor URP noemt.

Geen bericht aan een manager: BOOTH heeft geen manager. Hans kan dit naast voorstellen/booth.md leggen.

## Controle
Controleur (agent) rekende alle getallen na met eigen scripts en las de VRChat-bronnen. Akkoord met cijfer 3 en nee voor nu. Verwerkt: 112 winkels voor de betaalde tools, 8 in plaats van 14 stille winkels, slapen uit de tabel (valse treffers op 添い寝), kanttekeningen bij aai en poses, haar en geluid in de tabel, AI-verschil ±24 tegen 41 voor echte VRChat-tools, nieuwere likes bij twee tools, de uitspraak van VRChat over de render-pipeline bij Unity 6, en de gemiste fade-out-kandidaat.
