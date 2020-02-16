from .Postac import Postac

class Mag(Postac):
    def uderz_piescia(self, target=None):
        if target == None:
            print(self.imie+' uderza w powietrze.')
        else:
            print(self.imie + ' nie moge tego zrobic')
            print(target.imie + "owi zostaje " + str(target.zdrowie) + " hp " )

    def rzuc_kule_ognia(self, target):
        #info co sie dzieje
        print(self.imie + " rzuca kula ognia w " + str(target.imie))
        # logika czaru
        koszt_many = self.sila + self.inteligencja
        obrazenia = self.inteligencja+self.mana
        # rzucanie czaru
        self.rzuc_czar(koszt_many, obrazenia, target)

    def rzuc_porazenie(self, target):
        #info co sie dzieje
        print(self.imie + " rzuca porazenie w " + str(target.imie))
        #logika czaru
        koszt_many = 10
        obrazenia = int(self.inteligencja * 1.2)
        # rzucanie czaru
        self.rzuc_czar(koszt_many, obrazenia, target)