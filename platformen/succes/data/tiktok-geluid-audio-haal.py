# Verhaal 31: haalt van een steekproef filmpjes met "eigen geluid" alleen het geluid (wav, mono 16 kHz)
# en meet het volume met ffmpeg (volumedetect). Bewaart alleen id, account en volume, geen geluid.
# Gebruik: python3 tiktok-geluid-audio-haal.py <analyse.csv> <werkmap> <uit.csv> [per_account]
import csv, sys, os, random, subprocess, re, collections
from concurrent.futures import ThreadPoolExecutor
ana, werk, uit = sys.argv[1:4]; PER = int(sys.argv[4]) if len(sys.argv) > 4 else 20
os.makedirs(werk, exist_ok=True)
rij = [r for r in csv.DictReader(open(ana)) if r['soort'] == 'eigen']
per = collections.defaultdict(list)
for r in rij: per[r['account']].append(r)
random.seed(31)
kies = []
for a, rs in per.items():
    if len(rs) >= 20: kies += random.sample(rs, min(PER, len(rs)))
def meet(r):
    p = os.path.join(werk, r['id'] + '.wav')
    if not os.path.exists(p):
        subprocess.run(['yt-dlp', '-q', '-f', 'bestaudio/best', '-x', '--audio-format', 'wav',
                        '--postprocessor-args', 'ExtractAudio:-ac 1 -ar 16000', '-o', os.path.join(werk, '%(id)s.%(ext)s'),
                        f"https://www.tiktok.com/@{r['account']}/video/{r['id']}"], capture_output=True, timeout=120)
    if not os.path.exists(p): return (r['account'], r['id'], '', '')
    o = subprocess.run(['ffmpeg', '-i', p, '-af', 'volumedetect', '-f', 'null', '-'], capture_output=True, text=True).stderr
    mean = re.search(r'mean_volume: (-?[\d.]+|-inf)', o); mx = re.search(r'max_volume: (-?[\d.]+|-inf)', o)
    return (r['account'], r['id'], mean.group(1) if mean else '', mx.group(1) if mx else '')
with ThreadPoolExecutor(8) as ex: res = list(ex.map(meet, kies))
with open(uit, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['account', 'id', 'mean_db', 'max_db']); w.writerows(res)
print(len(res), sum(1 for x in res if x[2]))
