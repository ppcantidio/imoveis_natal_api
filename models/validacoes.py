import re


class Validacoes:
    
    def validar_email(email):
        formato_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(formato_email, email):
            return False
        else:
            return email

    def validar_nome():
        pass

    def validar_cpf():
        pass

    def validar_creci():
        pass

    def validar_telefone(telefone):
        pass