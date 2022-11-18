import unittest
from ..Konto import Konto

class TestKredyt(unittest.TestCase):
    imie = 'jarek'
    nazwisko = 'szparek'
    pesel = '12345678901'

    def test_zaciaganie_kredytu(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.history = [-100, 200, 300, 400, 500]
        czy_przyznany = konto.zaciagnij_kredyt(600)
        self.assertTrue(czy_przyznany)
        self.assertEqual(konto.saldo, 600)
    def test_zaciaganie_kredytu_ujemny_w_osttatnich_3(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.history = [-100, 200, 300, 400, -500]
        czy_przyznany = konto.zaciagnij_kredyt(600)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)
    def test_zaciaganie_kredytu_kwota_za_duza_na_nasze_ostatnie_5(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.history = [-100, 200, 300, 400, 500]
        czy_przyznany = konto.zaciagnij_kredyt(2000)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)
    def test_zaciaganie_kredytu_brak_historii(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.history = [0]
        czy_przyznany = konto.zaciagnij_kredyt(2000)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)
    def test_zaciaganie_kredytu_wielka_kwota_na_minus(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.history = [-105435435430, 200, 300, 400, 500]
        czy_przyznany = konto.zaciagnij_kredyt(2000)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)
    
    