from flask.views import MethodView
from models.users_models import User_Models
from flask import request, jsonify, Blueprint, session
from functools import wraps

users_routes = Blueprint('users_routes', __name__)

model = User_Models()

def login_requiered(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return jsonify({
                'status':'erro',
                'menssagem': 'faca o login primeiro',
                'codigo-requisicao': 'in300'
                })

    return wrap


def nao_logado(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return jsonify({
                'status':'erro',
                'menssagem': 'voce ja esta logado',
                'codigo-requisicao': 'in300'
                })

    return wrap

class User(MethodView):

    @users_routes.route('/criar', methods=['POST'])
    @login_requiered
    def criar_usuarios():
        user = model.criar_usuario(
            usuario=session['usuario'],
            nome=request.form.get('nome'),
            senha = request.form.get('senha'),
            email=request.form.get('email'),
            telefone=request.form.get('telefone')
        )

        return user
        

    # lembrar de editar essa funcao nos models
    @users_routes.route('/editar', methods=['POST'])
    @login_requiered
    def editar_usuario():       
        user = model.editar_usuario(
            usuario=session['usuario'],
            nome =request.form.get('nome'),
            email=request.form.get('email'),
            telefone=request.form.get('telefone')
        )

        return user


    @users_routes.route('/deletar', methods=['POST'])
    @login_requiered
    def deletar_usuario():
        resultado = model.deletar_usuario(
            usuario=session['usuario'],
            email_usuario=request.form.get('email_usuario')
        )

        return resultado


    @users_routes.route('/inativar', methods=['POST'])
    @login_requiered
    def inativar_usuario():

        usuario = model.inativar_usuario(
            usuario=session['usuario'],
            email_usuario=request.form.get('email_usuario')
        )

        return usuario

    
    @users_routes.route('/ativar', methods=['POST'])
    def ativar_usuario():
        usuario = model.ativar_usuario(
            usuario_requisitor=session['usuario'],
            id_requisitado=request.form.get('id_requisitado')
        )

        return usuario


    @users_routes.route('/permissoes', methods=['POST'])
    @login_requiered
    def editar_permissoes():
        user = model.editar_permissoes(
            usuario_requisitor=session['usuario'],
            id_requisitado=request.form.get('id_requisitado'),
            criar_usuarios=request.form.get('criar_usuarios'),
            excluir_usuarios=request.form.get('excluir_usuarios'),
            aprovar_imoveis=request.form.get('aprovar_imoveis'),
            excluir_imoveis=request.form.get('excluir_imoveis'),
            editar_imoveis=request.form.get('editar_imoveis'),
            ocultar_imoveis=request.form.get('ocultar_imoveis')
        )

        return user

    @users_routes.route('/todos', methods=['GET'])
    @login_requiered
    def  exibir_usuarios():

        return model.exbir_usuarios()

    
    @users_routes.route('/sair', methods=['GET'])
    def sair():
        return model.signout()


    @users_routes.route('/login', methods=['POST'])
    @nao_logado
    def login():
        email = request.form.get('email')
        senha = request.form.get('senha')

        login = model.login(
            email=email,
            senha=senha
        )

        return login