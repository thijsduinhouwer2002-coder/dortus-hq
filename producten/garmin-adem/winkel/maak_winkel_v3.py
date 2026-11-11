# Winkelbeelden Ebb v3 (besluit hoofdchat 11 nov 09:30 punt 3: nu, en eerlijk over het spel van nu).
# De oude beelden beloofden meters en dieren voor langer inhouden; het spel is nu dieren door trouw (besluit 10 nov 22:53).
# Bouwt op Mila's maak_winkel_mila.py (zelfde letters, kleuren, zee en horloge-uitsnede). Elk horloge is een echte opname
# uit de plaatjesbouw (simulator), niets bijgetekend op het scherm.
#   python3 maak_winkel_v3.py poster <inhouden-met-dier.png> <sea-log.png> <uit.png>
#   python3 maak_winkel_v3.py kaart <simulator.png> "<kop>" "<koraalwoord>" "<ondertekst>" <uit.png>
#   python3 maak_winkel_v3.py alles <map met <horloge>-scene<k>.png> <uitmap> [groot=fenix847mm] [klein=fr255]
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw  # noqa: E402
import maak_winkel_mila as m  # noqa: E402


def poster(hoofd, klein, uit, W=1000, H=1000):
    """Eén beeld dat zegt wat Ebb is: ademrondes met inhouden, de zee, en zeevrienden die je vindt door terug te komen."""
    im = Image.new("RGB", (W, H), m.NACHT)
    d = ImageDraw.Draw(im)
    m.kop_met_koraal(d, W, H * 0.03, "Breathe. Hold. Find friends.", "friends", m.letter(800, int(H * 0.088)))
    d.text((W / 2, H * 0.150), "Breath-hold rounds and calm breathing on your watch.", font=m.letter(500, int(H * 0.040)), fill=m.WIT, anchor="mt")
    d.text((W / 2, H * 0.200), "Come back, and the sea gives you a new friend: 24 to find.", font=m.letter(500, int(H * 0.040)), fill=m.TEAL, anchor="mt")
    # groot horloge: inhouden met je dier; klein horloge rechts ervoor: de sea log
    top, h = int(H * 0.285), int(H * 0.70)
    w = m.horloge(hoofd, h)
    x = (W - w.width) // 2 - int(W * 0.10)
    im.paste(w, (x, top), w)
    k = m.horloge(klein, int(H * 0.46))
    im.paste(k, (W - k.width - int(W * 0.015), top + int(H * 0.15)), k)
    m.zee(im, top + h * 0.80)
    d = ImageDraw.Draw(im)
    d.text((W / 2, H * 0.985), "One payment  ·  no subscription  ·  no account", font=m.letter(700, int(H * 0.034)), fill=m.WIT, anchor="mb")
    m.bewaar(im, uit)


# Kaarten v3: scène in de plaatjesbouw (Scenes.mc), bestandsnaam, kop, koraalwoord, ondertekst.
KAARTEN = [
    (2, "1-hold.png", "Hold while easy.", "easy", "The sea darkens. Your sea friend swims along."),
    (17, "2-new-friend.png", "A new friend.", "friend", "For sessions and weeks in a row, not long holds."),
    (4, "3-sea-log.png", "Your sea log.", "sea", "24 sea friends to find, and one bonus."),
    (7, "4-calm.png", "Calm 4-7-8.", "Calm", "Breathe in 4, hold 7, out 8, drawn as water."),
    (25, "5-sea-complete.png", "Sea complete.", "complete", "Find all 24 and the whole sea comes to celebrate."),
]


def alles(bron, uitmap, groot="fenix847mm", klein="fr255"):
    # De poster in de winkel is Mila's ontwerp (blad v10): python3 ontwerp/garmin/bron/poster_v3.py <s2> 0-poster-v3.png.
    # poster() hieronder is mijn eerdere proef en schrijft alleen nog 0-poster-proef.png.
    p = lambda h, k: os.path.join(bron, f"{h}-scene{k}.png")
    poster(p(groot, 2), p(klein, 4), os.path.join(uitmap, "0-poster-proef.png"))
    for k, naam, kop, koraal, onder in KAARTEN:
        # Sea complete als groepsfoto (blad v10) staat sinds 7209317 ook op 454 binnen de opnametijd.
        h = groot
        if os.path.exists(p(h, k)):
            m.kaart(p(h, k), kop, koraal, onder, os.path.join(uitmap, naam))
        else:
            print("ONTBREEKT", p(h, k))


if __name__ == "__main__":
    a = sys.argv
    if a[1] == "poster":
        poster(a[2], a[3], a[4])
    elif a[1] == "alles":
        alles(*a[2:])
    elif a[1] == "kaart":
        m.kaart(a[2], a[3], a[4], a[5], a[6])
