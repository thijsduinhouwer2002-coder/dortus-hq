# Sem, 16 nov 2026: soort contactadres per kanaal uit de openbare kanaaltekst. Schrijft nooit het adres zelf op, alleen het domein als het een eigen domein of bureau is.
# Gebruik: printf "nr\t/@handle\n" | python3 contact.py  (vanuit deze map)
import sys, json, re, time, csv
sys.path.insert(0,'.')
from importlib import import_module
yk = import_module('yt-kanaal')
lst = [l.split('\t') for l in sys.stdin.read().strip().split('\n')]
w = csv.writer(sys.stdout)
w.writerow(['nr','handle','abonnees','soort_adres','domein','zakelijk_knop'])
GRAT = ('gmail.','hotmail.','outlook.','yahoo.','icloud.','proton','live.','naver.','qq.com','163.com','gmx.')
for nr,h in lst:
    d = yk.kanaal(h)
    soort, dom = 'geen in tekst', ''
    for m in d['mail_in_beschrijving']:
        dm = m.split('@')[1].lower()
        if dm.startswith(GRAT): s='gratis adres (niet overnemen)'
        else: s='eigen domein of bureau'
        if soort!='eigen domein of bureau': soort, dom = s, ('' if s.startswith('gratis') else dm)
    w.writerow([nr,h,d['abonnees'],soort,dom,d['zakelijk_knop']])
    time.sleep(1)
