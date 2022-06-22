from api.utils.database import Database as DB
from api.utils.exceptions import CommonError
from api.mapper.usuario_mapper import UsuarioMapper


class UsuarioService:
    def registra_usuario(self, usuario_request: dict):
        # usuario_object = UsuarioMapper().registrar_usuario_mapper(usuario_request)
        usuario_object = usuario_request
        if DB().select_one_object('usuarios', {'nmApelido': usuario_object.get('nmApelido')}) is not None:
            raise CommonError(2)

        usuario_object = DB().insert_object(usuario_object, 'usuarios')
        return usuario_object
