# app.py

from flask import Flask
from flask import jsonify, request
import socket
import datetime
import sys
import logging
import json


app = Flask(__name__)
who = ""

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


@app.route("/")
def index():
    _datetime_utc = datetime.datetime.now(tz=datetime.timezone.utc)
    time = datetime.datetime.strftime(_datetime_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
    timesplit = time.split(".")
    visitor_ip_address = request.remote_addr
    hostname = socket.gethostname()
    server_ip_address = socket.gethostbyname(hostname)

    try:
        if len(timesplit[1].replace("Z", "")) > 3:
            time = timesplit[0] + "." + timesplit[1][:3] + "Z"
    except:
        pass

    data = {
        "message": "Hello {who} ci/cd by github actions".format(who=who),
        "time": time,
        "visit_ip_address": visitor_ip_address,
    }

    logging.info(
        "host_ip_address : " + server_ip_address + " || data = " + json.dumps(data)
    )

    return jsonify(data)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        # 명령어 인수를 통해 전달 받은 값을 전략명으로 처리하면 될 것 같다.
        who = sys.argv[1]
        port = 80
    elif len(sys.argv) > 2:
        who = sys.argv[1]
        port = sys.argv[2]
    else:
        port = 80
        who = "Arques"

    app.run(host="0.0.0.0", debug=False, port=port)
