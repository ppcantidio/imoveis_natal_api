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
    def editar_usuario():
        headers = request.headers

<<<<<<< HEAD
    @users_routes.route('/editar', methods=['POST'])
    def edit_user():
        headers = request.headers

        token = headers['token']

        id_usuario = tk.decrypt_token(token)

        return jsonify({'id': id_usuario})

=======
        id = headers['token']
>>>>>>> 3392a8cff0861494b7d2f303bdbcfd9af0e601bb

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