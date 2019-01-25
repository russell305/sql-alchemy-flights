#put on git
#set up flight and passenger
#send in value
# set up flight,flights html is alchemy
#export FLASK_APP=application.py

import os
from flask import Flask, render_template, request

# Import table definitions.
from models import *

app = Flask(__name__)

# Tell Flask what SQLAlchemy database to use.
app.config["SQLALCHEMY_DATABASE_URI"] = ("postgres://ayjxjjxhgpzlnl:f150cc319da46e38a1fb398ee335d98fa5468668d0d8aa3da415aed475d08f9b@ec2-54-225-227-125.compute-1.amazonaws.com:5432/d9prh5mib7dh2p")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).


db.init_app(app)

@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():

	flights = Flight.query.all()
	return render_template("index.html",flights=flights)

@app.route("/book_flight", methods=["POST"])	
def book_flight():
	print("book a flight")
	name = request.form.get("name")
	flight_id = int(request.form.get("flight_id"))
	flight = Flight.query.get(flight_id)
	passenger = Passenger(name=name, flight_id=flight_id)
	message = "Success"
	db.session.add(passenger)
	db.session.commit()
	return render_template("success.html", message = message)

@app.route("/flights")
def flights():
	"""List all flights"""
	flights = Flight.query.all()
	return render_template("flights.html", flights=flights)	

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
	"Individual Flight Data"
	flight = Flight.query.get(flight_id)
	passengers = Passenger.query.filter_by(flight_id=flight_id).all()
	return render_template("flight.html", flight=flight, passengers=passengers)








	

