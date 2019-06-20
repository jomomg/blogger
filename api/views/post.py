import json

from flask import request, jsonify

from .. import api
from api.models import Post
from api.utils.response import success_
from api.schemas.post import PostSchema


@api.route('/posts', methods=['POST'])
def add_blog_post():
    schema = PostSchema()
    post_data = schema.load_json(request.data)
    post = Post(**post_data)
    post.save()
    payload = schema.dump(post).data
    return jsonify(success_('post created', data=payload)), 201


@api.route('/posts', methods=['GET'])
def get_all_posts():
    schema = PostSchema(many=True)
    posts = Post.query.all()
    payload = schema.dump(posts).data
    return jsonify(success_('posts fetched', data=payload)), 200
