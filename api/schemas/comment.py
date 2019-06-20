from marshmallow import fields

from .base import AuditableBaseSchema
from .post import PostSchema


class CommentSchema(AuditableBaseSchema):
    body = fields.String(required=True)
    post_id = fields.String(required=True, load_only=True)
    post = fields.Nested(PostSchema, only=['id', 'title'], dump_only=True)
