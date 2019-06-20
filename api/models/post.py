from app import db
from .base import AuditableBaseModel


class Post(AuditableBaseModel):
    title = db.Column(db.String(180))
    description = db.Column(db.String(360))
    body = db.Column(db.Text)
    comments = db.relationship('Comment', backref='blog')

    def to_dict(self):
        fields = ('id', 'title', 'description', 'body', 'comments')
        return {field: getattr(self, field) for field in fields}

    def __repr__(self):
        return f'Post: {self.title}'
