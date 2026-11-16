extends Node
# Olaf 16 nov 2026, proef (tak claude/steam-hol-steam-proef, vraag Sanne in platformen/steam/samen-spelen.md):
# kan GodotSteam in onze Godot 4.3-build, en valt het spel netjes terug zonder Steam?
# Zonder Steam (GitHub Actions, offline, geen app-ID): aan = false, geen _process, het spel speelt zoals altijd.
# Geen naam "Steam" in de code (Engine.get_singleton), zodat het script ook zonder de extensie gewoon laadt.

# 0 tot de demo-app bestaat (stap voor Thijs). Met 0 en zonder steam_appid.txt start Steam nooit, ook niet als
# Thijs Steam open heeft; zo komt er bij een speeltest niets op zijn Steam-profiel te staan.
const APP_ID := 0

var aan := false
var uitslag := ""
var _s: Object = null

func _ready() -> void:
	set_process(false)

func start(app_id: int = APP_ID) -> String:
	if not Engine.has_singleton("Steam"):
		uitslag = "uit: geen GodotSteam in deze build"
		return uitslag
	_s = Engine.get_singleton("Steam")
	if app_id <= 0:
		uitslag = "uit: geen app-ID (GodotSteam %s geladen)" % _versie()
		_s = null
		return uitslag
	var r = _s.steamInitEx(app_id, false)
	if r is Dictionary:
		aan = int(r.get("status", -1)) == 0
		uitslag = "%s: status %s %s (GodotSteam %s)" % ["aan" if aan else "uit", r.get("status", "?"), r.get("verbal", ""), _versie()]
	else:
		aan = bool(r)
		uitslag = "%s: %s (GodotSteam %s)" % ["aan" if aan else "uit", str(r), _versie()]
	if not aan:
		_s = null
	set_process(aan)
	return uitslag

func _versie() -> String:
	if _s and _s.has_method("get_godotsteam_version"):
		return str(_s.get_godotsteam_version())
	return "?"

func _process(_d: float) -> void:
	_s.run_callbacks()
