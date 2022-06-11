from flask_restplus import Api


def init_app(app):
    api = Api(app)

    # Importando resources
    from api.resource.user_resource import UserResource


    # Registrando resources
    api.register_resource()
