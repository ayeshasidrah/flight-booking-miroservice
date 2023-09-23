from shared_services import root_dir
from flask import Flask, make_response
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

with open("{}/database/bookings.json".format(root_dir()), "r") as f:
    bookings = json.load(f)


@app.route("/", methods=['GET'])
def home():
    return make_response({
        "uri": "/",
        "subresource_uris": {
            "bookings": "/bookings",
            "booking": "/bookings/<username>"
        }
    })


@app.route("/bookings", methods=['GET'])
def booking_list():
    return make_response(bookings)


@app.route("/bookings/<username>", methods=['GET'])
def booking_record(username):
    if username not in bookings:
        print("No usernames found.")
        raise NotFound

    return make_response(bookings[username])


if __name__ == "__main__":
    app.run(port=5003, debug=True)

