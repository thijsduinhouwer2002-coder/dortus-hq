# Vier gifs voor de lange beschrijving op Steam (Hats of the Fallen)

Chris, 17 nov 2026, run 71. Voor Z6 in `platformen/steam/teksten-thijs.md` (voorstel Sem, 16 nov). Stand: CONCEPT, nog niet gekeurd door Daan, nog niet geüpload. Uploaden doet Thijs bij het vullen van de Steampagina (paginadag ±8 dec).

## De gifs

| Gif | Kopje (voorstel Sem) | Wat je ziet | Maat | Duur | Grootte |
|---|---|---|---|---|---|
| `1-heroes-come-in.gif` | Heroes fall | Een held met een emmer op zijn hoofd loopt het hol in, over de spijkers (hij licht rood op), naar Gloop, en wordt opgegeten. De emmer belandt op Gloop. | 616 x 160 | ±7,3 s | 144 kB |
| `2-gloop-wears-their-hats.gif` | Gloop wears their hats | Ingezoomd (2x): de hap, de emmer valt op Gloops kroon, munten springen naar de schat. | 616 x 320 | ±5,3 s | 280 kB |
| `3-they-come-back.gif` | The ones who escape come back | Tibbe de Hoard-Toucher, die eerder ontsnapte, komt terug met een boze bel boven zijn hoofd en loopt naar de spijkers. | 616 x 160 | ±10 s | 322 kB |
| `4-it-keeps-going-while-you-work.gif` | It keeps going while you work | De strook (zonder het logpaneel rechts), klein, onderaan een eenvoudig bureaublad boven de taakbalk, met twee lege vensters. Het hol na een week spelen (log: "227 came, 198 fell"), met een grote hoedenberg naast Gloop. | 616 x 280 | ±13,7 s | 114 kB |

Alles samen ±0,86 MB. Het laatste beeld van gif 1 tot 3 staat ±1,3 s stil, zodat het moment blijft hangen. Bestanden staan in deze map; ze worden gemaakt met `maak_gifs.py` (uitleg bovenin het script).

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
