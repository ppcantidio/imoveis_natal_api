from marshmallow import Schema, validate
from marshmallow.fields import Str, Integer, Boolean, Nested, List


from api.model.endereco import Endereco
from api.utils.messages import MSG_FIELD_REQUIRED


class Extras(Schema):
    inPiscinaInfantil = Boolean()
    inInterfone = Boolean()
    inQuadraEsportes = Boolean()
    inAcademia = Boolean()
    inEspacoGourmet = Boolean()
    inPortaria24h = Boolean()
    inElevadorServico = Boolean()
    inElevadorSocial = Boolean()
    inSalaoFestas = Boolean()


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
    lsImagens = List()
    nmVideoYoutube = Str()
    nmStatus = Str()
