extends SceneTree
# Olaf 24 nov 2026 (issue 5): het kernmoment van de val. Reeksbonus, de laag kern/klap.gd (getal blijft onder het
# maaiveld, gaat weg en zet dan zijn rekenen uit).
# Dat een vlucht de reeks op 0 zet, staat in de duurtest (logregel "HOL reeks").
# Gebruik: godot --headless --path . -s systemen/toetsen/toets_klap.gd  (0 FOUT = groen)

var fout := 0

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[klap-toets] OK " + wat)
	else:
		fout += 1
		print("[klap-toets] FOUT " + wat)

func _init() -> void:
	var AF = load("res://kern/afloop.gd")
	var K = load("res://kern/klap.gd")
	ok(AF.reeks_bonus(1) == 0 and AF.reeks_bonus(2) == 0, "eerste en tweede vangst op rij: geen bonus")
	ok(AF.reeks_bonus(3) == 1 and AF.reeks_bonus(4) == 2, "derde +1, vierde +2")
	ok(AF.reeks_bonus(6) == 4 and AF.reeks_bonus(50) == 4, "hooguit +4")
	ok(K.maat(0.0, 3) == 36 and K.maat(0.5, 3) == 24, "getal eerst 1,5 keer, dan 8 spelpixels (24 px op schaal 3)")
	ok(is_equal_approx(K.zicht(0.0), 1.0) and is_equal_approx(K.zicht(K.DUUR), 0.0), "getal vervaagt naar 0 aan het eind")
	ok(K.reeks_kleur(2) != K.reeks_kleur(6), "reeks x6 heeft een andere kleur dan x2")
	# de laag zelf: vangst, rekent mee, en daarna stil
	var k: Node2D = Node2D.new()
	k.set_script(K)
	root.add_child(k)
	await process_frame
	ok(not k.is_processing() and not k.bezig(), "laag rekent niet als er niets te zien is (CPU)")
	for i in 5:
		k.vangst(Vector2(40, 38), 9, i + 1)
	ok(k.bijs.size() == 3, "nooit meer dan drie getallen tegelijk (%d)" % k.bijs.size())
	ok(k.is_processing() and k.bezig(), "na een vangst rekent de laag mee")
	k._process(K.DUUR + 0.1)
	ok(not k.bezig() and not k.is_processing(), "na de duur weg en het rekenen weer uit")
	k.queue_free()
	print("[klap-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
