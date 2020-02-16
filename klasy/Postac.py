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