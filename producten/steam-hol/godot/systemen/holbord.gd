extends Node2D
# Bordje met het hol-niveau (Olaf 16 nov 2026, tekening en maten van Mila 16:20, plek keus A van Daan).
# Plankje op een paaltje links naast de stenen boog, in het gras. Blad `kunst/3d/holbord.png` (sprite `holbord`):
# cel `leeg` en `c0` tot `c9`, alle cellen 15 x 18 spelpixels met hetzelfde nulpunt (uitleg `ontwerp/steam/bordje/LEESMIJ.md`).
# Kind van het hol, vóór Wezens: het staat in spelpixels en de helden lopen ervoor langs.
# Zuinig: kijkt 10 keer per seconde of faam of de plek van de boog veranderde, en tekent alleen dan opnieuw (of tijdens de wip).
# Zonder blad doet het niets.

const BLAD_JSON := "res://kunst/3d/sprites.json"
const NAAM := "holbord"
const HN := preload("res://systemen/hol_niveau.gd")
const CEL := Vector2(15, 18)          # spelpixels
const LINKS_VAN_BOOG := 28.0          # Mila's proef: plank op spelpixel 4 bij de boog op 32 (ingang_kol 2)
const BOVEN := -1.0                   # bovenkant plank (rij 1 van de cel) op de vensterrand
const BALK_RIJ := 11.0
const BALK_HALF := 5.5
const LEEG_KLEUR := Color8(0x4e, 0x28, 0x1c)
const VOL_KLEUR := Color8(0xff, 0xe0, 0x7a)
const WIP_HOOG := 2.0                 # spelpixels
const WIP_S := 0.5
const KIJK_S := 0.1

var s = null          # de strook (faam, optocht)
var hol = null
var ct: CanvasTexture = null
var cw := 60
var ch := 72
var wip_t := -1.0
var _kijk_t := 0.0
var _faam := -1
var _x := -999.0
var _eerste := true
var hover := false   # muis op de plank (strook.gd _input)
var _niv := 1
var _niv_nu := 1

func zet(strook, h) -> void:
	s = strook
	hol = h
	if not FileAccess.file_exists(BLAD_JSON):
		return
	var d = JSON.parse_string(FileAccess.get_file_as_string(BLAD_JSON))
	if typeof(d) != TYPE_DICTIONARY or not d.has(NAAM) or typeof(d[NAAM]) != TYPE_DICTIONARY:
		return
	var blad := str(d[NAAM].get("blad", ""))
	if not ResourceLoader.exists(blad):
		return
	var cp = d[NAAM].get("cel_px", [60, 72])
	cw = int(cp[0])
	ch = int(cp[1])
	ct = CanvasTexture.new()
	ct.diffuse_texture = load(blad)
	ct.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS

func actief() -> bool:
	return ct != null

# Links van de plank (spelpixels); de boog schuift mee als het hol naar links groeit.
func plank_x() -> float:
	if hol == null:
		return 4.0
	return maxf(1.0, float(hol._ingang_x()) - LINKS_VAN_BOOG)

# Rechthoek van de plank in spelpixels (voor hover en toetsen).
func vlak() -> Rect2:
	return Rect2(plank_x(), BOVEN, CEL.x, CEL.y)

# "Level 5: the Thief. 12 more heroes."; met iets in de rij "7 levels waiting. Next in 2 min." (Sanne 16:00)
func hover_tekst() -> String:
	if s == null:
		return ""
	if int(s.rij) > 0:
		return HN.rij_hover(int(s.rij), float(s.rij_t))
	return HN.hover(int(s.faam))

func wip() -> void:
	if ct == null:
		return
	wip_t = 0.0
	queue_redraw()

func _process(delta: float) -> void:
	if s == null:
		return
	# rij bij de ingang (Sanne 16 nov 16:00): elke RIJ_S open seconden komt er één niveau uit de rij, met de wip
	if int(s.rij) > 0:
		s.rij_t += delta
		if s.rij_t >= HN.RIJ_S:
			s.rij_t = 0.0
			s.rij = int(s.rij) - 1
			s.log_regel("HOL rij: niveau %d uit de rij, nog %d" % [HN.zichtbaar(int(s.faam), int(s.rij)), int(s.rij)])
			_faam = -2   # opnieuw kijken: wip en tekenen
	if ct == null:
		return
	if wip_t >= 0.0:
		wip_t += delta
		if wip_t >= WIP_S:
			wip_t = -1.0
		queue_redraw()
	_kijk_t += delta
	if _kijk_t < KIJK_S:
		return
	_kijk_t = 0.0
	var f: int = int(s.faam)
	var x := plank_x()
	if f != _faam or x != _x:
		_niv_nu = HN.zichtbaar(f, int(s.rij))
		var oud_niv: int = _niv
		_faam = f
		_x = x
		_niv = _niv_nu
		if _eerste:
			_eerste = false
			# na weg zijn wipt het bordje één keer (Sanne 14:50); de optocht zelf komt later
			if typeof(s.optocht) == TYPE_DICTIONARY and bool(s.optocht.get("wip", false)):
				wip()
				s.log_regel("HOL bordje wip na weg (niveau %d)" % _niv)
		elif _niv > oud_niv:
			wip()
			s.log_regel("HOL bordje wip niveau %d" % _niv)
		queue_redraw()

static func cijfers(n: int) -> Array:
	var t := str(clampi(n, 0, 99))
	if t.length() == 1:
		return [[int(t), 0.0]]
	return [[int(t[0]), -2.5], [int(t[1]), 2.5]]

func _draw() -> void:
	if ct == null or s == null:
		return
	var y := BOVEN
	if wip_t >= 0.0:
		y -= round(WIP_HOOG * sin(PI * wip_t / WIP_S))
	var x := plank_x()
	draw_texture_rect_region(ct, Rect2(x, y, CEL.x, CEL.y), Rect2(0, 0, cw, ch))
	var f: int = maxi(0, int(s.faam))
	var rij: int = int(s.rij)
	for c in cijfers(HN.zichtbaar(f, rij)):
		draw_texture_rect_region(ct, Rect2(x + float(c[1]), y, CEL.x, CEL.y), Rect2((1 + int(c[0])) * cw, 0, cw, ch))
	var mid := x + CEL.x / 2.0
	var by := y + BALK_RIJ
	draw_rect(Rect2(mid - BALK_HALF, by, 2.0 * BALK_HALF, 1.0), LEEG_KLEUR)
	var d := 1.0 if rij > 0 else HN.deel(f)   # met iets in de rij staat het balkje vol
	var vol: float = round(2.0 * BALK_HALF * d * 3.0) / 3.0   # op schermpixels bij schaal 3
	if vol > 0.0:
		draw_rect(Rect2(mid - BALK_HALF, by, vol, 1.0), VOL_KLEUR)
