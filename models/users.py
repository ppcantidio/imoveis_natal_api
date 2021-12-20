import re
import json
from bson.objectid import ObjectId
from flask.json import jsonify
from models.validacoes import Validacoes
from controllers.database.database import Database
from acessos_token import Token


class User_Models:

    def __init__(self):
        self.db = Database()

        self.token = Token()

        self.validacoes = Validacoes()


    def  criar_usuario(self, nome, email, telefone):
        validacao_email = self.validacoes.validar_email(email)

        if validacao_email is False:
            return jsonify({
                'status': 'erro',
                'mensagem': 'preencha o campo email corretamente',
                'codigo-requisicao': 'in10'
            })
            
        nome = nome.strip()
        telefone = telefone.strip()

        if nome == '':
            return jsonify({
                'status': 'erro',
                'mensagem': 'o campo nome esta vazio',
                'codigo-requisicao': 'in06'
            })

        if telefone == '':
            return jsonify({
                'status': 'erro',
                'mensagem': 'o campo telefone esta vazio',
                'codigo-requisicao': 'in06'
            })

        email_existe = self.db.select_one_object('usuarios', {'email': email})
        telefone_existe = self.db.select_one_object('usuarios', {'telefone': telefone})

        if email_existe is not None:
            return jsonify({
                'status': 'erro',
                'mensagem': 'ja existe um usuario cadastrado com esse email',
                'codigo-requisicao': 'in04'
            })

        if telefone_existe is not None:
            return jsonify({
                'status': 'erro',
                'mensagem': 'ja existe um usuario cadastrado com esse telefone',
                'codigo-requisicao': 'in05'
            })

        usuario = {
            'nome': nome,
            'email': email,
            'telefone': telefone
        }

        usuario = self.db.insert_object(usuario, 'usuarios')

        usuario = self.db.select_one_object('usuarios', {'email': email})
        id = str(usuario.get('_id'))

        token = self.token.encrypt_token(id)

        usuario['_id'] = str(usuario['_id'])

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'usuario criado com sucesso',
            'codigo-requisicao': 'in200',
            'token': token,
            'usuario': usuario
        })

        return usuario


    def editar_usuario(self, id, nome, email, telefone):
        print(id)
        usuario = self.db.select_one_object('usuarios', {'_id': ObjectId(id)})

        nome = nome.strip()

        if nome != '':
            usuario['nome'] = nome

        validacao_email = self.validacoes.validar_email(email)
        validacao_telefone = self.validacoes.validar_telefone(telefone)

        if validacao_email is False:
            return jsonify({
                'status': 'erro',
                'mensagem': 'preencha o campo email corretamente',
                'codigo-requisicao': 'in10'
            })

        if validacao_telefone is False:
            return jsonify({
                'status': 'erro',
                'mensagem': 'preencha o campo telefone corretamente',
                'codigo-requisicao': 'in10'
            })

        if telefone != '':
            usuario['telefone'] = telefone

        if email != '':
            usuario['email'] = email

        self.db.update_object(usuario, 'processos', {'_id': ObjectId(id)})


    def excluir_usuario(self, id):
        usuario = self.db.select_one_object('processos', {'_id': ObjectId(id)})

        if usuario is None:
            return jsonify({
                'status': 'erro',
                'menssagem': 'nao existe nenhum usuario com esse id',
                "codigo_requisicao": 'in12'
            })

        self.db.delete_one('processos', {'_id': ObjectId(id)})

        return jsonify({
            'status': 'sucesso',
            "menssagem": 'usuario deletado com sucesso',
            'codigorequisicao': 'in200',
            'usuario': usuario
        })
