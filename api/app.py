from flask import Flask
from flask_restplus import Api


# Importando resources
from api.resource.usuario_resource import UsuarioResource
from api.resource.imovel_resource import ImovelResource
from api.resource.login_resource import LoginResource


def config_routes(app):
    api = Api(app)

    api.register_resource(UsuarioResource, '/api/v1/usuario')
    api.register_resource(ImovelResource, '/api/v1/imovel')
    api.register_resource(LoginResource, '/api/v1/login')


def create_app():
    app = Flask(__name__)
    config_routes(app)
    
    return app
