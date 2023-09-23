from shared_services import root_dir
import json
from flask import Flask, make_response
from werkzeug.exceptions import NotFound

app = Flask(__name__)

with open("{}/database/flights.json".format(root_dir(), 'r')) as f:
    flights = json.load(f)


@app.route("/", methods=['GET'])
def home():
    return make_response({
        "uri": ",",
        "sub_uri": {
            "flights": "/flights",
            "flight": "/flights/<id>"
        }
    })


@app.route("/flights", methods=['GET'])
def flights_record():
    return flights


@app.route("/flights/<flight_id>", methods=['GET'])
def flight_info(flight_id):
    if flight_id not in flights:
        raise NotFound

    result = flights[flight_id]
    result["uri"] = "/flights/{}".format(flight_id)

    return make_response(result)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
