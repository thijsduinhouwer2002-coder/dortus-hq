extends RefCounted
# De save mag nooit stilletjes weg (Olaf 26 nov, issue #194). Les uit Antimatter Dimensions (MIT, bekeken in
# organisatie/lat/broncode/antimatter-dimensions.md): daar is "I lost everything" de bovenste slechte review.
#
# Schrijven: eerst naar <pad>.tmp, teruglezen of alles erin staat, dan pas de oude save naar <naam>.vorige.json
# en de .tmp naar <pad>. Gaat de pc uit midden in het schrijven, dan staat de oude save er nog (als <pad> of als vorige).
# Lezen: <pad>, anders <naam>.vorige.json, anders een complete .tmp. Een onleesbare save wordt <naam>.kapot.json en
# wordt nooit overschreven (bestaat die al, dan komt er de tijd achter).
# Eerst weghalen en dan hernoemen, nooit hernoemen over een bestaand bestand heen: zo werkt het op Windows en Linux gelijk.

static func vorige(pad: String) -> String:
	return pad.get_basename() + ".vorige." + pad.get_extension()

static func tmp(pad: String) -> String:
	return pad + ".tmp"

# Vrije naam naast pad, bv. hol.kapot.json of hol.v2.json; bestaat hij al, dan hol.kapot.<tijd>.json (nooit overschrijven).
static func vrije_naam(pad: String, stuk: String) -> String:
	var n := pad.get_basename() + "." + stuk + "." + pad.get_extension()
	var i := 0
	while FileAccess.file_exists(n):
		i += 1
		n = "%s.%s.%d_%d.%s" % [pad.get_basename(), stuk, int(Time.get_unix_time_from_system()), i, pad.get_extension()]
	return n

# Zet een bestand opzij onder een vrije naam (kapot of oude versie). Geeft de nieuwe naam, of "" als het niet lukte.
static func zet_opzij(pad: String, stuk: String) -> String:
	if not FileAccess.file_exists(pad):
		return ""
	var n := vrije_naam(pad, stuk)
	if DirAccess.rename_absolute(pad, n) != OK:
		return ""
	return n

# true als de nieuwe save op <pad> staat. Bij false is er niets van de oude saves weg.
static func schrijf(pad: String, tekst: String) -> bool:
	var t := tmp(pad)
	var f := FileAccess.open(t, FileAccess.WRITE)
	if f == null:
		return false
	f.store_string(tekst)
	f.close()
	# terugelezen: een volle schijf of een half geschreven .tmp mag nooit over een goede save heen
	if FileAccess.get_file_as_string(t) != tekst:
		DirAccess.remove_absolute(t)
		return false
	var v := vorige(pad)
	# een onleesbare <pad> schuift nooit door naar vorige (dan was de goede vorige weg): eerst opzij als kapot
	if FileAccess.file_exists(pad) and _lees_dict(pad) == null and zet_opzij(pad, "kapot") == "":
		DirAccess.remove_absolute(t)
		return false
	if FileAccess.file_exists(pad):
		if FileAccess.file_exists(v) and DirAccess.remove_absolute(v) != OK:
			return false
		if DirAccess.rename_absolute(pad, v) != OK:
			return false
	# geen <pad> (eerste keer, of hij werd net kapot opzij gezet): de vorige blijft staan tot er een nieuwe goede is
	return DirAccess.rename_absolute(t, pad) == OK

static func _lees_dict(pad: String):
	if not FileAccess.file_exists(pad):
		return null
	var j := JSON.new()   # JSON.new().parse meldt geen engine-fout in het log, parse_string wel
	if j.parse(FileAccess.get_file_as_string(pad)) != OK:
		return null
	return j.data if typeof(j.data) == TYPE_DICTIONARY else null

# {"data": Dictionary of null, "bron": welk bestand, "kapot": naam van het opzij gezette kapotte bestand of ""}
static func lees(pad: String) -> Dictionary:
	var uit := {"data": null, "bron": "", "kapot": ""}
	var d = _lees_dict(pad)
	if d != null:
		uit.data = d
		uit.bron = pad
		return uit
	if FileAccess.file_exists(pad):
		uit.kapot = zet_opzij(pad, "kapot")
	for p in [vorige(pad), tmp(pad)]:
		d = _lees_dict(p)
		if d != null:
			uit.data = d
			uit.bron = p
			return uit
	return uit
