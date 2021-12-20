from controllers.database.database import Database
from flask import request, jsonify, Blueprint
from app import webapi
from acessos_token import Token
from bson.objectid import ObjectId

home_routes = Blueprint('home_routes', __name__)

tk = Token()

@home_routes.route('/', methods=['GET'])
def home():
    return 'Seja bem vindo a API de integracão do IMOVEIS NATAL'

@webapi.before_request
def before_request():
    url = request.url

    if '/api/usuarios/criar' not in url:
        headers = request.headers

        if 'token' not in headers:
            return jsonify({
                'status': 'erro',
                'menssagem': 'erro de segurança',
                'codigo_requisicao': 'in01'
            }), 403

        else:
            db = Database()

            token = headers['token']
            token = tk.decrypt_token(token)

            if token == True:
                return jsonify({
                "status":"erro",
                "mensagem": "token não pertence a nenhum usuario cadastrado",
                "codigo_requisicao": "in02"
            }), 403

            acess = db.select_one_object('usuarios', {'_id': ObjectId(token)})

            if acess is None:
                return jsonify({
                "status":"erro",
                "mensagem": "token não pertence a nenhum usuario cadastrado",
                "codigo_requisicao": "in02"
            }), 403


@webapi.errorhandler(404)
def page_not_found(e):
    return jsonify({
            "status":"erro",
            "mensagem": "url não encontrada",
            "codigo_requisicao": "in03"
        }), 404

        