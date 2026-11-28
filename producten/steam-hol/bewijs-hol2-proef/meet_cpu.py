"""CPU binnen één meetronde (Olaf, #388): het hol van nu op 96 px tegen Hol 2.0 op 120 px, om en om, met een placebo.
Placebo: twee keer precies hetzelfde (het hol van nu op 96, A tegen A'), zodat je ziet hoeveel de meting zelf schommelt.
Elke start: 15 s opwarmen, dan CPU-tijd van het proces over MEET s (uit /proc/<pid>/stat). Linux, Xvfb 1920x1080,
software-tekenen (llvmpipe), Godot 4.3, gewoon spel (geen film), zelfde fps (12) voor beide.
Gebruik: GODOT=<pad> RONDES=4 MEET=40 python3 meet_cpu.py  (vanuit producten/steam-hol/godot)"""
import os, subprocess, time, statistics, json, sys
G = os.environ["GODOT"]; RONDES = int(os.environ.get("RONDES", 4)); MEET = float(os.environ.get("MEET", 40))
TICK = os.sysconf("SC_CLK_TCK")
STANDEN = {
    "nu96": ["res://main.tscn", "--", "hoogte=96", "vers=1", "fps=12", "balk=0", "zaad=5"],
    "nu96b": ["res://main.tscn", "--", "hoogte=96", "vers=1", "fps=12", "balk=0", "zaad=5"],
    "hol2_120": ["res://hol2/hol2.tscn", "--", "hoogte=120", "fps=12", "zaad=5"],
}
def cpu(pid):
    v = open(f"/proc/{pid}/stat").read().rsplit(")", 1)[1].split()
    return (int(v[11]) + int(v[12])) / TICK
uit = {k: [] for k in STANDEN}
for r in range(RONDES):
    for k, a in STANDEN.items():
        p = subprocess.Popen([G, "--path", ".", "--rendering-driver", "opengl3"] + a, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(15)
        c1, t1 = cpu(p.pid), time.time()
        time.sleep(MEET)
        c2, t2 = cpu(p.pid), time.time()
        p.kill(); p.wait()
        uit[k].append(round((c2 - c1) * 10 / (t2 - t1), 3))
        print(r, k, uit[k][-1], flush=True)
s = {k: {"cpu_s_per_10s": v, "gemiddeld": round(statistics.mean(v), 3), "spreiding": round(statistics.pstdev(v), 3)} for k, v in uit.items()}
s["placebo_verschil_procent"] = round((s["nu96b"]["gemiddeld"] / s["nu96"]["gemiddeld"] - 1) * 100, 1)
s["hol2_tegen_nu96_procent"] = round((s["hol2_120"]["gemiddeld"] / s["nu96"]["gemiddeld"] - 1) * 100, 1)
json.dump(s, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cpu.json"), "w"), indent=1)
print(json.dumps(s, indent=1))
