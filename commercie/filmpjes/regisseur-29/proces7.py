"""Echte schermopname v7 voor de sale-Short (issue #159, Regisseur 26 nov 2026): één doorlopende opname van de
weergave, camera draait rond, de robot verandert in hetzelfde beeld. Het verloop staat in verloop7.py; de rest (echte
Blender met interface onder Xvfb, Click Joints Pro, beeld-voor-beeld-klok van 1/30 s, mss) komt uit regisseur-28/proces.py.
    blender --gpu-backend opengl start.blend --python proces7.py -- <map> <betaalde zip>"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
R26 = os.path.abspath(os.path.join(HIER, "..", "regisseur-26", "echt_opname.py"))
STUDIO = os.path.abspath(os.path.join(HIER, "..", "studio"))
r26 = open(R26, encoding="utf-8").read()

VERLOOP = open(os.path.join(HIER, "verloop7.py"), encoding="utf-8").read()

GEEN_FIGUUR_IMPORT = '''
import sys as _sys2
_sys2.path.insert(0, STUDIO_MAP)
import figuur_robot as R  # noqa: E402
import studio as S  # noqa: E402
'''

# Beeld voor beeld (CJ_BEELD=1, proef 7). Proef 4 tot 6 (GEZIEN): de weergave van Blender tekent op de runner maar 0,2
# tot 4 keer per seconde, dus een opname in echte tijd is een diashow met een vloeiende muis erover. Nu loopt er een
# eigen klok: elke tik is precies 1/30 s. Per tik zet het script de echte muis (xdotool) op zijn plek voor dat moment,
# laat Blender het hele venster echt tekenen en pakt dat scherm (mss, XGetImage) als één beeld voor ffmpeg. Het blijft
# de echte interface met echte kliks; alleen wacht de klok tot Blender klaar is met tekenen, zoals een opname die
# traag gemaakt en weer versneld is. Wat Blender blokkerend doet (Figure from rig) kost zo 0 s in de film.
STAP = r'''
if os.environ.get("CJ_BEELD") == "1":
    import atexit as _ax
    import time as _tm
    _VK = {"t": _tm.time(), "rest": 0, "n": 0, "ff": None, "sct": None, "mon": None, "muis": None, "glij": [],
           "teken_fout": 0, "echt0": _tm.time()}
    _echte_tijd = _tm.time
    _tm.time = lambda: _VK["t"]

    class _VGlij:
        """Zoals glij.py (zelfde boog en versnelling), maar op de eigen klok: per tik één xdotool mousemove."""
        def __init__(s, x0, y0, x1, y1, duur, boog_f):
            s.x0, s.y0, s.x1, s.y1, s.duur = float(x0), float(y0), float(x1), float(y1), max(0.05, float(duur))
            dx, dy = s.x1 - s.x0, s.y1 - s.y0
            d = math.hypot(dx, dy)
            s.nx, s.ny = (-dy / d, dx / d) if d > 0 else (0.0, 0.0)
            s.boog = min(36.0, d * 0.07) * float(boog_f) * (1 if int(s.x0 + s.y1) % 2 else -1)
            s.t0, s.klaar, s.gestopt = _VK["t"], False, False

        def zet(s, t):
            e = t * t * t * (t * (6 * t - 15) + 10)
            b = math.sin(math.pi * e) * s.boog
            x = s.x0 + (s.x1 - s.x0) * e + s.nx * b
            y = s.y0 + (s.y1 - s.y0) * e + s.ny * b
            subprocess.run(["xdotool", "mousemove", str(int(round(x))), str(int(round(y)))], check=False)

        def tik(s):
            if s.klaar:
                return
            t = min(1.0, (_VK["t"] - s.t0) / s.duur)
            s.zet(t)
            if t >= 1.0:
                s.klaar = True

        def poll(s):
            return 0 if s.klaar else None

        def terminate(s):
            s.klaar = s.gestopt = True

        def wait(s):
            if not s.gestopt and not s.klaar:
                s.zet(1.0)
            s.klaar = True
            return 0

    def _glij(x, y, duur, boog=1.0):
        g = _VGlij(MUIS["x"], MUIS["y"], x, y, duur, boog)
        _VK["glij"].append(g)
        return g

    def _begin():
        uitmap = scherm_basis.uitmap
        venster = bpy.context.window_manager.windows[0]
        try:
            if os.environ.get("CJ_PYLIB", "/tmp/pylib") not in sys.path:
                sys.path.insert(0, os.environ.get("CJ_PYLIB", "/tmp/pylib"))
            import mss as _mss
            _VK["sct"] = _mss.mss()
            _VK["mon"] = _VK["sct"].monitors[0]
            br, ho = _VK["mon"]["width"], _VK["mon"]["height"]
            log(f"KORT stap: mss {br}x{ho}")
        except Exception as f:  # noqa: BLE001
            log(f"KORT stap: mss niet te laden ({f}), dan import")
            r = subprocess.run(["xdpyinfo"], capture_output=True, text=True).stdout
            br, ho = (int(v) for v in r.split("dimensions:")[1].split()[0].split("x"))
        _VK["maat"] = (br, ho)
        _VK["ff"] = subprocess.Popen(
            ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{br}x{ho}", "-r", "30",
             "-i", "-", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "12", "-pix_fmt", "yuv420p",
             "-f", "mpegts", os.path.join(uitmap, "scherm-ruw.ts")], stdin=subprocess.PIPE)
        _VK["muis"] = open(os.path.join(uitmap, "muis.txt"), "w", buffering=1)
        with open(os.path.join(uitmap, "start.txt"), "w") as f_:
            f_.write(f"{_VK['t']:.4f}\n")
        _ax.register(_einde)
        log(f"KORT stap: begin op {_VK['t']:.3f}, venster {venster.width}x{venster.height}")

    def _einde():
        if _VK["ff"] is not None and _VK["ff"].stdin and not _VK["ff"].stdin.closed:
            _VK["ff"].stdin.close()
            _VK["ff"].wait()
            log(f"KORT stap: {_VK['n']} beelden in {_echte_tijd() - _VK['echt0']:.0f} s echte tijd")

    def _teken():
        herteken()
        venster = bpy.context.window_manager.windows[0]
        try:
            with bpy.context.temp_override(window=venster, screen=venster.screen):
                bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)
        except Exception as f:  # noqa: BLE001
            _VK["teken_fout"] += 1
            if _VK["teken_fout"] < 4:
                log(f"KORT stap: redraw_timer {f}")

    def _vang():
        br, ho = _VK["maat"]
        if _VK["sct"] is not None:
            raw = _VK["sct"].grab(_VK["mon"]).raw
        else:
            raw = subprocess.run(["import", "-window", "root", "-depth", "8", "bgra:-"], capture_output=True).stdout
        if len(raw) == br * ho * 4:
            _VK["ff"].stdin.write(raw)
        r = subprocess.run(["xdotool", "getmouselocation", "--shell"], capture_output=True, text=True).stdout
        w = dict(x.split("=", 1) for x in r.split() if "=" in x)
        if "X" in w:
            _VK["muis"].write(f"{_VK['t']:.4f} {w['X']} {w['Y']}\n")

    def stap_v():
        if _VK["ff"] is None:
            _begin()
        if _VK["rest"] <= 0:
            try:
                d = next(gang)
            except StopIteration:
                _einde()
                return None
            if d is None:
                _einde()
                return None
            _VK["rest"] = max(1, int(round(float(d) * 30)))
        if _VK.get("elke") is not None:   # beweging die ook tijdens de korte rust van de muis doorloopt
            _VK["elke"]()
        for g in list(_VK["glij"]):
            g.tik()
            if g.klaar:
                _VK["glij"].remove(g)
        _teken()
        _vang()
        _VK["n"] += 1
        if _VK["n"] % 300 == 0:
            log(f"KORT stap: {_VK['n']} beelden, {_echte_tijd() - _VK['echt0']:.0f} s echt")
        _VK["t"] += 1.0 / 30.0
        _VK["rest"] -= 1
        return 0.0

    _oud_verloop = verloop

    def verloop():
        yield from _oud_verloop_zonder_stop()

    def _oud_verloop_zonder_stop():
        try:
            yield from verloop_pro()
        except Exception as fout:  # noqa: BLE001
            import traceback
            log(f"KORT FOUT {fout}\\n{traceback.format_exc()}")
        deel("eind")
        with open(os.path.join(scherm_basis.uitmap, "film.json"), "w") as f_:
            json.dump(film, f_, indent=1)
        log(f"KORT klaar {film['n']} beelden")
        _einde()
        bpy.ops.wm.quit_blender()
        yield 0.1

    gang = verloop()
    bpy.app.timers.register(stap_v, first_interval=3.0)
else:
    bpy.app.timers.register(stap, first_interval=3.0)
'''

MIJN = f'''
_r28 = {{"V": {VERLOOP!r}, "I": {GEEN_FIGUUR_IMPORT.replace("STUDIO_MAP", repr(STUDIO))!r}, "S": {STAP!r}}}
_i, _j = src.index("def verloop_pro():"), src.index("RENDER_SAMPLES =")
src = src[:_i] + _r28["I"] + _r28["V"] + "\\n\\n" + src[_j:]
_oud = "\\nbpy.app.timers.register(stap, first_interval=3.0)"
assert src.count(_oud) == 1
src = src.replace(_oud, "\\n" + _r28["S"])
'''

_haak = "r14 = r14.replace(_haak, PATCH + _haak)"
assert r26.count(_haak) == 1
r26 = r26.replace(_haak, "r14 = r14.replace(_haak, PATCH + " + repr(MIJN) + " + _haak)")
r26 = r26.replace("HIER = os.path.dirname(os.path.abspath(__file__))", f"HIER = {os.path.dirname(R26)!r}", 1)
exec(compile(r26, R26, "exec"), {"__name__": "__main__", "__file__": R26})   # noqa: S102 (eigen code uit de repo)
