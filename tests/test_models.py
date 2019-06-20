import datetime as dt

from api.models import Post, Comment

POST_DATA = {
    'title': 'a random title',
    'description': 'a random description',
    'body': 'a random body'
}


class TestModels:
    @staticmethod
    def save_object(model, data):
        instance = model(**data)
        instance.save()
        return instance

    def assert_saving_object_works(self, model, obj_data):
        saved = self.save_object(model, obj_data)
        assert len(model.query.all()) == 1
        assert saved.id
        assert saved.created_at
        assert isinstance(saved.created_at, dt.datetime)

    def test_saving_blog_works(self, init_db):
        self.assert_saving_object_works(Post, POST_DATA)

    def test_saving_comment_works(self, init_db):
        blog = self.save_object(Post, POST_DATA)
        comment_data = {'body': 'this is my body', 'post_id': blog.id}
        self.assert_saving_object_works(Comment, comment_data)
