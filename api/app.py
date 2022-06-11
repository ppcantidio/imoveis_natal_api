from flask import Flask
from api.extensions import configuration


def create_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    configuration.load_extensions(app)
    return app
