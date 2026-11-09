extends Node2D
# Een strook van 220 px hoog over de hele breedte, net boven de taakbalk. Alles buiten de strook is doorzichtig
# en klikken gaan erdoorheen (mouse passthrough). In het log schrijven we wat we zien, als bewijs.

var t := 0.0
var strook := Rect2()
var stand := "vol60"  # vol60 (oud: elke frame, geen grens), fps30, zuinig (low processor, 15 fps)
var logpad := ""
var duur := 40.0

func log_regel(tekst: String) -> void:
	# De gewone exe heeft geen console; daarom schrijven we zelf een logbestand (pad via -- log=...).
	print(tekst)
	if logpad != "":
		var f := FileAccess.open(logpad, FileAccess.READ_WRITE if FileAccess.file_exists(logpad) else FileAccess.WRITE)
		if f:
			f.seek_end()
			f.store_line(tekst)
			f.close()

func _ready() -> void:
	for a in OS.get_cmdline_user_args():
		if a.begins_with("stand="):
			stand = a.substr(6)
		elif a.begins_with("log="):
			logpad = a.substr(4)
		elif a.begins_with("duur="):
			duur = float(a.substr(5))
	match stand:
		"fps30":
			Engine.max_fps = 30
		"zuinig":
			Engine.max_fps = 15
			OS.low_processor_usage_mode = true
	get_viewport().transparent_bg = true
	var scherm := DisplayServer.screen_get_usable_rect()  # zonder taakbalk
	var hoogte := 220
	var pos := Vector2i(scherm.position.x, scherm.position.y + scherm.size.y - hoogte)
	DisplayServer.window_set_size(Vector2i(scherm.size.x, hoogte))
	DisplayServer.window_set_position(pos)
	strook = Rect2(0, 60, scherm.size.x, hoogte - 60)
	# Alleen de strook vangt klikken; de lucht erboven laat ze door naar het venster eronder.
	DisplayServer.window_set_mouse_passthrough(PackedVector2Array([
		Vector2(0, 60), Vector2(scherm.size.x, 60), Vector2(scherm.size.x, hoogte), Vector2(0, hoogte)]))
	log_regel("PROEF stand=" + stand)
	log_regel("PROEF renderer=%s / %s" % [RenderingServer.get_video_adapter_name(), OS.get_name()])
	log_regel("PROEF bruikbaar scherm=%s venster pos=%s maat=%s" % [scherm, pos, DisplayServer.window_get_size()])
	log_regel("PROEF doorzichtig=%s altijd boven=%s" % [DisplayServer.window_get_flag(DisplayServer.WINDOW_FLAG_TRANSPARENT),
		DisplayServer.window_get_flag(DisplayServer.WINDOW_FLAG_ALWAYS_ON_TOP)])

func _input(event: InputEvent) -> void:
	if event is InputEventMouseButton and event.pressed:
		log_regel("PROEF klik in de strook op " + str(event.position))

func _process(delta: float) -> void:
	t += delta
	queue_redraw()
	if t > duur:
		log_regel("PROEF stand=%s fps na %d s=%d" % [stand, int(duur), Engine.get_frames_per_second()])
		get_tree().quit()

func _draw() -> void:
	# Papieren heuvels in lagen (de beeldtaal van Daan, heel grof), een lantaarn die beweegt.
	var w := strook.size.x
	var kleuren := [Color("#6b3a5a"), Color("#8a4a63"), Color("#2b1d33")]
	for i in 3:
		var pts := PackedVector2Array()
		var basis := 60.0 + 40.0 * i
		pts.append(Vector2(0, 220))
		var x := 0.0
		while x <= w:
			pts.append(Vector2(x, basis + 25.0 * sin(x / (180.0 + 60 * i) + i)))
			x += 24.0
		pts.append(Vector2(w, 220))
		draw_colored_polygon(pts, kleuren[i])
	var lx := fmod(t * 60.0, w)
	draw_circle(Vector2(lx, 170), 10.0, Color("#ffd27a"))
	draw_circle(Vector2(lx, 170), 22.0, Color("#5a3a4a"))  # gloed dekkend vooraf gemengd (halfdoorzichtig laat het bureaublad door)
	draw_circle(Vector2(lx, 170), 10.0, Color("#ffd27a"))
	draw_string(ThemeDB.fallback_font, Vector2(20, 100), "Dortus proef (%s): doorzichtig boven de taakbalk, t=%d s" % [stand, int(t)],
		HORIZONTAL_ALIGNMENT_LEFT, -1, 22, Color.WHITE)
