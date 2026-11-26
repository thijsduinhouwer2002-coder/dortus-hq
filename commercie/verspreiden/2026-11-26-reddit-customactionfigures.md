# r/customactionfigures: vraagpost over gewrichten, ma 30 nov (Verspreider, run 25, do 26 nov 2026, A)

**Status:** keuring Daan (#181). Na zijn ja: onderaan `berichten/hoofdchat.md` voor Thijs (ma 30 nov).

Rooster A (plekken). Eén eigen post van Thijs (zijn Reddit-account, zijn ja op de tekst, CLAUDE.md regel 4). Vervangt tekst 8 in `commercie/blender-click-joints/plekken-boost-2026-11-20.md`: die zei nog "We haven't print tested it yet" (mag niet meer sinds 24 nov 15:32, besluiten regel 20), ging over Pro 1.1 en een oude render. Niets geplaatst, niemand benaderd.

**Wanneer:** ma 30 nov, op een tijd die Thijs uitkomt (Reddit van Thijs: hooguit één ding per dag; vr 27 r/blender, za 28 r/NomadSculpting, zo 29 Blender Artists). Ma 30 nov is de voorlaatste saledag, dus wie in de reacties naar de tool vraagt, krijgt de korting nog. Duur voor Thijs: ±3 minuten.

## Waarom deze plek
- **Publiek:** 33.449 leden (DERDEN, Arctic Shift subreddits-API, opgehaald 26 nov ±12:45 NL: https://arctic-shift.photon-reddit.com/api/subreddits/search?subreddit=customactionfigures). Mensen die figuren aanpassen en steeds vaker zelf delen printen.
- **Regels:** de enige regel is "don't be evil" (niet spotten met beginners). De zijbalk zegt letterlijk: "Post pictures/videos of custom figures you like, or that you made, or that you're selling. Also let's talk about different ways to make them. And like tools and materials or whatever." (DERDEN, Arctic Shift rules- en subreddits-API, 26 nov). Praten over gereedschap mag dus uitdrukkelijk.
- **Vraag naar ons onderwerp is er nu:** in de laatste 100 posts (22 tot 26 nov, GEZIEN, Arctic Shift posts-API):
  - "How do you make 3d printed parts fit?" (25 nov, 1 antwoord: "measure the neck peg with a digital caliper, then make a hole in my sculpt with a sphere").
  - "How could I give this guy butterfly joints and a gi joe waist?" (25 nov, 18 reacties).
  - "the leg joint of my robot spirits rx78 broke on me" (24 nov).
  - "3D printable action figures" (24 nov, 215 punten, de best scorende post van die 100): een platform met printbare figuurdelen.
- **Waarschuwing uit dezelfde post:** de best gewaardeerde reactie daaronder (23 punten) is "this sub is just a giant advertisement space now" (GEZIEN, Arctic Shift comments-API). Daarom: een echte vraag aan de lezers, open zeggen dat wij de tool maken, geen link en geen prijs in de post, en eerlijk zeggen wat hij niet kan. Een link alleen als iemand erom vraagt.
- **Wat het ons oplevert naast verkoop:** antwoorden op "welke gewrichten breken het eerst" en "welk gewricht wil je dat een tool voor je maakt" zijn bruikbaar voor de Pro-lat en voor Click Cuts (butterfly joints en taille staan nergens in Pro; dat vragen we eerlijk als vraag, we beloven niets).
- **Verwacht:** 0 tot 2 verkopen en 0 tot 10 downloads van de gratis versie (GOK). Klein, maar het kost Thijs 3 minuten, en de antwoorden zijn gratis onderzoek bij precies ons publiek.

## Beeld
`ontwerp/pro-galerij/beelden/bereik-1920x1080.jpg` ("Every joint knows its limit", robot met bereik per gewricht en de knie van dichtbij). GESLAAGD in de blinde test: `organisatie/blindtest/uitslag/click-joints-pro-galerij-knie-2026-11-25-0859.md`. Het is een render uit Blender van onze eigen robot; de post zegt dat ook.

Bewust niet: het hoofdbeeld met "Rig in. Joints out." (leest op deze sub als advertentie, GOK) en de schermopname `commercie/blender-click-joints/reddit-pro-buig-11s.mp4` (eerlijker beeld, maar het eerste beeld van die video staat niet GESLAAGD in de blinde test, dus mag niet naar een klant, CLAUDE.md regel 9).

## Voor Thijs: zo plaats je hem
1. Ga naar https://www.reddit.com/r/customactionfigures/submit en kies **Images**.
2. Upload `bereik-1920x1080.jpg` (pad hierboven).
3. Flair: niet verplicht; kies er geen, of "user generated" als Reddit erom vraagt.
4. Plak de titel en de tekst hieronder.
5. Vraagt iemand naar de tool of de prijs: plak de reactie onderaan. Anders niets plakken.

**Titel**
```
We make a Blender add-on that cuts printable hinges and ball joints into figures. Which joints break first on yours?
```

**Tekst**
```
We make Click Joints, a Blender add-on for people who design their own printable figures or printed parts for customs. The picture is a render from Blender of our test robot: every elbow and knee gets a hinge with an end stop, so it bends one way and not backwards, and the shoulders, hips and neck get ball joints. You see how far each joint bends, in degrees, before you print.

What it can't do: on thin limbs, like a realistic figure around 150 mm, there's no room for a hinge in the arms, so it skips that joint and tells you why. It works best on figures about 200 mm and up with separate arms and legs.

So a question for people here who print or customize figures:
1. Which joints break or wear out first on yours?
2. Is there a joint you'd want a tool to cut for you that isn't a ball or a hinge? (I saw the butterfly joint and waist questions here this week.)

Whatever you use: print a small fit test with a few clearances before the real parts. Every printer is different.
```

**Reactie, alleen als iemand vraagt welke tool het is, wat hij kost of waar je hem haalt**
```
The free version (ball and pin joints, one at a time) is on Blender Extensions: https://extensions.blender.org/add-ons/click-joints/

The hinges with end stops and the one-button "whole rigged figure" are in Click Joints Pro, 25% off until December 1: https://dortus.com/click-joints/?van=caf

There's also a free fit test strip (five ball joints from 0.10 to 0.30 mm clearance) on Printables: https://www.printables.com/model/1929497-ball-joint-tolerance-test-010-to-030-mm
```

**Reactie, als iemand vraagt of wij het geprint hebben** (eerlijk, zonder "not print tested")
```
Good question. What you see is measured in Blender: the clearance, the wall thickness next to the socket and the bend range. That's why the fit test strip exists: print it first, because every printer is different. If you print one, I'd love to see how it comes out.
```

## Nagekeken (GEZIEN, curl, 26 nov ±12:50 NL)
- Live Gumroad-pagina Pro: "a hinge at every elbow and knee that stops where your rig stops, and a ball joint at the shoulders, hips and neck", "You see how far each joint bends, in degrees, before you print", "Works best on figures with separate arms and legs, at about 200 mm tall or more. On a realistic figure at 150 mm the arms are too thin for a hinge; the list says so", "Try it free first: the free Click Joints on Blender Extensions makes ball and pin joints, one at a time", "Hinges with end stops, Figure from rig and the Fit test strip are in Pro only".
- dortus.com/click-joints/?van=caf geeft 200 en linkt naar Gumroad Pro. Printables geeft 403 met curl (Cloudflare); de link staat al in gekeurde bundels (#122, #155).
- CYBER25 loopt van vr 27 nov t/m di 1 dec ("until December 1" klopt op ma 30 nov).
- Geen AI, geen "not print tested", geen bewering dat het klikt of dat wij printten, geen persoonsgegevens.

## Meten
`?van=caf` op dortus.com/click-joints/ (Umami), downloads gratis versie (extensions.blender.org), Gumroad-verkopen 30 nov en 1 dec, en het aantal reacties met een echt antwoord op de vraag. Na 14 dagen zonder bezoek of antwoord: deze sub valt af.
