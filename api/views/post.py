import json

from flask import request, jsonify

from .. import api
from api.models import Post
from api.utils.response import success_


@api.route('/posts', methods=['POST'])
def add_blog_post():
    post_data = json.loads(request.data)
    post = Post(**post_data)
    post.save()
    return jsonify(success_('post created', data=post.to_dict())), 201
