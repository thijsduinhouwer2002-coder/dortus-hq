# Mila 10 nov: de geluidjes van Het Hol, zelf gemaakt in code (geen licentie nodig, van ons, past bij de pixels).
# Olaf 01:40: "een paar korte geluidjes (val, hap, munten), standaard uit; Mila kiest de klank".
# Klank: zacht en rond (sinus en driehoek, geen scherpe blokgolf), kort, piek -9 dB: dit klinkt naast je werk, niet in een arcadehal.
# Uit: producten/steam-hol/godot/geluid/*.wav (22050 Hz, mono, 16 bit), plus een plaatje van de golfvormen om na te kijken.
import os, wave
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
UIT = os.path.join(R, "producten", "steam-hol", "godot", "geluid"); os.makedirs(UIT, exist_ok=True)
SR = 22050
rng = np.random.default_rng(7)

def t_(sec): return np.arange(int(sec * SR)) / SR
def sweep(f0, f1, sec, vorm="sin", kromme=1.0):
    t = t_(sec); x = (t / sec) ** kromme
    f = f0 + (f1 - f0) * x
    fase = 2 * np.pi * np.cumsum(f) / SR
    if vorm == "tri": return 2 / np.pi * np.arcsin(np.sin(fase))
    return np.sin(fase)
def env(n, a=0.004, d=None, sec=None):
    t = np.arange(n) / SR; sec = sec or n / SR
    e = np.minimum(1, t / a) if a > 0 else np.ones(n)
    m = min(n, int(0.003 * SR)); uitloop = np.ones(n); uitloop[n - m:] = np.linspace(1, 0, m)   # geen tik tussen twee tonen
    return e * np.exp(-t / (d or sec / 4)) * uitloop
def stil(sec): return np.zeros(int(sec * SR))
def lp(x, k=0.15):   # eenvoudig laagdoorlaatfilter: haalt het krassen eraf
    y = np.zeros_like(x); v = 0.0
    for i, s in enumerate(x): v += k * (s - v); y[i] = v
    return y
def schrijf(naam, x, piek_db=-9):
    x = x / (np.max(np.abs(x)) + 1e-9) * 10 ** (piek_db / 20)
    n = int(0.006 * SR); x[-n:] *= np.linspace(1, 0, n)          # geen tik aan het eind
    with wave.open(os.path.join(UIT, naam + ".wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())
    return x

def druppel(f0, f1, sec):   # waterdruppel: toon die snel omhoog glijdt en uitsterft = "blub"
    s = sweep(f0, f1, sec, kromme=0.5); return s * env(len(s), a=0.002, d=sec / 3)

def blip(f, sec, vorm="tri"):
    s = sweep(f, f, sec, vorm); return s * env(len(s), a=0.002, d=sec / 2.5)

geluiden = {}
# hap: Gloop slokt een held op, twee blubs van laag naar lager (slikken), dan een klein boertje
hap = np.concatenate([druppel(260, 620, 0.07), stil(0.02), druppel(190, 430, 0.09), stil(0.03)])
boer = sweep(110, 80, 0.12, "tri") * env(int(0.12 * SR), a=0.01, d=0.05) * 0.6
geluiden["hap"] = np.concatenate([hap, boer])
# munt: muntje komt op de schat, twee tonen omhoog (B5 dan E6), het bekende "pling"
geluiden["munt"] = np.concatenate([blip(988, 0.05), blip(1319, 0.16)])
# val: held valt in de stekelput, glijfluitje omlaag en een doffe plof
fluit = sweep(700, 170, 0.38, "tri", kromme=0.7) * np.concatenate([np.minimum(1, t_(0.38) / 0.01)]) * np.linspace(1, 0.5, int(0.38 * SR))
plof = lp(rng.standard_normal(int(0.1 * SR)), 0.08) * env(int(0.1 * SR), a=0.001, d=0.025) * 3 + sweep(90, 50, 0.1) * env(int(0.1 * SR), a=0.001, d=0.03)
geluiden["val"] = np.concatenate([fluit, plof])
# poef: het boze wolkje van een wrok knapt, kort zacht geruis met een plopje
ruis = lp(rng.standard_normal(int(0.14 * SR)), 0.25) * env(int(0.14 * SR), a=0.003, d=0.035)
plop = sweep(420, 160, 0.06) * env(int(0.06 * SR), a=0.001, d=0.02)
p = ruis.copy(); p[:len(plop)] += plop * 0.8
geluiden["poef"] = p
# koop: je koopt een upgrade, drie tonen omhoog (C6 E6 G6) en de laatste blijft even hangen
geluiden["koop"] = np.concatenate([blip(1047, 0.06), blip(1319, 0.06), blip(1568, 0.22)])
# lied: de bard ontsnapt en zingt over je hol, vier noten op een luit (getokkeld: driehoek met snel verval)
def tokkel(f, sec): s = 0.7 * sweep(f, f, sec, "tri") + 0.3 * sweep(2 * f, 2 * f, sec); return s * env(len(s), a=0.002, d=0.09)
geluiden["lied"] = np.concatenate([tokkel(523, 0.14), tokkel(659, 0.14), tokkel(784, 0.14), tokkel(659, 0.12), tokkel(880, 0.35)])

uit = {k: schrijf(k, v) for k, v in geluiden.items()}

# golfvormen en lengtes om na te kijken (ik kan niet luisteren, dus ik meet: lengte, piek, geen tik aan begin en eind)
try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(len(uit), 1, figsize=(8, 1.3 * len(uit)), facecolor="#1d1426")
    for a, (k, x) in zip(ax, uit.items()):
        a.plot(np.arange(len(x)) / SR, x, color="#f0b43c", lw=0.5); a.set_facecolor("#2b1d35")
        a.set_ylim(-0.4, 0.4); a.set_xlim(0, 0.9); a.text(0.82, 0.22, f"{k} {len(x)/SR:.2f}s", color="#f3e2c0")
        a.tick_params(colors="#a08aa8", labelsize=7)
    fig.tight_layout(); fig.savefig(os.path.join(R, "ontwerp", "steam", "mila", "geluid-golven.png"), dpi=90)
except ImportError:
    pass
for k, x in uit.items():
    print(k, f"{len(x)/SR:.2f}s", f"piek {20*np.log10(np.max(np.abs(x))):.1f} dB", f"begin {abs(x[0]):.3f} eind {abs(x[-1]):.3f}")
