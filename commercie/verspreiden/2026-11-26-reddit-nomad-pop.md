# r/NomadSculpting: antwoord op "How do I make a doll in nomadsculpt?" (Verspreider, run 16, 26 nov 2026)

Rooster A (plekken). Eén reactie van Thijs onder een bestaande vraag, geen eigen post. Heeft zijn ja op de tekst nodig (zijn account, CLAUDE.md regel 4). Reddit van Thijs: hooguit één ding per dag, dus **niet op vr 27 nov** (dan r/blender), maar **za 28 nov of later**, wanneer het hem uitkomt. Duur: ±2 min.

## Waarom deze plek
- De vraag is letterlijk ons product: "is it possible to make a 3d doll in nomad (that is posable)? I try to find tutorials but so far I found none" (DERDEN, https://www.reddit.com/r/NomadSculpting/comments/1xiach3/how_do_i_make_a_doll_in_nomadsculpt/, 29 okt 2026, flair Question, niet op slot, niet gearchiveerd, Arctic Shift 26 nov).
- De vier antwoorden geven geen stap-voor-stap. Eén zegt al "adapt from ones that use ZBrush or Blender", een ander "learn about tolerances", een derde gebruikt Inflate in Nomad voor speling (DERDEN, Arctic Shift comments-API, 26 nov). Ons antwoord vult precies dat gat: hoe je in Blender een kogel en kom met speling in millimetres uitsnijdt.
- Wie in de toekomst googelt op "posable doll nomad sculpt" komt op dit draadje uit (GOK). Een antwoord blijft staan; een post zakt weg.
- Publiek: r/NomadSculpting heeft 11.894 leden (DERDEN, Arctic Shift subreddits-API, 26 nov). Figuren printen gebeurt daar: "First Sculpt! (+3D print)" 101 punten, "Loudmouth, made with nomad and 3d printed" 85 punten (GEZIEN, Arctic Shift posts-API, okt en nov 2026).
- Regels (DERDEN, https://arctic-shift.photon-reddit.com/api/subreddits/rules?subreddits=NomadSculpting, 26 nov): Be Nice, **Keep it Relevant** ("only post about things related to Nomad Sculpt"), No URL shorteners, No Pirating. Geen verbod op eigen werk of links; makers delen er hun Gumroad-spullen (Free Nomad Sculpt hair tube, 42 punten, GEZIEN). Ons antwoord gaat over een sculpt uit Nomad en noemt de route vanuit Nomad, dus past bij "relevant". Daarom bewust geen eigen post: een post over een Blender-add-on is daar niet relevant genoeg.
- Bewust geen link naar Pro, geen prijs, geen sale: het gratis deel beantwoordt de vraag. Pro staat één klik verder op de pagina van de gratis versie. Zo leest het als hulp, niet als reclame.
- Verwacht: 0 tot 5 downloads van de gratis versie en 0 tot 1 verkoop in twee weken (GOK). Klein, maar het kost Thijs 2 minuten en het draadje blijft vindbaar.

## Wat Thijs doet
1. Open https://www.reddit.com/r/NomadSculpting/comments/1xiach3/how_do_i_make_a_doll_in_nomadsculpt/
2. Lees de regels rechts (±1 min). Staat er nu iets tegen links naar eigen werk of tools: niet plaatsen, één regel aan de hoofdchat.
3. Plak de tekst hieronder als reactie op de post zelf (niet onder een ander antwoord). Geen beeld nodig.

## Reactie (Engels, om te kopiëren)
```
Late reply, but in case anyone finds this thread later: Nomad doesn't have a joint tool, so the usual route is to sculpt the doll as one piece (or with separate limbs), export it as OBJ or STL, and cut the joints in Blender.

Full disclosure, I'm one of the makers: we made a free Blender add-on for exactly this step, Click Joints. You put the 3D cursor where the joint goes (shoulder, elbow, hip, knee), click Place joint, and it cuts the mesh into two closed parts with a ball and socket or a pin, with the clearance you set in millimetres. It also shows how far each ball joint can bend before the parts hit, so you see it before you print.

https://extensions.blender.org/add-ons/click-joints/

Tips that count whatever tool you use:
- Thicker limbs make joints easier. A ball needs a wall of about 1.5 mm or more around it, so very thin arms on a small doll won't fit one.
- Print a small test joint first: every printer is different. The right gap for FDM and resin is not the same.
- Keep the sculpt closed (no holes) before you cut. A voxel remesh in Nomad usually takes care of that.
```

## Als iemand reageert (Thijs plakt alleen als de vraag komt)
- **"Is it really free?"**
```
Yes, free and open source on Blender Extensions. There's also a paid version with hinges for elbows and knees and a fit test strip, but the free one does ball and pin joints.
```
- **"Can't I do this in Nomad?"**
```
You can get close with booleans and Inflate for the gap, like someone said above. The add-on just does the cut, the gap and the bend check in one click, and tells you when a wall gets too thin.
```

## Feiten en bron (GEZIEN 26 nov ±04:10 NL, curl)
- Gratis versie: "Set the 3D cursor where the joint goes, click Place joint, and Click Joints cuts the mesh into two watertight parts with a ball and socket or a pin, sized with the clearance your printer needs, in millimetres"; "measures how far the joint bends before the parts collide"; "Tight: wall 0.89 mm (aim for 1.5 mm or more)"; eerste zin "Turn a sculpt into an articulated, poseable figure for 3D printing, such as ... a doll" (https://extensions.blender.org/add-ons/click-joints/). Open source: GPL, code op GitHub (besluiten, Hackaday-tekst run 7).
- Pro: hinges met end stop en de Fit test strip "are in Pro only" (live Gumroad-pagina).
- Nomad exporteert OBJ en STL; voxel remesh in Nomad: algemene kennis van het programma, geen claim over ons product. Bewust niet genoemd: de nieuwe Blender-koppeling van Nomad (alleen één Reddit-post als bron, 1xj0267, niet zelf nagekeken).
- Niet beweerd: dat wij printten, dat het klikt, dat het een pose houdt. Geen AI, geen "not print tested".

## Meten
Gratis versie stond op 397 downloads (GEZIEN, extensions.blender.org, 26 nov ±04:00 NL). Geen ?van= mogelijk op een extensions-link; meten via de dagstijging rond de plaatsdatum en of iemand op de reactie antwoordt.
