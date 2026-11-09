extends SceneTree
# Toetsen voor held.gd en slijm.gd (Bram). Draaien: godot --headless --path <godot-map> -s systemen/toetsen/toets_held.gd
var fout := 0
var uitkomst := ""
var uit_info := {}

func ok(voorwaarde: bool, wat: String) -> void:
	if voorwaarde:
		print("[held-toets] OK ", wat)
	else:
		fout += 1
		print("[held-toets] FOUT ", wat)

func _klaar(_h, u: String, i: Dictionary) -> void:
	uitkomst = u
	uit_info = i

# Bouw een hol met slijm op kolom 6 en (optioneel) een put op kolom 9; laat één held lopen tot hij klaar is.
func speel(info: Dictionary, met_put := true, met_slijm := true) -> Dictionary:
	var hol := Node2D.new()
	hol.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	if met_put:
		hol.vallen[9] = "stekelput"
	var wezens := Node2D.new()
	hol.add_child(wezens)
	var slijm = null
	if met_slijm:
		slijm = Node2D.new()
		slijm.set_script(load("res://systemen/slijm.gd"))
		wezens.add_child(slijm)
		slijm.zet(hol, 6)
	var held := Node2D.new()
	held.set_script(load("res://systemen/held.gd"))
	wezens.add_child(held)
	uitkomst = ""
	uit_info = {}
	held.klaar.connect(_klaar)
	held.start(hol, info)
	var eerste_doel: int = held.doel_kol
	var trek: String = held.trek
	var stappen := 0
	while uitkomst == "" and stappen < 20000:
		held.stap(1.0 / 15.0)
		stappen += 1
	var r := {"uitkomst": uitkomst, "info": uit_info, "eerste_doel": eerste_doel, "trek": trek, "tijd": stappen / 15.0,
		"slijm_plat": slijm != null and not slijm.kan_vechten(), "slijm_gegeten": slijm.gegeten if slijm != null else 0,
		"slijm_bestaat": slijm != null and is_instance_valid(slijm)}
	hol.free()
	return r

func _init() -> void:
	# 1. de eerste held van een nieuw spel valt altijd, bij de eerste verdediging
	var r := speel({"naam": "Odo", "bezoeken": 0, "wrok": "", "moet_vallen": true, "zaad": 1})
	ok(r.uitkomst == "gevallen" and r.info.laatst_geraakt == "Gloop the Slime", "eerste held valt bij de slijm (%s, %s)" % [r.uitkomst, r.info.get("wat", "")])
	ok(r.slijm_gegeten == 1, "slijm telt zijn hap")
	ok(r.tijd < 60.0, "binnen een minuut goud (%.1f s)" % r.tijd)

	# 2. wrok tegen de put: loopt eerst naar de put, niet naar de schat
	r = speel({"naam": "Kees", "bezoeken": 1, "wrok": "the Spike Pit", "zaad": 2}, true, false)
	ok(r.eerste_doel == 9, "held met wrok tegen de put loopt eerst naar de put (doel %d)" % r.eerste_doel)
	ok(r.info.get("gezien_vijand", false), "hij heeft zijn vijand bereikt")
	r = speel({"naam": "Kees", "bezoeken": 1, "wrok": "Gloop the Slime", "zaad": 2})
	ok(r.eerste_doel == 6, "wrok tegen de slijm: doel is de slijm (doel %d)" % r.eerste_doel)
	r = speel({"naam": "Kees", "bezoeken": 1, "wrok": "Gloop the Slime", "zaad": 2}, true, false)
	ok(r.eerste_doel == 12, "vijand weg: dan gewoon naar de schat")

	# 3. geen verdediging: hij raakt de schat aan, pakt niets en wordt Hoard-Toucher
	r = speel({"naam": "Pim", "bezoeken": 0, "wrok": "", "zaad": 3}, false, false)
	ok(r.uitkomst == "ontsnapt" and r.info.get("hoard_toucher", false), "schat gehaald: ontsnapt als Hoard-Toucher")
	ok(String(r.info.get("wat", "")).contains("took nothing"), "hij pakt niets: " + String(r.info.get("wat", "")))

	# 3b. je graaft terwijl hij loopt: de schat schuift op en hij loopt mee naar de nieuwe plek
	var hol2 := Node2D.new()
	hol2.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	var w2 := Node2D.new()
	hol2.add_child(w2)
	var h2 := Node2D.new()
	h2.set_script(load("res://systemen/held.gd"))
	w2.add_child(h2)
	uitkomst = ""
	h2.klaar.connect(_klaar)
	h2.start(hol2, {"naam": "Ties", "bezoeken": 0, "wrok": "", "zaad": 4})
	var max_x := 0.0
	for i in 3000:
		if i == 60:
			hol2.schat_kol = 15
		if uitkomst != "":
			break
		max_x = maxf(max_x, h2.position.x)
		h2.stap(1.0 / 15.0)
	ok(absf(max_x - (15 * 16 + 8)) < 1.0 and uitkomst == "ontsnapt", "schat verschoven: hij loopt naar de nieuwe plek (x %.0f)" % max_x)
	hol2.free()

	# 4. schijterig draait om na de eerste klap; een verslagen bewoner is even plat en bestaat nog
	var gevlucht := 0
	var plat := 0
	var bestaat := 0
	var gevallen := 0
	var n := 400
	var vlucht_alle := 0
	for z in n:
		r = speel({"naam": "Wil", "bezoeken": 0, "wrok": "", "trek": "schijterig", "zaad": 1000 + z})
		if r.uitkomst == "ontsnapt" and not r.info.get("hoard_toucher", false):
			gevlucht += 1
			if r.slijm_plat or r.info.laatst_geraakt == "the Spike Pit":
				plat += 1
		if r.slijm_bestaat:
			bestaat += 1
	ok(gevlucht > 0 and plat == gevlucht, "schijterig vlucht na de eerste klap (%d keer)" % gevlucht)
	ok(bestaat == n, "slijm gaat nooit dood (%d van %d)" % [bestaat, n])

	# 5. verdeling met één slijm en één put: ongeveer 1 op 3 vlucht (balansdoel features.md).
	#    Kansen 45% en 35% komen uit sim/ (zie sim/UITKOMST.md); met de oude 30% en 22% vluchtte 59%.
	for z in n:
		var trekje := "schijterig" if z % 2 == 0 else "hebzuchtig"
		r = speel({"naam": "Rik%d" % z, "bezoeken": 0, "wrok": "", "trek": trekje, "zaad": 5000 + z})
		if r.uitkomst == "gevallen":
			gevallen += 1
		else:
			vlucht_alle += 1
	var deel := vlucht_alle / float(n)
	print("[held-toets] verdeling: %d gevallen, %d gevlucht (%.0f%%)" % [gevallen, vlucht_alle, deel * 100])
	ok(deel > 0.28 and deel < 0.48, "vluchten tussen 28%% en 48%% bij 1 slijm en 1 put (%.0f%%)" % (deel * 100))

	# 6. Hoard-Toucher komt brutaler terug: vaker vluchten
	var vlucht_ht := 0
	var vlucht_gewoon := 0
	for z in n:
		r = speel({"naam": "Gerda", "bezoeken": 1, "wrok": "", "trek": "hebzuchtig", "hoard_toucher": true, "zaad": 9000 + z})
		if r.uitkomst == "ontsnapt":
			vlucht_ht += 1
		r = speel({"naam": "Gerda", "bezoeken": 1, "wrok": "", "trek": "hebzuchtig", "zaad": 9000 + z})
		if r.uitkomst == "ontsnapt":
			vlucht_gewoon += 1
	ok(vlucht_ht > vlucht_gewoon, "Hoard-Toucher vlucht vaker (%d tegen %d)" % [vlucht_ht, vlucht_gewoon])

	# 7. slijm: staat bij de start NIET plat (Olaf 19:55), plat is een eigen frame, plat_s is in te stellen (demo)
	var hol3 := Node2D.new()
	hol3.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	var sl := Node2D.new()
	sl.set_script(load("res://systemen/slijm.gd"))
	hol3.add_child(sl)
	sl.zet(hol3, 6)
	ok(sl.kan_vechten() and not sl.is_plat(), "slijm staat bij de start klaar, niet plat")
	ok(sl.frame_nu()[0] == sl.RUST and sl.frame_nu()[1] == 0, "start: rustframe uit slijm.png")
	sl.plat_s = 9.0
	sl.plat()
	ok(sl.frame_nu()[1] == sl.PLAT and not sl.kan_vechten(), "plat: frame 11 uit slijm_leven.png, kan niet vechten")
	sl.stap(9.1)
	ok(sl.kan_vechten() and sl.frame_nu()[1] == sl.OPSTAAN, "na plat_s (9 s in de demo) staat hij op")
	sl.stap(0.5)
	ok(sl.frame_nu()[0] == sl.RUST and not sl.is_processing(), "daarna rust en zuinig (geen _process)")
	sl.raak()
	ok(sl.frame_nu()[1] == 6, "hap begint bij frame 6")
	sl.stap(0.85)
	ok(sl.frame_nu()[1] == 10, "hap eindigt bij frame 10")
	ok(sl.begin_leven() == "", "tijdens de hap geen leven-animatie")
	sl.stap(0.3)
	ok(sl.begin_leven() == "spugen" and sl.frame_nu()[1] == 2, "na een held gegeten: hij spuugt een laars uit (frame 2)")
	sl.stap(0.95)
	ok(sl.leven == "" and sl.laars_ligt() and absi(sl.laars_pos().x) == 16, "laars ligt naast hem op de vloer (x %d)" % sl.laars_pos().x)
	ok(sl.begin_leven() == "slapen" and sl.frame_nu()[1] in [0, 1], "laars al gespuugd: dan slaapt hij (frames 0 en 1)")
	sl.stap(4.1)
	ok(sl.leven == "" and not sl.is_processing(), "na het slapen weer rust en zuinig")
	var hd3 := Node2D.new()
	hd3.set_script(load("res://systemen/held.gd"))
	hol3.add_child(hd3)
	ok(sl.begin_leven() == "", "als er een held is: geen leven-animatie")
	hol3.free()

	# 8. held: vloer uit het hol, vast uiterlijk per naam, littekens per bezoek, teken boven het hoofd
	var hol4 := Node2D.new()
	hol4.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	hol4.vloer_y = 38.0
	var w4 := Node2D.new()
	hol4.add_child(w4)
	var h4 := Node2D.new()
	h4.set_script(load("res://systemen/held.gd"))
	w4.add_child(h4)
	h4.start(hol4, {"naam": "Kees", "bezoeken": 0, "wrok": "", "zaad": 7})
	for i in 60:
		h4.stap(1.0 / 15.0)
	ok(h4.staat == "lopen" and absf(h4.position.y - 38.0) < 0.01, "held staat op de vloer van het hol (y %.1f)" % h4.position.y)
	ok(h4.littekens.size() == 0, "eerste bezoek: geen litteken")
	ok(h4.teken_nu() == "", "geen wrok, ver van de schat: geen teken")
	var kleur_kees: int = h4.kleur_nr
	hol4.vallen[9] = "stekelput"
	var h5 := Node2D.new()
	h5.set_script(load("res://systemen/held.gd"))
	w4.add_child(h5)
	h5.start(hol4, {"naam": "Kees", "bezoeken": 2, "wrok": "the Spike Pit", "zaad": 8})
	h5.stap(0.1)
	ok(h5.kleur_nr == kleur_kees, "Kees heeft bij terugkomst dezelfde tuniek (rij %d)" % kleur_kees)
	ok(h5.littekens.size() == 2, "bezoek 3: twee littekens")
	h5.staat = "lopen"
	ok(h5.teken_nu() == "boos", "op weg naar zijn vijand: boos teken")
	var kleuren := {}
	var paar_fout := 0
	for z in 60:
		var hz := Node2D.new()
		hz.set_script(load("res://systemen/held.gd"))
		w4.add_child(hz)
		hz.start(hol4, {"naam": "Naam%d" % z, "bezoeken": 3, "wrok": "", "zaad": z})
		kleuren[hz.kleur_nr] = true
		if hz.littekens.size() != 3 or (hz.OOGLAP in hz.littekens and hz.SCHRAM in hz.littekens):
			paar_fout += 1
		hz.free()
	ok(paar_fout == 0, "aartsvijand: drie littekens, nooit ooglap en schram samen (%d fout)" % paar_fout)
	ok(kleuren.size() == 5, "alle vijf tuniekkleuren komen voor (%d)" % kleuren.size())
	hol4.free()

	# 9. wie Gloop overleeft is gebeten: volgende keer een hoed met een hap eruit
	var gebeten := false
	for z in 200:
		r = speel({"naam": "Bas", "bezoeken": 0, "wrok": "", "trek": "hebzuchtig", "zaad": 12000 + z}, false, true)
		if r.uitkomst == "ontsnapt" and r.info.get("laatst_geraakt", "") == "Gloop the Slime":
			gebeten = bool(r.info.get("gebeten", false))
			break
	ok(gebeten, "held die door Gloop geraakt werd en ontsnapte: info.gebeten")

	print("[held-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
