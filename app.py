from flask import Flask, jsonify
import random

app = Flask(__name__)

# Marcas de exemplo
marcas_locais = [
    {"nome": "Moose Coffee", "descricao": "Café local de qualidade", "ganho": "R$ 500 mil"},
    {"nome": "Posto Pinguim", "descricao": "Rede regional de postos de gasolina", "ganho": "R$ 600 mil"},
    {"nome": "Biscoitos Aurora", "descricao": "Fábrica tradicional da cidade", "ganho": "R$ 450 mil"}
]

marcas_nacionais = [
    {"nome": "Banco do Brasil", "descricao": "Banco estatal com presença nacional", "ganho": "R$ 1.5 milhão"},
    {"nome": "Petrobras", "descricao": "Gigante do setor de energia", "ganho": "R$ 1.8 milhão"},
    {"nome": "Magazine Luiza", "descricao": "Rede de varejo", "ganho": "R$ 1.6 milhão"}
]

marcas_globais = [
    {"nome": "Nike", "descricao": "Marca global de esportes", "ganho": "R$ 3 milhões"},
    {"nome": "Coca-Cola", "descricao": "Bebidas reconhecidas mundialmente", "ganho": "R$ 2.8 milhões"},
    {"nome": "Samsung", "descricao": "Tecnologia e inovação", "ganho": "R$ 2.9 milhões"}
]

@app.route("/")
def home():
    return "Sponsorship system online!"

@app.route("/sponsorship/local")
def local():
    selecionadas = random.sample(marcas_locais, 3)
    return jsonify(selecionadas)

@app.route("/sponsorship/national")
def national():
    selecionadas = random.sample(marcas_nacionais, 3)
    return jsonify(selecionadas)

@app.route("/sponsorship/global")
def global_():
    selecionadas = random.sample(marcas_globais, 3)
    return jsonify(selecionadas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
