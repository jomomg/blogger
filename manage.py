import os

from flask import jsonify

from config import config
from app import create_app


flask_env = os.getenv('FLASK_ENV')
app = create_app(config=config[flask_env])


@app.route('/')
def ping():
    return jsonify({
        'status': 'success',
        'message': 'I am running'
    }), 200


if __name__ == "__main__":
    app.run()
