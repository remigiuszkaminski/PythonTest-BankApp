import unittest
import requests

class TestObslugaKont(unittest.TestCase):
    
    body = {
        'imie': 'nick',
        'nazwisko': 'drenaz',
        'pesel' : '12312332166'
    }

    edytowane_body = {
        'imie': 'Maciek',
        'nazwisko': 'Block'
    }

    url = 'http://localhost:5000'

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url + '/konta/stworz_konto', json = self.body)
        self.assertEqual(create_resp.status_code, 201)

    def test_2_tworzenie_kont_unikatowy_pesel(self):
        create_resp = requests.post(self.url + '/konta/stworz_konto', json = self.body)
        self.assertEqual(create_resp.status_code, 400)

    def test_3_get_po_peselu(self):
        get_resp =requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["saldo"], 0)

    def test_4_put_edycja_konta(self):
        put_resp = requests.put(self.url + f"/konta/konto/{self.body['pesel']}", json = self.edytowane_body)
        self.assertEqual(put_resp.status_code, 200)
        resp_body = put_resp.json()
        self.assertEqual(resp_body["imie"], self.edytowane_body["imie"])
        self.assertEqual(resp_body["nazwisko"], self.edytowane_body["nazwisko"])
        self.assertEqual(resp_body["pesel"], self.body["pesel"])
        self.assertEqual(resp_body["saldo"], 0)

    def test_5_usuwanie_konta(self):
        del_resp = requests.delete(self.url + f"/konta/konto/{self.body['pesel']}", json = self.body)
        self.assertEqual(del_resp.status_code, 200)


    # def test_3_put_po_peselu(self):
    #     put_resp = requests.put(self.url + f"/konta/konto/{self.body['pesel']}")
    #     self.assertEqual(put_resp.status_code, 200)
        
        
