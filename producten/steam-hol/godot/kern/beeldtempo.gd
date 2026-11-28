extends RefCounted
# Beelden per seconde van de strook (Olaf, demolijst 2; Daan 13 nov 17:35).
# Gewoon 12 per s (#369, 28 nov): gelijk aan de loopklok van de 3D-helden (held_loop.gd LOOP_FPS 12). Op 10 per s
# kwam elk vijfde beeld een dubbele stap (12 stappen over 10 beelden), een hikje twee keer per seconde; op 240 px is
# een stap ±3 schermpixels en leest dat als haperen ("het lagt", Thijs 28 nov). Gemeten in één run per held: stappen
# met gelijke tussentijd en lengte 58% op 10, 74% op 12, 63% op 24 (GEZIEN, bewijs-fps-12/LEESMIJ.md).
# Was 10 (Daan 13 nov 17:35, duurtest zaad 4242: 0,157 tegen 0,434 CPU-s per 10 s op 15); 12 kost ±20% meer beelden.
# Tijdens een moment (val met schrik, hap van Gloop, vliegende muntjes) even sneller, zodat juist die vloeiend zijn:
# 24, een veelvoud van 12, zodat lopende helden om het andere beeld precies één stap zetten.
# Klimmen loopt op een klok van 0,1 s (held.gd PAS): op 12 per s blijft één op de zes beelden een klimstap staan.
# Met fps=<n> op de opdrachtregel (CPU-proef) blijft het vast op n.
const GEWOON := 12
const MOMENT := 24
const NA_S := 0.3            # na het moment nog even door, dan terug naar GEWOON

# Fakkels (en de pixelschat) krijgen een nieuw beeldje: 6 per s als er een held loopt, 3 per s in een leeg hol.
# Issue #79, tempo-regel 1 (organisatie/lat/hats-tempo.md): in een leeg hol bewoog alleen Gloop, de rest stond tot
# 30 s stil (GEZIEN, film van 10 min). Thijs 25 nov: rustig, zacht leven. 3 per s is een rustig flakkeren (het
# patroon van 12 standen duurt 4 s); het hol tekent dan 3 keer per s opnieuw, het venster tekende al door voor Gloop.
const FAKKEL_HELD := 6.0
const FAKKEL_LEEG := 3.0

static func fakkel_tempo(helden: int) -> float:
	return FAKKEL_HELD if helden > 0 else FAKKEL_LEEG

static func fakkels(s, helden: int, delta: float) -> void:
	s.anim_t += delta
	if s.anim_t >= 1.0 / fakkel_tempo(helden):
		s.anim_t = 0.0
		s.hol.tik()

static func is_moment(s) -> bool:
	if s.hol and "munten" in s.hol and not s.hol.munten.is_empty():
		return true
	if s.get("klap") != null and s.klap.bezig():
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
