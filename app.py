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
    ip_address = flask.request.remote_addr

    try:
        if len(timesplit[1].replace("Z", "")) > 3:
            time = timesplit[0] + "." + timesplit[1][:3] + "Z"
    except:
        pass

    data = {
        "message": "Hello {who} ci/cd by github actions".format(who=who),
        "time": time,
        "ip_address": ip_address,
    }
    return jsonify(data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 명령어 인수를 통해 전달 받은 값을 전략명으로 처리하면 될 것 같다.
        who = sys.argv[1]
    else:
        who = "Arques"

    app.run(host="0.0.0.0", debug=False)
