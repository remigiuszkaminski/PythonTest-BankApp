import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, rabat = ''):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        self.history = []
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
            self.history.append(-kwota)
        else:
            self.saldo = self.saldo
    
    def ksiegowanie_przychodzacego(self, kwota):
        if(kwota > 0):
            self.saldo = self.saldo + kwota
            self.history.append(kwota)
        else:
            self.saldo = self.saldo
    
    def ksiegowanie_ekspresowego(self, kwota):
            if(self.saldo >= kwota and kwota > 0):
                self.saldo = self.saldo - kwota - 1
                self.history.append(-kwota-1)
            else:
                self.saldo = self.saldo

    def zaciagnij_kredyt(self, kwota):
        last_3 = self.history[-3:]
        last_5 = sum(self.history[-5:])
        test = True
        for x in last_3:
            if(x < 0):
                test = False
                return False
        if((last_5>kwota) and (test)):
            self.saldo = self.saldo + kwota
            return True
        else:
            return False

    

            

class KontoFirmowe(Konto):
    def __init__(self, nazwafirmy, NIP):
        self.nazwafirmy = nazwafirmy
        self.NIP = NIP
        self.saldo = 0
        self.history = []
    def ksiegowanie_ekspresowego(self, kwota):
        if(self.saldo >= kwota and kwota > 0):
            self.saldo = self.saldo - kwota - 5
            self.history.append(-kwota-5)
        else:
            self.saldo = self.saldo
    def zaciagnij_kredyt(self, kwota):
        test = True
        if(2 * kwota <= self.saldo):
            test = True
        else:
            test = False
        if -1775 not in self.history:
            test = False
        if((test)):
            self.saldo = self.saldo + kwota
            return True
        else:
            return False 

