from flask import Flask
from flask import jsonify
import logging


app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "message" : "Hello World"
    }
    return jsonify(data)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)