# app.py

from flask import Flask
from flask import jsonify
import datetime
import sys


app = Flask(__name__)
who = ""


@app.route("/")
def index():
    _datetime_utc = datetime.datetime.now(tz=datetime.timezone.utc)
    time = datetime.datetime.strftime(_datetime_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
    timesplit = time.split(".")
    try:
        if len(timesplit[1].replace("Z", "")) > 3:
            time = timesplit[0] + "." + timesplit[1][:3] + "Z"
    except:
        pass

    data = {
        "message": "Hello {who} ci/cd by github actions".format(who=who),
        "time": time,
    }
    return jsonify(data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        who = sys.argv[1]
    else:
        who = "Arques"

    app.run(host="0.0.0.0", debug=False)
