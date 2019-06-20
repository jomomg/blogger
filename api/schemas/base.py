from marshmallow import Schema, fields

from api.utils.error_handler import ValidationError


class BaseSchema(Schema):
    id = fields.String(dump_only=True)

    def load_json(self, data):
        result, errors = self.loads(data)
        if errors:
            raise ValidationError('an error occurred', data=errors)
        else:
            return result

    def load_object(self, data, partial=False):
        result, errors = self.load(data, partial=partial)
        if errors:
            raise ValidationError('an error occurred', data=errors)
        else:
            return result


class AuditableBaseSchema(BaseSchema):
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
