from acessos_token import Token
from flask.json import jsonify
from bson.objectid import ObjectId
from models.validacoes import Validacoes
from controllers.database.database import Database


class User_Models:

    def __init__(self):
        self.db = Database()

        self.token = Token()

        self.validacoes = Validacoes()

    @staticmethod
    def retorna_booleano(string):
        if string == 'True':
            return True
        else:
            return  False

    def  criar_usuario(self, token, nome, email, telefone):
        # verificacao de permissoes
        id = self.token.decrypt_token(token)

        usuario_admin = self.db.select_one_object('usuarios', {'_id': ObjectId(id)})

        if usuario_admin['permissoes']['criar_usuarios'] == False:
            return jsonify({
                'status': 'erro',
                'mensagem': 'permissao insuficiente para realizar operacao',
                'codigo-requisicao': 'in00'
            })

        # validacao de dados
        validacao_email = self.validacoes.validar_email(email)
        validacao_nome = self.validacoes.validar_nome(nome)
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

        if validacao_nome is False:
            return jsonify({
                'status': 'erro',
                'mensagem': 'preencha o campo nome corretamente',
                'codigo-requisicao': 'in10'
            })

        # verificacao de existencia de dados
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

        # criando e inserindo usuario no banco de dados
        usuario = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'tipo': 'corretor',
            'status': 'ativo',
            'permissoes': {
                'criar_usuarios': False,
                'excluir_usuarios': False,
                'aprovar_imoveis': False,
                'excluir_imoveis_geral': False,
                'editar_imoveis_geral': False,
                'ocultar_imovies_geral': False,
                'permissoes_administrador': False
            }
        }

        usuario = self.db.insert_object(usuario, 'usuarios')

        usuario = self.db.select_one_object('usuarios', {'email': email})
        usuario['_id'] = str(usuario['_id'])

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'usuario criado com sucesso',
            'codigo-requisicao': 'in200',
            'token': self.token.encrypt_token(str(usuario.get('_id'))),
            'usuario': usuario
        })


    def editar_usuario(self, token, nome, email, telefone):
        id = self.token.decrypt_token(token)
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


    def editar_permissoes(self, token, email_usuario, criar_usuarios,  excluir_usuarios, aprovar_imoveis, excluir_imoveis, editar_imoveis, ocultar_imoveis):
        # verificacao de permissoes
        id_usuario = self.token.decrypt_token(token)

        usuario = self.db.select_one_object('usuarios', {'_id': ObjectId(id_usuario)})
        if  usuario['permissoes']['permissoes_administrador'] == False:
            return jsonify({
                'status': 'erro',
                "menssagem": 'permissoes insuficiente para realizacao operacao',
                'codigorequisicao': 'in300',
                'usuario': usuario
            })
        
        # fazendo alteracoes de permissoes no usuario
        usuario = self.db.select_one_object('usuarios', {'email': email_usuario})
        perimissoes_usuario = usuario['permissoes']

        perimissoes_usuario['criar_usuarios'] = self.retorna_booleano(criar_usuarios)
        perimissoes_usuario['excluir_usuarios'] = self.retorna_booleano(excluir_usuarios)
        perimissoes_usuario['aprovar_imoveis'] = self.retorna_booleano(aprovar_imoveis)
        perimissoes_usuario['excluir_imoveis'] = self.retorna_booleano(excluir_imoveis)
        perimissoes_usuario['editar_imoveis'] = self.retorna_booleano(editar_imoveis)
        perimissoes_usuario['ocultar_imoveis'] = self.retorna_booleano(ocultar_imoveis)

        usuario['permissoes'] =  perimissoes_usuario

        usuario = self.db.update_object(usuario, 'usuarios', {'email': email_usuario})

        return jsonify({
            'status': 'sucesso',
            "menssagem": 'permissoes do usuario alteradas com sucesso',
            'codigorequisicao': 'in200',
            'usuario': usuario
        })
