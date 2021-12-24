import re
import json
from flask.json import jsonify
from bson.objectid import ObjectId
from utils.exceptions import PermissaoInvalida
from models.validacoes import Validacoes
from utils.exceptions import ImovelNaoEncontrado
from controllers.database.database import Database

class Imoveis_Models():

    def __init__(self):
        self.db = Database()

        self.validacoes = Validacoes()

    
    def criar_imovel(self, usuario, titulo, tamanho, preco, quartos, banheiros, area_lazer, vagas_garagem, elevador, descricao):
        corretor = usuario
        imovel = {
            'corretor_id': corretor['_id'],
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

    def exbir_imovel(self, imovel_id):
        imovel = self.db.select_one_object('imoveis', {'_id': imovel_id})

        if imovel is None:
            raise ImovelNaoEncontrado()

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
            imovel['_id'] = str(imovel['_str'])
            imoveis_list.append(imovel)

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imoveis encontrados com sucesso',
            'codigo-requisicao': 'in200',
            'imoveis': imoveis_list
        })

    
    def editar_imovel(self, usuario, imovel_id, categoria, titulo, tamanho, preco, quartos, banheiros, area_lazer, vagas_garagem, elevador, descricao):
        imovel = self.db.select_one_object('imoveis', {'_id': imovel_id})

        corretor_id = imovel['corretor_id']

        if corretor_id != usuario['_id']:
            raise PermissaoInvalida()
        
        if categoria is not None:
            imovel['categoria'] = categoria

        if titulo is not None:
            imovel['titulo'] = titulo

        if tamanho is not None:
            imovel['tamanho'] = tamanho

        if preco is not None:
            imovel['preco'] = preco

        if quartos is not None:
            imovel['quartos'] =  quartos

        if banheiros is not None:
            imovel['banheiros'] = banheiros

        if area_lazer is not None:
            imovel['area_lazer'] = area_lazer

        if vagas_garagem is not None:
            imovel['vagas_garagem'] = vagas_garagem
            
        if elevador is not None:
            imovel['elevador'] = elevador

        if descricao is not None:
            imovel['descricao'] = descricao

        self.db.update_object(imovel, 'imoveis', {'_id':  imovel_id})
        imovel = self.db.select_one_object('imovies',  {'_id': imovel_id})
        imovel['_id'] = str(imovel['_id'])

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imovel editado com sucesso',
            'codigo-requisicao': 'in200',
            'imovel': imovel
        })


    def excluir_imovel(self, imovel_id, usuario):
        imovel = self.db.select_one_object('imoveis', {'_id': imovel_id})

        if imovel['corretor_id'] != usuario['_id']:
            if usuario['permissoes']['excluir_imoveis'] != True:
                raise PermissaoInvalida()
        
        self.db.delete_one('imoveis', {'_id': imovel_id})

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imovel deletado com sucesso',
            'codigo-requisicao': 'in200'
        })


    def inativar_imovel(self, imovel_id, usuario):
        imovel = self.db.select_one_object('imoveis', {'_id': imovel_id})

        if imovel['corretor_id'] != usuario['_id']:
            if usuario['permissoes']['inativar_imoveis'] != True:
                raise PermissaoInvalida()
        
        imovel['status'] = 'inativado'

        self.db.update_object(imovel, 'imoveis', {'_id': imovel_id})
        imovel['_id'] = str(imovel['_id'])

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imovel inativado com sucesso',
            'codigo-requisicao': 'in200',
            'imovel': imovel
        })

    
    def ativar_imovel(self):
        pass
