# Click Joints Pro: alinea "After you buy" op Gumroad (Bram, 26 nov 2026, issue #178)

**Waarom (geld):** wie in de sale op Gumroad koopt en de gratis Click Joints al heeft, installeert Pro ernaast. In 1.2.8 kunnen die twee niet tegelijk aan; de koper krijgt een fout en zoekt zelf uit waarom, en waar het paneel zit. Dat is een kans op een terugbetaling of een slechte eerste indruk. Effect op verkoop: GOK, klein; vooral minder afhakers en vragen.

**Gat (GEZIEN, curl 26 nov 22:10 NL):**
- Gumroad-pagina Pro (https://duinhouwer8.gumroad.com/l/click-joints-pro): geen woord over installeren, de gratis versie of de zijbalk.
- Superhive Docs-tab (https://superhivemarket.com/products/click-joints-pro/docs): "Getting started" met Install, "Coming from the free version" en "Open the panel".
- Na het kopen op Gumroad: de zip heeft geen leesmij (inhoud `producten/blender-gewrichten/click_joints/`, GEZIEN). De tekst voor de inhoudspagina (`commercie/verspreiden/2026-11-26-eigen-mensen.md` deel 2, nog niet geplaatst) noemt installeren, maar niet de gratis versie en niet de zijbalk.

**Bron van de woorden:** letterlijk de Docs-tab van Superhive (live, klopt met 1.2.8). Alleen "from your Superhive download" wordt "from your Gumroad library", gelijk aan de regel "Already bought Pro?". Paneeltab "Click Joints" en naam van de gratis "Click Joints" nagekeken in de code (`paneel.py` regel 70, `blender_manifest.toml`, GEZIEN).

## Plakken A: Gumroad, product Click Joints Pro, beschrijving

Zet dit direct boven de regel "Already bought Pro? ..." (dus onder "Clearance 0.2 mm by default."). "After you buy" als kopje (H3 of vet), de drie regels als opsomming:

```
After you buy
- Install: in Blender 4.2 or newer, go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right and choose Install from Disk. Pick click_joints_pro-1.2.8.zip from your Gumroad library (do not unzip it).
- Coming from the free version: turn the free one off first. In Edit > Preferences > Add-ons, search "Click Joints" and untick "Click Joints" (not "Click Joints Pro"). Your joints and settings stay in the .blend file.
- Open the panel: in the 3D viewport press N and open the Click Joints tab.
```

## Plakken B: Gumroad, Click Joints Pro, Content-tab (inhoudspagina, boven de zip)

Bij het plaatsen van deel 2 uit `commercie/verspreiden/2026-11-26-eigen-mensen.md`: vervang daar regel "1. In Blender, go to Edit > Preferences > Add-ons > Install from Disk and pick the zip below." door deze drie regels, de rest van deel 2 blijft gelijk:

```
1. Install: in Blender 4.2 or newer, go to Edit > Preferences > Get Extensions, open the drop-down menu at the top right and choose Install from Disk. Pick the zip below (do not unzip it).
   Coming from the free version? Turn it off first: in Edit > Preferences > Add-ons, search "Click Joints" and untick "Click Joints" (not "Click Joints Pro").
   Then press N in the 3D viewport and open the Click Joints tab.
```

Na het plakken met curl nakijken dat "After you buy" en "Click Joints tab" op de Pro-pagina staan (`bash platformen/blender/sale-controle.sh` stap 6 kijkt alleen naar het versieblok).

**Na 1.2.9:** 1.2.9 zet de gratis zelf uit (ontwerp.md). Dan wordt regel 2 van A en B: "Coming from the free version? Pro turns it off for you." Dat gaat mee in de keuring van 1.2.9.

## Stand
- 26 nov 22:20 NL: concept klaar, keuring gevraagd aan Daan in #226.
