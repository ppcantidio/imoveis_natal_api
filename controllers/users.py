from flask.views import MethodView
from flask import request, jsonify, Blueprint
from models.users_models import User_Models
from acessos_token import Token

users_routes = Blueprint('users_routes', __name__)

model = User_Models()

class User(MethodView):


    @users_routes.route('/criar', methods=['POST'])
    def criar_usuarios():
        headers = request.headers

        user = model.criar_usuario(
            token=headers['token'],
            nome=request.form.get('nome'),
            #senha = request.form('senha'),
            email=request.form.get('email'),
            telefone=request.form.get('telefone')
        )

        return user
        

    @users_routes.route('/editar', methods=['POST'])
    def editar_usuario():
        headers = request.headers
        
        user = model.editar_usuario(
            
            token=headers['token'],
            nome =request.form.get('nome'),
            #senha = request.form('senha'),
            email=request.form.get('email'),
            telefone=request.form.get('telefone')
        )

        return user


    @users_routes.route('/deletar', methods=['POST'])
    def deletar_usuario():
        headers = request.headers

        resultado = model.deletar_usuario(
            token=headers['token'],
            email_usuario=request.form.get('email_usuario')
        )

        return resultado


    @users_routes.route('/inativar', methods=['POST'])
    def inativar_usuario():
        pass


    @users_routes.route('/permissoes', methods=['POST'])
    def editar_permissoes():
        headers = request.headers

        user = model.editar_permissoes(
            token=headers['token'],
            email_usuario=request.form.get('email'),
            criar_usuarios=request.form.get('criar_usuarios'),
            excluir_usuarios=request.form.get('excluir_usuarios'),
            aprovar_imoveis=request.form.get('aprovar_imoveis'),
            excluir_imoveis=request.form.get('excluir_imoveis'),
            editar_imoveis=request.form.get('editar_imoveis'),
            ocultar_imoveis=request.form.get('ocultar_imoveis')
        )

        return user


    @users_routes.route('/usuarios', methods=['GET'])
    def  exibir_usuarios():
        headers = request.headers

        usuarios = model.exbir_usuarios(
            token=headers['token']
        )

        return usuarios
