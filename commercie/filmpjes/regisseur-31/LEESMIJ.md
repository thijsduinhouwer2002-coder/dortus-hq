# Regisseur 31: lanceer-Short Click Cuts in de vorm van v8c (#135)

Lokaal opgenomen (cloudsessie, 27 nov 2026): Blender 5.3.0 met interface onder Xvfb 1080x1920, Click Cuts 1.0.0 (main), Horse Statue 01 (Poly Haven, CC0).
- `cuts8.py`: speelt de gebruiker beeld voor beeld op een klok van 1/30 s met echte X-muis en kliks (python-xlib XTest; xdotool was er niet), pakt het scherm met mss. Uit: scherm-ruw.ts, muis.txt, film.json.
  `xvfb-run --server-args="-screen 0 1080x1920x24 -noreset" blender --gpu-backend opengl -p 0 0 1080 1920 start.blend --python cuts8.py -- <map> /tmp/click_cuts.zip <modelmap>` (met `LIBGL_ALWAYS_SOFTWARE=1`, mss en python-xlib in /tmp/pylib). Duurt ±5 min.
- `montage_cuts.py`: muispijl uit muis.txt, hook, eindtekst, muziek Deep Urban (Mixkit 623, vanaf 175,9 s). Lettertype als laatste argument: tiktok, montserrat of poppins (`fonts/`, alle drie OFL 1.1). `--eerste` maakt alleen het eerste beeld.
- `film-v8.json`, `opname-v8.log.gz`, `v8-strook.jpg` (1 beeld per seconde) horen bij `marketing/wachtrij/2026-12-01-yt-short-cuts-v8.mp4`.
