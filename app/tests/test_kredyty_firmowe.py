import unittest
from parameterized import parameterized
from ..Konto import KontoFirmowe
from unittest.mock import patch
class TestKredytFirmowy(unittest.TestCase):
    nazwafirmy = 'Lacka Sliwa'
    NIP = '5260211104'
    

    @patch('app.Konto.KontoFirmowe.pobierz_nip')
    def setUp(self, mock_pobierz_nip):
        mock_pobierz_nip.return_value = True
        self.konto = KontoFirmowe(self.nazwafirmy, self.NIP)

    @parameterized.expand([
        ([4661,-1775,300,100,500], 500, 249, True, 749),
        ([4661, 1775, 300, 100, 500], 500, 250, False, 500),
        ([666, 789], 700, 300, False, 700),
        ([-1775, 700], 800, 450, False, 800)
        
    ])
    def test_zaciagniecie_kredytu_firma(self, historia, saldo, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.history = historia
        self.konto.saldo = saldo
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)