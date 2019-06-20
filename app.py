from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from api import api as api_bp
from api.utils.error_handler import ValidationError

db = SQLAlchemy()
migrate = Migrate()


@api_bp.errorhandler(ValidationError)
def handle_validation_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    import api.models
    import api.views

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_bp)
    return app
