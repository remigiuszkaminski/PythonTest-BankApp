import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, rabat = ''):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        self.couponApplication(rabat)


    def couponApplication(self, rabat):
        if (len(rabat) == 8 and re.match(r'^PROM_', rabat) != None and (int(self.pesel[0:2]) > 60) or (int(self.pesel[3:4]) > 20) and (int(self.pesel[0:2]) < 60)): 
            validity = True
        else:
            validity = False

        if validity:
            self.saldo = 50
        else:
            self.saldo = 0