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


    def test_1_dodanie_konta_do_listy(self):
        konto=Konto(self.imie, self.nazwisko, self.pesel)
        konto2=Konto(self.imie, self.nazwisko, '12345678901')
        RejestrKont.addAccToArray(konto)
        RejestrKont.addAccToArray(konto2)
        self.assertEqual(RejestrKont.giveLengthOfArr(), 3, 'Nie zgadza sie liczba kont bo powinny byc 3')

    def test_2_wyszukiwanie_za_pomoca_peselu(self):
        konto=Konto(self.imie,self.nazwisko,'12312312366')
        RejestrKont.addAccToArray(konto)
        self.assertEqual(RejestrKont.searchByPesel('12312312366'), konto, 'nie wyszukalo danego konta mimo podanego numeru pesel :(')

    def test_3_brak_danego_numeru_pesel(self):
        self.assertEqual(RejestrKont.searchByPesel('12312312377'), None, 'Nie ma takiego numeru pesel, a nie zostalo zwrocone Nic')

    def test_4_aktualizacja_konta(self):
        konto = Konto(self.imie, self.nazwisko, '33445566778')
        RejestrKont.addAccToArray(konto)
        zapdejtowane = {
            "imie": "Dzialaj",
            "nazwisko": "Prosze",
            "saldo": 234
        }
        self.assertEqual(RejestrKont.updateAcc('33445566778', zapdejtowane), RejestrKont.searchByPesel('33445566778'), 'Dane nie sa takie same, czyli nie poszla aktualizacja')

    def test_5_aktualizacja_z_bledem(self):
        konto = Konto(self.imie, self.nazwisko, '33445566772')
        RejestrKont.addAccToArray(konto)
        zapdejtowane = {
            "imie": "Dzialaj",
            "nazwisko": "Prosze",
            "saldo": 234
        }
        self.assertEqual(RejestrKont.updateAcc('33445533372', zapdejtowane), None, 'Pesel nie istnieje, wiec nie powinno nic zmienic a zwrocic none')

    def test_6_usuwanie_konta(self):
        konto = Konto(self.imie, self.nazwisko, '33445566799')
        RejestrKont.addAccToArray(konto)
        dlugosc_przed_usunieciem = RejestrKont.giveLengthOfArr()
        RejestrKont.accRemove('33445566799')
        self.assertEqual(RejestrKont.searchByPesel('33445566799'), None, 'Nie usunieto uzytkownika mimo podanego numeru pesel, gdyz nadal znajduje konto o tym numerze pesel')
        self.assertEqual(RejestrKont.giveLengthOfArr(), dlugosc_przed_usunieciem - 1, "Dlugosc nie zmienila sie mimo ze konto zostalo usuniete, czyli w sumie nie zostalo")

    def test_7_usuwanie_z_blednym_pesel(self):
        dlugosc_przed_usunieciem = RejestrKont.giveLengthOfArr()
        self.assertEqual(RejestrKont.accRemove('33445533339'), None, 'Pesel nie istnieje, wiec nie powinno nic usunac a zwrocic none')
        self.assertEqual(RejestrKont.giveLengthOfArr(), dlugosc_przed_usunieciem, "Dlugosc nie powinna ulec zmianie")

    @classmethod
    def tearDownClass(cls):
        RejestrKont.Accounts=[]
    
        