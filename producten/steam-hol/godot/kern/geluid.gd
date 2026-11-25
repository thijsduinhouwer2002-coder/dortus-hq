extends Node
# Het Hol: de geluidjes echt afspelen (Sanne 25 nov 2026, issue #19, keuring Iris build f6aa9b6 punt 3: "een klap zonder
# tok voelt half"). Mila maakte de wav's op 10 nov (geluid/LEESMIJ.md), maar geen script speelde ze af: de knop Sound in
# het systeemvak zette dus niets aan of uit.
# - Kind van de strook (kern/venster.gd lagen). Afspelen via speel("val"), speel("munt"), ...
# - Zacht: -6 dB, en hooguit één munt per 0,12 s (voorstel Mila), anders wordt het geratel.
# - Uit via Sound in het systeemvak: dat dempt bus 0 (kern/systeemvak.gd), dus ook dit.
# - Rekent niets als er niets klinkt: alleen een paar spelers die klaarstaan.

const BESTAND := {
	"val": preload("res://geluid/val.wav"),
	"munt": preload("res://geluid/munt.wav"),
	"hap": preload("res://geluid/hap.wav"),
	"koop": preload("res://geluid/koop.wav"),
	"poef": preload("res://geluid/poef.wav"),
	"lied": preload("res://geluid/lied.wav"),
}
const VOLUME_DB := -6.0
const MUNT_GAT := 0.12      # seconden tussen twee munten
const MUNT_NA_KLAP := 0.18  # de munt komt net na de plof, zodat je ze apart hoort
const SPELERS := 4

var spelers: Array = []
var t := 0.0
var laatste := {}           # naam -> tijd waarop hij voor het laatst klonk
var wacht: Array = []       # [tijd, naam]: geluid dat zo meteen komt (munt na de klap)
var gespeeld: Array = []    # namen die echt klonken (voor de toets; hooguit 20)

func _ready() -> void:
	for i in SPELERS:
		var p := AudioStreamPlayer.new()
		p.volume_db = VOLUME_DB
		add_child(p)
		spelers.append(p)
	set_process(false)

# Mag dit geluid nu? Alleen de munt heeft een gat; de rest klinkt altijd.
static func mag(naam: String, nu: float, vorige) -> bool:
	if naam != "munt" or vorige == null:
		return true
	return nu - float(vorige) >= MUNT_GAT

func speel(naam: String) -> void:
	if not BESTAND.has(naam):
		return
	if not mag(naam, t, laatste.get(naam)):
		return
	laatste[naam] = t
	var p: AudioStreamPlayer = null
	for q in spelers:
		if not q.playing:
			p = q
			break
	if p == null:
		p = spelers[0]   # alles bezet: de oudste maakt plaats
	p.stream = BESTAND[naam]
	p.play()
	gespeeld.append(naam)
	if gespeeld.size() > 20:
		gespeeld.pop_front()

# Een vangst: plof (of hap als Gloop hem opat), en net daarna de munt.
func vangst(hap: bool) -> void:
	speel("hap" if hap else "val")
	wacht.append([t + MUNT_NA_KLAP, "munt"])
	set_process(true)

func _process(delta: float) -> void:
	t += delta
	var nog: Array = []
	for w in wacht:
		if t >= float(w[0]):
			speel(String(w[1]))
		else:
			nog.append(w)
	wacht = nog
	if wacht.is_empty():
		set_process(false)
