from marshmallow import Schema
from marshmallow.fields import Str

from api.utils.messages import MSG_FIELD_REQUIRED


class LoginRequestPost(Schema):
    username = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    passowrd = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
