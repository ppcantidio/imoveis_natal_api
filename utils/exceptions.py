class UsuarioNaoEncontrado(Exception):
    pass

class PermissaoInvalida(Exception):
    pass

class CampoIncorreto(Exception):
    def __init__(self, campo):
        self.campo = campo

class ImovelNaoEncontrado(Exception):
    pass

class ErroGenerico(Exception):
    def __init__(self, menssagem):
        self.menssagem = menssagem

class SenhaIncorreta(Exception):
    pass