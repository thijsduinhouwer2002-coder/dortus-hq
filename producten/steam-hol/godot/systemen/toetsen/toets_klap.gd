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
	# klap-ster van Mila (#43): 4 beelden op 8 per seconde, één keer, en de flits op de held (wit, half, niets)
	ok(K.ster_beeld(0.0) == 0 and K.ster_beeld(0.13) == 1 and K.ster_beeld(0.26) == 2 and K.ster_beeld(0.49) == 3, "klap-ster: beeld 0 tot 3, elk 0,125 s")
	ok(K.ster_beeld(0.5) == -1 and K.ster_beeld(2.0) == -1, "klap-ster: na 0,5 s weg (één keer, geen lus)")
	var KS: Texture2D = load("res://kunst/klapster.png")
	ok(KS.get_width() == 4 * KS.get_height(), "klapster.png: 4 vierkante beelden naast elkaar (%d x %d)" % [KS.get_width(), KS.get_height()])
	var HB = load("res://systemen/held_beeld.gd")
	ok(HB.flits("vallen", 0.0) == 1.0 and HB.flits("vallen", 0.13) == 0.5 and HB.flits("vallen", 0.2) == 0.0, "flits: 0,12 s wit, 0,06 s half, dan niets")
	ok(HB.flits("lopen", 0.0) == 0.0, "flits alleen bij vallen")
	var hn := Node2D.new()
	HB.flits_zet(hn, 1.0)
	ok(hn.material is ShaderMaterial and float(hn.material.get_shader_parameter("flits")) == 1.0, "flits: eigen ShaderMaterial op de held")
	HB.flits_zet(hn, 0.0)
	ok(hn.material == null, "na de flits weer geen materiaal (geen extra werk)")
	hn.free()
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
	# geluid (Sanne 25 nov, Iris punt 3): een vangst geeft een plof en net daarna een munt; munten niet ratelen
	var G = load("res://kern/geluid.gd")
	ok(G.mag("val", 0.0, 0.0) and G.mag("munt", 0.2, 0.0) and not G.mag("munt", 0.05, 0.0), "munt hooguit één per 0,12 s, plof altijd")
	var g: Node = Node.new()
	g.set_script(G)
	root.add_child(g)
	await process_frame
	ok(g.spelers.size() == G.SPELERS and not g.is_processing(), "geluid: spelers klaar, rekent niet als het stil is")
	g.vangst(false)
	ok(g.gespeeld == ["val"] and g.is_processing(), "vangst: eerst de plof")
	g._process(G.MUNT_NA_KLAP + 0.01)
	ok(g.gespeeld == ["val", "munt"] and not g.is_processing(), "vangst: dan de munt, en daarna weer stil")
	g.vangst(true)
	g.vangst(true)
	g._process(G.MUNT_NA_KLAP + 0.01)
	ok(g.gespeeld.slice(2) == ["hap", "hap", "munt"], "twee happen tegelijk: twee keer hap, maar één munt (%s)" % str(g.gespeeld))
	g.speel("koop")
	ok(g.gespeeld.back() == "koop" and g.spelers.any(func(p): return p.playing or p.stream != null), "koop klinkt")
	ok(is_equal_approx(g.spelers[0].volume_db, -6.0), "zacht: -6 dB")
	g.queue_free()
	# wegkijken (#86): de hoed van wie in de put viel komt op de toren, pas na Gloops eigen eerste hoed, niet in de demo
	var nep := GDScript.new()
	nep.source_code = "extends RefCounted\nvar demo := false\nvar slijm\nvar t := 0.0\nvar log := []\nfunc log_regel(r): log.append(r)\n"
	nep.reload()
	var st = nep.new()
	var sl: Node2D = Node2D.new()
	sl.set_script(load("res://systemen/slijm.gd"))
	st.slijm = sl
	var hs := GDScript.new()
	hs.source_code = "extends RefCounted\nvar hoed_nr := 6\n"
	hs.reload()
	var hd = hs.new()
	AF.put_hoed(st, hd)
	ok(sl.nacht_hoeden.is_empty() and sl.hoeden.is_empty(), "put-hoed: nog geen eigen hoed van Gloop, dan niets (eerste minuut blijft gelijk)")
	sl.hoeden.append(4)
	var at: int = sl.gegeten
	AF.put_hoed(st, hd)
	ok(sl.nacht_hoeden == [6] and sl.nacht_van > 0.0, "put-hoed: daarna valt zijn hoed op de toren (rij van de nacht, gestart)")
	ok(sl.gegeten == at, "put-hoed: telt niet als opgegeten (%d)" % sl.gegeten)
	ok(st.log.size() == 1 and String(st.log[0]).begins_with("HOL put-hoed 6"), "put-hoed: logregel voor de film")
	st.demo = true
	AF.put_hoed(st, hd)
	ok(sl.nacht_hoeden.size() == 1, "put-hoed: niet in de demo-film")
	# rij loopt al (Daan #92 punt 4): achteraan, de klok van de nacht start niet opnieuw
	st.demo = false
	var klok: float = sl.nacht_van
	sl.t += 5.0
	AF.put_hoed(st, hd)
	ok(sl.nacht_hoeden == [6, 6] and is_equal_approx(sl.nacht_van, klok), "put-hoed: achteraan de lopende rij, klok blijft %.2f" % sl.nacht_van)
	sl.free()
	print("[klap-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
