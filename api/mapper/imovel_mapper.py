class ImovelMapper:
    def insere_imovel_mapper(self, imovel_request: dict, nm_id_usuario: str):
        imovel_request['nmIdUsuario'] = nm_id_usuario
        return imovel_request
