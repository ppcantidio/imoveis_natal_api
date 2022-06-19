from marshmallow import Schema
from marshmallow.fields import Str, Integer, Boolean

from api.model.endereco import Endereco
from api.utils.messages import MSG_FIELD_REQUIRED


class UsuarioRequestPost(Schema):
    nmNomeCompleto = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    nmCpf = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    nmUsername = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    nmPassword = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
