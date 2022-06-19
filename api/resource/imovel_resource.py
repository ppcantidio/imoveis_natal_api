from flask_restplus import Resource
from flask import request

from api.model.imovel import ImovelRequestPost
from api.service.imovel_service import ImovelService

from api.utils.responses import (resp_ok, resp_error, resp_data_invalid)


class ImovelResource(Resource):
    def post(self, nm_id_usuario):
        """
        Insere imovel na base de dados
        """

        req_data = request.get_json() or None

        imovel_request, erros = ImovelRequestPost().load(req_data)
        if erros:
            return resp_data_invalid('Imovel', erros, 'Dados de entrada inválidos.')

        retorno = ImovelService().insere_imovel(imovel_request, nm_id_usuario)

        return resp_ok("Imovel", "Imovel inserido com sucesso", data=retorno)
