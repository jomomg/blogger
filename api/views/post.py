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
    data = schema.dump(post).data
    return jsonify(success_('post created', data=data)), 201
