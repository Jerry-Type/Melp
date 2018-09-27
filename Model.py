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
    id = db.Column(db.String(250), primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(250),nullable=False)
    email = db.Column(db.String(250),nullable=False)
    phone = db.Column(db.Text,nullable=False)
   
    def __init__(self, id, rating,name,email,phone):
        self.id = id
        self.rating = rating
        self.name = name
        self.email = email
        self.phone = phone

class RestaurantSchema(ma.Schema):
    #Partial implementation
    id = fields.String(required=True)
    rating = fields.Integer(required=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

