extends RefCounted
# Beelden per seconde van de strook (Olaf, demolijst 2; Daan 13 nov 17:35).
# Gewoon 10 per s: lopen leest op ware grootte als gewoon pixelart lopen en kost een derde van 15
# (duurtest zaad 4242: gemiddeld 0,157 tegen 0,434 CPU-s per 10 s, pieken 0,44 tegen 1,33).
# Tijdens een moment (val met schrik, hap van Gloop, vliegende muntjes) even sneller, zodat juist die vloeiend zijn.
# Sneller is 20 en niet 15: 20 is een veelvoud van de loopklok in held.gd (een stap per 0,1 s), dus helden die
# tijdens een moment lopen blijven in gelijke stappen (bij 15 zou elke derde beeld een stap overslaan: een hikje).
# Met fps=<n> op de opdrachtregel (CPU-proef) blijft het vast op n.
const GEWOON := 10
const MOMENT := 20
const NA_S := 0.3            # na het moment nog even door, dan terug naar GEWOON

static func is_moment(s) -> bool:
	if s.hol and "munten" in s.hol and not s.hol.munten.is_empty():
		return true
	if s.slijm and "hap_van" in s.slijm and "t" in s.slijm and float(s.slijm.t) < float(s.slijm.hap_van) + 1.0:
		return true
	for w in s.wezens.get_children():
		if w.has_method("is_held") and str(w.get("staat")) == "vallen":
			return true
	return false

static func tik(s) -> void:
	if s.film or s.fps_vast:
		return
	if is_moment(s):
		s.moment_tot = s.t + NA_S
	var doel: int = MOMENT if s.t < s.moment_tot else GEWOON
	if Engine.max_fps != doel:
		Engine.max_fps = doel
