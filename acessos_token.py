from des import DesKey
import base64
import os

class Token:

    @staticmethod
    def decrypt_token(token_usuario):
        try:
            key = DesKey(os.environ.get('DES_KEY').encode('ascii'))
                
            byte_token = base64.b64decode(token_usuario)

            id_usuario = key.decrypt(byte_token)

            return id_usuario.decode('ascii')
        except UnicodeDecodeError as e:
            return True
        except Exception as e:
            return True

    @staticmethod
    def encrypt_token(id_usuario):
        id_usuario = id_usuario.encode('ascii')

        key = DesKey(os.environ.get('DES_KEY').encode('ascii'))

        token = key.encrypt(id_usuario)

        token = base64.b64encode(token)

        return token.decode('ISO-8859-1')

        