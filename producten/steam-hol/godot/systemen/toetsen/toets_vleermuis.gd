extends SceneTree
# Toetsen voor de vleermuis (Bram 16 nov). Draaien: godot --headless --path <map met project.godot> -s systemen/toetsen/toets_vleermuis.gd
var fout := 0

class NepHol:
	var gang: Array[bool] = []
	var boven: Array[bool] = []
	var vallen := {}
	var ingang_kol := 2
	var schat_kol := 30
	func _hash(x: int, y: int) -> int:   # zelfde als hol/hol.gd
		return int(abs(sin(x * 12.9898 + y * 78.233) * 43758.5453)) % 97

class NepHeld extends Node2D:
	func is_held() -> bool:
		return true

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[hol-toets] OK ", wat)
	else:
		fout += 1
		print("[hol-toets] FOUT ", wat)

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
	var a: Vector2 = V.vlucht_plek(100.0, 200.0, 28.0, 0.0)
	var m: Vector2 = V.vlucht_plek(100.0, 200.0, 28.0, 0.5)
	var e: Vector2 = V.vlucht_plek(100.0, 200.0, 28.0, 1.0)
	ok(a.is_equal_approx(Vector2(100, 28)) and e.is_equal_approx(Vector2(200, 28)) and is_equal_approx(m.x, 150.0) and m.y > 32.0,
		"vlucht: van, boog de gang in, naar")
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
	held.position = Vector2(int(vm.vm[0]["k"]) * 16 + 3.0, 37.0)
	vm._process(0.016)
	ok(vm.vm[0]["t"] < 0.0, "even rust na het landen")
	print("[hol-toets] KLAAR vleermuis fouten=%d" % fout)
	quit(1 if fout > 0 else 0)
