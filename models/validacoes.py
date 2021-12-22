import re


class Validacoes:
    
    def validar_email(self, email):
        formato_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(formato_email, email):
            return False
        else:
            return email


    def validar_nome(self, nome):
        nome = nome.strip()

        if nome == '':
            return False
        else:
            return nome



    def validar_cpf():
        pass

    def validar_creci():
        pass

    def validar_telefone(self, telefone):
        formato_telefone = re.compile(r'\d*')

        if not re.fullmatch(formato_telefone, telefone):
            return False
        else:
            return telefone
