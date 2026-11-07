# Nog te onderzoeken

Kies er één per run. Vind je zelf een betere, zet hem erbij.

- Shopify vervolg A: hoe haalt een gewone nieuwe app zijn eerste 100 installs, en hoe vaak lukt dat (bericht Thijs 6 nov 20:32). Klaar 7 nov run 07:31: gevoel Thijs klopt, ±2 tot 6 van de 100 nieuwe apps haalt 100 installs in 2 tot 6 maanden, cijfer blijft 6, zie voorstellen/shopify.md
- Shopify vervolg B: aankomende EU-regel of Shopify-functie met datum zoeken (zie voorstellen/shopify.md). Deel 1 klaar 7 nov 08:05 (garantielabel-golf gemeten, ±60 apps, mediaan 0, top 50 reviews, nagekeken). Vrij voor de volgende run: deel 2 is e-facturen Duitsland 2027/2028 (alleen B2B) en scripttags 1 maart 2027, daarna oordeel 6 of 5
- Framer: klaar 6 nov, nee voor nu (cijfer 4), zie onderzocht.md
- Discord: klaar 6 nov run 21:31, eigen meting via de open API van de App Directory, nee voor nu (cijfer 5), zie onderzocht.md. Herhaalmeting kan over 4 weken met data/discord-haal-script.py

- Garmin Connect IQ: klaar 6 nov, nog niet klaar (cijfer 5). Vervolg: 3 tot 4 weken elke week de download-emmers van betaalde apps volgen met data/garmin-haal-script.py, zie voorstellen/garmin-connect-iq.md
- Fab (Epic, Unreal): klaar 6 nov run 22:31, eigen meting van 4.108 tools, nee voor nu (cijfer 3), zie onderzocht.md. Herhaalmeting kan met data/fab-zoek-script.py en fab-haal-script.py
- Modrinth (Minecraft-mods, makers krijgen geld uit advertentie-inkomsten, open API met downloads): klaar 7 nov run 08:31, eigen meting van 23.600 mods, nee (cijfer 3), zie onderzocht.md. Bereik top, geld bijna nul: verkopen verboden door EULA
- BuiltByBit en Polymart (betaalde Minecraft-serverplugins): klaar 7 nov run 09:31, eigen meting van 903 Polymart-producten via open API, nee (cijfer 2), zie voorstellen/builtbybit-polymart.md. BuiltByBit zelf alleen te meten met een account en API-sleutel
- Blender geld (taak Hans 6 nov): klaar 7 nov run 10:31, eigen meting op Superhive (verkooptellers op 3.166 pagina's), nu ja (cijfer 7), zie voorstellen/blender.md. Herhaalmeting over 4 weken met data/superhive-haal-script.py
- Foundry VTT (modules, betaald via de Patreon-koppeling van Foundry), zelf toegevoegd 7 nov: route (c) klaar 7 nov run 15:32: nee, cijfer 3, zie voorstellen/foundry-vtt.md. Eerder klaar 7 nov run 11:31, eigen meting van 9.360 modules via de Forge Bazaar en 23 Patreon-makers, nog niet klaar (cijfer 6), zie voorstellen/foundry-vtt.md. Hangt af van Thijs (AI-regels van Foundry, zie lijst Thijs)
- Fantasy Grounds Forge (betaalde extensies voor de tafelsoftware Fantasy Grounds), zelf toegevoegd 7 nov: klaar 7 nov run 11:31, eigen meting van 3.189 items, nee voor nu (cijfer 4), zie voorstellen/fantasy-grounds-forge.md. Herhaalmeting met data/fgforge-haal-script.sh
- Google Workspace Marketplace (add-ons voor Sheets, Docs, Gmail), opnieuw: klaar 7 nov run 12:31, eigen meting van 5.865 add-ons, nee voor nu (cijfer 5), zie voorstellen/google-workspace.md. Herhaalmeting over 4 weken met data/gwm-zoek-script.py geeft een echte lijst nieuwe add-ons
- Wix App Market (betaalde apps via Wix, op 6 nov niet te meten, nu leesbaar): klaar 7 nov run 13:31, eigen meting van 1.818 apps, nee voor nu (cijfer 3), zie voorstellen/wix.md. Herhaalmeting met data/wix-haal-script.py en wix-reviewdata-script.py
- TradingView (Pine Script-indicatoren, makers verkopen invite-only scripts), zelf toegevoegd 7 nov 13:52: niet zelf te meten, robots.txt van TradingView verbiedt AI-agents (ClaudeBot, ChatGPT-User) /scripts/ en /u/. Alleen met bronnen van derden te doen, of met toestemming
- Autodesk App Store (apps voor AutoCAD, Revit, Fusion, Inventor; betaalde apps in de winkel), zelf toegevoegd 7 nov: klaar 7 nov run 15:32, eigen meting van 5.055 apps, nog niet klaar (cijfer 4), zie voorstellen/autodesk.md. Vervolg: reviews per app tellen (browser of toestemming voor de API)
- aescripts.com (scripts voor After Effects, kleine makers verkopen): zelf toegevoegd 7 nov, geeft 403 op curl, niet te meten zonder browser
- SketchUp Extension Warehouse (betaalde extensies van kleine makers, ook via SketchUcation), zelf toegevoegd 7 nov: 7 nov run 16:33 niet zelf te meten. De winkel is een app in de browser die zijn cijfers (met downloads en datum per extensie, 1.429 stuks) uit een interne API haalt; die API lezen weigerde de veiligheidscontrole, net als bij Autodesk. SketchUcation verbiedt ClaudeBot in robots.txt. Toestemming gevraagd op lijst Thijs
- WooCommerce Marketplace (betaalde extensies op woocommerce.com, Woo verkoopt en betaalt de maker uit; productpagina's tonen installaties en publicatiedatum), zelf toegevoegd 7 nov: klaar 7 nov run 16:33, eigen meting van alle 1.562 productpagina's, nee (cijfer 2), zie voorstellen/woocommerce-marketplace.md. Herhaalmeting met data/woo-haal-script.py en woo-analyse-script.py
- BigCommerce App Marketplace (betaalde apps): in onderzoek 7 nov 17:50 (app-pagina heeft createdOn). Voorwerk 7 nov run 16:33: bereikbaar met curl, sitemap op /apps/sitemap-marketplace-apps.xml, pagina's tonen alleen reviewCount en rating, geen installs en in de lijst geen datum. Eerst uitzoeken of een app-pagina een datum heeft; anders alleen reviews te meten, zoals bij Wix
- Squarespace Extensions en Ecwid App Market: bereikbaar met curl, nog niet bekeken (Ecwid toont mogelijk installs). Ecwid 7 nov 17:47 bekeken: niet te meten, de pagina /apps bevat alle 474 apps maar zonder installs, datum of reviews; reviews komen er pas na laden via een script. Pebble (Core Devices, Rebble-winkel) 7 nov genoteerd: alleen gratis apps, geen betaling gevonden
- Craft CMS Plugin Store (betaalde plugins, Craft verkoopt en betaalt de maker uit, open API met installs), zelf toegevoegd 7 nov: klaar 7 nov run 17:32, eigen meting van alle 1.670 plugins via open API, nee voor nu (cijfer 4), zie voorstellen/craft-cms.md. Herhaalmeting rond feb 2027 (Craft 6) met data/craft-meting-script.py
- Statamic Marketplace (betaalde addons voor het Laravel-CMS Statamic, open API), zelf toegevoegd 7 nov: klaar 7 nov run 17:32, eigen meting van alle 645 addons plus Packagist, nee (cijfer 2), zie voorstellen/statamic.md
- Zotero (plugins)
- Anki (add-ons)
- Thunderbird (add-ons, makers als SmartTemplates verkopen Pro-licenties): klaar 7 nov run 13:31, eigen meting van 2.282 extensies, nee (cijfer 3), zie voorstellen/thunderbird.md. Herhaalmeting met data/thunderbird-haal-script.py
- Firefox (add-ons): klaar 7 nov run 13:31, eigen steekproef van 6.000, nee (cijfer 1), zie voorstellen/firefox.md
- Home Assistant (integraties via HACS, opnieuw met andere telling)
- Miro (apps)
- Slack (apps)
- Sketch (plugins)
- Zapier en Make (integraties)
- Neovim (plugins)
- Open VSX (Cursor, Windsurf): klaar 7 nov run 12:31, eigen steekproef van 2.500 extensies via open API, nee voor nu (cijfer 4), zie voorstellen/open-vsx.md. Herhaalmeting met data/openvsx-haal-script.py
- Trello (opnieuw: bereik was onbekend)
- Roblox Creator Store: klaar 6 nov, nog niet klaar (cijfer 4), zie onderzocht.md
- Unity Asset Store: klaar 6 nov run 22:31, eigen meting, nee voor nu (cijfer 3), zie onderzocht.md. Herhaalmeting kan met data/unity-haal-script.py
