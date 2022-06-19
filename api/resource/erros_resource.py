from flask import Blueprint, jsonify
from api.utils.exceptions import CommonError

errors_routes = Blueprint('errors_routes', __name__)


@errors_routes.app_errorhandler(CommonError)
def handle_validation_error(error):
    dict_errors = {
        '01': 'Erro generico',
        '02': 'Erro generico',
        '03': 'Erro generico',
        '04': 'Erro generico',
        '05': 'Erro generico',
        '06': 'Erro generico',
        '07': 'Erro generico'
    }

    return {
               "status": "error",
               "message": dict_errors.get(error.code_error)
           }, 422
