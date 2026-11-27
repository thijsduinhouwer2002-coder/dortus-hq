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
# Daan #237 (kan): het nootje knipte nog aan en uit naast de zachte tekens van #85. Nu komt elk nootje in IN_S op (van
# doorzichtig naar vol) en gaat het nootje van een lied-held in UIT_S weg: aan het eind van zijn 2 s, of eerder zodra er
# een teken boven die held opkomt (teken_van = speltijd waarop dat teken begon, -1 = geen teken).
const IN_S := 0.2
const UIT_S := 0.15
static func nootjes(soort_held: String, lied_held: bool, staat: String, t: float, teken_van: float = -1.0) -> Array:
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
			uit.append([x, -int(round(8.0 * u)), noot_alfa(u) * clampf(leef / IN_S, 0.0, 1.0)])
	elif lied_held and t < NOOT_LIED_S:
		var a := lied_alfa(t, teken_van)
		if a > 0.0:
			uit.append([-2, -int(round(sin(t * 6.0))), a])   # wipt op de maat
	return uit

# Dekking van het nootje van een lied-held: op in IN_S, weg in UIT_S voor het eind of vanaf het teken dat het overneemt.
static func lied_alfa(t: float, teken_van: float = -1.0) -> float:
	var a := minf(clampf(t / IN_S, 0.0, 1.0), clampf((NOOT_LIED_S - t) / UIT_S, 0.0, 1.0))
	if teken_van >= 0.0 and t >= teken_van:
		a = minf(a, clampf(1.0 - (t - teken_van) / UIT_S, 0.0, 1.0))
	return a

# Hoogte waar de nootjes van een held aan hangen (rij boven de hoed). Die springt per beeld (de kruin van het sprongbeeld
# ligt 2 spelpx hoger) en een nootje vlak onder het gras werd dan in één beeld weggeknipt (Daan #237). Nu glijdt de
# hoogte met hooguit GLIJ_PX per s naar het doel; de stand staat in w (h.wip). Geeft hele spelpixels.
const GLIJ_PX := 20.0
static func glij(w: Dictionary, doel: float, t: float) -> int:
	var nu: float = float(w.get("noot_y", doel))
	var dt: float = clampf(t - float(w.get("noot_t", t)), 0.0, 0.5)
	if absf(doel - nu) > 12.0:
		nu = doel   # nieuwe plek (ladder, ander venster): meteen
	else:
		nu = move_toward(nu, doel, GLIJ_PX * dt)
	w["noot_y"] = nu
	w["noot_t"] = t
	return int(round(nu))

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
