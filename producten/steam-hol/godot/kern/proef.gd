# Het Hol: startargumenten, proeven en winkelmomenten (Olaf 15 nov, uit kern/strook.gd gehaald; regel: bestand onder ±400).
# Alleen statische functies met de strook als eerste argument (`s`), net als wachtrij.gd en afloop.gd.
# De toestand (proef_*, moment_gemeld, hoogte, duur, ...) blijft in strook.gd.
extends RefCounted

# moment=val (Bram 15 nov 19:30): de held staat stil boven de stekels, met het uitroepteken, net voor hij wegzakt.
# De munten komen pas na de hele val (afloop.gd), dus held en munten samen in één beeld bestaat niet in het spel.
const MOMENT_VAL_T := 0.1    # tak val-schrik: rechtop in de schrik (held_beeld VAL_RECHT 0,12); main had 0,2. Daan 15 nov 21:45: proef op 0,2 (op 0,25 leest de held als klodder; 0,38 dekte de stekels af)

# Argumenten van de workflow (na `--`) gaan voor de bewaarde instelling.
static func lees_argumenten(s) -> void:
	for a in OS.get_cmdline_user_args():
		var kv: PackedStringArray = a.split("=", true, 1)
		if kv.size() < 2:
			continue
		match kv[0]:
			"hoogte": s.hoogte = clampi(int(kv[1]), 96, 160)
			"duur": s.duur = float(kv[1])
			"log": s.logpad = kv[1]
			"demo": s.demo = kv[1] == "1"
			"film": s.film = kv[1] == "1"
			"vers": s.vers = kv[1] == "1"
			"demo_einde": s.demo_grens = maxf(1.0, float(kv[1]))
			"fps":
				s.proef_fps = clampi(int(kv[1]), 8, 30)   # alleen voor de CPU-proef (demolijst 2), vast
				s.fps_vast = true
			"zaad": s.proef_zaad = int(kv[1])
			"deco_proef": s.proef_deco = kv[1] == "1"
			"royal_proef": s.proef_royal = kv[1] == "1"
			"graaf_proef": s.proef_graaf = kv[1] == "1"
			"laars_proef": s.proef_laars = kv[1] == "1"
			"spuug_proef": s.proef_spuug = clampi(int(kv[1]), 0, 3)
			"moment": s.proef_moment = kv[1] if kv[1] in ["hap", "val", "munt"] else ""
			"put_proef": s.proef_put = clampi(int(kv[1]), 0, 3)
			"figuur": s.proef_figuur = clampf(float(kv[1]), 0.5, 2.0)
			"uit3d": s.proef_uit3d = kv[1].split(",", false)

# Na het neerzetten van Gloop: laars, spugen en de winkelmomenten aanzetten.
static func na_slijm(s) -> void:
	var slijm = s.slijm
	var hol = s.hol
	if s.proef_laars and slijm.has_method("zet_laars_proef"):
		slijm.zet_laars_proef()
	if s.proef_spuug > 0 and slijm.has_method("zet_spuug_proef"):
		slijm.zet_spuug_proef(s.proef_spuug)
	if s.proef_moment == "hap" and "moment_hap" in slijm:
		slijm.moment_hap = true
	if s.proef_moment == "val" and "moment_val" in hol:
		hol.moment_val = true
	if s.proef_moment == "munt" and "moment_munt" in hol:
		hol.moment_munt = true

# Na het laden van de save: put en Royal meteen op hun stap.
static func na_laad(s) -> void:
	var hol = s.hol
	if s.proef_put > 0 and hol.upgrades != null:
		hol.upgrades.niveaus["stekelput"] = s.proef_put
		hol.queue_redraw()
	if s.proef_royal and hol.upgrades != null and s.slijm.has_method("upgrade_veranderd"):
		hol.upgrades.niveaus["slijm"] = 3
		s.slijm.upgrade_veranderd()
		s.bewaar()   # meteen bewaren, anders telt dezelfde weg-tijd na een harde afsluiting nog een keer

# Een vallende held (in _process): bij moment=val staan hij en het hol stil zodra hij MOMENT_VAL_T s valt.
static func kijk_val(s, w: Node) -> void:
	var hol = s.hol
	if hol.moment_val and not hol.moment_val_vast and float(w.get("val_t")) >= MOMENT_VAL_T:
		w.process_mode = Node.PROCESS_MODE_DISABLED
		hol.moment_val_vast = true
		hol.queue_redraw()

# Elk beeld: staat het moment stil, dan één logregel (de winkel-workflow maakt daarop zijn beelden).
static func tik(s) -> void:
	if s.proef_moment != "" and not s.moment_gemeld and staat_stil(s):
		s.moment_gemeld = true
		s.log_regel("HOL moment vast %s t=%.1f" % [s.proef_moment, s.t])

static func staat_stil(s) -> bool:
	match s.proef_moment:
		"val", "munt": return bool(s.hol.moment_val_vast)
		"hap": return "moment_vast" in s.slijm and float(s.slijm.moment_vast) >= 0.0 and float(s.slijm.t) >= float(s.slijm.moment_vast)
	return false
