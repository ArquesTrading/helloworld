# app.py

from flask import Flask
from flask import jsonify
import datetime


app = Flask(__name__)


@app.route("/")
def index():
    _datetime_utc = datetime.datetime.now(tz=datetime.timezone.utc)
    time = datetime.datetime.strftime(_datetime, format)
    timesplit = time.split(".")
    try:
        if len(timesplit[1].replace("Z", "")) > 3:
            time = timesplit[0] + "." + timesplit[1][:3] + "Z"
    except:
        pass

    data = {"message": "Hello Arqeus Hahahahahaha !!!", "time": time}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
