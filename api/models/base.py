import uuid
import base64
import datetime as dt

from app import db
from api.utils.error_handler import ValidationError


def generate_key():
    """Generate a url-safe uuid to use a database primary key"""

    _uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return _uuid.decode().replace('=', '')


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(28), default=generate_key, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_or_404(cls, pk):
        record = cls.query.get(pk)
        if not record:
            raise ValidationError(f'{cls.__name__.lower()} not found', status_code=404)
        return record


class AuditableBaseModel(BaseModel):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=dt.datetime.utcnow)
