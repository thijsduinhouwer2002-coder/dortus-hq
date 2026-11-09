# Schetsen TikTok Shop naar Moneybird (Daan, 9 nov 2026).
# Maakt HTML per scherm en zet ze met Playwright om naar PNG in deze map.
# Draaien: python3 maak.py
import pathlib, asyncio
from playwright.async_api import async_playwright

HIER = pathlib.Path(__file__).parent

CSS = r"""
:root{--papier:#F5F3EE;--kaart:#FFFFFF;--inkt:#17161C;--zacht:#6B6875;--lijn:#E4E1DA;
--accent:#4F3BD1;--accent-zacht:#ECE9FF;--goed:#0B6E3F;--goed-zacht:#E3F5EA;
--let:#9A5B00;--let-zacht:#FFF3D6;--fout:#C2261F;--fout-zacht:#FDE8E6}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,system-ui,sans-serif;background:var(--papier);color:var(--inkt);
font-size:15px;line-height:1.45;-webkit-font-smoothing:antialiased}
.num{font-variant-numeric:tabular-nums;font-feature-settings:"tnum"}
.top{display:flex;align-items:center;gap:14px;padding:18px 32px;border-bottom:1px solid var(--lijn);background:var(--kaart)}
.merk{display:flex;align-items:center;gap:10px;font-weight:700;font-size:17px;letter-spacing:-.01em}
.teken{width:30px;height:30px}
.pad{display:flex;align-items:center;gap:8px;margin-left:auto;font-size:13px;color:var(--zacht)}
.pil{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:99px;background:var(--papier);border:1px solid var(--lijn);font-weight:500;color:var(--inkt)}
.stip{width:7px;height:7px;border-radius:50%;background:var(--goed)}
main{padding:36px 32px 48px;max-width:1180px;margin:0 auto}
h1{font-size:28px;letter-spacing:-.02em;line-height:1.15;font-weight:700}
.sub{color:var(--zacht);margin-top:6px;font-size:16px}
.knop{display:inline-flex;align-items:center;gap:8px;border:0;border-radius:10px;padding:11px 18px;font:600 15px Inter;cursor:pointer}
.knop.hoofd{background:var(--accent);color:#fff}
.knop.rustig{background:var(--kaart);color:var(--inkt);border:1px solid var(--lijn)}
/* bon */
.bonnen{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:28px;align-items:start}
.bon{background:var(--kaart);padding:22px 22px 30px;position:relative;
box-shadow:0 1px 0 rgba(0,0,0,.04),0 8px 24px -12px rgba(23,22,28,.18);
-webkit-mask:linear-gradient(#000 0 0) top/100% calc(100% - 10px) no-repeat,
 conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/16px 10px repeat-x}
.bon .kop{display:flex;justify-content:space-between;align-items:baseline;color:var(--zacht);font-size:13px}
.bon .bank{font-size:30px;font-weight:700;letter-spacing:-.02em;margin:6px 0 2px}
.bon .klein{font-size:12.5px;color:var(--zacht)}
.regels{margin:16px 0 0;border-top:1px dashed var(--lijn);padding-top:12px}
.r{display:flex;gap:8px;font-size:14px;padding:3.5px 0}
.r .w{flex:1;display:flex;align-items:baseline;gap:6px;min-width:0}
.r .w:after{content:"";flex:1;border-bottom:1px dotted #CFCBC2;transform:translateY(-4px)}
.r .b{text-align:right;min-width:86px}
.r.min .w{color:var(--zacht)}
.som{display:flex;justify-content:space-between;margin-top:10px;padding-top:10px;border-top:2px solid var(--inkt);font-weight:700;font-size:15px}
.stempel{position:absolute;right:16px;top:58px;transform:rotate(-8deg);border:2.5px solid currentColor;border-radius:8px;
padding:3px 9px;font:800 13px Inter;letter-spacing:.08em;text-transform:uppercase;background:#fff}
.stempel.goed{color:var(--goed)} .stempel.let{color:var(--let)}
.noot{margin-top:14px;background:var(--let-zacht);border-radius:10px;padding:10px 12px;font-size:13.5px;color:#4A3200}
.noot b{color:var(--let)}
.balk{display:flex;align-items:center;gap:14px;margin-top:30px;padding:18px 20px;background:var(--kaart);border:1px solid var(--lijn);border-radius:14px}
.balk .t{flex:1}
.balk .t b{display:block;font-size:15px}
.balk .t span{color:var(--zacht);font-size:14px}
/* tabel */
.kaart{background:var(--kaart);border:1px solid var(--lijn);border-radius:14px}
table{width:100%;border-collapse:collapse}
th{font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--zacht);font-weight:600;text-align:left;padding:12px 18px;border-bottom:1px solid var(--lijn)}
td{padding:14px 18px;border-bottom:1px solid var(--lijn);font-size:14.5px}
tr:last-child td{border-bottom:0}
td.b,th.b{text-align:right}
.status{display:inline-flex;align-items:center;gap:6px;padding:3px 10px;border-radius:99px;font-size:13px;font-weight:600}
.status.goed{background:var(--goed-zacht);color:var(--goed)}
.status.let{background:var(--let-zacht);color:var(--let)}
.status.fout{background:var(--fout-zacht);color:var(--fout)}
.status.wacht{background:var(--accent-zacht);color:var(--accent)}
.tegels{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:24px 0}
.tegel{background:var(--kaart);border:1px solid var(--lijn);border-radius:14px;padding:16px 18px}
.tegel .l{font-size:13px;color:var(--zacht)} .tegel .g{font-size:26px;font-weight:700;letter-spacing:-.02em;margin-top:2px}
.meter{height:6px;border-radius:9px;background:var(--papier);margin-top:10px;overflow:hidden}
.meter i{display:block;height:100%;background:var(--accent);border-radius:9px}
.waarsch{display:flex;align-items:center;gap:12px;padding:12px 16px;border-radius:12px;background:var(--fout-zacht);color:#6E1510;font-size:14.5px;margin-top:18px}
.waarsch .knop{margin-left:auto;padding:7px 14px;font-size:14px;background:var(--fout);color:#fff}
"""

TEKEN = """<svg class="teken" viewBox="0 0 30 30" aria-hidden="true">
<path d="M6 3h18v22l-3-2-3 2-3-2-3 2-3-2-3 2z" fill="#4F3BD1"/>
<path d="M10 9h10M10 13h10" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".55"/>
<path d="M10.5 18.2l2.6 2.5 6-6" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>"""

def top(rechts=None):
    rechts = rechts or '<span class="pil"><span class="stip"></span>TikTok Shop</span> &rarr; <span class="pil"><span class="stip"></span>Moneybird: Studio Lente B.V.</span>'
    return f'<div class="top"><div class="merk">{TEKEN}Klopt</div><div class="pad">{rechts}</div></div>'

def bon(datum, bank, n, regels, som, stempel, noot=""):
    rs = "".join(f'<div class="r{" min" if b.startswith("&minus;") else ""}"><span class="w">{w}</span><span class="b num">{b}</span></div>' for w, b in regels)
    return f'''<div class="bon"><div class="kop"><span>Uitbetaling {datum}</span><span>{n} bestellingen</span></div>
<div class="bank num">{bank}</div><div class="klein">op je bank gekomen</div>{stempel}
<div class="regels">{rs}</div><div class="som"><span>Naar Moneybird</span><span class="num">{som}</span></div>{noot}</div>'''

def proef():
    b1 = bon("6 nov", "&euro; 1.284,60", 42, [("Omzet", "1.512,00"), ("Kortingen", "&minus;96,40"), ("Verzendkosten", "38,50"),
        ("Commissie TikTok", "&minus;151,20"), ("Btw over kosten", "&minus;18,30")], "&euro; 1.284,60", '<span class="stempel goed">Klopt</span>')
    b2 = bon("30 okt", "&euro; 862,15", 29, [("Omzet", "1.006,00"), ("Kortingen", "&minus;58,00"), ("Terugbetaald", "&minus;42,00"),
        ("Verzendkosten", "24,75"), ("Commissie TikTok", "&minus;100,60"), ("Btw over kosten", "&minus;12,00"), ("Apart gezet", "44,00")],
        "&euro; 862,15", '<span class="stempel let">&euro;&nbsp;44 apart</span>',
        '<div class="noot"><b>&euro; 44,00 apart gezet.</b> TikTok telt bij twee bestellingen zelf niet goed op. Wij zetten het verschil op een tussenrekening, je omzet blijft kloppen.</div>')
    b3 = bon("23 okt", "&euro; 1.031,90", 35, [("Omzet", "1.205,00"), ("Kortingen", "&minus;71,10"), ("Verzendkosten", "31,00"),
        ("Commissie TikTok", "&minus;118,40"), ("Btw over kosten", "&minus;14,60")], "&euro; 1.031,90", '<span class="stempel goed">Klopt</span>')
    return top() + f'''<main><h1>Zo boeken wij je uitbetalingen in Moneybird</h1>
<p class="sub">Een proef met je laatste drie. Er gaat nog niets naar Moneybird; straks kies je zelf vanaf welke datum we boeken.</p>
<div class="bonnen">{b1}{b2}{b3}</div>
<div class="balk"><div class="t"><b>Ziet het er goed uit?</b><span>Kies daarna je grootboekrekeningen. Wij stellen ze al voor.</span></div>
<button class="knop rustig">Bekijk per bestelling</button><button class="knop hoofd">Verder naar rekeningen &rarr;</button></div></main>'''

def koppelen():
    blok = lambda naam, kleur, letter, staat, knop: f'''<div class="kaart" style="flex:1;padding:26px;display:flex;flex-direction:column;gap:14px">
<div style="display:flex;align-items:center;gap:12px"><div style="width:44px;height:44px;border-radius:11px;background:{kleur};color:#fff;display:grid;place-items:center;font:800 20px Inter">{letter}</div>
<div><b style="font-size:17px">{naam}</b><div style="color:var(--zacht);font-size:14px">{staat}</div></div></div>{knop}</div>'''
    tt = blok("TikTok Shop", "#17161C", "T", "Studio Lente &middot; gekoppeld", '<span class="status goed" style="align-self:flex-start">&#10003; Klaar</span>')
    mb = blok("Moneybird", "#1E6FD9", "M", "Je boekhouding", '<button class="knop hoofd" style="align-self:flex-start">Koppel Moneybird</button>')
    return top('<span class="pil">Stap 1 van 3</span>') + f'''<main style="max-width:860px"><h1>Koppel je boekhouding</h1>
<p class="sub">Daarna zie je meteen hoe je laatste uitbetalingen geboekt worden. Er gaat nog niets naar Moneybird.</p>
<div style="display:flex;gap:18px;margin-top:28px;align-items:stretch">{tt}<div style="align-self:center;font-size:22px;color:var(--zacht)">&rarr;</div>{mb}</div>
<p style="margin-top:22px;color:var(--zacht);font-size:14px">Geen Moneybird? <a href="#" style="color:var(--accent);font-weight:600">Zet je op de wachtlijst voor Exact</a></p></main>'''

def overzicht():
    rij = lambda d, b, n, s, sk: f'<tr><td>{d}</td><td class="b num"><b>{b}</b></td><td class="b num">{n}</td><td><span class="status {sk}">{s}</span></td><td class="b" style="color:var(--accent);font-weight:600">Bekijk</td></tr>'
    rows = (rij("6 nov", "&euro; 1.284,60", 42, "Wacht op koppeling", "wacht")
          + rij("30 okt", "&euro; 862,15", 29, "Geboekt, &euro; 44 apart", "let")
          + rij("23 okt", "&euro; 1.031,90", 35, "&#10003; Geboekt", "goed")
          + rij("16 okt", "&euro; 1.122,40", 38, "&#10003; Geboekt", "goed")
          + rij("9 okt", "&euro; 948,00", 31, "Moneybird weigerde", "fout"))
    kop = '<span class="pil"><span class="stip"></span>TikTok Shop</span> &rarr; <span class="pil"><span class="stip" style="background:var(--fout)"></span>Moneybird: verlopen</span>'
    return top(kop) + f'''<main><div style="display:flex;align-items:flex-end;gap:16px"><div><h1>Uitbetalingen</h1>
<p class="sub">Laatst bijgewerkt vandaag 09:12. Boeken staat stil tot je Moneybird opnieuw koppelt.</p></div>
<button class="knop rustig" style="margin-left:auto">Instellingen</button></div>
<div class="waarsch"><b>Koppeling met Moneybird verlopen.</b> Boeken staat stil, er gaat niets verloren.<button class="knop">Opnieuw koppelen</button></div>
<div class="tegels"><div class="tegel"><div class="l">Op je bank in november</div><div class="g num">&euro; 1.284,60</div></div>
<div class="tegel"><div class="l">Apart gezet, alles open</div><div class="g num">&euro; 44,00</div></div>
<div class="tegel"><div class="l">Gratis bestellingen deze maand</div><div class="g num">42 van 30</div><div class="meter"><i style="width:100%"></i></div>
<a href="#" style="display:inline-block;margin-top:8px;font-size:13.5px;color:var(--accent);font-weight:600">Abonnement nemen, &euro; 15 per maand</a></div></div>
<div class="kaart"><table><tr><th>Datum</th><th class="b">Op je bank</th><th class="b">Bestellingen</th><th>Status</th><th></th></tr>{rows}</table></div></main>'''

def staten():
    vak = lambda inhoud: f'<div class="kaart" style="padding:34px 26px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:10px;min-height:270px;justify-content:center">{inhoud}</div>'
    groot = TEKEN.replace('class="teken"', 'style="width:56px;height:56px"')
    leeg = vak(f'{groot}<b style="font-size:17px">Nog geen uitbetalingen</b><span style="color:var(--zacht);font-size:14px;max-width:260px">Zodra TikTok iets uitbetaalt, staat het hier.</span>')
    laden = vak('''<div style="width:220px"><div style="height:8px;border-radius:9px;background:var(--papier);overflow:hidden"><i style="display:block;width:55%;height:100%;background:var(--accent)"></i></div></div>
<b style="font-size:17px">Uitbetalingen ophalen</b><span style="color:var(--zacht);font-size:14px">2 van 3 opgehaald. Dit duurt meestal minder dan een minuut.</span>''')
    fout = vak('''<div style="width:52px;height:52px;border-radius:50%;background:var(--fout-zacht);color:var(--fout);display:grid;place-items:center;font:800 24px Inter">!</div>
<b style="font-size:17px">TikTok gaf geen antwoord</b><span style="color:var(--zacht);font-size:14px;max-width:260px">Dat ligt niet aan jou. We proberen het over 5 minuten vanzelf opnieuw.</span><button class="knop rustig">Nu opnieuw proberen</button>''')
    niet = vak('''<div style="width:52px;height:52px;border-radius:50%;background:var(--accent-zacht);color:var(--accent);display:grid;place-items:center;font:800 16px Inter">NL</div><b style="font-size:17px">Nu alleen voor Nederlandse winkels</b>
<span style="color:var(--zacht);font-size:14px;max-width:260px">We breiden uit per land. Laat je e-mail achter, dan hoor je het als het voor jou werkt.</span><button class="knop hoofd">Zet me op de wachtlijst</button>''')
    kopv = bon("16 okt", "&euro; 948,00", 31, [("Omzet", "1.110,00"), ("Kortingen", "&minus;64,00"), ("Verzendkosten", "28,00"),
        ("Commissie TikTok", "&minus;110,00"), ("Btw over kosten", "&minus;13,20")], "&euro; 950,80", '<span class="stempel let">&euro;&nbsp;2,80 open</span>',
        '<div class="r" style="color:var(--let);font-weight:600;margin-top:6px"><span class="w">Open, niet geboekt</span><span class="b num">&minus;2,80</span></div>'
        '<div class="noot"><b>&euro; 2,80 niet geboekt.</b> Bij bestelling 5770&hellip;21 telt TikTok&rsquo;s totaal anders op dan de regels. Kijk het na in Seller Center; wij boeken alleen wat we kunnen verklaren.</div>')
    return top() + f'''<main><h1>Lege staat, laden, fout en "nog niet voor jou"</h1>
<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin-top:24px">{leeg}{laden}{fout}{niet}</div>
<h1 style="margin-top:40px;font-size:22px">Verschil op bestellingniveau (niet geboekt)</h1>
<div class="bonnen" style="grid-template-columns:repeat(3,1fr)">{kopv}</div></main>'''

def mobiel():
    return proef().replace('grid-template-columns:repeat(3,1fr)', '')

SCHERMEN = [("1-koppelen", koppelen, 1280), ("2-proef", proef, 1280), ("3-overzicht", overzicht, 1280),
            ("4-staten", staten, 1280), ("5-proef-telefoon", proef, 390)]

async def main():
    async with async_playwright() as p:
        br = await p.chromium.launch()
        for naam, f, breed in SCHERMEN:
            css = CSS
            if breed < 600:
                css += ".bonnen{grid-template-columns:1fr}main{padding:22px 16px}.top{padding:14px 16px}.pad{display:none}h1{font-size:23px}.balk{flex-direction:column;align-items:stretch}.balk .knop{justify-content:center}"
            html = f'<!doctype html><html lang="nl"><meta charset="utf-8"><style>{css}</style><body>{f()}</body></html>'
            (HIER / f"{naam}.html").write_text(html)
            pg = await br.new_page(viewport={"width": breed, "height": 800}, device_scale_factor=1)
            await pg.set_content(html)
            await pg.screenshot(path=str(HIER / f"{naam}.png"), full_page=True)
            await pg.close()
        await br.close()

asyncio.run(main())
