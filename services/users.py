from werkzeug.exceptions import NotFound, ServiceUnavailable
import requests
from flask import Flask, make_response
from shared_services import root_dir
import json

app = Flask(__name__)

with open("{}/database/users.json".format(root_dir(), 'r')) as f:
    users = json.load(f)


@app.route("/", methods=['GET'])
def home():
    return make_response({
        "uri": "/",
        "subresource_uris": {
            "users": "/users",
            "user": "/users/<username>",
            "bookings": "/users/<username>/bookings"
        }
    })


@app.route("/users", methods=['GET'])
def users_list():
    return make_response(users)


@app.route("/users/<username>", methods=['GET'])
def users_record(username):
    if username not in users:
        raise NotFound

    return users[username]


@app.route("/users/<username>/bookings", methods=['GET'])
def user_bookings(username):
    if username not in users:
        raise NotFound

    try:
        users_bookings = requests.get("http://127.0.0.1:5003/bookings/{}".format(username))
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable("The Bookings service is unavailable.")

    if users_bookings.status_code == 404:
        raise NotFound("No bookings were found for {}".format(username))

    users_bookings = users_bookings.json()
    print(users_bookings)

    result = {}
    for date, flights in users_bookings.items():
        result[date] = []
        for i in flights:
            try:
                flights = requests.get("http://127.0.0.1:5001/flights/{}".format(i))
            except requests.exceptions.ConnectionError:
                raise ServiceUnavailable("The booking service is unavailable.")
            flights = flights.json()
            result[date].append({
                "name": flights["name"],
                "depart": flights["from"],
                "destination": flights["to"],
                "uri": flights["uri"]
            })
    print(make_response(result))

    return make_response(result)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
