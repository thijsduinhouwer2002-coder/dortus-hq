extends RefCounted
# Knop en kaartje van het bord (Olaf 28 nov, #333 punt c: "UI looks too plain", uit kern/tekst.gd gehaald, dat was 480 regels).
# Statisch: `t` is het tekstvak (kern/tekst.gd) en alles wordt getekend tijdens zijn _draw().
# Wat er bij kwam (alleen te zien vanaf 160 px, op 120 en 96 even groot als eerst):
# - de knop is een echte drukknop: een donkere onderlip onder de pil (zoals de knoppen in Rusty's Retirement een dikke
#   onderrand hebben), glans en lip rekenen mee met de knophoogte in plaats van vaste pixels;
# - het kaartje groeit op 200 en 240 px mee met de strook (maten() in tekst.gd, hooguit 1,25 keer de maat van 160);
# - de uitleg wordt kleiner als hij niet past, nooit afgeknipt.

const DEMO_EINDE := preload("res://kern/demo_einde.gd")

# Een knop in het paneel. Geeft het vak terug (vensterpixels, voor de klik in kaartje.gd).
# getal (Daan 15 nov 14:45, kan): achter de tekst een muntje en dan het getal, zodat "Undo" plus muntje "+45" in een
# blik zegt dat je goud terugkrijgt. Leeg = alleen de tekst.
static func knop(t, x: float, y: float, h: float, tekst_: String, maat: int, font: Font, getal := "") -> Rect2:
	var sc: float = t.schaal
	var tw: float = font.get_string_size(tekst_, HORIZONTAL_ALIGNMENT_LEFT, -1, maat).x
	var mw := 0.0   # muntje plus getal
	if getal != "":
		mw = 2 * sc + 5 * sc + 1 + font.get_string_size(getal, HORIZONTAL_ALIGNMENT_LEFT, -1, maat).x
	var w := tw + mw + 6 * sc
	var r := Rect2(x, y, w, h)
	var tx := x + 3 * sc
	var kleur := Color("#f3e2c0")
	var ty := y + h / 2.0 + maat * 0.35
	if t.met_3d:
		# ronde pil (Daan ronde 2): gouden rand, warm terracotta, glansstrook bovenin, zachte schaduw eronder.
		# Onderlip (28 nov): de pil staat op een donkere rand van ±h/10, de letter zit midden op de pil zelf.
		var lip := maxf(2.0, roundf(h / 10.0))
		var rond := int(h / 2.0)
		var sch: StyleBoxFlat = t._doos("knop_schaduw")
		sch.set_corner_radius_all(rond)
		t.draw_style_box(sch, r)
		var lp: StyleBoxFlat = t._doos("knop_lip")
		lp.set_corner_radius_all(rond)
		t.draw_style_box(lp, r)
		var sb: StyleBoxFlat = t._doos("knop")
		sb.set_corner_radius_all(int((h - lip) / 2.0))
		t.draw_style_box(sb, Rect2(x, y, w, h - lip))
		var gl: StyleBoxFlat = t._doos("knop_glans")
		gl.set_corner_radius_all(int(h * 0.15))
		var gi := maxf(4.0, h * 0.2)   # glans niet tegen de gouden rand
		t.draw_style_box(gl, Rect2(x + gi, y + maxf(3.0, h * 0.11), w - 2.0 * gi, h * 0.24))
		tx = x + (w - tw - mw) / 2.0
		ty = y + (h - lip) / 2.0 + maat * 0.35
		kleur = Color("#ffe8a0")
		t._tekst(font, Vector2(tx, ty), tekst_, -1, maat, kleur)
	else:
		t.draw_rect(r, Color("#f2c14e"))
		t.draw_rect(r.grow(-sc), Color("#5e3e33"))   # pixelterugval warm (kan 2 Daan 15 nov, was pruim 503856)
		t.draw_string(font, Vector2(tx, ty), tekst_, HORIZONTAL_ALIGNMENT_LEFT, -1, maat, kleur)
	if getal != "":
		var mx := tx + tw + 2 * sc
		t._munt(Vector2(mx, ty - maat * 0.35 - 2 * sc))
		var gp := Vector2(mx + 5 * sc + 1, ty)   # Daan #344 K2: 1 px lucht tussen munt en getal (op 120 raakte hij de 4)
		if t.met_3d:
			t._tekst(font, gp, getal, -1, maat, kleur)
		else:
			t.draw_string(font, gp, getal, HORIZONTAL_ALIGNMENT_LEFT, -1, maat, kleur)
	return r

# lettermaat die in breed past, niet kleiner dan ondergrens
static func past(font: Font, tekst_: String, maat: int, breed: float, ondergrens := 10) -> int:
	var m := maat
	while m > ondergrens and font.get_string_size(tekst_, HORIZONTAL_ALIGNMENT_LEFT, -1, m).x > breed:
		m -= 1
	return m

# Het kaartje (Sanne, features.md feature 5): naam, uitleg, kost met muntje, "Buy" of "x more gold", en "Undo" met muntje "+45".
# Zelfde vak als het paneel bij hover (hover_vak), dus ook op 96 px past het en vangt strook.gd daar de muis.
static func kaart(t) -> void:
	var font: Font = t._letter(450)
	var vet: Font = t._letter(600)
	var M: Dictionary = t.maten()
	var sc: float = t.schaal
	var kop: int = M.kop
	var maat: int = M.tekst
	var regel_h: int = M.regel_h
	var f: float = M.munt
	var bw: float = t.vak_breedte()
	var x: float = t.breedte - bw - 8
	var vak: Rect2 = t.hover_vak()
	var kaart_: Dictionary = t.kaart
	t._paneel(Rect2(vak.position.x, vak.position.y, t.breedte - 2 - vak.position.x, t.hoogte - 2 - vak.position.y))
	var y0: float = t.hoogte - int(M.onder) - regel_h * 4
	t._tekst(vet, Vector2(x, y0 + kop + int(M.kop_dy)), String(kaart_.titel), bw * 0.62, kop, Color("#ffe07a"))
	# rechts op de kopregel: wat je hebt, als muntje plus getal (zelfde plek als bij de kroniek)
	var goud: int = t.goud
	var gw: float = vet.get_string_size(str(goud), HORIZONTAL_ALIGNMENT_LEFT, -1, kop).x
	var gx: float = x + bw - gw - 5 * sc * f - (maxf(15, t.marge_r()) if t.met_3d else 6)   # 3D: niet tegen de lijst (15: paneel rechts 3 px smaller, ronde 3)
	t._munt(t._munt_p(gx, y0 + kop + int(M.kop_dy), kop, f), f)
	t._tekst(vet, Vector2(gx + 5 * sc * f + 2, y0 + kop + int(M.kop_dy)), str(goud), -1, kop, Color("#f6e8ce") if t.met_3d else Color("#ffe07a"))
	var uitleg := String(kaart_.uitleg)
	var ub: float = bw - t.marge_r()
	t.draw_string(font, Vector2(x, y0 + regel_h + maat), uitleg, HORIZONTAL_ALIGNMENT_LEFT, ub, past(font, uitleg, int(M.uitleg), ub), Color("#f3e2c0"))
	var ky: float = y0 + regel_h * 2 + int(M.knop_dy)
	var kh: float = M.knop_h
	var kx := x
	t.knop_koop = Rect2()
	t.knop_undo = Rect2()
	t.knop_weg = Rect2()
	if int(kaart_.kost) >= 0 and bool(kaart_.get("demo_over", false)):
		# demo voorbij: tekst in plaats van de knop, zonder klikvlak (kern/demo_einde.gd)
		var vol: String = DEMO_EINDE.KAART
		t.draw_string(font, Vector2(kx, ky + kh / 2.0 + maat * 0.35), vol, HORIZONTAL_ALIGNMENT_LEFT, -1, maat, Color("#ffe07a"))
		kx += font.get_string_size(vol, HORIZONTAL_ALIGNMENT_LEFT, -1, maat).x + 4 * sc
	elif int(kaart_.kost) >= 0:
		if bool(kaart_.kan):
			t.knop_koop = knop(t, kx, ky, kh, "Buy", int(M.knop), vet, str(int(kaart_.kost)))   # muntje vóór de prijs, zoals bij Undo (28 nov)
			kx = t.knop_koop.end.x + 4 * sc
		else:
			var grijs := "%d  (%d more gold)" % [int(kaart_.kost), int(kaart_.tekort)]
			t._munt(Vector2(kx, ky + kh / 2.0 - 2 * sc))
			t.draw_string(font, Vector2(kx + 5 * sc + 2, ky + kh / 2.0 + maat * 0.35), grijs, HORIZONTAL_ALIGNMENT_LEFT, -1, maat, Color("#a8968a"))
			kx += 5 * sc + 2 + font.get_string_size(grijs, HORIZONTAL_ALIGNMENT_LEFT, -1, maat).x + 4 * sc
	if int(kaart_.terug) > 0:
		t.knop_undo = knop(t, kx, ky, kh, "Undo", int(M.knop2), vet, "+%d" % int(kaart_.terug))
		kx = t.knop_undo.end.x + 4 * sc
	if bool(kaart_.get("weg", false)):
		t.knop_weg = knop(t, kx, ky, kh, "Remove", int(M.knop2), vet)
