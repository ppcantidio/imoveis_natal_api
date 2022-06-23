from flask import request
from flask_restx import Resource

from api.service.login_service import LoginService
from api.model.login import LoginRequestPost
from api.utils.responses import (resp_data_invalid, resp_ok)


class LoginResource(Resource):
    def post(self):
        """
        Autentica o usuario
        """

        req_data = request.get_json() or {}

        login_request, erros = LoginRequestPost().load(req_data)
        if erros:
            return resp_data_invalid('Login', erros, 'Dados de entrada inválidos.')

        retorno = LoginService().autentica_usuario(login_request)

        return resp_ok("Login", "Usuario autenticado com sucesso", data=retorno)
