from PIL import Image
S = '/tmp/claude-0/ebbgif/src/'
FPS = 12
N = 600


def L(n):
    return Image.open(S + n + '.png').convert('RGB').crop((20, 150, 693, 823)).resize((N, N), Image.LANCZOS)


seq = [('menu-krab', 1.2), ('fade', 'sessie-krab-in-dag', 0.4), ('sessie-krab-in-dag', 0.6),
       ('fade', 'sessie-krab-uit-dag', 1.3), ('sessie-krab-uit-dag', 0.4),
       ('fade', 'sessie-krab-in-dag', 1.3), ('sessie-krab-in-dag', 0.4),
       ('fade', 'sessie-krab-uit-dag', 1.3), ('sessie-krab-uit-dag', 0.3),
       ('fade', 'sessie-krab-hold-dag', 0.6), ('sessie-krab-hold-dag', 2.2),
       ('fade', 'einde-6b', 0.5), ('einde-6b', 2.2), ('fade', 'sealog-2', 0.5), ('sealog-2', 1.6)]
fr = []
cur = None
for s in seq:
    if s[0] == 'fade':
        nxt = L(s[1])
        k = int(s[2] * FPS)
        for i in range(1, k + 1):
            t = i / k
            t = t * t * (3 - 2 * t)
            fr.append(Image.blend(cur, nxt, t))
        cur = nxt
    else:
        cur = L(s[0])
        fr += [cur] * int(s[1] * FPS)
for i, f in enumerate(fr):
    f.save(f'/tmp/claude-0/ebbgif/frames/f{i:04d}.png')
print(len(fr), len(fr) / FPS, 's')
