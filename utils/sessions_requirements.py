from flask import jsonify, session
from functools import wraps

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