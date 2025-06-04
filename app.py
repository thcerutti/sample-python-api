from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample route
@app.route('/')
def home():
    return "Hello, Flask API!"

# Example API endpoint (GET)
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify(message=f"Hello, {name}!")

# Example API endpoint (POST)
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(received=data)

if __name__ == '__main__':
    app.run(debug=True)
