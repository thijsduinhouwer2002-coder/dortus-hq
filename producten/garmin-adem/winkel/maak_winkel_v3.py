# Winkelbeelden Ebb v3 (besluit hoofdchat 11 nov 09:30 punt 3: nu, en eerlijk over het spel van nu).
# De oude beelden beloofden meters en dieren voor langer inhouden; het spel is nu dieren door trouw (besluit 10 nov 22:53).
# Bouwt op Mila's maak_winkel_mila.py (zelfde letters, kleuren, zee en horloge-uitsnede). Elk horloge is een echte opname
# uit de plaatjesbouw (simulator), niets bijgetekend op het scherm.
#   python3 maak_winkel_v3.py poster <inhouden-met-dier.png> <sea-log.png> <uit.png>
#   python3 maak_winkel_v3.py kaart <simulator.png> "<kop>" "<koraalwoord>" "<ondertekst>" <uit.png>
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw  # noqa: E402
import maak_winkel_mila as m  # noqa: E402


def poster(hoofd, klein, uit, W=1000, H=1000):
    """Eén beeld dat zegt wat Ebb is: ademrondes met inhouden, de zee, en zeevrienden die je vindt door terug te komen."""
    im = Image.new("RGB", (W, H), m.NACHT)
    d = ImageDraw.Draw(im)
    m.kop_met_koraal(d, W, H * 0.03, "Breathe. Hold. Find friends.", "friends", m.letter(800, int(H * 0.098)))
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


if __name__ == "__main__":
    a = sys.argv
    if a[1] == "poster":
        poster(a[2], a[3], a[4])
    elif a[1] == "kaart":
        m.kaart(a[2], a[3], a[4], a[5], a[6])
