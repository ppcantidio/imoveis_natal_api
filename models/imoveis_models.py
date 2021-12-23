import re
import json
from bson.objectid import ObjectId
from flask.json import jsonify
from controllers.exceptions import ImovelNaoEncontrado
from models.validacoes import Validacoes
from controllers.database.database import Database
from acessos_token import Token

class Imoveis_Models():

    def __init__(self):
        self.db = Database()

        self.validacoes = Validacoes()

        self.token = Token()

    
    def criar_imovel(self, token, titulo, tamanho, preco, quartos, banheiros, area_lazer, vagas_garagem, elevador, descricao):
        id_corretor = self.token.decrypt_token(token)
        corretor = self.db.select_one_object('usuarios', {'_id': ObjectId(id_corretor)})

        imovel = {
            'corretor_id': ObjectId(id_corretor),
            'corretor_nome': corretor['nome'],
            'corretor_email': corretor['email'],
            'corretor_telefone': corretor['telefone'],
            'titulo': titulo,
            'descricao': descricao,
            'tamanho': tamanho,
            'preco': preco,
            'quartos': quartos,
            'banheiros': banheiros,
            'area_lazer': area_lazer,
            'vagas_garagem': vagas_garagem,
            'elevador': elevador,
            'status': 'inativo'
        }

        self.db.insert_object(imovel, 'imoveis')

        del imovel['corretor_id']
        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imovel criado com sucesso',
            'imovel': imovel

        })

    def exbir_imovel(self, id_imovel):
        imovel = self.db.select_one_object('imoveis', {'_id': ObjectId(id_imovel)})

        if imovel is None:
            raise ImovelNaoEncontrado()

        id_corretor = imovel['corretor_id']

        corretor = self.db.select_one_object('usuarios', {'_id': ObjectId(id_corretor)})

        imovel['corretor_nome'] = corretor['nome']
        imovel['corretor_email'] = corretor['email']
        imovel['corretor_telefone'] = corretor['telefone']

        self.db.update_object(imovel, 'imoveis', {'_id': ObjectId(id_imovel)})
        
        del imovel['corretor_id']
        imovel['_id'] = str(imovel['_id'])

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imovel encontrado com sucesso',
            'codigo-requsicao': 'in200',
            'imovel': imovel
        })


    def exibir_todos_imoveis(self):
        imoveis_list = []
        imoveis = self.db.select_all_objects('imoveis')

        for imovel in imoveis:
            del imovel['corretor_id']
            imovel['_id'] = str(imovel['_str'])
            imoveis_list.append(imovel)

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imoveis encontrados com sucesso',
            'codigo-requisicao': 'in200',
            'imoveis': imoveis_list
        })

