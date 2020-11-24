# app.py

from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route("/")
def index():
    data = {"message": "Hello Arqeus !!!"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
