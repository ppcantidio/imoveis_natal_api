from marshmallow import Schema
from marshmallow.fields import Str

from api.utils.messages import MSG_FIELD_REQUIRED


class LoginRequestPost(Schema):
    nmUsername = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    nmPassword = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
