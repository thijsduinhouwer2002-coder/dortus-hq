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
	while uitkomst == "" and stappen < 20000:
		held.stap(1.0 / 15.0)
		stappen += 1
		if held.staat in ["vallen", "weg"]:
			val_stappen += 1
	var r := {"uitkomst": uitkomst, "info": uit_info, "eerste_doel": eerste_doel, "trek": trek, "tijd": stappen / 15.0,
		"slijm_plat": slijm != null and not slijm.kan_vechten(), "slijm_gegeten": slijm.gegeten if slijm != null else 0,
		"slijm_bestaat": slijm != null and is_instance_valid(slijm),
		"slijm_hoeden": slijm.hoeden.duplicate() if slijm != null else [],
		"val_teken": held.val_teken, "val_tijd": val_stappen / 15.0}
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
	var laars_x: int = sl.laars_pos().x
	ok(sl.leven == "" and sl.laars_ligt() and absi(sl.laars_pos().x) == 16, "laars ligt naast hem op de vloer (x %d)" % sl.laars_pos().x)
	ok(sl.begin_leven() == "slapen" and sl.frame_nu()[1] in [0, 1], "laars al gespuugd: dan slaapt hij (frames 0 en 1)")
	sl.stap(4.1)
	ok(sl.leven == "" and not sl.is_processing(), "na het slapen weer rust en zuinig")
	ok(sl.laars_ligt() and sl.laars_pos().x == laars_x, "laars blijft op zijn plek liggen, ook na het slapen")
	sl.laars_weg()
	ok(not sl.laars_ligt(), "na de wekker is de laars weg")
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
	hol5.add_child(g)
	g.zet(hol5, 6)
	ok(g.toren().is_empty() and g.berg().is_empty() and g.hover_regel() == "Gloop has no hats yet.", "zonder hoeden: geen toren, geen berg")
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
	var alle_soorten := true
	for h in g.hoeden:
		if h < 0 or h >= 10:
			alle_soorten = false
	ok(alle_soorten and g.hoeden.has(9), "10 hoedsoorten (Mila): index 0 tot 9 blijft heel")
	var d: Dictionary = g.naar_dict()
	var g2 = Node2D.new()
	g2.set_script(load("res://systemen/slijm.gd"))
	hol5.add_child(g2)
	g2.zet(hol5, 8)
	ok(g2.hoeden.is_empty(), "elke slijm zijn eigen toren")
	g2.van_dict(d)
	ok(g2.hoeden == g.hoeden and g2.gegeten == 3000, "hoeden komen terug uit de save (%d)" % g2.hoeden.size())
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
	hol_b.add_child(sl_b)
	sl_b.zet(hol_b, 6)
	sl_b.plat()
	ok(absf(sl_b.plat_tot - sl_b.t - 40.0) < 0.01, "Bouncy Gloop: plat 40 s in plaats van 60 (%.1f)" % (sl_b.plat_tot - sl_b.t))
	hol_b.free()

	# Sanne toets 7 punt 2: de val duurt ±1 s en je ziet hem wegzakken (niet één beeld half doorzichtig)
	r = speel({"naam": "Bram", "bezoeken": 1, "wrok": "the Spike Pit", "moet_afgerekend": true, "zaad": 5})
	ok(r.val_tijd >= 1.0 and r.val_tijd <= 1.3, "de val duurt ±1 s tot klaar() (%.2f s)" % r.val_tijd)
	ok(r.val_teken == "boos", "terugkomer op weg naar zijn put had het boze wolkje toen hij viel (%s)" % r.val_teken)
	var hv := Node2D.new()
	hv.set_script(load("res://systemen/held.gd"))
	hv.val_teken = "boos"
	var b0: Dictionary = hv.val_beeld(0.05)
	var b1: Dictionary = hv.val_beeld(0.45)
	var b2: Dictionary = hv.val_beeld(0.7)
	var b3: Dictionary = hv.val_beeld(1.0)
	ok(int(b0.hop) < 0 and int(b0.zak) == 0, "eerst schrik: hop omhoog, nog niet gezakt (hop %d)" % b0.hop)
	ok(int(b1.zak) > 0 and int(b1.zak) < int(b2.zak) and int(b2.zak) < 16, "dan zakt hij zichtbaar in stappen (%d, %d)" % [b1.zak, b2.zak])
	ok(int(b3.zak) == 16, "op 1,0 s helemaal onder de vloer (%d)" % b3.zak)
	ok(String(b0.teken) == "poef" and String(b3.teken) == "", "boze wolkje knapt als poef, daarna geen teken")
	var hbeeld = load("res://systemen/held_beeld.gd")
	var fasen: Array = []
	for i in 8:
		var vbi: Dictionary = hv.val_beeld(i * 0.05)
		if String(vbi.teken) == "poef":
			fasen.append(hbeeld.poef_beeld(float(vbi.poef_fase)))
	ok(fasen == [0, 0, 1, 1, 2, 2, 3, 3], "poef: Mila's 4 beelden op 10 fps, één keer (%s)" % str(fasen))
	ok(hbeeld.POEF.get_width() == 48 and hbeeld.POEF.get_height() == 10, "poef.png is 4 beelden van 12 x 10")
	hv.val_teken = ""
	ok(String(hv.val_beeld(0.1).teken) == "uitroep", "zonder wrok: uitroepteken bij de schrik")
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
	ok(sl_u.top_nu() == top_klein - 1, "Big Gloop: kruin 1 hoger (%d tegen %d)" % [sl_u.top_nu(), top_klein])
	var toren_groot: Array = sl_u.toren()
	ok(int(toren_groot[0][2]) == int(toren_klein[0][2]) - 1 and int(toren_groot[1][2]) == int(toren_klein[1][2]) - 1, "de hoedentoren schuift 1 mee, zakt niet in zijn kruin")
	ok(sl_u.hoogste_punt() == int(toren_groot[1][2]) + sl_u.HOED_TOP[1], "hoogste punt = bovenkant van de bovenste hoed (%d)" % sl_u.hoogste_punt())
	sl_u.plat()
	ok(sl_u.frame_nu()[0] == sl_u.LEVEN_GROOT and sl_u.frame_nu()[1] == sl_u.PLAT, "Big Gloop plat: plat-frame uit het grote blad")
	upg_u.verkoop("slijm")
	sl_u.upgrade_veranderd()
	ok(sl_u.frame_nu()[0] == sl_u.LEVEN and sl_u.niveau() == 0, "Undo: weer het gewone blad")
	hol_u.free()

	# Trick Lid: de magier ziet de put niet meer (idee Sanne 10 nov 03:10)
	ok(is_equal_approx(HS.kans_factor("magier", "stekelput"), 0.3) and is_equal_approx(HS.kans_factor("magier", "stekelput", true), 1.0), "Trick Lid: magier van 0,3 naar 1,0 voor de put")
	ok(is_equal_approx(HS.kans_factor("dief", "stekelput", true), 0.5) and is_equal_approx(HS.kans_factor("magier", "slijm", true), 1.25), "Trick Lid verandert niets voor de dief of voor Gloop")

	print("[held-toets] klaar: %d FOUT" % fout)
	quit(1 if fout > 0 else 0)
