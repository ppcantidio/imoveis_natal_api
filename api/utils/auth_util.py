import json
import python_jwt as jwt
from datetime import datetime, timedelta
from flask import request, jsonify
from api.utils.exceptions import CommonError
from dynaconf import settings

def encrypt_password(password):
    pass


def decrypt_password(password):
    pass

def validate_token(token):
    try:
        pass
    except:
        pass


def token_requied():
    def wrapper(*args, **kwargs):
        token = request.header.get('token')
        if not token:
            raise CommonError(5)

        try:
            data = jwt.decode(token, settings.get('SECRET_KEY'))
            current_user = 'deu certo'
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        return current_user

    return wrapper