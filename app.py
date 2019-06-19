from flask import Flask, Blueprint, jsonify


app_bp = Blueprint('app', __name__)


@app_bp.route('/')
def ping():
    return jsonify({
        'status': 'success',
        'message': 'I am running'
    }), 200


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(app_bp)
    return app

