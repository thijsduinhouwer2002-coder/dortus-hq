extends Node2D
# Hoedenwand (Bram 16 nov 2026, idee en model van Mila, "Het Hol moet vol" punt 4; voorstel aan Olaf, hij beslist).
# Elke held die Gloop opat laat een hoed achter die scheef half in de aardwand boven de gang steekt: de wand is het
# logboek van wie Gloop at. Eén hoed per gangkolom zonder kamer erboven, de oudste hoeden eerst (slijm.hoeden,
# oudste vooraan), op vaste hash-plekken. Een jong hol heeft dus een paar hoeden in de wand, een oud hol een volle wand.
# Zuinig: tekent alleen opnieuw als er een hoed bijkomt of het hol verandert (kijkt één keer per seconde).
# Kind van het hol, vóór Vleermuis en Wezens. Zonder blad (kunst/3d/hoedenwand.png) doet hij niets.

const BLAD_JSON := "res://kunst/3d/sprites.json"
const NAAM := "hoedenwand"
const KOL := 16
const MIDDEN_Y := [14, 15, 16, 17, 18, 19]   # midden van de hoed in spelpixels (gras tot 8, gang vanaf 24)

var hol = null
var slijm = null
var ct: CanvasTexture = null
var info := {}
var _sleutel := ""
var _kijk_t := 0.0

func zet(h, s) -> void:
	hol = h
	slijm = s
	if not FileAccess.file_exists(BLAD_JSON):
		return
	var d = JSON.parse_string(FileAccess.get_file_as_string(BLAD_JSON))
	if typeof(d) != TYPE_DICTIONARY or not d.has(NAAM) or typeof(d[NAAM]) != TYPE_DICTIONARY:
		return
	var blad := str(d[NAAM].get("blad", ""))
	if not ResourceLoader.exists(blad):
		return
	info = d[NAAM]
	ct = CanvasTexture.new()
	ct.diffuse_texture = load(blad)
	ct.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS
	queue_redraw()

# Kolommen waar een hoed in de wand mag: boven gegraven gang, geen kamer erboven, niet bij de schacht en niet boven
# de schatkamer (daar staan Gloop en zijn toren). Volgorde: vaste hash, zodat de wand elke start gelijk vult.
static func plekken(h) -> Array:
	var uit: Array = []
	for k in range(h.ingang_kol + 1, mini(h.schat_kol - 1, h.gang.size())):
		if h.gang[k] and not h.boven[k]:
			uit.append(k)
	uit.sort_custom(func(a, b): return h._hash(a, 23) > h._hash(b, 23) or (h._hash(a, 23) == h._hash(b, 23) and a < b))
	return uit

# [{k, nr, y, dx}] voor de hoeden die in de wand zitten: de oudste hoeden eerst, zoveel als er plek is.
static func indeling(h, hoeden: Array) -> Array:
	var p := plekken(h)
	var uit: Array = []
	for i in mini(p.size(), hoeden.size()):
		var k: int = p[i]
		uit.append({"k": k, "nr": int(hoeden[i]) % 10, "y": MIDDEN_Y[h._hash(k, 29) % MIDDEN_Y.size()], "dx": h._hash(k, 31) % 3 - 1})
	return uit

func _hoeden() -> Array:
	if slijm == null or not ("hoeden" in slijm):
		return []
	return slijm.hoeden

func _sleutel_nu() -> String:
	return "%d|%d|%d|%d|%d" % [_hoeden().size(), hol.gang.count(true), hol.boven.count(true), hol.schat_kol, hol.ingang_kol]

func _process(delta: float) -> void:
	if ct == null or hol == null:
		return
	_kijk_t += delta
	if _kijk_t >= 1.0:
		_kijk_t = 0.0
		var s := _sleutel_nu()
		if s != _sleutel:
			_sleutel = s
			queue_redraw()

func _draw() -> void:
	if ct == null or hol == null:
		return
	var px := float(info["px"])
	var cw := float(info["cel_px"][0])
	var ch := float(info["cel_px"][1])
	var ax := float(info["anker_x"])
	for d in indeling(hol, _hoeden()):
		var x: float = d["k"] * KOL + KOL / 2.0 + d["dx"] - ax / px
		var y: float = d["y"] - ch / px / 2.0
		draw_texture_rect_region(ct, Rect2(x, y, cw / px, ch / px), Rect2(int(d["nr"]) * cw, 0, cw, ch))
