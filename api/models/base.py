import datetime as dt
from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(28), primary_key=True)


class AuditableBaseModel(BaseModel):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=dt.datetime.utcnow)
