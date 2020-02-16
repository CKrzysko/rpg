class Postac:
    def __init__(self, imie, sila, zrecznosc, inteligencja, mana, zdrowie):
        self.imie = imie
        self.sila = sila
        self.zrecznosc = zrecznosc
        self.inteligencja = inteligencja
        self.mana = mana
        self.zdrowie = zdrowie
        self.zyje = True

    def pobierz_mane(self, koszt_many):
        if self.mana < koszt_many:
            print(self.imie + " ma za mało many.")
            return False
        print(self.imie + " uzywa", koszt_many, "many.", "Zostaje mu", self.mana, "many")
        self.mana = self.mana - koszt_many
        return True

    def rzuc_czar(self, koszt_many, obrazenia, target):
        czy_moge = self.pobierz_mane(koszt_many)
        if czy_moge:
            target.zabierz_zycie(obrazenia)
        else:
            pass



    def zabierz_zycie(self, obrazenia):
        if self.mana >0:
            self.zdrowie = self.zdrowie - obrazenia
            print(self.imie + " traci", obrazenia, "hp" '. Zostaje mu', self.zdrowie, "hp")
        elif self.zdrowie<0:
            self.zyje = False
            print(self.imie+" nie zyje.")



    def uderz_piescia(self, target):
        print(self.imie+' uderza piescia w '+target.imie)
        mana = self.sila + self.inteligencja
        obrazenia = self.sila + self.zrecznosc
        target.zabierz_zycie(self.sila)



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


xav = Mag(imie='Xav', sila=1, zrecznosc=1, inteligencja=9, mana=25, zdrowie=20)
bob = Barb(imie='Bob', sila=9, zrecznosc=5, inteligencja=1, mana=50, zdrowie=90)



