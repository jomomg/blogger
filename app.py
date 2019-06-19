from flask import Flask


def register_blueprints():
    pass


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints()
    return app

