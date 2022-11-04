import unittest

from ..Konto import Konto
from ..Konto import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):
    imie = 'darek'
    nazwisko = 'janusz'
    pesel = '99922333555'
    rabat = 'PROM_OMX'

    nazwafirmy = 'Pankracy i fajtłacy'
    NIP = '9988776655'
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, "Januszewski", '94320943890890432')
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, '94320943890890432', 'Brak numeru pesel')

    
    #tutaj proszę dodawać nowe testy
    def test_dlugosc_pesel(self):
        drugie_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(len(drugie_konto.pesel), len('11111111111'), 'Niepoprawny pesel!')
    def test_rabat(self):
        drugie_konto = Konto(self.imie, self.nazwisko, self.pesel, self.rabat)
        self.assertEqual(drugie_konto.saldo, 50, 'Pomimo poprawnego kodu rabatowego saldo początkowe wynosi nie wynosi 50')
        drugie_konto = Konto(self.imie, self.nazwisko, self.pesel, 'PRMM_XYZ')
        self.assertEqual(drugie_konto.saldo, 0, 'Pomimo zaaplikowania złego kuponu saldo nie równa się 0')
        drugie_konto = Konto(self.imie, self.nazwisko, self.pesel )
        self.assertEqual(drugie_konto.saldo, 0, 'Pomimo zaaplikowania pustego kuponu saldo nie równa się 0')
        drugie_konto = Konto(self.imie, self.nazwisko, self.pesel, 'XYZPROM_')
        self.assertEqual(drugie_konto.saldo, 0, 'Pomimo zaaplikowania złego kuponu saldo nie równa się 0')
    def test_rabat_wiek(self):
        drugie_konto = Konto(self.imie, self.nazwisko, self.pesel, self.rabat)
        self.assertEqual(drugie_konto.saldo, 50, 'Pomimo bycia rocznikiem 1960+ saldo nie równa się 50')
        drugie_konto = Konto(self.imie, self.nazwisko, '59123456789', 'PROM_XYZ')
        self.assertEqual(drugie_konto.saldo, 0, 'Pomimo bycia rocznikiem 1960- saldo nie równa się 0')
        drugie_konto = Konto(self.imie, self.nazwisko, '02223456789', 'PROM_XYZ')
        self.assertEqual(drugie_konto.saldo, 0, 'Pomimo bycia rocznikiem 1960+ saldo nie równa się 50')

    def test_tworzenie_konta_firmowego(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        self.assertEqual(konto.nazwafirmy, self.nazwafirmy, 'Nazwa firmy nie została zapisana!')
        self.assertEqual(konto.NIP, self.NIP, 'NIP nie został zapisany!')

    def test_podanie_poprawnego_NIP(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        self.assertEqual(len(konto.NIP), len('1234567891'), 'Niepoprawny NIP')



        