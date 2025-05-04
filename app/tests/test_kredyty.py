import unittest
from parameterized import parameterized
from ..Konto import Konto



class TestKredyt(unittest.TestCase):
    imie = 'jarek'
    nazwisko = 'szparek'
    pesel = '12345678901'
    
    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([-100,200,300,100,500], 500, True, 500),
        ([-10000,200,300,100,500], 500, False, 0),
        ([-100,200,300,100,-500], 500, False , 0),
        ([-100,200,300,100,500], 2500, False, 0)
    ])
    def test_5_zaciagniecie_kredytu(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.history = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)

    # def test_zaciaganie_kredytu(self):
    #     konto = Konto(self.imie, self.nazwisko, self.pesel)
    #     konto.history = [-100, 200, 300, 400, 500]
    #     czy_przyznany = konto.zaciagnij_kredyt(600)
    #     self.assertTrue(czy_przyznany)
    #     self.assertEqual(konto.saldo, 600)
    # def test_zaciaganie_kredytu_ujemny_w_osttatnich_3(self):
    #     konto = Konto(self.imie, self.nazwisko, self.pesel)
    #     konto.history = [-100, 200, 300, 400, -500]
    #     czy_przyznany = konto.zaciagnij_kredyt(600)
    #     self.assertFalse(czy_przyznany)
    #     self.assertEqual(konto.saldo, 0)
    # def test_zaciaganie_kredytu_kwota_za_duza_na_nasze_ostatnie_5(self):
    #     konto = Konto(self.imie, self.nazwisko, self.pesel)
    #     konto.history = [-100, 200, 300, 400, 500]
    #     czy_przyznany = konto.zaciagnij_kredyt(2000)
    #     self.assertFalse(czy_przyznany)
    #     self.assertEqual(konto.saldo, 0)
    # def test_zaciaganie_kredytu_brak_historii(self):
    #     konto = Konto(self.imie, self.nazwisko, self.pesel)
    #     konto.history = [0]
    #     czy_przyznany = konto.zaciagnij_kredyt(2000)
    #     self.assertFalse(czy_przyznany)
    #     self.assertEqual(konto.saldo, 0)
    # def test_zaciaganie_kredytu_wielka_kwota_na_minus(self):
    #     konto = Konto(self.imie, self.nazwisko, self.pesel)
    #     konto.history = [-105435435430, 200, 300, 400, 500]
    #     czy_przyznany = konto.zaciagnij_kredyt(2000)
    #     self.assertFalse(czy_przyznany)
    #     self.assertEqual(konto.saldo, 0)
    
    