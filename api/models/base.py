import datetime as dt
from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(28), primary_key=True)


class AuditableBaseModel(BaseModel):
    __abstract__ = True

    created_at = db.Column(db.Datetime, default=dt.datetime.utcnow)
    updated_at = db.Column(db.Datetime, onupdate=dt.datetime.utcnow)
