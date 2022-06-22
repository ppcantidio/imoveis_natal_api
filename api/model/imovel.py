from email.policy import default
from marshmallow import Schema, validate
from marshmallow.fields import Str, Integer, Boolean, Nested, List


from api.model.endereco import Endereco
from api.utils.messages import MSG_FIELD_REQUIRED


class Extras(Schema):
    inPiscinaInfantil = Boolean(required=False, default=None)
    inInterfone = Boolean(required=False, default=None)
    inQuadraEsportes = Boolean(required=False, default=None)
    inAcademia = Boolean(required=False, default=None)
    inEspacoGourmet = Boolean(required=False, default=None)
    inPortaria24h = Boolean(required=False, default=None)
    inElevadorServico = Boolean(required=False, default=None)
    inElevadorSocial = Boolean(required=False, default=None)
    inSalaoFestas = Boolean(required=False, default=None)


class ImovelRequestPost(Schema):
    nmTitulo = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    nmDescricao = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    nmTipoImovel = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    nmCategoriaImovel = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    obEndereco = Nested(Endereco)
    qtdQuartos = Integer(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    qtdSuited = Integer(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    qtdBanheiros = Integer(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    qtdVagasGaragem = Integer(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    vlValorImovel = Integer(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    obExtras = List(Nested(Extras), required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    # lsImagens = List(required=True, default=None)
    nmVideoYoutube = Str(required=False, default=None)
    nmStatus = Str(required=False, default=None)
