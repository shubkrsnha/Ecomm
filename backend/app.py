from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_data():
    # Create some dummy data
    products = [
        {"id": 1, "name": "Laptop", "price": 50000},
        {"id": 2, "name": "Mobile", "price": 15000},
        {"id": 3, "name": "Headphones", "price": 2000},
    ]
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)




