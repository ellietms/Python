from logging import debug
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['POST'])
def home():
    print(request.get_json())
    someData = request.get_json()
    return jsonify({"first": someData})


if __name__ == "__main__":
    app.run(debug=True)
