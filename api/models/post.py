from app import db
from .base import AuditableBaseModel


class Post(AuditableBaseModel):
    title = db.Column(db.String(180))
    description = db.Column(db.String(360))
    body = db.Column(db.Text)
    comments = db.relationship('Comment', backref='blog')

    def __repr__(self):
        return f'Post: {self.title}'
