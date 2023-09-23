from werkzeug.exceptions import NotFound
from flask import Flask, make_response
from shared_services import root_dir
import json

app = Flask(__name__)

with open("{}/database/flighttimes1.json".format(root_dir(), "r")) as f:
    flight_times = json.load(f)


@app.route("/", methods=['GET'])
def home():
    return make_response({
        "uri": "/",
        "subresource_uris": {
            "flight_times": "/flight-times",
            "flight_time": "/flight-times/<date>"
        }
    })


@app.route("//flight-times", methods=['GET'])
def flight_times_list():
    return make_response(flight_times)


@app.route("//flight-times/<date>", methods=['GET'])
def flight_records(date):
    if date not in flight_times:
        raise NotFound

    print(flight_times[date])
    return make_response(flight_times[date])


if __name__ == "__main__":
    app.run(port=5002, debug=True)
