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



def main():
	# Create tables based on each table definition in `models`
	#db.create_all()
	flights_list = Flight.query.all()
	for index in flights_list:
		print (index)
		print("hi russ", index.origin)
		print("hi russ", index.destination)
		
if __name__ == "__main__":
	# Allows for command line interaction with Flask application
	with app.app_context():
		main()	