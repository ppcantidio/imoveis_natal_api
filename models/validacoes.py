import re
from utils.exceptions import CampoIncorreto

class Validacoes:
    
    def validar_email(self, email):
        if email  == None:
            raise CampoIncorreto('email')

        formato_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(formato_email, email):
            raise CampoIncorreto('email')


    def validar_nome(self, nome):
        if nome  == None:
            raise CampoIncorreto('nome')

        nome = nome.strip()

        if nome == '':
            raise CampoIncorreto('nome')


    def validar_telefone(self, telefone):
        if telefone  == None:
            raise CampoIncorreto('telefone')

        formato_telefone = re.compile(r'\d*')

        if not re.fullmatch(formato_telefone, telefone):
            raise CampoIncorreto('telefone')


    def validar_senha(self, senha):
        if senha  == None:
            raise CampoIncorreto('senha')

        senha = senha.strip()

        if senha == '':
            raise CampoIncorreto('senha')


    def string(self, string, valor, campo):
        if string == None:
            return None

        tamanho_string = len(string)

        if tamanho_string > valor or string.strip() == '':
            raise CampoIncorreto(campo)

        return string

    def int(self, integer, valor, campo):
        try:
            if integer == None:
                return None

            tamanho_integer = len(integer)

            integer = int(integer)

            if tamanho_integer > valor:
                raise CampoIncorreto(campo)

            return integer
        except:
            raise CampoIncorreto(campo)


    def booleano(self, booleano):
        if booleano == None:
            return None

        booleano = booleano.lower()
        booleano = booleano.capitalize()

        if booleano == 'True':
            return True
        else:
            return  False
        