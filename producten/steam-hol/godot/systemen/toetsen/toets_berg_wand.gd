extends SceneTree
# Bram 17 nov 2026 (Daan 10:50, controleur 14:35 punt 1 en 2): de linkergrens van de hoedenberg in een ECHT 3D-hol met
# het wandblad, niet met een nep-hol. Meet de getekende berghoeden (berg_3d) tegen de getekende wandgaten (zoals
# hol_vast.gd ze tekent) en eist minstens 2 spelpx lucht; en dat eten berg_max niet verandert als de wand vol is.
# Gebruik: godot --headless --path . -s systemen/toetsen/toets_berg_wand.gd  (0 fouten = groen)

var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[berg-wand] OK " + wat)
	else:
		fout += 1
		print("[berg-wand] FOUT " + wat)

# Kleinste afstand (spelpx, hol) van een getekende berghoed tot een getekend wandgat; 1e9 = geen gat.
func afstand(g, hol) -> float:
	var H3 = load("res://hol/hol_3d.gd")
	var HV = load("res://hol/hol_vast.gd")
	var sch: float = absf(g.scale.x)
	var wp: Array = HV.wand_plekken(hol, H3.schatkamer_aan(hol))
	var gaten := []
	for i in mini(mini(g.hoeden.size(), HV.WAND_MAX), wp.size()):
		gaten.append(Rect2((Vector2(wp[i]) - Vector2(7.5, 6)).floor(), Vector2(15, 12)))
	var hoog: float = g.berg_hoog()
	var d := 1e9
	for e in g.berg_3d():
		var x: float = g.position.x + float(e[1]) * sch
		var nul: float = g.position.y + float(e[2]) * sch
		var vak := Rect2(x - 5.0 * sch, nul - hoog * sch, 11.2 * sch, hoog * sch)   # rechts tot ±6,2 (controleur punt 7)
		for r in gaten:
			if r.position.x >= g.position.x:
				continue
			var dx := maxf(0.0, maxf(r.position.x - vak.end.x, vak.position.x - r.end.x))
			var dy := maxf(0.0, maxf(r.position.y - vak.end.y, vak.position.y - r.end.y))
			d = minf(d, maxf(dx, dy))
	return d

func _init() -> void:
	var H3 = load("res://hol/hol_3d.gd")
	ok(H3.heeft_wand(), "wandblad geladen (anders bewijst deze toets niets)")
	for proef in [[480, 26, 1.0], [480, 26, 1.15], [640, 40, 1.0], [320, 20, 1.15]]:
		var hol := Node2D.new()
		hol.set_script(load("res://hol/hol.gd"))
		root.add_child(hol)
		hol.maak(int(proef[0]))
		hol.leg_aan(int(proef[1]))
		hol.vallen.clear()   # geen put: dan telt alleen de wand en de rand
		var g := Node2D.new()
		g.set_script(load("res://systemen/slijm.gd"))
		hol.add_child(g)
		g.zet(hol, 10)
		g.position = hol.cel_naar_pos(Vector2i(hol.schat_kol - 2, 0))
		g.scale = Vector2.ONE * float(proef[2])
		for i in 1200:
			g.hoeden.append(i % 10)
		g.werk_berg_grens()
		var naam := "hol %d/%d figuur %.2f" % [proef[0], proef[1], proef[2]]
		var d := afstand(g, hol)
		ok(d >= 2.0 - 0.01, "%s: berg (%d plekjes) minstens 2 spelpx van elk getekend gat (%.2f)" % [naam, g.berg_max, d])
		var links := 1e9
		for e in g.berg_3d():
			links = minf(links, g.position.x + (float(e[1]) - 5.0) * absf(g.scale.x))
		ok(links >= 2.0 - 0.01, "%s: berg binnen de linkerrand (%.1f)" % [naam, links])
		var voor: int = g.berg_max
		for i in 20:
			g.hoeden.append(i % 10)
			g.werk_berg_grens()
		ok(g.berg_max == voor, "%s: 20 hoeden erbij, wand vol, berg_max blijft %d (%d)" % [naam, voor, g.berg_max])
		hol.queue_free()
	print("[berg-wand] KLAAR fouten=%d" % fout)
	quit(1 if fout > 0 else 0)
