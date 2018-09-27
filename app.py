from flask import Blueprint
from flask_restful import Api
from resources.Restaurante import Restaurante

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(Restaurante,'/restaurant')
