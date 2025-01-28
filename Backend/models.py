from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(200))
    business_name = db.Column(db.String(100))
    driver_license = db.Column(db.String(50))
    insurance = db.Column(db.String(50))
    medical_card = db.Column(db.String(50))
    usdot = db.Column(db.String(50))
    mc_number = db.Column(db.String(50))
    vin_truck = db.Column(db.String(50))
    vin_trailer = db.Column(db.String(50))
    membership_type = db.Column(db.String(20))  # Local, State, National

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float)
    size = db.Column(db.String(50))
    requirements = db.Column(db.String(200))
    pickup_location = db.Column(db.String(200))
    dropoff_location = db.Column(db.String(200))
    load_details = db.Column(db.String(200))
    bol = db.Column(db.String(200))  # Bill of Lading
    pictures = db.Column(db.String(200))  # URL or path to uploaded pictures