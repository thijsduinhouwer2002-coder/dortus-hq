extends Node2D
# De eerste minuut: altijd één doel in beeld (Sanne 25 nov, issue #19 punt 4 en bouwblad C in platformen/steam/spelgevoel.md).
# Thijs 24 nov: "het is niet duidelijk wat je moet doen". Rusty's Retirement en Windowstead: steeds één doel tegelijk.
# Eén regel groot (minstens 12 px op 120) op een donker plaatje in de lucht boven het hol, met een pijltje dat zacht
# op en neer wipt naar de plek, en een gouden rand die zacht ademt om het vak waar je moet klikken. Geen uitlegscherm.
# Stappen (spelerstekst is concept tot Thijs hem schrijft):
#   0 WELKOM  4 s naam en wat het is, daarna nooit meer
#   1 KIJK    geen tekst: de eerste held valt in de put die er al staat, de muntjes vliegen (het beeld vertelt het)
#   2 GRAAF   "Click the dirt to dig." tot het eerste gegraven vak (gang of kamer, waar ook)
#   3 VAL     "Click the tunnel to set a trap." tot er een put bij komt (waar ook)
#   4 KLAAR   niets meer; het doel op het bord (kern/kaartje.gd doel_regel) neemt het over
# Doet de speler 20 s niets bij stap 2 of 3, dan wipt de pijl één keer groter. Nooit een tweede regel.
# Een bestaande save zonder "uitleg" telt als KLAAR (wie al speelde krijgt geen les).

const HOL := preload("res://hol/hol.gd")
const FREDOKA := preload("res://kunst/letters/Fredoka.ttf")

enum { WELKOM, KIJK, GRAAF, VAL, KLAAR }
const WELKOM_S := 4.0
const KIJK_MAX_S := 30.0      # komt er toch geen vangst (vreemde save), dan na 30 s door naar graven
const NA_MUNT_S := 1.6        # na de eerste muntjes even kijken, dan pas de regel
const DUW_S := 20.0           # zo lang niets gedaan: de pijl wipt één keer groter
const TEKST := {
	WELKOM: "Hats of the Fallen. Your taskbar has a basement.",
	GRAAF: "Click the dirt to dig.",
	VAL: "Click the tunnel to set a trap.",
}

var s                          # de strook
var stap := KLAAR
var stap_t := 0.0              # tijd in deze stap
var duw_t := -1.0              # wanneer de pijl groter wipte (eenmalig per stap)
var goud_start := 0
var munt_t := -1.0
var vallen_start := 0
var gegraven_kol := -1
var letter: FontVariation

func zet(strook, begin_stap: int) -> void:
	s = strook
	stap = clampi(begin_stap, WELKOM, KLAAR)
	letter = FontVariation.new()
	letter.base_font = FREDOKA
	letter.variation_opentype = {TextServerManager.get_primary_interface().name_to_tag("wght"): 600}
	goud_start = int(s.hol.goud)
	vallen_start = s.hol.vallen.size()
	s.hol.gegraven.connect(_gegraven)
	set_process(stap != KLAAR)
	if stap != KLAAR:
		_log()

func actief() -> bool:
	return stap != KLAAR

func _log() -> void:
	s.log_regel("HOL uitleg stap %d t=%.1f %s" % [stap, s.t, TEKST.get(stap, "")])

func _naar(n: int) -> void:
	stap = n
	stap_t = 0.0
	duw_t = -1.0
	if stap == VAL:
		vallen_start = s.hol.vallen.size()
	_log()
	if stap == KLAAR:
		set_process(false)
	queue_redraw()

func _gegraven(cel: Vector2i) -> void:
	gegraven_kol = cel.x
	if stap == GRAAF:
		_naar(VAL)

func _process(delta: float) -> void:
	stap_t += delta
	match stap:
		WELKOM:
			if stap_t >= WELKOM_S:
				_naar(KIJK)
		KIJK:
			if munt_t < 0.0 and int(s.hol.goud) > goud_start:
				munt_t = stap_t
			if (munt_t >= 0.0 and stap_t - munt_t >= NA_MUNT_S) or stap_t >= KIJK_MAX_S:
				_naar(GRAAF)
		VAL:
			if s.hol.vallen.size() > vallen_start:
				_naar(KLAAR)
			else:
				vallen_start = mini(vallen_start, s.hol.vallen.size())   # put weggehaald: de volgende telt
	if (stap == GRAAF or stap == VAL) and duw_t < 0.0 and stap_t >= DUW_S:
		duw_t = stap_t
		s.log_regel("HOL uitleg duw stap %d" % stap)
	# uitleg_klik=<s>: een speler die na zoveel seconden precies doet wat er staat (alleen voor de film en de toets)
	if s.proef_uitleg_klik > 0.0 and (stap == GRAAF or stap == VAL) and stap_t >= s.proef_uitleg_klik:
		var vak := doel_vak()
		var was := stap
		if vak.size.x > 0:
			var p: Vector2 = (vak.get_center() - s.hol.position) / s.schaal
			var wat: String = s.hol.klik(p)
			if wat != "" and s.slijm != null and s.slijm.has_method("werk_berg_grens"):
				s.slijm.werk_berg_grens()
			s.log_regel("HOL uitleg proefklik %s: %s" % [vak.get_center(), wat])
			if stap == was:
				stap_t = -1000.0   # klik deed niets: niet blijven klikken
	queue_redraw()

# ---- waar moet de speler klikken (kolom, en of het de kamerrij of de gang is) ----
func doel_kol() -> int:
	var h = s.hol
	var gloop: int = h.pos_naar_cel(s.slijm.position).x if s.slijm != null else -99
	if stap == GRAAF:
		# een kamer boven de gang, vlak achter de ingang: daar is de grond het best te zien en is niets anders te klikken
		for k in range(h.ingang_kol + 2, h.schat_kol - 1):
			if h.gang[k] and not h.boven[k] and absi(k - gloop) > 1:
				return k
		return h.ingang_kol - 1 if h.ingang_kol > 1 else -1   # alles al open: de gang naar links verlengen
	if stap == VAL:
		if _put_mag(gegraven_kol, gloop):
			return gegraven_kol   # onder het vak dat hij net groef
		for k in range(h.ingang_kol + 1, h.schat_kol):
			if _put_mag(k, gloop):
				return k
	return -1

func _put_mag(k: int, gloop: int) -> bool:
	var h = s.hol
	return k > h.ingang_kol and k < h.schat_kol and k < h.gang.size() and h.gang[k] and not h.vallen.has(k) and absi(k - gloop) > 1

func doel_vak() -> Rect2:
	var k := doel_kol()
	if k < 0:
		return Rect2()
	var sc: float = s.schaal
	var o: Vector2 = s.hol.position
	var kamer: bool = stap == GRAAF and bool(s.hol.gang[k])
	var y0: float = HOL.OPP if kamer else HOL.GANG_BOVEN
	var y1: float = HOL.GANG_BOVEN if kamer else HOL.GANG_ONDER
	return Rect2(o.x + k * HOL.KOL * sc, o.y + y0 * sc, HOL.KOL * sc, (y1 - y0) * sc)

func maat() -> int:
	return maxi(12, 5 * int(s.schaal))   # 15 px op 120, 12 op 96, 20 op 160

func _draw() -> void:
	if stap == KLAAR or stap == KIJK:
		return
	var t: String = TEKST.get(stap, "")
	var m := maat()
	var sc: float = s.schaal
	var lucht: float = s.hol.position.y + HOL.OPP * sc   # hoogte van de lucht boven het gras, in vensterpixels
	var tb := letter.get_string_size(t, HORIZONTAL_ALIGNMENT_LEFT, -1, m)
	var ph := float(m) + 6.0
	var py := maxf(0.0, lucht - ph - 1.0)
	var pijl_x := -1.0
	var vak := doel_vak()
	if stap != WELKOM and vak.size.x > 0:
		pijl_x = vak.position.x + vak.size.x / 2.0
		# ademende gouden rand om het vak (1,2 s per keer, rustig: geen knipperen)
		var a := 0.7 + 0.3 * sin(stap_t * TAU / 1.2)
		draw_rect(vak.grow(-1.0), Color(1.0, 0.86, 0.42, 0.10 + 0.08 * a), true)
		draw_rect(vak.grow(-sc * 0.5), Color(1.0, 0.86, 0.42, a), false, sc)
	# plaatje met de regel: naast de pijl, of midden boven het hol bij het welkom
	var px: float
	var hol_breed: float = (s.hol.max_kol + 1) * HOL.KOL * sc
	if pijl_x >= 0.0:
		px = pijl_x + 4.0 * sc
		if px + tb.x + 12.0 > hol_breed:
			px = pijl_x - 4.0 * sc - tb.x - 12.0
	else:
		px = s.hol.position.x + maxf(8.0, (hol_breed - tb.x) / 2.0)
	px = maxf(2.0, px)
	var plaat := Rect2(px, py, tb.x + 12.0, ph)
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(0.13, 0.07, 0.05, 0.9)
	sb.border_color = Color("#e8b040")
	sb.set_border_width_all(1)
	sb.set_corner_radius_all(int(ph / 2.0))
	sb.anti_aliasing = true
	draw_style_box(sb, plaat)
	draw_string(letter, Vector2(px + 6.0, py + ph / 2.0 + m * 0.36), t, HORIZONTAL_ALIGNMENT_LEFT, -1, m, Color("#ffe07a"))
	if pijl_x >= 0.0:
		# pijltje naar beneden in de lucht, wipt zacht 2 spelpixels; na 20 s niets één keer groter
		var groot := 1.0
		if duw_t >= 0.0 and stap_t - duw_t < 0.8:
			groot = 1.0 + 0.6 * sin((stap_t - duw_t) / 0.8 * PI)
		var wip := (0.5 + 0.5 * sin(stap_t * TAU / 0.9)) * 2.0 * sc
		# De punt raakt de bovenkant van het gouden vak. Bij de val ligt dat vak een rij onder het pas gegraven
		# kamertje: dan loopt een steel door het kamertje, zodat je niet eerst naar het kamertje kijkt (Daan #64 C3).
		var bw := 3.5 * sc * groot
		var kop := 5.0 * sc * groot
		var top := py + 1.0 + wip
		var doel_y := maxf(lucht, vak.position.y) - 1.0
		var punt := maxf(top + kop, doel_y + wip * 0.5)
		var kop_top := punt - kop
		var donker := Color(0.13, 0.07, 0.05, 0.9)
		if kop_top - top > 1.0:
			var st := maxf(1.0, 0.9 * sc)
			var steel := Rect2(pijl_x - st, top, st * 2.0, kop_top - top + 0.5)
			draw_rect(steel.grow(1.0), donker, true)
			draw_rect(steel, Color("#ffe07a"), true)
		var pts := PackedVector2Array([Vector2(pijl_x - bw, kop_top), Vector2(pijl_x + bw, kop_top), Vector2(pijl_x, punt)])
		draw_colored_polygon(pts, Color("#ffe07a"))
		draw_polyline(PackedVector2Array([pts[0], pts[1], pts[2], pts[0]]), donker, 1.5, true)
