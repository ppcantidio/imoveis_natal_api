import re
import json
from flask.json import jsonify
from controllers.database.database import Database
from acessos_token import Token


class User_Models:

    def __init__(self):
        self.db = Database()

        self.token = Token()


    def  criar_usuario(self, nome, email, telefone):
        formato_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(formato_email, email):
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

        if email_existe == '':
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
