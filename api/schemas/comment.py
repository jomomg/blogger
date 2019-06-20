from marshmallow import fields

from .base import AuditableBaseSchema
from .post import PostSchema


class CommentSchema(AuditableBaseSchema):
    body = fields.String()
    post = fields.Nested(PostSchema, only=('id', 'title'))
