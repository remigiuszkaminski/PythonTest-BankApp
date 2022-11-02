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
    

    def ksiegowanie_wychodzacego(self, kwota):
        if(self.saldo >= kwota and kwota > 0):
            self.saldo = self.saldo - kwota
        else:
            self.saldo = self.saldo
    
    def ksiegowanie_przychodzacego(self, kwota):
        if(kwota > 0):
            self.saldo = self.saldo + kwota
        else:
            self.saldo = self.saldo
    
    def ksiegowanie_ekspresowego(self, kwota):
        try:
            self.imie

            if(self.saldo >= kwota and kwota > 0):
                self.saldo = self.saldo - kwota - 1
            else:
                self.saldo = self.saldo
        except AttributeError:
            if(self.saldo >= kwota and kwota > 0):
                self.saldo = self.saldo - kwota - 5
            else:
                self.saldo = self.saldo

class KontoFirmowe(Konto):
    def __init__(self, nazwafirmy, NIP):
        self.nazwafirmy = nazwafirmy
        self.NIP = NIP
        self.saldo = 0
    

