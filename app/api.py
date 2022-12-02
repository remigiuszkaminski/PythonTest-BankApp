from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.addAccToArray(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    ilosc = RejestrKont.giveLengthOfArr()
    return jsonify(str(ilosc)), 200
@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    szukane = RejestrKont.searchByPesel(pesel)
    return jsonify(imie=szukane.imie, nazwisko=szukane.nazwisko,pesel = szukane.pesel, saldo=szukane.saldo), 200

# @app.route("konta/konto/<pesel>", methods=['PUT'])
# def update_konto_z_peselem(pesel):

@app.route("konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_konto(pesel):
    dane = request.get_json()
    konto = RejestrKont.searchByPesel(pesel)
    konto.imie = dane["imie"] if "imie" in dane else konto.imie
    konto.nazwisko = dane["nazwisko"] if "nazwisko" in dane else konto.nazwisko
    konto.pesel = dane["pesel"] if "pesel" in dane else konto.pesel
    konto.saldo = dane["saldo"] if "saldo" in dane else konto.dane
    return jsonify("Zakonczono sukcesem"), 200

