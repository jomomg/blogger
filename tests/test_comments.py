import json

from api.models import Post, Comment


class TestComments:
    post_data = {
        'title': 'a random title',
        'description': 'a random description',
        'body': 'a random body'
    }

    def creating_comment_succeeds(self, client, init_db):
        post_id = Post(**self.post_data).save().id
        comment_data = {
            'body': 'this is a test comment',
            'post_id': post_id
        }
        res = client.post('/api/comments', data=json.dumps(comment_data))
        assert res.status_code == 201
        payload = json.loads(res.data)
        assert payload['data']['body'] == comment_data['body']
        assert payload['data']['post']['id'] == post_id

    def getting_all_comments_succeeds(self, client, init_db):
        post_id = Post(**self.post_data).save().id
        comment_data = {'body': 'test_comment', 'post_id': post_id}
        # save three comments
        for i in range(3):
            Comment(**comment_data).save()
        res = client.get('/api/comments')
        assert res.status_code == 200
        payload = json.loads(res.data)
        assert len(payload['data']) == 3

    def test_getting_single_comment_succeeds(self, client, init_db):
        post_id = Post(**self.post_data).save().id
        comment_data = {'body': 'test_comment', 'post_id': post_id}
        comment_id = Comment(**comment_data).save().id
        res = client.get(f'/api/comments/{comment_id}')
        assert res.status_code == 200

    def test_getting_nonexistent_comment_returns_404(self, client, init_db):
        comment_id = 'does_not_exist'
        res = client.get(f'/api/comments/{comment_id}')
        assert res.status_code == 404
