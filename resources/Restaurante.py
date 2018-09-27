from flask import request
from flask_restful import Resource,reqparse
from Model import db, Restaurant, RestaurantSchema

restaurantes_schema = RestaurantSchema(many=True)
restaurant_schema = RestaurantSchema()

parser = reqparse.RequestParser()

class Restaurante(Resource):
    def get(self):
        restaurantes = Restaurant.query.all()
        print("Here")
        restaurantes = restaurantes_schema .dump(restaurantes).data
        return {'status': 'success', 'data': restaurantes}, 200

    def post(self):
        json_data = request.get_json(force=True)
        print (json_data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        data, errors = restaurant_schema.load(json_data)
        #print ("The data",data,errors)
        if errors:
            return errors, 422
        restaurant = Restaurant.query.filter_by(id=data['id']).first()
        if restaurant:
            return {'message': 'Restaurant already exists'}, 400
        restaurante = Restaurant(
            id=json_data['id'],
            rating =  json_data['rating'],
            name = json_data['name'],
            email = json_data['email'],
            phone = json_data['phone']
            )
        db.session.add(restaurante)
        db.session.commit()

        result = restaurant_schema.dump(restaurante).data

        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        data, errors = restaurant_schema.load(json_data)
        if errors:
            return errors, 422
        restaurant = Restaurant.query.filter_by(id=data['id']).first()
        if not restaurant:
            return {'message': 'Restaurant does not exist'}, 400
        restaurant.name = data['name']
        db.session.commit()
        result = restaurant_schema.dump(restaurant).data 
        #print ("El resultado es :",result)
        return { "status": 'success', 'data': result }, 202

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        data, errors = restaurant_schema.load(json_data)
        if errors:
            return errors, 422
        restaurant = Restaurant.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = restaurant_schema.dump(restaurant).data
        #print ("El resultado es :",result)
        return { "status": 'success', 'data': result,'message': 'Resgister delete'}, 200
