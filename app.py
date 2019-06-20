from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from api import api as api_bp

db = SQLAlchemy()
migrate = Migrate()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    import api.models
    import api.views

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_bp)
    return app
