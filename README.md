# flight-booking-miroservice

## To Install
```
pip install requirements.txt
```
### Create virtual env
```commandline
python -m venv vnev
```

### To Run
```commandline
services/bookings.py
services/flights.py
services/flighttime.py
services/users.py
```

## Api's
### Bookings Service (port 5003)
This api is used to get all the flight bookings by users. To access all bookings and users information is available at port - 
http://127.0.0.1:5001/bookings

you  can filter the bookings made by username, this api gives info on the flight id and flght time for the booking made - 
http://127.0.0.1:5001/bookings/ <username>

### Flights Service (port 5001)
This Api gets the information about flights. Its operating times, source and destination information at the following api - http://127.0.0.1:5001/flights

You can filter the flights based on their id - http://127.0.0.1:5001/flights/<id>

### Flight Times info (port 5002)
This Api provides all the operating flights. You can filter the flights operating by going to this Api -
http://127.0.0.1:5002/flight-times/ <date>

It gives you the flight id and its to and from info for the specified day

### Users (port 5000)
This Api provides all the users info at - http://127.0.0.1:5000/users

You can access a single user info at - http://127.0.0.1:5001/users/ <username>/