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

    
    def criar_imovel(self, id_usuario, titulo, tamanho, preco, quartos, banheiros, area_lazer, vagas_garagem, elevador):
        pass