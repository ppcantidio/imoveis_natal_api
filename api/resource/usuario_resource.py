from flask import request
from flask_restplus import Resource

from api.model.usuario import UsuarioRequestPost
from api.service.usuario_service import UsuarioService

from api.utils.responses import resp_data_invalid, resp_ok


class UsuarioResource(Resource):
    def post(self):
        """
       Registra usuario na base de dados
       """
        req_data = request.json_get()

        usuario_request, erros = UsuarioRequestPost.load(req_data)
        if erros:
            return resp_data_invalid('Usuario', erros, 'Dados de entrada inválidos.')

        retorno = UsuarioService().registra_usuario(usuario_request)

        return resp_ok('Usuario', 'Usuario criado com sucesso', data=retorno)



