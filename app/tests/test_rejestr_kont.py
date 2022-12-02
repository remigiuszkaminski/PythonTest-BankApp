import unittest

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestRejestrKont(unittest.TestCase):
    imie = 'TaiLung'
    nazwisko = 'KungFuPanda'
    pesel = '11223344556'

    @classmethod
    def setUpClass(cls):
        konto=Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.addAccToArray(konto)


    def test_dodanie_konta_do_listy(self):
        konto=Konto(self.imie, self.nazwisko, self.pesel)
        konto2=Konto(self.imie, self.nazwisko, '12345678901')
        RejestrKont.addAccToArray(konto)
        RejestrKont.addAccToArray(konto2)
        self.assertEqual(RejestrKont.giveLengthOfArr(), 3, 'Nie zgadza sie liczba kont bo powinny byc 3')

    def test_wyszukiwanie_za_pomoca_peselu(self):
        konto=Konto(self.imie,self.nazwisko,'12312312366')
        RejestrKont.addAccToArray(konto)
        self.assertEqual(RejestrKont.searchByPesel('12312312366'), konto, 'nie wyszukalo danego konta mimo podanego numeru pesel :(')

    def test_brak_danego_numeru_pesel(self):
        self.assertEqual(RejestrKont.searchByPesel('12312312377'), None, 'Nie ma takiego numeru pesel, a nie zostalo zwrocone Nic')

    @classmethod
    def tearDownClass(cls):
        RejestrKont.Accounts=[]
    
        