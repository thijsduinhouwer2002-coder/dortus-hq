# Joris, run 34. Zoekbalk in andere talen (hl=pt-BR, de, es, fr, nl) voor Google Foto s, Agenda en Pinterest.
import subprocess,re,json,time,urllib.parse,sys
sys.path.insert(0,'/home/claude/dortus-hq/platformen/succes/data')
exec(open('/home/claude/dortus-hq/platformen/succes/data/chrome-zoekplek-haal.py').read().split('if len(sys.argv)')[0].split('Q = """')[0])
def haal(url): return subprocess.run(['curl','-sS','-L','-m','30','-A','Mozilla/5.0',url],capture_output=True,text=True).stdout
exec('def recs(h):'+open('/home/claude/dortus-hq/platformen/succes/data/chrome-zoekplek-haal.py').read().split('def recs(h):')[1].split('if len(sys.argv)')[0])
T=[('pt-BR','excluir fotos google fotos em massa'),('de','google fotos massenbearbeitung'),('pt-BR','excluir eventos google agenda'),('de','google kalender termine löschen'),('es','eliminar eventos google calendar'),('fr','supprimer événements google agenda'),('nl','google agenda afspraken verwijderen'),('pt-BR','estatísticas pinterest')]
for hl,q in T:
  rs=recs(haal('https://chromewebstore.google.com/search/'+urllib.parse.quote(q)+'?hl='+hl))
  print('==',hl,q,len(rs))
  for i,r in enumerate(rs[:6],1): print(' ',i,r[0][:6],r[14],'|',r[2][:85])
  time.sleep(1.3)
