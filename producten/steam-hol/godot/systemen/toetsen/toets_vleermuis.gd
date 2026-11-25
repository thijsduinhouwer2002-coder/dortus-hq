extends SceneTree
# Toetsen voor de vleermuis (Bram 16 nov). Draaien: godot --headless --path <map met project.godot> -s systemen/toetsen/toets_vleermuis.gd
var fout := 0

class NepHol:
	var gang: Array[bool] = []
	var boven: Array[bool] = []
	var vallen := {}
	var ingang_kol := 2
	var schat_kol := 30
	var deco_proef := false   # true: hol_vast.gd ziet het hol nooit als vol (zoals de keurstrook)
	func _hash(x: int, y: int) -> int:   # zelfde als hol/hol.gd
		return int(abs(sin(x * 12.9898 + y * 78.233) * 43758.5453)) % 97

class NepHeld extends Node2D:
	func is_held() -> bool:
		return true

class NepGloop extends Node2D:
	var groot := false
	func berg(_tel := -1) -> Array:
		return []
	func is_groot() -> bool:
		return groot

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[hol-toets] OK ", wat)
	else:
		fout += 1
		print("[hol-toets] FOUT ", wat)

# Raakt de held (x ± 5, de hele ganghoogte) de vleermuis zoals _draw() hem tekent? Hangend 18 breed, vliegend 0,6 keer.
func _raakt(vm, v: Dictionary, held_x: float) -> bool:
	var mx := int(v["k"]) * 16 + 8.0
	var half := 9.0
	if v["t"] >= 0.0 or float(v["zweef_t"]) >= 0.0:
		mx = vm.lucht_plek(v).x
		half = 9.0 * vm.VLIEG_MAAL
	return absf(held_x - mx) < half + 5.0

func nep(van: int, tot: int, breed := 40) -> NepHol:
	var h := NepHol.new()
	for k in breed:
		h.gang.append(k >= van and k <= tot)
		h.boven.append(false)
	h.ingang_kol = van
	h.schat_kol = tot
	return h

func _init() -> void:
	var V = load("res://systemen/vleermuis.gd")
	ok(V.aantal(5) == 0 and V.aantal(10) == 1 and V.aantal(23) == 1 and V.aantal(24) == 2, "aantal: leeg hol geen, groot hol twee")
	var h := nep(2, 30)
	h.deco_proef = true   # eerst de gewone regels, zonder het volle hol van hol_vast.gd
	h.vallen[10] = "stekelput"
	h.boven[14] = true
	var p: Array = V.plekken(h)
	ok(not p.has(2) and not p.has(3) and not p.has(29) and not p.has(30), "niet bij schacht en schatkamer: " + str(p))
	ok(not p.has(10) and not p.has(14) and p.has(4) and p.has(28), "niet boven een val of onder een kamer")
	var k2: Array = V.kies(h, 2)
	ok(k2.size() == 2 and absi(int(k2[0]) - int(k2[1])) >= 3, "twee plekken, ver genoeg uit elkaar: " + str(k2))
	ok(V.kies(h, 2) == k2, "vaste keuze (hash), elke start gelijk")
	for k in k2:
		ok(V.mag_hangen(h, int(k)), "gekozen plek %d mag" % int(k))
	# vlucht weg van de held: held links van kolom 20, dan naar rechts
	var d: int = V.vlucht_doel(h, 20, 20 * 16 + 2.0, [])
	ok(d > 20 and d - 20 >= 2 and V.mag_hangen(h, d), "held links: vliegt naar rechts (%d)" % d)
	d = V.vlucht_doel(h, 20, 20 * 16 + 14.0, [])
	ok(d < 20 and 20 - d >= 2 and V.mag_hangen(h, d), "held rechts: vliegt naar links (%d)" % d)
	d = V.vlucht_doel(h, 27, 27 * 16 + 2.0, [])
	ok(d >= 0 and d < 27, "aan het eind van de gang: dan toch de andere kant op (%d)" % d)
	ok(V.vlucht_doel(h, 20, 322.0, [22, 23]) == 24, "bezette plekken overslaan")
	# vol hol (Olaf, hol_vast.gd): niet hangen waar al een stut, spinrag of vaandel hangt (kan Olaf 16 nov 09:45)
	var hv := nep(2, 30)
	hv.vallen[10] = "stekelput"
	hv.boven[14] = true
	var HV = load("res://hol/hol_vast.gd")
	var bezet: Dictionary = V.vol_plafond_kols(hv)
	var pv: Array = V.plekken(hv)
	ok(bezet.size() > 0, "vol hol: er hangen plafonddingen (%s)" % str(bezet.keys()))
	var los := true
	for k in pv:
		if bezet.has(k):
			los = false
	ok(los and pv.size() > 0, "vol hol: vleermuis nooit onder een plafondding (%s)" % str(pv))
	var nagelopen := {}
	var vorige := -99
	for k in range(hv.ingang_kol + 1, hv.schat_kol - 1):
		if HV.vol_plafond(hv, k, vorige) >= 0:
			nagelopen[k] = true
			vorige = k
	ok(nagelopen == bezet, "vol hol: zelfde kolommen als hol_vast.gd tekent")
	for k in V.kies(hv, 2):
		ok(not bezet.has(k), "vol hol: gekozen plek %d is vrij" % int(k))
	var a: Vector2 = V.vlucht_plek(100.0, 200.0, 28.0, 0.0)
	var m: Vector2 = V.vlucht_plek(100.0, 200.0, 28.0, 0.5)
	var e: Vector2 = V.vlucht_plek(100.0, 200.0, 28.0, 1.0)
	ok(a.is_equal_approx(Vector2(100, 28)) and e.is_equal_approx(Vector2(200, 28)) and is_equal_approx(m.x, 150.0) and m.y > 28.5 and m.y < 30.0,
		"vlucht: van, kleine boog (boven de hoofden), naar")
	# klein hol: geen vleermuis; groot hol: een die opvliegt als een held eronder loopt, en daarna weer hangt
	var root_node := Node2D.new()
	get_root().add_child(root_node)
	var wezens := Node2D.new()
	var vm := Node2D.new()
	vm.set_script(V)
	root_node.add_child(vm)
	root_node.add_child(wezens)
	vm.zet(nep(2, 8), wezens)
	ok(vm.ct != null, "blad kunst/3d/vleermuis.png geladen")
	ok(vm.vm.size() == 0, "klein hol (7 tegels): geen vleermuis")
	vm.hol = h
	vm.herkies()
	ok(vm.vm.size() == 2, "groot hol (29 tegels): twee vleermuizen")
	var k0: int = int(vm.vm[0]["k"])
	var held := NepHeld.new()
	wezens.add_child(held)
	held.position = Vector2(k0 * 16 + 3.0, 37.0)
	vm._process(0.016)
	ok(vm.vm[0]["t"] >= 0.0 and int(vm.vm[0]["naar"]) != k0, "held eronder: vleermuis vliegt op")
	for i in 100:
		vm._process(0.016)
	ok(vm.vm[0]["t"] < 0.0 and int(vm.vm[0]["k"]) == int(vm.vm[0]["naar"]) and int(vm.vm[0]["k"]) != k0, "na de vlucht hangt hij op een nieuwe plek")
	held.position = Vector2(int(vm.vm[0]["k"]) * 16 + 8.0 - 20.0, 37.0)
	vm._process(0.016)
	ok(vm.vm[0]["t"] < 0.0, "even rust na het landen (held op 20 px)")
	held.position = Vector2(int(vm.vm[0]["k"]) * 16 + 8.0 - 12.0, 37.0)
	vm._process(0.016)
	ok(vm.vm[0]["t"] >= 0.0, "held raakt hem bijna (12 px): ook in de rust weg")
	for i in 100:
		vm._process(0.016)
	wezens.remove_child(held)
	# Daan #59: de held liep een halve seconde door de vleermuis heen. Nu: een held die onder elke vleermuis
	# door loopt (gewoon tempo 5,6 en eerste held 15 px/s, beide kanten op) raakt hem nooit.
	for snel in [5.6, 7.5, 15.0]:
		for richting in [1.0, -1.0]:
			vm.hol = h
			vm.herkies()
			var loper := NepHeld.new()
			wezens.add_child(loper)
			var start_x: float = (3 * 16.0) if richting > 0 else (29 * 16.0)
			loper.position = Vector2(start_x, 37.0)
			var raak := 0
			var langs := 0
			var vlucht := 0
			for i in int(26 * 16 / snel / 0.02):
				loper.position.x += richting * snel * 0.02
				vm._process(0.02)
				for v in vm.vm:
					if v["t"] >= 0.0:
						vlucht += 1
					if _raakt(vm, v, loper.position.x):
						if v["t"] >= 0.0 and float(v.get("tempo", 1.0)) > 1.0:
							langs += 1   # klem: snel langs de held, mag kort
						else:
							raak += 1
			ok(raak == 0 and vlucht > 0, "held op %s px/s (%s) raakt geen hangende of wegvliegende vleermuis (%d beelden raak, %d in de lucht)" % [str(snel), "rechts" if richting > 0 else "links", raak, vlucht])
			ok(langs * 0.02 <= 0.5, "klem aan het eind: samen hooguit 0,5 s langs de held (%.2f s)" % (langs * 0.02))
			wezens.remove_child(loper)
			loper.free()
	# Kort hol zoals de eerste minuut (zaad 2: ladder 6, put 9, Gloop): maar één plek. Daan #59 zag de held er dwars
	# doorheen lopen, want er was geen plek om heen te vliegen. Nu: snel langs, achter de held fladderen, dan terug.
	var w3 := Node2D.new()
	var vm3 := Node2D.new()
	vm3.set_script(V)
	root_node.add_child(vm3)
	root_node.add_child(w3)
	var eerst := nep(6, 16)
	eerst.deco_proef = true
	eerst.vallen[9] = "stekelput"
	var gl3 := NepGloop.new()
	gl3.position = Vector2(221.5, 37.0)
	w3.add_child(gl3)
	vm3.zet(eerst, w3)
	vm3._process(0.016)
	ok(vm3.vm.size() == 1 and int(vm3.vm[0]["k"]) == 8 and V.plekken(eerst, vm3._grens) == [8], "kort hol: één vleermuis op de enige plek (%s)" % str(vm3.vm))
	var eh := NepHeld.new()
	w3.add_child(eh)
	eh.position = Vector2(100.0, 37.0)
	var eraak := 0
	var elangs := 0
	var gezweefd := false
	for i in 1000:   # 20 s: held loopt op 7,5 px/s helemaal door
		eh.position.x += 7.5 * 0.02
		vm3._process(0.02)
		var v3: Dictionary = vm3.vm[0]
		if float(v3["zweef_t"]) >= 0.0:
			gezweefd = true
		if _raakt(vm3, v3, eh.position.x):
			if v3["t"] >= 0.0 and float(v3["tempo"]) > 1.0:
				elangs += 1
			else:
				eraak += 1
	ok(eraak == 0 and gezweefd, "kort hol: held raakt de vleermuis niet, die fladdert achter hem (%d beelden raak)" % eraak)
	ok(elangs * 0.02 <= 0.4, "kort hol: hooguit 0,4 s snel langs de held (%.2f s)" % (elangs * 0.02))
	ok(vm3.vm[0]["t"] < 0.0 and float(vm3.vm[0]["zweef_t"]) < 0.0 and int(vm3.vm[0]["k"]) == 8, "kort hol: daarna hangt hij weer op zijn plek")
	# nooit achter de hoedenberg (Mila 17 nov 08:00): rechterrand tegel minstens 70 (groot 72) spelpixels links van Gloop
	ok(is_equal_approx(V.berg_grens(456.0, false), 386.0) and is_equal_approx(V.berg_grens(456.0, true), 384.0), "berggrens 70, groot 72")
	ok(is_equal_approx(V.berg_grens(456.0, false, 1.15), 456.0 - 80.5), "berggrens schaalt mee met Gloop (1,15)")
	var gx := 28 * 16 + 8.0   # Gloop op schat_kol - 2 zoals strook.gd
	var gr: float = V.berg_grens(gx, false)
	var pg: Array = V.plekken(h, gr)
	var achter := false
	for k in pg:
		if int(k) * 16 + 16 > gx - 70.0:
			achter = true
	ok(not achter and pg.size() > 0 and not pg.has(24) and pg.has(22), "met Gloop: geen plek binnen 70 px van zijn midden (%s)" % str(pg))
	for k in V.kies(h, 2, gr):
		ok(V.mag_hangen(h, int(k), gr), "gekozen plek %d ligt links van de berg" % int(k))
	var dg: int = V.vlucht_doel(h, 20, 20 * 16 + 2.0, [], gr)
	ok(dg >= 0 and dg * 16 + 16 <= gx - 70.0, "vlucht weg van de held gaat niet achter de berg (%d)" % dg)
	var kort := nep(2, 12)   # 11 gangtegels, maar links van de berg alleen 4 en 5, en daar zit een val
	kort.deco_proef = true
	kort.vallen[4] = "stekelput"
	kort.vallen[5] = "stekelput"
	ok(V.kies(kort, 1, V.berg_grens(10 * 16 + 8.0, false)).size() == 0, "kort hol: geen plek links van de berg, dan geen vleermuis")
	# in het spel: Gloop in Wezens, eerste beeld kiest opnieuw met zijn grens
	var w2 := Node2D.new()
	var vm2 := Node2D.new()
	vm2.set_script(V)
	root_node.add_child(vm2)
	root_node.add_child(w2)
	vm2.zet(h, w2)
	var gl := NepGloop.new()
	gl.groot = true
	gl.position = Vector2(gx, 37.0)
	w2.add_child(gl)
	vm2._process(0.016)
	var alle_links: bool = vm2.vm.size() > 0
	for v in vm2.vm:
		if int(v["k"]) * 16 + 16 > gx - 72.0:
			alle_links = false
	ok(alle_links, "spel: na het eerste beeld hangt elke vleermuis links van de berg (groot lijf, %s)" % str(vm2.vm))
	var kort2 := nep(2, 12)
	kort2.deco_proef = true
	kort2.vallen[4] = "stekelput"
	kort2.vallen[5] = "stekelput"
	vm2.zet(kort2, w2)   # zonder grens: dan hangt er wel een (achter de berg)
	ok(vm2.vm.size() == 1, "kort hol zonder Gloop-grens: wel een vleermuis (toets toetst iets)")
	gl.position = Vector2(10 * 16 + 8.0, 37.0)
	vm2._kijk_t = 1.0
	vm2._process(0.016)
	ok(vm2.vm.size() == 0, "spel: kort hol met Gloop, geen vleermuis (%d)" % vm2.vm.size())
	# spinrag (hol_vast.gd, Olaf 08:35): bij de berg web wel, spin niet; zelfde grens als de vleermuis (groot lijf)
	ok(is_equal_approx(HV.spin_grens(h), V.berg_grens(28 * 16 + 8.0, true)), "spinrag-grens = vleermuis-grens bij Gloop op schat_kol - 2 (%s)" % str(HV.spin_grens(h)))
	# spinrag niet boven de hoedenberg (Daan 17 nov 10:50): grens = linkerkant van het meest linkse plekje, groot lijf
	var S = load("res://systemen/slijm.gd")
	var bm_oud: int = S.berg_max
	S.zet_berg_max(10)   # 10 plekjes = 4 schuine rijen, meest links d = 3: -14 - 18 - 3 - 5 = -40, min 2 lucht
	var verwacht: float = 28 * 16 + 8.0 - 40.0 - 2.0
	ok(is_equal_approx(HV.berg_links(h), verwacht), "spinrag: bergrand bij 10 plekjes %s (verwacht %s)" % [str(HV.berg_links(h)), str(verwacht)])
	S.zet_berg_max(1)
	ok(HV.berg_links(h) > verwacht, "spinrag: kleinere berg, grens verder rechts")
	S.zet_berg_max(0)
	ok(HV.berg_links(h) == INF, "spinrag: geen berg, geen grens")
	S.zet_berg_max(1 << 30)
	ok(is_equal_approx(HV.berg_links(h), HV.spin_grens(h)), "spinrag: grens nog niet berekend, dan de volle berg van de vleermuis")
	ok(HV._spin_rechts(Vector2(100, 0), true, false) == 108.0, "spinrag: pixelding is een tegel breed")
	S.zet_berg_max(bm_oud)
	print("[hol-toets] KLAAR vleermuis fouten=%d" % fout)
	quit(1 if fout > 0 else 0)
