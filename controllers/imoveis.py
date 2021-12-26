from flask.views import MethodView
from flask import request, jsonify, Blueprint, session
from models.imoveis_models import Imoveis_Models
from utils.sessions_requirements import nao_logado, login_requiered

imoveis_routes = Blueprint('imoveis_routes', __name__)

model = Imoveis_Models()

class Imoveis(MethodView):


    @imoveis_routes.route('/criar', methods=['POST'])
    @login_requiered
    def criar_imovel():
        imovel = model.criar_imovel(
            usuario=session['usuario'],
            titulo=request.form.get('titulo'),
            descricao=request.form.get('descricao'),
            categoria=request.form.get('categoria'),
            tipo=request.form.get('tipo'),
            cidade=request.form.get('cidade'),
            bairro=request.form.get('bairro'),
            valor=request.form.get('valor'),
            tamanho=request.form.get('tamanho'),
            quartos=request.form.get('quartos'),
            suites=request.form.get('suites'),
            vagas_garagem=request.form.get('vagas_garagem'),
            elevador_servico=request.form.get('elevadores'),
            piscina_coletiva=request.form.get('piscina_infantil'),
            interfone=request.form.get('interfone'),
            quadra_esportes=request.form.get('quadra_esportes'),
            jardim=request.form.get('jardim'),
            playground=request.form.get('playground'),
            academia=request.form.get('academia'),
            espaco_gourmet=request.form.get('espaco_gourmet'),
            lavanderia=request.form.get('lavanderia'),
            portaria24h=request.form.get('portaria24h'),
            salao_festas=request.form.get('salao_festas'),
            link_youtube=request.form.get('link_youtube')
        )

        return imovel


    @imoveis_routes.route('exibir/todos', methods=['GET'])
    def exibir_todos_imoveis():

        return model.exibir_todos_imoveis()


    @imoveis_routes.route('/editar', methods=['POST'])
    @login_requiered
    def editar_imovel():
        imovel = model.editar_imovel(
            usuario=session['usuario'],
            imovel_id=request.form.get('imovel_id')
        )

        return imovel


    @imoveis_routes.route('/excluir', methods=['POST'])
    @login_requiered
    def excluir_imovel(self):
        imovel = model.excluir_imovel(
            imovel_id=request.form.get('imovel_id'),
            usuario=session['usuario']
        )

        return imovel


    @imoveis_routes.route('/meus_imoveis', methods=['GET'])
    @login_requiered
    def meus_imoveis():
        imoveis = model.busca_personalizada(
            corretor_id=session['usuario']['_id']
        )

        return imoveis


    @imoveis_routes.route('/busca', methods=['GET'])
    def exibir_imovel():
        imoveis = model.busca_personalizada(
            tipo=request.args.get('tipo'),
            categoria=request.args.get('categoria'),
            bairro=request.args.get('bairro'),
            valor=request.args.get('valor'),
            quartos=request.args.get('quartos'),
            imovel_id=request.args.get('imovel_id'),
            corretor_id=request.args.get('corretor_id'),

        )

        return imoveis