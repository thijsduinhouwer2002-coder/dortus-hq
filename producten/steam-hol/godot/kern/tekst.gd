extends Node2D
# Kleine tekst in de strook zelf (geen kaartjes over andere vensters, eis Thijs 9 nov).
# Altijd: één regel kroniek en het goud. Bij hover binnen de strook: de laatste drie regels.

var regels: Array[String] = []
var goud := 0
var hover := false
var breedte := 1280.0
var hoogte := 120.0
var schaal := 3
const PANEEL := preload("res://kunst/paneel.png")   # Daan: 12 x 12, 9-slice rand 4 (kunst.json)
const R := 4
# Paneel in de 3D-stijl (Daan 14 nov, ontwerp/steam/paneel-3d/LEESMIJ.md ronde 2): pruimhouten plaat met zachte gouden rand
# als 9-slice (bron 384 px, rand 128), letter Fredoka (SIL OFL, kunst/letters/), ronde knop en rond muntje.
# Uit = het pixelpaneel van voor 14 nov (alleen een terugvalschakelaar).
static var met_3d := true
const PANEEL_3D := preload("res://kunst/paneel_3d.png")
const BRON_RAND := 128
const FREDOKA := preload("res://kunst/letters/Fredoka.ttf")
var letters := {}   # gewicht -> FontVariation

func _letter(gewicht: int) -> Font:
	if not met_3d:
		return ThemeDB.fallback_font
	if not letters.has(gewicht):
		var f := FontVariation.new()
		f.base_font = FREDOKA
		f.variation_opentype = {TextServerManager.get_primary_interface().name_to_tag("wght"): gewicht}
		letters[gewicht] = f
	return letters[gewicht]

# StyleBoxen één keer maken en bewaren (kan-punt controleur 14 nov): niet bij elke tekening nieuwe objecten.
# Alleen de hoekstraal hangt af van schaal en knophoogte; die zet de tekenaar per keer.
var dozen := {}

func _doos(naam: String) -> StyleBoxFlat:
	if dozen.has(naam):
		return dozen[naam]
	var sb := StyleBoxFlat.new()
	match naam:
		"paneel_schaduw":
			sb.bg_color = Color(0.09, 0.03, 0.11, 0.0)
			sb.shadow_color = Color(0.09, 0.03, 0.11, 0.55)
			sb.shadow_size = 3
			sb.shadow_offset = Vector2(1, 3)   # bijna niets links of boven: Windows tekent niets buiten het muisvlak (controleur 14 nov)
		"knop_schaduw":
			sb.bg_color = Color(0.08, 0.02, 0.09, 0.0)
			sb.shadow_color = Color(0.08, 0.02, 0.09, 0.5)
			sb.shadow_size = 2
			sb.shadow_offset = Vector2(0, 2)
		"knop":
			sb.bg_color = Color("#7a426c")
			sb.border_color = Color("#e8b040")
			sb.set_border_width_all(2)
			sb.anti_aliasing = true
		"knop_glans":
			sb.bg_color = Color("#925880")
		_:
			push_error("tekst.gd: onbekende doos " + naam)
	dozen[naam] = sb
	return sb

# tekst met een zachte donkere schaduw van 1 px eronder (Daan ronde 2: titel en getal)
func _tekst(font: Font, p: Vector2, t: String, breed: float, maat: int, kleur: Color, schaduw := true) -> void:
	if schaduw and met_3d:
		draw_string(font, p + Vector2(0, 1), t, HORIZONTAL_ALIGNMENT_LEFT, breed, maat, Color(0.08, 0.02, 0.09, 0.65))
	draw_string(font, p, t, HORIZONTAL_ALIGNMENT_LEFT, breed, maat, kleur)
# Het kaartje voor upgrades (kern/kaartje.gd): als dit niet leeg is, toont het paneel het kaartje in plaats van de kroniek.
var kaart := {}
var knop_koop := Rect2()   # in vensterpixels, voor de klik (strook.gd); leeg als er geen knop staat
var knop_undo := Rect2()
var knop_weg := Rect2()

# Daans paneel als 9-slice, met de schaal van de strook (scherpe pixels)
func _paneel(rect: Rect2) -> void:
	if met_3d:
		_paneel_3d(rect)
		return
	var m := R * schaal
	var xs := [rect.position.x, rect.position.x + m, rect.end.x - m, rect.end.x]
	var ys := [rect.position.y, rect.position.y + m, rect.end.y - m, rect.end.y]
	var bx := [0, R, 12 - R, 12]
	for i in 3:
		for j in 3:
			draw_texture_rect_region(PANEEL, Rect2(xs[i], ys[j], xs[i + 1] - xs[i], ys[j + 1] - ys[j]),
				Rect2(bx[i], bx[j], bx[i + 1] - bx[i], bx[j + 1] - bx[j]))

# 3D-paneel: 4 px lucht rechts en onder (Daan ronde 2), zachte schaduw naar het hol, rand 4,5 spelpixel (18 px op 160)
func _paneel_3d(rect: Rect2) -> void:
	var r := Rect2(rect.position, rect.size - Vector2(2, 2))
	var sb := _doos("paneel_schaduw")
	sb.set_corner_radius_all(int(3.5 * schaal))
	draw_style_box(sb, r)
	var m := roundf(4.5 * schaal)
	var S := float(PANEEL_3D.get_width())
	var xs := [r.position.x, r.position.x + m, r.end.x - m, r.end.x]
	var ys := [r.position.y, r.position.y + m, r.end.y - m, r.end.y]
	var bx := [0.0, BRON_RAND, S - BRON_RAND, S]
	for i in 3:
		for j in 3:
			draw_texture_rect_region(PANEEL_3D, Rect2(xs[i], ys[j], xs[i + 1] - xs[i], ys[j + 1] - ys[j]),
				Rect2(bx[i], bx[j], bx[i + 1] - bx[i], bx[j + 1] - bx[j]))

# muntje van 4 x 4 spelpixels: donkere rand, goud, één glimpixel
func _munt(p: Vector2) -> void:
	if met_3d:
		# rond en glanzend, zelfde plek als het pixelmuntje (4 x 4 spelpixels vanaf p), met een kleine schaduw
		var c := p + Vector2(2, 2) * schaal
		var rr := 2.4 * schaal
		draw_circle(c + Vector2(0.5, 1.5), rr, Color(0.12, 0.04, 0.12, 0.45))
		draw_circle(c, rr, Color("#aa691e"))
		draw_circle(c + Vector2(-0.3, -0.3), rr - 1.2, Color("#f2b632"))
		draw_circle(c + Vector2(-0.8, -0.9) * schaal, 0.6 * schaal, Color("#fff0aa"))
		return
	var px := float(schaal)
	var rand := Color("#7a4a12")
	var goudk := Color("#f2c14e")
	var vorm := [".XX.", "XGGX", "XGGX", ".XX."]
	for j in 4:
		for i in 4:
			var c: String = vorm[j][i]
			if c == "X":
				draw_rect(Rect2(p.x + i * px, p.y + j * px, px, px), rand)
			elif c == "G":
				draw_rect(Rect2(p.x + i * px, p.y + j * px, px, px), Color("#ffe07a") if (i == 1 and j == 1) else goudk)

func vak_breedte() -> float:
	return minf(430.0, breedte * 0.3)

func zet(r: Array[String], g: int) -> void:
	regels = r
	goud = g
	queue_redraw()

func _ready() -> void:
	texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR if met_3d else CanvasItem.TEXTURE_FILTER_NEAREST

# Het vak van het paneel bij hover (drie regels), in vensterpixels: strook.gd laat de muis daar vangen, zodat het
# paneel op 96 px niet dichtklapt als de muis boven het maaiveld komt (zelfde rekensom als _draw).
func hover_vak() -> Rect2:
	var maat := 12 if hoogte < 110 else 13
	var regel_h := maat + 4
	var binnen := 5 * schaal
	var x := breedte - vak_breedte() - 8
	var y0 := hoogte - 2 - (binnen - 2) - regel_h * 4
	var links := x - binnen + 4
	var top := y0 - binnen + 2
	return Rect2(links, top, breedte - links, hoogte - top)

# Een knop in het paneel: donker vlak, gouden rand van één spelpixel, tekst in het midden. Geeft het vak terug.
func _knop(x: float, y: float, h: float, tekst_: String, maat: int, font: Font) -> Rect2:
	var w := font.get_string_size(tekst_, HORIZONTAL_ALIGNMENT_LEFT, -1, maat).x + 6 * schaal
	var r := Rect2(x, y, w, h)
	if met_3d:
		# ronde pil (Daan ronde 2): gouden rand, warm pruimroze, glansstrook bovenin, zachte schaduw eronder
		var sch := _doos("knop_schaduw")
		sch.set_corner_radius_all(int(h / 2.0))
		draw_style_box(sch, r)
		var sb := _doos("knop")
		sb.set_corner_radius_all(int(h / 2.0))
		draw_style_box(sb, r)
		var gl := _doos("knop_glans")
		gl.set_corner_radius_all(int(h * 0.15))
		draw_style_box(gl, Rect2(x + 4, y + 3, w - 8, h * 0.27))
		var tw := font.get_string_size(tekst_, HORIZONTAL_ALIGNMENT_LEFT, -1, maat).x
		_tekst(font, Vector2(x + (w - tw) / 2.0, y + h / 2.0 + maat * 0.35), tekst_, -1, maat, Color("#ffe8a0"))
		return r
	draw_rect(r, Color("#f2c14e"))
	draw_rect(r.grow(-schaal), Color("#503856"))
	draw_string(font, Vector2(x + 3 * schaal, y + h / 2.0 + maat * 0.35), tekst_, HORIZONTAL_ALIGNMENT_LEFT, -1, maat, Color("#f3e2c0"))
	return r

# Het kaartje (Sanne, features.md feature 5): naam, uitleg, kost met muntje, "Buy" of "x more gold", en "Undo +45".
# Zelfde vak als het paneel bij hover (hover_vak), dus ook op 96 px past het en vangt strook.gd daar de muis.
func _draw_kaart() -> void:
	var font := _letter(450)
	var vet := _letter(600)
	var maat := 12 if hoogte < 110 else 13
	var regel_h := maat + 4
	var bw := vak_breedte()
	var x := breedte - bw - 8
	var vak := hover_vak()
	_paneel(Rect2(vak.position.x, vak.position.y, breedte - 2 - vak.position.x, hoogte - 2 - vak.position.y))
	var y0 := hoogte - 2 - (5 * schaal - 2) - regel_h * 4
	_tekst(vet, Vector2(x, y0 + maat), String(kaart.titel), bw * 0.62, maat, Color("#ffe07a"))
	# rechts op de kopregel: wat je hebt, als muntje plus getal (zelfde plek als bij de kroniek)
	var gw := vet.get_string_size(str(goud), HORIZONTAL_ALIGNMENT_LEFT, -1, maat).x
	var gx := x + bw - gw - 5 * schaal - (12 if met_3d else 6)   # 3D: niet tegen de gouden rand
	_munt(Vector2(gx, y0 + maat / 2.0 - 2 * schaal + 1))
	_tekst(vet, Vector2(gx + 5 * schaal + 2, y0 + maat), str(goud), -1, maat, Color("#f6e8ce") if met_3d else Color("#ffe07a"))
	draw_string(font, Vector2(x, y0 + regel_h + maat), String(kaart.uitleg), HORIZONTAL_ALIGNMENT_LEFT, bw, maat - 1, Color("#f3e2c0"))
	var ky := y0 + regel_h * 2 + 3
	var kh := float(regel_h + 2 * schaal)
	var kx := x
	knop_koop = Rect2()
	knop_undo = Rect2()
	knop_weg = Rect2()
	if int(kaart.kost) >= 0 and bool(kaart.get("demo_over", false)):
		# demo voorbij: tekst in plaats van de knop, zonder klikvlak (kern/demo_einde.gd)
		var vol: String = preload("res://kern/demo_einde.gd").KAART
		draw_string(font, Vector2(kx, ky + kh / 2.0 + maat * 0.35), vol, HORIZONTAL_ALIGNMENT_LEFT, -1, maat, Color("#ffe07a"))
		kx += font.get_string_size(vol, HORIZONTAL_ALIGNMENT_LEFT, -1, maat).x + 4 * schaal
	elif int(kaart.kost) >= 0:
		if bool(kaart.kan):
			knop_koop = _knop(kx, ky, kh, "Buy  %d" % int(kaart.kost), maat, vet)
			kx = knop_koop.end.x + 4 * schaal
		else:
			var grijs := "%d  (%d more gold)" % [int(kaart.kost), int(kaart.tekort)]
			_munt(Vector2(kx, ky + kh / 2.0 - 2 * schaal))
			draw_string(font, Vector2(kx + 5 * schaal + 2, ky + kh / 2.0 + maat * 0.35), grijs, HORIZONTAL_ALIGNMENT_LEFT, -1, maat, Color("#9a8a9a"))
			kx += 5 * schaal + 2 + font.get_string_size(grijs, HORIZONTAL_ALIGNMENT_LEFT, -1, maat).x + 4 * schaal
	if int(kaart.terug) > 0:
		knop_undo = _knop(kx, ky, kh, "Undo  +%d" % int(kaart.terug), maat - 1, vet)
		kx = knop_undo.end.x + 4 * schaal
	if bool(kaart.get("weg", false)):
		knop_weg = _knop(kx, ky, kh, "Remove", maat - 1, vet)

func _draw() -> void:
	if not kaart.is_empty():
		_draw_kaart()
		return
	knop_koop = Rect2()
	knop_undo = Rect2()
	knop_weg = Rect2()
	var font := _letter(450)
	var maat := 12 if hoogte < 110 else 13
	var n := 3 if hover else 1
	var toon: Array[String] = []
	for i in range(max(0, regels.size() - n), regels.size()):
		toon.append(regels[i])
	var regel_h := maat + 4
	var bw := vak_breedte()
	var x := breedte - bw - 8
	var binnen := 5 * schaal   # tekst begint 5 spelpixels binnen de buitenkant van Daans paneel (kunst.json)
	var y0 := hoogte - 2 - (binnen - 2) - regel_h * (toon.size() + 1)
	# paneel van x - binnen tot de rechterrand, van boven de kop tot onderaan de strook
	var links := x - binnen + 4
	var top := y0 - binnen + 2
	_paneel(Rect2(links, top, breedte - 2 - links, hoogte - 2 - top))
	# goud als muntje plus getal in plaats van "Hoard: 24 gold" (Mila 20:55, stijl.md punt 5); zelfde kleuren als de
	# vliegende muntjes in hol.gd, 4 x 4 spelpixels, op de schaal van de strook (scherpe pixels)
	var mx := x
	var my := y0 + maat / 2.0 - 2 * schaal + 1
	_munt(Vector2(mx, my))
	_tekst(_letter(600), Vector2(x + 5 * schaal + 2, y0 + maat), str(goud), bw, maat, Color("#ffe07a"))
	for i in toon.size():
		# nooit afkappen (Sanne 9 nov): eerst kleiner tot 10 px, past het dan nog niet, dan op een woordgrens met "..."
		var r: String = toon[i]
		var m := maat
		while m > 10 and font.get_string_size(r, HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > bw:
			m -= 1
		if font.get_string_size(r, HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > bw:
			var woorden := r.split(" ")
			while woorden.size() > 1 and font.get_string_size(" ".join(woorden) + "...", HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > bw:
				woorden.remove_at(woorden.size() - 1)
			r = " ".join(woorden) + "..."
		draw_string(font, Vector2(x, y0 + regel_h * (i + 1) + maat), r, HORIZONTAL_ALIGNMENT_LEFT, -1, m, Color("#f3e2c0"))
