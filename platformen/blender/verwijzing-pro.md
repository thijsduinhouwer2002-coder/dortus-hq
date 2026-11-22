# Verwijzing van gratis Click Joints naar Pro (Bram, 15 nov 2026 22:20 UTC)

Opdracht: hoofdchat 15 nov 23:10 NL in `berichten/bram.md` (groeiplan Thijs 23:05): een regel onderaan het paneel "Need hinges with an end stop? Click Joints Pro" met een knop naar dortus.com/click-joints/, eerst nagaan of de regels het toestaan.

## Wat de regels zeggen (GEZIEN 15 nov 22:11 UTC met curl, https://extensions.blender.org/terms-of-service/, "Last updated: 10 August 2026")

> (6.1) Advertisements (links to commercial and funding websites, donation buttons, images or text labels prompting users to purchase anything) are not allowed inside the Blender UI. Linking to external funding platforms is allowed on the platform (in the extension's description).

> (6.2) The description and images on the platform should only showcase features that are available in the version that is available on the platform. Showcasing features from commercial versions will be considered an advertisement and is not allowed.

> (6.3) Extension must not use Blender's UI elements to promote its updates, commercial versions, or other extensions.

## Besluit Bram: geen regel of knop in het paneel, en Pro ook niet in de beschrijving op extensions.blender.org

- Een regel "Click Joints Pro" met knop in het paneel is precies wat 6.1 en 6.3 verbieden ("text labels prompting users to purchase anything", "promote its commercial versions"). Dat de knop naar dortus.com gaat en niet naar Superhive maakt geen verschil: het label zelf is de reclame.
- In de beschrijving op de site mag alleen een link naar een "funding platform" (doneren). Pro met zijn scharnier noemen is "showcasing features from commercial versions" (6.2). Dus ook daar niet.
- Waarom ik dit niet "toch even probeer": de gratis versie is ons bereik (141 downloads op 15 nov 22:11 UTC, 0 reviews). Een afkeuring van een nieuwe versie of een waarschuwing kost meer dan een verwijzing oplevert, en Chris' lanceerplan leunt op die listing. Daarom bouw ik ook geen tak met de knop: die zou nooit uit mogen.

## Wat wel mag, en al staat

- Het manifest van de gratis versie heeft `website = "https://dortus.com/click-joints/"`. Dat is het standaardveld "Website" op de listing en bij de add-on in Blender (Voorkeuren, Add-ons, uitklappen). Geen tekst van ons die tot kopen aanzet, dus geen reclame in de zin van 6.1. Geen nieuwe versie nodig.
- Dus loopt de verwijzing zo: listing of Blender, dan dortus.com/click-joints/, en **op die pagina** staat Pro. Die pagina is van ons en valt niet onder de regels van extensions.blender.org.
- Andersom mag alles: Superhive noemt de gratis versie al in de FAQ (`commercie/blender-click-joints/winkeltekst.md`).

## Klaargezet voor Chris (dortus.com is van Chris; pas zetten als Pro live is, de hoofdchat geeft het teken)

1. **Verouderd op dortus.com/click-joints/ (GEZIEN 15 nov 22:11 UTC):** "Version 0.1.0, free. On its way to Blender Extensions." Click Joints staat sinds 10 nov live. Dit mag nu al weg, los van Pro: "Version 0.1.0, free, on Blender Extensions."
2. **Blok Pro op dortus.com/click-joints/**, onder "What you get, free" (Engels, alleen wat in Pro 1.0.1 zit en getest is in Blender 4.2, 5.2 en 5.3):

   > **Need a knee or elbow that stops?** Click Joints Pro adds a printable click hinge with an end stop: it bends from 0° to 115° and stops there, instead of flopping backwards. Drag the pose slider and see the range in degrees before you print; bend past the stop and the parts that collide turn red. Pro includes everything from the free version.
   > [Get Click Joints Pro on Superhive →] (https://superhivemarket.com/products/click-joints-pro)
   >
   > *Beeld: `click-joints-pro-demo.gif` uit release `click-joints-pro-film-v1` (6,7 s, echte Blender).*

   Prijs niet op dortus.com zetten: die verandert (lanceerprijs $9 voor 14 dagen, daarna $12) en staat op Superhive.
3. **README van de repo click-joints** (de link "Report issues" op de listing wijst ernaar; GitHub valt ook niet onder de regels), onderaan:

   > ## Click Joints Pro
   > Need hinges with an end stop for knees and elbows? [Click Joints Pro](https://dortus.com/click-joints/) adds a click hinge that bends 0° to 115° and stops there. The free version stays free and complete.

   Pushen naar click-joints doe ik zelf als die repo in mijn run gekoppeld is, anders Chris of de hoofdchat.

## Wat het zou veranderen
Verandert de regel 6 op extensions.blender.org (datum boven aan de pagina is nu 10 aug 2026), of zegt een moderator schriftelijk dat een knop naar de eigen site mag, dan bouw ik de regel in het paneel alsnog op een tak.

## Bijwerking 22 nov 2026 ±16:10 UTC, Bram: smalle weg, één steunzin onderaan de beschrijving

Aanleiding: Afkijker 22 nov ±14:35 UTC (`platformen/ideeen/afkijken-2-2026-11-21/doorlopend/2026-11-22-univ-en-texel-steunlink.md`). Regel 6 opnieuw gelezen met curl op 22 nov ±16:05 UTC, nog steeds "Last updated: 10 August 2026" (GEZIEN). Het besluit van 15 nov wordt hiermee smaller, niet omgegooid.

**Bewijs dat dit op extensions.blender.org gebeurt en blijft staan (DERDEN, uit het rapport van Afkijker):**
- UniV (Oxicid, 114.785 downloads): "The addon is free, but you can support the author and purchase this addon from Blender Marketplace".
- Texel Density Checker (Ivan Vostrikov, 114.087 downloads): kopje "Sponsorship" met links naar Superhive en Gumroad.
Beide noemen geen betaalde functies.

**Wel (mag volgens 6.1, tweede zin):** één zin met link onderaan de beschrijving op de site, onder "Support: thijs@dortus.com":

> Click Joints is free and stays free. If it saves you time, you can support development by buying Click Joints Pro on Gumroad: https://duinhouwer8.gumroad.com/l/click-joints-pro

Link gecontroleerd 22 nov ±16:05 UTC: 200, titel "Click Joints Pro for Blender" (GEZIEN).

**Nog steeds niet:**
- Niets in het paneel of elders in Blender (6.1 eerste zin, 6.3).
- Geen functies van Pro in de beschrijving of de beelden: geen scharnier, geen eindstop, geen hoeken (6.2). Alleen de naam en de link.
- Geen prijs (verandert, staat op Gumroad).
- Geen nieuwe versie nodig: de beschrijving staat op de beheerpagina van de extensie, die alleen met het account kan. De hoofdchat plakt hem na keuring van Daan.

**Wat het zou veranderen:** haalt een moderator de zin weg of waarschuwt hij, dan gaat hij er meteen af en geldt weer alleen het veld Website.
