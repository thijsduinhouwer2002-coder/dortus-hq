extends SceneTree
# Olaf 28 nov 2026 (issue #388): Hol 2.0 proef, zonder beeld.
# - indeling: elke twee niveaus naast elkaar hebben een ladder, vallen staan niet op een ladder;
# - klikken om te lopen: Gloop komt vanaf de troon op elk niveau aan (tuin, 1, 2, 3) en weer terug;
# - scharrelen: 15 min spel met de tabel, Gloop staat nooit 40 s stil zonder gedraging, minstens 8 soorten gedrag;
# - helden: in 15 min vallen er helden op verdieping 1 en 2, en niemand blijft hangen;
# - besturen: W/S klimt alleen bij een ladder.
# - maat (#401, Daan #394 moet 1): op elk scherm 120 spelpx en 3 lagen in beeld; het venster is hoogte x schaal.
# Gebruik: godot --headless --path . -s systemen/toetsen/toets_hol2.gd  (0 fouten = groen)

var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[hol2] OK " + wat)
	else:
		fout += 1
		print("[hol2] FOUT " + wat)

func _init() -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = 7
	var kaart := Node2D.new()
	kaart.set_script(load("res://hol2/kaart.gd"))
	root.add_child(kaart)
	kaart.maak(1920, 3, rng)
	for n in range(0, 3):
		ok(not kaart.ladder_tussen(n, n + 1, 900.0).is_empty(), "ladder tussen niveau %d en %d" % [n, n + 1])
	var op_ladder := 0
	for v in kaart.vallen:
		for l in kaart.ladders:
			if (l.boven == v.niveau or l.onder == v.niveau) and absf(l.x - v.x) < 14:
				op_ladder += 1
	ok(op_ladder == 0, "geen val op een ladder (%d)" % op_ladder)
	ok(kaart.voet_y(0) == 22 and kaart.voet_y(1) == 70 and kaart.voet_y(2) == 118, "maten uit het ontwerpblad (22, 70, 118)")
	ok(kaart.niveau_bij(10) == 0 and kaart.niveau_bij(50) == 1 and kaart.niveau_bij(100) == 2 and kaart.niveau_bij(150) == 3, "klik-y naar niveau")

	var logs: Array = []
	var gl = load("res://hol2/gloop2.gd").new()
	gl.rng = rng
	gl.log_f = func(r): logs.append(r)
	gl.helden_ref = []
	gl.zet(kaart, kaart.troon_niveau, kaart.troon_x - 8)
	for doel in [[0, 300.0], [3, 1500.0], [1, 100.0], [2, 1900.0]]:
		gl.klik_naar(doel[0], doel[1])
		var t := 0.0
		while gl.loopt() and t < 400.0:
			gl.werk(0.1)
			t += 0.1
		ok(gl.niveau == doel[0] and absf(gl.x - clampf(doel[1], 4.0, 1916.0)) < 1.0 and not gl.klimt,
			"klik naar niveau %d x %d: aangekomen in %.0f s (niveau %d x %d)" % [doel[0], doel[1], t, gl.niveau, gl.x])

	# scharrelen met de tabel, met helden
	var helden: Array = []
	gl.helden_ref = helden
	gl.zet(kaart, kaart.troon_niveau, kaart.troon_x - 8)
	gl.doet = ""
	gl.kies()
	var gezien := {}
	var stil := 0.0
	var langst := 0.0
	var vorig: Vector2 = gl.pos()
	var vallen := {1: 0, 2: 0, 3: 0}
	var schat := 0
	var volgende := 2.0
	var n := 0
	var oud := 0
	var t2 := 0.0
	while t2 < 900.0:
		gl.werk(0.1)
		if gl.gekozen != "":
			gezien[gl.gekozen] = true
		if gl.pos() == vorig and gl.doet in ["", "op_weg"]:
			stil += 0.1
			langst = maxf(langst, stil)
		else:
			stil = 0.0
		vorig = gl.pos()
		volgende -= 0.1
		if volgende <= 0.0 and helden.size() < 10:
			var h = load("res://hol2/held2.gd").new()
			h.start(kaart, rng, "held0", "h%d" % n)
			n += 1
			helden.append(h)
			volgende = rng.randf_range(9.0, 16.0)
		for h in helden.duplicate():
			var e: String = h.werk(0.1)
			if e == "val":
				vallen[h.niveau] += 1
			elif e == "schat":
				schat += 1
			if h.weg:
				helden.erase(h)
			elif h.t > 400.0:
				oud += 1
				helden.erase(h)
		t2 += 0.1
	ok(langst < 40.0, "Gloop staat nooit lang stil zonder gedraging (langst %.1f s)" % langst)
	ok(gezien.size() >= 8, "minstens 8 soorten gedrag in 15 min (%d: %s)" % [gezien.size(), ", ".join(gezien.keys())])
	ok(vallen[1] > 0 and vallen[2] > 0, "helden vallen op verdieping 1 (%d) en 2 (%d)" % [vallen[1], vallen[2]])
	ok(oud == 0, "geen held blijft langer dan 400 s hangen (%d)" % oud)
	print("[hol2] info: %d helden, schat gepakt %d keer" % [n, schat])

	# besturen: W/S klimt alleen bij een ladder
	gl.zet(kaart, 1, 960.0)
	gl.pad.clear()
	var l: Dictionary = kaart.ladder_tussen(1, 2, 960.0)
	var ver := 960.0
	ok(not gl.klim_toets(false) or absf(l.x - 960.0) < 8.0, "S klimt niet zonder ladder")
	gl.pad.clear()
	gl.x = l.x + kaart.LAD_B / 2.0
	ok(gl.klim_toets(false), "S klimt bij een ladder naar beneden")
	var t3 := 0.0
	while gl.loopt() and t3 < 20.0:
		gl.stap(0.1)
		t3 += 0.1
	ok(gl.niveau == 2, "na het klimmen op verdieping 2 (%d)" % gl.niveau)

	# maat op elk scherm
	var H2 = load("res://hol2/hol2.gd")
	for sc in [[1, Vector2i(1920, 1080)], [2, Vector2i(3840, 2160)], [3, Vector2i(5760, 3240)]]:
		var m: Dictionary = H2.maten(120, sc[0], sc[1])
		ok(m.spel_h == 120 and m.venster_h == 120 * sc[0] and m.breed == 1920 and H2.lagen_in_beeld(m.spel_h) == 3,
			"schaal %d op %s: 120 spelpx, venster %d, breed %d, %d lagen in beeld" % [sc[0], sc[1], m.venster_h, m.breed, H2.lagen_in_beeld(m.spel_h)])
	var klein: Dictionary = H2.maten(240, 3, Vector2i(1280, 720))
	ok(klein.venster_h <= 360 and klein.spel_h == 240, "te grote schaal op een klein scherm gaat omlaag (schaal %d)" % klein.schaal)
	ok(H2.lagen_in_beeld(96) == 2 and H2.lagen_in_beeld(240) == 5, "96 spelpx 2 lagen, 240 spelpx 5 lagen")
	var F = load("res://hol2/focus.gd")
	ok(OS.get_name() == "Windows" or F.terug() == "niet op Windows", "focus-hulpje doet niets buiten Windows")
	print("[hol2] FOUT %d" % fout)
	quit(1 if fout > 0 else 0)
