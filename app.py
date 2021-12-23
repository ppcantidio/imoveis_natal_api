from flask import Flask
from dotenv import load_dotenv

load_dotenv('.env')

webapi = Flask(__name__)
webapi.secret_key = 'enhasupersecreta'

#importando blueprints
from controllers.users import users_routes
from controllers.Home import home_routes
from controllers.imoveis import imoveis_routes

#registrando blueprints
webapi.register_blueprint(users_routes, url_prefix='/api/usuarios/')
webapi.register_blueprint(home_routes, url_prefix='/api/v1')
webapi.register_blueprint(imoveis_routes, url_prefix='/api/v1/imoveis')

