from flask import request
from flask_restful import Resource,reqparse
from Model import db, Restaurant, RestaurantSchema
from sqlalchemy import text
from sqlalchemy import func
import math

restaurantes_schema = RestaurantSchema(many=True)
restaurant_schema = RestaurantSchema()

parser = reqparse.RequestParser()

class Statistics(Resource):
    def get(self):
        args = request.args
        #print (args['latitude'])
        #set_query = str("SELECT * FROM melp.restaurants as A WHERE ST_PointInsideCircle(ST_Point(A.lng,A.lat),"+args['longitude']+","+args['latitude']+","+args['radius']+")")
        set_query = str("SELECT * FROM melp.restaurants as A WHERE ST_DWithin(ST_MakePoint(A.lng,A.lat), ST_MakePoint("+args['longitude']+","+args['latitude']+")::geography,"+args['radius']+")")  
        #print (set_query)
        restaurantes = Restaurant.query.from_statement(text(set_query))
        restaurantes = restaurantes_schema.dump(restaurantes).data
        number_restaurants = len(restaurantes)
        avg_rating = sum([restaurant['rating'] for restaurant in restaurantes ])/float(number_restaurants)
        if number_restaurants>1:
           desv_rating= math.sqrt(sum([(restaurant['rating']-avg_rating)**2 for restaurant in restaurantes ])/(len(restaurantes)-1.0))
        else:
            desv_rating = 0.0
        #print (number_restaurants,avg_rating,desv_rating)
        return { "status": 'success', 'data': {'count':number_restaurants,'avg':avg_rating,'std':desv_rating} }, 201