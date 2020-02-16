from klasy.Mag import Mag
from klasy.Barb import Barb

xav = Mag(imie='Xav', sila=1, zrecznosc=1, inteligencja=9, mana=25, zdrowie=20)
bob = Barb(imie='Bob', sila=9, zrecznosc=5, inteligencja=1, mana=50, zdrowie=90)

bob.wydaj_okrzyk()
xav.rzuc_kule_ognia(bob)
bob.uderz_piescia(xav)
