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