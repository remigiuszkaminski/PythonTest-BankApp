import unittest
import requests

class TestObslugaKont(unittest.TestCase):
    body = {
        'imie': 'nick',
        'nazwisko': 'drenaz',
        'pesel' : '54678912344'
    }

    url = 'http://localhost:5000'

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url + '/konta/stworz_konto', json = self.body)
        self.assertEqual(create_resp.status_code, 201)

    def test_2_get_po_peselu(self):
        get_resp =requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
