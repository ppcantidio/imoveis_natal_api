import jwt
from datetime import datetime, timedelta
from dynaconf import settings

from flask import jsonify

from api.utils.exceptions import CommonError
from api.utils.database import Database as DB
from api.utils.auth_util import decrypt_password
from werkzeug.security import check_password_hash



class LoginService:
    def autentica_usuario(self, login_request):
        username = login_request.get('nmUsername')
        password = login_request.get('nmPassword')

        usuario_object = DB().select_one_object('usuarios', {'nmUsername': username})
        if usuario_object is None:
            raise CommonError(4)

        if check_password_hash(usuario_object['nmPassword'], password) == False:
            raise CommonError(5)
        
        token = jwt.encode({'username': username, 'exp': datetime.now() + timedelta(hours=12) },
                           settings.get('SECRET_KEY'))

        return {'token': token, 'exp': datetime.now() + timedelta(hours=12)}