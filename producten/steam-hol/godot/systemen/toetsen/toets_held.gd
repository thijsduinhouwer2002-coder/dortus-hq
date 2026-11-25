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

# twee info-woordenboeken gelijk, los van de volgorde van de sleutels
func _zelfde(a: Dictionary, b: Dictionary) -> bool:
	if a.size() != b.size():
		return false
	for k in a.keys():
		if not b.has(k) or a[k] != b[k]:
			return false
	return true

func _klaar(_h, u: String, i: Dictionary) -> void:
	uitkomst = u
	uit_info = i

# Bouw een hol met slijm op kolom 6 en (optioneel) een put op kolom 9; laat één held lopen tot hij klaar is.
func speel(info: Dictionary, met_put := true, met_slijm := true, upg = null) -> Dictionary:
	var hol := Node2D.new()
	hol.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	hol.upgrades = upg
	if met_put:
		hol.vallen[9] = "stekelput"
	var wezens := Node2D.new()
	hol.add_child(wezens)
	var slijm = null
	if met_slijm:
		slijm = Node2D.new()
		slijm.set_script(load("res://systemen/slijm.gd"))
		slijm.met_3d = false   # deze toetsen gaan over de pixelbeelden; 3D apart onderaan
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
	var val_stappen := 0
	var x_val := [-1.0, -1.0]   # x bij het begin van de val en na 4 beelden (0,27 s)
	while uitkomst == "" and stappen < 20000:
		held.stap(1.0 / 15.0)
		stappen += 1
		if held.staat in ["vallen", "weg"]:
			val_stappen += 1
			if val_stappen == 1:
				x_val[0] = held.position.x
			if val_stappen == 4:
				x_val[1] = held.position.x
	var r := {"uitkomst": uitkomst, "info": uit_info, "eerste_doel": eerste_doel, "trek": trek, "tijd": stappen / 15.0,
		"slijm_plat": slijm != null and not slijm.kan_vechten(), "slijm_gegeten": slijm.gegeten if slijm != null else 0,
		"slijm_bestaat": slijm != null and is_instance_valid(slijm),
		"slijm_hoeden": slijm.hoeden.duplicate() if slijm != null else [],
		"val_teken": held.val_teken, "val_tijd": val_stappen / 15.0, "x_val": x_val}
	hol.free()
	return r

func _init() -> void:
	# 0. een held die in de put valt, schuift binnen de schrik naar het midden van de putkolom (moet Daan 15 nov 17:50)
	var rp := speel({"naam": "Kees", "bezoeken": 0, "wrok": "", "moet_vallen": true, "zaad": 1}, true, false)
	ok(rp.uitkomst == "gevallen" and is_equal_approx(float(rp.x_val[1]), 9 * 16 + 7.0), "val: na 0,27 s in de put, 1 spelpixel links van het midden (x %s, kolom 9 = 151)" % [rp.x_val])
	ok(is_equal_approx(float(rp.x_val[1]), round(float(rp.x_val[1]))), "val: hele spelpixels")
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
	sl.met_3d = false   # deze toetsen gaan over de pixelbeelden; 3D apart onderaan
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
	var laars_x: int = sl.laars_pos().x
	ok(sl.leven == "" and sl.laars_ligt() and absi(sl.laars_pos().x) == 15, "laars ligt naast hem op de vloer (x %d)" % sl.laars_pos().x)
	ok(sl.begin_leven() == "slapen" and sl.frame_nu()[1] in [0, 1], "laars al gespuugd: dan slaapt hij (frames 0 en 1)")
	sl.stap(4.1)
	ok(sl.leven == "" and not sl.is_processing(), "na het slapen weer rust en zuinig")
	ok(sl.laars_ligt() and sl.laars_pos().x == laars_x, "laars blijft op zijn plek liggen, ook na het slapen")
	sl.laars_weg()
	ok(not sl.laars_ligt(), "na de wekker is de laars weg")
	sl.zet_laars_proef()   # keurstrook laars_proef=1 (Bram 14 nov)
	ok(sl.laars_ligt() and sl.laars_pos() == Vector2i(15, 0) and sl.leven == "", "laars_proef: laars ligt vast rechts naast hem op de vloer")
	sl.laars_weg()
	sl.zet_spuug_proef(2)   # keurstrook spuug_proef=2 (Bram 15 nov)
	var lp: Vector2i = sl.laars_pos()
	sl.stap(5.0)
	ok(sl.leven == "spugen" and sl.frame_nu()[1] == sl.SPUGEN[3] and sl.laars_pos() == lp, "spuug_proef 2: na 5 s nog steeds hetzelfde spuugbeeld, laars op dezelfde plek")
	sl.zet_spuug_proef(1)
	sl.stap(1.0)
	ok(sl.frame_nu()[1] == sl.SPUGEN[0], "spuug_proef 1: blijft in kneep")
	sl.spuug_vast = -1.0
	sl.stap(1.0)
	ok(sl.leven == "" and sl.laars_ligt(), "na de proef gaat spugen gewoon af: laars ligt")
	sl.laars_weg()
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
	var hol6 := Node2D.new()
	hol6.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	var kees2 := Node2D.new()
	kees2.set_script(load("res://systemen/held.gd"))
	hol6.add_child(kees2)
	kees2.start(hol6, {"naam": "Kees II", "bezoeken": 0, "wrok": "Gloop the Slime", "zaad": 3})
	ok(not kees2.is_gebeten(), "Kees II met een wrok tegen Gloop is zelf niet gebeten (gewone hoed)")
	hol6.free()

	# 10. vaste uitkomsten voor de eerste tien minuten (Olaf 20:25 en 20:45, Sanne features.md)
	var vl := 0
	var dl := 0
	var og := 0
	for z in 30:
		r = speel({"naam": "Vlucht%d" % z, "bezoeken": 0, "wrok": "", "trek": "hebzuchtig", "moet_vluchten": true, "zaad": 300 + z})
		if r.uitkomst == "ontsnapt" and r.info.get("laatst_geraakt", "") == "Gloop the Slime" and r.slijm_plat:
			vl += 1
		r = speel({"naam": "Door%d" % z, "bezoeken": 0, "wrok": "", "trek": "schijterig", "moet_doorlopen": true, "zaad": 400 + z})
		if r.uitkomst == "ontsnapt" and bool(r.info.get("hoard_toucher", false)):
			dl += 1
		r = speel({"naam": "Hap%d" % z, "bezoeken": 0, "wrok": "", "moet_opgegeten": true, "zaad": 500 + z})
		if r.uitkomst == "gevallen" and r.info.get("laatst_geraakt", "") == "Gloop the Slime" and r.slijm_hoeden.size() == 1:
			og += 1
	ok(vl == 30, "moet_vluchten: één klap van Gloop en hij rent, met wrok (%d van 30)" % vl)
	ok(dl == 30, "moet_doorlopen: ook een schijterige komt langs alles en wordt Hoard-Toucher (%d van 30)" % dl)
	ok(og == 30, "moet_opgegeten: Gloop eet hem en draagt zijn hoed (%d van 30)" % og)
	r = speel({"naam": "Put", "bezoeken": 0, "wrok": "", "moet_opgegeten": true, "zaad": 7}, true, false)
	ok(r.uitkomst == "ontsnapt" and bool(r.info.get("hoard_toucher", false)), "moet_opgegeten zonder bewoner: overleeft de put, raakt de schat aan")

	# 11. hoedentoren: zijn hoed gaat op Gloop. Ook een aartsvijand, zolang de wand niet te zien is (Sanne 22:55;
	#     deze toets zei eerst "naar de wand", gewijzigd op haar besluit; met WAND_ER waar gaat hij weer naar de wand)
	r = speel({"naam": "Odo", "bezoeken": 0, "wrok": "", "moet_vallen": true, "zaad": 1})
	var odo_hoed := absi(hash("Odo")) % 10   # Mila 21:55: 10 hoedsoorten, held.gd rekent nu % HOED_SOORTEN
	ok(r.slijm_hoeden == [odo_hoed] and r.info.get("hoed_naar", "") == "bewoner" and int(r.info.get("hoeden_bewoner", 0)) == 1,
		"Odo's hoed (%d) staat op Gloop: %s" % [odo_hoed, str(r.slijm_hoeden)])
	r = speel({"naam": "Nemesis", "bezoeken": 3, "wrok": "Gloop the Slime", "moet_opgegeten": true, "zaad": 2})
	var nem_hoed := absi(hash("Nemesis")) % 10
	ok(r.uitkomst == "gevallen" and r.slijm_hoeden == [nem_hoed] and r.info.get("hoed_naar", "") == "bewoner"
		and int(r.info.get("hoeden_bewoner", 0)) == 1,
		"aartsvijand zonder wand: zijn hoed (%d) gaat op Gloop als trofee (%s)" % [nem_hoed, str(r.slijm_hoeden)])
	# Mila 23:00 en 23:10: helm met kam vanaf rij 0, kroon 2; held en slijm gebruiken dezelfde tabel
	var hs = load("res://systemen/held.gd").new()
	var ss = load("res://systemen/slijm.gd").new()
	ok(hs.HOED_TOP == [0, 0, 2, 3, 2, 0, 0, 0, 2, 0] and ss.HOED_TOP == hs.HOED_TOP, "HOED_TOP van Mila in held.gd en slijm.gd gelijk")
	hs.free()
	ss.free()
	# Olaf 22:35: info.snelheid voor de demo; dezelfde held met snelheid 1,4 is ruim eerder klaar, met dezelfde uitkomst
	var traag: Dictionary = speel({"naam": "Rap", "bezoeken": 0, "wrok": "", "moet_doorlopen": true, "zaad": 5})
	var rap: Dictionary = speel({"naam": "Rap", "bezoeken": 0, "wrok": "", "moet_doorlopen": true, "zaad": 5, "snelheid": 1.4})
	ok(traag.uitkomst == "ontsnapt" and rap.uitkomst == "ontsnapt" and bool(rap.info.get("hoard_toucher", false))
		and rap.tijd < traag.tijd * 0.8 and rap.tijd > traag.tijd * 0.6,
		"snelheid 1,4: Hoard-Toucher in %.1f s in plaats van %.1f s" % [rap.tijd, traag.tijd])

	# 12. toren en berg op de slijm zelf
	var hol5 := Node2D.new()
	hol5.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	var g = Node2D.new()
	g.set_script(load("res://systemen/slijm.gd"))
	g.met_3d = false   # deze toetsen gaan over de pixelbeelden; 3D apart onderaan
	hol5.add_child(g)
	g.zet(hol5, 6)
	ok(g.toren().is_empty() and g.berg().is_empty() and g.hover_regel() == "Gloop has no hats yet.", "zonder hoeden: geen toren, geen berg")
	var gt = Node2D.new()
	gt.set_script(load("res://systemen/slijm.gd"))
	gt._toren_uit_argument(PackedStringArray(["hoogte=120", "toren=0,4"]))
	ok(gt.hoeden.is_empty(), "strooktest: toren=... zonder vers=1 doet niets (geen hoeden in een echte save)")
	gt._toren_uit_argument(PackedStringArray(["hoogte=120", "vers=1", "toren=0,4,x,15,6"]))
	ok(gt.hoeden == [0, 4, 5, 6] and gt.gegeten == 4, "strooktest: toren=... met vers=1 geeft Gloop die hoeden (%s)" % str(gt.hoeden))
	gt.free()
	for i in 3:
		g.raak(i)
	g.stap(2.0)
	var tr: Array = g.toren()
	# onderste hoed met zijn onderste rij 1 px in de bovenkant van Gloop (rust: y 6 in zijn frame = -10)
	ok(tr.size() == 3 and int(tr[0][2]) + g.HOED_ONDER[0] == -10, "eerste hoed zakt 1 px in Gloop (y %d)" % int(tr[0][2]))
	ok(int(tr[1][2]) + g.HOED_ONDER[1] == int(tr[0][2]) + g.HOED_TOP[0], "tweede hoed 1 px in de eerste")
	ok(int(tr[0][1]) == 0 and int(tr[1][1]) == 1 and int(tr[2][1]) == -1, "scheef om en om (0, +1, -1)")
	for i in 7:
		g.raak(i % 4)
	ok(g.hoeden.size() == 10 and g.hoeden_op_hoofd().size() == 4 and g.hoeden_op_berg() == 6, "10 hoeden: 4 op zijn hoofd, 6 op de berg")
	ok(g.berg_maat() == 1 and g.berg().size() == 3, "maat 1 vanaf 5 hoeden: 3 zichtbaar op de berg (%d)" % g.berg().size())
	ok(g.hover_regel() == "Gloop wears 4 hats. 6 more in the pile.", "hover: " + g.hover_regel())
	var berg_rechts := -99
	for b in g.berg():
		berg_rechts = maxi(berg_rechts, int(b[1]))
	ok(berg_rechts <= -8, "de berg ligt links naast hem (x %d)" % berg_rechts)
	g.plat()
	g.stap(1.0)
	var op_vloer := true
	for h in g.toren():
		if int(h[2]) + g.HOED_ONDER[int(h[0])] != -1:
			op_vloer = false
	ok(g.toren().size() == 4 and op_vloer, "plat: de toren valt mee, de hoeden liggen op de vloer")
	g.stap(g.plat_s + 1.0)
	ok(int(g.toren()[0][2]) + g.HOED_ONDER[int(g.toren()[0][0])] < -5, "opgestaan: de toren staat weer op zijn hoofd")
	for i in 90:
		g.raak(i % 4)
	ok(g.hoeden.size() == 100 and g.berg_maat() == 3 and g.berg().size() == 10 and g.hoed_bijnaam() == "Milliner", "100 hoeden: maat 3, 10 zichtbaar, Milliner")
	# Sanne 9 nov 21:50: zesde maat bij 3000; maat 6 breder, niet hoger dan maat 5
	hol5.ingang_kol = 0   # linkergrens (Bram 17 nov): hier gaat het om de maten, dus ruimte genoeg links van Gloop
	g.stap(0.01)
	for i in 900:
		g.raak(i % 10)
	var hoogste5 := 0
	var links5 := 0
	for b in g.berg():
		hoogste5 = mini(hoogste5, int(b[2]))
		links5 = mini(links5, int(b[1]))
	ok(g.berg_maat() == 5 and g.berg().size() == 21, "1000 hoeden: maat 5, 21 zichtbaar (%d)" % g.berg().size())
	for i in 1999:
		g.raak(i % 10)
	ok(g.berg_maat() == 5, "2999 hoeden: nog maat 5")
	g.raak(9)
	var hoogste6 := 0
	var links6 := 0
	for b in g.berg():
		hoogste6 = mini(hoogste6, int(b[2]))
		links6 = mini(links6, int(b[1]))
	ok(g.berg_maat() == 6 and g.berg().size() == 33, "3000 hoeden: maat 6, 33 zichtbaar (%d)" % g.berg().size())
	ok(hoogste6 >= hoogste5 and links6 < links5, "maat 6 is breder (x %d < %d), niet hoger (y %d >= %d)" % [links6, links5, hoogste6, hoogste5])
	# Linkergrens (Daan 17 nov 08:40 punt 3 en 09:45 moet 4): de berg komt niet over de put of de ingang links van Gloop.
	var vrij_max: int = g.berg_max
	hol5.vallen[4] = "stekelput"
	g.stap(0.01)
	var grens_x: float = 5.0 * 16.0 + g.BERG_GRENS_LUCHT
	var links_g := 1e9
	for b in g.berg():   # pixelberg in deze toets; de 3D-berg ligt BERG_3D_LUCHT verder rechts dan berg(), dus nog binnen
		links_g = minf(links_g, g.position.x + (float(b[1]) - g.BERG_3D_LUCHT - g.BERG_HALF) * absf(g.scale.x))
	ok(g.berg().size() >= 1 and g.berg().size() < 33 and g.berg().size() == g.berg_max and links_g >= grens_x - 0.01,
		"linkergrens: put op kolom 4, berg %d plekjes, linkerkant %.1f >= %.1f" % [g.berg().size(), links_g, grens_x])
	var voor_g: Array = g.berg().duplicate(true)
	g.raak(3)
	var anders_g := 0
	for k in mini(voor_g.size(), g.berg().size()):
		if int(voor_g[k][3]) != int(g.berg()[k][3]):
			anders_g += 1
	ok(g.berg().size() == voor_g.size() and anders_g == 1, "linkergrens: een hoed erbij bedekt er een, de berg wordt niet breder (%d anders)" % anders_g)
	hol5.vallen.erase(4)
	hol5.vallen[5] = "stekelput"   # vlak naast Gloop (kolom 6): toch 1 plekje, de berg verdwijnt niet (controleur 10:40)
	g.stap(0.01)
	ok(g.berg().size() == 1, "linkergrens: put vlak naast Gloop, nog 1 plekje (%d)" % g.berg().size())
	hol5.vallen.erase(5)
	hol5.vallen[2] = "stekelput"
	g.scale = Vector2.ONE * 1.15
	g.stap(0.01)
	var grens_s: float = 3.0 * 16.0 + g.BERG_GRENS_LUCHT
	var links_s := 1e9
	for b in g.berg():
		links_s = minf(links_s, g.position.x + (float(b[1]) - g.BERG_3D_LUCHT - g.BERG_HALF) * 1.15)
	var n_s: int = g.berg().size()
	ok(links_s >= grens_s - 0.01 and n_s > 1 and n_s < 33, "linkergrens ook op figuur 1,15, put op 2 (%.1f >= %.1f, %d plekjes)" % [links_s, grens_s, n_s])
	g.scale = Vector2.ONE
	hol5.vallen.erase(2)
	g.stap(0.01)
	ok(g.berg_max == vrij_max and g.berg().size() == 33, "linkergrens: put weg, de berg mag weer breed (%d)" % g.berg().size())
	# Daan 17 nov 10:50: de grens geldt voor alles links, ook de beeldrand (hol-x 0) en de gaten in de aardwand.
	var oud_ik: int = hol5.ingang_kol
	var oud_px: float = g.position.x
	hol5.ingang_kol = 99   # ingang rechts: dan telt alleen de rand van het venster
	g.position.x = 60.0
	g.stap(0.01)
	var links_r := 1e9
	for b in g.berg():
		links_r = minf(links_r, g.position.x + (float(b[1]) - g.BERG_3D_LUCHT - g.BERG_HALF) * absf(g.scale.x))
	ok(g.berg().size() >= 1 and g.berg().size() < 33 and links_r >= g.BERG_GRENS_LUCHT - 0.01,
		"linkergrens: beeldrand, Gloop op x 60, %d plekjes, linkerkant %.1f >= 2" % [g.berg().size(), links_r])
	g.position.x = oud_px
	hol5.ingang_kol = oud_ik
	g.stap(0.01)
	var vrij_n: int = g.plekjes_binnen(-80.0)
	var hoog_gat := Rect2(-50.0, -22.0, 13.0, 11.0)   # gat in de wand linksboven, zoals op 120 (GEZIEN 17 nov)
	var n_gat: int = g.plekjes_binnen(-80.0, [hoog_gat])
	ok(n_gat >= 3 and n_gat < vrij_n, "linkergrens: gat in de wand houdt de berg kleiner (%d < %d)" % [n_gat, vrij_n])
	var n_laag: int = g.plekjes_binnen(-80.0, [Rect2(-60.0, -60.0, 10.0, 10.0)])   # gat ver boven de berg: telt niet
	ok(n_laag == vrij_n, "linkergrens: een gat boven de berg telt niet (%d)" % n_laag)
	var vak_ok := true
	for k in n_gat:
		var rp_g: Vector2i = g.plek_rij_pos(k)
		var x_g: float = -14.0 - 3.0 * rp_g.x - 6.0 * rp_g.y - g.BERG_3D_LUCHT
		var vak := Rect2(x_g - g.BERG_HALF, -3.0 * rp_g.x - g.berg_hoog(), g.BERG_HALF * 2.0, g.berg_hoog())
		if vak.grow(g.BERG_GRENS_LUCHT - 0.01).intersects(hoog_gat):
			vak_ok = false
	ok(vak_ok, "linkergrens: geen enkel plekje binnen 2 spelpx van het gat")
	var vol_ok := false
	for m in [1, 3, 6, 10, 15, 21, 27, 33]:
		if n_gat == m:
			vol_ok = true
	ok(vol_ok, "linkergrens: bij een gat hele schuine rijen (%d)" % n_gat)
	hol5.ingang_kol = 2
	g.stap(0.01)
	var alle_soorten := true
	for h in g.hoeden:
		if h < 0 or h >= 10:
			alle_soorten = false
	ok(alle_soorten and g.hoeden.has(9), "10 hoedsoorten (Mila): index 0 tot 9 blijft heel")
	var d: Dictionary = g.naar_dict()
	var g2 = Node2D.new()
	g2.set_script(load("res://systemen/slijm.gd"))
	g2.met_3d = false   # deze toetsen gaan over de pixelbeelden; 3D apart onderaan
	hol5.add_child(g2)
	g2.zet(hol5, 8)
	ok(g2.hoeden.is_empty(), "elke slijm zijn eigen toren")
	g2.van_dict(d)
	ok(g2.hoeden == g.hoeden and g2.gegeten == g.gegeten and g.gegeten >= 3000, "hoeden komen terug uit de save (%d)" % g2.hoeden.size())
	hol5.free()

	# Sanne toets 6 punt 1: moet_afgerekend. Wrok tegen de put: overleeft Gloop (kolom 6), valt in de put (kolom 9)
	var af := 0
	var af_bew := 0
	for z in 30:
		r = speel({"naam": "Bram", "bezoeken": 1, "wrok": "the Spike Pit", "moet_afgerekend": true, "zaad": 700 + z})
		if r.uitkomst == "gevallen" and r.info.laatst_geraakt == "the Spike Pit" and String(r.info.wat).begins_with("finally"):
			af += 1
		r = speel({"naam": "Wim", "bezoeken": 1, "wrok": "Gloop the Slime", "moet_afgerekend": true, "zaad": 800 + z})
		if r.uitkomst == "gevallen" and r.info.laatst_geraakt == "Gloop the Slime" and r.slijm_hoeden.size() == 1:
			af_bew += 1
	ok(af == 30, "moet_afgerekend: wrok tegen de put, valt precies in de put (%d van 30)" % af)
	ok(af_bew == 30, "moet_afgerekend: wrok tegen Gloop, Gloop eet hem en draagt zijn hoed (%d van 30)" % af_bew)
	r = speel({"naam": "Bram", "bezoeken": 1, "wrok": "the Spike Pit", "moet_afgerekend": true, "zaad": 9}, false, true)
	ok(r.uitkomst == "ontsnapt" and bool(r.info.get("hoard_toucher", false)), "moet_afgerekend zonder put: overleeft Gloop en raakt de schat aan")

	# upgrades (systemen/upgrades.gd): +7 procentpunt per stap, Deep Pit, Bouncy Gloop
	var U = load("res://systemen/upgrades.gd")
	var vol = U.new()
	vol.van_dict({"slijm": 3, "stekelput": 3})
	var zonder_upg := 0
	var met_upg := 0
	for z in 300:
		r = speel({"naam": "U%d" % z, "bezoeken": 0, "wrok": "", "trek": "hebzuchtig", "zaad": 1000 + z}, false, true)
		if r.uitkomst == "gevallen":
			zonder_upg += 1
		r = speel({"naam": "U%d" % z, "bezoeken": 0, "wrok": "", "trek": "hebzuchtig", "zaad": 1000 + z}, false, true, vol)
		if r.uitkomst == "gevallen":
			met_upg += 1
	# hebzuchtig, alleen Gloop: een keer gooien (daarna plat), dus ±45% zonder en ±66% met drie stappen
	ok(zonder_upg > 105 and zonder_upg < 165, "zonder upgrades valt ±45%% bij Gloop (%d van 300)" % zonder_upg)
	ok(met_upg > 170 and met_upg < 230 and met_upg > zonder_upg + 30, "met Royal Gloop valt ±66%% (%d van 300)" % met_upg)
	var diep = U.new()
	diep.van_dict({"stekelput": 2})
	var omgekeerd := 0
	for z in 100:
		r = speel({"naam": "S%d" % z, "bezoeken": 0, "wrok": "", "trek": "schijterig", "zaad": 2000 + z}, true, false, diep)
		if r.uitkomst == "ontsnapt" and not bool(r.info.get("hoard_toucher", false)):
			omgekeerd += 1
	var omgekeerd_zonder := 0
	for z in 100:
		r = speel({"naam": "S%d" % z, "bezoeken": 0, "wrok": "", "trek": "schijterig", "zaad": 2000 + z}, true, false)
		if r.uitkomst == "ontsnapt" and not bool(r.info.get("hoard_toucher", false)):
			omgekeerd_zonder += 1
	ok(omgekeerd_zonder > 10, "controle: zonder Deep Pit keert een schijterige held wel eens om (%d van 100)" % omgekeerd_zonder)
	ok(omgekeerd == 0, "Deep Pit: een schijterige held keert na de put niet om (%d keer wel)" % omgekeerd)
	var hol_b := Node2D.new()
	hol_b.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	var bouncy = U.new()
	bouncy.van_dict({"slijm": 2})
	hol_b.upgrades = bouncy
	var sl_b := Node2D.new()
	sl_b.set_script(load("res://systemen/slijm.gd"))
	sl_b.met_3d = false   # deze toetsen gaan over de pixelbeelden; 3D apart onderaan
	hol_b.add_child(sl_b)
	sl_b.zet(hol_b, 6)
	sl_b.plat()
	ok(absf(sl_b.plat_tot - sl_b.t - 20.0) < 0.01, "Bouncy Gloop: plat 20 s in plaats van 30 (%.1f)" % (sl_b.plat_tot - sl_b.t))
	hol_b.free()

	# Sanne toets 7 punt 2: je ziet hem wegzakken (niet één beeld half doorzichtig); Iris #25: hij valt meteen, ±0,7 s (was ±1 s)
	r = speel({"naam": "Bram", "bezoeken": 1, "wrok": "the Spike Pit", "moet_afgerekend": true, "zaad": 5})
	ok(r.val_tijd >= 0.65 and r.val_tijd <= 0.9, "de val duurt ±0,7 s tot klaar() (%.2f s)" % r.val_tijd)
	ok(r.val_teken == "boos", "terugkomer op weg naar zijn put had het boze wolkje toen hij viel (%s)" % r.val_teken)
	var hv := Node2D.new()
	hv.set_script(load("res://systemen/held.gd"))
	hv.val_teken = "boos"
	var b0: Dictionary = hv.val_beeld(0.05)
	var b0t: Dictionary = hv.val_beeld(0.2)
	var b1: Dictionary = hv.val_beeld(0.32)
	var b2: Dictionary = hv.val_beeld(0.48)
	var b3: Dictionary = hv.val_beeld(hv.VAL_WEG)
	ok(int(b0.hop) < 0 and int(b0.zak) == 0, "eerst schrik: hop omhoog, nog niet gezakt (hop %d)" % b0.hop)
	ok(int(b1.zak) > 0 and int(b1.zak) < int(b2.zak) and int(b2.zak) < 16, "dan zakt hij zichtbaar in stappen (%d, %d)" % [b1.zak, b2.zak])
	ok(int(b3.zak) == 16, "op VAL_WEG (0,6 s) helemaal onder de vloer (%d)" % b3.zak)
	ok(String(b0.teken) == "" and String(b0t.teken) == "poef" and String(b3.teken) == "", "boze wolkje: niet tijdens de witte flits (Daan #53 kan 1), dan poef, daarna geen teken")
	var hbeeld = load("res://systemen/held_beeld.gd")
	var fasen: Array = []
	for i in 8:
		var vbi: Dictionary = hv.val_beeld(hv.VAL_TEKEN_VAN + i * 0.05)
		if String(vbi.teken) == "poef":
			fasen.append(hbeeld.poef_beeld(float(vbi.poef_fase)))
	ok(fasen == [0, 0, 1, 1, 2, 2, 3, 3], "poef: Mila's 4 beelden op 10 fps, één keer (%s)" % str(fasen))
	ok(hbeeld.POEF.get_width() == 48 and hbeeld.POEF.get_height() == 10, "poef.png is 4 beelden van 12 x 10")
	hv.val_teken = ""
	ok(String(hv.val_beeld(0.2).teken) == "uitroep" and String(hv.val_beeld(0.1).teken) == "", "zonder wrok: uitroepteken bij de schrik, na de witte flits")
	ok(bool(hv.val_beeld(0.5).hoed), "in de put zakt de hoed mee")
	hv.info["hoed_naar"] = "bewoner"
	ok(not bool(hv.val_beeld(0.5).hoed), "opgegeten: de hoed staat al op de toren, dus niet ook nog op zijn hoofd")
	hv.free()

	# bewaren midden in het hol (Olaf kan-punt 00:40): herstel uit JSON loopt precies zo verder als het origineel
	var gelijk := 0
	var midden := 0
	for z in 20:
		var ha := Node2D.new()
		ha.set_script(load("res://systemen/toetsen/nep_hol.gd"))
		ha.vallen[5] = "stekelput"
		ha.vallen[9] = "stekelput"
		var hb := Node2D.new()
		hb.set_script(load("res://systemen/toetsen/nep_hol.gd"))
		hb.vallen[5] = "stekelput"
		hb.vallen[9] = "stekelput"
		var hel_a := Node2D.new()
		hel_a.set_script(load("res://systemen/held.gd"))
		ha.add_child(hel_a)
		# om de beurt met een wrok tegen de put (loopt eerst naar kolom 5 of 9, boos teken)
		var wr: String = "the Spike Pit" if z % 2 == 1 else ""
		hel_a.start(ha, {"naam": "Sla%d" % z, "bezoeken": z % 3, "wrok": wr, "zaad": 3000 + z, "kleur": Color(0.2, 0.4, 0.6)})
		for stp in 30 + z * 7:
			if hel_a.staat != "weg":
				hel_a.stap(1.0 / 15.0)
		if hel_a.staat in ["lopen", "vluchten", "vallen"]:
			midden += 1
		var tekst := JSON.stringify(hel_a.naar_dict())
		var hel_b := Node2D.new()
		hel_b.set_script(load("res://systemen/held.gd"))
		hb.add_child(hel_b)
		hel_b.herstel(hb, JSON.parse_string(tekst))
		var na := 0
		var zelfde_pad := true
		while hel_a.staat != "weg" and na < 5000:
			hel_a.stap(1.0 / 15.0)
			hel_b.stap(1.0 / 15.0)
			na += 1
			if hel_a.staat != hel_b.staat or hel_a.position.distance_to(hel_b.position) > 0.001:
				zelfde_pad = false
		var ia: Dictionary = hel_a.info.duplicate()
		var ib: Dictionary = hel_b.info.duplicate()
		for kk in ["kleur", "hoed", "zaad"]:
			ia.erase(kk)
			ib.erase(kk)
		if not zelfde_pad or hel_b.staat != "weg":
			print("[held-toets] herstel anders bij z=%d: %s/%s x %.2f/%.2f na %d" % [z, hel_a.staat, hel_b.staat, hel_a.position.x, hel_b.position.x, na])
		if zelfde_pad and hel_b.staat == "weg" and hel_a.klappen == hel_b.klappen and _zelfde(ia, ib) and String(hel_a.info.get("wat", "")) == String(hel_b.info.get("wat", "")) and hel_b.info.get("kleur") is Color:
			gelijk += 1
		ha.free()
		hb.free()
	ok(midden >= 8, "de meeste werden echt onderweg bewaard (%d van 20)" % midden)
	ok(gelijk == 20, "held bewaard midden in het hol loopt na herstel precies zo verder (%d van 20)" % gelijk)

	# heldensoorten (Bram 10 nov, versie 1, systemen/heldensoort.gd)
	var HS = load("res://systemen/heldensoort.gd")
	var tel := {}
	for soort in ["", "ridder", "dief", "magier", "bard"]:
		tel[soort] = {"put": 0, "slijm": 0, "vlucht": 0, "lied": 0, "tijd": 0.0}
		for z in 120:
			var rs := speel({"naam": "Toets%d" % z, "zaad": 7000 + z, "trek": "schijterig" if z % 2 == 0 else "hebzuchtig", "soort_held": soort})
			var lg := String(rs.info.get("laatst_geraakt", ""))
			if rs.uitkomst == "gevallen":
				tel[soort]["put" if lg == "the Spike Pit" else "slijm"] += 1
			else:
				tel[soort]["vlucht"] += 1
			if int(rs.info.get("lied", 0)) > 0:
				tel[soort]["lied"] += 1
			tel[soort]["tijd"] += rs.tijd / 120.0
	print("[held-toets] soorten (120 elk, put/slijm/vlucht/lied/tijd): ", tel)
	ok(tel["magier"]["put"] < tel[""]["put"] / 2, "magiër valt veel minder in de put (%d tegen %d)" % [tel["magier"]["put"], tel[""]["put"]])
	ok(tel["dief"]["put"] < tel[""]["put"], "dief springt vaker over de put (%d tegen %d)" % [tel["dief"]["put"], tel[""]["put"]])
	ok(tel["ridder"]["tijd"] > tel[""]["tijd"] and tel["dief"]["tijd"] < tel[""]["tijd"], "ridder trager, dief sneller (%.1f / %.1f / %.1f s)" % [tel["ridder"]["tijd"], tel[""]["tijd"], tel["dief"]["tijd"]])
	ok(tel["ridder"]["put"] > tel[""]["put"], "ridder is taai: komt na een klap van Gloop vaker tot de put (%d tegen %d)" % [tel["ridder"]["put"], tel[""]["put"]])
	for sh in tel:
		var vls: float = float(tel[sh]["vlucht"]) / 120.0
		ok(vls > 0.2 and vls < 0.5, "soort '%s' vlucht %.0f%% (doel ±1 op 3, per soort tussen 20 en 50%%)" % [sh, vls * 100.0])
	ok(tel["bard"]["lied"] == tel["bard"]["vlucht"] and tel["bard"]["lied"] > 0 and tel[""]["lied"] == 0 and tel["ridder"]["lied"] == 0, "alleen een bard die ontsnapt zingt (%d van %d)" % [tel["bard"]["lied"], tel["bard"]["vlucht"]])
	var rz := speel({"naam": "Zonder", "zaad": 42})
	var rz2 := speel({"naam": "Zonder", "zaad": 42, "soort_held": "draak"})
	ok(rz.uitkomst == rz2.uitkomst and is_equal_approx(rz.tijd, rz2.tijd), "onbekende soort = gewone held, dus de demo blijft gelijk")
	var kr := RandomNumberGenerator.new()
	kr.seed = 3
	var gekozen := {}
	var eerste_tien_gewoon := true
	for nr in range(1, 1001):
		var ks: String = HS.kies(nr, kr)
		if nr <= 10 and ks != "":
			eerste_tien_gewoon = false
		gekozen[ks] = int(gekozen.get(ks, 0)) + 1
	ok(eerste_tien_gewoon, "de eerste 10 helden van een nieuw spel zijn gewoon (eerste tien minuten blijven gelijk)")
	ok(gekozen.size() == 5 and int(gekozen[""]) > 450 and int(gekozen.get("bard", 0)) < int(gekozen.get("dief", 0)), "daarna meestal gewoon, een bard is zeldzaam %s" % str(gekozen))
	var hd := Node2D.new()
	hd.set_script(load("res://systemen/held.gd"))
	var hol_d := Node2D.new()
	hol_d.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	hol_d.add_child(Node2D.new())
	hol_d.get_child(0).add_child(hd)
	hd.start(hol_d, {"naam": "Sir Bewaar", "soort_held": "ridder"})
	var dsoort: Dictionary = JSON.parse_string(JSON.stringify(hd.naar_dict()))
	var hd2 := Node2D.new()
	hd2.set_script(load("res://systemen/held.gd"))
	hol_d.get_child(0).add_child(hd2)
	hd2.herstel(hol_d, dsoort)
	ok(hd2.soort_held == "ridder", "soort blijft na bewaren en laden")
	# karaktertrekken erbij (Bram 10 nov, versie 1): slaapkop, wraakzuchtig, opschepper
	var x_tsk := 0.0
	var x_tgw := 0.0
	var x_dutjes := 0
	for z in 40:
		var x_rk := speel({"naam": "Slaap%d" % z, "zaad": 9100 + z, "trek": "slaapkop"}, false, false)
		var x_rg := speel({"naam": "Slaap%d" % z, "zaad": 9100 + z, "trek": "hebzuchtig"}, false, false)
		x_tsk += x_rk.tijd / 40.0
		x_tgw += x_rg.tijd / 40.0
		if bool(x_rk.info.get("dutje", false)):
			x_dutjes += 1
	ok(x_dutjes == 40 and x_tsk > x_tgw + 3.0, "slaapkop doet een dutje in een leeg hol (%d van 40, %.1f s tegen %.1f s)" % [x_dutjes, x_tsk, x_tgw])
	var hslaap := Node2D.new()
	hslaap.set_script(load("res://systemen/held.gd"))
	var x_hol_s := Node2D.new()
	x_hol_s.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	x_hol_s.add_child(Node2D.new())
	x_hol_s.get_child(0).add_child(hslaap)
	hslaap.start(x_hol_s, {"naam": "Dut", "zaad": 5, "trek": "slaapkop"})
	var x_stappen_s := 0
	while hslaap.staat != "dutten" and x_stappen_s < 3000:
		hslaap.stap(1.0 / 15.0)
		x_stappen_s += 1
	ok(hslaap.staat == "dutten" and hslaap.teken_nu() == "zzz", "tijdens het dutje zzz boven zijn hoofd")
	var dslaap: Dictionary = JSON.parse_string(JSON.stringify(hslaap.naar_dict()))
	var hslaap2 := Node2D.new()
	hslaap2.set_script(load("res://systemen/held.gd"))
	x_hol_s.get_child(0).add_child(hslaap2)
	hslaap2.herstel(x_hol_s, dslaap)
	ok(hslaap2.staat == "dutten" and is_equal_approx(hslaap2.dut_tot, hslaap.dut_tot) and hslaap2.dut_kol == -1, "midden in een dutje bewaard en terug: slaapt verder, geen tweede dutje")
	var x_af_w := 0
	var x_af_g := 0
	for z in 150:
		var x_rw := speel({"naam": "Wraak%d" % z, "zaad": 9500 + z, "trek": "wraakzuchtig", "wrok": "the Spike Pit", "bezoeken": 1})
		var x_rn := speel({"naam": "Wraak%d" % z, "zaad": 9500 + z, "trek": "hebzuchtig", "wrok": "the Spike Pit", "bezoeken": 1})
		if String(x_rw.info.get("wat", "")).begins_with("finally"):
			x_af_w += 1
		if String(x_rn.info.get("wat", "")).begins_with("finally"):
			x_af_g += 1
	ok(x_af_w > x_af_g, "wraakzuchtig valt vaker in zijn eigen vijand (%d tegen %d van 150)" % [x_af_w, x_af_g])
	var x_tr := RandomNumberGenerator.new()
	x_tr.seed = 11
	var x_tk_tel := {}
	var x_tk_eerst := true
	for nr in range(1, 1001):
		var x_tk: String = HS.kies_trek(nr, x_tr)
		if nr <= 10 and x_tk != "":
			x_tk_eerst = false
		x_tk_tel[x_tk] = int(x_tk_tel.get(x_tk, 0)) + 1
	ok(x_tk_eerst and x_tk_tel.size() == 4 and int(x_tk_tel[""]) > 700, "nieuwe trekken pas na held 10, dan ±1 op 5 %s" % str(x_tk_tel))
	# Gloop per upgrade-stap (Mila 10 nov 02:55) en het koop-moment (Sanne toets 8 punt 1)
	var hol_u := Node2D.new()
	hol_u.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	var upg_u = U.new()
	hol_u.upgrades = upg_u
	var sl_u := Node2D.new()
	sl_u.set_script(load("res://systemen/slijm.gd"))
	sl_u.met_3d = false   # deze toetsen gaan over de pixelbeelden; 3D apart onderaan
	hol_u.add_child(sl_u)
	sl_u.zet(hol_u, 6)
	for hh in [4, 1]:
		sl_u.krijg_hoed(hh)
	var top_klein: int = sl_u.top_nu()
	var toren_klein: Array = sl_u.toren()
	ok(sl_u.frame_nu()[0] == sl_u.RUST and sl_u.niveau() == 0, "zonder upgrade: het gewone blad")
	upg_u.koop("slijm", 1000)
	sl_u.vier_koop()
	ok(sl_u.frame_nu()[0] == sl_u.RUST and sl_u.wip_nu() == -2, "koop-moment beeld 0: nog klein, 2 omhoog")
	sl_u.stap(0.25)
	ok(sl_u.frame_nu()[0] == sl_u.RUST_GROOT and sl_u.wip_nu() == -3, "beeld 1: groot lijf, 3 omhoog (zwelt)")
	sl_u.stap(0.2)
	ok(sl_u.wip_nu() == -1 and sl_u.is_processing(), "beeld 2: 1 omhoog, nog bezig")
	sl_u.stap(0.3)
	ok(sl_u.wip_nu() == 0 and not sl_u.is_processing(), "na 0,6 s: weer op de vloer en zuinig")
	ok(sl_u.top_nu() == top_klein - 2, "Big Gloop: kruin 2 hoger (%d tegen %d)" % [sl_u.top_nu(), top_klein])
	var toren_groot: Array = sl_u.toren()
	ok(int(toren_groot[0][2]) == int(toren_klein[0][2]) - 2 and int(toren_groot[1][2]) == int(toren_klein[1][2]) - 2, "de hoedentoren schuift 2 mee, zakt niet in zijn kruin")
	ok(sl_u.hoogste_punt() == int(toren_groot[1][2]) + sl_u.HOED_TOP[1], "hoogste punt = bovenkant van de bovenste hoed (%d)" % sl_u.hoogste_punt())
	sl_u.plat()
	ok(sl_u.frame_nu()[0] == sl_u.LEVEN_GROOT and sl_u.frame_nu()[1] == sl_u.PLAT, "Big Gloop plat: plat-frame uit het grote blad")
	upg_u.verkoop("slijm")
	sl_u.upgrade_veranderd()
	ok(sl_u.frame_nu()[0] == sl_u.LEVEN and sl_u.niveau() == 0, "Undo: weer het gewone blad")
	# Mila 04:55: grote bladen zijn 20 breed, de berg schuift 2 naar links bij Big Gloop
	ok(sl_u.RUST_GROOT.get_width() == 6 * 20 and sl_u.LEVEN_GROOT.get_width() == 13 * 20 and sl_u.UPG.get_width() == 68, "grote bladen 20 x 16 per frame, upgrades-blad 68 breed")
	for hh in range(8):
		sl_u.krijg_hoed(hh % 10)
	sl_u.plat_tot = -100.0
	var berg_klein: Array = sl_u.berg()
	upg_u.koop("slijm", 1000)
	sl_u.upgrade_veranderd()
	var berg_groot: Array = sl_u.berg()
	ok(berg_klein.size() > 0 and int(berg_groot[0][1]) == int(berg_klein[0][1]) - 2, "berg 2 pixels naar links bij Big Gloop (%d tegen %d)" % [int(berg_groot[0][1]), int(berg_klein[0][1])])
	# Controleur 04:22: Undo binnen 0,6 s stopt het koop-moment meteen
	upg_u.koop("slijm", 1000)
	sl_u.vier_koop()
	sl_u.stap(0.25)
	ok(sl_u.wip_nu() != 0, "koop-moment loopt")
	upg_u.verkoop("slijm")
	sl_u.upgrade_veranderd()
	ok(sl_u.wip_nu() == 0 and sl_u.niveau() == 1, "Undo midden in het koop-moment: meteen weer op de vloer")
	# Royal in 3D (Bram 14 nov): zonder blad "royal" de pixel-cape; met blad een eigen, bredere cel onder zijn midden
	sl_u._laad_royal()
	ok(not sl_u.royal_3d_aan("") , "Royal 3D: zonder 3D-lijf nooit aan (dan de pixel-cape)")
	if sl_u.royal3d == null:
		ok(not sl_u.royal_3d_aan("rust") and sl_u.royal_rect("achter", 0).size.x == 0.0, "Royal 3D: nog geen blad royal, dan de pixel-cape en -zoom")
	var ri_oud: Dictionary = sl_u.royal3d_info
	sl_u.royal3d_info = {"frames": ["achter", "voor"], "cel_px": [160, 64], "px": 4, "anker_x": 80}
	ok(sl_u.is_groot() and sl_u.royal_rect("achter", 0) == Rect2(-20, -16, 40, 16), "Royal 3D: cel 40 spelpixels breed, midden onder hem, onderkant op de vloer (%s)" % str(sl_u.royal_rect("achter", 0)))
	ok(sl_u.royal_rect("voor", -2) == Rect2(-20, -18, 40, 16) and sl_u.royal_rect("kroon", 0).size.x == 0.0, "Royal 3D: wipt mee, onbekend frame tekent niets")
	var rt_oud: CanvasTexture = sl_u.royal3d
	if sl_u.royal3d == null:
		sl_u.royal3d = CanvasTexture.new()
	var gekocht := 0
	while sl_u.niveau() < 3 and gekocht < 5:
		upg_u.koop("slijm", 100000)
		sl_u.upgrade_veranderd()
		gekocht += 1
	sl_u.plat_tot = -100.0
	ok(sl_u.niveau() >= 3 and not sl_u.ster_aan("rust") and sl_u.ster_aan(""), "Royal 3D: geen pixelster, zonder 3D-lijf wel (Daan 10:45 moet 2, niveau %d)" % sl_u.niveau())
	for i in gekocht:
		upg_u.verkoop("slijm")
	sl_u.upgrade_veranderd()
	sl_u.royal3d = rt_oud
	sl_u.royal3d_info = ri_oud
	hol_u.free()

	# Trick Lid: de magier ziet de put niet meer (idee Sanne 10 nov 03:10)
	ok(is_equal_approx(HS.kans_factor("magier", "stekelput"), 0.3) and is_equal_approx(HS.kans_factor("magier", "stekelput", true), 1.0), "Trick Lid: magier van 0,3 naar 1,0 voor de put")
	ok(is_equal_approx(HS.kans_factor("dief", "stekelput", true), 0.5) and is_equal_approx(HS.kans_factor("magier", "slijm", true), 1.25), "Trick Lid verandert niets voor de dief of voor Gloop")

	# Muzieknootjes (Sanne toets 10 punt 1)
	var HB = load("res://systemen/held_beeld.gd")
	ok(HB.nootjes("bard", false, "lopen", 0.5).size() == 1 and HB.nootjes("bard", false, "lopen", 2.5).size() == 2 and HB.nootjes("bard", false, "vluchten", 9.0).size() == 2, "bard: elke 2 s een nootje, 2 tegelijk, ook vluchtend")
	var nt0: Array = HB.nootjes("bard", false, "lopen", 0.1)[0]
	var nt1: Array = HB.nootjes("bard", false, "lopen", 1.9)[0]
	ok(int(nt1[1]) < int(nt0[1]) and float(nt1[2]) < float(nt0[2]), "nootje stijgt op en vervaagt")
	ok(HB.noot_alfa(1.0) == 0.0 and HB.noot_alfa(0.95) < 0.1 and HB.noot_alfa(0.0) == 1.0 and HB.noot_alfa(0.5) > 0.7, "nootje is weg voor het eind van zijn weg (Daan 03:50)")
	ok(HB.nootjes("bard", false, "vallen", 1.0).is_empty() and HB.nootjes("", false, "lopen", 1.0).is_empty() and HB.nootjes("ridder", false, "lopen", 1.0).is_empty(), "geen nootjes bij vallen of bij andere helden")
	ok(HB.nootjes("", true, "afdalen", 1.0).size() == 1 and HB.nootjes("", true, "lopen", 2.5).is_empty(), "held door het lied: de eerste 2 s één nootje")
	# 3D-lijf uit de pijplijn (Bram 13 nov, producten/steam-hol/pijplijn/)
	var hol_3 := Node2D.new()
	hol_3.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	hol_3.upgrades = U.new()
	var g3 := Node2D.new()
	g3.set_script(load("res://systemen/slijm.gd"))
	hol_3.add_child(g3)
	g3.zet(hol_3, 6)
	if FileAccess.file_exists("res://kunst/3d/sprites.json"):
		ok(g3.beeld_3d() == "rust" and g3.lijf3d != null and g3.lijf3d.texture_filter == CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS, "3D: rust uit kunst/3d/gloop.png, filter lineair")
		var tex: Texture2D = g3.lijf3d.diffuse_texture
		ok(tex.get_width() == int(g3.lijf3d_info["cel_px"][0]) * g3.lijf3d_info["frames"].size() and tex.get_height() == int(g3.lijf3d_info["cel_px"][1]), "3D: blad heeft de maat uit sprites.json (%dx%d)" % [tex.get_width(), tex.get_height()])
		var t3: int = g3.top_nu()
		ok(t3 >= 2 and t3 <= 12, "3D: kruin op een redelijke hoogte (%d)" % t3)
		g3.krijg_hoed(4)
		ok(int(g3.toren()[0][2]) + g3.HOED_ONDER[4] == -16 + t3, "3D: de eerste hoed staat op zijn kruin")
		var t3d: Array = g3.toren_3d()
		var hb_t = load("res://systemen/held_beeld.gd")
		hb_t._laad_3d()
		if hb_t.held3d.has("hoeden"):
			ok(t3d.size() == 1 and is_equal_approx(float(t3d[0][2]), float(-16 + t3)), "3D-toren: nulpunt van de eerste 3D-hoed op zijn kruin (%s)" % str(t3d))
			g3.krijg_hoed(7)
			var t3e: Array = g3.toren_3d()
			ok(t3e.size() == 2 and is_equal_approx(float(t3e[1][2]), float(t3e[0][3]) + 1.0), "3D-toren: tweede hoed 1 spelpixel in de bovenkant van de eerste, nooit zwevend")
			ok(g3.hoogste_punt() == int(floor(float(t3e[1][3]) + 0.001)), "3D-toren: hoogste punt is de bovenkant van de bovenste hoed")
			# plafond (Daan 14 nov 00:40): veel hoeden, dan blijft de bovenkant 2 spelpixels onder de bovenrand, alles schuift pl_gelijk in elkaar
			var voor_pl: Array = g3.hoeden.duplicate()
			for hh in [0, 5, 1, 6, 2, 3, 8, 9]:
				g3.krijg_hoed(hh)
			var pos_pl: Vector2 = g3.position
			g3.position.y = 20.0   # zo laag dat de toren van 4 hoeden tegen het plafond komt (in het hol pas met de gang hoger)
			var tp: Array = g3.toren_3d()
			var rand_min := 99.0   # kleinste rand van een hoed boven de vorige
			for k in range(1, tp.size()):
				rand_min = minf(rand_min, float(tp[k - 1][3]) - float(tp[k][3]))
			ok(rand_min >= 1.0 - 0.01, "3D-toren plafond: van elke hoed blijft minstens 1 spelpixel rand (%.2f)" % rand_min)
			ok(float(tp[-1][3]) >= g3.plafond_y() - 0.01 or absf(rand_min - 1.0) < 0.01, "3D-toren plafond: bovenkant %.2f niet boven %.2f (%d hoeden)" % [float(tp[-1][3]), g3.plafond_y(), tp.size()])
			var pl_gelijk := true
			var ov0 := float(tp[1][2]) - float(tp[0][3])
			for k in range(1, tp.size()):
				pl_gelijk = pl_gelijk and absf((float(tp[k][2]) - float(tp[k - 1][3])) - ov0) < 0.01
			ok(pl_gelijk and ov0 > 1.0, "3D-toren plafond: elke hoed zakt evenveel extra in de vorige (%.2f)" % ov0)
			ok(absf(float(tp[-1][3]) - g3.plafond_y()) < 0.01 or ov0 >= 1.0 + g3.TOREN_MAX_EXTRA - 0.01 or absf(rand_min - 1.0) < 0.01, "3D-toren plafond: precies tegen het plafond, of de grootste overlap")
			var tpx: Array = g3.toren()
			var rand_px := 99
			for k in range(1, tpx.size()):
				rand_px = mini(rand_px, (int(tpx[k - 1][2]) + g3.HOED_TOP[int(tpx[k - 1][0])]) - (int(tpx[k][2]) + g3.HOED_TOP[int(tpx[k][0])]))
			ok(rand_px >= 1, "pixeltoren plafond: van elke hoed blijft een rand (%d)" % rand_px)
			ok(int(tpx[-1][2]) + g3.HOED_TOP[int(tpx[-1][0])] >= int(floor(g3.plafond_y())) or rand_px == 1, "pixeltoren plafond: bovenkant niet boven de rand")
			# hoogste_punt_rust (Olaf 14 nov 01:50): rust-frame, geen wip, met plafond; zzz minstens 1 spelpixel onder de rand
			ok(g3.hoogste_punt_rust() >= int(floor(g3.plafond_y())) or absf(rand_min - 1.0) < 0.01, "rustpunt volgt het plafond (%d, plafond %.1f)" % [g3.hoogste_punt_rust(), g3.plafond_y()])
			var rp0: int = g3.hoogste_punt_rust()
			var kv: float = g3.koop_van
			g3.koop_van = g3.t - 0.05
			ok(g3.hoogste_punt_rust() == rp0, "rustpunt wipt niet mee met het koop-moment")
			g3.koop_van = kv
			ok(g3._rust_som == false, "rustpunt zet de schakelaar terug")
			ok(is_equal_approx(g3.teken_rand_y(), 1.0 - g3.position.y), "teken-rand 1 spelpixel onder de bovenrand")
			g3.position = pos_pl
			g3.hoeden = voor_pl
			ok(is_equal_approx(float(g3.toren_3d()[1][2]), float(g3.toren_3d()[0][3]) + 1.0), "3D-toren: met twee hoeden geen extra overlap")
			# hoedenberg in 3D (Bram 14 nov): zelfde plekken als berg(), nulpunt op de onderrand van de pixelhoed
			var voor_b: Array = g3.hoeden.duplicate()
			for hh in [0, 5, 1, 6, 2, 3, 8, 9, 4, 7]:
				g3.krijg_hoed(hh)
			var bp: Array = g3.berg()
			var b3d: Array = g3.berg_3d()
			var b_ok := b3d.size() == bp.size() and bp.size() >= 3
			for k in mini(bp.size(), b3d.size()):
				b_ok = b_ok and int(b3d[k][0]) == int(bp[k][0]) and is_equal_approx(float(b3d[k][1]), float(bp[k][1]) - g3.BERG_3D_LUCHT)
				b_ok = b_ok and is_equal_approx(float(b3d[k][2]), float(int(bp[k][2]) + 1 + g3.HOED_ONDER[int(bp[k][0])]))
			ok(b_ok, "3D-berg: zelfde hoeden en plekken als de pixelberg, 1 spelpixel verder van Gloop (%d)" % b3d.size())
			ok(b3d.size() > 0 and is_equal_approx(float(b3d[0][2]), 0.0), "3D-berg: onderste rij staat op de vloer")
			# Waar nachthoeden landen (Sanne 17 nov 07:00): oude toren tot de landing, dan springt de onderste in 0,3 s naar
			# een vast plekje op de berg, en daar ligt hij daarna
			var voor_n3: Array = g3.hoeden.duplicate()
			g3.hoeden.assign([0, 1, 2, 3, 4, 5, 6, 7])
			var oude_onder: int = g3.hoeden[4]
			g3.krijg_hoed_later(9)
			g3.start_nacht(0.0)
			g3.stap(0.01)
			ok(g3.nacht_valt() and g3.hoeden.size() == 9 and g3.berg_tel() == 8, "nachtland: tijdens de val telt de berg nog de oude 8 (%d)" % g3.berg_tel())
			ok(g3.toren_3d(g3.hoeden.slice(4, 8), true).size() == 4 and g3.hoeden_op_hoofd().size() == 4, "nachtland: oude toren 4, geen vijfde plek")
			ok(not g3.berg_boog()[0], "nachtland: nog geen boog voor de landing")
			g3.stap(g3.VAL_S + g3.SPRING_S * 0.5 - 0.01)
			var bb3: Array = g3.berg_boog()
			var top3: Array = []
			for e3 in g3.berg_3d(9):
				if int(e3[3]) == 4:
					top3 = e3   # het plekje van de nieuwste (index 4 in hoeden bij 9 hoeden)
			ok(not top3.is_empty(), "nachtland: de nieuwste (index 4) ligt op een plekje van de berg bij 9")
			if top3.is_empty():
				top3 = [0, 0.0, 0.0, 4]   # controleur 09:30: geen SCRIPT ERROR die de toetsrun laat hangen, maar een FOUT
			var voet3: Array = g3.toren_3d()[0]
			ok(not g3.nacht_valt() and bb3[0] and int(bb3[1]) == oude_onder and g3.berg_tel() == 8, "nachtland: na de landing vliegt de oude onderste (%s) in een boog, berg wacht (%s)" % [str(bb3), str(g3.berg_tel())])
			ok(float(bb3[2]) < float(voet3[1]) and float(bb3[2]) > float(top3[1]) and float(bb3[3]) < minf(float(voet3[2]), float(top3[2])), "nachtland: halverwege tussen toren en berg en hoger dan beide (%s, %s, %s)" % [str(bb3), str(voet3), str(top3)])
			g3.stap(g3.SPRING_S * 0.48)
			var bb_eind: Array = g3.berg_boog()
			ok(bb_eind[0] and absf(float(bb_eind[2]) - float(top3[1])) <= 2.0 and absf(float(bb_eind[3]) - float(top3[2])) <= 2.0, "nachtland: aan het eind van de boog is hij bij zijn plekje (%s tegen %s)" % [str(bb_eind), str(top3)])
			g3.stap(g3.SPRING_S * 0.02 + 0.02)
			var gel := false
			for e3 in g3.berg_3d():
				gel = gel or (int(e3[3]) == 4 and int(e3[0]) == oude_onder and is_equal_approx(float(e3[1]), float(top3[1])) and is_equal_approx(float(e3[2]), float(top3[2])))
			ok(not g3.berg_boog()[0] and g3.berg_tel() == 9 and gel, "nachtland: na 0,3 s ligt hij op het plekje waar de boog heen ging")
			ok(g3.hoeden_op_hoofd() == [5, 6, 7, 9], "nachtland: op de toren de laatste 4 (%s)" % str(g3.hoeden_op_hoofd()))
			# plof (Sanne 08:50): 19 hoeden in één nacht, één boog naar het plekje van de laatste hoed van de berg
			g3.hoeden.assign([0, 1, 2, 3, 4, 5, 6, 7])
			for pi in 19:
				g3.krijg_hoed_later((pi * 3) % 10)
			g3.start_nacht(0.0)
			g3.stap(0.01)
			var plof_eind: float = float(g3.nacht_ev[-1][0]) + g3.SPRING_S + 0.1 if not g3.nacht_ev.is_empty() else 0.0
			var bb_plof: Array = [false]
			var stappen := 0
			while (g3.t < plof_eind or g3.nacht_bezig() or g3.berg_tel() < g3.hoeden.size()) and stappen < 5000:
				g3.stap(0.01)
				stappen += 1
				var bq: Array = g3.berg_boog()
				if bq[0]:
					bb_plof = bq
			var ip: int = g3.hoeden.size() - g3.OP_HOOFD - 1
			var plek_p: Array = []
			for e3 in g3.berg_3d():
				if int(e3[3]) == ip:
					plek_p = e3
			ok(g3.hoeden.size() == 27 and bb_plof[0] and not plek_p.is_empty() and int(bb_plof[1]) == g3.hoeden[ip] and absf(float(bb_plof[2]) - float(plek_p[1])) <= 3.0 and absf(float(bb_plof[3]) - float(plek_p[2])) <= 3.0, "plof: de laatste boog eindigt op het plekje van de nieuwste hoed van de berg (%s tegen %s)" % [str(bb_plof), str(plek_p)])
			# Daan 09:45 en controleur 09:45: beeld voor beeld (0,01 s) door drie nachten in één sessie, de derde met een hap
			# midden in de nacht. Per beeld: geen plekje gaat weg, hooguit één plekje krijgt een andere hoed, en een hoed die
			# bedekt werd komt nooit meer boven.
			g3._sessie_weg()
			g3.nacht_ev.clear()
			g3.val_voor = -1
			g3.hoeden.clear()
			for i3 in 60:
				g3.hoeden.append((i3 * 7) % 10)
			var mon_vorig := {}
			var bedekt := {}
			var mon_fout := ""
			var mon_beelden := 0
			for nacht in 3:
				for i3 in 25:
					g3.krijg_hoed_later((i3 * 3 + nacht) % 10)
				g3.start_nacht(0.0)
				var gehapt := false
				var st := 0
				while (g3.nacht_bezig() or g3.berg_tel() < g3.hoeden.size() or st < 20) and st < 3000:
					g3.stap(0.01)
					st += 1
					if nacht == 2 and not gehapt and g3.nacht_gelegd >= 5:
						g3.raak(4)   # hap terwijl de nacht nog valt
						gehapt = true
					var mon_nu := {}
					for e in g3.berg():
						mon_nu[Vector2(float(e[1]), float(e[2]) + g3.HOED_ONDER[int(e[0])])] = int(e[3])
					var mon_anders := 0
					for plek in mon_vorig:
						if not mon_nu.has(plek):
							mon_fout = "nacht %d t %.2f: plekje %s weg" % [nacht, g3.t, str(plek)]
						elif int(mon_nu[plek]) != int(mon_vorig[plek]):
							mon_anders += 1
							bedekt[int(mon_vorig[plek])] = true
					for plek in mon_nu:
						if bedekt.has(int(mon_nu[plek])):
							mon_fout = "nacht %d t %.2f: bedekte hoed %d komt terug" % [nacht, g3.t, int(mon_nu[plek])]
					if mon_anders > 1:
						mon_fout = "nacht %d t %.2f: %d plekjes anders in één beeld" % [nacht, g3.t, mon_anders]
					mon_vorig = mon_nu
					mon_beelden += 1
			ok(mon_fout == "" and g3._pl_start >= 0 and mon_beelden > 100, "plof: beeld voor beeld door drie nachten en een hap, nooit meer dan één plekje anders, niets weg, niets bedekts terug (%s, %d beelden)" % [mon_fout, mon_beelden])
			g3.stap(5.0)   # de hap en de blije tijd van de monitor uit laten lopen
			g3._sessie_weg()
			g3.nacht_ev.clear()
			g3.val_voor = -1
			g3.hoed_valt = false
			# plat tijdens de boog (controleur): geen hoed die nergens staat
			g3.hoeden.assign([0, 1, 2, 3, 4, 5, 6, 7])
			g3.krijg_hoed_later(8)
			g3.start_nacht(0.0)
			g3.stap(0.01)
			g3.stap(g3.VAL_S + 0.05)
			var tel_boog: int = g3.berg_tel()
			g3.plat_tot = g3.t + 1.0
			ok(tel_boog == 8 and (not g3.is_plat() or (g3.berg_tel() == 9 and not g3.berg_boog()[0])), "nachtland: plat tijdens de boog zet de hoed meteen op de berg (%d)" % g3.berg_tel())
			g3.plat_tot = -10.0
			g3.hoeden = voor_n3
			g3.nacht_ev.clear()
			g3.val_voor = -1
			g3.hoed_valt = false
			g3.met_3d = false
			ok(g3.berg_3d().is_empty(), "3D-berg: zonder met_3d leeg (dan pixels)")
			g3.met_3d = true
			g3.hoeden = voor_b
			g3.hoeden.pop_back()   # terug naar één hoed voor de toetsen hieronder
		g3.plat()
		ok(g3.beeld_3d() == "plat", "3D: plat-beeld")
		g3.plat_tot = -100.0
		g3.hap_van = g3.t
		var standen: Array = g3.lijf3d_info["frames"]
		ok(g3.beeld_3d() == ("hap" if standen.has("hap") else ""), "3D: hap (of pixels als het blad geen hap heeft)")
		g3.raak(2)
		g3.t = g3.hap_van + g3.HAP_S + 0.1
		ok(g3.beeld_3d() == ("blij" if standen.has("blij") else "rust"), "3D: blij na een hoed erbij")
		g3.t = g3.blij_tot + 0.1
		ok(g3.beeld_3d() == "rust", "3D: na blij weer rust")
		ok(g3.knipper() == standen.has("knipper"), "3D: knipperen alleen als het blad het heeft")
		ok(g3.beeld_3d() == ("knipper" if standen.has("knipper") else "rust"), "3D: knipper-beeld")
		g3.t += g3.KNIPPER_S + 0.01   # niet knipper_tot: zonder knipper-beeld staat die op -10
		ok(g3.beeld_3d() == "rust", "3D: na 0,2 s ogen weer open")
		g3.stap(0.01)
		ok(not g3.is_processing(), "3D: na knipperen geen _process meer (zuinig)")
		# Leven in het spel 3 (Olaf 15 nov, getallen Daan juice.md): knijpen vanaf de voet, ademen met een wekker
		ok(g3.knijp_nu() == Vector2.ONE and g3.knijp_dy() == 0, "knijp: in rust niets")
		var tor_rust: Array = g3.toren_3d()
		g3.hap_van = g3.t
		g3.blij_tot = g3.t + g3.HAP_S + g3.BLIJ_S
		var lm: Vector2 = g3.lijf_maat()
		var kh: Vector2 = g3.knijp_nu()
		ok(kh.x > 1.15 and kh.y < 0.9 and g3.knijp_dy() == int(round(lm.y * 0.2)), "knijp: hap plat en breed (%s, kruin %d lager, lijf %s)" % [kh, g3.knijp_dy(), lm])
		ok(is_equal_approx(lm.y * (kh.y - 1.0), float(-g3.knijp_dy())), "knijp: de kruin zakt een heel aantal spelpixels, net als de toren")
		var tor_hap: Array = g3.toren_3d()
		ok(tor_rust.size() > 0 and tor_hap.size() == tor_rust.size() and is_equal_approx(float(tor_hap[0][2]), float(tor_rust[0][2]) + g3.knijp_dy()), "knijp: de toren zakt mee in de hap")
		g3.t = g3.hap_van + 0.1
		ok(g3.knijp_nu().x < 1.0 and g3.knijp_nu().y > 1.0 and g3.knijp_dy() < 0, "knijp: hap veert terug via 0,9 / 1,1 (%s)" % g3.knijp_nu())
		g3.t = g3.hap_van + 0.5
		ok(g3.knijp_nu() == Vector2.ONE, "knijp: na 0,33 s weer 1,0 (hap)")
		g3.t = g3.hap_van + g3.HAP_S + 0.02
		ok(g3.knijp_nu().x < 1.0 and g3.knijp_nu().y > 1.0, "knijp: blij rekt omhoog (%s)" % g3.knijp_nu())
		ok(not g3.adem(), "adem: niet tijdens blij")
		g3.t = g3.blij_tot + 0.1
		ok(g3.knijp_nu() == Vector2.ONE, "knijp: na blij weer 1,0")
		g3.set_process(false)
		ok(g3.adem() == standen.has("rust"), "adem: in rust wel")
		ok(g3.knijp_nu().x == 1.0 and is_equal_approx(lm.y * (g3.knijp_nu().y - 1.0), 1.0) and g3.knijp_dy() == -1, "adem: kruin precies één spelpixel hoger (%s)" % g3.knijp_nu())
		ok(not g3.is_processing(), "adem: zonder _process (twee wekkers)")
		var tor_adem: Array = g3.toren_3d()
		ok(tor_adem.size() == tor_rust.size() and is_equal_approx(float(tor_adem[0][2]), float(tor_rust[0][2]) - 1.0), "adem: de toren gaat 1 spelpixel mee omhoog")
		g3.adem_uit()
		ok(g3.knijp_nu() == Vector2.ONE, "adem: na de tweede wekker terug")
		g3.met_3d = false
		g3.adem_aan = true
		ok(g3.knijp_nu() == Vector2.ONE, "knijp: de pixel-Gloop knijpt niet")
		g3.met_3d = true
		g3.adem_aan = false
		g3.hap_van = -100.0
		# Spugen in 3D (Bram 15 nov): knipper, knipper, hap, hap; nooit meer het pixelbeeld zolang er een 3D-blad is
		g3.leven = "spugen"
		g3.leven_van = g3.t
		var sp_ok := true
		var sp_zag := []
		for i in 4:
			g3.t = g3.leven_van + 0.2 * i + 0.05
			var verwacht: String = g3.SPUUG_3D[i] if standen.has(g3.SPUUG_3D[i]) else "rust"
			sp_zag.append(g3.beeld_3d())
			sp_ok = sp_ok and g3.beeld_3d() == verwacht
		ok(sp_ok, "3D: spugen als kneep, kneep, spuug, spuug (%s)" % ", ".join(sp_zag))
		g3.laars_kant = 1
		g3.t = g3.leven_van + 0.6
		var lp0: Vector2i = g3.laars_pos()
		g3.t = g3.leven_van + 0.6 + g3.BOOG_S
		var lp1: Vector2i = g3.laars_pos()
		ok(lp0.x == g3.LAARS_START_3D and lp1.x == 15, "3D: laars begint achter het lijf op x 6 en landt op 15 (%d, %d)" % [lp0.x, lp1.x])
		g3.t = g3.leven_van + 0.6 + g3.BOOG_S + 0.01
		g3.stap(0.0)
		ok(g3.leven == "" and g3.beeld_3d() == "rust" and g3.laars_ligt(), "3D: na het spugen weer rust, laars ligt")
		g3.laars_weg()
		g3.met_3d = false
		ok(g3.beeld_3d() == "", "3D uit: de oude pixel-Gloop")
	else:
		print("[held-toets] let op: geen kunst/3d/sprites.json, 3D-toetsen overgeslagen")
	hol_3.free()

	# Lopen (#25, moet Daan #35): elke beeldwissel schuift precies stap_px uit sprites.json, het loopbeeld volgt de weg.
	# Bij elk beeldtempo (10, 15, 20 fps en haperend) is elke verschuiving een heel aantal stappen, nooit een rest.
	for fps in [10.0, 20.0, 15.0, 12.0]:
		var hol_p := Node2D.new()
		hol_p.set_script(load("res://systemen/toetsen/nep_hol.gd"))
		var hp := Node2D.new()
		hp.set_script(load("res://systemen/held.gd"))
		hol_p.add_child(hp)
		hp.start(hol_p, {"naam": "Pas", "trek": "dapper"})
		var np := 0
		while hp.staat != "lopen" and np < 2000:
			hp.stap(1.0 / fps)
			np += 1
		var heel := true
		var beelden := {}
		var x0: float = hp.position.x
		for i in int(fps * 6):
			hp.stap(1.0 / fps)
			if hp.staat != "lopen":
				break
			var n_st: float = absf(hp.position.x - x0) / float(hp.loop_stap)
			heel = heel and absf(n_st - roundf(n_st)) < 0.01
			beelden[hp.HELD_LOOP.beeld(hp)] = true
			x0 = hp.position.x
		ok(heel, "loop: op %d fps elke verschuiving een heel aantal stappen van %.3f" % [int(fps), hp.loop_stap])
		if fps == 12.0:
			ok(beelden.size() == hp.loop_n and hp.loop_n == 6, "loop: alle 6 loopbeelden komen voorbij (%s)" % str(beelden.keys()))
		hol_p.free()
	# haperende beelden rond 12 per s (0,083 s plus of min): toch elke wissel precies 1 stap
	for afw in [0.001, 0.005]:
		var hol_q := Node2D.new()
		hol_q.set_script(load("res://systemen/toetsen/nep_hol.gd"))
		var hq := Node2D.new()
		hq.set_script(load("res://systemen/held.gd"))
		hol_q.add_child(hq)
		hq.start(hol_q, {"naam": "Hap", "trek": "dapper"})
		var nq := 0
		while hq.staat != "lopen" and nq < 2000:
			hq.stap(1.0 / 12.0)
			nq += 1
		var spr := {}
		var xq: float = hq.position.x
		for i in 30:
			hq.stap(1.0 / 12.0 - afw if i % 2 == 0 else 1.0 / 12.0 + afw)
			if hq.staat != "lopen" or hq.HELD_LOOP.pose(hq) != "":
				xq = hq.position.x
				continue
			spr[snappedf(absf(hq.position.x - xq) / float(hq.loop_stap), 0.01)] = true
			xq = hq.position.x
		ok(spr.keys().size() >= 1 and spr.keys().all(func(k): return k == 1.0 or k == 0.0), "loop: haperend (%.3f s) toch hooguit 1 stap per beeld (%s)" % [afw, str(spr.keys())])
		hol_q.free()
	# 3D-helden (Bram 13 nov): schakelaar standaard uit, standen, en het blad laadt lineair als het er is.
	var HB3 = load("res://systemen/held_beeld.gd")
	ok(HB3.met_3d == true, "3D-held: schakelaar staat aan (hoeden A, akkoord Daan 13 nov 20:50)")
	ok(HB3.stand_3d("lopen", 0) == "stap1" and HB3.stand_3d("lopen", 5) == "stap6" and HB3.stand_3d("vluchten", 6) == "stap1", "3D-held: lopen stap1 tot stap6 in een kring")
	ok(HB3.stand_3d("lopen", 1, 9.0, false) == "rust", "3D-held: oud blad zonder stap6 houdt stap1, rust, stap2, rust")
	ok(HB3.stand_3d("vallen", 3) == "vallen" and HB3.stand_3d("klimmen", 2) == "rust", "3D-held: vallen en anders rust")
	ok(HB3.stand_3d("vallen", 3, 0.05) == "schrik" and HB3.stand_3d("vallen", 3, HB3.VAL_RECHT) == "vallen", "3D-held: eerste deel van de val de stand schrik (rechtop), daarna de valstand")
	ok(ceilf(load("res://kern/proef.gd").MOMENT_VAL_T * 15.0) / 15.0 < HB3.VAL_RECHT, "moment=val staat op 15 fps stil terwijl de held nog rechtop staat")
	HB3._laad_3d()
	if FileAccess.file_exists("res://kunst/3d/ridder.png"):
		ok(HB3.held3d.has("ridder") and HB3.held3d["ridder"][0].texture_filter == CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS, "3D-held: ridder-blad geladen, filter lineair")
	# eigen bladen (Daan 22:45): gewone held per tuniek held0..held4, dief en bard eigen blad; ontbreekt er een, dan ridder/heks
	ok(HB3.blad_voor("ridder", 3) == "ridder" and HB3.blad_voor("magier", 0) == "heks", "3D-held: ridder en magier hun eigen blad")
	ok(HB3.eigen_blad("", 2) == "held2" and HB3.eigen_blad("", 7) == "held2" and HB3.eigen_blad("dief", 1) == "dief" and HB3.eigen_blad("bard", 0) == "bard", "3D-held: eigen blad per tuniek (kleur_nr), dief en bard")
	ok(HB3.blad_voor("", 0) != "" and HB3.blad_voor("dief", 1) != "" and HB3.blad_voor("bard", 2) != "", "3D-held: gewone held, dief en bard niet in pixels")
	for k in 5:
		if HB3.held3d.has("held%d" % k):
			ok(HB3.blad_voor("", k) == "held%d" % k, "3D-held: gewone held kleur %d krijgt held%d" % [k, k])
	if HB3.held3d.has("dief") and HB3.held3d.has("bard"):
		ok(HB3.blad_voor("dief", 4) == "dief" and HB3.blad_voor("bard", 3) == "bard", "3D-held: dief en bard hun eigen blad")
		var di: Dictionary = HB3.held3d["dief"][1]
		var rj: Dictionary = HB3.held3d["ridder"][1]
		ok(absf(float(di.get("eenheid_px", 0)) - float(rj.get("eenheid_px", 1))) < 0.01, "3D-held: dief even groot als de ridder (zelfde eenheid)")
	var bewaard: Dictionary = HB3.held3d.duplicate()
	for k in ["held0", "held1", "held2", "held3", "held4", "dief", "bard"]:
		HB3.held3d.erase(k)
	ok(HB3.blad_voor("", 0) != HB3.blad_voor("", 1) and HB3.blad_voor("dief", 1) in ["ridder", "heks"], "3D-held: zonder eigen blad terugval op ridder of heks")
	HB3.GEWOON_3D = false
	ok(HB3.blad_voor("", 0) == "" and HB3.blad_voor("ridder", 0) == "ridder", "3D-held: GEWOON_3D uit en geen eigen blad geeft pixels")
	HB3.GEWOON_3D = true
	HB3.held3d = bewaard
	# tekens in 3D (Bram 14 nov, Daan 00:55): blad in de volgorde van tekens.png, 8 x 8 spelpixels, zonder blad pixels
	if FileAccess.file_exists("res://kunst/3d/tekens.png"):
		ok(HB3.held3d.has("tekens"), "3D-teken: blad tekens geladen")
	if HB3.held3d.has("tekens"):
		var ti: Dictionary = HB3.held3d["tekens"][1]
		var volg_ok := true
		for tn in HB3.TEKEN:
			volg_ok = volg_ok and (ti["frames"] as Array).find(tn) == int(HB3.TEKEN[tn])
		ok(volg_ok, "3D-teken: zelfde volgorde als tekens.png (%s)" % str(ti["frames"]))
		ok(float(ti["cel_px"][1]) / float(ti["px"]) == 8.0 and float(ti["cel_px"][0]) / float(ti["px"]) <= 10.0, "3D-teken: cel 8 hoog, hooguit 10 breed (%s)" % str(ti["cel_px"]))
		ok(HB3.held3d["tekens"][0].texture_filter == CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS, "3D-teken: lineair gefilterd")
	var doek_t := Node2D.new()
	ok(HB3.teken_3d(doek_t, "poef", 0.0, 0.0) == false, "3D-teken: onbekend teken (poef) geeft false, dan tekent de held zelf")
	# laars (Olaf 14 nov): 3D zodra het tekens-blad een beeld "laars" heeft, anders false en tekent slijm.gd de pixel-laars
	var heeft_laars: bool = HB3.held3d.has("tekens") and (HB3.held3d["tekens"][1]["frames"] as Array).has("laars")
	if heeft_laars:   # niet tekenen buiten _draw; wel het voetpunt: onder-midden zoals de pixel-laars (8 x 8)
		var li: Dictionary = HB3.held3d["tekens"][1]
		ok(float(li["anker_x"]) / float(li["px"]) == 4.0 and float(li["cel_px"][1]) / float(li["px"]) == 8.0, "3D-laars: voetpunt onder-midden, 8 hoog")
	else:
		ok(HB3.teken_3d(doek_t, "laars", 16.0, 0.0) == false, "3D-laars: nog niet in het blad, dan false en de pixel-laars")
	HB3.met_3d = false
	ok(HB3.teken_3d(doek_t, "zzz", 0.0, 0.0) == false, "3D-teken: met_3d uit geeft false, ook met blad")
	HB3.met_3d = true
	var tb: Dictionary = HB3.held3d.duplicate()
	HB3.held3d.erase("tekens")
	ok(HB3.teken_3d(doek_t, "zzz", 0.0, 0.0) == false, "3D-teken: zonder blad false, dan tekens.png")
	HB3.held3d = tb
	doek_t.position = Vector2(10, 5)
	ok(HB3.teken_onder_min(doek_t) == 1 + 8 - 5, "teken-rand: bovenkant van het teken 1 spelpixel onder de bovenrand (%d)" % HB3.teken_onder_min(doek_t))
	ok(HB3.noot_y_min(doek_t) == 9 + 1 - 5, "noot-rand: noot blijft onder het gras (rij 9) (%d)" % HB3.noot_y_min(doek_t))
	ok(HB3.teken_onder_gras(doek_t) == 9 + 8 - 5, "teken-gras: bovenkant van het teken op de eerste rij aarde (%d)" % HB3.teken_onder_gras(doek_t))
	doek_t.scale = Vector2(1.15, 1.15)
	ok(HB3.noot_y_min(doek_t) == int(ceil(4.0 / 1.15)) + 1, "noot-rand bij figuur 1,15: gedeeld door de schaal (%d)" % HB3.noot_y_min(doek_t))
	doek_t.scale = Vector2.ONE
	ok(HB3.teken_vak_3d(doek_t, "bestaat_niet", Vector2.ZERO) == false, "3D-noot: onbekend frame geeft false, dan pixels")
	if HB3.held3d.has("tekens") and (HB3.held3d["tekens"][1]["frames"] as Array).has("noot"):
		ok((HB3.held3d["tekens"][1]["frames"] as Array).find("noot") == 5, "3D-noot: 6e frame in het blad")
	doek_t.free()
	# hoeden in 3D (keuze A, Daan 13 nov 19:35): losse hoed tuimelt bij vallen, kruin en nulpunt uit de pijplijn
	var t0: Vector3 = HB3.hoed_tuimel(0.0)
	var t1: Vector3 = HB3.hoed_tuimel(0.2)
	var t2: Vector3 = HB3.hoed_tuimel(1.4)
	ok(t0.length() < 0.001, "3D-hoed: tuimelen begint op de kruin")
	ok(t1.y < -1.0 and t2.y > 6.0 and absf(t2.z) > 1.5, "3D-hoed: wipt eerst op (%.1f), zakt daarna de put in (%.1f) en draait weg (%.1f)" % [t1.y, t2.y, t2.z])
	if HB3.held3d.has("hoeden") and HB3.held3d.has("ridder"):
		var hi: Dictionary = HB3.held3d["hoeden"][1]
		var ri: Dictionary = HB3.held3d["ridder"][1]
		ok((hi["frames"] as Array).size() == 10 and hi.has("nul_y"), "3D-hoed: blad met 10 hoeden en nulpunt per hoed")
		ok(ri.has("kruin") and (ri["kruin"] as Array).size() == (ri["frames"] as Array).size(), "3D-hoed: kruin per stand van de ridder")
		var e_h := float(hi.get("eenheid_px", 0)); var e_r := float(ri.get("eenheid_px", 1))
		ok(absf(e_h / e_r - 1.3) < 0.01 and absf(float(hi.get("maal", 0)) - 1.3) < 0.001, "3D-hoed: hoedenblad op 1,3 keer de ridder, maal 1,3 in de info (%.3f)" % (e_h / e_r))
	# Lopen per soort (#25, Sanne bouwblad A): snelheid = stap_px x 12, vluchten 1,5 keer zo snel; trek maakt niet meer uit
	var snelheden := {}
	for soort_t in ["", "ridder", "magier", "bard", "dief"]:
		var hol_t := Node2D.new()
		hol_t.set_script(load("res://systemen/toetsen/nep_hol.gd"))
		hol_t.schat_kol = 30
		var ht := Node2D.new()
		ht.set_script(load("res://systemen/held.gd"))
		hol_t.add_child(ht)
		ht.start(hol_t, {"naam": "Snel" + soort_t, "trek": "hebzuchtig", "soort_held": soort_t})
		var nt := 0
		while ht.staat != "lopen" and nt < 2000:
			ht.stap(0.1)
			nt += 1
		var x_t: float = ht.position.x
		var loop_t := 0.0
		for i in 100:
			var kijk_v: bool = ht.HELD_LOOP.pose(ht) == "kijk" or ht.HELD_LOOP.kijkt(ht)
			ht.stap(0.1)
			if not kijk_v:
				loop_t += 0.1
		snelheden[soort_t] = (ht.position.x - x_t) / maxf(loop_t, 0.1)
		hol_t.free()
	print("[held-toets] loopsnelheid per soort (spelpx/s, zonder stilstaan): %s" % str(snelheden))
	ok(absf(float(snelheden[""]) - 5.6) < 0.6 and absf(float(snelheden["ridder"]) - 3.9) < 0.5 and absf(float(snelheden["dief"]) - 7.5) < 0.8, "loop: gewoon ±5,6, ridder ±3,9, dief ±7,5 spelpx/s (Sanne A)")
	ok(float(snelheden["ridder"]) < float(snelheden["bard"]) and float(snelheden["bard"]) < float(snelheden[""]) and float(snelheden[""]) < float(snelheden["dief"]), "loop: ridder < bard < gewoon < dief, je ziet het verschil")
	# rondkijken en omdraaien (Sanne A, goob): elke 3 tot 6 s 1 s stil met het kijk-beeld; vluchten begint met het draai-beeld
	var hol_kk := Node2D.new()
	hol_kk.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	hol_kk.schat_kol = 30
	var hkk := Node2D.new()
	hkk.set_script(load("res://systemen/held.gd"))
	hol_kk.add_child(hkk)
	hkk.start(hol_kk, {"naam": "Kijk", "trek": "hebzuchtig"})
	var kijk_keer := 0
	var was_kijk := false
	var kijk_lang := 0.0
	var kijk_nu := 0.0
	var kijk_af := 0
	var max_stil := 0.0
	for i in 600:
		var x_k: float = hkk.position.x
		hkk.stap(1.0 / 30.0)
		var is_kijk: bool = hkk.HELD_LOOP.pose(hkk) == "kijk"
		if is_kijk and not was_kijk:
			kijk_keer += 1
		if is_kijk:
			kijk_nu += 1.0 / 30.0
			max_stil = maxf(max_stil, absf(hkk.position.x - x_k))
		elif was_kijk:
			kijk_lang += kijk_nu
			kijk_af += 1
			kijk_nu = 0.0
		was_kijk = is_kijk
	ok(kijk_keer >= 3 and kijk_keer <= 6, "kijken: in 20 s 3 tot 6 keer stilstaan (%d)" % kijk_keer)
	ok(max_stil == 0.0 and kijk_af > 0 and absf(kijk_lang / kijk_af - 1.0) < 0.1, "kijken: dan staat hij echt stil, ±1 s per keer (%.2f s)" % (kijk_lang / maxf(kijk_af, 1)))
	hkk.HELD_LOOP.draai(hkk)
	ok(hkk.HELD_LOOP.pose(hkk) == "draai" and hkk.staat == "vluchten", "draaien: vluchten begint met het draai-beeld")
	var x_d: float = hkk.position.x
	hkk.stap(0.1)
	ok(hkk.position.x == x_d, "draaien: tijdens het draai-beeld schuift hij niet")
	hkk.stap(0.3)
	ok(hkk.HELD_LOOP.pose(hkk) == "" and hkk.position.x < x_d, "draaien: daarna rent hij terug")
	hol_kk.free()
	# Een val doet altijd iets (#25, Sanne B): geen enkele held loopt over de put zonder te vallen of te springen
	var over := 0
	var gesprongen := 0
	var gevallen_p := 0
	var tekens_p := {}
	for z in 300:
		var soort_z: String = ["", "dief", "magier", "ridder", "bard"][z % 5]
		var hol_v := Node2D.new()
		hol_v.set_script(load("res://systemen/toetsen/nep_hol.gd"))
		hol_v.vallen[9] = "stekelput"
		var hv2 := Node2D.new()
		hv2.set_script(load("res://systemen/held.gd"))
		hol_v.add_child(hv2)
		uitkomst = ""
		hv2.klaar.connect(_klaar)
		hv2.start(hol_v, {"naam": "Val%d" % z, "bezoeken": 0, "wrok": "", "zaad": 7000 + z, "soort_held": soort_z})
		var sprong_z := false
		var val_z := false
		var over_z := false
		var put_l: float = 9 * 16
		var put_r: float = 10 * 16
		var na := 0
		while uitkomst == "" and na < 20000:
			hv2.stap(1.0 / 30.0)
			na += 1
			if hv2.spring_t >= 0.0:
				if not sprong_z:
					tekens_p[soort_z] = hv2.teken_nu()
				sprong_z = true
			if hv2.staat == "vallen":
				val_z = true
			# over de put gelopen: voeten op de vloer midden boven de put, zonder sprong of val
			# ook terug bij vluchten: dan springt hij terug (zweetdruppel), nooit gewoon eroverheen
			var boven_put: bool = hv2.spring_t < 0.0 and hv2.position.x > put_l + 4 and hv2.position.x < put_r - 4
			if boven_put and ((hv2.staat == "lopen" and not sprong_z and not val_z) or hv2.staat == "vluchten"):
				over_z = true
		if over_z:
			over += 1
		if sprong_z:
			gesprongen += 1
		if val_z:
			gevallen_p += 1
		hol_v.free()
	ok(over == 0, "val doet altijd iets: geen held loopt over de put zonder te vallen of te springen (%d)" % over)
	ok(gesprongen + gevallen_p >= 300 and gesprongen > 0 and gevallen_p > 0, "val doet altijd iets: %d gevallen, %d gesprongen van 300" % [gevallen_p, gesprongen])
	ok(String(tekens_p.get("dief", "")) == "streep" and String(tekens_p.get("magier", "")) == "oog" and String(tekens_p.get("ridder", "")) == "uitroep", "sprong: dief strepen, magier oog, ridder uitroep (%s)" % str(tekens_p))
	# leven in het spel, punt 2 (hoofdchat 15 nov): de hoed vliegt van de held in een boog naar de toren en wiebelt na
	var gv = Node2D.new()
	gv.set_script(load("res://systemen/slijm.gd"))
	gv.raak(3, Vector2(14, -10))
	ok(gv.hoed_van == Vector2(14, -10) and gv.hoed_vliegt(), "hoedvlucht: begint bij de hap, vanaf het hoofd van de held")
	var v0: Array = gv.hoed_vlucht(0.0, -20.0)
	ok(v0[0] == false, "hoedvlucht: voor de beet nog niet te zien (de held heeft hem op)")
	gv.t = gv.hoed_vlucht_van + gv.VLUCHT_VAN + 0.0001
	var v1: Array = gv.hoed_vlucht(0.0, -20.0)
	ok(v1[0] and absf(float(v1[1]) - 14.0) < 0.1 and absf(float(v1[2]) + 10.0) < 0.1, "hoedvlucht: start op het hoofd van de held (%s)" % str(v1))
	gv.t = gv.hoed_vlucht_van + gv.VLUCHT_VAN + gv.VLUCHT_S * 0.5
	var v2: Array = gv.hoed_vlucht(0.0, -20.0)
	ok(float(v2[2]) < -20.0 and float(v2[1]) > 0.0 and float(v2[1]) < 14.0, "hoedvlucht: halverwege boven de rechte lijn, tussen held en toren (%s)" % str(v2))
	gv.t = gv.hoed_vlucht_van + gv.VLUCHT_VAN + gv.VLUCHT_S + 0.0001
	var v3: Array = gv.hoed_vlucht(0.0, -20.0)
	ok(is_equal_approx(float(v3[1]), 0.0) and is_equal_approx(float(v3[2]), -20.0), "hoedvlucht: landt precies op zijn plek op de toren")
	var grootst := 0.0
	for i in 20:
		gv.t = gv.hoed_vlucht_van + gv.VLUCHT_VAN + gv.VLUCHT_S + gv.WIEBEL_S * i / 20.0
		grootst = maxf(grootst, absf(float(gv.hoed_vlucht(0.0, -20.0)[3])))
	ok(is_equal_approx(grootst, deg_to_rad(gv.WIEBEL_GRAAD)), "hoedvlucht: wiebelt na, eerste uitslag 8 graden (Daan) (%.1f)" % rad_to_deg(grootst))
	var stapjes := true
	for i in 40:
		gv.t = gv.hoed_vlucht_van + gv.VLUCHT_VAN + gv.VLUCHT_S + gv.WIEBEL_S * i / 40.0
		var gr := rad_to_deg(float(gv.hoed_vlucht(0.0, -20.0)[3]))
		if absf(gr - snappedf(gr, 4.0)) > 0.01:
			stapjes = false
	ok(stapjes, "hoedvlucht: wiebel in stapjes van 4 graden")
	gv.t = gv.hoed_vlucht_van + gv.VLUCHT_VAN + gv.VLUCHT_S + 0.02
	ok(is_equal_approx(float(gv.hoed_vlucht(0.0, -20.0)[4]), 0.9), "hoedvlucht: bij de landing één beeld plat, 90% hoog")
	gv.t = gv.hoed_vlucht_van + gv.VLUCHT_VAN + gv.VLUCHT_S * 0.37
	var vh: Array = gv.hoed_vlucht(0.0, -20.0)
	ok(is_equal_approx(float(vh[1]), round(float(vh[1]))) and is_equal_approx(float(vh[2]), round(float(vh[2]))), "hoedvlucht: op hele spelpixels (%s)" % str(vh))
	gv.t = gv.hoed_vlucht_van + gv.VLUCHT_VAN + gv.VLUCHT_S + gv.WIEBEL_S + 0.01
	var v4: Array = gv.hoed_vlucht(0.0, -20.0)
	ok(not gv.hoed_vliegt() and v4[0] and is_equal_approx(float(v4[3]), 0.0), "hoedvlucht: daarna stil op de toren")
	ok(gv.hoed_vlucht_van + gv.VLUCHT_VAN + gv.VLUCHT_S + gv.WIEBEL_S <= gv.hoed_vlucht_van + gv.HAP_S + gv.BLIJ_S, "hoedvlucht: klaar binnen de blije tijd (process loopt nog)")
	gv.free()
	# winkelbeeld moment=hap (Bram 15 nov): bij de eerste hap met hoed blijft Gloop staan met de hoed hoog in de boog
	var gm = Node2D.new()
	gm.set_script(load("res://systemen/slijm.gd"))
	gm.moment_hap = true
	gm.raak(-1)
	ok(gm.moment_vast < 0.0, "moment=hap: een hap zonder hoed zet niets stil")
	gm.raak(2, Vector2(14, -10))
	for i in 60:
		gm.stap(0.05)
	var vm: Array = gm.hoed_vlucht(0.0, -20.0)
	ok(is_equal_approx(gm.t, gm.moment_vast) and gm.hoed_vliegt() and vm[0] and float(vm[2]) < -20.0, "moment=hap: na 3 s hangt de hoed nog boven de rechte lijn (%s)" % str(vm))
	ok(gm.frame_nu()[1] in gm.HAP, "moment=hap: Gloop staat stil in de hap (%s)" % str(gm.frame_nu()))
	var hoeden_voor: int = gm.hoeden.size()
	gm.plat()
	gm.raak(4, Vector2(10, -10))
	ok(not gm.is_plat() and gm.hoeden.size() == hoeden_voor and gm.hoed_vliegt(), "moment=hap: plat of een volgende hap verandert het stille beeld niet")
	gm.free()
	# Hoeden van de nacht (Sanne 17 nov 06:05, features.md; bouw Bram): na weg niet meteen op de toren, maar na de wip
	# een voor een van boven op de top; eerste 10 elk 0,3 s, de rest in één plof; samen hooguit ±4 s; save gelijk
	var VG = load("res://systemen/voortgang.gd")
	var gn = Node2D.new()
	gn.set_script(load("res://systemen/slijm.gd"))
	gn.krijg_hoed(1)
	gn.krijg_hoed(2)
	var gn_ref = Node2D.new()
	gn_ref.set_script(load("res://systemen/slijm.gd"))
	gn_ref.krijg_hoed(1)
	gn_ref.krijg_hoed(2)
	var uk := {"opgegeten": 29}
	var per_n: Array = VG.geef_hoeden([gn], uk, 7, true)
	VG.geef_hoeden([gn_ref], {"opgegeten": 29}, 7)
	ok(per_n == [29] and gn.hoeden.size() == 2 and gn.nacht_hoeden.size() == 29 and bool(uk.hoeden_gegeven), "nachthoeden: 29 in de rij, toren nog op 2 (%s)" % str(per_n))
	ok(gn.naar_dict().hoeden.size() == 31 and gn.naar_dict().hoeden == gn_ref.naar_dict().hoeden and gn.gegeten == gn_ref.gegeten, "nachthoeden: save gelijk aan meteen geven (afsluiten tijdens het vallen verliest niets)")
	gn.start_nacht()
	var eerste_t := -1.0
	var tiende_t := -1.0
	var alles_t := -1.0
	var stappen_n := {}
	var geland_voor_volgende := true
	var vorige_n := 2
	var blij_vroeg := false
	for i in 120:
		var vlucht_voor: float = gn.hoed_vlucht_van
		gn.stap(0.05)
		var nh: int = gn.hoeden.size()
		if nh > vorige_n:
			# de vorige val moet al voorbij zijn (landing) als de volgende begint
			if vorige_n > 2 and gn.t - vlucht_voor - gn.VLUCHT_VAN < gn.VAL_S:
				geland_voor_volgende = false
			stappen_n[nh - vorige_n] = true
			if eerste_t < 0.0:
				eerste_t = gn.t
			if nh >= 12 and tiende_t < 0.0:
				tiende_t = gn.t
			if nh == 31:
				alles_t = gn.t
			vorige_n = nh
		if gn.hoed_valt and gn.hoed_vliegt() and gn.t < gn.blij_van and gn.beeld_3d() == "blij":
			blij_vroeg = true
	ok(eerste_t >= gn.NACHT_WACHT_S - 0.01 and eerste_t <= gn.NACHT_WACHT_S + 0.06, "nachthoeden: eerste valt na de wip, op %.2f s" % eerste_t)
	ok(tiende_t > 0.0 and absf(tiende_t - eerste_t - 2 * gn.NACHT_TRAAG_S - 7 * gn.NACHT_TUSSEN_S) < 0.06, "nachthoeden: tiende 3,1 s na de eerste (eerste drie 0,5 s, Daan) (%.2f)" % (tiende_t - eerste_t))
	ok(alles_t > 0.0 and alles_t - eerste_t + gn.VAL_S + gn.WIEBEL_S <= 4.3, "nachthoeden: alles staat en wiebelde uit binnen ±4,2 s (Daan) (%.2f s)" % (alles_t - eerste_t + gn.VAL_S + gn.WIEBEL_S))
	ok(stappen_n.keys().has(1) and stappen_n.keys().has(19) and stappen_n.size() == 2, "nachthoeden: tien keer één, dan één plof van 19 (%s)" % str(stappen_n.keys()))
	ok(gn.hoeden == gn_ref.hoeden and gn.nacht_hoeden.is_empty(), "nachthoeden: dezelfde hoeden in dezelfde volgorde als meteen geven")
	ok(geland_voor_volgende and gn.VAL_S < gn.NACHT_TUSSEN_S, "nachthoeden: elke hoed is geland voor de volgende valt")
	ok(not blij_vroeg, "nachthoeden: Gloop pas blij bij de landing, niet tijdens de val")
	ok(gn.nacht_hoeden.is_empty() and not gn.hoed_vliegt() and gn.t > gn.blij_tot, "nachthoeden: daarna geen werk meer (rij leeg, hoed stil, blij voorbij: stap zet process uit)")
	# de val zelf: recht omlaag op de top, van boven het hol, steeds lager, geen draai; landing en wiebel als bij de held
	gn.position.y = 80.0   # zoals in het hol: Gloop staat onderin, de bovenrand ver boven hem
	gn.hoeden.append(5)
	gn.hoed_valt = true
	gn.hoed_vlucht_van = gn.t - gn.VLUCHT_VAN - 0.0001
	var vy := []
	var recht := true
	for i in 6:
		var vv: Array = gn.hoed_vlucht(3.0, -24.0)
		vy.append(float(vv[2]))
		if not vv[0] or not is_equal_approx(float(vv[1]), 3.0) or not is_equal_approx(float(vv[3]), 0.0):
			recht = false
		gn.t += gn.VAL_S / 6.0
	ok(recht and vy[0] < -24.0 and vy[0] <= gn.plafond_y() - gn.VAL_HOOG + 0.5, "nachthoed: begint boven het hol, recht boven de top, zonder draai (%s)" % str(vy))
	var dalend := true
	for i in range(1, vy.size()):
		if vy[i] < vy[i - 1]:
			dalend = false
	ok(dalend, "nachthoed: valt alleen omlaag (%s)" % str(vy))
	gn.t = gn.hoed_vlucht_van + gn.VLUCHT_VAN + gn.VAL_S + 0.02
	var vland: Array = gn.hoed_vlucht(3.0, -24.0)
	ok(is_equal_approx(float(vland[2]), -24.0) and is_equal_approx(float(vland[4]), 0.9), "nachthoed: landt op de top met één beeld plat (%s)" % str(vland))
	gn.t = gn.hoed_vlucht_van + gn.VLUCHT_VAN + gn.VAL_S + gn.WIEBEL_S + 0.01
	ok(not gn.hoed_vliegt(), "nachthoed: daarna stil")
	# een held die daarna gegeten wordt, krijgt weer de gewone boog
	gn.raak(2, Vector2(14, -10))
	ok(not gn.hoed_valt, "nachthoed: de volgende hap vliegt weer in een boog")
	# hap tijdens het vallen (controleur punt 1): de rij eerst op de toren, dan de hoed van de held bovenop met de boog
	var gh = Node2D.new()
	gh.set_script(load("res://systemen/slijm.gd"))
	for hh in [1, 2, 3, 4, 5]:
		gh.krijg_hoed_later(hh)
	gh.start_nacht()
	for i in 21:
		gh.stap(0.05)
	var n_hap: int = gh.raak(7, Vector2(14, -10))
	ok(n_hap == 6 and gh.hoeden == [1, 2, 3, 4, 5, 7] and gh.nacht_hoeden.is_empty() and not gh.hoed_valt, "nachthoeden: hap tijdens het vallen telt alles en zet de held-hoed bovenop (%d, %s)" % [n_hap, str(gh.hoeden)])
	gh.stap(0.4)
	ok(gh.hoed_vliegt() and not gh.hoed_valt and is_equal_approx(gh.hoed_van.x, 14.0), "nachthoeden: de boog van de held blijft daarna van hem")
	gh.free()
	# niets in de rij: start_nacht doet niets
	var g0 = Node2D.new()
	g0.set_script(load("res://systemen/slijm.gd"))
	g0.start_nacht()
	ok(g0.nacht_van < 0.0 and g0.hoeden.is_empty(), "nachthoeden: zonder hoeden van de nacht geen rij")
	ok(gn.nacht_aantal(-0.1, 5) == 0 and gn.nacht_aantal(0.0, 5) == 1 and gn.nacht_aantal(0.45, 5) == 1 and gn.nacht_aantal(0.5, 5) == 2 and gn.nacht_aantal(1.0, 5) == 3 and gn.nacht_aantal(1.3, 5) == 4 and gn.nacht_aantal(9.0, 5) == 5 and gn.nacht_aantal(3.1, 40) == 10 and gn.nacht_aantal(3.4, 40) == 40, "nachthoeden: tempo 0,5 / 0,5 / dan 0,3, plof na de tiende (Daan)")
	# wiebel van de vorige nooit hard afkappen: loopt door tot de nieuwe landt, dan in 0,1 s naar 0
	var gw = Node2D.new()
	gw.set_script(load("res://systemen/slijm.gd"))
	for hh in [1, 2, 3, 4, 5]:
		gw.krijg_hoed_later(hh)
	gw.start_nacht(0.0)
	gw.stap(0.0)
	var max_voor := 0.0   # tussen eigen landing en landing van de volgende
	var na_demp := 0.0    # meer dan 0,1 s na de landing van de volgende
	var gezien_vorige := false
	for i in 80:
		gw.stap(0.0125)
		if gw.hoeden.size() >= 2 and gw.vorige_idx == gw.hoeden.size() - 2:
			var land_nieuw: float = gw.hoed_vlucht_van + gw.VLUCHT_VAN + gw.VAL_S
			var a := absf(gw.vorige_wiebel(gw.vorige_idx))
			if a > 0.0:
				gezien_vorige = true
			if gw.t > land_nieuw + gw.UITDEMP_S + 0.001:
				na_demp = maxf(na_demp, a)
	ok(gezien_vorige and na_demp == 0.0, "nachthoeden: vorige hoed wiebelt nog even uit onder de nieuwe en staat 0,1 s na diens landing stil")
	gw.free()
	# van_dict (laden) leegt de rij
	gn.krijg_hoed_later(3)
	gn.van_dict(gn_ref.naar_dict())
	ok(gn.nacht_hoeden.is_empty() and gn.hoeden == gn_ref.hoeden, "nachthoeden: laden leegt de rij")
	gn.free()
	gn_ref.free()
	g0.free()
	# Berg groeit ook binnen een maat (Sanne 17 nov 07:00): recht evenredig naar het aantal van de volgende maat
	var gz = Node2D.new()
	gz.set_script(load("res://systemen/slijm.gd"))
	var zz := []
	for tz in [0, 4, 5, 24, 25, 44, 70, 99, 100, 299, 300, 1000, 2999, 3000, 9000]:
		zz.append(gz.berg_zichtbaar(tz))
	ok(zz == [0, 0, 1, 5, 6, 7, 8, 9, 10, 14, 15, 21, 32, 33, 33], "berg binnen een maat: 44 -> 7, 70 -> 8, grenzen gelijk (%s)" % str(zz))
	for i in 70:
		gz.krijg_hoed(i % 10)
	var bz: Array = gz.berg()
	var nieuwste_ok := false
	for e in bz:
		nieuwste_ok = nieuwste_ok or (int(e[3]) == gz.hoeden_op_berg() - 1 and int(e[0]) == gz.hoeden[gz.hoeden_op_berg() - 1])
	ok(bz.size() == 8 and nieuwste_ok, "berg: 8 zichtbaar, de nieuwste ligt erop (%d)" % bz.size())
	# Vaste plekjes (Iris keuring 20, Sanne 17 nov 08:50): hoed voor hoed van 5 tot 3200 hoeden. Elk plekje houdt zijn plaats,
	# er komen alleen plekjes bij, per hoed verandert hooguit één plekje (daar ligt de nieuwste), en je ziet de nieuwste n.
	gz.hoeden.clear()
	for i in 3200:
		gz.hoeden.append(i % 10)
	var vast_ok := true
	var een_ok := true
	var nieuwste_n_ok := true
	var steun_ok := true
	var vorige := {}
	var waarom := ""
	for tz in range(5, 3200):
		var bt: Array = gz.berg(tz)
		var nu := {}
		var op: int = tz - gz.OP_HOOFD
		var idx := {}
		for e in bt:
			nu[Vector2(float(e[1]), float(e[2]) + gz.HOED_ONDER[int(e[0])])] = int(e[3])
			idx[int(e[3])] = true
		for i in range(op - bt.size(), op):
			if not idx.has(i):
				nieuwste_n_ok = false
		var anders := 0
		for plek in vorige:
			if not nu.has(plek):
				vast_ok = false
				waarom = "tel %d plek %s weg" % [tz, str(plek)]
			elif int(nu[plek]) != int(vorige[plek]):
				anders += 1
				if int(nu[plek]) != op - 1:
					een_ok = false
		if anders + (nu.size() - vorige.size()) > 1:
			een_ok = false
			waarom = "tel %d: %d anders, %d erbij" % [tz, anders, nu.size() - vorige.size()]
		vorige = nu
	for k in 33:
		var rpk: Vector2i = gz.plek_rij_pos(k)
		if rpk.x > 0:
			var a := -1
			var b := -1
			for j in k:
				var q: Vector2i = gz.plek_rij_pos(j)
				if q == Vector2i(rpk.x - 1, rpk.y):
					a = j
				if q == Vector2i(rpk.x - 1, rpk.y + 1):
					b = j
			steun_ok = steun_ok and a >= 0 and b >= 0
	ok(vast_ok, "vaste plekjes: geen zichtbare hoed springt van plek, er komen alleen plekjes bij (%s)" % waarom)
	ok(een_ok, "vaste plekjes: per hoed verandert hooguit één plekje, en daar ligt de nieuwste (%s)" % waarom)
	ok(nieuwste_n_ok, "vaste plekjes: de berg toont altijd de nieuwste n hoeden")
	ok(steun_ok, "vaste plekjes: elk plekje boven de vloer ligt op twee plekjes die er al waren")
	var k70: Array = gz.berg(74)
	gz._pk_tel = -1          # zoals na laden: niets bewaard (controleur 09:30)
	gz._pk_bewaard = {}
	gz._pk_kaart = []
	gz._pk_waar = {}
	var k70b: Array = gz.berg(74)
	ok(k70.size() == 8 and k70 == k70b and gz.berg(3199).size() == 33, "vaste plekjes: zelfde tel geeft zelfde berg, ook opnieuw gerekend zoals na laden; 33 bij 3000+")
	var kaart_ro: Array = gz.berg_plekken(74)
	ok(kaart_ro.is_read_only(), "vaste plekjes: de bewaarde kaart kan niemand aanpassen")
	gz.free()
	# eerste start: hoogte bij de schaal van het scherm (Olaf 16 nov)
	var PR = load("res://kern/proef.gd")
	ok(PR.hoogte_voor_dpi(96) == 120 and PR.hoogte_voor_dpi(110) == 120, "schaal 100% en 115%: 120 px")
	ok(PR.hoogte_voor_dpi(120) == 160 and PR.hoogte_voor_dpi(144) == 160 and PR.hoogte_voor_dpi(192) == 160, "schaal 125%, 150% en 200%: 160 px")
	# een hapering (één beeld van 2,5 s) mag een held niet over een val laten springen (Bram 16 nov, vraag Sanne
	# over de koper-duurtest): hij loopt dan 25 pixels in één keer, meer dan een kolom van 16
	var hh := Node2D.new()
	hh.set_script(load("res://systemen/toetsen/nep_hol.gd"))
	for kk in range(3, 12):
		hh.vallen[kk] = "stekelput"
	var hw := Node2D.new()
	hh.add_child(hw)
	var hk := Node2D.new()
	hk.set_script(load("res://systemen/held.gd"))
	hw.add_child(hk)
	hk.start(hh, {"naam": "Haper", "bezoeken": 0, "wrok": "", "moet_doorlopen": true, "zaad": 3})
	var hn := 0
	while hk.staat in ["afdalen", "lopen"] and hn < 200:
		hk.stap(2.5)
		hn += 1
	ok(hk.gezien.size() == 9, "hapering: met beelden van 2,5 s gooit hij toch bij alle 9 vallen (%d)" % hk.gezien.size())
	hh.free()
	print("[held-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
