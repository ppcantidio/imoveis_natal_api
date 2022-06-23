from flask import Blueprint, jsonify
from api.utils.exceptions import CommonError

errors_routes = Blueprint('errors_routes', __name__)


@errors_routes.app_errorhandler(CommonError)
def handle_validation_error(CommonErrorObject):
    dict_errors = {
        '1': 'Erro generico',
        '2': 'Erro generico',
        '3': 'Erro generico',
        '4': 'Erro generico',
        '5': 'Erro generico',
        '6': 'Erro generico',
        '7': 'Erro generico'
    }

    return jsonify({
               "status": "erro",
               "menssagem": dict_errors.get(str(CommonErrorObject.code_error))
           })
