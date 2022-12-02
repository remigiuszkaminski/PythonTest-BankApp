import unittest

from ..Konto import KontoFirmowe

class TestKredytFirmowy(unittest.TestCase):
    nazwafirmy = 'Lacka Sliwa'
    NIP = '13245678901'
    
    def setUp(self):
        self.konto = KontoFirmowe(self.nazwafirmy, self.NIP)

    @parameterized.expand([
        ([4661,-1750,300,100,500], 500, 250, True, 750),
        ([4661, 1750, 300, 100, 500], 500, 250, False, 500),
        ([666, 789], 700, 300, False, 700),
        ([-1750, 700], 800, 450, False, 800)
        
    ])
    def test_zaciagniecie_kredytu_firma(self, historia, saldo, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.history = historia
        self.konto.saldo = saldo
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEquals(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)