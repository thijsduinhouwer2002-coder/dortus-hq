extends Node2D
# Een strook van 220 px hoog over de hele breedte, net boven de taakbalk. Alles buiten de strook is doorzichtig
# en klikken gaan erdoorheen (mouse passthrough). In het log schrijven we wat we zien, als bewijs.

var t := 0.0
var strook := Rect2()

func _ready() -> void:
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
	print("PROEF renderer=", RenderingServer.get_video_adapter_name(), " / ", OS.get_name(),
		" driver=", ProjectSettings.get_setting("rendering/renderer/rendering_method"))
	print("PROEF bruikbaar scherm=", scherm, " venster pos=", pos, " maat=", DisplayServer.window_get_size())
	print("PROEF doorzichtig gevraagd=", DisplayServer.window_get_flag(DisplayServer.WINDOW_FLAG_TRANSPARENT),
		" altijd boven=", DisplayServer.window_get_flag(DisplayServer.WINDOW_FLAG_ALWAYS_ON_TOP))

func _process(delta: float) -> void:
	t += delta
	queue_redraw()
	if t > 40.0:
		print("PROEF fps na 40 s=", Engine.get_frames_per_second())
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
	draw_circle(Vector2(lx, 170), 22.0, Color(1, 0.82, 0.48, 0.25))
	draw_string(ThemeDB.fallback_font, Vector2(20, 100), "Dortus proef: doorzichtig boven de taakbalk, t=%d s" % int(t),
		HORIZONTAL_ALIGNMENT_LEFT, -1, 22, Color.WHITE)
