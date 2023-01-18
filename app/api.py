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

@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_konto(pesel):
    aktualizowane = request.get_json()
    if 'pesel' in aktualizowane and RejestrKont.searchByPesel(aktualizowane['pesel']) != None:
        return jsonify("Konto to istnieje, mozliwosc aktualizowania"), 400
    konto = RejestrKont.updateAcc(pesel, aktualizowane)
    if(konto == None):
        return jsonify("Konto o danym peselu nie istnieje"), 200
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200


@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def usun_konto(pesel):
    konto = RejestrKont.accRemove(pesel)
    if(konto == None):
        return jsonify("Konto o danym peselu nie istnieje"), 200
    return jsonify("Konto zostalo usuniete"), 200
    

