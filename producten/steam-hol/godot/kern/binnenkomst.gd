extends RefCounted
const SOORT := preload("res://systemen/heldensoort.gd")   # ridder, dief, magier, bard en drie trekken (Bram, versie 1)
# Deel van kern/strook.gd (Olaf): een nieuwe held of een terugkomer laten binnenkomen.
# Losgehaald 13 nov 2026 (strook.gd was 512 regels, regel onder ±400). Statisch; `s` is de strook.
# Gedrag gelijk aan voor het splitsen (film.log van de demo gelijk).

# Mag deze held de naamgenoot-regel krijgen? Alleen een II of III, één keer per voornaam per speelbeurt, en hooguit
# één naamgenoot-regel per NAAMGENOOT_PAUZE seconden (Iris keuring 23 punt 1: zes keer "wants dad's boot back" tussen
# 884 en 1363 s in duurtest 44127812882). Anders krijgt hij de gewone binnenkomstregel; zijn voornaam blijft vrij.
const NAAMGENOOT_PAUZE := 300.0
static func naamgenoot_mag(naam: String, gezien: Dictionary, t: float, laatst: float) -> bool:
	if not (naam.ends_with(" II") or naam.ends_with(" III")):
		return false
	if gezien.has(naam.split(" ")[0]):
		return false
	return t - laatst >= NAAMGENOOT_PAUZE

# De volle naam van de ouder: "Kees II" -> "Kees", "Kees III" -> "Kees II". Alleen die laars telt (Iris 19 nov).
static func ouder_naam(naam: String) -> String:
	var basis := naam.split(" ")[0]
	if naam.ends_with(" III"):
		return basis + " II"
	return basis

const EERSTE_SNEL := 2.0

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
		elif naamgenoot_mag(naam, s.naamgenoot_gezien, s.t, s.naamgenoot_laatst):
			# één naamgenoot-regel per voornaam per speelbeurt (Sanne 16 nov 22:00, balans.md vraag 2); daarna de gewone regel
			s.naamgenoot_gezien[naam.split(" ")[0]] = true
			s.naamgenoot_laatst = s.t
			var ng_soort := "naamgenoot_laars" if s.laars_namen.has(ouder_naam(naam)) else "naamgenoot"
			s._kroniek(s.regels.kies(ng_soort, {"naam": naam, "oud": naam.split(" ")[0]}), true)
		elif soort_h != "":
			s._kroniek(s.regels.kies("binnen_" + soort_h, {"naam": naam}), true)   # de soort zie je meteen ("Sir Odo clanks in.")
			info["binnen_soort"] = soort_h   # opzet: de vangst of vlucht slaat erop terug (afloop.gd, Sanne 17 nov 09:02)
		elif trek_h != "":
			s._kroniek(s.regels.kies("binnen_" + trek_h, {"naam": naam}), true)    # de drie nieuwe trekken zie je alleen hier
			info["binnen_soort"] = trek_h
		else:
			s._kroniek(s.regels.kies("binnen", {"naam": naam}), true)
	# kaartje na terugkomst (moet Daan 16 nov 23:30): de telling staat bovenaan tot de eerste nieuwe held binnen is
	if s.tekst != null and String(s.tekst.vast) != "":
		s.tekst.vast = ""
		s.tekst.queue_redraw()
	s.namen_recent.append(String(info.naam))
	while s.namen_recent.size() > 24:
		s.namen_recent.remove_at(0)
	match stap:
		"vallen":
			info["moet_vallen"] = true
			# Iris (#25, build 46cdec1): de eerste klap kwam pas op 37 s. De eerste held van een vers spel rent recht op de
			# eerste val af (zelfde beelden sneller, held_loop.gd), zodat de eerste klap rond 10 s valt.
			if not s.demo:
				info["snelheid"] = EERSTE_SNEL
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
	# elke held, ook na de vaste stappen: de Windows-toets (demo-einde) kijkt hiernaar (kan-punt controleur 13 nov)
	s.log_regel("HOL held binnen: %s" % info.naam)
	s.eerste_held_gedaan = true
	var d := info.duplicate()
	d["kleur"] = Color(info.kleur)
	d["hoed"] = Color(info.hoed)
	var held := Node2D.new()
	held.set_script(s.held_script)
	s.wezens.add_child(held)
	held.scale = Vector2.ONE * float(s.proef_figuur)   # figuur=<factor> (keurstand), oorsprong is het voetpunt
	held.klaar.connect(s._held_klaar)
	held.start(s.hol, d)
	return true

# Welke vaste stap is nu aan de beurt: "" (vrij spel) of "wacht" (de volgende stap kan nog niet, even later opnieuw).
# (Olaf 15 nov: uit strook.gd hierheen, strook.gd houdt _begin_stap als doorgeefluik.)
static func begin_stap(s) -> String:
	var wacht := false
	for stap in s._begin_lijst():
		if s.begin_gedaan.has(stap):
			continue
		if stap == "terug" and s._terugkomer_i(s.begin_vlucht) < 0:
			wacht = true       # hij is nog in het hol; eerst een andere stap
			continue
		if stap == "terug" and s.demo and s.t - s.vlucht_t < 4.0:
			return "wacht"     # demo: niet meteen na zijn vlucht terug, anders komen vier regels in 2 s (film run 42721290569)
		if stap == "doorlopen" and s.demo and s.t - s.opgegeten_t < 10.0:
			return "wacht"     # demo: Hoard-Toucher 4 s later dan voorheen, de drukke stap rond 30 s (Sanne toets 6, punt 3)
		if stap.begins_with("opgegeten") and s.slijm.has_method("kan_vechten") and not s.slijm.kan_vechten():
			wacht = true       # Gloop ligt plat; wacht tot hij weer op is
			continue
		return stap
	return "wacht" if wacht else ""
