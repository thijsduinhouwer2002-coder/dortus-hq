extends RefCounted
# Worm en mot in het klein leven (Olaf 26 nov, issue #190). Bladen en model van Mila (#179, Daan #180 ja met een 8):
# kunst/3d/worm.png (op, piek, links, rechts) en mot.png (open, dicht), gegevens in kunst/3d/sprites.json zoals de vleermuis
# (px bladpixels per spelpixel, anker_x in bladpixels, nul_y in spelpixels vanaf de bovenkant van de cel).
# - worm: steekt zijn kop uit een hoopje aarde op de gangvloer en kijkt rond, volgorde van Mila: piek, op, links, op, rechts,
#   op, piek; zacht in en uit (4 stappen). Alleen een nieuw beeld als de stand verandert (±2 per s, 8 per s tijdens het faden).
# - mot: fladdert een lusje rond de fakkelvlam, vleugels om en om open en dicht (leven.gd tekent hem met 12 beelden per s).
# Plek van de worm: een gewone gangtegel, niet bij schacht, val, vloerding, stut, Gloop en zijn hoedenberg, en geen held
# dichtbij (een held die over een worm loopt leest als een fout). Zonder blad komen ze niet (leven.gd beest == null).

const BLAD_JSON := "res://kunst/3d/sprites.json"
const KOL := 16
const GANG_ONDER := 38          # vloerlijn van een figuur (hol.gd)
const GANG_BOVEN := 24
const WORM_REEKS := [1, 0, 2, 0, 3, 0, 1]   # index in frames: op 0, piek 1, links 2, rechts 3
const FADE_S := 0.5
const FADE_STAP := 4
const HELD_VER := 48.0          # geen held binnen zoveel spelpixels als de worm begint (held ±5 px/s, worm 4,2 s)
const TROON := 3                # niet op de laatste tegels voor de schat (Gloop staat op schat_kol - 2)
const BERG_MARGE := 70.0        # zelfde als vleermuis.gd: rechts hiervan van Gloop af ligt zijn hoedenberg
const MOT_RX := 6.0             # lusje rond de vlam (spelpixels)
const MOT_RY := 2.5
const MOT_HOOG := -6.0          # midden van de lus zoveel boven de vlam (negatief: eronder; de vlam hangt vlak onder het plafond)
const MOT_SLAG := 7.0           # vleugels per seconde om

var worm := {}
var mot := {}
var worm_ct: CanvasTexture = null
var mot_ct: CanvasTexture = null

static func laad():
	if not FileAccess.file_exists(BLAD_JSON):
		return null
	var d = JSON.parse_string(FileAccess.get_file_as_string(BLAD_JSON))
	if typeof(d) != TYPE_DICTIONARY or not d.has("worm") or not d.has("mot"):
		return null
	var b = load("res://systemen/leven_beest.gd").new()
	b.worm = d["worm"]
	b.mot = d["mot"]
	b.worm_ct = _ct(str(b.worm.get("blad", "")))
	b.mot_ct = _ct(str(b.mot.get("blad", "")))
	if b.worm_ct == null or b.mot_ct == null:
		return null
	return b

static func _ct(pad: String) -> CanvasTexture:
	if not ResourceLoader.exists(pad):
		return null
	var ct := CanvasTexture.new()
	ct.diffuse_texture = load(pad)
	ct.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS   # zoals de vleermuis
	return ct

# dekking op tijd t van d seconden, in FADE_STAP stappen (zo blijft het aantal nieuwe beelden klein)
static func dek_stap(t: float, d: float) -> int:
	var f := clampf(minf(t / FADE_S, (d - t) / FADE_S), 0.0, 1.0)
	return int(ceil(f * FADE_STAP))

# stand van de worm: beeld uit de reeks keer 10 plus de dekstap; verandert die, dan pas opnieuw tekenen
static func worm_stand(t: float, d: float) -> int:
	var i := clampi(int(t / (d / WORM_REEKS.size())), 0, WORM_REEKS.size() - 1)
	return WORM_REEKS[i] * 10 + dek_stap(t, d)

static func _gloop(h):
	var w = h.get_node_or_null("Wezens")
	if w == null:
		return null
	for c in w.get_children():
		if c.has_method("berg") and c.has_method("is_groot"):
			return c
	return null

# gangkolommen waar een worm kan (zonder te kijken naar helden)
static func worm_kolommen(h) -> Array:
	var HV = load("res://hol/hol_vast.gd")
	var bezet := {}
	var vol: bool = HV.is_vol(h)
	if vol:
		for ding in HV.vol_rij(h):
			if not ding[2] or int(ding[1]) == 7:   # vloerding of stut
				bezet[int(ding[0])] = true
	else:   # zelfde lus als hol_vast.gd teken(): hh onder 14 is een stut, onder 30 een vloerding
		var vorige := -99
		for k in range(h.ingang_kol + 1, h.schat_kol - 1):
			if h.vallen.has(k):
				continue
			var hh: int = HV.deco_hh(h, k, h._hash(k, 7), vorige)
			if hh < 30 or (hh < 36 and not h.boven[k]):
				vorige = k
			if hh < 30:
				bezet[k] = true
	var grens := 1e9
	var g = _gloop(h)
	if g != null:
		grens = g.position.x - BERG_MARGE * maxf(1.0, absf(g.scale.x))
	var uit: Array = []
	for k in range(h.ingang_kol + 2, h.schat_kol - TROON):
		if k >= h.gang.size() or not h.gang[k] or bezet.has(k) or (vol and HV.is_los(h, k)) or HV.vloer_dicht(h, k):
			continue
		if k * KOL + KOL > grens:
			continue
		uit.append(k)
	return uit

# plek (midden van het hoopje op de vloer) voor een worm, of null; willekeurig uit de vrije kolommen
static func worm_plek(h, rng: RandomNumberGenerator):
	var helden: Array = []
	var w = h.get_node_or_null("Wezens")
	if w != null:
		for c in w.get_children():
			if c.has_method("is_held") and c.position.y > GANG_BOVEN:
				helden.append(c.position.x)
	var vrij: Array = []
	for k in worm_kolommen(h):
		var x: float = k * KOL + KOL / 2.0
		var ok := true
		for hx in helden:
			if absf(float(hx) - x) < HELD_VER:
				ok = false
		if ok:
			vrij.append(x)
	if vrij.is_empty():
		return null
	return Vector2(vrij[rng.randi_range(0, vrij.size() - 1)], GANG_ONDER)

func teken_worm(c: CanvasItem, plek: Vector2, t: float, d: float) -> void:
	var st := worm_stand(t, d)
	var f: int = st / 10
	var a := float(st % 10) / FADE_STAP
	if a <= 0.0:
		return
	var px := float(worm["px"])
	var cw := float(worm["cel_px"][0])
	var ch := float(worm["cel_px"][1])
	var nul: float = float(worm["nul_y"][f])
	var x := roundf(plek.x - float(worm["anker_x"]) / px)
	c.draw_texture_rect_region(worm_ct, Rect2(x, plek.y - nul, cw / px, ch / px), Rect2(f * cw, 0, cw, ch), Color(1, 1, 1, a))

# midden van de mot op tijd t, rond de vlam op plek
static func mot_plek(plek: Vector2, t: float) -> Vector2:
	var a := t * 1.8
	var p := plek + Vector2(cos(a) * MOT_RX, sin(a * 2.0) * MOT_RY - MOT_HOOG)
	return p

func teken_mot(c: CanvasItem, plek: Vector2, t: float, d: float) -> void:
	var a := clampf(minf(t / FADE_S, (d - t) / FADE_S), 0.0, 1.0)
	if a <= 0.0:
		return
	var f := int(t * MOT_SLAG) % 2
	var px := float(mot["px"])
	var cw := float(mot["cel_px"][0])
	var ch := float(mot["cel_px"][1])
	var p := mot_plek(plek, t)
	var nul: float = float(mot["nul_y"][f])
	var y := maxf(p.y - nul, GANG_BOVEN + 1.0)   # nooit door het plafond
	c.draw_texture_rect_region(mot_ct, Rect2(p.x - float(mot["anker_x"]) / px, y, cw / px, ch / px),
			Rect2(f * cw, 0, cw, ch), Color(1, 1, 1, a))
