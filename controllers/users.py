from flask.views import MethodView
from models.users_models import User_Models
from flask import request, jsonify, Blueprint, session
from utils.sessions_requirements import nao_logado, login_requiered

users_routes = Blueprint('users_routes', __name__)

model = User_Models()

class User(MethodView):

    @users_routes.route('/', methods=['POST', 'GET'])
    def usuarios():
        requisicao = request.method

        if requisicao == 'POST':
            user = model.criar_usuario(
                #usuario_requisitor=session['usuario'],
                nome=request.form.get('nome'),
                senha = request.form.get('senha'),
                email=request.form.get('email'),
                telefone=request.form.get('telefone')
            )

            return user

        elif requisicao == 'GET':
            return model.exbir_usuarios()
        

    # lembrar de editar essa funcao nos models
    # verificar se o usuario que esta solicitando a edicao eh o dono da conta
    @users_routes.route('/<id>', methods=['PUT'])
    @login_requiered
    def editar_usuario(id):       
        user = model.editar_usuario(
            usuario_requisitor=id,
            nome =request.form.get('nome'),
            email=request.form.get('email'),
            telefone=request.form.get('telefone')
        )

        return user


    @users_routes.route('/<id>', methods=['DELETE'])
    @login_requiered
    def deletar_usuario(id):
        resultado = model.deletar_usuario(
            usuario_requisitor=session['usuario'],
            id_requisitado=id
        )

        return resultado


    @users_routes.route('/inativar', methods=['PUT'])
    @login_requiered
    def inativar_usuario():

        usuario = model.inativar_usuario(
            usuario=session['usuario'],
            id_requisitado=request.form.get('id_requisitado')
        )

        return usuario

    
    @users_routes.route('/ativar', methods=['PUT'])
    @login_requiered
    def ativar_usuario():
        usuario = model.ativar_usuario(
            usuario_requisitor=session['usuario'],
            id_requisitado=request.form.get('id_requisitado')
        )

        return usuario


    @users_routes.route('/permissoes/', methods=['PUT'])
    @login_requiered
    def editar_permissoes():
        user = model.editar_permissoes(
            usuario_requisitor=session['usuario'],
            id_requisitado=request.form.get('id_requisitado'),
            criar_usuarios=request.form.get('criar_usuarios'),
            excluir_usuarios=request.form.get('excluir_usuarios'),
            excluir_imoveis=request.form.get('excluir_imoveis'),
            editar_imoveis=request.form.get('editar_imoveis'),
            inativar_imoveis=request.form.get('inativar_imoveis'),
            ativar_imoveis=request.form.get('ativar_imoveis'),
            editar_permissoes=request.form.get('editar_permissoes'),
            inativar_usuarios=request.form.get('inativar_usuarios'),
            ativar_usuarios=request.form.get('ativar_usuarios'),
        )

        return user

    
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


    @users_routes.route('/perfil', methods=['GET'])
    @login_requiered
    def exibir_perfil():
        print(session)
        usuario = model.exibir_usuario(
            usuario_id=session['usuario']['_id']
        )

        return usuario

    
    @users_routes.route('/trocar_senha', methods=['PUT'])
    @login_requiered
    def trocar_senha():
        usuario = model.trocar_senha(
            usuario_requisitor=session['usuario'],
            senha_atual=request.form.get('senha_atual'),
            senha_nova=request.form.get('senha_nova'),
            senha_repetida=request.form.get('senha_repetida')
        )

        return usuario
        

    @users_routes.route('/info/<id>')
    def infos_publicas(id):
        usuario = model.infos_publicas(corretor_id=id)

        return usuario