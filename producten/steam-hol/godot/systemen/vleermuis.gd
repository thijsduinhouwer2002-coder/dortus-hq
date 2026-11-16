extends Node2D
# Vleermuis (Bram 16 nov 2026, Mila 09:00 "Het Hol moet vol", punt 4b; model van Mila, blad uit de pijplijn).
# Hangt ondersteboven aan het gangplafond. Loopt er een held onder door, dan fladdert hij op naar een andere plek
# in de gang. Eén vleermuis vanaf MIN_GANG gangtegels, twee vanaf TWEE_GANG (een leeg hol blijft rustig).
# Zuinig: tekent alleen opnieuw als hij vliegt of verhuist (±1,2 s per keer); hangend kost hij niets.
# Kind van het hol, vóór Wezens: hij staat in spelpixels en de helden lopen voor hem langs.
# Zonder blad (kunst/3d/vleermuis.png) doet hij niets.

const BLAD_JSON := "res://kunst/3d/sprites.json"
const NAAM := "vleermuis"
const KOL := 16
const GANG_BOVEN := 24
const MIN_GANG := 10
const TWEE_GANG := 24
const VLIEG_S := 1.2      # zo lang duurt een vlucht
const SLAG_S := 0.08      # vleugels om de 0,08 s open of half dicht
const SCHRIK_X := 10.0    # held binnen zoveel spelpixels (x): opvliegen
const RUST_S := 2.0       # na het landen zo lang niet opnieuw schrikken
const VLIEG_MAAL := 0.6   # het vliegbeeld is breed (vleugels open); kleiner tekenen, dan is hij even groot als hangend
const BOOG := 5.0         # zoveel spelpixels zakt hij midden in de vlucht de gang in

var hol = null
var wezens: Node = null
var ct: CanvasTexture = null
var info := {}
var vm: Array = []        # per vleermuis: {"k": kolom, "naar": kolom, "t": tijd in de lucht of -1, "rust": s}
var _sleutel := ""
var _kijk_t := 0.0

func zet(h, w: Node) -> void:
	hol = h
	wezens = w
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
	herkies()

static func aantal(gang_tegels: int) -> int:
	if gang_tegels >= TWEE_GANG:
		return 2
	return 1 if gang_tegels >= MIN_GANG else 0

# Hangen mag onder een dicht plafond in de gang, niet bij schacht, val, Gloop en de schatkamer (zelfde plekken als spinrag).
static func mag_hangen(h, k: int) -> bool:
	if k <= h.ingang_kol + 1 or k >= h.schat_kol - 1 or k >= h.gang.size():
		return false
	return h.gang[k] and not h.boven[k] and not h.vallen.has(k)

static func plekken(h) -> Array:
	var uit: Array = []
	for k in h.gang.size():
		if mag_hangen(h, k):
			uit.append(k)
	return uit

# Vaste keuze per hol (hash zoals de versiering), minstens 3 kolommen uit elkaar.
static func kies(h, n: int) -> Array:
	var kand := plekken(h)
	kand.sort_custom(func(a, b): return h._hash(a, 11) > h._hash(b, 11) or (h._hash(a, 11) == h._hash(b, 11) and a < b))
	var uit: Array = []
	for k in kand:
		if uit.size() >= n:
			break
		var vrij := true
		for j in uit:
			if absi(int(j) - int(k)) < 3:
				vrij = false
		if vrij:
			uit.append(k)
	return uit

# Waarheen bij schrik: de dichtstbijzijnde vrije plek minstens 2 kolommen weg, liefst weg van de held.
static func vlucht_doel(h, van: int, held_x: float, bezet: Array) -> int:
	var beste := -1
	var beste_s := 1e9
	var weg_rechts: bool = held_x <= van * KOL + KOL / 2.0
	for k in plekken(h):
		if absi(k - van) < 2 or bezet.has(k):
			continue
		var s := float(absi(k - van))
		if (k > van) != weg_rechts:
			s += 100.0   # naar de held toe alleen als het niet anders kan
		if s < beste_s:
			beste_s = s
			beste = k
	return beste

# Plek van het midden van de vleermuis in de lucht, f van 0 tot 1: zacht op gang, boog de gang in, zacht landen.
static func vlucht_plek(van_x: float, naar_x: float, y: float, f: float) -> Vector2:
	var g := clampf(f, 0.0, 1.0)
	var z := g * g * (3.0 - 2.0 * g)
	return Vector2(lerpf(van_x, naar_x, z), y + sin(PI * g) * BOOG)

func _sleutel_nu() -> String:
	return "%d|%d|%d|%d|%d" % [hol.gang.count(true), hol.boven.count(true), hol.vallen.size(), hol.schat_kol, hol.ingang_kol]

func herkies() -> void:
	_sleutel = _sleutel_nu()
	var tegels := 0
	for b in hol.gang:
		if b:
			tegels += 1
	var gekozen := kies(hol, aantal(tegels))
	vm.clear()
	for k in gekozen:
		vm.append({"k": k, "naar": k, "t": -1.0, "rust": 0.0})
	queue_redraw()

func _process(delta: float) -> void:
	if ct == null or hol == null:
		return
	_kijk_t += delta
	if _kijk_t >= 1.0:   # gang of vallen veranderd (graven, kopen): opnieuw kiezen. Eén keer per seconde is genoeg.
		_kijk_t = 0.0
		if _sleutel_nu() != _sleutel:
			herkies()
	var bezet: Array = []
	for v in vm:
		bezet.append(v["naar"])
	for v in vm:
		if v["t"] >= 0.0:
			v["t"] += delta
			if v["t"] >= VLIEG_S:
				v["t"] = -1.0
				v["k"] = v["naar"]
				v["rust"] = RUST_S
			queue_redraw()
			continue
		if v["rust"] > 0.0:
			v["rust"] -= delta
			continue
		var held_x := _held_onder(int(v["k"]))
		if held_x > -1e8:
			var doel := vlucht_doel(hol, int(v["k"]), held_x, bezet)
			if doel >= 0:
				v["naar"] = doel
				v["t"] = 0.0
				bezet.append(doel)
				queue_redraw()

func _held_onder(k: int) -> float:
	if wezens == null:
		return -1e9
	var x := k * KOL + KOL / 2.0
	for w in wezens.get_children():
		if w.has_method("is_held") and w.position.y > GANG_BOVEN and absf(w.position.x - x) < SCHRIK_X:
			return w.position.x
	return -1e9

func _draw() -> void:
	if ct == null:
		return
	var px := float(info["px"])
	var cw := float(info["cel_px"][0])
	var ch := float(info["cel_px"][1])
	var ax := float(info["anker_x"])
	var tops: Array = info.get("top", [0, 0])
	for v in vm:
		if v["t"] < 0.0:
			# hangend: frame 0, bovenkant van het lijf 1 spelpixel onder het plafond
			var x := int(v["k"]) * KOL + KOL / 2.0 - ax / px
			var y := GANG_BOVEN + 1 - float(tops[0])
			draw_texture_rect_region(ct, Rect2(x, y, cw / px, ch / px), Rect2(0, 0, cw, ch))
		else:
			var f: float = v["t"] / VLIEG_S
			var p := vlucht_plek(int(v["k"]) * KOL + KOL / 2.0, int(v["naar"]) * KOL + KOL / 2.0, GANG_BOVEN + 4.0, f)
			var open := int(v["t"] / SLAG_S) % 2 == 0
			var b := cw / px * VLIEG_MAAL
			var hh := ch / px * VLIEG_MAAL * (1.0 if open else 0.55)
			draw_texture_rect_region(ct, Rect2(p.x - ax / px * VLIEG_MAAL, p.y - hh / 2.0, b, hh), Rect2(cw, 0, cw, ch))
