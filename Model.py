from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class Restaurant(db.Model):
    #Partial implementation
    __tablename__ = 'restaurants'
    __table_args__ = {"schema":"melp"}
    id = db.Column(db.Text, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text,nullable=False)
    site = db.Column(db.Text,nullable=False)
    email = db.Column(db.Text,nullable=False)
    phone = db.Column(db.Text,nullable=False)
    street = db.Column(db.Text,nullable=False)
    city = db.Column(db.Text,nullable=False)
    state = db.Column(db.Text,nullable=False)
    lat = db.Column(db.Float,nullable=False)
    lng = db.Column(db.Float,nullable=False)
    

   
    def __init__(self, id, rating,name,site,email,phone,street,city,state,lat,lng):
        self.id = id
        self.rating = rating
        self.name = name
        self.site = site
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.lat = lat
        self.lng = lng

class RestaurantSchema(ma.Schema):
    #Partial implementation
    id = fields.String(required=True)
    rating = fields.Integer(required=False)
    name = fields.String(required=False)
    site = fields.String(required=False)
    email = fields.String(required=False)
    phone = fields.String(required=False)
    street = fields.String(required=False)
    city = fields.String(required=False)
    state = fields.String(required=False)
    lat = fields.Float(required=False)
    lng = fields.Float(required=False)

