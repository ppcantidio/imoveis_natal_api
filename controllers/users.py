from flask.views import MethodView
from flask import request, jsonify, Blueprint
from models.users import User_Models

users_routes = Blueprint('users_routes', __name__)

model = User_Models()

class User(MethodView):


    @users_routes.route('/criar', methods=['POST'])
    def criar_usuarios():
        nome  = request.form.get('nome')
        #senha = request.form('senha')
        email = request.form.get('email')
        telefone = request.form.get('telefone')

        user = model.criar_usuario(
            nome=nome,
            #senha=senha,
            email=email,
            telefone=telefone,
        )

        return user
        
    @users_routes.route('/editar', methods=['POST'])
    def editar_usuario():
        headers = request.headers

        id = headers['token']

        nome  = request.form.get('nome')
        #senha = request.form('senha')
        email = request.form.get('email')
        telefone = request.form.get('telefone')

        user = model.editar_usuario(
            nome=nome,
            email=email,
            telefone=telefone
        )

        return user
        

    def deletar_usuario():
        pass