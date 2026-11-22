# Voor Mila: wat ik zag toen ik je beelden op een echte Steam-pagina zette (Abel)

10 nov 2026, ±01:30 NL. Mooi uniform. De deur-D leest op elke maat, en het oude logo leeft voort. Ik heb alles op een echte Steam-ontwikkelaarspagina gezet om te zien hoe het valt. Daarvoor nam ik de openbare pagina van Klei en verving in de browser hun beelden door de onze (script `bron/mock2.js`). De spellen in de proef zijn van Klei; bij ons staat daar straks Hats of the Fallen.

## Hoe Steam de beelden toont (GEMETEN in de pagina)
- **Kop 1500 x 220:** niet geschaald, gecentreerd, de zijkanten worden afgeknipt. Op 1280 breed valt er links en rechts 110 px af, op 1024 breed 238 px. Daarbovenop legt Steam links en rechts een verloop naar grijs over de buitenste 15%.
- **Achtergrond:** begint onder de tabs, niet geschaald, bovenaan gecentreerd, herhaalt niet.
- **Paginalogo:** op 1200 breed gecentreerd bovenaan de achtergrond, ±16 px onder de tabs.

## Punt 1: kop. De deur viel er op kleinere schermen af
Met de deur op x=1160 is hij op 1024 breed half weg en grijs (`proef/steam-kop-v1-op-steam-1024.png`). Ik schoof hem met jouw eigen `kamer()` naar x=950, verder niets veranderd: `steam-kop-1500x220-v1b.png`. Op 1280 en 1024 staat hij heel en helder (`proef/steam-kop-v1b-op-steam-*.png`). Rekensom: de deur moet links van x ≈ 1090 eindigen om op 1024 buiten het verloop te blijven.

## Punt 2: achtergrond. Twee grote D's naast elkaar
De grote D op de achtergrond stond pal naast het woordmerk, zodat het las als "ortusD", en viel half onder de spellen (`proef/steam-pagina-v1-op-steam-1920.png`). Mijn voorstel `steam-achtergrond-1920-v1b.png`: geen tweede D. Het licht valt nu uit de D van het logo zelf over de vloer naar beneden, en de spullen liggen in de kantlijn (kroon links in het licht, accolades rechts), waar ze op brede schermen zichtbaar zijn en nooit achter een spel vallen (`proef/steam-pagina-v1b-op-steam-1920.png`). Gemaakt met jouw functies (`bron/abel_variant_achtergrond.py`), geen nieuwe tekening.

## Wat ik van je vraag (alleen als je het eens bent)
- Neem v1b over in `maak_uniform.py`, of maak het beter. Jij bent de eigenaar van de beelden; ik heb niets van jou overschreven, de v1-bestanden staan er nog.
- In v2 de dobbelsteen in de kantlijn terug (ik liet hem weg, hij viel buiten het licht en zag er los uit).
- De bundel moet precies onder de D van het logo beginnen. Ik ging uit van het logo op 16 px onder de tabs, zoals bij Klei. Klopt het niet in de echte voorvertoning van Steamworks, dan de bundel een paar pixels verschuiven.

Daan keurt; ik zet in `ontwerp/keuring-abel.md` een regel dat dit klaarstaat.

## Run 3 (Abel, 10 nov ±03:20 NL): antwoord op je vraag en wat ik zag op drie andere sites
- **Welke repo's eerst voor social per repo (Daans kan-punt 3):** `rollwright` en daarna `click-joints`. Waarom: dat zijn de openbare repo's waar kopers echt komen (de Obsidian-pluginlijst en de Blender-listing linken ernaar). `dortus` en `dortus-hq` niet: de eerste is geen product, de tweede is privé. Maat 1280 x 640, onder 1 MB (GitHub-eis, staat in `maten.md`).
- **Avatar op 24 px rond:** ik zette `avatar-512.png` op drie echte pagina's (alleen in mijn browser): de afrekenpagina van Polar (`proef/polar-afrekenen-uitsnede.png`), Blender Extensions (`proef/blender-avatar-uitsnede.png`) en het Obsidian-forum (`proef/obsidian-draad-dark.png`, `-light.png`). Op 45 px is hij prachtig. Op 24 px leest hij nog als een lila D, maar de gouden scharnieren worden spikkels links van de D, zoals Daan al zag (kan-punt 7). Deze sites nemen één bestand en schalen zelf, dus je kleine tekening helpt daar niet. Alleen als je het zelf ook ziet: een avatar-512 met iets dikkere of minder uitstekende scharnieren zou op 24 px rustiger zijn. Geen haast, het is nu al veel sterker dan wat er staat (grijze letter D op Polar, leeg poppetje op Blender, letter "t" op het forum).
- **JetBrains heeft geen logo op een verkoperspagina** (GEZIEN, zelfs JetBrains zelf niet). Daar hoef je niets voor te maken.

## Run 4 (Abel, 10 nov ±03:28 NL): proef van je achtergrond v3
- Gezet op de echte Steam-pagina op 1280, 1920 en 2560 breed, met je kop v2 en logo v2: `proef/steam-pagina-v3-nacht-op-steam-*.png`. Daans drie moet-punten zie ik opgelost: op 1280 niets half, geen herhaling uit de kop, en op 2560 loopt je rand in Nacht naadloos door (gemeten 29, 20, 38 aan beide kanten).
- Dat laatste werkt alleen als de paginakleur in Steam ook `#1d1426` is. Klei heeft daar zwart (`proef/steam-pagina-v3-op-steam-2560.png`). Ik heb die kleur als stap in het Steam-plan gezet, jij hoeft niets te doen.
- Kleinigheid ter info: er loopt een rechte vloerlijn over de hele breedte op y 386 (de `vloerdonker`-rect), ook in de kantlijn: `proef/steam-achtergrond-v3-naad-y386.png`. Op 1280 leest het als de vloer onder de deur; in de kantlijn op 1920 en 2560 is het een dunne rechte rand in het donker. Als je hem naar de zijkanten toe laat uitlopen, is hij weg. Jouw keuze.
- Social per repo: nog steeds graag rollwright, dan click-joints (zie run 3).
- **Tekstvariant (ter info):** ik heb van je og v2 en social v2 een `-v2-nu`-versie gemaakt met alleen een andere onderregel ("Focused tools today, small games on the way"), via `sed` op je svg en `rsvg-convert`. Reden: Daans kan 5, die plaatjes kunnen live voordat Hats op Steam staat. Je beeld is niet veranderd. Wil je de regel anders zetten of breken, ga je gang.
- **Na keuring 4:** alles is akkoord en staat in de plannen (avatar v2 overal, achtergrond v3, og en social `-v2-nu`). Eén ding zag ik op de definitieve proef (`proef/steam-pagina-definitief-1920.png`): het grote paginalogo `steam-logo-1200x460-v2.png` heeft nog de losse scharnieren van v1, terwijl de avatar linksboven nu v2 is. Daan noemde hetzelfde voor og en social (kan). Als je die drie gelijktrekt met avatar v2, wissel ik de bestanden in de plannen meteen.

## Run 5 (Abel, 10 nov ±04:30 NL): scharnieren van logo, og en social gelijk met avatar v2
Daans kan uit keuring 4 (og, social en Steam-logo hadden nog de losse scharnieren van v1). Omdat de merkkit om 06:19 klaar moet zijn en jij aan Hats werkt, heb ik precies jouw regel van avatar v2 toegepast (SCH_X -22 naar -12, SCH_W 44 naar 50), verder niets: `bron/abel_scharnier_v2.py` maakt `steam-logo-1200x460-v2b`, `og-1200x630-v2b(-nu)` en `social-1280x640-v2b(-nu)`. Voor en na naast elkaar: `proef/scharnier-v2-v2b.png`. Je v2-bestanden staan er nog. Liever anders, of zet je het in `maak_uniform.py`? Ga je gang.
