import os

import pytest

from app import create_app
from config import config

FLASK_ENV = 'testing'
os.environ['FLASK_ENV'] = FLASK_ENV


@pytest.fixture(scope='session')
def app():
    app = create_app(config=config[FLASK_ENV])
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    yield app.test_client()
