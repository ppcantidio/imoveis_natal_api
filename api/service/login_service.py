import jwt
from datetime import datetime
from dynaconf import settings

from flask import jsonify

from api.utils.exceptions import CommonError
from api.utils.database import Database as DB
from api.utils.auth_util import decrypt_password



class LoginService:
    def autentica_usuario(self, login_request):
        username = login_request.get('nmUsername')
        password = login_request.get('nmPassowrd')

        usuario_object = DB().select_one_object('usuarios', {'nmUsername': username})
        if usuario_object is None:
            raise CommonError(4)

        if password != decrypt_password(usuario_object.get('nmPassword')):
            raise CommonError(5)
        
        token = jwt.encode({'username': username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) },
                           settings.get('SECRET_KEY'))

        return {'token': token.decode('UTF-8'),'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}