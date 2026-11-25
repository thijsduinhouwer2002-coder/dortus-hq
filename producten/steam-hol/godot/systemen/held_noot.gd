extends RefCounted
# Muzieknootjes boven een held (los van held_beeld.gd sinds 25 nov, Olaf #25: dat bestand bleef anders boven de 400 regels).
# held_beeld.gd houdt nootjes() en noot_alfa() als doorgeefluik, zodat toetsen en aanroepers niets merken.
# Gebruikt van de held alleen h.HELD_BEELD (noot_y_min en teken_vak_3d).

# Muzieknootjes (Sanne toets 10 punt 1: "het lied zie je niet"). Een bard die binnenloopt of vlucht laat elke 2 s een
# nootje opstijgen (4 s lang, 8 spelpixels omhoog, vervaagt), dus 2 tegelijk; een held die door het lied komt heeft
# de eerste 2 s één nootje boven zijn hoofd. Geeft [x, dy, alfa] per nootje; dy 0 = vlak boven de hoed.
const NOOT_ELKE_S := 2.0
const NOOT_LEEF_S := 4.0
const NOOT_LIED_S := 2.0
static func nootjes(soort_held: String, lied_held: bool, staat: String, t: float) -> Array:
	var uit := []
	if staat in ["weg", "vallen"]:
		return uit
	if soort_held == "bard" and staat in ["afdalen", "lopen", "vluchten", "klimmen"]:
		var k := int(floor(t / NOOT_ELKE_S))
		for i: int in [k, k - 1]:
			if i < 0:
				continue
			var leef: float = t - float(i) * NOOT_ELKE_S
			if leef < 0.0 or leef >= NOOT_LEEF_S:
				continue
			var u: float = leef / NOOT_LEEF_S
			var x := (2 if i % 2 == 0 else -5) + int(round(sin(leef * 3.0)))   # om en om links en rechts, wiebelt een pixel
			uit.append([x, -int(round(8.0 * u)), noot_alfa(u)])
	elif lied_held and t < NOOT_LIED_S:
		uit.append([-2, -int(round(sin(t * 6.0))), 1.0])   # wipt op de maat
	return uit

# Alfa van een opstijgend nootje: vervaagt, en in het laatste kwart sneller naar 0, zodat hij verdwijnt voor hij een rand
# raakt (Daan 14 nov 03:50: niet doormidden gaan).
static func noot_alfa(u: float) -> float:
	return clampf((1.0 - u * u) * clampf((1.0 - u) / 0.25, 0.0, 1.0), 0.0, 1.0)

# Nootje van 5 x 5 in pixels (achtste noot met vlag), tot Mila er een tekening voor heeft (tekens.png, 2 beelden).
const NOOT_PIX := ["..##.", "..#.#", "..#..", "###..", "###.."]
static func noot(h, x: int, y: int, alfa: float) -> void:
	var y_min: int = h.HELD_BEELD.noot_y_min(h)   # Daan 14 nov 02:45, 15 nov 14:45: de noot blijft onder het gras
	if y < y_min:   # Daan 03:50: wil hij hoger dan mag, dan vervaagt hij daar in 3 spelpixels in plaats van te blijven hangen
		alfa *= clampf(1.0 - float(y_min - y) / 3.0, 0.0, 1.0)
		y = y_min
	if alfa <= 0.02:
		return
	if h.HELD_BEELD.teken_vak_3d(h, "noot", Vector2(x - 2, y - 3), Color(1, 1, 1, alfa)):
		return   # 3D-noot uit het blad tekens (Daan: valt in het 8x8-vak precies over het 5x5-pixelnootje)
	var licht := Color(1.0, 0.88, 0.45, alfa)
	var rand := Color(0.13, 0.08, 0.05, alfa * 0.9)
	for ry in 5:
		for rx in 5:
			if NOOT_PIX[ry][rx] == "#":
				for d in [Vector2i(-1, 0), Vector2i(1, 0), Vector2i(0, -1), Vector2i(0, 1)]:
					var nx: int = rx + d.x
					var ny: int = ry + d.y
					if nx < 0 or ny < 0 or nx > 4 or ny > 4 or NOOT_PIX[ny][nx] != "#":
						h.draw_rect(Rect2(x + nx, y + ny, 1, 1), rand)   # donkere rand, leesbaar op lucht en aarde
	for ry in 5:
		for rx in 5:
			if NOOT_PIX[ry][rx] == "#":
				h.draw_rect(Rect2(x + rx, y + ry, 1, 1), licht)
