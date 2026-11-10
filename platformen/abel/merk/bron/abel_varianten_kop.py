# Abel: variant van Mila's kop met de deur op x=950 (zie merk/voor-mila.md). Leest maak_uniform.py uit dezelfde map en schrijft hiernaast; daarna PNG handmatig naar merk/ kopieren.
import os
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'maak_uniform.py')).read().split('if __name__')[0]
src=src.replace('os.path.dirname(os.path.abspath(__file__)) + "/.."', repr(os.path.dirname(os.path.abspath(__file__))))
exec(src)
schrijf('steam-kop-1500x220-v1b',1500,220,kamer(1500,220,950,24,0.27))
