class RejestrKont:

    Accounts = []

    @classmethod
    def addAccToArray(cls, account):
        cls.Accounts.append(account)
    @classmethod
    def searchByPesel(cls, pesel):
        return next((x for x in cls.Accounts if x.pesel == pesel), None)
    @classmethod
    def giveLengthOfArr(cls):
        return len(cls.Accounts)

    @classmethod
    def updateAcc(cls, pesel, dane):
        if(cls.searchByPesel(pesel) != None):
            konto=cls.searchByPesel(pesel)
            konto.imie=dane['imie'] if 'imie' in dane else konto.imie
            konto.nazwisko=dane['nazwisko'] if 'nazwisko' in dane else konto.nazwisko
            konto.pesel=dane['pesel'] if 'pesel' in dane else konto.pesel
            konto.saldo=dane['saldo'] if 'saldo' in dane else konto.saldo
            return konto
        else:
            return None

    @classmethod
    def accRemove(cls, pesel):
        if(cls.searchByPesel(pesel) != None):
            cls.Accounts = [
                x for x in cls.Accounts if x.pesel != pesel
            ]
            return "Usunieto uzytkownika o danym pesel"
        else:
            return None
                