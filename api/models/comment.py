from app import db
from .base import AuditableBaseModel


class Comment(AuditableBaseModel):
    body = db.Column(db.String(1000))
    blog_id = db.Column(db.String(28), db.ForeignKey('post.id'))

    def __repr__(self):
        return f'Comment {self.body}'
