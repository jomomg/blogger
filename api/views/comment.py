from flask import request

from .. import api
from api.models import Comment
from api.schemas.comment import CommentSchema
from .base import create, list_all, get_single_item


@api.route('/comments', methods=['POST'])
def add_comment():
    return create(Comment, CommentSchema, request)


@api.route('/comments', methods=['GET'])
def get_all_comments():
    return list_all(Comment, CommentSchema)


@api.route('/comments/<comment_id>', methods=['GET'])
def get_single_comment(comment_id):
    return get_single_item(Comment, CommentSchema, comment_id)
