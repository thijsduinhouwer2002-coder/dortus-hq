extends RefCounted
# Bewaren van een held die nog in het hol loopt (Olaf, kan-punt 00:40: bij wisselen van hoogte of afsluiten verdween hij).
# Los van held.gd sinds 25 nov (issue #25, held.gd bleef anders boven de 400 regels); held.gd roept dit aan.
# naar_dict(h) geeft alleen JSON-veilige waarden (kleuren als tekst, rng.state als tekst want JSON rekent met doubles);
# herstel(held, hol, d) zet hem precies terug, ook midden in een val. Roep herstel aan na add_child (anders vindt hij de
# bewoners niet). Een held die al "weg" is geeft {}: niet bewaren. Midden in een sprong bewaard: de sprong gaat na herstel
# precies zo verder (alle loopvelden gaan mee).
# Alleen de velden hieronder worden weer een Color of een heel getal; een nieuw kleurveld hier bijzetten.
const KLEUR_VELDEN := ["kleur", "hoed"]
const HEEL_VELDEN := ["bezoeken", "hoed_nr", "kleur_nr", "hoeden_bewoner", "zaad", "taai", "lied"]

static func naar_dict(h) -> Dictionary:
	if h.staat == "weg":
		return {}
	var i := {}
	for k in h.info.keys():
		var v = h.info[k]
		i[k] = (v as Color).to_html(false) if v is Color else v
	return {"info": i, "staat": h.staat, "x": h.position.x, "y": h.position.y, "doel_kol": h.doel_kol, "vijand_kol": h.vijand_kol,
		"klappen": h.klappen, "t": h.t, "geraakt_tot": h.geraakt_tot, "val_t": h.val_t, "val_teken": h.val_teken,
		"gezien": h.gezien.keys(), "verdedigingen": h.verdedigingen, "rng": str(h.rng.state),
		"dut_kol": h.dut_kol, "dut_tot": h.dut_tot, "pas_klok": h.pas_klok, "pas_rest": h.pas_rest,
		"loop": [h.afgelegd, h.loop_klok, h.kijk_tot, h.volgende_kijk, h.draai_tot, h.spring_t, h.spring_van, h.spring_naar],
		"spring_teken": h.spring_teken, "na_sprong": h.na_sprong, "rng_loop": str(h.rng_loop.state),
		"terug_gesprongen": h.terug_gesprongen.keys(), "precies": precies_van(h)}

# De klokken precies (JSON schrijft getallen afgerond; een klok net op een beeldgrens gaf dan na herstel één beeld
# verschil). Als bytes in base64, ook in een oude save zonder dit veld werkt herstel gewoon zoals eerst.
static func precies_van(h) -> String:
	var a := PackedFloat64Array([h.t, h.pas_klok, h.loop_klok, h.kijk_tot, h.volgende_kijk, h.draai_tot, h.spring_t, h.afgelegd,
		h.position.x, h.position.y, h.val_t, h.geraakt_tot, h.dut_tot])
	return Marshalls.raw_to_base64(a.to_byte_array())

static func precies_naar(held, tekst: String) -> void:
	var a := Marshalls.base64_to_raw(tekst).to_float64_array()
	if a.size() != 13:
		return
	held.t = a[0]; held.pas_klok = a[1]; held.loop_klok = a[2]; held.kijk_tot = a[3]; held.volgende_kijk = a[4]
	held.draai_tot = a[5]; held.spring_t = a[6]; held.afgelegd = a[7]; held.position = Vector2(a[8], a[9])
	held.val_t = a[10]; held.geraakt_tot = a[11]; held.dut_tot = a[12]

static func herstel(held, hol, d: Dictionary) -> void:
	var i: Dictionary = (d.get("info", {}) as Dictionary).duplicate()
	for k in KLEUR_VELDEN:
		if i.get(k) is String:
			i[k] = Color(String(i[k]))
	for k in HEEL_VELDEN:
		if i.get(k) is float:
			i[k] = int(i[k])
	var gezien_v = i.get("gezien_vijand", null)
	held.start(hol, i)
	if gezien_v != null:
		held.info["gezien_vijand"] = gezien_v   # start() zet hem terug op false via _kies_doel
	held.staat = String(d.get("staat", held.staat))
	held.position = Vector2(float(d.get("x", held.position.x)), float(d.get("y", held.position.y)))
	if not d.has("pas_rest"):
		held.position = held.position.round()   # oude save: lopen ging toen in delen van een pixel
	held.doel_kol = int(d.get("doel_kol", held.doel_kol))
	held.vijand_kol = int(d.get("vijand_kol", held.vijand_kol))
	held.klappen = int(d.get("klappen", 0))
	held.t = float(d.get("t", 0.0))
	held.geraakt_tot = float(d.get("geraakt_tot", 0.0))
	held.val_t = float(d.get("val_t", 0.0))
	held.val_teken = String(d.get("val_teken", ""))
	held.gezien.clear()
	for k in d.get("gezien", []):
		held.gezien[int(k)] = true
	held.verdedigingen = int(d.get("verdedigingen", 0))
	held.dut_kol = int(d.get("dut_kol", held.dut_kol))
	held.dut_tot = float(d.get("dut_tot", 0.0))
	held.pas_klok = float(d.get("pas_klok", held.PAS / 4.0))
	held.pas_rest = float(d.get("pas_rest", 0.0))
	var lp: Array = d.get("loop", [])
	if lp.size() == 8:
		held.afgelegd = float(lp[0]); held.loop_klok = float(lp[1]); held.kijk_tot = float(lp[2]); held.volgende_kijk = float(lp[3])
		held.draai_tot = float(lp[4]); held.spring_t = float(lp[5]); held.spring_van = float(lp[6]); held.spring_naar = float(lp[7])
	held.spring_teken = String(d.get("spring_teken", ""))
	held.na_sprong = String(d.get("na_sprong", ""))
	held.terug_gesprongen.clear()
	for k in d.get("terug_gesprongen", []):
		held.terug_gesprongen[int(k)] = true
	if d.has("precies"):
		precies_naar(held, String(d.precies))
	if d.has("rng_loop"):
		held.rng_loop.state = String(d.rng_loop).to_int()
	if d.has("rng"):
		held.rng.state = String(d.rng).to_int()
