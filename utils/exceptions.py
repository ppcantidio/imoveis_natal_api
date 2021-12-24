class UsuarioNaoEncontrado(Exception):
    pass

class PermissaoInvalida(Exception):
    pass

class CampoIncorreto(Exception):
    def __init__(self, campo):
        self.campo = campo

class ImovelNaoEncontrado(Exception):
    pass
