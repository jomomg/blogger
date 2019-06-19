from flask import Flask

from api import api_bp


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(api_bp)
    return app

