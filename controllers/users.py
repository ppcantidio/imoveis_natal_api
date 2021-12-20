from flask.views import MethodView
from flask import request, jsonify, Blueprint
from models.users import User_Models
from acessos_token import Token

users_routes = Blueprint('users_routes', __name__)

model = User_Models()

tk = Token()

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
    def edit_user():
        headers = request.headers

        token = headers['token']

        id_usuario = tk.decrypt_token(token)

        nome  = request.form.get('nome')
        #senha = request.form('senha')
        email = request.form.get('email')
        telefone = request.form.get('telefone')

        user = model.editar_usuario(
            id=id_usuario,
            nome=nome,
            email=email,
            telefone=telefone
        )

        return user
        

    def deletar_usuario():
        pass