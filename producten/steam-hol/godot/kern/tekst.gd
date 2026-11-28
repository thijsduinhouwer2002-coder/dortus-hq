extends Node2D
# Kleine tekst in de strook zelf (geen kaartjes over andere vensters, eis Thijs 9 nov).
# Altijd: één regel kroniek en het goud. Bij hover binnen de strook: de laatste drie regels.

var regels: Array[String] = []
var goud := 0
var doel := ""   # kopregel rechts als het kaartje dicht is: volgend doel (kern/kaartje.gd doel_regel, Iris 16 nov)
# Muis erop: het bord staat vol (open = 1). Gaat de muis weg terwijl de regel al weg is, dan glijdt het bord in
# 0,35 s terug naar één rij in plaats van in één beeld te springen (Daan #261 kan-punt 1, Sanne 27 nov).
var hover := false:
	set(v):
		if v == hover:
			return
		hover = v
		if v:
			open = 1.0
		set_process(true)
		queue_redraw()
var vast := ""   # telling na terugkomst: bovenaan het kaartje tot de eerste nieuwe held binnen is (moet Daan 16 nov 23:30)
var weg_regels: Array[String] = []   # het verhaal van de nacht (Iris keuring 16 punt 2): regels van vóór het weggaan niet meer op het kaartje
var weg_tel := ""   # de telling van de laatste keer weg; blijft deze speelbeurt staan (vast gaat weg bij de eerste nieuwe held)
var breedte := 1280.0
var hoogte := 120.0
var schaal := 3
const PANEEL := preload("res://kunst/paneel.png")   # Daan: 12 x 12, 9-slice rand 4 (kunst.json)
const R := 4
# Paneel in de 3D-stijl (Daan 14 nov, ontwerp/steam/paneel-3d/LEESMIJ.md ronde 2): warm donkerbruine plaat met zachte gouden rand (15 nov, was pruim)
# als 9-slice (bron 384 px, rand 128), letter Fredoka (SIL OFL, kunst/letters/), ronde knop en rond muntje.
# Uit = het pixelpaneel van voor 14 nov (alleen een terugvalschakelaar).
static var met_3d := true
# 25 nov (Mila #43, Olaf akkoord): krijtbord in een houten lijst, zelfde 9-slice; het oude bruine paneel blijft als kunst/paneel_3d.png
# 26 nov (Mila #197, Iris "los venster"): paneel_hol.png is nu een planken bord in de aarde (modellen/plankbord.py), zelfde 9-slice
const PANEEL_3D := preload("res://kunst/paneel_hol.png")
const BRON_RAND := 128
const FREDOKA := preload("res://kunst/letters/Fredoka.ttf")
const KAART := preload("res://kern/tekst_kaart.gd")
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
			sb.bg_color = Color(0.10, 0.05, 0.03, 0.0)
			sb.shadow_color = Color(0.10, 0.05, 0.03, 0.55)
			sb.shadow_size = 3
			sb.shadow_offset = Vector2(1, 3)   # bijna niets links of boven: Windows tekent niets buiten het muisvlak (controleur 14 nov)
		"knop_schaduw":
			sb.bg_color = Color(0.09, 0.04, 0.02, 0.0)
			sb.shadow_color = Color(0.09, 0.04, 0.02, 0.5)
			sb.shadow_size = 2
			sb.shadow_offset = Vector2(0, 2)
		"knop":
			sb.bg_color = Color("#a65c38")   # warm terracotta (Daan 15 nov, punt 1 Thijs; was pruim 7a426c; 14:20 een tikje lichter, kan 1 Daan)
			sb.border_color = Color("#e8b040")
			sb.set_border_width_all(2)
			sb.anti_aliasing = true
		"knop_glans":
			sb.bg_color = Color("#c4825a")
		"knop_lip":
			sb.bg_color = Color("#5e2e1a")   # donkere onderlip van de drukknop (28 nov, #333 c)
			sb.border_color = Color("#b07a2a")
			sb.set_border_width_all(2)
			sb.anti_aliasing = true
		_:
			push_error("tekst.gd: onbekende doos " + naam)
	dozen[naam] = sb
	return sb

# tekst met een zachte donkere schaduw van 1 px eronder (Daan ronde 2: titel en getal)
func _tekst(font: Font, p: Vector2, t: String, breed: float, maat: int, kleur: Color, schaduw := true) -> void:
	if schaduw and met_3d:
		# vanaf 200 px 2 px diep (28 nov, #333 c: op schaal 5 viel 1 px weg en las de letter dun en plat)
		draw_string(font, p + Vector2(0, maxf(1.0, roundf(schaal / 3.0))), t, HORIZONTAL_ALIGNMENT_LEFT, breed, maat, Color(0.09, 0.04, 0.02, 0.65))
	draw_string(font, p, t, HORIZONTAL_ALIGNMENT_LEFT, breed, maat, kleur)
# Het kaartje voor upgrades (kern/kaartje.gd): als dit niet leeg is, toont het paneel het kaartje in plaats van de kroniek.
var kaart := {}
var knop_koop := Rect2()   # in vensterpixels, voor de klik (strook.gd); leeg als er geen knop staat
var knop_undo := Rect2()
var knop_weg := Rect2()

# Daans paneel als 9-slice, met de schaal van de strook (scherpe pixels)
func _paneel(rect: Rect2, vol_h := 0.0) -> void:
	if met_3d:
		_paneel_3d(rect, vol_h)
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
# vol_h > 0: het bord klapt in of uit. Dan wordt het hout niet samengeperst maar van boven afgesneden (zelfde
# dichtheid als het volle bord), zodat de naad tussen de planken met de tekst meeschuift en nooit door het goud
# of het doel loopt (Sanne 27 nov, gezien in de film van muis weg bij Daan #261).
func _paneel_3d(rect: Rect2, vol_h := 0.0) -> void:
	var r := Rect2(rect.position, rect.size - Vector2(5, 2))   # rechts 7 px lucht tot de schermrand (Daan ronde 3, kan)
	var sb := _doos("paneel_schaduw")
	sb.set_corner_radius_all(int(3.5 * schaal))
	draw_style_box(sb, r)
	var m := roundf(4.5 * schaal)
	var S := float(PANEEL_3D.get_width())
	var xs := [r.position.x, r.position.x + m, r.end.x - m, r.end.x]
	var ys := [r.position.y, r.position.y + m, r.end.y - m, r.end.y]
	var bx := [0.0, BRON_RAND, S - BRON_RAND, S]
	var by := bx.duplicate()
	by[2] = BRON_RAND + bron_midden(S - 2.0 * BRON_RAND, r.size.y - 2.0 * m, vol_h - 2.0 * m)
	for i in 3:
		for j in 3:
			draw_texture_rect_region(PANEEL_3D, Rect2(xs[i], ys[j], xs[i + 1] - xs[i], ys[j + 1] - ys[j]),
				Rect2(bx[i], by[j], bx[i + 1] - bx[i], by[j + 1] - by[j]))

# hoeveel bronpixels van het midden het bord toont: het hele midden, of bij een kleiner bord dan vol het bovenste deel
static func bron_midden(bron: float, h: float, vol: float) -> float:
	if vol <= 0.0 or h >= vol:
		return bron
	return bron * maxf(h, 1.0) / vol

# muntje van 4 x 4 spelpixels: donkere rand, goud, één glimpixel
func _munt(p: Vector2, f := 1.0) -> void:
	if met_3d:
		# rond en glanzend, zelfde plek als het pixelmuntje (4 x 4 spelpixels vanaf p, keer f), met een kleine schaduw
		var c := p + Vector2(2, 2) * schaal * f
		var rr := 2.4 * schaal * f
		# gladde rand (Mila 14 nov 23:50): om elke cirkel een antialiased boog van 1 schermpixel, zie hol.gd munt_3d
		_munt_laag(c + Vector2(0.5, 1.5), rr, Color(0.12, 0.06, 0.03, 0.45))
		_munt_laag(c, rr, Color("#aa691e"))
		_munt_laag(c + Vector2(-0.3, -0.3), rr - 1.2, Color("#f2b632"))
		_munt_laag(c + Vector2(-0.8, -0.9) * schaal * f, 0.6 * schaal * f, Color("#fff0aa"))
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

# Maten per strookhoogte (Daan ronde 3, 14 nov): op 160 px groter (kop en getal 18, tekst 15, knop 16 en 28 hoog,
# minstens 8 px tussen knop en gouden binnenrand); op 120 alles zoals het was; op 96 de knop 2 px hoger (vrij van de onderrand).
# kop/tekst/uitleg/knop/knop2: lettermaten; regel_h: regelafstand; onder: ruimte onder de laatste regel tot de strookrand;
# boven: ruimte boven de kopregel tot de bovenkant van het paneel; knop_h en knop_dy: hoogte en extra ruimte boven de knop;
# kop_dy: kopregel iets hoger (op 160 3 px, anders plakt de grote kop tegen de regel eronder); op 96 1 px lager, vrij van het hout
# bovenaan (kan Daan nakeuring #52, Mila 25 nov); munt: maat van het muntje.
# Vanaf 200 px (schaal 5) groeien kaartje en hover mee, hooguit 1,25 keer de maat van 160 (28 nov, #333 c: op 200 was
# het kaartje een klein regeltje in een groot leeg bord). Het dichte bord (bord_maten) houdt de maat van 160.
func maten(groei := true) -> Dictionary:
	if met_3d and hoogte >= 140:
		var k := clampf(schaal / 4.0, 1.0, 1.25) if groei else 1.0
		return {"kop": roundi(18 * k), "tekst": roundi(15 * k), "uitleg": roundi(15 * k), "knop": roundi(16 * k),
			"knop2": roundi(16 * k), "regel_h": roundi(20 * k), "onder": roundi(12 * k), "boven": roundi(14 * k),
			"knop_h": roundf(28.0 * k), "knop_dy": roundi(7 * k), "munt": 1.2, "kop_dy": roundi(-3 * k)}
	var m := 12 if hoogte < 110 else 13
	var binnen := 5 * schaal
	return {"kop": m, "tekst": m, "uitleg": m - 1, "knop": m, "knop2": m - 1, "regel_h": m + 4, "onder": binnen,
		"boven": binnen - 2, "knop_h": float(m + 4 + 2 * schaal), "knop_dy": 1 if (met_3d and hoogte < 110) else 3, "munt": 1.0, "kop_dy": 1 if (met_3d and hoogte < 110) else 0}

func _munt_laag(c: Vector2, r: float, kleur: Color) -> void:
	var rr := maxf(r - 0.5, 0.5)
	# doorzichtig (de schaduw): schijf een halve pixel kleiner, anders mengt de rand dubbel (controleur 15 nov)
	draw_circle(c, rr - 0.5 if kleur.a < 1.0 else rr, kleur)
	draw_arc(c, rr, 0.0, TAU, 48, kleur, 1.0, true)

# muntje naast een getal met lettermaat kop op basislijn y: linksboven van het muntje (zelfde plek als vroeger bij factor 1)
func _munt_p(x: float, basis: float, kop: int, f: float) -> Vector2:
	if f == 1.0:
		return Vector2(x, basis - kop + kop / 2.0 - 2 * schaal + 1)
	return Vector2(x, basis - 0.4 * kop - 2 * schaal * f)

func vak_breedte() -> float:
	return minf(430.0, breedte * 0.3)

# Binnenruimte (moet Daan #45, 25 nov): de houten lijst van het krijtbord is ±2,1 spelpixel (6 px op 120), dus de tekst
# blijft rechts minstens 3 px van het hout (marge_r) en het paneel begint links ver genoeg vóór de tekst (paneel_links).
# Op 120: rechts 4,7 px en links 5,7 px lucht tussen hout en letter; op 96 en 160 rekent het mee met de schaal.
func marge_r() -> float:
	return 3.0 * schaal + 1.0 if met_3d else 0.0

func paneel_links(x: float) -> float:
	var binnen: float = 5.0 * schaal
	if met_3d:
		return x - maxf(binnen - 4.0, 4.0 * schaal)
	return x - binnen + 4.0

# Welke regels het paneel toont (getoetst in toets_systemen.gd). Na terugkomst (tel = de telling van de nacht) nooit
# een regel van vóór het weggaan, ook niet als de eerste nieuwe held al binnen is (Iris keuring 16 punt 2; in run
# 44017687872 stond anders "Gerda says this is a quick one." van vóór de nacht boven de telling). Wat telt: wat na de
# telling kwam, en het verhaal van de nacht (wr), per tekst hooguit zo vaak als in het verhaal ("had a busy shift."
# van de vorige nacht telt niet, controleur 17 nov). Met de muis erop en vast gezet: vast bovenaan, de rest eronder.
static func kies_toon(r: Array[String], v: String, wr: Array[String], tel: String, n: int, muis: bool) -> Array[String]:
	var mag: Array[String] = []   # kandidaten in volgorde, de nieuwste achteraan
	var ti := r.rfind(tel) if tel != "" else -1
	var over := {}
	for w in wr:
		over[w] = int(over.get(w, 0)) + 1
	for i in range(r.size() - 1, -1, -1):
		if ti < 0 or i >= ti:
			mag.push_front(r[i])
		elif int(over.get(r[i], 0)) > 0:
			over[r[i]] = int(over[r[i]]) - 1
			mag.push_front(r[i])
	var toon: Array[String] = []
	if muis and v != "" and mag.has(v):
		toon.append(v)
		var rest: Array[String] = []
		for i in range(mag.size() - 1, -1, -1):
			if rest.size() >= n - 1:
				break
			if mag[i] != v:
				rest.push_front(mag[i])
		toon.append_array(rest)
	else:
		for i in range(max(0, mag.size() - n), mag.size()):
			toon.append(mag[i])
	return toon

func zet(r: Array[String], g: int) -> void:
	var sleutel := "%d|%s" % [r.size(), r.back() if r.size() > 0 else ""]
	if sleutel != regel_sleutel:
		regel_sleutel = sleutel
		regel_sinds = 0.0   # nieuwe regel: weer 6 s in beeld
		set_process(true)
	regels = r
	goud = g
	queue_redraw()

# Bouwblad D (Sanne 25 nov, issue #19, Thijs "tekst heel klein en te veel", Iris tekst 6): het dichte bord toont
# één regel in grote letters (hoofdletters minstens 12 px op 120) en die regel gaat na 6 s zacht weg. Daarna staan
# alleen het goud en het doel op het bord. Muis erop: de laatste drie regels zoals altijd (oude maten, Daan r3).
const REGEL_TIJD := 6.0
const REGEL_WEG := 0.6   # zacht weg in de laatste 0,6 s
var regel_sleutel := ""
var regel_sinds := 99.0

# Bord klapt in (Sanne 27 nov, Iris 1b0e933 punt 1 voor mooi 9: "lege onderste helft na de regel, het grootste lege vlak
# in beeld"). Is de regel weg, dan zakt het bord in 0,35 s zacht naar één rij (goud en doel); komt er een nieuwe regel,
# dan rijst het in 0,25 s weer op. Zo zie je meer hol en minder plank, en het opkomen zelf zegt: er is nieuws.
# open = 1 bord met regel, 0 alleen de kopregel. Muis erop, telling na terugkomst of het kaartje: altijd vol.
const IN_S := 0.35
const UIT_S := 0.25
var open := 1.0

static func open_doel(sinds: float) -> float:
	return 1.0 if sinds < REGEL_TIJD else 0.0

# met de muis erop blijft het bord vol, dus het zakt pas als de muis weg is
static func bord_doel(sinds: float, muis: bool) -> float:
	return 1.0 if muis else open_doel(sinds)

static func open_stap(nu: float, doel_: float, delta: float) -> float:
	if doel_ > nu:
		return minf(doel_, nu + delta / UIT_S)
	return maxf(doel_, nu - delta / IN_S)

# zachte s-kromme, zodat het bord niet stoot bij begin en einde
static func open_glad(o: float) -> float:
	return o * o * (3.0 - 2.0 * o)

func _process(delta: float) -> void:
	var voor := regel_sinds
	regel_sinds += delta
	var o := open_stap(open, bord_doel(regel_sinds, hover), delta)
	var beweegt := o != open
	open = o
	if voor < REGEL_TIJD + 0.05:
		if regel_sinds >= REGEL_TIJD - REGEL_WEG or beweegt:
			queue_redraw()
	elif beweegt:
		queue_redraw()
	else:
		set_process(false)

# 1 = regel helemaal te zien, 0 = weg (getoetst in toets_systemen.gd)
static func regel_zicht(sinds: float) -> float:
	if sinds <= REGEL_TIJD - REGEL_WEG:
		return 1.0
	return clampf((REGEL_TIJD - sinds) / REGEL_WEG, 0.0, 1.0)

# Maten van het dichte bord (bouwblad D): hoofdletters van Fredoka zijn 0,7 em, dus 18 geeft 12,6 px op 120.
# Op 96 past 15 (10,5 px), op 160 24 (16,8 px). Het kaartje en de hover houden maten().
func bord_maten() -> Dictionary:
	if not met_3d:
		return maten()
	var M := maten(false)
	if hoogte >= 140:
		M.kop = 24; M.tekst = 24; M.uitleg = 22; M.regel_h = 29
	elif hoogte >= 110:
		M.kop = 18; M.tekst = 18; M.uitleg = 17; M.regel_h = 22; M.munt = 1.3   # muntje mee met het grotere getal
	else:
		M.kop = 15; M.tekst = 15; M.uitleg = 14; M.regel_h = 19; M.munt = 1.2
	return M

func _ready() -> void:
	texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR if met_3d else CanvasItem.TEXTURE_FILTER_NEAREST

# Het vak van het paneel bij hover (drie regels), in vensterpixels: strook.gd laat de muis daar vangen, zodat het
# paneel op 96 px niet dichtklapt als de muis boven het maaiveld komt (zelfde rekensom als _draw).
func hover_vak() -> Rect2:
	var M := maten()
	var x := breedte - vak_breedte() - 8
	var y0 := hoogte - int(M.onder) - int(M.regel_h) * 4
	var links := paneel_links(x)
	var top := y0 - int(M.boven)
	return Rect2(links, top, breedte - links, hoogte - top)

# Knop en kaartje staan sinds 28 nov in kern/tekst_kaart.gd (dit bestand was 480 regels).
func _knop(x: float, y: float, h: float, tekst_: String, maat: int, font: Font, getal := "") -> Rect2:
	return KAART.knop(self, x, y, h, tekst_, maat, font, getal)

func _draw_kaart() -> void:
	KAART.kaart(self)

func _draw() -> void:
	if not kaart.is_empty():
		_draw_kaart()
		return
	knop_koop = Rect2()
	knop_undo = Rect2()
	knop_weg = Rect2()
	var font := _letter(450)
	var M := maten() if hover else bord_maten()
	var kop: int = M.kop
	var maat: int = M.tekst
	var f: float = M.munt
	var n := 3 if hover else 1
	var toon: Array[String] = kies_toon(regels, vast, weg_regels, weg_tel, n, hover)
	# dicht bord: de regel gaat na 6 s zacht weg; het bord blijft even hoog (geen springend paneel)
	var zicht := 1.0 if (hover or vast != "") else regel_zicht(regel_sinds)
	var regel_h: int = M.regel_h
	var bw := vak_breedte()
	var x := breedte - bw - 8
	var y0 := float(hoogte - int(M.onder) - regel_h * (toon.size() + 1))
	if not hover and vast == "" and met_3d and toon.size() > 0:
		# ingeklapt bord (Iris 1b0e933 punt 1): de regel-rij schuift onder de strook weg, tot op hele pixels
		y0 += roundf(float(regel_h * toon.size()) * (1.0 - open_glad(open)))
		zicht *= open_glad(open)
	# paneel van paneel_links(x) tot de rechterrand, van boven de kop tot onderaan de strook
	var links := paneel_links(x)
	var top := y0 - int(M.boven)
	var vol_h := 0.0
	if not hover and vast == "" and met_3d and toon.size() > 0:
		vol_h = hoogte - 2 - (float(hoogte - int(M.onder) - regel_h * (toon.size() + 1)) - int(M.boven)) - 2.0
	_paneel(Rect2(links, top, breedte - 2 - links, hoogte - 2 - top), vol_h)
	# goud als muntje plus getal in plaats van "Hoard: 24 gold" (Mila 20:55, stijl.md punt 5); zelfde kleuren als de
	# vliegende muntjes in hol.gd, 4 x 4 spelpixels, op de schaal van de strook (scherpe pixels)
	_munt(_munt_p(x, y0 + kop + int(M.kop_dy), kop, f), f)
	_tekst(_letter(600), Vector2(x + 5 * schaal * f + 2, y0 + kop + int(M.kop_dy)), str(goud), bw, kop, Color("#ffe07a"))
	_draw_doel(x, y0 + kop + int(M.kop_dy), bw, kop, f, font, int(M.uitleg))
	var bt: float = bw - marge_r()   # regels niet tot in de houten lijst (moet Daan #45)
	if zicht <= 0.0:
		return
	var ondergrens := 10 if hover else maat - 3   # dicht bord: hooguit 3 px kleiner, dan liever "..."
	for i in toon.size():
		# nooit afkappen (Sanne 9 nov): eerst kleiner tot 10 px, past het dan nog niet, dan op een woordgrens met "..."
		var r: String = toon[i]
		var m := maat
		while m > ondergrens and font.get_string_size(r, HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > bt:
			m -= 1
		if font.get_string_size(r, HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > bt:
			var woorden := r.split(" ")
			while woorden.size() > 1 and font.get_string_size(" ".join(woorden) + "...", HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > bt:
				woorden.remove_at(woorden.size() - 1)
			r = " ".join(woorden) + "..."
		draw_string(font, Vector2(x, y0 + regel_h * (i + 1) + maat), r, HORIZONTAL_ALIGNMENT_LEFT, -1, m, Color("#f3e2c0", zicht))

# Het volgende doel rechts op de kopregel, naast het goud (Iris keuring 1, probleem 2). Rechts uitgelijnd binnen het vak,
# kleiner dan de kop; past hij niet naast het goud, dan kleiner tot 10 px, en anders niet tonen (nooit over het goud).
# Kan het al: goudgeel, anders gedempt, zodat het een doel is en geen knop.
func _draw_doel(x: float, basis: float, bw: float, kop: int, f: float, font: Font, maat_doel := -1) -> void:
	if doel == "":
		return
	var klaar := doel.contains("ready")
	# kan Daan 16 nov: "ready" in dezelfde vette goudletter als het getal (kleur was al gelijk, #ffe07a), dan leest het als uitnodiging
	if klaar:
		font = _letter(600)
	var gw := _letter(600).get_string_size(str(goud), HORIZONTAL_ALIGNMENT_LEFT, -1, kop).x
	var vrij := bw - (5 * schaal * f + 2 + gw) - 3 * schaal - marge_r()
	var m := int(maten().uitleg) if maat_doel < 0 else maat_doel
	while m > 10 and font.get_string_size(doel, HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > vrij:
		m -= 1
	var w := font.get_string_size(doel, HORIZONTAL_ALIGNMENT_LEFT, -1, m).x
	if w > vrij:
		return
	# kan Daan 16 nov 21:10: de gedempte letter een tikje lichter (was #cdb48f, op het bruin de zwakste tekst); blijft
	# donkerder dan de kroniekletter #f3e2c0, zodat het een doel blijft en geen knop
	var kleur := Color("#ffe07a") if klaar else Color("#dcc6a2")
	_tekst(font, Vector2(x + bw - w - marge_r(), basis), doel, -1, m, kleur)
