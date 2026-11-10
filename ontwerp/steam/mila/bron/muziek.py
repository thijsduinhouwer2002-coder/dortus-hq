# Mila 10 nov: muziek van Het Hol, "Gloop's Lullaby". Zelf gemaakt in code: getokkelde luit (Karplus-Strong, een
# geplukte snaar nagebootst), een zachte bas en een eenvoudige melodie. Loopt naadloos rond (de naklank van het eind
# loopt door in het begin). Rustig, 72 slagen per minuut, A klein: een knus hol, niet spannend, past naast werk.
# Uit: producten/steam-hol/godot/geluid/muziek_hol.ogg (Godot: loop aan). Ook een plaatje om na te kijken.
import os, subprocess, wave
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
UIT = os.path.join(R, "producten", "steam-hol", "godot", "geluid"); os.makedirs(UIT, exist_ok=True)
SR = 32000
BPM = 72
SLAG = 60 / BPM
rng = np.random.default_rng(14)

def noot(naam):   # "A3" -> Hz
    i = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"].index(naam[:-1])
    return 440 * 2 ** ((i - 9) / 12 + int(naam[-1]) - 4)

def snaar(f, sec, helder=0.5, verval=0.996):
    """Karplus-Strong: ruis in een lus van één golflengte, elke ronde iets gemiddeld en zachter = geplukte snaar."""
    n = int(sec * SR); P = SR / f; N = max(2, int(P)); w = P - N   # zuiver stemmen: lus van N + w monsters
    y = np.zeros(n + N + 1)
    start = rng.uniform(-1, 1, N)
    k = int(2 + (1 - helder) * 6)                          # zachter tokkelen: begin al wat gladder
    start = np.convolve(start, np.ones(k) / k, mode="same")
    y[:N] = start
    i = N
    while i < n + N:
        j = min(i + N, n + N)
        a = y[i - N:j - N]; b = y[i - N - 1:j - N - 1] if i - N - 1 >= 0 else np.concatenate([[0], y[i - N:j - N - 1]])
        y[i:j] = verval * ((1 - w) * a + w * b)
        i = j
    uit = y[N:N + n]
    m = int(0.01 * SR); uit[-m:] *= np.linspace(1, 0, m)
    return uit

maten_A = [("A", ["A2", "E3", "A3", "C4", "E4"]), ("G", ["G2", "D3", "G3", "B3", "D4"]),
           ("F", ["F2", "C3", "F3", "A3", "C4"]), ("E", ["E2", "B2", "E3", "G#3", "B3"])]
maten_B = [("C", ["C3", "G3", "C4", "E4", "G4"]), ("G", ["G2", "D3", "G3", "B3", "D4"]),
           ("Am", ["A2", "E3", "A3", "C4", "E4"]), ("E", ["E2", "B2", "E3", "G#3", "B3"])]
# melodie: per maat vier tellen, "-" = rust, noten uit het akkoord en de A-klein-toonladder; eenvoudig, om te neuriën
mel_A1 = [["E5", "-", "C5", "D5"], ["B4", "-", "G4", "-"], ["A4", "C5", "F5", "E5"], ["E5", "-", "-", "-"]]
mel_A2 = [["E5", "-", "C5", "D5"], ["B4", "D5", "G5", "F5"], ["E5", "C5", "A4", "C5"], ["B4", "-", "G#4", "-"]]
mel_B = [["G5", "-", "E5", "C5"], ["D5", "-", "B4", "-"], ["C5", "E5", "A5", "-"], ["G#5", "-", "B4", "-"]]
stuk = [(maten_A, None), (maten_A, mel_A1), (maten_A, mel_A2), (maten_B, mel_B), (maten_A, mel_A1), (maten_A, None)]

maten = sum(len(m) for m, _ in stuk)
lengte = int(maten * 4 * SLAG * SR)
staart = int(3 * SR)
mix = np.zeros(lengte + staart)

def leg(x, t, vol):
    a = int(t * SR); b = a + len(x)
    mix[a:b] += x * vol

t = 0.0
tokkel = [0, 2, 3, 4, 3, 2, 1, 2]   # vingerpatroon over acht achtsten
for blok, mel in stuk:
    for m, (_, ak) in enumerate(blok):
        leg(snaar(noot(ak[0]), 3.0, 0.3, 0.997), t, 0.55)                     # bas op tel 1
        leg(snaar(noot(ak[0]), 2.0, 0.3, 0.996), t + 2 * SLAG, 0.35)          # en zachter op tel 3
        for e, i in enumerate(tokkel):
            if e == 0: continue
            menselijk = rng.uniform(-0.012, 0.012)                            # niet als een machine
            leg(snaar(noot(ak[i]), 1.8, 0.45, 0.995), t + e * SLAG / 2 + menselijk, 0.26 + 0.04 * (e % 2 == 0))
        if mel:
            for tel, nm in enumerate(mel[m]):
                if nm == "-": continue
                leg(snaar(noot(nm), 2.4, 0.7, 0.9965), t + tel * SLAG + rng.uniform(-0.008, 0.008), 0.42)
        t += 4 * SLAG

# naadloos: de naklank na het eind komt bovenop het begin
lus = mix[:lengte].copy(); lus[:staart] += mix[lengte:]
# warm maken: zacht laagdoorlaat en een kleine kamer (twee echo's)
for vertraging, vol in [(0.083, 0.18), (0.131, 0.12)]:
    d = int(vertraging * SR); lus += np.roll(lus, d) * vol            # np.roll houdt het rond, dus ook naadloos
from scipy.signal import lfilter
k = 0.35
_, zi = lfilter([k], [1, -(1 - k)], lus, zi=[0.0])      # eerste ronde alleen voor de eindstand van het filter
y, _ = lfilter([k], [1, -(1 - k)], lus, zi=zi)          # tweede ronde begint daarmee: ook het filter is naadloos
lus = y / np.max(np.abs(y)) * 10 ** (-14 / 20)                         # -14 dB: achtergrond, zachter dan de geluidjes

wav = os.path.join(UIT, "muziek_hol.wav")
with wave.open(wav, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((lus * 32767).astype(np.int16).tobytes())
ogg = os.path.join(UIT, "muziek_hol.ogg")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-c:a", "libvorbis", "-q:a", "4", ogg], check=True)
os.remove(wav)
print(f"{maten} maten, {lengte / SR:.1f} s, naad: begin {lus[0]:.4f} eind {lus[-1]:.4f}, ogg {os.path.getsize(ogg) // 1024} kB")

try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(2, 1, figsize=(9, 3.6), facecolor="#1d1426")
    ax[0].plot(np.arange(len(lus)) / SR, lus, color="#f0b43c", lw=0.3); ax[0].set_title("muziek_hol, heel stuk", color="#f3e2c0", fontsize=9)
    naad = np.concatenate([lus[-SR:], lus[:SR]])
    ax[1].plot(np.arange(len(naad)) / SR - 1, naad, color="#57c49c", lw=0.4); ax[1].axvline(0, color="#ee6a4f", lw=0.8)
    ax[1].set_title("naad: laatste en eerste seconde aan elkaar (rode lijn)", color="#f3e2c0", fontsize=9)
    for a in ax: a.set_facecolor("#2b1d35"); a.tick_params(colors="#a08aa8", labelsize=7)
    fig.tight_layout(); fig.savefig(os.path.join(R, "ontwerp", "steam", "mila", "muziek-golf.png"), dpi=90)
except ImportError:
    pass
