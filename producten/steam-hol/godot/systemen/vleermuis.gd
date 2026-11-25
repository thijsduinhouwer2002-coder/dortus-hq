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
# Held binnen zoveel spelpixels (x): opvliegen. Daan #59: met 10 liep de held een halve seconde door hem heen,
# want de vleermuis is 18 breed en de held 10: ze raken elkaar al op 14. Op 26 is er 12 px lucht, ook voor de
# eerste held die 2 keer zo snel loopt (±15 px/s: 0,8 s, dan is de vleermuis al driekwart weg).
const SCHRIK_X := 26.0
const TERUG_TEMPO := 2.0  # zoveel keer sneller als hij langs de held moet (klem aan het eind van de gang)
const UITWIJK_X := 20.0   # geen andere plek: zoveel spelpixels achter de held gaan fladderen
const ZWEEF_MIN_S := 0.6  # minstens zo lang fladderen voor hij terugvliegt
const RAAK_X := 15.0      # zo dichtbij raken held en vleermuis elkaar: dan ook tijdens de rust weg
const RUST_S := 2.0       # na het landen zo lang niet opnieuw schrikken (behalve bij RAAK_X)
const VLIEG_MAAL := 0.6   # het vliegbeeld is breed (vleugels open); kleiner tekenen, dan is hij even groot als hangend
const BOOG := 1.5         # zoveel spelpixels zakt hij midden in de vlucht; klein, want de held is bijna zo hoog als de gang
const VLIEG_Y := 3.5      # midden van de vliegende vleermuis zoveel onder het gangplafond (boven de hoofden)
# Nooit achter de hoedenberg (Mila 17 nov 08:00, moet Daan 07:45): de rechterrand van zijn tegel ligt minstens zoveel
# spelpixels links van Gloops midden. Volle berg 8 onderaan: x = -12 - 6*7 - 3 = -57, plus halve hoed en lucht; groot lijf -59.
# Keer de schaal van Gloop (proef_figuur), want de berg schaalt mee.
const BERG_MARGE := 70.0
const BERG_MARGE_GROOT := 72.0

var hol = null
var wezens: Node = null
var ct: CanvasTexture = null
var info := {}
var vm: Array = []        # per vleermuis: {"k": kolom, "naar": kolom, "t": tijd in de lucht of -1, "rust": s}
var _sleutel := ""
var _kijk_t := 1.0   # 1: het eerste beeld kijkt meteen, dan staat Gloop er al (strook.gd zet hem na zet())
var _grens := 1e9     # rechterrand van een hangplek hooguit hier (spelpixels); 1e9 = geen Gloop gevonden
# vleermuis_proef=1 (alleen om op te keuren, leest de startargumenten zelf): elke vleermuis vliegt om de 4 s op,
# ook zonder held eronder. In het echte spel nooit.
var proef := "vleermuis_proef=1" in OS.get_cmdline_user_args()
var _proef_t := 0.0

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
# grens: de rechterrand van de tegel (k * KOL + KOL) mag niet rechts hiervan liggen (hoedenberg, zie BERG_MARGE).
static func mag_hangen(h, k: int, grens := 1e9) -> bool:
	if k <= h.ingang_kol + 1 or k >= h.schat_kol - 1 or k >= h.gang.size():
		return false
	if k * KOL + KOL > grens:
		return false
	return h.gang[k] and not h.boven[k] and not h.vallen.has(k)

# Uiterste rechterrand voor een hangplek bij Gloop op gloop_x: zijn volle berg plus lucht, keer zijn schaal.
static func berg_grens(gloop_x: float, groot: bool, schaal := 1.0) -> float:
	return gloop_x - (BERG_MARGE_GROOT if groot else BERG_MARGE) * maxf(1.0, schaal)

static func plekken(h, grens := 1e9) -> Array:
	var uit: Array = []
	var bezet := vol_plafond_kols(h)
	for k in h.gang.size():
		if mag_hangen(h, k, grens) and not bezet.has(k):
			uit.append(k)
	return uit

# In een vol hol (Olaf, hol_vast.gd) hangt aan veel plafondtegels al een stut, spinrag of vaandel: daar hangt
# geen vleermuis (kan Olaf 16 nov 09:45). Zelfde loop als hol_vast.gd _teken_vol(), zodat de kolommen precies kloppen.
# Zonder is_vol/vol_plafond in hol_vast.gd (oudere versie) geeft dit niets terug.
static func vol_plafond_kols(h) -> Dictionary:
	var uit := {}
	var HV = load("res://hol/hol_vast.gd")
	if HV == null:
		return uit
	var namen := {}
	for m in HV.get_script_method_list():
		namen[m["name"]] = true
	if not (namen.has("is_vol") and namen.has("vol_plafond")) or not HV.is_vol(h):
		return uit
	var vorige := -99
	for k in range(h.ingang_kol + 1, h.schat_kol - 1):
		if k >= h.boven.size():
			break
		if HV.vol_plafond(h, k, vorige) >= 0:
			uit[k] = true
			vorige = k
	return uit

# Vaste keuze per hol (hash zoals de versiering), minstens 3 kolommen uit elkaar.
static func kies(h, n: int, grens := 1e9) -> Array:
	var kand := plekken(h, grens)
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

# Waarheen bij schrik: de dichtstbijzijnde vrije plek minstens 2 kolommen weg, liefst weg van de held,
# en niet boven een andere held (helden_x: hun x; daar zou hij meteen weer opvliegen).
static func vlucht_doel(h, van: int, held_x: float, bezet: Array, grens := 1e9, helden_x: Array = []) -> int:
	var beste := -1
	var beste_s := 1e9
	var weg_rechts: bool = held_x <= van * KOL + KOL / 2.0
	for k in plekken(h, grens):
		if absi(k - van) < 2 or bezet.has(k):
			continue
		var s := float(absi(k - van))
		if (k > van) != weg_rechts:
			s += 100.0   # naar de held toe alleen als het niet anders kan
		for hx in helden_x:
			if absf(float(hx) - (k * KOL + KOL / 2.0)) < SCHRIK_X:
				s += 50.0   # boven een held landen alleen als het niet anders kan
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
	_grens = _grens_nu()
	return "%d|%d|%d|%d|%d|%d" % [hol.gang.count(true), hol.boven.count(true), hol.vallen.size(), hol.schat_kol, hol.ingang_kol, int(_grens)]

# Gloop staat in Wezens (het kind met berg() en is_groot()); zonder Gloop geen grens.
func _grens_nu() -> float:
	if wezens == null:
		return 1e9
	for w in wezens.get_children():
		if w.has_method("berg") and w.has_method("is_groot"):
			return berg_grens(w.position.x, w.is_groot(), absf(w.scale.x))
	return 1e9

func herkies() -> void:
	_sleutel = _sleutel_nu()
	var tegels := 0
	for b in hol.gang:
		if b:
			tegels += 1
	var gekozen := kies(hol, aantal(tegels), _grens)   # past er geen plek (kort hol), dan geen vleermuis
	vm.clear()
	for k in gekozen:
		vm.append({"k": k, "naar": k, "t": -1.0, "rust": 0.0, "zweef_t": -1.0})
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
			v["t"] += delta * float(v.get("tempo", 1.0))
			if v["t"] >= VLIEG_S:
				v["t"] = -1.0
				v["tempo"] = 1.0
				if v.get("uitwijk", false):
					v["uitwijk"] = false
					v["zweef_t"] = 0.0   # niet landen: fladderen tot de held voorbij zijn plek is
				else:
					v["k"] = v["naar"]
					v["rust"] = RUST_S
			queue_redraw()
			continue
		var thuis := int(v["k"]) * KOL + KOL / 2.0
		var held_x := _held_onder(int(v["k"]))
		if float(v.get("zweef_t", -1.0)) >= 0.0:
			v["zweef_t"] += delta
			queue_redraw()
			if held_x < -1e8 and v["zweef_t"] >= ZWEEF_MIN_S:   # held voorbij: terug naar zijn plek
				v["zweef_t"] = -1.0
				_vlieg(v, float(v["naar_x"]), thuis, int(v["k"]), 1.0)
			continue
		if v["rust"] > 0.0:
			v["rust"] -= delta
			if held_x < -1e8 or absf(held_x - thuis) >= RAAK_X:
				continue
		if proef and held_x < -1e8:
			_proef_t += delta
			if _proef_t >= 4.0:
				_proef_t = 0.0
				held_x = int(v["k"]) * KOL + 2.0
		if held_x > -1e8:
			var doel := vlucht_doel(hol, int(v["k"]), held_x, bezet, _grens, _helden_x())
			if doel >= 0:
				# Klem aan het eind van de gang: dan moet hij langs de held. Dat doet hij snel (0,6 s), achter
				# het hoofd langs, zodat het leest als wegfladderen en niet als er doorheen lopen (Daan #59).
				var naar := doel * KOL + KOL / 2.0
				_vlieg(v, thuis, naar, doel, TERUG_TEMPO if (naar > thuis) == (held_x > thuis) else 1.0)
				bezet.append(doel)
			else:
				# Geen andere plek (kort hol, zoals de eerste minuut: alleen tussen ladder en put): snel langs de held
				# naar achter hem, daar fladderen tot hij voorbij is, dan terug (Daan #59: niet meer stil laten hangen).
				var achter := held_x + (UITWIJK_X if held_x > thuis else -UITWIJK_X)
				achter = clampf(achter, hol.ingang_kol * KOL + KOL / 2.0, hol.schat_kol * KOL + KOL / 2.0)   # in de schacht mag, in de grond niet
				_vlieg(v, thuis, achter, int(v["k"]), TERUG_TEMPO)
				v["uitwijk"] = true

func _vlieg(v: Dictionary, van_x: float, naar_x: float, naar_k: int, tempo: float) -> void:
	v["van_x"] = van_x
	v["naar_x"] = naar_x
	v["naar"] = naar_k
	v["t"] = 0.0
	v["tempo"] = tempo
	queue_redraw()

# Midden van een vliegende of fladderende vleermuis (alleen geldig als hij niet hangt).
func lucht_plek(v: Dictionary) -> Vector2:
	if v["t"] >= 0.0:
		return vlucht_plek(float(v["van_x"]), float(v["naar_x"]), GANG_BOVEN + VLIEG_Y, v["t"] / VLIEG_S)
	return Vector2(float(v["naar_x"]), GANG_BOVEN + VLIEG_Y + sin(float(v["zweef_t"]) * 5.0) * 0.8)

func _held_onder(k: int) -> float:
	if wezens == null:
		return -1e9
	var x := k * KOL + KOL / 2.0
	var beste := -1e9
	for w in wezens.get_children():   # de dichtstbijzijnde held binnen SCHRIK_X
		if w.has_method("is_held") and w.position.y > GANG_BOVEN and absf(w.position.x - x) < SCHRIK_X:
			if beste < -1e8 or absf(w.position.x - x) < absf(beste - x):
				beste = w.position.x
	return beste

func _helden_x() -> Array:
	var uit: Array = []
	if wezens != null:
		for w in wezens.get_children():
			if w.has_method("is_held") and w.position.y > GANG_BOVEN:
				uit.append(w.position.x)
	return uit

func _draw() -> void:
	if ct == null:
		return
	var px := float(info["px"])
	var cw := float(info["cel_px"][0])
	var ch := float(info["cel_px"][1])
	var ax := float(info["anker_x"])
	var tops: Array = info.get("top", [0, 0])
	for v in vm:
		if v["t"] < 0.0 and float(v.get("zweef_t", -1.0)) < 0.0:
			# hangend: frame 0, bovenkant van het lijf 1 spelpixel onder het plafond
			var x := int(v["k"]) * KOL + KOL / 2.0 - ax / px
			var y := GANG_BOVEN + 1 - float(tops[0])
			draw_texture_rect_region(ct, Rect2(x, y, cw / px, ch / px), Rect2(0, 0, cw, ch))
		else:
			var p := lucht_plek(v)
			var open := int((v["t"] if v["t"] >= 0.0 else float(v["zweef_t"])) / SLAG_S) % 2 == 0
			var b := cw / px * VLIEG_MAAL
			var hh := ch / px * VLIEG_MAAL * (1.0 if open else 0.55)
			draw_texture_rect_region(ct, Rect2(p.x - ax / px * VLIEG_MAAL, p.y - hh / 2.0, b, hh), Rect2(cw, 0, cw, ch))
