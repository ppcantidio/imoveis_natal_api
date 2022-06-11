import logging

from api.utils.database import DB
from api.utils.exceptions import CommonError
from api.utils.funcoes_util import retorna_mongodb_object

from api.mapper.imovel_mapper import ImovelMapper


class ImovelService:
    """
    Classe que trata requisicoes para Imovel
    """
    def insere_imovel(self, imovel_request, nm_id_usuario):
        logging.info('Inserindo imovel na base')
        usuario = DB().select_one_object('usuarios', {'_id': Object(nm_id_usuario)})
        if usuario is None:
            raise CommonError(1)
        
        imovel_object = ImovelMapper().insere_imovel_mapper(imovel_request)
        imovel_object = DB().insert_object(imovel_object, 'imoveis')

        retorno = retorna_mongodb_object(imovel_object)

        return retorno

        