# Hol 2.0 proef (Olaf, #388): wat elk beeld opnieuw getekend wordt (vallen, fakkels, hoedenstapel, helden, Gloop)
# en het bord rechts: alleen twee getallen, goud en hoeden (zoals Rusty), plus de gouden rand van de besturen-stand.
# Statische functies met hol2.gd als eerste argument (`s`).
extends RefCounted

const CIJFERS := ["111101101101111", "010110010010111", "111001111100111", "111001111001111", "101101111001001",
	"111100111001111", "111100111101111", "111001010010010", "111101111101111", "111101111001111"]
const GOUD := Color8(246, 204, 76)

static func _tegel(s, laag: CanvasItem, naam: String, pos: Vector2) -> void:
	var v: Array = s.info.tegels[naam]
	laag.draw_texture_rect_region(s.tex_tegels, Rect2(pos, Vector2(v[2], v[3])), Rect2(v[0], v[1], v[2], v[3]))

static func _rect(naam: String, s) -> Rect2:
	var v: Array = s.info.tegels[naam]
	return Rect2(v[0], v[1], v[2], v[3])

static func teken_leven(s) -> void:
	var laag: CanvasItem = s.leven
	var k = s.kaart
	var boven: float = s.scroll - 50.0
	var onder: float = s.scroll + s.spel_h + 20.0
	for v in k.vallen:
		var y: float = k.voet_y(v.niveau)
		if y < boven or y > onder:
			continue
		if v.soort == "luik":
			_tegel(s, laag, "luik_open" if v.open > 0.0 else "luik", Vector2(v.x, y))
		else:
			_tegel(s, laag, "stekels", Vector2(v.x, y - 2))
	var f := int(s.t * 3.0) % 2
	for p in k.fakkels:
		if p.y < boven or p.y > onder:
			continue
		_tegel(s, laag, "fakkel%d" % f, p)
	# hoedenstapel naast de troon: elke held die viel, is een hoed erbij
	var hi: Dictionary = s.info.hoeden
	var hx: float = k.troon_x - 12
	var hy: float = k.voet_y(k.troon_niveau)
	for i in s.hoeden.size():
		var rij: int = i % 14
		var kol: int = i / 14
		laag.draw_texture_rect_region(s.tex_fig.hoeden, Rect2(hx - kol * 7 - hi.w / 2.0, hy - hi.h - rij * 3, hi.w, hi.h),
			Rect2(s.hoeden[i] * hi.w, 0, hi.w, hi.h))
	for h in s.helden:
		if h.y < boven or h.y > onder + 20:
			continue
		h.teken(laag, s.tex_fig[h.soort], s.info[h.soort])
	s.gloop.teken(laag, s.tex_fig.gloop, s.info.gloop, s.tex_tegels, _rect("munt", s))
	for p in s.poef:
		var r := int(p.t * 14.0)
		for d in [Vector2(-1, -1), Vector2(1, -1), Vector2(-1, 1), Vector2(1, 1), Vector2(0, -1.4)]:
			laag.draw_rect(Rect2((p.pos + d * (2 + r)).round(), Vector2(1, 1)), Color8(210, 210, 200))

static func _getal(laag: CanvasItem, n: int, pos: Vector2, kleur: Color) -> float:
	var txt := str(n)
	var x := pos.x
	for c in txt:
		var m: String = CIJFERS[int(c)]
		for i in 15:
			if m[i] == "1":
				laag.draw_rect(Rect2(x + i % 3, pos.y + i / 3, 1, 1), kleur)
		x += 4
	return x

static func teken_scherm(s) -> void:
	var laag: CanvasItem = s.scherm_laag
	var w: float = s.breed
	var h: float = s.spel_h
	# bord rechts in de tuin, met een donkere onderlegger zodat het op gras en lucht leest
	var y := 11.0 - roundf(s.scroll)
	if y > -8.0:
		var x0 := w - 70.0
		laag.draw_rect(Rect2(x0 - 3, y - 2, 64, 9), Color(0.08, 0.06, 0.07, 0.75))
		laag.draw_texture_rect_region(s.tex_tegels, Rect2(x0, y + 1, 3, 3), _rect("munt", s))
		var x := _getal(laag, s.goud, Vector2(x0 + 5, y), GOUD)
		var hi: Dictionary = s.info.hoeden
		laag.draw_texture_rect_region(s.tex_fig.hoeden, Rect2(x + 6, y, hi.w, hi.h), Rect2(0, 0, hi.w, hi.h))
		_getal(laag, s.hoeden.size(), Vector2(x + 8 + hi.w, y), Color8(230, 226, 214))
		_knop(laag, knop_rect(s), s.besturen)
	if s.besturen:
		laag.draw_rect(Rect2(0, 0, w, 1), GOUD)
		laag.draw_rect(Rect2(0, h - 1, w, 1), GOUD)
		laag.draw_rect(Rect2(0, 0, 1, h), GOUD)
		laag.draw_rect(Rect2(w - 1, 0, 1, h), GOUD)

# Stuurknop (Sanne #401 punt 5, ontwerpblad punt 2): vierkant van 9 spelpx links van het bord, vier pijltjes.
# Een klik zet de besturen-stand aan of uit (een klik op Gloop is voor het kaartje van het echte spel).
static func knop_rect(s) -> Rect2:
	return Rect2(s.breed - 84.0, 9.0 - roundf(s.scroll), 9, 9)

static func _knop(laag: CanvasItem, r: Rect2, aan: bool) -> void:
	laag.draw_rect(r, GOUD if aan else Color(0.08, 0.06, 0.07, 0.85))
	laag.draw_rect(r, GOUD, false, 1.0)
	var k := Color(0.08, 0.06, 0.07) if aan else GOUD
	var c := r.position + Vector2(4, 4)
	for d in [Vector2(0, -1), Vector2(0, 1), Vector2(-1, 0), Vector2(1, 0)]:
		var p: Vector2 = c + d * 3
		laag.draw_rect(Rect2(p, Vector2(1, 1)), k)                      # punt van het pijltje
		laag.draw_rect(Rect2(p - d + Vector2(d.y, d.x), Vector2(1, 1)), k)  # twee schouders
		laag.draw_rect(Rect2(p - d - Vector2(d.y, d.x), Vector2(1, 1)), k)
	laag.draw_rect(Rect2(c, Vector2(1, 1)), k)                          # midden: Gloop
