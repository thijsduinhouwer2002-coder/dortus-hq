# Het Hol: welk deel van het venster de muis vangt (Olaf 15 nov, uit kern/strook.gd gehaald; regel: bestand onder ±400).
# Alleen statische functies met de strook als eerste argument (`s`). De toestand (vangt_y, vlak_paneel, vlak_gloop,
# lucht_gemeld) blijft in strook.gd; strook.gd heeft dunne doorgeefluiken _muis_vlak, muis_vlak_punten en gloop_bult.
#
# Normaal het hol plus wat erboven getekend staat; bij hover ook het paneel met drie regels, want dat reikt bij 96 px
# tot boven het maaiveld en zou anders meteen weer dichtklappen (controleur 00:30). Lege lucht laat klikken altijd door
# naar het venster erachter.
# Let op (Bram 14 nov 02:35, Godot 4.3 DisplayServer.xml): op Windows tekent het venster NIETS buiten dit vlak. Daarom
# volgt het vlak de bovenrand van gras, plantjes en ingang (hol_vast.gd `rand`, één keer gemeten na elk nieuw vast
# beeld) en een bult boven Gloop met zijn hoedentoren (rust-hoogte, zodat het vlak niet bij elke wip verandert).
# Besluit Olaf 14 nov 03:30: gras en toren zichtbaar, de paar spelpixels gras vangen dan ook de muis.
extends RefCounted

const HOL := preload("res://hol/hol.gd")
const BALK := preload("res://kern/balk.gd")

# Olaf 25 nov (issue #24): draait hol-balk.exe, dan krijgt dat het vlak en laat het de muis buiten het vlak door met
# WS_EX_TRANSPARENT. Het venster zelf vangt dan overal (geen passthrough), dus er wordt niets meer weggeknipt.
static func zet(s, paneel: bool) -> void:
	s.vlak_paneel = paneel
	if BALK.actief():
		var t := tops(s, paneel)
		BALK.vlak(t)
		_meld_lucht(s, t)
		if not s.balk_vol:
			s.balk_vol = true
			DisplayServer.window_set_mouse_passthrough(PackedVector2Array())
		return
	DisplayServer.window_set_mouse_passthrough(punten(s, paneel))

# De punten van het vlak (los, voor de toetsen). Per pixelkolom een bovenkant, gelijke stukken samengevoegd.
static func punten(s, paneel: bool) -> PackedVector2Array:
	var w := DisplayServer.window_get_size()
	var t := tops(s, paneel)
	var vlak := PackedVector2Array([Vector2(0, w.y)])
	var x0 := 0
	for x in range(1, w.x + 1):
		if x == w.x or t[x] != t[x0]:
			vlak.append(Vector2(x0, t[x0]))
			vlak.append(Vector2(x, t[x0]))
			x0 = x
	vlak.append(Vector2(w.x, w.y))
	_meld_lucht(s, t)
	return vlak

# Per pixelkolom de bovenkant van wat de muis vangt (venster-pixels).
static func tops(s, paneel: bool) -> PackedInt32Array:
	var hol = s.hol
	var w := DisplayServer.window_get_size()
	var uit := PackedInt32Array()
	uit.resize(w.x)
	uit.fill(s.vangt_y)
	var boven: int = s.vangt_y - HOL.OPP * s.schaal
	var r: PackedInt32Array = hol.vast.rand if hol != null and hol.vast != null else PackedInt32Array()
	var hx := int(hol.position.x) if hol != null else 0   # nu altijd 0, maar zelfde som als gloop_bult (controleur kan 3)
	for x in r.size():
		if x + hx >= 0 and x + hx < w.x:
			uit[x + hx] = mini(uit[x + hx], boven + r[x])
	s.vlak_gloop = gloop_bult(s)
	for x in range(maxi(0, s.vlak_gloop.x), mini(w.x, s.vlak_gloop.y)):
		uit[x] = mini(uit[x], s.vlak_gloop.z)
	if paneel and s.tekst and s.tekst.has_method("hover_vak"):
		var pr: Rect2 = s.tekst.hover_vak()
		var top := int(clampf(pr.position.y, 0.0, float(s.vangt_y)))
		for x in range(int(clampf(pr.position.x, 0.0, float(w.x))), w.x):
			uit[x] = mini(uit[x], top)
	return uit

static func _meld_lucht(s, t: PackedInt32Array) -> void:
	var r: PackedInt32Array = s.hol.vast.rand if s.hol != null and s.hol.vast != null else PackedInt32Array()
	if not s.lucht_gemeld and r.size() > 0:
		s.lucht_gemeld = true
		# voor de Windows-stap "Klikken door de lucht": een plek waar echt lucht is (4 px onder de bovenrand)
		var vrij := -1
		for x in range(200, mini(t.size(), r.size())):
			if t[x] > 4 + 2 * s.schaal:
				vrij = x
				break
		s.log_regel("HOL muisvlak %s, lucht vrij op x=%d" % ["via de balk" if BALK.actief() else "passthrough", vrij])

# Bult boven Gloop: van de bovenkant van zijn toren (in rust) tot het maaiveld, zo breed als hij met hoeden is.
static func gloop_bult(s) -> Vector3i:
	var hol = s.hol
	var slijm = s.slijm
	if slijm == null or hol == null or not slijm.has_method("hoogste_punt_rust"):
		return Vector3i(-1, -1, -1)
	var boven: int = s.vangt_y - HOL.OPP * s.schaal
	var rel := float(slijm.hoogste_punt_rust())   # in Gloop-pixels; figuur=<factor> pas hieronder (controleur 15 nov)
	# slaapt hij, dan staat de zzz 9 boven de toren, nooit hoger dan 1 onder de bovenrand (slijm.gd; controleur kan 1)
	if "leven" in slijm and slijm.leven == "slapen" and slijm.has_method("teken_rand_y"):
		rel = maxf(minf(rel - 9.0, -25.0), ceilf(slijm.teken_rand_y()))
	rel *= s.proef_figuur
	var top := int(floor((slijm.position.y + rel - 1.0) * s.schaal)) + boven
	var x := int(hol.position.x + slijm.position.x * s.schaal)
	var halve := int(ceil(11 * s.schaal * s.proef_figuur))   # bij figuur > 1 is de toren breder
	return Vector3i(x - halve, x + halve, clampi(top, 0, s.vangt_y))
