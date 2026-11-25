extends SceneTree
# Olaf 25 nov 2026 (issue #97): licht en klein leven in een echt hol.
# - lichtkaart: gras blijft 1, gang donkerder dan aarde ver van licht, bij de fakkel lichter dan ver weg;
# - flakkeren blijft tussen 0,9 en 1,0;
# - lichtplas om de fakkel groot genoeg (Daan #106);
# - leven: elk ding vindt een plek in een gewoon hol, de vleermuis wiegt zacht in en uit;
#   in 10 min spel nooit twee tegelijk, gaten tussen 5 en 15 s, alle drie soorten komen voor.
# Gebruik: godot --headless --path . -s systemen/toetsen/toets_licht.gd  (0 fouten = groen)

var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[licht] OK " + wat)
	else:
		fout += 1
		print("[licht] FOUT " + wat)

func helder(c: Color) -> float:
	return (c.r + c.g + c.b) / 3.0

func _init() -> void:
	var L = load("res://systemen/licht.gd")
	var G = load("res://systemen/licht_gloed.gd")
	var V = load("res://systemen/leven.gd")
	var hol := Node2D.new()
	hol.set_script(load("res://hol/hol.gd"))
	root.add_child(hol)
	hol.maak(480)
	hol.leg_aan(26)
	var licht = L.maak_in(hol)
	licht._maak_kaart()
	var img: Image = licht.tex.get_image()
	var px := func(x: float, y: float) -> Color:
		return img.get_pixel(int(x / L.STAP), int(y / L.STAP))
	ok(helder(px.call(100, 2)) > 0.99, "gras en lucht blijven ongemoeid (%.2f)" % helder(px.call(100, 2)))
	var f: Vector2 = L.fakkel_punt(hol)
	var ver_gang := Vector2((hol.schat_kol - 5) * 16 + 8, 32)
	ok(f.distance_to(ver_gang) > 40, "meetplek in de gang ver van de fakkel (%.0f)" % f.distance_to(ver_gang))
	var bij: float = helder(px.call(f.x + 6, 30))
	var ver: float = helder(px.call(ver_gang.x, ver_gang.y))
	ok(bij > ver + 0.15, "gang bij de fakkel lichter dan ver weg (%.2f tegen %.2f)" % [bij, ver])
	var aarde: float = helder(px.call(40, 20))
	ok(hol.boven[2] == false, "meetplek aarde is dicht")
	ok(ver < aarde, "gang ver van licht donkerder dan aarde ver van licht (%.2f tegen %.2f)" % [ver, aarde])
	ok(ver > 0.5, "nooit zwart: donkerste gang %.2f" % ver)
	var lo := 9.0
	var hi := 0.0
	for i in 2000:
		var v: float = G.flakker(i * 0.037, i % 3)
		lo = minf(lo, v)
		hi = maxf(hi, v)
	ok(lo >= 0.9 - 0.001 and hi <= 1.0 + 0.001, "flakkeren tussen 0,9 en 1,0 (%.3f tot %.3f)" % [lo, hi])
	var kaart: int = licht.keer
	licht._process(1.0)
	licht._process(1.0)
	ok(licht.keer == kaart + 1, "kaart niet opnieuw zonder verandering (%d keer)" % licht.keer)

	# Daan #106 moet 3: de plas om de fakkel is groot en fel genoeg (2 tegels, dekking 0,4 tegen 0,2 eerst)
	ok(G.FAKKEL_R >= 30.0 and G.KLEUR_FAKKEL.a >= 0.35, "lichtplas om de fakkel: straal %.0f, dekking %.2f" % [G.FAKKEL_R, G.KLEUR_FAKKEL.a])
	# vleermuis in het hol (zelfde als hol_lagen.gd), zodat hij kan wiegen
	var wz := Node2D.new()
	var vm := Node2D.new()
	vm.set_script(load("res://systemen/vleermuis.gd"))
	vm.name = "Vleermuis"
	hol.add_child(vm)
	hol.add_child(wz)
	vm.zet(hol, wz)
	ok(vm.vm.size() >= 1, "vleermuis hangt in het hol (%d)" % vm.vm.size())
	for s in V.SOORTEN:
		ok(V.kies_plek(hol, s) != null, "plek voor %s in een gewoon hol" % s)
	ok(not ("worm" in V.SOORTEN or "mot" in V.SOORTEN or "kruimels" in V.SOORTEN), "worm, mot en kruimels zijn eruit (Daan #106)")
	var VM = load("res://systemen/vleermuis.gd")
	var hk := 0.0
	for i in 300:
		hk = maxf(hk, absf(VM.wieg_hoek(i * 0.01)))
	ok(hk <= VM.WIEG_HOEK + 0.001 and hk > 0.1 and VM.wieg_hoek(0.0) == 0.0 and VM.wieg_hoek(VM.WIEG_S) == 0.0,
			"vleermuis wiegt zacht in en uit (grootste hoek %.2f)" % hk)

	var lv = V.maak_in(hol, 3)
	var gaten: Array = []
	var stil := 0.0
	var was := ""
	for i in 6000:   # 10 min op 10 beelden per s
		lv._process(0.1)
		vm._process(0.1)
		if lv.soort == "":
			stil += 0.1
		elif was == "":
			if i > 1:
				gaten.append(stil)
			stil = 0.0
		was = lv.soort
	var lo_g := 99.0
	var hi_g := 0.0
	for g in gaten:
		lo_g = minf(lo_g, g)
		hi_g = maxf(hi_g, g)
	ok(gaten.size() >= 25, "in 10 min %d kleine dingen" % (gaten.size() + 1))
	ok(lo_g >= 4.9 and hi_g <= 15.2, "gaten tussen 5 en 15 s (%.1f tot %.1f)" % [lo_g, hi_g])
	for s in V.SOORTEN:
		ok(int(lv.gedaan.get(s, 0)) >= 3, "%s kwam %d keer" % [s, int(lv.gedaan.get(s, 0))])
	print("[licht] klaar: FOUT %d" % fout)
	quit(1 if fout > 0 else 0)
