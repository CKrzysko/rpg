from .Postac import Postac

class Barb(Postac):
    def uderz_piescia(self, target):
        print(self.imie+' uderza piescia w '+str(target.imie))
        obrazenia = self.sila + self.zrecznosc
        self.zabierz_zycie(obrazenia)

    def wydaj_okrzyk(self):
        koszt_many=10
        okrzyk = self.pobierz_mane(koszt_many)
        if okrzyk:
            self.sila = self.sila + 5
            print(self.imie + ": Okrzyk bojowy dal +" + str(5) + " do sily." + ' Teraz ma lacznie '+ str(self.sila) + ' sily.')
        else:
            pass