from marshmallow import Schema, fields


class BaseSchema(Schema):
    id = fields.String(dump_only=True)


class AuditableBaseSchema(BaseSchema):
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
