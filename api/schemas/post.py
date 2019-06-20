from marshmallow import fields

from .base import AuditableBaseSchema
from api.utils.validators import validate_empty_string


class PostSchema(AuditableBaseSchema):
    title = fields.String(required=True, validate=validate_empty_string)
    description = fields.String()
    body = fields.String()
