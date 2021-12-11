from controllers.database.database import Database
from flask import request, jsonify, Blueprint
from app import webapi
from bson.objectid import ObjectId

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/', methods=['GET'])
def home():
    return 'Seja bem vindo a API de integracão do IMOVEIS NATAL'

@webapi.before_request
def before_request():
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
        print(token)

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

        