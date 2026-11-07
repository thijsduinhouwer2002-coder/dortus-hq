# Stijl van Dortus

Beheerd door Daan (`organisatie/rollen/ontwerper.md`). Wat we altijd doen en nooit doen, voor alle producten, winkelpagina's en dortus.com. Versie 2, 7 november 2026. Groeit mee na elke beoordeling.

## Het gevoel in één zin

Een Dortus-product voelt alsof het altijd al bij de app hoorde: rustig, duidelijk, en het doet wat je verwacht bij de eerste klik.

## Uiterlijk in een app (Obsidian, JetBrains)

Altijd:
- De kleuren, letters, randen en afstanden van het platform. In Obsidian alleen CSS-variabelen (`--background-secondary`, `--text-normal`, `--interactive-accent`, `--size-4-2`, `--radius-s` en zo). Zo werkt het vanzelf in licht, donker en elk thema.
- De gewone onderdelen van het platform: `Setting` voor instellingen, `setHeading()` voor kopjes, `Notice` voor korte meldingen, `Modal` voor een vraag, de ingebouwde iconen (Lucide in Obsidian).
- Getest in licht, donker en minstens 3 populaire thema's (Minimal, AnuPpuccin, Things, Border) en in een smal venster.
- Eén accentkleur, die van het platform. Een icoon mag die kleur hebben, tekst niet.
- Alles werkt met alleen het toetsenbord, en elke knop zonder tekst heeft een naam (tooltip of `aria-label`).

Nooit:
- Vaste kleuren in de gratis versie. Vaste kleuren mogen alleen in een betaalde skin die de gebruiker zelf kiest, en die moet in licht en donker leesbaar zijn.
- Eigen lettertypes laden, schaduwen of bewegingen die aandacht trekken.
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

## Het betaalde deel

- Gratis is compleet: alles wat je nodig hebt werkt zonder te betalen. Betalen is voor wie meer wil (mooier, sneller, extra).
- Je ziet wat je koopt voordat je betaalt: een voorbeeld in de app of een plaatje op de koopknop.
- Eén rustige plek in de instellingen, onderaan. Nooit een popup, nooit een melding in een notitie, nooit herhaald vragen.
- De koopknop zegt de prijs: "Buy for $6", zodat niemand schrikt op de betaalpagina.

## Winkelpagina's en dortus.com

- De eerste schermafbeelding laat in één oogopslag zien wat het doet: het product in gebruik, in een gewone notitie of editor, met echte voorbeeldinhoud. Geen logo of tekstplaat als eerste plaatje.
- Schermafbeeldingen in het standaardthema, licht en donker allebei, scherp (factor 2), zonder persoonlijke bestanden in beeld.
- Eerste zin van de pagina: wat het doet, in maximaal 15 woorden. Daarna een korte lijst, daarna details.
- Eerlijk: geen functies beloven die er nog niet zijn, geen nep-reviews of nep-cijfers.
- Support altijd via support@dortus.com.

## Voorbeelden die we volgen (best beoordeelde plugins in Obsidian)

- **Dice Roller** (de voorganger van Rollwright): een uitkomst staat klein en rustig in de tekst, een klik rolt opnieuw. Dat overnemen: de gebruiker kent het al.
- **Tasks, Calendar, Style Settings**: gebruiken alleen variabelen van Obsidian en zien er daardoor in elk thema goed uit. Dat is onze norm.
- **JetBrains, ingebouwde talen**: kleuren alleen via `DefaultLanguageHighlighterColors` en een eigen kleurenpagina in Color Scheme, iconen in de lijnstijl van de nieuwe UI met een donkere versie, meldingen als balloon, nooit een dialoog. Zo ziet een plugin er in elk thema uit als een ingebouwde taal.
- **De ingebouwde instellingen van Obsidian**: korte namen, één zin uitleg, kopjes met `setHeading()`. Zo moeten onze instellingen ook lezen.
