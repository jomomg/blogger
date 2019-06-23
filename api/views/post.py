from flask import request

from .. import api
from api.models import Post
from api.schemas.post import PostSchema
from .base import create, list_all, get_single_item


@api.route('/posts', methods=['POST'])
def add_blog_post():
    return create(Post, PostSchema, request)


@api.route('/posts', methods=['GET'])
def get_all_posts():
    return list_all(Post, PostSchema)


@api.route('/posts/<post_id>', methods=['GET'])
def get_single_post(post_id):
    return get_single_item(Post, PostSchema, post_id)
