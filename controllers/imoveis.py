from flask.views import MethodView
from flask import request, jsonify, Blueprint, session
from models.imoveis_models import Imoveis_Models
from utils.sessions_requirements import nao_logado, login_requiered

imoveis_routes = Blueprint('imoveis_routes', __name__)

model = Imoveis_Models()

class Imoveis(MethodView):


    @login_requiered
    @imoveis_routes.route('/criar', methods=['POST'])
    def criar_imovel():
        imovel = model.criar_imovel(
            usuario=session['usuario'],
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

    
    @login_requiered
    @imoveis_routes.route('/exibir', methods=['GET'])
    def exibir_imovel():
        imovel_id = request.args.get('id')

        imovel = model.exbir_imovel(imovel_id)

        return imovel


    @imoveis_routes.route('/exibir/todos', methods=['GET'])
    def exibir_todos_imoveis():

        return model.exibir_todos_imoveis()


    @login_requiered
    @imoveis_routes.route('/editar', methods=['POST'])
    def editar_imovel():
        imovel = model.editar_imovel(
            usuario=session['usuario'],
            imovel_id=request.form.get('imovel_id')
        )

        return imovel


    @login_requiered
    @imoveis_routes.route('/excluir', methods=['POST'])
    def excluir_imovel(self):
        imovel = model.excluir_imovel(
            imovel_id=request.form.get('imovel_id'),
            usuario=session['usuario']
        )