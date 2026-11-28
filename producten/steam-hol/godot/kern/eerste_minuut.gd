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
# Sanne 28 nov (#368, speeltest Thijs 10:36 "ik snap echt niet wat ik moet doen"): zijn save van 24 nov liep door, dus hij
# kreeg nooit een les. Nu: een save van vóór uitleg-versie 2 (UITLEG_V) krijgt de les één keer opnieuw, zonder de
# kijkstap (er lopen al helden): welkom met het doel, graven, val. Kan een stap nergens (alles gegraven, overal een
# put), dan gaat hij na 1 s door, zodat de les nooit vastloopt. Het welkom zegt nu het doel en niet alleen de naam:
# Thijs wist niet waarom hij iets zou doen.
# Gloop-les (Daan #68, issue #62): de eerste keer dat Gloops ring aangaat (systemen/gloop_ring.gd) staat één keer
# dezelfde regel met pijl op Gloop: "Click Gloop to grow him." Weg zodra hij op Gloop klikt (kaartje open), de ring
# uitgaat, of na 20 s. Daarna nooit meer: de ring alleen zegt het dan. Zo leert de speler wat de ring betekent en
# blijft het bord rustig (Thijs 25 nov). Bewaard als "gloop_les" in de save.
# Sanne 28 nov (#406, Iris #399 punt 1 en 2): (1) het welkom stond midden boven het hele hol, en bij een oude save is
# dat leeg gras ver links van waar het hol echt is (x ±1085 tot 1440 op 1920); niemand zag het. Nu staat het boven het
# hol zelf (ingang tot schat), nooit over het bord, en bij een oude save 6 s (de eerste 1 tot 2 s tekent het venster
# nog niet). (2) "Click Gloop to grow him." ging na 6 s weg als Gloop plat ging en kwam nooit terug. Nu telt de les pas
# als gehad als de speler één keer het kaartje van Gloop opende ("gloop_klik" in de save); tot dan komt de regel terug
# zodra de ring weer aangaat, en staat de ring aan zonder klik, dan na GLOOP_TERUG_S opnieuw.

const HOL := preload("res://hol/hol.gd")
const FREDOKA := preload("res://kunst/letters/Fredoka.ttf")

enum { WELKOM, KIJK, GRAAF, VAL, KLAAR }
const WELKOM_S := 4.0
const KIJK_MAX_S := 30.0      # komt er toch geen vangst (vreemde save), dan na 30 s door naar graven
const NA_MUNT_S := 1.6        # na de eerste muntjes even kijken, dan pas de regel
const DUW_S := 20.0           # zo lang niets gedaan: de pijl wipt één keer groter
const UITLEG_V := 2           # saves met een lagere "uitleg_v" krijgen de les één keer opnieuw (#368)
const GEEN_DOEL_S := 1.0      # zo lang geen plek om te klikken: stap overslaan
const TEKST := {
	WELKOM: "Heroes want your gold. Trap them first!",   # concept tot Thijs hem schrijft
	GRAAF: "Click the dirt to dig.",
	VAL: "Click the tunnel to set a trap.",
}
const GLOOP_TEKST := "Click Gloop to grow him."
const GLOOP_MAX_S := 20.0
const GLOOP_TERUG_S := 45.0   # ring aan, les weg zonder klik: zo lang later komt hij terug (#406)
const WELKOM_OPNIEUW_S := 6.0 # oude save: welkom langer, de eerste 1 tot 2 s tekent het venster nog niet (#406)

var gloop_gezien := false      # de speler opende één keer het kaartje van Gloop (save "gloop_klik", #406)
var gloop_rust := 0.0          # tijd sinds de Gloop-les wegging zonder klik, met de ring aan
var gloop_t := -1.0            # >= 0: de Gloop-les staat nu in beeld, zo lang al

var s                          # de strook
var stap := KLAAR
var stap_t := 0.0              # tijd in deze stap
var duw_t := -1.0              # wanneer de pijl groter wipte (eenmalig per stap)
var goud_start := 0
var munt_t := -1.0
var vallen_start := 0
var gegraven_kol := -1
var letter: FontVariation
var opnieuw := false           # oude save: na het welkom meteen graven, geen kijkstap
var geen_doel_t := 0.0

# Waar begint de les bij het laden van een save (los te toetsen). Geen save: 0 (welkom).
static func begin_uit_save(data: Dictionary) -> int:
	var st := clampi(int(data.get("uitleg", KLAAR)), WELKOM, KLAAR)
	if st == KLAAR and int(data.get("uitleg_v", 0)) < UITLEG_V:
		return WELKOM
	return st

static func opnieuw_uit_save(data: Dictionary) -> bool:
	return int(data.get("uitleg_v", 0)) < UITLEG_V and int(data.get("uitleg", KLAAR)) == KLAAR

func zet(strook, begin_stap: int) -> void:
	s = strook
	stap = clampi(begin_stap, WELKOM, KLAAR)
	letter = FontVariation.new()
	letter.base_font = FREDOKA
	letter.variation_opentype = {TextServerManager.get_primary_interface().name_to_tag("wght"): 600}
	goud_start = int(s.hol.goud)
	vallen_start = s.hol.vallen.size()
	s.hol.gegraven.connect(_gegraven)
	set_process(true)   # ook na de les: de Gloop-les kan terugkomen tot het kaartje één keer open was (#406)
	if stap != KLAAR:
		_log()

func actief() -> bool:
	return stap != KLAAR

# ---- Gloop-les: los te toetsen ----
static func gloop_les_mag(gezien: bool, stap_: int, ring: bool) -> bool:
	return ring and not gezien and stap_ == KLAAR

static func gloop_les_weg(t_: float, kaart: String, ring: bool) -> bool:
	return t_ >= GLOOP_MAX_S or kaart != "" or not ring

# Komt de Gloop-les terug? Alleen na de eerste minuut, zonder klik ooit, met de ring aan en lang genoeg rust (#406).
static func gloop_les_terug(gezien: bool, stap_: int, ring: bool, rust: float) -> bool:
	return not gezien and stap_ == KLAAR and ring and rust >= GLOOP_TERUG_S

# Hoe lang het welkom staat (#406): bij een oude save langer.
static func welkom_s(opnieuw_: bool) -> float:
	return WELKOM_OPNIEUW_S if opnieuw_ else WELKOM_S

# kern/kaartje.gd open roept dit: kaartje van Gloop open = les gehad (#406)
func kaartje_open(soort: String) -> void:
	if soort == "slijm" and not gloop_gezien:
		gloop_gezien = true
		s.log_regel("HOL uitleg gloop gehad: kaartje open t=%.1f" % s.t)

# kern/kaartje.gd tik roept dit als de ring aangaat
func ring_aan() -> void:
	if not gloop_les_mag(gloop_gezien, stap, true) or gloop_t >= 0.0:
		return
	gloop_t = 0.0
	gloop_rust = 0.0
	s.log_regel("HOL uitleg gloop aan t=%.1f %s" % [s.t, GLOOP_TEKST])
	set_process(true)
	queue_redraw()

func _gloop_tik(delta: float) -> void:
	gloop_t += delta
	var ring: bool = s.slijm != null and s.slijm.has_method("ring_aan") and s.slijm.ring_aan()
	if s.proef_uitleg_klik > 0.0 and gloop_t >= s.proef_uitleg_klik and s.kaart_soort == "":
		s.log_regel("HOL uitleg gloop proefklik")
		load("res://kern/kaartje.gd").open(s, "slijm")
	if gloop_les_weg(gloop_t, s.kaart_soort, ring):
		s.log_regel("HOL uitleg gloop weg t=%.1f na %.1f s (%s)" % [s.t, gloop_t,
			"klik" if s.kaart_soort != "" else ("ring uit" if not ring else "tijd")])
		gloop_t = -1.0
		gloop_rust = 0.0
	queue_redraw()

func _log() -> void:
	s.log_regel("HOL uitleg stap %d t=%.1f %s" % [stap, s.t, TEKST.get(stap, "")])

func _naar(n: int) -> void:
	stap = n
	stap_t = 0.0
	geen_doel_t = 0.0
	duw_t = -1.0
	if stap == VAL:
		vallen_start = s.hol.vallen.size()
	_log()
	if stap == KLAAR:
		if s.slijm != null and s.slijm.has_method("ring_aan") and s.slijm.ring_aan():
			ring_aan()   # de ring ging al aan tijdens de les: de Gloop-les nu
	queue_redraw()

func _gegraven(cel: Vector2i) -> void:
	gegraven_kol = cel.x
	if stap == GRAAF:
		_naar(VAL)

func _process(delta: float) -> void:
	if gloop_t >= 0.0:
		_gloop_tik(delta)
		return
	if stap == KLAAR:
		if not gloop_gezien:
			var ring: bool = s.slijm != null and s.slijm.has_method("ring_aan") and s.slijm.ring_aan()
			gloop_rust = gloop_rust + delta if ring else 0.0
			if gloop_les_terug(gloop_gezien, stap, ring, gloop_rust):
				ring_aan()
		return
	stap_t += delta
	match stap:
		WELKOM:
			if stap_t >= welkom_s(opnieuw):
				_naar(GRAAF if opnieuw else KIJK)
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
	if (stap == GRAAF or stap == VAL) and doel_kol() < 0:
		geen_doel_t += delta
		if geen_doel_t >= GEEN_DOEL_S:
			s.log_regel("HOL uitleg stap %d overgeslagen: geen plek" % stap)
			_naar(VAL if stap == GRAAF else KLAAR)
			queue_redraw()
			return
	else:
		geen_doel_t = 0.0
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
	if gloop_t >= 0.0:
		_teken_gloop()
		return
	if stap == KLAAR or stap == KIJK:
		return
	var t: String = TEKST.get(stap, "")
	var pijl_x := -1.0
	var vak := doel_vak()
	var sc: float = s.schaal
	if stap != WELKOM and vak.size.x > 0:
		pijl_x = vak.position.x + vak.size.x / 2.0
		# ademende gouden rand om het vak (1,2 s per keer, rustig: geen knipperen)
		var a := 0.7 + 0.3 * sin(stap_t * TAU / 1.2)
		draw_rect(vak.grow(-1.0), Color(1.0, 0.86, 0.42, 0.10 + 0.08 * a), true)
		draw_rect(vak.grow(-sc * 0.5), Color(1.0, 0.86, 0.42, a), false, sc)
	var groot := 1.0
	if duw_t >= 0.0 and stap_t - duw_t < 0.8:
		groot = 1.0 + 0.6 * sin((stap_t - duw_t) / 0.8 * PI)
	_teken_plaat(t, pijl_x, vak.position.y if pijl_x >= 0.0 else 0.0, stap_t, groot)

# Gloop-les: dezelfde plaat en pijl, de punt op de bovenkant van Gloop (met zijn hoeden), geen gouden vak (de ring is het vak)
func _teken_gloop() -> void:
	if s.slijm == null:
		return
	var sc: float = s.schaal
	var KJ = load("res://kern/kaartje.gd")
	var o: Vector2 = s.hol.position
	var gx: float = o.x + float(s.slijm.position.x) * sc
	var top: float = o.y + float(KJ.munt_top(s)) * sc - 2.0 * sc   # 2 spelpixels lucht boven zijn kruin
	_teken_plaat(GLOOP_TEKST, gx, top, gloop_t, 1.0)

# Plaat met de regel in de lucht boven het hol, en (pijl_x >= 0) een pijltje naar beneden tot doel_y (vensterpixels).
func _teken_plaat(t: String, pijl_x: float, doel_y_in: float, tijd: float, groot: float) -> void:
	var m := maat()
	var sc: float = s.schaal
	var lucht: float = s.hol.position.y + HOL.OPP * sc   # hoogte van de lucht boven het gras, in vensterpixels
	var tb := letter.get_string_size(t, HORIZONTAL_ALIGNMENT_LEFT, -1, m)
	# 28 nov (#333 c, "UI looks too plain"): een afgewerkt bordje in plaats van een dun lijntje: donkere buitenrand,
	# gouden rand die meegroeit met de schaal, glansstrook bovenin, donkere onderlip en een letter met schaduw.
	# Op 120 en lager blijft de maat van het bordje gelijk (rand 1, ruimte 6), alleen buitenrand, lip en glans komen erbij.
	var rand := maxf(1.0, roundf(sc * 0.4))
	var lip := maxf(1.0, roundf(sc * 0.4))
	var ruim := maxf(6.0, 2.0 * sc)
	var ph := float(m) + maxf(6.0, 1.6 * sc) + lip
	var py := maxf(0.0, lucht - ph - 1.0)
	# plaatje met de regel: naast de pijl, of midden boven het hol bij het welkom
	var px: float
	var pw := tb.x + 2.0 * ruim
	var hol_breed: float = (s.hol.max_kol + 1) * HOL.KOL * sc
	if pijl_x >= 0.0:
		px = pijl_x + 4.0 * sc
		if px + pw > hol_breed:
			px = pijl_x - 4.0 * sc - pw
	else:
		# welkom (#406): midden boven het hol zelf (ingang tot schat), niet boven het hele venster
		var midden: float = s.hol.position.x + (float(s.hol.ingang_kol + s.hol.schat_kol + 1) / 2.0) * HOL.KOL * sc
		px = midden - pw / 2.0
	# nooit over het bord rechts (kern/tekst.gd), daar zag Iris hem niet (#406)
	if s.tekst != null and s.tekst.has_method("vak_breedte"):
		var bord_x: float = s.tekst.position.x + s.tekst.paneel_links(s.tekst.breedte - s.tekst.vak_breedte() - 8) - 4.0
		px = minf(px, bord_x - pw)
	px = maxf(2.0, px)
	var plaat := Rect2(px, py, pw, ph)
	var rond := int(ph / 2.0)
	var buiten := _doos("buiten")
	buiten.set_corner_radius_all(rond + 1)
	draw_style_box(buiten, plaat.grow(1.0))
	var lp := _doos("lip")
	lp.set_corner_radius_all(rond)
	draw_style_box(lp, plaat)
	var sb := _doos("plaat")
	sb.set_border_width_all(int(rand))
	sb.set_corner_radius_all(int((ph - lip) / 2.0))
	draw_style_box(sb, Rect2(px, py, pw, ph - lip))
	var gl := _doos("glans")
	gl.set_corner_radius_all(int(ph * 0.2))
	draw_style_box(gl, Rect2(px + ph * 0.45, py + rand + maxf(1.0, sc * 0.3), pw - ph * 0.9, maxf(1.0, (ph - lip) * 0.18)))
	var ty := py + (ph - lip) / 2.0 + m * 0.36
	draw_string(letter, Vector2(px + ruim, ty + maxf(1.0, roundf(sc / 3.0))), t, HORIZONTAL_ALIGNMENT_LEFT, -1, m, Color(0.09, 0.04, 0.02, 0.7))
	draw_string(letter, Vector2(px + ruim, ty), t, HORIZONTAL_ALIGNMENT_LEFT, -1, m, Color("#ffe07a"))
	if pijl_x >= 0.0:
		# pijltje naar beneden in de lucht, wipt zacht 2 spelpixels; na 20 s niets één keer groter
		var wip := (0.5 + 0.5 * sin(tijd * TAU / 0.9)) * 2.0 * sc
		# De punt raakt de bovenkant van het doel. Ligt dat onder de grond (een vak in de gang, of Gloop), dan loopt
		# een steel door de grond, zodat je niet eerst naar het kamertje kijkt (Daan #64 C3).
		var bw := 3.5 * sc * groot
		var kop := 5.0 * sc * groot
		var top := py + 1.0 + wip
		var doel_y := maxf(lucht, doel_y_in) - 1.0
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
		draw_polyline(PackedVector2Array([pts[0], pts[1], pts[2], pts[0]]), donker, maxf(1.5, sc * 0.4), true)

# StyleBoxen van het bordje één keer maken (zoals tekst.gd _doos)
var dozen := {}

func _doos(naam: String) -> StyleBoxFlat:
	if dozen.has(naam):
		return dozen[naam]
	var sb := StyleBoxFlat.new()
	sb.anti_aliasing = true
	match naam:
		"buiten":
			sb.bg_color = Color(0.07, 0.03, 0.02, 0.85)
		"plaat":
			sb.bg_color = Color("#3a2016")
			sb.border_color = Color("#e8b040")
		"lip":
			sb.bg_color = Color("#8a5a18")   # donkere onderkant van de gouden rand
		"glans":
			sb.bg_color = Color(1.0, 0.86, 0.6, 0.16)
	dozen[naam] = sb
	return sb
