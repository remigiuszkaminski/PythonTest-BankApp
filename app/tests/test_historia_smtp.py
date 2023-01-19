import unittest
from ..Konto import Konto
from ..Konto import KontoFirmowe
from unittest.mock import patch, Mock, MagicMock
from ..SMTPConnection import SMTPConnection
from datetime import date

class TestSMTPHistory(unittest.TestCase):

    imie = 'jarek'
    nazwisko = 'szparek'
    pesel = '12345678901'

    nazwafirmy = 'Drainage'
    NIP = '5544332211'

    def test_wysylanie_historii_osobiste(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.ksiegowanie_przychodzacego(500)
        konto.ksiegowanie_przychodzacego(300)
        konto.ksiegowanie_wychodzacego(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value=True)
        status = konto.wysylanie_historii_na_maila('jarus2115@lipa.com', smtp_connector)
        self.assertTrue(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {date.today().strftime('%Y-%m-%d')}", f"Twoja historia konta to: {konto.history}", "jarus2115@lipa.com")

    def test_wysylanie_historii_osobiste_fail(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.ksiegowanie_przychodzacego(500)
        konto.ksiegowanie_przychodzacego(300)
        konto.ksiegowanie_wychodzacego(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value=False)
        status = konto.wysylanie_historii_na_maila('jarus2115@lipa.com', smtp_connector)
        self.assertFalse(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {date.today().strftime('%Y-%m-%d')}", f"Twoja historia konta to: {konto.history}", "jarus2115@lipa.com")

    @patch('app.Konto.KontoFirmowe.pobierz_nip')
    def test_wysylanie_historii_firmowe(self, mock_pobierz_nip):
        mock_pobierz_nip.return_value = True
        konto2 = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto2.ksiegowanie_przychodzacego(993)
        konto2.ksiegowanie_przychodzacego(10000)
        konto2.ksiegowanie_ekspresowego(234)
        konto2.ksiegowanie_wychodzacego(50)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value=True)
        status = konto2.wysylanie_historii_na_maila('drainageplease@gmail.com', smtp_connector)
        self.assertTrue(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {date.today().strftime('%Y-%m-%d')}", f"Historia konta Twojej firmy to: {konto2.history}", "drainageplease@gmail.com")

    @patch('app.Konto.KontoFirmowe.pobierz_nip')
    def test_wysylanie_historii_firmowe(self, mock_pobierz_nip):
        mock_pobierz_nip.return_value = True
        konto2 = KontoFirmowe(self.nazwafirmy, self.NIP)
        konto2.ksiegowanie_przychodzacego(993)
        konto2.ksiegowanie_przychodzacego(10000)
        konto2.ksiegowanie_ekspresowego(234)
        konto2.ksiegowanie_wychodzacego(50)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value=False)
        status = konto2.wysylanie_historii_na_maila('drainageplease@gmail.com', smtp_connector)
        self.assertFalse(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {date.today().strftime('%Y-%m-%d')}", f"Historia konta Twojej firmy to: {konto2.history}", "drainageplease@gmail.com")