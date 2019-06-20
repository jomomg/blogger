import json

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
