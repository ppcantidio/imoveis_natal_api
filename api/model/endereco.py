from marshmallow import Schema
from marshmallow.fields import Str

from api.utils.messages import MSG_FIELD_REQUIRED


class Endereco(Schema):
    nmLogradouro = Str()
    nmNumero = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    nmComplemento = Str()
    nmBairro = Str()
    nmMunicipio = Str()
    nmUf = Str()
    nmPais = Str()
    nmCep = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
