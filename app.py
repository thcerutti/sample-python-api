from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Allow all origins

# Sample route
@app.route('/')
def home():
    return jsonify({"message": "hello world"})

# Lista os biomas disponíveis
@app.route('/api/biomas', methods=['GET'])
def buscar_biomas():
    with open('data/biomas.json') as arquivo:
        data = json.load(arquivo)
    return jsonify(data)

# Busca especies em extinção
@app.route('/api/especies', methods=['GET'])
def buscar_especies():
    with open('data/especies.json') as arquivo:
        data = json.load(arquivo)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
