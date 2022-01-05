from flask.views import MethodView
from flask import request, jsonify, Blueprint, session
from models.imoveis_models import Imoveis_Models
from utils.sessions_requirements import nao_logado, login_requiered

imoveis_routes = Blueprint('imoveis_routes', __name__)

model = Imoveis_Models()

class Imoveis(MethodView):


    @imoveis_routes.route('/', methods=['POST', 'GET'])
    def imovel():

        requisicao = request.method

        print(requisicao)

        if requisicao == 'POST':
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
                piscina_infantil=request.form.get('piscina_infantil'),
                interfone=request.form.get('interfone'),
                quadra_esportes=request.form.get('quadra_esportes'),
                jardim=request.form.get('jardim'),
                playground=request.form.get('playground'),
                academia=request.form.get('academia'),
                espaco_gourmet=request.form.get('espaco_gourmet'),
                lavanderia=request.form.get('lavanderia'),
                portaria24h=request.form.get('portaria24h'),
                salao_festas=request.form.get('salao_festas'),
                banheiros=request.form.get('banheiros'),
                link_youtube=request.form.get('link_youtube')
            )

            return imovel

        elif requisicao == 'GET':
            return model.exibir_todos_imoveis()


    @imoveis_routes.route('/<id>', methods=['PUT'])
    @login_requiered
    def editar_imovel(id):
        imovel = model.editar_imovel(
            imovel_id=id,
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
            piscina_infantil=request.form.get('piscina_infantil'),
            interfone=request.form.get('interfone'),
            quadra_esportes=request.form.get('quadra_esportes'),
            jardim=request.form.get('jardim'),
            playground=request.form.get('playground'),
            academia=request.form.get('academia'),
            espaco_gourmet=request.form.get('espaco_gourmet'),
            lavanderia=request.form.get('lavanderia'),
            portaria24h=request.form.get('portaria24h'),
            salao_festas=request.form.get('salao_festas'),
            banheiros=request.form.get('banheiros'),
            link_youtube=request.form.get('link_youtube')
        )

        return imovel


    @imoveis_routes.route('/<id>', methods=['DELETE'])
    @login_requiered
    def excluir_imovel(id):
        imovel = model.excluir_imovel(
            imovel_id=id,
            usuario=session['usuario']
        )

        return imovel


    @imoveis_routes.route('/meus_imoveis', methods=['GET'])
    @login_requiered
    def meus_imoveis():
        imoveis = model.meus_imoveis(
            corretor_id=session['usuario']['_id']
        )

        return imoveis


    @imoveis_routes.route('/busca', methods=['GET'])
    def busca():
        print('teste')
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