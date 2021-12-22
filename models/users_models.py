from acessos_token import Token
from flask.json import jsonify
from bson.objectid import ObjectId
from models.validacoes import Validacoes
from controllers.database.database import Database
from controllers.exceptions  import UsuarioNaoEncontrado, PermissaoInvalida
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


    def verifica_permissao(self, token, permissao):
        id = self.token.decrypt_token(token)

        usuario =  self.db.select_one_object('usuarios', {'_id': ObjectId(id)})

        if usuario['permissoes'][permissao]  ==  False:
            raise PermissaoInvalida()

    def  criar_usuario(self, token, nome, email, telefone):
        self.verifica_permissao(token, 'criar_usuarios')

        # validacao de dados
        self.validacoes.validar_email(email)
        self.validacoes.validar_nome(nome)
        self.validacoes.validar_telefone(telefone)

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
                'editar_permissoes': False
            }
        }

        usuario = self.db.insert_object(usuario, 'usuarios')

        usuario = self.db.select_one_object('usuarios', {'email': email})
        del usuario['_id']

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
        usuario = self.db.select_one_object('usuarios', {'_id': ObjectId(id)})
        del usuario['_id']

        return jsonify({
            'status': 'sucesso',
            "menssagem": 'usuario editado com sucesso',
            'codigorequisicao': 'in200',
            'usuario': usuario
        }) 


    def editar_permissoes(self, token, email_usuario, criar_usuarios,  excluir_usuarios, aprovar_imoveis, excluir_imoveis, editar_imoveis, ocultar_imoveis):
        # verificacao de permissoes
        self.verifica_permissao(token, 'editar_permissoes')
        
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
        usuario = self.db.select_one_object('usuarios', {'email': email_usuario})

        del usuario['_id']

        return jsonify({
            'status': 'sucesso',
            "menssagem": 'permissoes do usuario alteradas com sucesso',
            'codigorequisicao': 'in200',
            'usuario': usuario
        })


    def deletar_usuario(self, email_usuario, token):
        self.verifica_permissao(token, 'excluir_usuarios')

        id  = self.token.decrypt_token(token)

        usuario = self.db.select_one_object('usuarios',  {'email': email_usuario})

        if usuario['_id'] == ObjectId(id):
            return jsonify({
                'status': 'erro',
                'menssagem': 'voce nao pode excluir seu proprio usuario',
                'codigorequisicao': 'in300'
            })

        if usuario is None:
            raise UsuarioNaoEncontrado()

        self.db.delete_one('usuarios', {'email', email_usuario})

        return jsonify({
            'status': 'sucesso',
            "menssagem": 'usuario deletado com sucesso',
            'codigorequisicao': 'in200',
        })
       
        
    def exbir_usuarios(self):
        lista_usuarios = []

        usuarios =  self.db.select_all_objects('usuarios')

        for usuario in usuarios:
            del usuario['_id']
            lista_usuarios.append(usuario)

        return jsonify({
            'status': 'sucesso',
            "menssagem": 'usuarios encontrados com sucesso',
            'codigorequisicao': 'in200',
            'usuario': usuarios
        })


    def inativar_usuario(self, token,  email_usuario):
        id_usuario = self.token.decrypt_token(token)

        usuario_adm = self.db.select_one_object('usuarios', {'_id': ObjectId(id_usuario)})

        if usuario_adm['tipo'] !=  'administrador':
            return  jsonify({
                'status': 'erro',
                "menssagem": 'permissoes insuficientes para realizacao operacao',
                'codigorequisicao': 'in300',
            })


        usuario = self.db.select_one_object('usuarios', {'email': email_usuario})

        if usuario['_id'] == ObjectId(id_usuario):
            return jsonify({
                'status': 'erro',
                'menssagem': 'voce nao pode inativar seu proprio usuario',
                'codigorequisicao': 'in300'
            })

        if usuario is None:
            raise UsuarioNaoEncontrado()

        usuario['status'] = 'inativado'

        self.db.update_object(usuario, 'usuarios', {'email': email_usuario})
        usuario = self.db.select_one_object(usuario,  {'email': email_usuario})
        del usuario['_id']

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'usuario inativado com sucesso',
            'usuario': usuario
        })
