from flask import Flask
from app import api_bp
from Model import db

#def create_app(config_filename):

myapp = Flask(__name__)
myapp.config.from_object("config")
myapp.register_blueprint(api_bp, url_prefix='/api')
db.init_app(myapp)


if __name__ == "__main__":
    #myapp = create_app("config")
    myapp.run(debug=True)

