"""Update-video "Click Joints Pro 1.2 is here: what's new" (Chris, 24 nov 2026).

Bouwt uit bestaande, gekeurde beelden een liggende video van ±60 s:
titel, per nieuwigheid één beeld met onderschrift, eindkaart met de koplink.
Geen nieuwe opname, geen AI-beeld, geen stem. Draaien vanuit deze map:
    python3 maak.py
Uitvoer: update-1.2-concept.mp4 (zonder geluid; geluid via filmpjes/geluid/geluid.py als Daan ja zegt).
"""
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

HIER = Path(__file__).parent
BRON = HIER / "bron"
UIT = HIER / "werk"
UIT.mkdir(exist_ok=True)
PRO = HIER.parent / "pro-uitleg"
F = "/usr/share/fonts/opentype/inter/"
B, S, R = F + "Inter-Bold.otf", F + "Inter-SemiBold.otf", F + "Inter-Regular.otf"
W, H = 1920, 1080


def kaart(naam, kop, onder=None, achter=None, dim=0.25):
    if achter:
        im = Image.open(achter).convert("RGB").resize((W, H))
        im = ImageEnhance.Brightness(im).enhance(dim)
    else:
        im = Image.new("RGB", (W, H), (22, 24, 28))
    d = ImageDraw.Draw(im)
    fk = ImageFont.truetype(B, 92)
    y = 400 if onder else 470
    for regel in kop.split("\n"):
        w = d.textlength(regel, font=fk)
        d.text(((W - w) / 2, y), regel, font=fk, fill=(255, 255, 255))
        y += 112
    if onder:
        fo = ImageFont.truetype(R, 46)
        for regel in onder.split("\n"):
            w = d.textlength(regel, font=fo)
            d.text(((W - w) / 2, y + 30), regel, font=fo, fill=(200, 230, 210))
            y += 62
    p = UIT / f"{naam}.png"
    im.save(p)
    return p


def balk(naam, beeld, tekst):
    """Beeld met een donkere balk onderaan en één regel tekst."""
    im = Image.open(beeld).convert("RGB").resize((W, H))
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle([0, H - 150, W, H], fill=(0, 0, 0, 200))
    f = ImageFont.truetype(S, 54)
    w = d.textlength(tekst, font=f)
    d.text(((W - w) / 2, H - 112), tekst, font=f, fill=(255, 255, 255))
    p = UIT / f"{naam}.png"
    im.save(p)
    return p


def still(png, sec, uit):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-t", str(sec), "-i", str(png),
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-crf", "20", str(uit)], check=True)


def clip(bron, tekst, uit, start=0, dur=None):
    """Bestaande clip met dezelfde onderbalk als de stills."""
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    d.rectangle([0, H - 150, W, H], fill=(0, 0, 0, 200))
    f = ImageFont.truetype(S, 54)
    w = d.textlength(tekst, font=f)
    d.text(((W - w) / 2, H - 112), tekst, font=f, fill=(255, 255, 255))
    op = UIT / (Path(uit).stem + "-balk.png")
    over.save(op)
    cmd = ["ffmpeg", "-y", "-v", "error", "-ss", str(start)]
    if dur:
        cmd += ["-t", str(dur)]
    # De clips uit pro-uitleg hebben al hun eigen tekst links en onderaan: geen balk erover.
    cmd += ["-i", str(bron), "-vf", "scale=1920:1080,fps=30,format=yuv420p",
            "-an", "-c:v", "libx264", "-crf", "20", str(uit)]
    subprocess.run(cmd, check=True)


delen = []
def voeg(p):
    delen.append(p)

s = UIT / "s"
still(kaart("01-titel", "Click Joints Pro 1.2 is here", "What's new, in one minute",
            BRON / "held-3-voor-na.png", 0.3), 4, f"{s}01.mp4"); voeg(f"{s}01.mp4")
still(balk("02-enkels", BRON / "w1-figuur.png",
           "\"More bones\": ankles too, 0 to 90 degrees (Blender 5.2+)"), 7, f"{s}02.mp4"); voeg(f"{s}02.mp4")
still(kaart("03-shift", "Shift + right click\non the skin",
            "now works with Knee, Elbow, Ankle and the hinge buttons"), 5, f"{s}03.mp4"); voeg(f"{s}03.mp4")
still(kaart("04-reden", "Clearer messages",
            "When a joint cannot be cut, the list shows the real reason\nand what you can do"), 5, f"{s}04.mp4"); voeg(f"{s}04.mp4")
clip(PRO / "2-fit-test.mp4", "Fit test strip: print this first", f"{s}05.mp4"); voeg(f"{s}05.mp4")
still(balk("06-strip", BRON / "w3-testkaart.png",
           "Five clearances, 0.10 to 0.30 mm, each with its number"), 5, f"{s}06.mp4"); voeg(f"{s}06.mp4")
clip(PRO / "1-figure-from-rig.mp4", "Figure from rig: one button, a poseable figure", f"{s}07.mp4", 0, 16)
voeg(f"{s}07.mp4")
still(kaart("08-eind", "Get Click Joints Pro", "dortus.com/yt\nEvery 1.x update is free",
            BRON / "held-3-voor-na.png", 0.3), 6, f"{s}08.mp4"); voeg(f"{s}08.mp4")

lijst = UIT / "lijst.txt"
lijst.write_text("".join(f"file '{Path(p).resolve()}'\n" for p in delen))
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lijst),
                "-c:v", "libx264", "-crf", "21", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                str(HIER / "update-1.2-concept.mp4")], check=True)
print("klaar:", HIER / "update-1.2-concept.mp4")
