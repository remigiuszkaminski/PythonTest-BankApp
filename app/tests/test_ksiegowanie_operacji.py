import unittest

from ..Konto import Konto
from ..Konto import KontoFirmowe



class TestSendingAndReceivingMoney(unittest.TestCase):
    imie = 'TaiLung'
    nazwisko = 'KungFuPanda'
    pesel = '11223344556'
    rabat = 'PROM_SIX'
    nazwafirmy = 'KungFuTajluuung'
    NIP = '1234567891'
    def test_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 900
        konto.ksiegowanie_przychodzacego(200)
        self.assertEqual(konto.saldo, 900+200, 'Saldo nie jest równe wartosci oczekiwanej po zaksiegowaniu przelewu przychodzacego')
    def test_przelew_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 900
        konto.ksiegowanie_wychodzacego(200)
        self.assertEqual(konto.saldo, 900-200, 'Saldo nie jest równe wartości oczekiwanej po zaksięgowaniu przelewu')
    def test_brak_pieniedzy_na_przelew(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 900
        konto.ksiegowanie_wychodzacego(1000)
        self.assertEqual(konto.saldo, 900, 'Saldo nie jest takie samo mimo podanej zbyt dużej kwoty przelewu')
    def test_proba_przelewu_ujemnego(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 900
        konto.ksiegowanie_przychodzacego(-1000)
        self.assertEqual(konto.saldo, 900, 'Saldo nie jest takie samo mimo podanej ujemnej kwoty przelewu')

    def test_przelew_przychodzacy_firma(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 900
        konto.ksiegowanie_przychodzacego(900)
        self.assertEqual(konto.saldo, 900+900, 'Saldo nie jest rowne wartosci oczekiwanej')
    def test_przelew_wychodzacy_firma(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 900
        konto.ksiegowanie_wychodzacego(300)
        self.assertEqual(konto.saldo, 900-300, 'Saldo nie jest rowne wartosci oczekiwanej')
    def test_przelew_wychodzacy_zerowanie_firma(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 900
        konto.ksiegowanie_wychodzacego(900)
        self.assertEqual(konto.saldo, 900-900, 'Saldo nie jest rowne wartosci oczekiwanej')
    def test_brak_kasy_na_przelew_wychodzacy_firma(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 900
        konto.ksiegowanie_wychodzacego(10000)
        self.assertEqual(konto.saldo, konto.saldo, 'Saldo nie jest rowne wartosci oczekiwanej')



    def test_ekspresowy_wychodzacy_osoba(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 900
        konto.ksiegowanie_ekspresowego(900)
        self.assertEqual(konto.saldo, 900-900-1, 'Saldo nie jest rowne wartosci oczekiwanej')
    def test_brak_kasy_ekspresowy_wychodzacy_osoba(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 900
        konto.ksiegowanie_ekspresowego(901)
        self.assertEqual(konto.saldo, konto.saldo, 'Saldo nie jest rowne wartosci oczekiwanej')
    def test_ekspresowy_wychodzacy_firma(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 800
        konto.ksiegowanie_ekspresowego(800)
        self.assertEqual(konto.saldo, 800-800-5, 'saldo nie jest rowne wartosci oczekiwanej')
    def test_brak_kasy_ekspresowy_wychodzacy_firma(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 800
        konto.ksiegowanie_ekspresowego(805)
        self.assertEqual(konto.saldo, konto.saldo, 'saldo nie jest rowne wartosci oczekiwanej')

    def test_dzialanie_historii_na_koncie(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 900
        konto.ksiegowanie_wychodzacego(300)
        self.assertEqual(konto.history, [-300], 'historia konta sie nie zgadza')
    def test_wielokrotna_historia_na_koncie(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 800
        konto.ksiegowanie_przychodzacego(900)
        konto.ksiegowanie_wychodzacego(300)
        self.assertEqual(konto.history, [900, -300], 'historia konta nie zgadza sie')
    def test_historia_ekspresowa_konto(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 700
        konto.ksiegowanie_ekspresowego(200)
        self.assertEqual(konto.history, [-201], 'historia konta nie zgadza sie')
    def test_historia_ekspresowa_firma(self):
        konto = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto.saldo = 200
        konto.ksiegowanie_ekspresowego(50)
        self.assertEqual(konto.history, [-55], 'historia konta firmowego nie zgadza sie')


