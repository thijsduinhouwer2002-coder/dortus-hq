# Vier gifs voor de lange beschrijving op Steam (Hats of the Fallen)

Chris, 17 nov 2026, run 71. Voor Z6 in `platformen/steam/teksten-thijs.md` (voorstel Sem, 16 nov). Stand: CONCEPT, nog niet gekeurd door Daan, nog niet geüpload. Uploaden doet Thijs bij het vullen van de Steampagina (paginadag ±8 dec).

## De gifs

| Gif | Kopje (voorstel Sem) | Wat je ziet | Maat | Duur | Grootte |
|---|---|---|---|---|---|
| `1-heroes-come-in.gif` | Heroes fall | Een held met een emmer op zijn hoofd loopt het hol in, over de spijkers (hij licht rood op), naar Gloop, en wordt opgegeten. De emmer belandt op Gloop. | 616 x 160 | ±7,3 s | 144 kB |
| `2-gloop-wears-their-hats.gif` | Gloop wears their hats | Ingezoomd (2x): de hap, de emmer valt op Gloops kroon, munten springen naar de schat. | 616 x 320 | ±5,3 s | 280 kB |
| `3-they-come-back.gif` | The ones who escape come back | Tibbe de Hoard-Toucher, die eerder ontsnapte, komt terug met een boze bel boven zijn hoofd en loopt naar de spijkers. | 616 x 160 | ±10 s | 322 kB |
| `4-it-keeps-going-while-you-work.gif` | It keeps going while you work | **Nieuw in run 72 (na Daan 17 nov 01:30).** De rechterhelft van het hol (hoedenberg, Gloop, schat, laatste kamer) als strook van 130 px, boven de onderrand van één werkvenster met gevulde regels en een knipperend cursortje, onder een taakbalk. Een munt vliegt naar de schat, Gloop knijpt tevreden een oog dicht; dan de hap en ligt er een laars bij de schat. | 616 x 216 | ±7,3 s (laatste 1 s stil) | 91 kB |

Alles samen ±0,84 MB. Het laatste beeld van gif 1 tot 3 staat ±1,3 s stil, zodat het moment blijft hangen. Bestanden staan in deze map; ze worden gemaakt met `maak_gifs.py` (uitleg bovenin het script).

## Waarom zo

- **Echte beelden**, geen nagemaakte scènes: losse beelden uit de Windows-build van Olaf (tak `schermen`, commit 453aac1, `steam-hol/winkel-1920-demo-160/los` en `winkel-1920-week-160-claude-steam-hol-vol/los`), 3 beelden per seconde. Daardoor lopen de figuurtjes wat schokkerig. Ik heb er bewust geen tussenbeelden bij laten verzinnen.
- **Breedte 616 px.** Sem gokte 616. Wat ik zag (GEZIEN 17 nov, Steampagina van Rusty's Retirement met curl): 3 van de 5 beeld- en filmblokken in de beschrijving zijn 616 breed, de andere 735 en 800 (die schaalt Steam terug). De Steamworks-docs noemen geen breedte. 616 is dus veilig.
- **Geen tekst in de gifs.** Steam zegt letterlijk dat tekst in beelden per taal opnieuw gemaakt moet worden en raadt beelden zonder tekst aan (DERDEN, partner.steamgames.com/doc/store/page/description). Het logpaneel van het spel (Engelse zinnen) staat er daarom in geen enkele gif op; in gif 4 is het eraf gesneden, want op 616 px was het nog te lezen (controleur).
- **Grenzen van Steam** (DERDEN, zelfde pagina): elk beeld onder 5 MB, alle screenshots en gifs samen onder 15 MB. Wij zitten op ±0,86 MB.
- **Steam zet gifs om naar filmpjes.** Op de pagina van Rusty's staan de bewegende blokken als `.webm` en `.mp4` met een stilstaand eerste beeld (GEZIEN). Het eerste beeld van elke gif is dus ook wat je ziet voordat hij speelt; bij alle vier staat er dan al iets herkenbaars (held, Gloop, de strook).
- **Achtergrond**: de strook heeft kleine doorzichtige stukjes (boven hoeden, de onderrand). Daar staat een eigen schemerblauw bureaublad achter, in alle vier hetzelfde. Geen echt besturingssysteem, geen logo's.

## Eerlijk: wat niet helemaal past bij Sems kopjes

1. **"Heroes fall"**: in de demofilm sterft geen held in een val. De spijkers doen pijn (rood oplichten) maar de held loopt door; Gloop eet hem op. Het kopje klopt dus voor het spel als geheel (in de bron van gif 4 staat in het log "The Spike Pit had a busy shift"), maar gif 1 laat een hap zien, geen val. Voorstel: kopje "Heroes come for the gold" of de val opnemen zodra Olaf echte opnames van een week heeft waarin een held in de put valt (zijn mp4's na de speeltestbuild van vr 20 nov).
2. **Gif 1 en 2 tonen dezelfde hap.** Gif 1 van een afstand (het pad), gif 2 dichtbij (de hoed). Als er later een tweede hoed-moment uit een andere opname is (bijvoorbeeld de hoge hoed van Tibbe op de emmer, beeld 200 tot 205 van de demo), kan gif 2 dat worden, dan zie je de stapel groeien.
3. **Gif 3, "komt terug"**: zonder het eerdere ontsnappen zie je alleen een boze held met een wapen. Het kopje moet het verhaal vertellen. Het verband dat Olaf noemde is op deze maat niet te zien.
4. **Gif 4** is rustig en er beweegt weinig (de goudteller staat stil op 1655). Het spel is ±68 px hoog in een beeld van 280. Mila kan het bureaublad mooier maken als ze wil; de strook zelf blijft de echte opname.

## Wie nog wat doet
- **Daan**: keuren (beeld, uitsnede, kleur van het bureaublad).
- **Sem**: de kopjes, eventueel kopje 1 aanpassen (zie boven).
- **Thijs**: twee zinnen per kopje (Z6) en uploaden op de paginadag.

## Controle
Controleur (17 nov, run 71): akkoord mits. MOET: het logpaneel in gif 4 was nog te lezen; nu eraf gesneden. KAN verwerkt: gif 4 met grotere strook en kleiner bureaublad, gif 3 begint later en iets naar links (minder halve figuren aan de rand), eind 1,3 s stil. Niet verwerkt: gif 2 blijft een 2x vergroting (iets zacht), tot er opnames op hogere resolutie zijn. De controleur vindt "Heroes fall" wel passen: "fall" is sneuvelen, net als in "Hats of the Fallen".

## Gif 4 opnieuw (run 72, 17 nov ±02:00 UTC), op de moets van Daan
- **(a) uitsnede rechterhelft:** x 700 tot 1460 uit de strook van 1920, geschaald naar 616 breed, dus 130 px hoog (was 68). Het logpaneel valt erbuiten.
- **(b) iets wat gebeurt:** bron zoals Daan zei, `steam-hol/winkel-1920-week-160-momenthap-run43741420761/los` op `schermen`. Beelden f210 tot f240 (munt vliegt naar de schat, Gloop knijpt zijn oog dicht) en f280 tot f335 (hap, daarna de laars bij de schat). Het stuk f245 tot f275 is weggelaten: daar beweegt ±10 s niets. Geen beeld is bewerkt of verzonnen.
- **Eerlijk, wat er niet in zit:** in deze opname komt in de rechterhelft geen held aanlopen. De ridder valt rond f240 in de put links (x ±250), buiten de uitsnede, en bij de hap is geen held te zien. "Held komt aan" en "hoed valt op de stapel" staan dus niet in deze gif. Dat kan pas met een opname waarin een held tot Gloop loopt in de week-strook (Olafs mp4's na de speeltestbuild van vr 20 nov); gif 1 en 2 laten dat al zien.
- **(c) bovenrand:** één werkvenster, 74 px zichtbaar, vijf gevulde regels in rustig blauw, groen, oker en lila, geen tekst en geen logo's, cursortje knippert om de 2 beelden.
- **(d) duur:** 22 beelden op 3 per s, ±7,3 s, laatste beeld ±1 s stil. 91 kB.
- Voorblad met 6 beelden: `gif4-blad-run72.png`.
- **Gif 3 (kan van Daan, later beginnen):** niet aangepast. Een tel later beginnen haalt beeld 1 schoon, maar de bovenrand snijdt de held omdat de strook maar 160 hoog is; lager kan niet zonder een hogere opname. Volgt als Daan het een moet vindt.
- Controleur: geen aparte, Daan keurt het beeld; zelf nagekeken: maat, duur, beelden op ware grootte, geen leesbare tekst.
