# Stijl van Dortus

Beheerd door Daan (`organisatie/rollen/ontwerper.md`). Wat we altijd doen en nooit doen, voor alle producten, winkelpagina's en dortus.com. Versie 16, 8 november 2026. Groeit mee na elke beoordeling.

## Het gevoel in één zin

Een Dortus-product valt op: het heeft een eigen gezicht dat je in één oogopslag herkent, het is leuk om op te klikken, en het werkt in elk thema alsof het er altijd al hoorde. (Versie 8: de oude zin "rustig, past bij de app" was de ondergrens, niet het doel. Zie "De lat" in `organisatie/rollen/ontwerper.md`.)

## Eigen gezicht (sinds versie 8)

- Elk product heeft één sterk eigen element dat overal terugkomt: in de app, in de winkelplaatjes, op de poster. Bij Rollwright het token met de d20.
- Het eigen gezicht bouwen we op de kleuren van het thema: verloop en randen met `color-mix()` van de accentkleur over de achtergrond, en de kleuren `--color-yellow`, `--color-red` van het thema voor bijzondere momenten. Zo is het eigen, en toch leesbaar in licht, donker en elk thema.
- Een eigen icoon of teken mag (als CSS-masker of SVG die de themakleur volgt). Een eigen lettertype laden nog steeds niet.
- Bewegingen: kort (onder de halve seconde), alleen na een klik van de gebruiker, nooit bij openen, nooit herhalend, en uit bij `prefers-reduced-motion`. Een beweging vertelt iets (de worp rolt, een 20 licht op), anders laten we hem weg.
- Een bijzonder moment (crit, fumble, iets wat lukt) komt pas als de uitkomst er is, nooit eerder: geen kleur of teken dat het verklapt terwijl het nog rolt. En het moment krijgt een echte klap (iets wat even opspringt), geen zachte kleurwissel. (Versie 9.)
- Tekst uit een tabel of lijst is rustiger dan een getal: geen pil, geen vet, wel het eigen teken zodat je ziet dat je erop kunt klikken. (Versie 9.)
- Een teken dat bij een uitkomst hoort (NAT 20, MIN) komt erbij zonder iets op te schuiven: als sticker op de hoek, niet in de regel. Een regel tekst mag nooit verspringen door een klik. De sticker dekt het getal nooit af en leest op ware grootte. (Versie 11.)
- Bij een programmeertool (JetBrains) blijven we van de kleuren in de editor af: die kiest de programmeur zelf. Het eigen gezicht zit daar in het pluginicoon, de poster en het kleine icoon in onze meldingen, en die drie vertellen hetzelfde verhaal (bij Bison & Flex: de boog van scanner naar grammatica). (Versie 10.)
- Een signaalkleur (goed, krap, fout) mag nooit lijken op een kleur die het platform zelf al gebruikt voor iets anders. Blender tekent een selectie oranje, dus daar is krap amber geel, niet oranje. Kijk bij elk nieuw platform eerst welke kleuren al een betekenis hebben. (Versie 14, Click Joints.)
- Meet een signaalkleur in de echte weergave van het platform, niet op de kleurkiezer. In Blender Solid komt geen kleur boven ±`#AE` per kanaal; geel met wit erin wordt daar mosterd, verzadigd citroengeel (`#FFEA00`) blijft geel. Kies daarom verzadigde tinten zonder wit, en toets rood, groen en geel ook zoals iemand zonder groen zien ze ziet. (Versie 16, proefstrook Click Joints.)
- Een functie die iets weghaalt of verandert, toon je op een winkelplaatje als voor en na, niet alleen als menu. (Versie 16, Bison & Flex plaatje 5.)
- Een pluginicoon vertelt in één beeld wat ons onderscheidt, geen abstracte vormen. Toets het op ware grootte (40px en 16px, licht en donker), niet alleen groot. Onder 16px weglaten wat niet leest. (Versie 10.)
- De vraag bij elk oordeel: zou een gebruiker hier een schermafbeelding van maken om aan een vriend te laten zien?

## Uiterlijk in een app (Obsidian, JetBrains)

Altijd:
- De kleuren, letters, randen en afstanden van het platform. In Obsidian alleen CSS-variabelen (`--background-secondary`, `--text-normal`, `--interactive-accent`, `--size-4-2`, `--radius-s` en zo). Zo werkt het vanzelf in licht, donker en elk thema.
- De gewone onderdelen van het platform: `Setting` voor instellingen, `setHeading()` voor kopjes, `Notice` voor korte meldingen, `Modal` voor een vraag, de ingebouwde iconen (Lucide in Obsidian).
- Getest in licht, donker en minstens 3 populaire thema's (Minimal, AnuPpuccin, Things, Border) en in een smal venster.
- Eén accentkleur, die van het platform. Een icoon mag die kleur hebben, gewone tekst niet (een korte naam in kleine hoofdletters, zoals in het logboek, mag gemengd met de tekstkleur).
- Alles werkt met alleen het toetsenbord, en elke knop zonder tekst heeft een naam (tooltip of `aria-label`).
- In Obsidian zowel de leesweergave als Live Preview bekijken. Ze moeten er hetzelfde uitzien. Live Preview zet `white-space: pre-wrap` op de regel: wat je erin rendert krijgt `white-space: normal`, anders worden regeleinden lege regels.
- Een knop om te kopen is een gewone knop met de prijs erop ("Buy for $6"), geen opvallende accentknop.

Nooit:
- Vaste kleuren in de gratis versie. Vaste kleuren mogen alleen in een betaalde skin die de gebruiker zelf kiest, en die moet in licht en donker leesbaar zijn.
- Eigen lettertypes laden. Schaduwen en bewegingen zonder betekenis, of die blijven bewegen (versie 8: korte bewegingen na een klik en een zachte gloed mogen wel, zie "Eigen gezicht").
- Knipperen of verspringen: een uitkomst die verandert, verandert op zijn plek, de regel eromheen schuift niet.

## Teksten

- Engels in de producten (de markt is wereldwijd), Nederlands in de repo.
- Sentence case op knoppen en kopjes: "Get the paid skins", niet "Get The Paid Skins". Dat is ook de regel van Obsidian.
- Altijd de hoofdletterregel van het platform. Obsidian: overal sentence case. JetBrains: Title Case op knoppen, menu's, tooltips van acties en kopjes van dialogen; sentence case voor links, snelle oplossingen, meldingen (kopje en acties) en gewone zinnen ([Capitalization](https://plugins.jetbrains.com/docs/intellij/capitalization.html)).
- Kort. Een omschrijving onder een instelling is één zin. Lange uitleg hoort in de README, niet in de app.
- Een knop zegt wat er gebeurt: "Roll", "Replace", "Activate". Niet "OK" of "Submit".
- Foutmeldingen zeggen wat er mis is en wat je kunt doen, in gewone woorden: "This formula ends with +. Add a number or a die after it." Nooit een technische melding of een stack.
- Geen uitroeptekens, geen emoji, geen verkooppraat in de app.

## Leeg begin

- Een nieuwe gebruiker ziet binnen een minuut iets werken. Een leeg paneel zegt in één zin wat je moet doen, liefst met een voorbeeld dat je kunt aanklikken.
- Een leeg paneel is ook een eerste indruk: het eigen teken groot, één korte zin, de knop eronder, in het midden. Nooit een losse grijze zin met een knop eraan vast. (Versie 12.)

## Het betaalde deel

- Gratis is compleet: alles wat je nodig hebt werkt zonder te betalen. Betalen is voor wie meer wil (mooier, sneller, extra).
- Je ziet wat je koopt voordat je betaalt: een voorbeeld in de app of een plaatje op de koopknop.
- Een voorbeeld van een skin toont groot wat per skin anders is, niet wat in elke skin hetzelfde is. (Versie 12, Rollwright: de gouden crit is overal gelijk, dus de gewone worp staat voorop.)
- Een lijstplaatje over skins of thema's toont hetzelfde scherm naast elkaar in elke variant, licht en donker, van echte schermen op leesbare grootte. Nooit een kleine tegel opgeblazen. (Versie 13, Rollwright plaatje 3.)
- Winkelplaatjes en posters opslaan als jpg (kwaliteit 90) of volle png, nooit met een palet van 256 kleuren: dat maakt verlopen en skinkleuren grijs. (Versie 13.)
- Een uitkomst zonder eigen vlak (tabel, lijst) neemt de letter van het thema, niet van de skin. Test elke skin ook in het andere thema. (Versie 13, Arcane licht.)
- Eén rustige plek in de instellingen, onderaan. Nooit een popup, nooit een melding in een notitie, nooit herhaald vragen.
- De koopknop zegt de prijs: "Buy for $6", zodat niemand schrikt op de betaalpagina.
- Een betaalde functie die je (nog) niet hebt, geeft nooit een foutmelding. De eerste keer één rustige melding die zegt wat Pro is, daarna stil of een korte hint zonder knop. Wat elke gebruiker van de app gewoon verwacht (zoals Ctrl+B binnen één bestand), zetten we niet achter betalen.
- De tekst over Pro zegt precies wat Pro is. Klopt de tekst niet met wat er gebeurt, dan voelt het als een truc.
- Een melding over Pro komt alleen na een bewuste actie (een klik of een sneltoets), nooit bij zweven, kijken of openen.
- Een knop met "trial" of "buy" brengt je in één stap naar de proef of de aankoop van dit product, nooit naar een algemene voorpagina.

## Winkelpagina's en dortus.com

- Het eerste lijstplaatje is een poster (versie 8, bericht Thijs 22:10): een korte kop van hoogstens zes woorden, het product groot en mooi in beeld in echt gebruik, het eigen teken als enig logo. Geen kale schermafbeelding van een witte notitie, geen tekstplaat zonder product.
- Toont de poster een betaalde functie, dan staat dat op de poster zelf, leesbaar op 900 breed (een PRO-label bij die functie en een regel wat gratis is). Niet alleen in een kleine grijze voetregel. (Versie 10.)
- Een poster is gemaakt van echte schermen uit de test, alleen bijgesneden; daaromheen mag een eigen achtergrond, kop en pijl. Een scherm mag licht gedraaid staan, en een uitvergroting van één detail mag als die op hoge zoom echt is opgenomen (scherp, geen opgeblazen pixels). Elke tekst op de poster klopt met de prijs: noemt hij "free", dan staat de betaalde optie ernaast. (Versie 12.) Geen vensterknoppen van een ander systeem dan de toetsen die we noemen (Ctrl, dan geen Mac-stippen). (Versie 10.)
- Plaatje 2 en verder zijn kaarten in dezelfde stijl als de poster: dezelfde achtergrond en merkregel, een FREE- of PRO-chip, één kop van hoogstens zes woorden, hoogstens twee regels uitleg, en één echt scherm groot. Elke kaart toont één functie, en de uitleg zegt alleen wat op het scherm te zien is. Een betaalde functie toon je werkend, nooit de melding dat hij betaald is. Licht en donker om en om. (Versie 15, Bison & Flex.)
- In de README een korte bewegende GIF (±5 seconden) bovenaan die het mooiste moment laat zien.
- Schermafbeeldingen in het standaardthema, licht en donker allebei, scherp (factor 2), zonder persoonlijke bestanden in beeld.
- Het eerste plaatje toont ook wat je typt, niet alleen de uitkomst: "dit typ je, dit krijg je" (bijvoorbeeld één regel met de code naast regels met de uitkomst).
- Geen lege helft: venster laag genoeg of bijsnijden tot de inhoud. Geen rand of balk van het testscherm in beeld.
- Niets in beeld dat op een fout lijkt: geen rode statusiconen, geen gele lampjes, geen focusrand, geen hoofdletters midden in een zin.
- Geen meters of tellers die niets met het product te maken hebben (geheugenmeter, klok, testbalk). Uitkomsten die in meer plaatjes staan, zijn in elk plaatje gelijk, en een uitkomst blijft op één regel waar dat kan.
- Na een klik in de test eerst de focus weghalen, dan pas de opname maken.
- Taal van de winkel (Engels), ook in projectnamen, bestandsnamen en commentaar in de voorbeeldcode.
- Eerste zin van de pagina: wat het doet, in maximaal 15 woorden. Daarna een korte lijst, daarna details.
- Eerlijk: geen functies beloven die er nog niet zijn, geen nep-reviews of nep-cijfers.
- Support via **thijs@dortus.com** (keuze van Thijs, 7 nov 2026: persoonlijker). In de app, de README en op dortus.com. Niet meer support@dortus.com.
- Persoonlijk, één keer per pagina: de regel "Made by Thijs at [Dortus](https://dortus.com)" bovenaan de winkelpagina, in de zin over voor wie het is ("Made by Thijs at Dortus for game masters ..."). Niet in de app zelf, geen foto, geen verhaal: één regel is genoeg.
- Opbouw van een README als winkelpagina: één zin wat het doet, het eerste plaatje, de regel "Made by Thijs ...", "What you can do" (hoogstens zes punten), een tweede plaatje, "Quick start" in drie stappen, de prijs in één zin. Daaronder "Full reference" met kopjes, dan Paid, Privacy, Support, License.

## Voorbeelden die we volgen

Versie 8, wat ik overneem en waarom:
- **Fantasy Statblocks** (Obsidian, 371.393 downloads, DERDEN): je herkent het meteen aan het monsterblok uit het spelersboek. Overnemen: een eigen herkenbaar teken en kleine hoofdletters voor namen. Waarom: herkenbaar zijn is wat ons nu ontbreekt.
- **Dice So Nice (Foundry) en D&D Beyond**: rollen voelt echt en een crit is een feestje. Overnemen: het moment, klein en snel in de tekst. Niet: 3D en wachten.
- **Things 3 en Linear**: elke klik geeft een kleine fijne reactie, niets beweegt zonder reden. Overnemen: indrukken, landen, nooit herhalen.

- **Excalidraw, Kanban, Fantasy Statblocks (READMEs, 8 nov):** zelfs de grootste plugins openen met een tekstregel en één kale schermafbeelding, geen poster en geen GIF. Overnemen: niets; juist daarom valt een poster met een korte kop en een GIF bovenaan bij ons op. (Versie 9.)

Eerder:

- **Dice Roller** (de voorganger van Rollwright): een uitkomst staat klein en rustig in de tekst, een klik rolt opnieuw. Dat overnemen: de gebruiker kent het al.
- **Tasks, Calendar, Style Settings**: gebruiken alleen variabelen van Obsidian en zien er daardoor in elk thema goed uit. Dat is onze norm.
- **JetBrains, ingebouwde talen**: kleuren alleen via `DefaultLanguageHighlighterColors` en een eigen kleurenpagina in Color Scheme, iconen in de lijnstijl van de nieuwe UI met een donkere versie, meldingen als balloon, nooit een dialoog. Zo ziet een plugin er in elk thema uit als een ingebouwde taal.
- **De ingebouwde instellingen van Obsidian**: korte namen, één zin uitleg, kopjes met `setHeading()`. Zo moeten onze instellingen ook lezen.
