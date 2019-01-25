from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
	__tablename__ = "flights3"
	id = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String, nullable=False)
	destination = db.Column(db.String, nullable=False)
	duration = db.Column(db.Integer, nullable=False)

class Book(db.Model):
	__tablename__ = "books1"
	id = db.Column(db.Integer, primary_key=True)	
	isbn = db.Column(db.String, nullable=False)
	title = db.Column(db.String, nullable=False)
	author = db.Column(db.String, nullable=False)
	year = db.Column(db.Integer, nullable=False)

class Passenger(db.Model):
	__tablename__ = "passengers"
	id = db.Column(db.Integer, primary_key=True)	
	name = db.Column(db.String, nullable=False)
	flight_id = db.Column(db.Integer, db.ForeignKey("flights3.id"), nullable=False)
