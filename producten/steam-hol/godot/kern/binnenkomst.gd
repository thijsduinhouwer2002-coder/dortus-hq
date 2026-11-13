extends RefCounted
const SOORT := preload("res://systemen/heldensoort.gd")   # ridder, dief, magier, bard en drie trekken (Bram, versie 1)
# Deel van kern/strook.gd (Olaf): een nieuwe held of een terugkomer laten binnenkomen.
# Losgehaald 13 nov 2026 (strook.gd was 512 regels, regel onder ±400). Statisch; `s` is de strook.
# Gedrag gelijk aan voor het splitsen (film.log van de demo gelijk).

static func nieuwe_held(s) -> bool:
	var info := {}
	var stap: String = s._begin_stap()
	if stap == "wacht":
		return false
	# volgende held is een terugkomer: 25% (sim/UITKOMST.md); in de demo 50%, zodat de film een wrok laat zien.
	# Een aartsvijand (3 keer gevlucht) die aan de beurt is komt maar 15% van de keren.
	var kies := -1
	if stap == "terug":
		kies = s._terugkomer_i(s.begin_vlucht)
	elif stap == "" and not s.terugkomers.is_empty() and s.rng.randf() < (0.5 if s.demo else 0.25):
		var kan: Array = []
		for i in s.terugkomers.size():
			if not s.demo or s.t - float(s.vlucht_tijd.get(String(s.terugkomers[i].naam), -100.0)) >= s.DEMO_TERUG_NA:
				kan.append(i)
		if not kan.is_empty():
			kies = kan[s.rng.randi_range(0, kan.size() - 1)]
			# en pas vanaf de 60e nieuwe held, ±1 uur (Sanne features.md: geen aartsvijand in het eerste uur; Brams sim,
			# sim/UITKOMST.md: anders 32% van de spellen in uur 1). Niet in de demo, daar telt de film.
			if int(s.terugkomers[kies].bezoeken) >= 3 and ((not s.demo and not SOORT.aarts_mag(s.helden_nr)) or s.rng.randf() >= 0.15):
				kies = -1
	if kies >= 0:
		info = s.terugkomers.pop_at(kies)
		var w: String = String(info.wrok)
		if int(info.bezoeken) >= 3:
			s._kroniek(s.regels.kies("aartsvijand", {"naam": info.naam}))
		elif w == s.slijm.naam():
			s._kroniek(s._terug_regel("terug_bewoner", info, {"bewoner": s._bewoner()}))
		elif w.begins_with("the "):
			s._kroniek(s._terug_regel("terug_val", info, {"val": w}))
		else:
			s._kroniek(s.regels.kies("terug", {"naam": info.naam, "held": s._held_naam(info)}))
	else:
		var naam: String = s._vrije_naam()
		s.helden_nr += 1
		info = {"naam": naam, "bezoeken": 0, "wrok": "",
			"kleur": s.KLEUREN[s.rng.randi_range(0, s.KLEUREN.size() - 1)], "hoed": s.HOEDEN[s.rng.randi_range(0, s.HOEDEN.size() - 1)],
			"taai": s.rng.randi_range(0, 1), "hoed_nr": s.rng.randi_range(0, 9)}   # alle tien hoeden (Bram 22:40)
		if s.demo:
			info["hoed_nr"] = s.DEMO_HOEDEN[s.demo_hoed_i % s.DEMO_HOEDEN.size()]
			s.demo_hoed_i += 1
		# heldensoort en trek (Bram, versie 1): niet in de vaste stappen van het begin, en de eerste 10 helden gewoon
		var soort_h := ""
		var trek_h := ""
		if stap == "":
			soort_h = SOORT.kies(s.helden_nr, s.rng)
			trek_h = SOORT.kies_trek(s.helden_nr, s.rng)
		elif stap == "vluchten" and s.demo and s.DEMO_BARD:
			soort_h = "bard"
		if soort_h != "":
			info["soort_held"] = soort_h
		if trek_h != "":
			info["trek"] = trek_h
		if s.lied_helden > 0 and stap != "vluchten":
			# hij komt door het lied van de bard: dat moet je zien, dus een gebeurtenis die voorgaat en niet vervalt
			# (Sanne toets 9, punt 3). lied_helden telt pas af in _process als deze held er is.
			info["lied_held"] = true
			s._kroniek(s.regels.kies("binnen_lied", {"naam": naam}), false, "binnen_lied")
		elif naam.ends_with(" II") or naam.ends_with(" III"):
			s._kroniek(s.regels.kies("naamgenoot", {"naam": naam, "oud": naam.split(" ")[0]}), true)
		elif soort_h != "":
			s._kroniek(s.regels.kies("binnen_" + soort_h, {"naam": naam}), true)   # de soort zie je meteen ("Sir Odo clanks in.")
		elif trek_h != "":
			s._kroniek(s.regels.kies("binnen_" + trek_h, {"naam": naam}), true)    # de drie nieuwe trekken zie je alleen hier
		else:
			s._kroniek(s.regels.kies("binnen", {"naam": naam}), true)
	match stap:
		"vallen": info["moet_vallen"] = true
		"terug":
			# de wrok krijgt een afloop: hij komt terug voor de put en valt erin, of Gloop eet hem (Sanne toets 6, punt 1).
			# Ook buiten de demo, maar alleen in de eerste tien minuten (stap "terug" in BEGIN); daarna kan een terugkomer
			# weer ontsnappen en groeit zijn wrok.
			if String(info.get("wrok", "")).begins_with("the "):
				info["moet_vallen"] = true     # eerste verdediging op zijn pad is zijn vijand: hij loopt eerst naar de put
			else:
				info["moet_opgegeten"] = true
		"vluchten":
			info["moet_vluchten"] = true
			s.begin_vlucht = String(info.naam)
		"opgegeten", "opgegeten2":
			info["moet_opgegeten"] = true
			if stap == "opgegeten2" and s.demo:
				# Sanne toets 7, punt 1: de minuut eindigt met een clou. Zij kwam rond 43 s binnen en liep 16 s naar Gloop
				# (hap op 59,8 s, niet te zien); 1.5 gaf de hap op 55,7 s (run 42735021882), 1.8 rond 53,5 s, met regel en hoed op de toren
				info["snelheid"] = 1.8
				info["demo_clou"] = true   # haar hoed op de toren krijgt altijd een regel (controleur kan-punt 1)
			if stap == "opgegeten":
				s.opgegeten_t = s.t
				if s.demo:
					s.demo_hoed_i -= 1   # hij krijgt de kroon; zijn plek in DEMO_HOEDEN gaat naar de volgende (pan voor de Hoard-Toucher)
				# de eerste hoed op Gloop moet in één beeld lezen: de kroon (index 4 in Mila's held_hoeden.png),
				# zolang held.gd nog maar 4 hoeden kent de paarse puntmuts (index 1) (Sanne toets 4, punt 2)
				var tops: Array = s.held_script.get_script_constant_map().get("HOED_TOP", [])
				info["hoed_nr"] = 4 if tops.size() >= 10 else 1
		"doorlopen":
			info["moet_doorlopen"] = true
			if s.demo:
				info["snelheid"] = 2.0   # held.gd (Bram 23:30): raakt de schat binnen de minuut en rent nog weg; 2 sinds keus b van Daan (hele pixels per stap, 1,4 werd 1 en dan kwam hij te laat)
	if stap != "":
		s.begin_gedaan.append(stap)
		s.log_regel("HOL begin: %s (%s)" % [stap, info.naam])
	s.eerste_held_gedaan = true
	var d := info.duplicate()
	d["kleur"] = Color(info.kleur)
	d["hoed"] = Color(info.hoed)
	var held := Node2D.new()
	held.set_script(s.held_script)
	s.wezens.add_child(held)
	held.klaar.connect(s._held_klaar)
	held.start(s.hol, d)
	return true
