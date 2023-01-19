import re
import requests
import os
from datetime import date
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
        self.sprawdz_nip(NIP)
        self.saldo = 0
        self.history = []


    def pobierz_nip(self, NIP):
        dzis = date.today().strftime("%Y-%m-%d")
        response = requests.get(
                f"{os.environ.get('BANK_APP_MF_URL')}/api/search/nip/{NIP}?date={dzis}"
                )
        if (response.status_code == 200):
            return True
        else:
            return False
        
    def sprawdz_nip(self, NIP):
        if(len(NIP) == 10 and NIP.isdigit()):
            if (self.pobierz_nip(NIP)):
                self.NIP = NIP
            else:
                self.NIP = 'PRANIE'
        else:
            self.NIP = 'Niepoprawny NIP'
    
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
        
        

