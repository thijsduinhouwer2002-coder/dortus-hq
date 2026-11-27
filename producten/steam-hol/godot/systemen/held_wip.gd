extends RefCounted
# Tekens boven een held poppen op en gaan zacht weg (#85). Les uit Godot Open RPG (GDQuest, MIT, src/field/ui/popups/
# ui_popup.gd): een teken knipt nooit aan of uit, het groeit, wipt af en toe even "to draw the player's eye" met een pauze
# ertussen "so that the popup doesn't look overly energetic", en gaat korter weg dan het kwam.
# Keuzes Sanne (27 nov): komen 0,2 s met een zachte rem, weg 0,15 s, een kleine wip elke 2,5 s (bureauspel, niet 0,8 s),
# het sprongteken alleen de komwip. Het 3D-teken groeit (lineair gefilterd, mag); een pixelteken (tekens.png, oog,
# strepen) schaalt nooit: dat wipt hele spelpixels omhoog en zakt terug, en vervaagt bij komen en gaan.
# De stand staat op de held zelf (h.wip), zodat elke held zijn eigen klok heeft en de toets het kan nakijken.

const IN_S := 0.2      # zo lang groeit een teken
const UIT_S := 0.15    # zo lang gaat het weg
const PAUZE_S := 2.5   # om de zoveel tijd één kleine wip zolang het teken staat
const WIP_S := 0.3     # duur van die wip
const IN_PX := 2       # pixelteken bij komen: zo hoog wipt het (hele spelpixels)
const WIP_PX := 1      # wip in de pauze: zo hoog (hele spelpixels)
const KLEIN := 0.25    # 3D-teken: hiermee begint het te groeien en hier eindigt het weggaan

# Wat er nu boven het hoofd hoort, gegeven het teken van dit moment (tk, "" = geen). Geeft 0, 1 of 2 tekens terug, eerst
# het teken dat weggaat, dan het huidige: {"tk", "s" (schaal 3D), "hop" (spelpixels, alleen pixeltekens), "dy" (spelpixels,
# beide), "a" (dekking)}. sprong = het teken hoort bij een sprong over een val (geen pauze-wip).
static func stand(h, tk: String, t: float, sprong: bool) -> Array:
	if _wissel != 0 and not _aan():
		return [] if tk == "" else [{"tk": tk, "s": 1.0, "hop": 0, "dy": 0, "a": 1.0}]   # meten: zoals voor #85
	var w: Dictionary = h.wip
	var oud := String(w.get("tk", ""))
	if oud != tk:
		if oud != "":
			var nu := vorm(w, t)   # weggaan begint waar het nu is: midden in het groeien krimpt het vanaf daar
			w["weg_tk"] = oud
			w["weg_van"] = t
			w["weg_s"] = float(nu.s)
			w["weg_a"] = float(nu.a)
			w["weg_dy"] = int(nu.dy) + int(nu.hop)
		w["tk"] = tk
		w["van"] = t
		w["sprong"] = sprong
	var uit: Array = []
	if String(w.get("weg_tk", "")) != "":
		var u := (t - float(w.weg_van)) / UIT_S
		if u >= 1.0 or u < 0.0:
			w["weg_tk"] = ""
		else:
			var e := u * u   # eerst langzaam, dan weg
			uit.append({"tk": String(w.weg_tk), "s": lerpf(float(w.weg_s), KLEIN, e), "hop": 0,
				"dy": int(w.weg_dy) - int(round(u)), "a": float(w.weg_a) * (1.0 - u)})
	if tk != "":
		var v := vorm(w, t)
		v["tk"] = tk
		uit.append(v)
	return uit

# Vorm van het huidige teken op tijd t (los van tekenen, zodat de toets het kan nakijken).
static func vorm(w: Dictionary, t: float) -> Dictionary:
	var a := t - float(w.get("van", t))
	if a < IN_S:
		var u := clampf(a / IN_S, 0.0, 1.0)
		var e := 1.0 - pow(1.0 - u, 3.0)   # zachte rem
		return {"s": lerpf(KLEIN, 1.0, e), "hop": -int(round(IN_PX * sin(PI * u))), "dy": 0, "a": minf(1.0, 0.25 + u * 1.5)}
	var dy := 0
	if not bool(w.get("sprong", false)):
		var p := fmod(a - IN_S, PAUZE_S)
		if p >= PAUZE_S - WIP_S:
			dy = -int(round(WIP_PX * sin(PI * (p - (PAUZE_S - WIP_S)) / WIP_S)))
	return {"s": 1.0, "hop": 0, "dy": dy, "a": 1.0}

# Meten (#85, CPU hooguit +1 procent om en om): startargument wissel=tekens zet de wip om de 20 s aan en uit (oneven
# blokken uit: dan knipt het teken zoals vroeger), wissel=nep schrijft dezelfde regels maar laat hem aan (placebo).
# Regel "HOL wissel tekens aan|uit unix=<s> t=<speltijd> pad=Hol" voor platformen/steam/data/cpu-duur/cpu_stenen.py.
const WISSEL_S := 20.0
static var _wissel := -1   # -1 nog niet gelezen, 0 uit, 1 echt, 2 placebo
static var _was := true
static func _aan() -> bool:
	if _wissel < 0:
		var a := OS.get_cmdline_user_args()
		_wissel = 1 if "wissel=tekens" in a else (2 if "wissel=nep" in a else 0)
		if _wissel == 0:
			return true
	var aan := int(Time.get_unix_time_from_system() / WISSEL_S) % 2 == 0
	if aan != _was:
		_was = aan
		var lus := Engine.get_main_loop() as SceneTree
		var sc: Node = lus.current_scene if lus != null else null
		var t: float = float(sc.get("t")) if sc != null and sc.get("t") != null else -1.0
		print("HOL wissel tekens %s unix=%.2f t=%.2f pad=Hol" % ["aan" if aan else "uit", Time.get_unix_time_from_system(), t])
	return aan or _wissel == 2
