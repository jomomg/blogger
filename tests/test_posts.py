import json

from api.models import Post

POST_DATA = {
    'title': 'a random title',
    'description': 'a random description',
    'body': 'a random body'
}


class TestPosts:
    def test_adding_a_post_succeeds(self, client, init_db):
        res = client.post('/api/posts', data=json.dumps(POST_DATA))
        assert res.status_code == 201
        res_data = json.loads(res.data)
        assert res_data['status'] == 'success'
        assert res_data['message'] == 'post created'
        assert res_data['data']['id']
        assert res_data['data']['title'] == POST_DATA['title']

    def test_getting_all_blog_posts_succeeds(self, client, init_db):
        for i in range(2):
            client.post('/api/posts', data=json.dumps(POST_DATA))
        res = client.get('/api/posts')
        assert res.status_code == 200
        assert len(json.loads(res.data)['data']) == 2

    def test_omitting_required_field_raises_error(self, client):
        res = client.post('/api/posts', data=json.dumps({}))
        assert res.status_code == 400
        assert json.loads(res.data)['status'] == 'error'

    def test_blank_fields_not_allowed(self, client):
        res = client.post('/api/posts', data=json.dumps({'title': ''}))
        assert res.status_code == 400
        assert json.loads(res.data)['status'] == 'error'

    def test_getting_a_single_post_succeeds(self, client, init_db):
        post_id = Post(**POST_DATA).save().id
        res = client.get(f'/api/posts/{post_id}')
        assert res.status_code == 200
        assert json.loads(res.data)['data']['id'] == post_id

    def test_getting_a_nonexistent_post_returns_404(self, client, init_db):
        post_id = 'nonexistent'
        res = client.get(f'/api/posts/{post_id}')
        assert res.status_code == 404
