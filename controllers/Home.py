from utils.database.database import Database
from flask import request, jsonify, Blueprint
from app import webapi
from utils.exceptions import UsuarioNaoEncontrado,  PermissaoInvalida, CampoIncorreto, ImovelNaoEncontrado, SenhaIncorreta
from bson.objectid import ObjectId


home_routes = Blueprint('home_routes', __name__)


@home_routes.route('/', methods=['GET'])
def home():
    return 'Seja bem vindo a API de integracão do IMOVEIS NATAL'

# @webapi.before_request
# def before_request():
#     url = request.url

#     if '/usuarios' not in url:
#         headers = request.headers

#         if 'token' not in headers:
#             return jsonify({
#                 'status': 'erro',
#                 'menssagem': 'erro de segurança',
#                 'codigo_requisicao': 'in01'
#             }), 403

#         else:
#             db = Database()

#             token = headers['token']
#             token = tk.decrypt_token(token)

#             if token == True:
#                 return jsonify({
#                 "status":"erro",
#                 "mensagem": "token não pertence a nenhum usuario cadastrado",
#                 "codigo_requisicao": "in02"
#             }), 403

#             acess = db.select_one_object('usuarios', {'_id': ObjectId(token)})

#             if acess is None:
#                 return jsonify({
#                 "status":"erro",
#                 "mensagem": "token não pertence a nenhum usuario cadastrado",
#                 "codigo_requisicao": "in02"
#             }), 403

#             if acess['status'] == 'inativo':
#                 return jsonify({
#                 "status":"erro",
#                 "mensagem": "o seu usuario esta inativado",
#                 "codigo_requisicao": "in02"
#             }), 403

@home_routes.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


@webapi.errorhandler(404)
def page_not_found(e):
    return jsonify({
            "status":"erro",
            "mensagem": "url não encontrada",
            "codigo_requisicao": "in03"
        }), 404


@webapi.errorhandler(UsuarioNaoEncontrado)
def usuario_nao_encontrado(UsuarioNaoEncontradoObject):
    return jsonify({
                'status': 'erro',
                'menssagem': 'usuario não  encontrado no sistema',
                'codigo-requisicao':  'in204'
            }), 204


@webapi.errorhandler(PermissaoInvalida)
def permissao_invalida(PermissaoInvalidaObject):
    return jsonify({
                'status': 'erro',
                'menssagem': 'permissão invalida',
                'codigo-requisicao':  'in404'
            })


@webapi.errorhandler(CampoIncorreto)
def campo_incorreto(CampoIncorretoObject):
    return jsonify({
                'status': 'erro',
                'menssagem': f'o campo {CampoIncorretoObject.campo} não foi preenchido corretamente',
                'codigo-requisicao': 'in400'
    }), 400


@webapi.errorhandler(ImovelNaoEncontrado)
def imovel_nao_encontrado(ImovelNaoEncontradoObject):
    return jsonify({
                'status': 'erro',
                'menssagem': 'imovel não encontrado no sistema',
                'codigo-requisicao': 'in204'
    }), 204


@webapi.errorhandler(SenhaIncorreta)
def senha_incorreta(SenhaIncorretaObject):
    return jsonify({
                'status': 'erro',
                'menssagem': 'senha incorreta',
                'codigo-requisicao': 'in422'
    }), 422