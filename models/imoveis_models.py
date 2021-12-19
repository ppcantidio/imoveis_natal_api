import re
import json
from bson.objectid import ObjectId
from flask.json import jsonify
from models.validacoes import Validacoes
from controllers.database.database import Database

class Imoveis_Models():

    def __init__(self):
        self.db = Database()

        self.validacoes = Validacoes()

    
    def criar_imovel(id_usuario, titulo, imovel, ):
        pass