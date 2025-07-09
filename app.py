from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import requests
from datetime import datetime

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # Ensure Unicode characters are not escaped
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

@app.route('/api/noticias', methods=['GET'])
def buscar_noticias():
    feed_url = 'https://jornal.usp.br/tag/ecologia/feed/'
    response = requests.get(feed_url)
    response.encoding = 'utf-8'  # Ensure proper UTF-8 encoding
    xml_content = response.text
    import xml.etree.ElementTree as ET

    root = ET.fromstring(xml_content)
    items = []
    for item in root.findall('.//item'):
        title = item.find('title').text
        link = item.find('link').text
        pub_date = item.find('pubDate').text
        creator = item.find('{http://purl.org/dc/elements/1.1/}creator').text if item.find('{http://purl.org/dc/elements/1.1/}creator') is not None else 'Unknown'
        category = item.find('.//category').text if item.find('category') is not None else 'Uncategorized'
        pub_date_parsed = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z").__format__("%Y-%m-%d %H:%M:%S")
        noticia = {
            "title": title,
            "link": link,
            "pub_date": pub_date_parsed,
            "creator": creator,
            "category": category
        }
        items.append(noticia)

    response = jsonify({"items": items})
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run(debug=True)
