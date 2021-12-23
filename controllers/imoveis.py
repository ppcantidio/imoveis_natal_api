from flask.views import MethodView
from flask import request, jsonify, Blueprint
from models.imoveis_models import Imoveis_Models


imoveis_routes = Blueprint('imoveis_routes', __name__)

model = Imoveis_Models()

class Imoveis(MethodView):


    @imoveis_routes.route('/criar', methods=['POST'])
    def criar_imovel():
        headers = request.headers

        imovel = model.criar_imovel(
            token = headers['token'],
            categoria=request.form.get('categoria'),
            titulo=request.form.get('titulo'),
            tamanho=request.form.get('tamanho'),
            preco=request.form.get('preco'),
            quartos=request.form.get('quartos'),
            banheiros=request.form.get('banheiros'),
            area_lazer=request.form.get('area_lazer'),
            vagas_garagem=request.form.get('vagas_garagem'),
            elevador=request.form.get('elevador'),
            descricao=request.form.get('descricao')
        )

        return imovel


    @imoveis_routes.route('/exibir', methods=['GET'])
    def exibir_imovel():
        imovel_id = request.args.get('id')

        imovel = model.exbir_imovel(imovel_id)

        return imovel

    
    @imoveis_routes.route('/exibir/todos', methods=['GET'])
    def exibir_todos_imoveis():

        return model.exibir_todos_imoveis()
