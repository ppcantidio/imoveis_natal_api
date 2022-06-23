from werkzeug.security import generate_password_hash
from datetime import datetime


class UsuarioMapper:
    def registrar_usuario_mapper(self, usuario_mapper: dict):
        password_hash = generate_password_hash(usuario_mapper['nmPassword'])
        usuario_mapper['nmPassword'] = password_hash
        usuario_mapper['dtDataCriacao'] = datetime.now()

        return usuario_mapper