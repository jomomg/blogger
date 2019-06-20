from marshmallow import fields

from .base import AuditableBaseSchema


class PostSchema(AuditableBaseSchema):
    title = fields.String(required=True)
    description = fields.String()
    body = fields.String()
